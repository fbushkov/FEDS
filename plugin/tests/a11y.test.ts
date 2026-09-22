import { readFileSync, readdirSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { describe, expect, it } from 'vitest';
import { checkSet, describeIssue, isInverse, type ColorResolver } from '../src/core/a11y';
import type { BuildDef, SetDef } from '../src/core/build';
import type { Preset, RGBA } from '../src/core/types';

const ROOT = join(__dirname, '../..');
const DIR = join(ROOT, 'presets');
const load = <T>(f: string): T => JSON.parse(readFileSync(join(DIR, f), 'utf-8'));

interface IndexEntry { level: number; name: string; modes: Record<string, string>; targets?: Record<string, string> }
const INDEX: IndexEntry[] = JSON.parse(readFileSync(join(ROOT, 'analysis/token-index.json'), 'utf-8'));
const BY_NAME = new Map(INDEX.map((e) => [e.name, e]));
// алиасы L3 и L2 из пресетов перекрывают индекс библиотеки: так проверяется то, что будет записано
const PRESETS: Preset[] = readdirSync(DIR).filter((f) => f.endsWith('.tokens.json')).map((f) => load<Preset>(f));
const L3 = new Map(PRESETS.flatMap((p) => p.l3.map((t) => [t.name, t.alias] as const)));
const L2 = new Map(PRESETS.flatMap((p) => (p.l2 ?? []).map((t) => [t.name, t.values] as const)));

function parse(s: string): RGBA | null {
  const m = /rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)/.exec(s);
  return m ? { r: +m[1] / 255, g: +m[2] / 255, b: +m[3] / 255, a: m[4] === undefined ? 1 : +m[4] } : null;
}

const resolve: ColorResolver = (name, mode) => {
  const alias = L3.get(name) ?? BY_NAME.get(name)?.targets?.mode_1;
  const key = alias ?? name;
  const preset = L2.get(key) as Record<string, string> | undefined;
  const l2 = BY_NAME.get(key);
  if (!l2 && !preset) return null;
  if (l2?.level === 1) return parse(l2.modes.mode_1);
  const l1 = BY_NAME.get(preset?.[mode] ?? l2?.targets?.[mode] ?? '');
  return l1 ? parse(l1.modes.mode_1) : null;
};

const BUILDS = readdirSync(DIR).filter((f) => f.endsWith('.build.json')).map((f) => load<BuildDef>(f));
// вложенные экземпляры (кнопки в Alert, контрол в Select) проверяются на подложке хозяина
const SETS = new Map(BUILDS.flatMap((d) => d.sets.map((s) => [s.name, s] as const)));
const lookup = (name: string) => SETS.get(name);

// строго: новые наборы, инверсия и тёмная тема у всех; light существующей палитры — в отчёт
// строго везде: обе темы исправлены до порогов WCAG AA (tools/light_theme_fix.py, tools/dark_theme_fix.py)
const isStrict = (_def: BuildDef, _set: SetDef, _values: Record<string, string>, _mode: string) => true;

describe('Доступность собираемых наборов', () => {
  for (const def of BUILDS) {
    for (const set of def.sets) {
      // у повтора существующего компонента строго проверяются новые части (инверсия, расширения);
      // нарушения в исходной палитре уходят в отчёт reports/a11y-contrast.md и чинятся только по решению автора
      it(`${set.name}: контраст WCAG и иконка в цвет текста`, () => {
        const issues = checkSet(set, resolve, lookup).filter((i) => i.kind !== 'unresolved')
          .filter((i) => isStrict(def, set, Object.fromEntries(i.variant.split(', ').map((kv) => kv.split('='))), i.mode));
        expect(issues.map(describeIssue)).toEqual([]);
      });
    }
  }

  it('отчёт по существующей палитре', () => {
    const rows = new Map<string, { worst: number; need: number; where: Set<string> }>();
    for (const def of BUILDS) for (const set of def.sets) for (const i of checkSet(set, resolve, lookup)) {
      if (i.kind !== 'contrast') continue;
      const key = `${i.token} (${i.mode})`;
      const r = rows.get(key) ?? { worst: 99, need: i.need!, where: new Set<string>() };
      r.worst = Math.min(r.worst, i.ratio!);
      r.where.add(set.name);
      rows.set(key, r);
    }
    const lines = [
      '# Контраст: существующая палитра (FEDS)', '',
      'Автопроверка описаний сборки (`plugin/src/core/a11y.ts`): текст ≥ 4.5:1, иконки ≥ 3:1 на фоне варианта, режимы light и dark, Disabled не проверяется (WCAG 1.4.3).',
      'Это токены **существующей** системы: плагин их не меняет без решения автора. Новые компоненты и расширения проверяются строго (тест падает).', '',
      '| Токен (режим) | Худший контраст | Нужно | Наборы |', '|---|---|---|---|',
      ...[...rows.entries()].sort((a, b) => a[1].worst - b[1].worst)
        .map(([k, r]) => `| \`${k}\` | ${r.worst.toFixed(2)} | ${r.need} | ${[...r.where].join(', ')} |`), '',
    ];
    writeFileSync(join(ROOT, 'reports/a11y-contrast.md'), lines.join('\n'));
    expect(rows.size).toBeGreaterThanOrEqual(0);
  });
});

describe('Вложенные кнопки проверяются на подложке хозяина', () => {
  const alertSet = BUILDS.find((d) => d.component === 'alert')!.sets[0];
  const bad = (patch: (s: SetDef) => void) => { const s = JSON.parse(JSON.stringify(alertSet)) as SetDef; patch(s); return checkSet(s, resolve, lookup).filter((i) => i.kind === 'contrast'); };
  it('Inverse на жёлтой заливке Warning Bold не проходит WCAG', () => {
    const issues = bad((s) => { (s.vars!.a1.map as Record<string, string>)['Bold|False|Warning'] = 'Inverse'; });
    expect(issues.some((i) => i.variant.includes('Role=Warning') && i.node.startsWith('Action'))).toBe(true);
  });
  it('без закреплённой светлой темы Text Inverse на заливке Bold не проходит в dark', () => {
    const issues = bad((s) => { delete (s.root as { theme?: unknown }).theme; });
    expect(issues.some((i) => i.mode === 'dark' && i.variant.includes('Appearance=Bold'))).toBe(true);
  });
});
