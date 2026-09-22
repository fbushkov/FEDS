import type { Analysis } from './analyze';
import type { ApplyReport, DiffResult, Preset } from './types';

const STATUS: Record<string, string> = {
  add: 'добавится', same: 'есть, совпадает', changed: 'есть, отличается', extra: 'лишний', blocked: 'заблокирован',
};

/** Таблица токенов для контракта (F5): токен → L2 → значение light/dark. */
export function tokensTable(preset: Preset, values: (name: string, mode: 'light' | 'dark') => string): string {
  const lines = [
    `# Токены: ${preset.title ?? preset.component}`, '',
    'Три уровня: `3. Components` → `2. General` (light / dark) → `1. Primitives`. Значения — из текущего файла Figma.', '',
    `## Уровень 3 · \`3. Components\` (${preset.l3.length})`, '',
    '| Токен L3 | Ссылка L2 | light | dark |', '|---|---|---|---|',
    ...preset.l3.map((t) => `| \`${t.name}\` | \`${t.alias}\` | ${values(t.alias, 'light')} | ${values(t.alias, 'dark')} |`),
    '',
  ];
  if (preset.l2?.length) {
    lines.push(`## Уровень 2 компонента · \`2. General\` (${preset.l2.length})`, '',
      '| Токен L2 | light → L1 | dark → L1 |', '|---|---|---|',
      ...preset.l2.map((t) => `| \`${t.name}\` | \`${t.values.light}\` | \`${t.values.dark}\` |`), '');
  }
  if (preset.exceptions?.length) {
    lines.push('### Исключения', '', ...preset.exceptions.map((e) => `- \`${e.token}\` — ${e.reason}`), '');
  }
  return lines.join('\n');
}

export function diffMarkdown(d: DiffResult): string {
  const lines = [`# Дифф токенов: ${d.component}`, ''];
  if (d.errors.length) lines.push('## Ошибки', '', ...d.errors.map((e) => `- ${e}`), '');
  if (d.warnings.length) lines.push('## Предупреждения', '', ...d.warnings.map((e) => `- ${e}`), '');
  lines.push('| Уровень | Имя | Статус | Сейчас | Будет |', '|---|---|---|---|---|');
  for (const r of d.rows) {
    lines.push(`| ${r.level === 'style' ? 'стиль' : 'L' + r.level} | \`${r.name}\` | ${STATUS[r.status]} | ${r.current ?? ''} | ${r.target ?? ''} |`);
  }
  return lines.join('\n') + '\n';
}

export function applyMarkdown(r: ApplyReport): string {
  const sec = (t: string, xs: string[]) => (xs.length ? [`## ${t} (${xs.length})`, '', ...xs.map((x) => `- \`${x}\``), ''] : []);
  return [
    `# Отчёт FEDS: ${r.component}`, '',
    ...sec('Создано', r.created), ...sec('Изменено', r.updated), ...sec('Удалено', r.removed),
    ...sec('Стили', r.styles), ...sec('Пропущено (уже есть)', r.skipped),
    ...sec('Предупреждения', r.warnings), ...sec('Ошибки', r.errors),
  ].join('\n');
}

export function analysisMarkdown(a: Analysis): string {
  const lines = ['# Анализ системы (FEDS)', '', '| Коллекция | Уровень | Режимы | Переменных |', '|---|---|---|---|'];
  for (const c of a.collections) lines.push(`| ${c.name} | ${c.level} | ${c.modes.join(', ')} | ${c.count} |`);
  lines.push('', `Текстовых стилей: ${a.textStyles} · эффект-стилей: ${a.effectStyles}`, '');
  lines.push(`Компоненты в L3: ${a.componentRoots.map((r) => `${r.root} (${r.count})`).join(', ')}`, '');
  lines.push(`Пары inverse-*: ${a.inversePairs.pairs}, без пары: ${a.inversePairs.orphans.length}`, '');
  for (const i of a.issues) {
    lines.push(`## ${i.title}: ${i.items.length}`, '', ...i.items.slice(0, 200).map((x) => `- \`${x}\``), '');
  }
  return lines.join('\n');
}
