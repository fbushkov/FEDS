import { readFileSync, readdirSync } from 'node:fs';
import { join } from 'node:path';
import { describe, expect, it } from 'vitest';
import { buildOrder, collectRefs, expandSet, gridSlots, type BuildDef } from '../src/core/build';
import type { Preset } from '../src/core/types';
import keys from '../src/library-keys.json';

const DIR = join(__dirname, '../../presets');
const load = <T>(f: string): T => JSON.parse(readFileSync(join(DIR, f), 'utf-8'));
const button = load<BuildDef>('button.build.json');
const alert = load<BuildDef>('alert.build.json');
const skeleton = load<BuildDef>('skeleton.build.json');
const ALERT = alert.sets.find((s) => s.name === 'Alert')!;
const PRESETS: Preset[] = readdirSync(DIR).filter((f) => f.endsWith('.tokens.json')).map((f) => load<Preset>(f));
const VARS = new Set(PRESETS.flatMap((p) => [...p.l3, ...(p.l2 ?? [])].map((t) => t.name)));
const STYLES = new Set(PRESETS.flatMap((p) => (p.textStyles ?? []).map((s) => s.name)));

describe('Button: повтор текущей сборки', () => {
  it('6 наборов: типы файла + Inverse у Filled, Outline и Text (для тёмных и насыщенных поверхностей)', () => {
    expect(button.sets.map((s) => [s.name, expandSet(s).length])).toEqual([
      ['Button / Filled', 196], ['Button / Icon - Filled', 196], ['Button / Outline', 196],
      ['Button / Icon - Outline', 196], ['Button / Text', 112], ['Button / Icon Only', 168],
    ]);
    const types = new Set(button.sets.flatMap((s) => s.axes.find((a) => a.name === 'Type')!.values));
    for (const t of ['On-bold', 'On-bright']) expect(types.has(t)).toBe(false);
  });

  it('Inverse: Filled — светлая заливка и тёмный текст, Outline — светлые рамка и текст, Text — светлый текст', () => {
    const at = (i: number) => expandSet(button.sets[i]).find((x) => x.name === 'Size=L, Type=Inverse, State=Default, Loading=False')!.root;
    expect(at(0).fill).toBe('button/fill/inverse/bg/default');
    expect(at(0).children.find((c) => c.name === 'Действие')!.text!.fill).toBe('button/fill/inverse/text/default');
    expect(at(2).stroke!.color).toBe('button/outline/inverse/border/default');
    const text = at(4);
    expect(text.children.find((c) => c.name === 'Действие')!.text!.fill).toBe('button/text-button/inverse/text/default');
    expect(text.children.find((c) => c.name === 'Left Icon')!.icon!.color).toBe('button/text-button/inverse/icon/primary/default');
  });

  it('вариант Filled L Primary Hover Loading устроен как в файле', () => {
    const v = expandSet(button.sets[0]).find((x) => x.name === 'Size=L, Type=Primary, State=Hover, Loading=True')!;
    expect(v.root.children.map((c) => c.name)).toEqual(['Focus Ring', 'Left Icon', 'Действие', 'Right Icon', 'Cancel']);
    expect(v.root.fill).toBe('button/fill/primary/bg/hover');
    expect(v.root.layout?.gap).toBe('button/size/l/gap');
    expect(v.root.children[0].offset).toBe(4);
    expect(v.root.children[1].opacity).toBe(0);
  });

  it('Disabled — без кольца фокуса; Icon Only Inverse — свои токены иконки', () => {
    const d = expandSet(button.sets[0]).find((x) => x.values.State === 'Disabled')!;
    expect(d.root.children.some((c) => c.name === 'Focus Ring')).toBe(false);
    const io = expandSet(button.sets[5]).find((x) => x.name === 'Size=M, Type=Inverse-secondary, State=Default, Loading=False')!;
    expect(io.root.fill).toBe('button/text-button/inverse/bg/default');
    expect(io.root.children.find((c) => c.name === 'Icon')!.icon!.color).toBe('button/text-button/inverse/icon/secondary/default');
  });

  it('сетка: колонки по Type, в блоке 7 строк; Inverse — на тёмной части', () => {
    const s = gridSlots(button.sets[0], expandSet(button.sets[0]));
    expect(Math.max(...[...s.values()].map((x) => x.row))).toBe(6);
    expect([...s.entries()].find(([n]) => n.includes('Type=Inverse,'))![1]).toMatchObject({ half: 1, col: 6 });
    expect(Math.max(...[...s.values()].map((x) => x.col))).toBe(6);
  });
});

