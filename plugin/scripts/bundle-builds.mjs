// Собирает presets/*.build.json в src/builds.generated.json — описания сборки и спецификации.
import { readdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const dir = join(here, '../../presets');
const builds = readdirSync(dir).filter((f) => f.endsWith('.build.json')).sort()
  .map((f) => JSON.parse(readFileSync(join(dir, f), 'utf-8')));
writeFileSync(join(here, '../src/builds.generated.json'), JSON.stringify(builds));
console.log(`builds: ${builds.length} → src/builds.generated.json (${builds.map((b) => b.component).join(', ')})`);
