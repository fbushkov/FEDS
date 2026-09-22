import { SnapIndex, segmentOk } from './snapshot';
import type { Conventions, Snapshot } from './types';

export interface Issue { kind: string; title: string; items: string[] }

export interface Analysis {
  collections: { name: string; modes: string[]; count: number; level: string }[];
  textStyles: number;
  effectStyles: number;
  componentRoots: { root: string; count: number }[];
  grammar: { root: string; count: number; segments: string[][] }[];
  inversePairs: { pairs: number; orphans: string[] };
  issues: Issue[];
  missing: string[];
}

/** F1: разбор системы. Ничего не исправляет. */
export function analyze(snap: Snapshot, conv: Conventions): Analysis {
  const ix = new SnapIndex(snap, conv);
  const missing = (['l1', 'l2', 'l3'] as const).filter((k) => !ix[k]).map((k) => conv.collections[k]);
  const levelName = (id: string) =>
    id === ix.l1?.id ? 'L1' : id === ix.l2?.id ? 'L2' : id === ix.l3?.id ? 'L3' : '—';

  const collections = snap.collections.map((c) => ({
    name: c.name,
    modes: c.modes.map((m) => m.name),
    count: snap.variables.filter((v) => v.collectionId === c.id).length,
    level: levelName(c.id),
  }));

  const broken: string[] = [];
  const skip: string[] = [];
  const raw: string[] = [];
  const noScope: string[] = [];
  const badName: string[] = [];
  for (const v of snap.variables) {
    const lvl = ix.levelOf(v);
    if (!lvl) continue;
    if (!segmentOk(v.name, conv)) badName.push(v.name);
    if (lvl > 1 && (v.scopes.length === 0 || v.scopes.includes('ALL_SCOPES'))) noScope.push(`${v.name} (L${lvl})`);
    for (const [modeId, val] of Object.entries(v.values)) {
      if (val.kind === 'value') {
        if (lvl > 1) raw.push(`${v.name} (L${lvl})`);
        continue;
      }
      const t = ix.byId.get(val.id);
      if (!t) {
        broken.push(`${v.name} → ${val.id}`);
        continue;
      }
      const tl = ix.levelOf(t);
      if (tl !== lvl - 1) skip.push(`${v.name} (L${lvl}) → ${t.name} (L${tl || '?'})${modeId ? '' : ''}`);
    }
  }

  // дубли без учёта регистра
  const lower = new Map<string, string[]>();
  for (const v of snap.variables) {
    const k = v.collectionId + '|' + v.name.toLowerCase();
    lower.set(k, [...(lower.get(k) ?? []), v.name]);
  }
  const dupes = [...lower.values()].filter((x) => x.length > 1).map((x) => x.join(' = '));

  // корни L3 = компоненты
  const rootCount = new Map<string, number>();
  for (const v of ix.all(3)) rootCount.set(v.name.split('/')[0], (rootCount.get(v.name.split('/')[0]) ?? 0) + 1);

  // грамматика L2 по корням
  const groups = new Map<string, string[][]>();
  for (const v of ix.all(2)) {
    const s = v.name.split('/');
    const root = s[0] === 'color' ? s.slice(0, 2).join('/') : s[0];
    groups.set(root, [...(groups.get(root) ?? []), s]);
  }
  const grammar = [...groups.entries()].map(([root, rows]) => {
    const len = Math.max(...rows.map((r) => r.length));
    const segments: string[][] = [];
    for (let i = 0; i < len; i++) segments.push([...new Set(rows.map((r) => r[i]).filter(Boolean))].sort());
    return { root, count: rows.length, segments };
  });

  // пары inverse-*
  const l2names = new Set(ix.all(2).map((v) => v.name));
  let pairs = 0;
  const orphans: string[] = [];
  for (const n of l2names) {
    const s = n.split('/');
    const i = s.findIndex((x) => x.startsWith('inverse-'));
    if (i < 0) continue;
    const base = [...s];
    base[i] = s[i].slice('inverse-'.length);
    if (l2names.has(base.join('/'))) pairs++;
    else orphans.push(n);
  }

  const issues: Issue[] = [
    { kind: 'broken', title: 'Битые алиасы', items: broken },
    { kind: 'skip', title: 'Ссылки через уровень или вверх', items: skip },
    { kind: 'raw', title: 'Сырые значения выше L1', items: raw },
    { kind: 'scope', title: 'Без scopes или ALL_SCOPES (L2/L3)', items: noScope },
    { kind: 'name', title: 'Имена не по регулярке сегмента', items: badName },
    { kind: 'dupe', title: 'Дубли имён (без учёта регистра)', items: dupes },
  ];

  return {
    collections,
    textStyles: snap.styles.filter((s) => s.kind === 'TEXT').length,
    effectStyles: snap.styles.filter((s) => s.kind === 'EFFECT').length,
    componentRoots: [...rootCount.entries()].map(([root, count]) => ({ root, count })).sort((a, b) => a.root.localeCompare(b.root)),
    grammar,
    inversePairs: { pairs, orphans },
    issues,
    missing,
  };
}
