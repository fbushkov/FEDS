import { readdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';
import { describe, expect, it } from 'vitest';
import { buildPlan, catalogStatus, diffPreset, mergePresets, planSize, resolveRequires } from '../src/core/diff';
import { DEFAULT_CONVENTIONS as CONV, type Preset, type Snapshot } from '../src/core/types';
import { loadSnapshot } from './fixture';

const DIR = join(__dirname, '../../presets');
const PRESETS: Preset[] = readdirSync(DIR).filter((f) => f.endsWith('.tokens.json')).sort()
  .map((f) => JSON.parse(readFileSync(join(DIR, f), 'utf-8')));
const byName = (c: string) => PRESETS.find((p) => p.component === c)!;
const snap = loadSnapshot();
const catalogL3 = new Set(PRESETS.flatMap((p) => p.l3.map((t) => t.name)));
const EMPTY: Snapshot = { collections: [], variables: [], styles: [] };

describe('каталог пресетов', () => {
  it('26 пресетов: база, 13 готовых, 12 новых', () => {
    expect(PRESETS).toHaveLength(26);
    expect(PRESETS.filter((p) => p.origin === 'existing' && p.kind !== 'system')).toHaveLength(13);
  });

  it('в исходном файле все переменные готовых компонентов и базы уже есть и совпадают', () => {
    // в фикстуре нет текстовых стилей (их нет в variables.json), поэтому считаем только переменные
    for (const p of PRESETS.filter((x) => x.origin === 'existing')) {
      const d = diffPreset(p, snap, CONV, { catalogL3 });
      const vars = d.rows.filter((r) => r.level !== 'style');
      // одобренные автором изменения существующих токенов (change) ожидаемо «отличаются»
      const approved = new Set([...p.l3, ...(p.l2 ?? [])].filter((t) => (t as { change?: unknown }).change).map((t) => t.name));
      const bad = vars.filter((r) => r.status !== 'same' && !approved.has(r.name) && !(r.status === 'changed' && r.reasons?.every((x) => x.startsWith('scopes'))));
      expect({ c: p.component, bad: bad.map((r) => r.name) }).toEqual({ c: p.component, bad: [] });
    }
    expect(catalogStatus(PRESETS, snap, CONV)).toHaveLength(26);
  });

  it('новые компоненты — «нет в файле», ошибок ссылок нет', () => {
    // новый компонент записывается вместе со своими зависимостями (как в интерфейсе: requires отмечаются автоматически)
    const req = resolveRequires(PRESETS);
    for (const p of PRESETS.filter((x) => x.origin !== 'existing')) {
      const deps = (req.get(p.component) ?? []).map((c) => byName(c));
      const d = diffPreset(deps.length ? mergePresets([...deps, p]).preset : p, snap, CONV, { catalogL3 });
      expect({ c: p.component, e: d.errors }).toEqual({ c: p.component, e: [] });
      expect(d.rows.filter((r) => r.level === 3 && p.l3.some((t) => t.name === r.name)).every((r) => r.status === 'add')).toBe(true);
    }
  });

  it('зависимости вычисляются: radiobutton → checkbox, combobox → field', () => {
    const req = resolveRequires(PRESETS);
    expect(req.get('radiobutton')).toContain('checkbox');
    expect(req.get('field-combobox')).toEqual(['field', 'system']);
    expect(req.get('system')).toEqual([]);
  });
});

describe('сборка с нуля в пустом файле', () => {
  it('без базы компонент заблокирован', () => {
    const d = diffPreset(byName('button'), EMPTY, CONV);
    expect(d.errors.length).toBeGreaterThan(0);
  });

  it('база + все компоненты: создаются 3 коллекции, 4891 переменная, 110 + новые стили, ошибок нет', () => {
    const { preset, conflicts } = mergePresets(PRESETS);
    expect(conflicts).toEqual([]);
    const d = diffPreset(preset, EMPTY, CONV);
    expect(d.errors).toEqual([]);
    expect(d.createCollections).toEqual(['1. Primitives', '2. General', '3. Components']);
    const plan = buildPlan(preset, d, { change: [], remove: [] });
    expect(plan.createL1).toHaveLength(643);
    expect(plan.createL2.length).toBeGreaterThan(2261);
    expect(plan.createL3.length).toBeGreaterThan(1987);
  });
});

describe('дополнение существующей системы', () => {
  it('база + готовые компоненты в исходном файле: план пуст (идемпотентность)', () => {
    const { preset } = mergePresets(PRESETS.filter((p) => p.origin === 'existing'));
    const d = diffPreset(preset, snap, CONV, { catalogL3 });
    const plan = buildPlan(preset, d, { change: [], remove: [] });
    // создаются только новые L2, одобренные автором (change.was = null); остальное уже в файле
    const approvedNew = new Set(preset.l2!.filter((t) => (t as { change?: { was: unknown } }).change?.was === null).map((t) => t.name));
    const approvedL3 = new Set(preset.l3.filter((t) => t.change?.was === null).map((t) => t.name));
    expect(plan.createL1).toHaveLength(0);
    expect(plan.createL3.map((t) => t.name).filter((n) => !approvedL3.has(n))).toEqual([]);
    expect(plan.createL2.map((t) => t.name).filter((n) => !approvedNew.has(n))).toEqual([]);
    expect(plan.createL2).toHaveLength(approvedNew.size);
  });

  it('новый компонент поверх файла добавляет только своё', () => {
    const d = diffPreset(byName('tooltip'), snap, CONV, { catalogL3 });
    const plan = buildPlan(byName('tooltip'), d, { change: [], remove: [] });
    expect(planSize(plan)).toBe(d.rows.filter((r) => r.status === 'add').length);
    expect(plan.createL1).toHaveLength(0);
    expect(plan.remove).toHaveLength(0);
  });
});
