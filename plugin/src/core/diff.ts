import { hexToRgba, rgbaToHex, sameColor } from './color';
import { effectiveContrast } from './contrast';
import { SnapIndex, isColor, ownPrefixes, segmentOk } from './snapshot';
import type {
  Approvals, ContrastRow, Conventions, DiffResult, DiffRow, Plan, Preset, PresetL1, PresetL2, RGBA, Snapshot, SnapVariable,
} from './types';

const MODES = ['light', 'dark'] as const;

function sameScopes(a: string[], b: string[]): boolean {
  return a.length === b.length && [...a].sort().join() === [...b].sort().join();
}

function fmt(v: string | number): string {
  return typeof v === 'number' ? String(v) : v;
}

/** Объединение нескольких пресетов в один пакет (система + компоненты). Одинаковые записи схлопываются. */
export function mergePresets(list: Preset[]): { preset: Preset; conflicts: string[] } {
  if (list.length === 1) return { preset: list[0], conflicts: [] };
  const conflicts: string[] = [];
  const pick = <T extends { name: string }>(items: T[], kind: string): T[] => {
    const map = new Map<string, T>();
    for (const t of items) {
      const prev = map.get(t.name);
      if (prev && JSON.stringify(prev) !== JSON.stringify(t)) conflicts.push(`${kind} ${t.name}: разные определения в пресетах`);
      if (!prev) map.set(t.name, t);
    }
    return [...map.values()];
  };
  return {
    preset: {
      component: list.map((p) => p.component).join(' + '),
      title: `${list.length} пресет(ов)`,
      prefixes: [...new Set(list.flatMap((p) => ownPrefixes(p.component, p.roots, p.prefixes)))],
      l1: pick(list.flatMap((p) => p.l1 ?? []), 'L1'),
      l2: pick(list.flatMap((p) => p.l2 ?? []), 'L2'),
      l3: pick(list.flatMap((p) => p.l3), 'L3'),
      textStyles: pick(list.flatMap((p) => p.textStyles ?? []), 'Стиль'),
      contrast: list.flatMap((p) => p.contrast ?? []),
      exceptions: list.flatMap((p) => p.exceptions ?? []),
      decisions: [],
    },
    conflicts,
  };
}

export interface DiffOptions {
  /** Все L3 из каталога пресетов: такие токены не считаются «лишними» для другого пресета. */
  catalogL3?: Set<string>;
  /** Текстовые стили. По решению автора (2026-09-21) не создаются: типографика компонентов — переменные L2. */
  styles?: boolean;
}

