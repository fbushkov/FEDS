// Ядро сборки компонента (F7) и спецификации (F6): развёртка шаблона presets/{c}.build.json в варианты.
// Не зависит от `figma` — тестируется в Node. Правило — docs/build-rules.md.

export type Cond = Record<string, string | string[]>;
export type ByAxis = { by: string; map: Record<string, string | number> };
export type Val = string | number | ByAxis;

export interface LayoutTpl {
  /** Направление; может зависеть от варианта (`{by: 'Field', map: {Horizontal: 'H', …}}`). */
  dir: 'H' | 'V' | ByAxis;
  gap?: Val; px?: Val; py?: Val; pt?: Val; pb?: Val; pl?: Val; pr?: Val;
  /** Выравнивание; может зависеть от варианта (`{by: 'State', map: {Empty: 'CENTER', …}}`). */
  align?: 'MIN' | 'CENTER' | 'MAX' | 'SPACE_BETWEEN' | ByAxis;
  counter?: 'MIN' | 'CENTER' | 'MAX' | ByAxis;
  w?: 'HUG' | 'FILL' | 'FIXED';
  h?: 'HUG' | 'FILL' | 'FIXED';
}

export interface NodeTpl {
  type: 'frame' | 'text' | 'rect' | 'icon' | 'instance';
  name: string;
  when?: Cond;
  layout?: LayoutTpl;
  w?: 'HUG' | 'FILL' | 'FIXED';
  width?: Val; height?: Val; minW?: Val; maxW?: Val;
  radius?: Val;
  fill?: Val;
  stroke?: { color?: Val; weight?: Val; align?: 'INSIDE' | 'OUTSIDE' | 'CENTER'; dash?: number[] };
  opacity?: Val;
  /** Закрепить тему `2. General` на узле (explicit mode): 'light' | 'dark'; пустая строка — наследовать.
   *  Нужен там, где подложка одинакова в обеих темах (Alert Bold): вложенные кнопки берут значения этой темы. */
  theme?: Val;
  /** Тень (DROP_SHADOW) на переменных: смещение, размытие, растяжение, цвет. */
  shadow?: { x: Val; y: Val; blur: Val; spread: Val; color: Val };
  visible?: boolean;
  /** focus — вокруг родителя с отступом offset (отрицательный — внутрь); center; stretch-x; after — справа от родителя (x = ширина + offset, y = 0);
   *  at — в точке pos (статус и бейдж в углу аватара, как в файле). */
  abs?: 'focus' | 'center' | 'stretch-x' | 'after' | 'at';
  pos?: { x: Val; y: Val };
  offset?: Val;
  refs?: { visible?: string; characters?: string; mainComponent?: string };
  /** style — текстовый стиль (как в готовых компонентах); typography — база переменных L2 `…/{size|line-height|letter-spacing|weight}`
   *  для прямой привязки без стиля (новые компоненты), fontStyle — начертание Roboto под weight. */
  text?: { chars: Val; style?: Val; typography?: Val; fontStyle?: string; fill?: Val; truncate?: boolean; wrap?: boolean };
  icon?: { name: Val; size?: Val; color?: Val };
  instance?: { set: Val; variant: Record<string, Val>; props?: Record<string, Val | boolean> };
  /** Вложенный экземпляр: свойства открываются наружу (isExposedInstance). */
  expose?: boolean;
  children?: NodeTpl[];
}

export interface PropDef { name: string; type: 'TEXT' | 'BOOLEAN' | 'INSTANCE_SWAP'; default: string | boolean }

export interface VarDef { from: string | string[]; case?: 'lower'; map?: Record<string, string> }

export interface SetDef {
  /** Имя набора; при пустых осях — одиночный компонент (как `_ Avatar / Counter / m` в файле). */
  name: string;
  description?: string;
  axes: { name: string; values: string[] }[];
  exclude?: Cond[];
  /** columns — ось колонок; blocks — ось блоков строк; rows — оси внутри блока;
   *  split — ось, чьи значения делят набор на половины (Inverse: светлая слева, тёмная справа). */
  grid?: {
    columns: string; blocks?: string; rows?: string[]; split?: string | { axis: string; values: string[] };
    /** Колонки, которые показываются на своей подложке (значение оси колонок → переменная фона), после светлой и тёмной половин.
     *  Например, приватная часть `_ Alert / Action` — на тёмной поверхности и на заливке роли, где она применяется. */
    backdrops?: Record<string, string>;
  };
  vars?: Record<string, VarDef>;
  props: PropDef[];
  root: NodeTpl;
  /** Новый набор внутри повтора существующего компонента (Field / Select у Select): проверяется строго. */
  origin?: 'existing' | 'new';
  /** Варианты, которые WCAG не требует читать (недоступные, 1.4.3): не проверяются на контраст. */
  a11y?: {
    exempt?: Cond; reason?: string;
    /** На каких подложках стоит вариант (значение оси → переменные фона): проверяется худший случай. */
    surfaces?: { axis: string; map: Record<string, string[]> };
  };
}