describe('Alert: новый компонент по тому же правилу', () => {
  const vs = expandSet(ALERT);
  const v = (n: string) => vs.find((x) => x.name === n)!;
  const find = (r: { name: string; children: unknown[] }, name: string): any => r.name === name ? r : (r.children as typeof r[]).map((c) => find(c, name)).find(Boolean);
  it('48 вариантов: Subtle 16 + Default 16 + Bold 16 (Bold без Inverse, со свёрнутым видом)', () => {
    expect(vs).toHaveLength(48);
    expect(vs.filter((x) => x.values.Appearance === 'Bold' && x.values.Expanded === 'False')).toHaveLength(8);
  });
  it('Subtle Inverse берёт inverse-токены, иконка — по роли, закрытие — Button Icon Only', () => {
    const x = v('Appearance=Subtle, Role=Error, Size=S, Inverse=True, Expanded=True');
    expect(x.root.fill).toBe('alert/bg/inverse-error');
    expect(x.root.children[0].icon).toEqual({ name: 'circle-alert', size: 'alert/size/s/icon', color: 'alert/icon/inverse-error' });
    expect(find(x.root, 'Close').instance?.variant).toEqual({ Size: 'S', Type: 'Inverse-secondary', State: 'Default', Loading: 'False' });
  });
  it('Default (Flag): нейтральная карточка, действия — ссылки, закрывается', () => {
    const x = v('Appearance=Default, Role=Success, Size=M, Inverse=False, Expanded=True');
    expect(x.root.fill).toBe('alert/default/bg');
    expect(find(x.root, 'Action').instance).toMatchObject({ set: 'Button / Text', variant: { Type: 'Primary' } });
    expect(find(x.root, 'Close')).toBeTruthy();
  });
  it('Bold (Flag): заливка роли, светлая тема закреплена, действия — Text Inverse, шеврон — Icon Only Inverse-primary', () => {
    const e = v('Appearance=Bold, Role=Error, Size=M, Inverse=False, Expanded=True');
    expect(e.root.fill).toBe('alert/bold/bg/error');
    expect(e.root.theme).toBe('light');
    expect(find(e.root, 'Close')).toBeUndefined();
    expect(find(e.root, 'Action').instance).toMatchObject({ set: 'Button / Text', variant: { Type: 'Inverse' } });
    expect(find(e.root, 'Expand').instance).toMatchObject({ set: 'Button / Icon Only', variant: { Type: 'Inverse-primary' }, props: { '↳ Icon': 'icon:chevron-up' } });
    const c = v('Appearance=Bold, Role=Warning, Size=M, Inverse=False, Expanded=False');
    expect(find(c.root, 'Description')).toBeUndefined();
    expect(find(c.root, 'Actions')).toBeUndefined();
    // жёлтая заливка: белое не читается — обычные тёмные кнопки
    expect(find(c.root, 'Expand').instance).toMatchObject({ variant: { Type: 'Secondary' }, props: { '↳ Icon': 'icon:chevron-down' } });
    expect(find(v('Appearance=Bold, Role=Warning, Size=M, Inverse=False, Expanded=True').root, 'Action').instance.variant.Type).toBe('Secondary');
    expect(v('Appearance=Subtle, Role=Info, Size=M, Inverse=False, Expanded=True').root.theme).toBeUndefined();
  });
  it('Inverse: действия — кнопки типа Inverse (Outline и Text), своих кнопок у Alert нет', () => {
    const d = v('Appearance=Default, Role=Info, Size=M, Inverse=True, Expanded=True');
    expect(find(d.root, 'Action').instance).toMatchObject({ set: 'Button / Text', variant: { Type: 'Inverse' } });
    const s = v('Appearance=Subtle, Role=Info, Size=M, Inverse=True, Expanded=True');
    expect(find(s.root, 'Action').instance).toMatchObject({ set: 'Button / Outline', variant: { Type: 'Inverse' } });
    expect(find(s.root, 'Second Action').instance).toMatchObject({ set: 'Button / Text', variant: { Type: 'Inverse' } });
    expect(alert.sets.map((x) => x.name)).toEqual(['Alert']);
  });
});

