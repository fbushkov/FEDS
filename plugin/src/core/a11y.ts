// Проверка доступности описаний сборки до записи в Figma (docs/build-rules.md, раздел 5):
// контраст текста ≥ 4.5 и иконок ≥ 3 на фоне варианта, в light и dark; иконка рядом с текстом — того же цвета.
import { blend, contrastRatio } from './contrast';
import { expandSet, matches, type RNode, type SetDef, type Variant } from './build';
import type { RGBA } from './types';

export type Mode = 'light' | 'dark';
/** Разрешает имя переменной (L3 или L2) в цвет для режима темы. */
export type ColorResolver = (name: string, mode: Mode) => RGBA | null;

export interface A11yIssue {
  kind: 'contrast' | 'pair' | 'unresolved';
  set: string; variant: string; node: string; token: string; mode: Mode;
  ratio?: number; need?: number; detail?: string;
}

export const MIN_TEXT = 4.5;
export const MIN_ICON = 3;
/** Состояния, которые WCAG не требует читать (1.4.3: неактивные элементы). */
const EXEMPT_STATES = new Set(['Disabled']);

/** Поверхности, на которых стоит вариант: из данных набора (a11y.surfaces) или по инверсии. */
export function surfacesOf(values: Record<string, string>, set?: SetDef): string[] {
  const s = set?.a11y?.surfaces;
  const own = s ? s.map[values[s.axis]] : undefined;
  if (own?.length) return own;
  return [isInverse(values) ? 'color/bg/section/inverse-main' : 'color/bg/section/main'];
}

export function isInverse(values: Record<string, string>): boolean {
  return values.Inverse === 'True' || Object.values(values).some((v) => /^Inverse/.test(v));
}

function close(a: RGBA, b: RGBA): boolean {
  const d = Math.max(Math.abs(a.r - b.r), Math.abs(a.g - b.g), Math.abs(a.b - b.b));
  return d < 0.02 && Math.abs((a.a ?? 1) - (b.a ?? 1)) <= 0.06;
}

/** Набор по имени — для проверки вложенных экземпляров (кнопки в Alert проверяются на его подложке). */
export type SetLookup = (name: string) => SetDef | undefined;

export function checkSet(set: SetDef, resolve: ColorResolver, lookup?: SetLookup): A11yIssue[] {
  const out: A11yIssue[] = [];
  const nestedCache = new Map<string, Variant[]>();
  const nestedVariant = (name: string, variant: Record<string, string>): Variant | undefined => {
    const def = lookup?.(name);
    if (!def) return undefined;
    if (!nestedCache.has(name)) nestedCache.set(name, expandSet(def));
    return nestedCache.get(name)!.find((x) => matches(x.values, variant));
  };
  for (const v of expandSet(set)) {
    if (Object.values(v.values).some((x) => EXEMPT_STATES.has(x))) continue;
    if (set.a11y?.exempt && matches(v.values, set.a11y.exempt)) continue;
    for (const outer of ['light', 'dark'] as Mode[]) {
     for (const baseName of surfacesOf(v.values, set)) {
      const base = resolve(baseName, outer);
      if (!base) continue;
      const get = (token: unknown, node: string, mode: Mode): RGBA | null => {
        if (typeof token !== 'string') return null;
        const c = resolve(token, mode);
        if (!c) out.push({ kind: 'unresolved', set: set.name, variant: v.name, mode, node, token });
        return c;
      };
      // mode — действующая тема узла: закреплённая (theme) или унаследованная; path — путь для вложенных экземпляров
      const walk = (n: RNode, bg: RGBA, inherited: Mode, path: string) => {
        // скрытые по умолчанию части (звёздочка, доп. текст) проверяются: их включают свойством
        if (n.opacity === 0) return;
        const mode = n.theme ?? inherited;
        const at = { set: set.name, variant: v.name, mode };
        const label = path ? `${path} › ${n.name}` : n.name;
        let here = bg;
        if ((n.type === 'frame' || n.type === 'rect') && n.fill !== undefined) {
          const f = get(n.fill, label, mode);
          if (f) here = blend(f, bg);
        }
        if (n.type === 'text' && n.text?.fill !== undefined) {
          const c = get(n.text.fill, label, mode);
          if (c) {
            const ratio = contrastRatio(blend(c, here), here);
            if (ratio < MIN_TEXT) out.push({ kind: 'contrast', ...at, node: label, token: String(n.text.fill), ratio, need: MIN_TEXT });
          }
        }
        if (n.type === 'icon' && n.icon?.color !== undefined) {
          const c = get(n.icon.color, label, mode);
          if (c) {
            const ratio = contrastRatio(blend(c, here), here);
            if (ratio < MIN_ICON) out.push({ kind: 'contrast', ...at, node: label, token: String(n.icon.color), ratio, need: MIN_ICON });
          }
        }
        // вложенный экземпляр (кнопка в Alert): его слои проверяются на подложке хозяина в действующей теме
        if (n.type === 'instance' && n.instance) {
          const nv = nestedVariant(n.instance.set, n.instance.variant);
          if (nv && !Object.values(nv.values).some((x) => EXEMPT_STATES.has(x))) walk(nv.root, here, mode, label);
          return;
        }
        // иконка и текст в одной группе — один цвет в каждом состоянии
        const text = n.children.find((c) => c.type === 'text' && c.text?.fill !== undefined && c.opacity !== 0);
        if (text) {
          const tc = get(text.text!.fill, text.name, mode);
          for (const ic of n.children.filter((c) => c.type === 'icon' && c.icon?.color !== undefined && c.opacity !== 0)) {
            const icc = get(ic.icon!.color, ic.name, mode);
            if (tc && icc && !close(tc, icc)) {
              out.push({ kind: 'pair', ...at, node: ic.name, token: String(ic.icon!.color), detail: `текст ${text.text!.fill}` });
            }
          }
        }
        for (const c of n.children) walk(c, here, mode, path);
      };
      walk(v.root, base, outer, '');
     }
    }
  }
  return out;
}

export function describeIssue(i: A11yIssue): string {
  const where = `${i.set} · ${i.variant} · ${i.node} (${i.mode})`;
  if (i.kind === 'contrast') return `${where}: ${i.token} — контраст ${i.ratio!.toFixed(2)}, нужно ≥ ${i.need}`;
  if (i.kind === 'pair') return `${where}: иконка ${i.token} не совпадает по цвету с ${i.detail}`;
  return `${where}: нет значения ${i.token}`;
}