export interface SpecItem {
  set: string; variant: Record<string, string>; props?: Record<string, string | boolean>; label?: string; width?: number;
  /** Свойства открытых вложенных экземпляров: { "Action": { "Loading": "True" } }. */
  nested?: Record<string, Record<string, string | boolean>>;
}
export interface SpecCard { title?: string; description?: string; inverse?: boolean; items: SpecItem[] }
export interface SpecColumn { title: string; description?: string; width?: number; grid?: number; cards: SpecCard[] }
export interface SpecDef { title: string; description?: string; columns: SpecColumn[] }

export interface BuildDef {
  component: string;
  title: string;
  page?: string;
  origin?: 'existing' | 'new';
  requires?: string[];
  notes?: string[];
  sets: SetDef[];
  spec?: SpecDef;
  /** Явные исключения из правила L3 → L2 → L1 (например, цвет тени на L1, пока эффекты не проработаны). */
  exceptions?: { token: string; reason: string }[];
}

// ---------------------------------------------------------------- развёрнутые узлы
export type RVal = string | number;

export interface RNode {
  type: NodeTpl['type'];
  name: string;
  layout?: { dir: 'H' | 'V'; gap?: RVal; pt?: RVal; pb?: RVal; pl?: RVal; pr?: RVal; align: string; counter: string; w: string; h: string };
  w?: 'HUG' | 'FILL' | 'FIXED';
  width?: RVal; height?: RVal; minW?: RVal; maxW?: RVal;
  radius?: RVal;
  fill?: RVal;
  stroke?: { color?: RVal; weight?: RVal; align: string; dash?: number[] };
  opacity?: RVal;
  theme?: 'light' | 'dark';
  shadow?: { x?: RVal; y?: RVal; blur?: RVal; spread?: RVal; color?: RVal };
  visible?: boolean;
  abs?: NodeTpl['abs'];
  offset?: number;
  pos?: { x: number; y: number };
  refs?: NodeTpl['refs'];
  text?: { chars: string; style?: string; typography?: string; fontStyle?: string; fill?: RVal; truncate?: boolean; wrap?: boolean };
  icon?: { name: string; size?: RVal; color?: RVal };
  instance?: { set: string; variant: Record<string, string>; props: Record<string, string | boolean> };
  expose?: boolean;
  children: RNode[];
}

export interface Variant { name: string; values: Record<string, string>; root: RNode }

// ---------------------------------------------------------------- развёртка
export function matches(values: Record<string, string>, cond?: Cond): boolean {
  if (!cond) return true;
  return Object.entries(cond).every(([k, v]) => (Array.isArray(v) ? v.includes(values[k]) : values[k] === v));
}

export function combinations(set: SetDef): Record<string, string>[] {
  let out: Record<string, string>[] = [{}];
  for (const a of set.axes) out = out.flatMap((o) => a.values.map((v) => ({ ...o, [a.name]: v })));
  return out.filter((o) => !(set.exclude ?? []).some((ex) => matches(o, ex)));
}

export function variantName(set: SetDef, values: Record<string, string>): string {
  return set.axes.map((a) => `${a.name}=${values[a.name]}`).join(', ');
}

function varsFor(set: SetDef, values: Record<string, string>): Record<string, string> {
  const out: Record<string, string> = { ...values };
  for (const [key, def] of Object.entries(set.vars ?? {})) {
    const src = Array.isArray(def.from) ? def.from.map((f) => values[f]).join('|') : values[def.from];
    let v = def.map && src in def.map ? def.map[src] : src;
    if (def.case === 'lower') v = v.toLowerCase();
    out[key] = v;
  }
  return out;
}

function isBy(v: unknown): v is ByAxis {
  return typeof v === 'object' && v !== null && 'by' in v && 'map' in v;
}

export function resolveVal(v: Val | undefined, values: Record<string, string>, vars: Record<string, string>): RVal | undefined {
  if (v === undefined) return undefined;
  if (isBy(v)) return resolveVal(v.map[values[v.by]], values, vars);
  if (typeof v === 'number') return v;
  return v.replace(/\{([^}]+)\}/g, (_, k) => {
    if (!(k in vars)) throw new Error(`нет подстановки {${k}} в «${v}»`);
    return vars[k];
  });
}

