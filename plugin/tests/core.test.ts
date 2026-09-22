import { describe, expect, it } from 'vitest';
import { analyze } from '../src/core/analyze';
import { buildPlan, diffPreset, planSize } from '../src/core/diff';
import { SnapIndex, ownPrefixes } from '../src/core/snapshot';
import { DEFAULT_CONVENTIONS as CONV, type Preset } from '../src/core/types';
import { loadSnapshot } from './fixture';

const snap = loadSnapshot();

describe('анализ системы (F1)', () => {
  const a = analyze(snap, CONV);
  it('находит три уровня и их размеры', () => {
    expect(a.missing).toEqual([]);
    expect(a.collections.map((c) => [c.name, c.count])).toEqual([
      ['1. Primitives', 643], ['2. General', 2261], ['3. Components', 1987],
    ]);
  });
  it('битых алиасов и ссылок через уровень нет', () => {
    expect(a.issues.find((i) => i.kind === 'broken')!.items).toEqual([]);
    expect(a.issues.find((i) => i.kind === 'skip')!.items).toEqual([]);
  });
  it('видит 12 корней L3 и единственное сырое значение в L2', () => {
    expect(a.componentRoots).toHaveLength(12);
    expect(a.issues.find((i) => i.kind === 'raw')!.items).toEqual(['number (L2)', 'number (L2)']);
  });
});

describe('обратная сборка: пресет из существующих токенов даёт 0 изменений', () => {
  const ix = new SnapIndex(snap, CONV);
  const l3 = ix.all(3).filter((v) => v.name.startsWith('badge/')).map((v) => ({
    name: v.name, type: v.type as 'COLOR' | 'FLOAT', alias: ix.aliasName(v)!, scopes: [] as string[],
  }));
  const preset: Preset = { component: 'badge', l3 };
  const d = diffPreset(preset, snap, CONV);
  it('все 121 токен — «есть, совпадает»', () => {
    expect(d.createCollections).toEqual([]);
    expect(d.errors).toEqual([]);
    expect(d.rows.filter((r) => r.status === 'same')).toHaveLength(121);
    expect(d.rows.filter((r) => r.status !== 'same')).toEqual([]);
  });
  it('план пустой — повторный запуск ничего не создаёт', () => {
    expect(planSize(buildPlan(preset, d, { change: [], remove: [] }))).toBe(0);
  });
});

describe('новый компонент', () => {
  const preset: Preset = {
    component: 'tooltip',
    l2: [
      { name: 'space/tooltip/x', type: 'FLOAT', scopes: ['GAP'], values: { light: 'space/8', dark: 'space/8' } },
      { name: 'size/tooltip/max-width', type: 'FLOAT', scopes: ['WIDTH_HEIGHT'], values: { light: 320, dark: 320 } },
    ],
    l3: [
      { name: 'tooltip/bg', type: 'COLOR', alias: 'color/bg/raised/inverse-main', scopes: ['FRAME_FILL'] },
      { name: 'tooltip/text', type: 'COLOR', alias: 'color/static/text/base/inverse-hard', scopes: ['TEXT_FILL'] },
      { name: 'tooltip/size/x', type: 'FLOAT', alias: 'space/tooltip/x', scopes: ['GAP'] },
      { name: 'tooltip/size/max-width', type: 'FLOAT', alias: 'size/tooltip/max-width', scopes: ['WIDTH_HEIGHT'] },
    ],
    contrast: [{ fg: 'tooltip/text', bg: 'tooltip/bg', kind: 'text' }],
    exceptions: [{ token: 'size/tooltip/max-width', reason: 'нет size/320 в L1' }],
  };

  it('всё добавляется, ошибок нет, контраст считается в обоих режимах', () => {
    const d = diffPreset(preset, snap, CONV);
    expect(d.errors).toEqual([]);
    expect(d.rows.every((r) => r.status === 'add')).toBe(true);
    expect(d.contrast).toHaveLength(2);
    expect(d.contrast.every((c) => c.ratio > 4.5)).toBe(true);
    const plan = buildPlan(preset, d, { change: [], remove: [] });
    expect(plan.createL2).toHaveLength(2);
    expect(plan.createL3).toHaveLength(4);
  });

  it('сырое значение без исключения — ошибка', () => {
    const d = diffPreset({ ...preset, exceptions: [] }, snap, CONV);
    expect(d.errors.some((e) => e.includes('size/tooltip/max-width'))).toBe(true);
  });

  it('алиас на несуществующий L2 блокирует токен', () => {
    const d = diffPreset({ ...preset, l3: [{ name: 'tooltip/x', type: 'COLOR', alias: 'color/nope', scopes: ['FRAME_FILL'] }] }, snap, CONV);
    expect(d.rows[d.rows.length - 1].status).toBe('blocked');
    expect(d.errors).toHaveLength(1);
  });
});

describe('изменения и удаления только по разрешению', () => {
  const preset: Preset = {
    component: 'link',
    l3: [{ name: 'link/focus-ring', type: 'COLOR', alias: 'color/static/border/base/hard', scopes: ['STROKE_COLOR'] }],
  };
  const d = diffPreset(preset, snap, CONV);
  it('отличающийся токен помечен changed, остальные токены link — extra', () => {
    expect(d.rows.find((r) => r.name === 'link/focus-ring')!.status).toBe('changed');
    expect(d.rows.filter((r) => r.status === 'extra').length).toBe(59);
  });
  it('без разрешения план пустой', () => {
    expect(planSize(buildPlan(preset, d, { change: [], remove: [] }))).toBe(0);
  });
  it('с разрешением попадает в план', () => {
    const p = buildPlan(preset, d, { change: ['link/focus-ring'], remove: ['link/size/m/x'] });
    expect(p.updateL3).toHaveLength(1);
    expect(p.remove.map((r) => r.name)).toEqual(['link/size/m/x']);
  });
});

describe('префиксы семейства field', () => {
  it('field-combobox владеет только своим поддеревом', () => {
    expect(ownPrefixes('field-combobox', ['field'])).toEqual(['field/combobox/', 'field/size/combobox/']);
    expect(ownPrefixes('tooltip')).toEqual(['tooltip/']);
  });
});