describe('все ссылки схем существуют', () => {
  // все описания сборки из presets/ — новый компонент попадает в проверку автоматически
  const ALL = readdirSync(DIR).filter((f) => f.endsWith('.build.json')).map((f) => load<BuildDef>(f));
  const allSets = new Set(ALL.flatMap((d) => d.sets.map((s) => s.name)));
  for (const def of ALL) {
    const refs = collectRefs(def);
    const exc = new Set((def.exceptions ?? []).map((e) => e.token));
    it(`${def.component}: переменные есть в пресетах`, () => expect([...refs.variables].filter((v) => !VARS.has(v) && !exc.has(v))).toEqual([]));
    it(`${def.component}: стили есть в пресетах`, () => expect([...refs.styles].filter((s) => !STYLES.has(s))).toEqual([]));
    it(`${def.component}: иконки есть в ключах библиотеки`, () => expect([...refs.icons].filter((i) => !(i in keys.icons))).toEqual([]));
    it(`${def.component}: вложенные наборы собираются этим плагином`, () => expect([...refs.sets].filter((s) => !allSets.has(s))).toEqual([]));
  }
  it('Alert собирается после Button', () => {
    expect(buildOrder([alert, button, skeleton]).map((d) => d.component)).toEqual(['button', 'alert', 'skeleton']);
  });
});

describe('раскладка и вложенные экземпляры', () => {
  it('Alert: инверсные варианты — правая половина (колонки 2–3), блоки по Appearance', () => {
    const vs = expandSet(ALERT);
    const s = gridSlots(ALERT, vs);
    const inv = vs.filter((v) => v.values.Inverse === 'True').map((v) => s.get(v.name)!);
    expect(new Set(inv.map((x) => x.half))).toEqual(new Set([1]));
    expect(Math.min(...inv.map((x) => x.col))).toBe(2);
    expect(Math.max(...[...s.values()].map((x) => x.block))).toBe(2);
  });
  it('Button / Icon Only: инверсные типы — на тёмной части, порядок колонок как в файле', () => {
    const set = button.sets[5];
    const s = gridSlots(set, expandSet(set));
    const byType = (t: string) => [...s.entries()].find(([n]) => n.includes(`Type=${t},`))![1];
    expect(byType('Inverse-primary')).toMatchObject({ half: 1, col: 4 });
    expect(byType('Danger')).toMatchObject({ half: 0, col: 3 });
  });
  it('Alert: наружу открыты только Action и Second Action, закрытие статично', () => {
    const v = expandSet(ALERT)[0];
    const names: string[] = [];
    const walk = (n: { name: string; expose?: boolean; children: unknown[] }) => { if (n.expose) names.push(n.name); (n.children as typeof n[]).forEach(walk); };
    walk(v.root);
    expect([...new Set(names)]).toEqual(['Action', 'Second Action']);
  });
});

describe('Skeleton и правило загрузки', () => {
  it('3 набора: Line 8, Circle 10, Block 12', () => {
    expect(skeleton.sets.map((s) => [s.name, expandSet(s).length])).toEqual([['Skeleton / Line', 8], ['Skeleton / Circle', 10], ['Skeleton / Block', 12]]);
  });
  it('инверсия — отдельная правая половина, цвет через inverse-bg', () => {
    const set = skeleton.sets[0];
    const vs = expandSet(set);
    const inv = vs.find((v) => v.name === 'Size=M, Inverse=True')!;
    expect(inv.root.fill).toBe('skeleton/shape/inverse-bg');
    expect(gridSlots(set, vs).get(inv.name)).toMatchObject({ half: 1, col: 5 });
  });
  it('у Alert нет своих состояний и загрузки; типографика — переменные, без стилей', () => {
    expect(ALERT.axes.map((a) => a.name)).toEqual(['Appearance', 'Role', 'Size', 'Inverse', 'Expanded']);
    const refs = collectRefs(alert);
    expect([...refs.styles]).toEqual([]);
    expect(refs.variables.has('typography/alert/m/title/weight')).toBe(true);
  });
});