function expandNode(t: NodeTpl, values: Record<string, string>, vars: Record<string, string>): RNode | null {
  if (!matches(values, t.when)) return null;
  const r = (v: Val | undefined) => resolveVal(v, values, vars);
  const n: RNode = { type: t.type, name: String(r(t.name)), children: [] };
  if (t.layout) {
    const l = t.layout;
    n.layout = {
      dir: String(r(l.dir)) as 'H' | 'V', gap: r(l.gap), pt: r(l.pt ?? l.py), pb: r(l.pb ?? l.py), pl: r(l.pl ?? l.px), pr: r(l.pr ?? l.px),
      align: String(r(l.align) ?? 'MIN'), counter: String(r(l.counter) ?? 'MIN'), w: l.w ?? 'HUG', h: l.h ?? 'HUG',
    };
  }
  if (t.w) n.w = t.w;
  for (const k of ['width', 'height', 'minW', 'maxW', 'radius', 'fill', 'opacity'] as const) {
    const v = r(t[k]);
    // пустое значение по оси (by: { Default: '' }) — свойство у варианта не задаётся
    if (v !== undefined && v !== '') n[k] = v;
  }
  if (t.stroke) n.stroke = { color: r(t.stroke.color), weight: r(t.stroke.weight), align: t.stroke.align ?? 'INSIDE', dash: t.stroke.dash };
  if (t.shadow) n.shadow = { x: r(t.shadow.x), y: r(t.shadow.y), blur: r(t.shadow.blur), spread: r(t.shadow.spread), color: r(t.shadow.color) };
  if (t.visible !== undefined) n.visible = t.visible;
  const theme = r(t.theme);
  if (theme === 'light' || theme === 'dark') n.theme = theme;
  if (t.abs) n.abs = t.abs;
  if (t.offset !== undefined) n.offset = Number(r(t.offset));
  if (t.pos) n.pos = { x: Number(r(t.pos.x)), y: Number(r(t.pos.y)) };
  if (t.refs) n.refs = t.refs;
  if (t.text) {
    n.text = {
      chars: String(r(t.text.chars)), style: t.text.style ? String(r(t.text.style)) : undefined,
      typography: t.text.typography ? String(r(t.text.typography)) : undefined, fontStyle: t.text.fontStyle,
      fill: r(t.text.fill), truncate: t.text.truncate, wrap: t.text.wrap,
    };
  }
  if (t.icon) n.icon = { name: String(r(t.icon.name)), size: r(t.icon.size), color: r(t.icon.color) };
  if (t.expose) n.expose = true;
  if (t.instance) {
    n.instance = {
      set: String(r(t.instance.set)),
      variant: Object.fromEntries(Object.entries(t.instance.variant).map(([k, v]) => [k, String(r(v))])),
      props: Object.fromEntries(Object.entries(t.instance.props ?? {}).map(([k, v]) => [k, typeof v === 'boolean' ? v : String(r(v))])),
    };
  }
  for (const c of t.children ?? []) {
    const e = expandNode(c, values, vars);
    if (e) n.children.push(e);
  }
  return n;
}

export function expandSet(set: SetDef): Variant[] {
  return combinations(set).map((values) => {
    const vars = varsFor(set, values);
    const root = expandNode(set.root, values, vars)!;
    root.name = variantName(set, values);
    return { name: root.name, values, root };
  });
}

// ---------------------------------------------------------------- ссылки
export interface BuildRefs {
  variables: Set<string>;
  styles: Set<string>;
  icons: Set<string>;
  sets: Set<string>;
}

const isToken = (v: RVal | undefined): v is string => typeof v === 'string' && v.includes('/');
export const TYPO_PROPS = ['size', 'line-height', 'letter-spacing', 'weight'] as const;

