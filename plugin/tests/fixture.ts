// Снимок из реального экспорта input/tokens/variables.json — фикстура для тестов ядра.
import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import type { ModeValue, SnapCollection, SnapVariable, Snapshot } from '../src/core/types';

const SRC = resolve(__dirname, '../../input/tokens/variables.json');

function parseColor(s: string) {
  const m = s.match(/rgba\(([^)]+)\)/);
  if (!m) return undefined;
  const [r, g, b, a] = m[1].split(',').map(Number);
  return { r: r / 255, g: g / 255, b: b / 255, a };
}

let cache: Snapshot | undefined;

export function loadSnapshot(): Snapshot {
  if (cache) return cache;
  const data = JSON.parse(readFileSync(SRC, 'utf-8'));
  const collections: SnapCollection[] = [];
  const raw: { col: string; ref: string; node: any; modeKeys: Record<string, string> }[] = [];

  for (const [colKey, body] of Object.entries<any>(data)) {
    const meta = body.$collection_metadata;
    const modes = meta.modes.map((m: any) => ({ id: `${meta.figmaId}/${m.key}`, name: m.name }));
    collections.push({ id: meta.figmaId, name: meta.name, modes, defaultModeId: modes[0].id });
    const modeKeys = Object.fromEntries(meta.modes.map((m: any) => [m.key, `${meta.figmaId}/${m.key}`]));
    const walk = (node: any, path: string[]) => {
      if (node && typeof node === 'object') {
        if (node.$variable_metadata) {
          raw.push({ col: meta.figmaId, ref: `{${colKey}.${path.join('.')}}`, node, modeKeys });
          return;
        }
        for (const [k, v] of Object.entries(node)) if (k !== '$collection_metadata') walk(v, [...path, k]);
      }
    };
    walk(body, []);
  }

  const refToId = new Map(raw.map((r) => [r.ref, r.node.$variable_metadata.figmaId as string]));
  const variables: SnapVariable[] = raw.map(({ col, node, modeKeys }) => {
    const meta = node.$variable_metadata;
    const values: Record<string, ModeValue> = {};
    for (const [k, val] of Object.entries<any>(meta.modes)) {
      const id = modeKeys[k];
      if (typeof val === 'string' && val.startsWith('{')) values[id] = { kind: 'alias', id: refToId.get(val) ?? val };
      else if (typeof val === 'string' && val.startsWith('rgba')) values[id] = { kind: 'value', value: parseColor(val)! };
      else values[id] = { kind: 'value', value: val };
    }
    return {
      id: meta.figmaId, name: meta.name, collectionId: col,
      type: node.$type === 'color' ? 'COLOR' : 'FLOAT',
      scopes: [], hidden: false, description: node.$description ?? '', remote: false, values,
    };
  });
  cache = { collections, variables, styles: [{ id: 's1', name: 'typography/action/button/m', kind: 'TEXT' }] };
  return cache;
}
