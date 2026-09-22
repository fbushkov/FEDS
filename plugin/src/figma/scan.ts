import type { ModeValue, SnapVariable, Snapshot, VarType } from '../core/types';

function toModeValue(v: VariableValue): ModeValue {
  if (typeof v === 'object' && v !== null && 'type' in v && v.type === 'VARIABLE_ALIAS') return { kind: 'alias', id: v.id };
  if (typeof v === 'object' && v !== null && 'r' in v) {
    const c = v as RGBA | RGB;
    return { kind: 'value', value: { r: c.r, g: c.g, b: c.b, a: 'a' in c ? c.a : 1 } };
  }
  return { kind: 'value', value: v as number | string | boolean };
}

function toSnap(v: Variable, remote = false): SnapVariable {
  const values: Record<string, ModeValue> = {};
  for (const [modeId, val] of Object.entries(v.valuesByMode)) values[modeId] = toModeValue(val);
  return {
    id: v.id, name: v.name, collectionId: v.variableCollectionId, type: v.resolvedType as VarType,
    scopes: [...v.scopes], hidden: v.hiddenFromPublishing, description: v.description, remote, values,
  };
}

/** Снимок локальных переменных и стилей файла (только чтение). */
export async function takeSnapshot(): Promise<Snapshot> {
  const [cols, vars, text, effect] = await Promise.all([
    figma.variables.getLocalVariableCollectionsAsync(),
    figma.variables.getLocalVariablesAsync(),
    figma.getLocalTextStylesAsync(),
    figma.getLocalEffectStylesAsync(),
  ]);
  const variables = vars.map((v) => toSnap(v));
  const known = new Set(variables.map((v) => v.id));

  // Алиасы на переменные других файлов (библиотек) — дочитываем, чтобы не считать их битыми.
  const foreign = new Set<string>();
  for (const v of variables) for (const val of Object.values(v.values)) if (val.kind === 'alias' && !known.has(val.id)) foreign.add(val.id);
  for (const id of foreign) {
    const r = await figma.variables.getVariableByIdAsync(id);
    if (r) variables.push(toSnap(r, true));
  }

  return {
    collections: cols.map((c) => ({ id: c.id, name: c.name, modes: c.modes.map((m) => ({ id: m.modeId, name: m.name })), defaultModeId: c.defaultModeId })),
    variables,
    styles: [
      ...text.map((s) => ({
        id: s.id, name: s.name, kind: 'TEXT' as const,
        boundVars: Object.fromEntries(Object.entries(s.boundVariables ?? {}).map(([k, a]) => [k, (a as VariableAlias).id])),
      })),
      ...effect.map((s) => ({ id: s.id, name: s.name, kind: 'EFFECT' as const })),
    ],
  };
}