/** F3: дифф пресета (или пакета) с файлом. Ничего не меняет. */
export function diffPreset(preset: Preset, snap: Snapshot, conv: Conventions, opts: DiffOptions = {}): DiffResult {
  const ix = new SnapIndex(snap, conv);
  const errors: string[] = [];
  const warnings: string[] = [];
  const rows: DiffRow[] = [];
  const exc = new Set((preset.exceptions ?? []).map((e) => e.token));
  const presetL1 = new Map((preset.l1 ?? []).map((t) => [t.name, t]));
  const presetL2 = new Map((preset.l2 ?? []).map((t) => [t.name, t]));
  const presetL3 = new Map(preset.l3.map((t) => [t.name, t]));
  const modeL2 = (m: 'light' | 'dark') => (m === 'light' ? conv.modes.light : conv.modes.dark);

  const createCollections = (['l1', 'l2', 'l3'] as const).filter((k) => !ix[k]).map((k) => conv.collections[k]);
  for (const c of createCollections) warnings.push(`Коллекции «${c}» нет в файле — она будет создана.`);
  if (ix.l2) {
    for (const m of MODES) {
      if (!ix.modeId(ix.l2, modeL2(m))) errors.push(`В «${conv.collections.l2}» нет режима «${modeL2(m)}». Добавлять режимы в существующую коллекцию плагин не будет.`);
    }
  }
  const l1Type = (name: string) => presetL1.get(name)?.type ?? ix.get(1, name)?.type;

  // ---- L1
  for (const t of preset.l1 ?? []) {
    if (!segmentOk(t.name, conv)) errors.push(`L1 ${t.name}: имя не по регулярке сегмента`);
    if (t.type === 'COLOR' && (typeof t.value !== 'string' || !hexToRgba(t.value))) errors.push(`L1 ${t.name}: цвет должен быть hex или rgba()`);
    const ex = ix.get(1, t.name);
    if (!ex) {
      rows.push({ level: 1, name: t.name, status: 'add', target: fmt(t.value) });
      continue;
    }
    const r = ix.resolve(ex, 'light');
    const cur = r?.kind === 'value' ? (isColor(r.value) ? rgbaToHex(r.value) : String(r.value)) : ix.aliasName(ex) ?? '?';
    const want = typeof t.value === 'string' ? t.value.toLowerCase() : String(t.value);
    const reasons: string[] = [];
    const want2 = t.type === 'COLOR' && typeof t.value === 'string' ? hexToRgba(t.value) : undefined;
    const equal = want2 && r?.kind === 'value' && isColor(r.value) ? sameColor(r.value, want2) : cur.toLowerCase() === want;
    if (!equal) reasons.push(`значение: ${cur} → ${want}`);
    if (!sameScopes(ex.scopes, t.scopes)) reasons.push(`scopes: ${ex.scopes.join(',') || '—'} → ${t.scopes.join(',') || '—'}`);
    rows.push({ level: 1, name: t.name, status: reasons.length ? 'changed' : 'same', current: cur, target: want, reasons, existingId: ex.id });
  }

  // ---- L2
  for (const t of preset.l2 ?? []) {
    if (!segmentOk(t.name, conv)) errors.push(`L2 ${t.name}: имя не по регулярке сегмента`);
    for (const m of MODES) {
      const val = t.values[m];
      if (typeof val === 'string') {
        const type = l1Type(val);
        if (!type) errors.push(`L2 ${t.name} [${m}]: примитив «${val}» не найден в «${conv.collections.l1}»`);
        else if ((type === 'COLOR') !== (t.type === 'COLOR')) errors.push(`L2 ${t.name} [${m}]: тип примитива «${val}» не совпадает`);
      } else if (!exc.has(t.name)) {
        errors.push(`L2 ${t.name} [${m}]: сырое значение ${val} без записи в exceptions`);
      }
    }
    const ex = ix.get(2, t.name);
    if (!ex) {
      rows.push({ level: 2, name: t.name, status: 'add', target: `${fmt(t.values.light)} | ${fmt(t.values.dark)}` });
      continue;
    }
    const reasons: string[] = [];
    const cur = MODES.map((m) => ix.aliasName(ex, modeL2(m)) ?? rawOf(ix, ex, modeL2(m)));
    const want = MODES.map((m) => fmt(t.values[m]));
    if (cur.join('|') !== want.join('|')) reasons.push(`значение: ${cur.join(' | ')} → ${want.join(' | ')}`);
    if (!sameScopes(ex.scopes, t.scopes)) reasons.push(`scopes: ${ex.scopes.join(',')} → ${t.scopes.join(',')}`);
    rows.push({
      level: 2, name: t.name, status: reasons.length ? 'changed' : 'same', current: cur.join(' | '), target: want.join(' | '),
      reasons, existingId: ex.id,
    });
  }

  // ---- L3
  for (const t of preset.l3) {
    if (!segmentOk(t.name, conv)) errors.push(`L3 ${t.name}: имя не по регулярке сегмента`);
    const target = presetL2.get(t.alias) ?? ix.get(2, t.alias);
    if (!target) {
      if ((ix.get(1, t.alias) || presetL1.has(t.alias)) && exc.has(t.name)) {
        warnings.push(`L3 ${t.name} → L1 ${t.alias}: исключение, помечено в пресете`);
      } else {
        errors.push(`L3 ${t.name}: алиас «${t.alias}» не найден в «${conv.collections.l2}» (не хватает зависимого пресета?)`);
        rows.push({ level: 3, name: t.name, status: 'blocked', target: t.alias, reasons: ['нет цели алиаса'] });
        continue;
      }
    } else if (target.type !== t.type) {
      errors.push(`L3 ${t.name}: тип ${t.type} ≠ ${target.type} у «${t.alias}»`);
    }
    const ex = ix.get(3, t.name);
    if (!ex) {
      rows.push({ level: 3, name: t.name, status: 'add', target: t.alias });
      continue;
    }
    const reasons: string[] = [];
    const cur = ix.aliasName(ex) ?? rawOf(ix, ex);
    if (cur !== t.alias) reasons.push(`алиас: ${cur} → ${t.alias}`);
    if (!sameScopes(ex.scopes, t.scopes)) reasons.push(`scopes: ${ex.scopes.join(',')} → ${t.scopes.join(',')}`);
    rows.push({ level: 3, name: t.name, status: reasons.length ? 'changed' : 'same', current: cur, target: t.alias, reasons, existingId: ex.id });
  }

  // ---- лишние: токены пресета в файле, которых нет ни в пресете, ни в других пресетах каталога
  const prefixes = ownPrefixes(preset.component, preset.roots, preset.prefixes);
  for (const v of ix.all(3)) {
    if (prefixes.some((p) => v.name.startsWith(p)) && !presetL3.has(v.name) && !opts.catalogL3?.has(v.name)) {
      rows.push({ level: 3, name: v.name, status: 'extra', current: ix.aliasName(v) ?? rawOf(ix, v), existingId: v.id });
    }
  }

  // ---- текстовые стили
  for (const s of opts.styles ? preset.textStyles ?? [] : []) {
    for (const [prop, vname] of Object.entries(s.vars)) {
      if (!presetL2.has(vname) && !ix.get(2, vname)) errors.push(`Стиль ${s.name}: переменная ${prop} «${vname}» не найдена в L2`);
    }
    const ex = snap.styles.find((x) => x.kind === 'TEXT' && x.name === s.name);
    rows.push({ level: 'style', name: s.name, status: ex ? 'same' : 'add', existingId: ex?.id, target: `${s.fontFamily ?? 'Roboto'} ${s.fontStyle ?? ''}`.trim() });
  }

  // ---- контраст
  const contrast: ContrastRow[] = [];
  for (const c of preset.contrast ?? []) {
    const need = c.kind === 'text' ? 4.5 : 3;
    for (const m of MODES) {
      const fg = valueOf(c.fg, m, preset, ix, conv, presetL1, presetL2);
      const bg = valueOf(c.bg, m, preset, ix, conv, presetL1, presetL2);
      const base = valueOf(c.over ?? 'color/bg/page/main', m, preset, ix, conv, presetL1, presetL2) ?? { r: 1, g: 1, b: 1, a: 1 };
      if (!fg || !bg) {
        warnings.push(`Контраст ${c.fg} / ${c.bg} [${m}]: не удалось получить цвет`);
        continue;
      }
      const ratio = effectiveContrast(fg, bg, base);
      const ok = ratio >= need;
      contrast.push({ fg: c.fg, bg: c.bg, mode: m, ratio, need, ok, accepted: !!c.accepted });
      if (!ok && !c.accepted) warnings.push(`Контраст ${c.fg} на ${c.bg} [${m}] = ${ratio.toFixed(2)} < ${need}`);
    }
  }

  return { component: preset.component, createCollections, rows, errors, warnings, contrast };
}

