// Собирает presets/*.tokens.json в src/presets.generated.json — каталог, встроенный в плагин.
import { readdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const dir = join(here, '../../presets');
const out = join(here, '../src/presets.generated.json');

const files = readdirSync(dir).filter((f) => f.endsWith('.tokens.json')).sort();
const presets = files.map((f) => JSON.parse(readFileSync(join(dir, f), 'utf-8')));
writeFileSync(out, JSON.stringify(presets));
console.log(`presets: ${presets.length} → src/presets.generated.json (${presets.map((p) => p.component).join(', ') || 'пусто'})`);