export function collectRefs(def: BuildDef, variants?: Map<string, Variant[]>): BuildRefs {
  const refs: BuildRefs = { variables: new Set(), styles: new Set(), icons: new Set(), sets: new Set() };
  const walk = (n: RNode) => {
    const l = n.layout;
    for (const v of [l?.gap, l?.pt, l?.pb, l?.pl, l?.pr, n.width, n.height, n.minW, n.maxW, n.radius, n.fill, n.opacity,
      n.stroke?.color, n.stroke?.weight, n.text?.fill, n.icon?.size, n.icon?.color,
      n.shadow?.x, n.shadow?.y, n.shadow?.blur, n.shadow?.spread, n.shadow?.color]) if (isToken(v)) refs.variables.add(v);
    if (n.text?.style) refs.styles.add(n.text.style);
    if (n.text?.typography) for (const p of TYPO_PROPS) refs.variables.add(`${n.text.typography}/${p}`);
    if (n.icon) refs.icons.add(n.icon.name);
    if (n.instance) {
      refs.sets.add(n.instance.set);
      for (const v of Object.values(n.instance.props)) if (typeof v === 'string' && v.startsWith('icon:')) refs.icons.add(v.slice(5));
    }
    n.children.forEach(walk);
  };
  for (const s of def.sets) {
    for (const v of variants?.get(s.name) ?? expandSet(s)) walk(v.root);
    for (const p of s.props) if (p.type === 'INSTANCE_SWAP') refs.icons.add(String(p.default));
  }
  for (const c of def.spec?.columns ?? []) for (const card of c.cards) for (const it of card.items) refs.sets.add(it.set);
  return refs;
}

/** Порядок сборки: сначала компоненты, от которых зависят другие (Alert после Button). */
export function buildOrder(defs: BuildDef[]): BuildDef[] {
  const byName = new Map(defs.map((d) => [d.component, d]));
  const out: BuildDef[] = [];
  const seen = new Set<string>();
  const visit = (d: BuildDef) => {
    if (seen.has(d.component)) return;
    seen.add(d.component);
    for (const r of d.requires ?? []) { const x = byName.get(r); if (x) visit(x); }
    out.push(d);
  };
  defs.forEach(visit);
  return out;
}

/** Раскладка вариантов сеткой: колонки — ось типа, блоки — размер, строки — остальные оси.
 *  С split значения оси (например, Inverse) раскладываются половинами слева направо. */
export function gridSlots(set: SetDef, variants: Variant[]): Map<string, { col: number; row: number; block: number; half: number }> {
  const g = set.grid ?? { columns: set.axes[1]?.name ?? set.axes[0].name };
  const axis = (n: string) => set.axes.find((a) => a.name === n)!;
  const cols = axis(g.columns).values;
  const blocks = g.blocks ? axis(g.blocks).values : [''];
  // split: вся ось (значения идут половинами) или часть значений оси колонок (уходят на тёмную половину)
  const splitAxis = typeof g.split === 'string' ? g.split : g.split?.axis;
  const darkValues = typeof g.split === 'object' ? g.split.values : null;
  const halves = typeof g.split === 'string' ? axis(g.split).values : [''];
  const drops = Object.keys(g.backdrops ?? {});
  const halfOf = (v: Record<string, string>) => {
    const d = drops.indexOf(v[g.columns]);
    if (d >= 0) return 2 + d;
    return !splitAxis ? 0 : darkValues ? (darkValues.includes(v[splitAxis]) ? 1 : 0) : halves.indexOf(v[splitAxis]);
  };
  // колонки идут полосами: светлая, тёмная, затем подложки; внутри полосы — порядок значений оси
  const pairs = [...new Set(variants.map((v) => `${halfOf(v.values)}:${cols.indexOf(v.values[g.columns])}`))]
    .map((k) => k.split(':').map(Number)).sort((a, b) => a[0] - b[0] || a[1] - b[1]).map((x) => x.join(':'));
  const rowAxes = (g.rows ?? set.axes.map((a) => a.name).filter((n) => n !== g.columns && n !== g.blocks && n !== splitAxis)).map(axis);
  const rowKey = (v: Record<string, string>) => rowAxes.map((a) => a.values.indexOf(v[a.name]));
  const slots = new Map<string, { col: number; row: number; block: number; half: number }>();
  for (const block of blocks) {
    const inBlock = variants.filter((v) => !g.blocks || v.values[g.blocks] === block);
    const keys = [...new Set(inBlock.map((v) => rowKey(v.values).join(',')))]
      .sort((a, b) => { const x = a.split(',').map(Number), y = b.split(',').map(Number); for (let i = 0; i < x.length; i++) if (x[i] !== y[i]) return x[i] - y[i]; return 0; });
    for (const v of inBlock) {
      const half = halfOf(v.values);
      const col = pairs.indexOf(`${half}:${cols.indexOf(v.values[g.columns])}`);
      slots.set(v.name, { col, row: keys.indexOf(rowKey(v.values).join(',')), block: blocks.indexOf(block), half });
    }
  }
  return slots;
}