function rawOf(ix: SnapIndex, v: SnapVariable, mode = 'light'): string {
  const r = ix.resolve(v, mode);
  if (!r || r.kind !== 'value') return '?';
  return isColor(r.value) ? rgbaToHex(r.value) : String(r.value);
}

function valueOf(
  name: string, m: 'light' | 'dark', preset: Preset, ix: SnapIndex, conv: Conventions,
  presetL1: Map<string, PresetL1>, presetL2: Map<string, PresetL2>, depth = 0,
): RGBA | undefined {
  if (depth > 5) return undefined;
  const modeName = m === 'light' ? conv.modes.light : conv.modes.dark;
  const l3 = preset.l3.find((t) => t.name === name);
  if (l3) return valueOf(l3.alias, m, preset, ix, conv, presetL1, presetL2, depth + 1);
  const l2 = presetL2.get(name);
  if (l2) {
    const val = l2.values[m];
    return typeof val === 'string' ? valueOf(val, m, preset, ix, conv, presetL1, presetL2, depth + 1) : undefined;
  }
  const l1 = presetL1.get(name);
  if (l1 && typeof l1.value === 'string') return hexToRgba(l1.value);
  const v = ix.get(3, name) ?? ix.get(2, name) ?? ix.get(1, name);
  const r = v ? ix.resolve(v, modeName) : undefined;
  return r && r.kind === 'value' && isColor(r.value) ? r.value : undefined;
}