describe('Семейство Select: один публикуемый набор, Field — режим', () => {
  const select = load<BuildDef>('select.build.json');
  const fam = select.sets.find((s) => s.name === 'Select')!;
  const vs = expandSet(fam);
  const find = (r: { name: string; children: unknown[] }, name: string): any => r.name === name ? r : (r.children as typeof r[]).map((c) => find(c, name)).find(Boolean);
  it('публикуется только Select; контрол, список и пункты — приватные части', () => {
    expect(select.sets.filter((s) => !s.name.startsWith('_ ')).map((s) => s.name)).toEqual(['Select']);
    expect(select.sets.some((s) => s.name.startsWith('Field'))).toBe(false);
  });
  it('144 варианта: Field × Type × Size × Open × Inverse', () => expect(vs).toHaveLength(144));
  it('Field = None — только контрол; Vertical — столбец; Horizontal — Label слева', () => {
    const none = vs.find((v) => v.name === 'Field=None, Type=Base, Size=M, Open=False, Inverse=False')!;
    expect(find(none.root, 'Label')).toBeUndefined();
    expect(find(none.root, 'Description')).toBeUndefined();
    const h = vs.find((v) => v.name === 'Field=Horizontal, Type=Error, Size=M, Open=False, Inverse=False')!;
    expect(h.root.layout?.dir).toBe('H');
    expect(find(h.root, 'Label').width).toBe('field/size/label/m/horizontal');
    expect(find(h.root, 'Error')).toBeTruthy();
    expect(vs.find((v) => v.name.startsWith('Field=Vertical'))!.root.layout?.dir).toBe('V');
  });
  it('список показывается только при Open, контрол и список открыты наружу', () => {
    const open = vs.find((v) => v.name === 'Field=None, Type=Base, Size=M, Open=True, Inverse=False')!;
    expect(find(open.root, 'Dropdown').instance).toMatchObject({ set: '_ Select / Dropdown / M', variant: { State: 'Default' } });
    expect(find(open.root, 'Select').expose && find(open.root, 'Dropdown').expose).toBe(true);
    const closed = vs.find((v) => v.name === 'Field=None, Type=Base, Size=M, Open=False, Inverse=False')!;
    expect(find(closed.root, 'Dropdown')).toBeUndefined();
  });
  it('список: тень на переменных effects/select, пустой и загрузка', () => {
    const dd = expandSet(select.sets.find((s) => s.name === '_ Select / Dropdown / M')!);
    expect(dd.map((v) => v.values.State)).toEqual(['Default', 'Default', 'Empty', 'Empty', 'Loading', 'Loading']);
    expect(dd[0].root.shadow).toMatchObject({ blur: 'effects/select/blur/m', y: 'effects/select/y/m' });
  });
});

describe('Select: список в состояниях Empty и Loading', () => {
  const select = load<BuildDef>('select.build.json');
  const dd = select.sets.find((s) => s.name === '_ Select / Dropdown / M')!;
  const at = (state: string) => expandSet(dd).find((v) => v.values.State === state && v.values.Inverse === 'False')!.root;
  it('панель своей высоты, подсказка и загрузка по центру; у списка высота по пунктам', () => {
    for (const st of ['Empty', 'Loading']) {
      expect(at(st).height).toBe('field/size/select/m/dropdown-box/empty-height');
      expect(at(st).layout).toMatchObject({ align: 'CENTER', counter: 'CENTER' });
    }
    expect(at('Default').height).toBeUndefined();
    expect(at('Default').layout).toMatchObject({ align: 'MIN', counter: 'MIN' });
  });
});
