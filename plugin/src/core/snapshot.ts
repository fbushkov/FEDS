import type { Conventions, ModeValue, RGBA, SnapCollection, SnapVariable, Snapshot } from './types';

/** Индекс снимка: быстрый доступ к коллекциям уровней и переменным по имени. */
export class SnapIndex {
  readonly byId = new Map<string, SnapVariable>();
  readonly l1?: SnapCollection;
  readonly l2?: SnapCollection;
  readonly l3?: SnapCollection;
  private readonly byName = new Map<string, Map<string, SnapVariable>>();

  constructor(readonly snap: Snapshot, readonly conv: Conventions) {
    const find = (n: string) => snap.collections.find((c) => c.name === n);
    this.l1 = find(conv.collections.l1);
    this.l2 = find(conv.collections.l2);
    this.l3 = find(conv.collections.l3);
    for (const v of snap.variables) {
      this.byId.set(v.id, v);
      if (!this.byName.has(v.collectionId)) this.byName.set(v.collectionId, new Map());
      this.byName.get(v.collectionId)!.set(v.name, v);
    }
  }

  get(level: 1 | 2 | 3, name: string): SnapVariable | undefined {
    const col = level === 1 ? this.l1 : level === 2 ? this.l2 : this.l3;
    return col ? this.byName.get(col.id)?.get(name) : undefined;
  }

  all(level: 1 | 2 | 3): SnapVariable[] {
    const col = level === 1 ? this.l1 : level === 2 ? this.l2 : this.l3;
    return col ? [...(this.byName.get(col.id)?.values() ?? [])] : [];
  }

  levelOf(v: SnapVariable): 1 | 2 | 3 | 0 {
    if (v.collectionId === this.l1?.id) return 1;
    if (v.collectionId === this.l2?.id) return 2;
    if (v.collectionId === this.l3?.id) return 3;
    return 0;
  }

  modeId(col: SnapCollection | undefined, name: string): string | undefined {
    return col?.modes.find((m) => m.name === name)?.id;
  }

  /** Значение переменной в режиме (по имени режима L2), с разворотом алиасов. */
  resolve(v: SnapVariable, modeName: string, depth = 0): ModeValue | undefined {
    if (depth > 10) return undefined;
    const col = this.snap.collections.find((c) => c.id === v.collectionId);
    const modeId = this.modeId(col, modeName) ?? col?.defaultModeId ?? Object.keys(v.values)[0];
    const val = v.values[modeId] ?? Object.values(v.values)[0];
    if (!val) return undefined;
    if (val.kind === 'alias') {
      const t = this.byId.get(val.id);
      return t ? this.resolve(t, modeName, depth + 1) : undefined;
    }
    return val;
  }

  /** Имя цели алиаса в режиме (или undefined, если значение сырое). */
  aliasName(v: SnapVariable, modeName?: string): string | undefined {
    const col = this.snap.collections.find((c) => c.id === v.collectionId);
    const modeId = (modeName && this.modeId(col, modeName)) || col?.defaultModeId || Object.keys(v.values)[0];
    const val = v.values[modeId];
    return val?.kind === 'alias' ? this.byId.get(val.id)?.name ?? `?${val.id}` : undefined;
  }
}

export function isColor(v: unknown): v is RGBA {
  return typeof v === 'object' && v !== null && 'r' in v && 'g' in v && 'b' in v;
}

export function segmentOk(name: string, conv: Conventions): boolean {
  const re = new RegExp(conv.segment);
  return name.split('/').every((s) => re.test(s));
}

/** Корни L3, которыми владеет пресет, и префиксы для поиска «лишних» токенов. */
export function ownPrefixes(component: string, roots?: string[], prefixes?: string[]): string[] {
  if (prefixes && prefixes.length) return prefixes;
  const r = roots && roots.length ? roots : [component.split('/')[0]];
  if (r.length === 1 && r[0] !== component && component.startsWith(r[0] + '-')) {
    const sub = component.slice(r[0].length + 1);
    return [`${r[0]}/${sub}/`, `${r[0]}/size/${sub}/`];
  }
  return r.map((x) => x + '/');
}
