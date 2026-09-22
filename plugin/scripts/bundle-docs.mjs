// Собирает документацию компонентов (input/builds, input/backlog) в src/docs.generated.json.
// Соответствие файла и пресета — в DOCS ниже; новый документ добавляется одной строкой.
import { existsSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const root = join(here, '../..');

// [путь от корня проекта, пресет, группа]
const DOCS = [
  ['input/builds/avatar/avatar-avatar-group.md', 'avatar', 'existing'],
  ['input/builds/badge/badge.md', 'badge', 'existing'],
  ['input/builds/button/button.md', 'button', 'existing'],
  ['input/builds/checkbox/checkboxcheckboxcard.md', 'checkbox', 'existing'],
  ['input/builds/chip/chip.md', 'chip', 'existing'],
  ['input/builds/divider/divider.md', 'divider', 'existing'],
  ['input/builds/field/field.md', 'field', 'existing'],
  ['input/builds/input.md', 'field', 'existing'],
  ['input/builds/text-area.md', 'field', 'existing'],
  ['input/builds/password-input.md', 'field', 'existing'],
  ['input/builds/search-input.md', 'field', 'existing'],
  ['input/builds/link/link.md', 'link', 'existing'],
  ['input/builds/priority-indicator/priority-indicator.md', 'priority-indicator', 'existing'],
  ['input/builds/radiobutton/radiobuttonradiobuttoncard.md', 'radiobutton', 'existing'],
  ['input/builds/simple-select/select.md', 'field-select', 'existing'],
  ['input/builds/status/status.md', 'status', 'existing'],
  ['input/builds/switch/switchtoggle.md', 'switch', 'existing'],
  ['input/builds/number-input.md', 'field-number-input', 'new'],
  ['input/backlog/accordion.md', 'accordion', 'new'],
  ['input/backlog/alert.md', 'alert', 'new'],
  ['input/backlog/banner.md', 'banner', 'new'],
  ['input/backlog/breadcrumbs.md', 'breadcrumbs', 'new'],
  ['input/backlog/combobox.md', 'field-combobox', 'new'],
  ['input/backlog/dropdown.md', 'field-dropdown', 'new'],
  ['input/backlog/hint.md', 'hint', 'new'],
  ['input/backlog/multiselect.md', 'field-multiselect', 'new'],
  ['input/backlog/popover.md', 'popover', 'new'],
  ['input/backlog/skeleton.md', 'skeleton', 'new'],
  ['input/backlog/tooltip.md', 'tooltip', 'new'],
];

function clean(md) {
  // YAML-шапка служебная, в выгрузку не идёт
  return md.replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n/, '').replace(/\r\n/g, '\n').trim() + '\n';
}

const docs = [];
for (const [path, component, group] of DOCS) {
  const full = join(root, path);
  if (!existsSync(full)) {
    console.warn(`docs: нет файла ${path}`);
    continue;
  }
  const content = clean(readFileSync(full, 'utf-8'));
  const title = (content.match(/^#\s+(.+)$/m)?.[1] ?? path.split('/').pop()).trim();
  const id = path.split('/').pop().replace(/\.md$/, '');
  docs.push({ id, title, component, group, source: path, content });
}
writeFileSync(join(here, '../src/docs.generated.json'), JSON.stringify(docs));
console.log(`docs: ${docs.length} → src/docs.generated.json`);
