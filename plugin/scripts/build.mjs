// Сборка плагина: dist/code.js (main) и dist/ui.html (UI со встроенными скриптом и стилями).
import * as esbuild from 'esbuild';
import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const watch = process.argv.includes('--watch');
mkdirSync(join(root, 'dist'), { recursive: true });

const common = { bundle: true, target: 'es2017', logLevel: 'info', minify: !watch };

async function buildUi() {
  const js = await esbuild.build({ ...common, entryPoints: [join(root, 'src/ui/ui.ts')], write: false });
  const css = readFileSync(join(root, 'src/ui/ui.css'), 'utf-8');
  const html = readFileSync(join(root, 'src/ui/ui.html'), 'utf-8')
    .replace('/*__CSS__*/', () => css)
    .replace('/*__JS__*/', () => js.outputFiles[0].text.replace(/<\/script/g, '<\\/script'));
  writeFileSync(join(root, 'dist/ui.html'), html);
}

const mainOpts = { ...common, entryPoints: [join(root, 'src/main.ts')], outfile: join(root, 'dist/code.js') };

if (watch) {
  const ctx = await esbuild.context(mainOpts);
  await ctx.watch();
  const uiCtx = await esbuild.context({
    ...common, entryPoints: [join(root, 'src/ui/ui.ts')], write: false,
    plugins: [{ name: 'ui', setup: (b) => b.onEnd(() => buildUi()) }],
  });
  await uiCtx.watch();
} else {
  await esbuild.build(mainOpts);
  await buildUi();
}