/** План записи: безопасные добавления + то, что пользователь явно разрешил. */
export function buildPlan(preset: Preset, diff: DiffResult, approvals: Approvals): Plan {
  const change = new Set(approvals.change);
  const remove = new Set(approvals.remove);
  const status = new Map(diff.rows.map((r) => [`${r.level}|${r.name}`, r]));
  const is = (lvl: 1 | 2 | 3 | 'style', name: string, s: string) => status.get(`${lvl}|${name}`)?.status === s;
  return {
    component: preset.component,
    createCollections: diff.createCollections,
    createL1: (preset.l1 ?? []).filter((t) => is(1, t.name, 'add')),
    updateL1: (preset.l1 ?? []).filter((t) => is(1, t.name, 'changed') && change.has(t.name)),
    createL2: (preset.l2 ?? []).filter((t) => is(2, t.name, 'add')),
    updateL2: (preset.l2 ?? []).filter((t) => is(2, t.name, 'changed') && change.has(t.name)),
    createL3: preset.l3.filter((t) => is(3, t.name, 'add')),
    updateL3: preset.l3.filter((t) => is(3, t.name, 'changed') && change.has(t.name)),
    remove: diff.rows.filter((r) => r.status === 'extra' && remove.has(r.name) && r.existingId).map((r) => ({ id: r.existingId!, name: r.name })),
    createStyles: (preset.textStyles ?? []).filter((s) => is('style', s.name, 'add')),
    exceptions: (preset.exceptions ?? []).map((e) => e.token),
  };
}

export function planSize(p: Plan): number {
  return p.createL1.length + p.updateL1.length + p.createL2.length + p.updateL2.length + p.createL3.length +
    p.updateL3.length + p.remove.length + p.createStyles.length;
}

// ---------------------------------------------------------------- каталог
export type CatalogState = 'in-file' | 'partial' | 'absent' | 'differs';

export interface CatalogStatus {
  component: string;
  state: CatalogState;
  add: number;
  same: number;
  changed: number;
  extra: number;
  blocked: number;
  total: number;
}

/** Статус каждого пресета каталога относительно файла: что уже есть, что можно добавить. */
export function catalogStatus(presets: Preset[], snap: Snapshot, conv: Conventions): CatalogStatus[] {
  const catalogL3 = new Set(presets.flatMap((p) => p.l3.map((t) => t.name)));
  return presets.map((p) => {
    const d = diffPreset(p, snap, conv, { catalogL3 });
    const by = (s: string) => d.rows.filter((r) => r.status === s).length;
    const add = by('add'), same = by('same'), changed = by('changed'), extra = by('extra'), blocked = by('blocked');
    const total = d.rows.filter((r) => r.status !== 'extra').length;
    const state: CatalogState = changed ? 'differs' : add + blocked === 0 ? 'in-file' : same === 0 ? 'absent' : 'partial';
    return { component: p.component, state, add, same, changed, extra, blocked, total };
  });
}

/** Зависимости пресета: пресеты каталога, которым принадлежат L2/L1, на которые он ссылается. */
export function resolveRequires(presets: Preset[]): Map<string, string[]> {
  const ownerL2 = new Map<string, string>();
  const ownerL1 = new Map<string, string>();
  for (const p of presets) {
    for (const t of p.l2 ?? []) if (!ownerL2.has(t.name)) ownerL2.set(t.name, p.component);
    for (const t of p.l1 ?? []) if (!ownerL1.has(t.name)) ownerL1.set(t.name, p.component);
  }
  const out = new Map<string, string[]>();
  for (const p of presets) {
    const req = new Set<string>();
    for (const t of p.l3) { const o = ownerL2.get(t.alias); if (o && o !== p.component) req.add(o); }
    for (const t of p.l2 ?? []) for (const v of Object.values(t.values)) {
      if (typeof v === 'string') { const o = ownerL1.get(v); if (o && o !== p.component) req.add(o); }
    }
    for (const s of p.textStyles ?? []) for (const v of Object.values(s.vars)) {
      const o = ownerL2.get(v); if (o && o !== p.component) req.add(o);
    }
    out.set(p.component, [...req].sort());
  }
  return out;
}
