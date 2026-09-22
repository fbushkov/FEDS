import { analyze } from './core/analyze';
import { expandSet, type BuildDef } from './core/build';
import { rgbaToHex } from './core/color';
import { buildPlan, catalogStatus, diffPreset, mergePresets, planSize, resolveRequires } from './core/diff';
import { analysisMarkdown, applyMarkdown, diffMarkdown, tokensTable } from './core/markdown';
import { SnapIndex, isColor } from './core/snapshot';
import { DEFAULT_CONVENTIONS, type Conventions, type Preset } from './core/types';
import { applyPlan } from './figma/apply';
import { runBuild } from './figma/run-build';
import { takeSnapshot } from './figma/scan';
import type { BuildMeta, DocMeta, ExportFile, ToMain, ToUI } from './messages';
import buildsRaw from './builds.generated.json';
import docsRaw from './docs.generated.json';
import presetsRaw from './presets.generated.json';

const VERSION = '0.3.7';
const STORAGE_KEY = 'feds.conventions';

const DOCS = docsRaw as (DocMeta & { content: string })[];
const PRESETS = presetsRaw as Preset[];
const BUILDS = buildsRaw as unknown as BuildDef[];
const BUILD_META: BuildMeta[] = BUILDS.map((b) => ({
  component: b.component, title: b.title, origin: b.origin, page: b.page, requires: b.requires ?? [], notes: b.notes ?? [],
  sets: b.sets.map((s) => ({ name: s.name, variants: expandSet(s).length })), specColumns: (b.spec?.columns ?? []).map((c) => c.title),
}));
const REQUIRES = resolveRequires(PRESETS);
for (const p of PRESETS) p.requires = [...new Set([...(REQUIRES.get(p.component) ?? []), ...(p.includes ?? [])])];

figma.showUI(__html__, { width: 720, height: 760, themeColors: true, title: 'FEDS' });

const post = (msg: ToUI) => figma.ui.postMessage(msg);

async function conventions(): Promise<Conventions> {
  const saved = (await figma.clientStorage.getAsync(STORAGE_KEY)) as Conventions | undefined;
  return saved ? { ...DEFAULT_CONVENTIONS, ...saved } : DEFAULT_CONVENTIONS;
}

function show(v: unknown): string {
  return isColor(v) ? rgbaToHex(v) : String(v);
}

/** Значение L2/L1 для таблицы токенов: из файла, иначе из пресета (через примитив файла). */
function valueFor(ix: SnapIndex, conv: Conventions, preset: Preset, name: string, mode: 'light' | 'dark'): string {
  const modeName = mode === 'light' ? conv.modes.light : conv.modes.dark;
  const v = ix.get(2, name) ?? ix.get(1, name);
  if (v) {
    const r = ix.resolve(v, modeName);
    return r?.kind === 'value' ? show(r.value) : '—';
  }
  const l2 = preset.l2?.find((t) => t.name === name);
  if (l2) {
    const val = l2.values[mode];
    if (typeof val === 'number') return String(val);
    const p = ix.get(1, val);
    const r = p ? ix.resolve(p, modeName) : undefined;
    return r?.kind === 'value' ? `${show(r.value)} (${val})` : val;
  }
  return '—';
}

const catalogL3 = () => new Set(PRESETS.flatMap((p) => p.l3.map((t) => t.name)));

function merged(list: Preset[]) {
  const { preset, conflicts } = mergePresets(list);
  return { preset, conflicts };
}

function docsFiles(ix: SnapIndex, conv: Conventions, docIds: string[], tokenComponents: string[], extra: Preset[]): ExportFile[] {
  const byComp = new Map([...PRESETS, ...extra].map((p) => [p.component, p]));
  const groupName = (g: string) => (g === 'new' ? 'Новые компоненты' : 'Готовые компоненты');
  const files: ExportFile[] = [];
  const index: string[] = ['# Документация FEDS', '', `Файл: ${figma.root.name} · выгрузка ${new Date().toLocaleString('ru-RU')}`, ''];
  for (const id of docIds) {
    const d = DOCS.find((x) => x.id === id);
    if (!d) continue;
    const p = byComp.get(d.component);
    const folder = `${groupName(d.group)}/${p?.title ?? d.component}`;
    files.push({ name: `${folder}/${d.id}.md`, content: d.content });
    index.push(`- [${d.title}](${encodeURI(`${folder}/${d.id}.md`)}) — \`${d.component}\``);
  }
  for (const c of tokenComponents) {
    const p = byComp.get(c);
    if (!p || !p.l3.length) continue;
    const doc = DOCS.find((x) => x.component === c);
    const folder = `${groupName(doc?.group ?? p.origin ?? 'new')}/${p.title ?? c}`;
    const md = tokensTable(p, (name, mode) => valueFor(ix, conv, p, name, mode));
    files.push({ name: `${folder}/${c}-tokens.md`, content: md });
    index.push(`- [Токены: ${p.title ?? c}](${encodeURI(`${folder}/${c}-tokens.md`)})`);
  }
  files.unshift({ name: 'README.md', content: index.join('\n') + '\n' });
  return files;
}

figma.ui.onmessage = async (msg: ToMain) => {
  try {
    const conv = await conventions();
    switch (msg.type) {
      case 'init':
        post({
          type: 'init', presets: PRESETS, docs: DOCS.map(({ content, ...meta }) => meta), builds: BUILD_META,
          conventions: conv, fileName: figma.root.name, version: VERSION,
        });
        break;
      case 'analyze': {
        const a = analyze(await takeSnapshot(), conv);
        post({ type: 'analysis', analysis: a, markdown: analysisMarkdown(a) });
        break;
      }
      case 'catalog':
        post({ type: 'catalog', statuses: catalogStatus(PRESETS, await takeSnapshot(), conv) });
        break;
      case 'diff': {
        const { preset, conflicts } = merged(msg.presets);
        const d = diffPreset(preset, await takeSnapshot(), conv, { catalogL3: catalogL3() });
        d.errors.unshift(...conflicts);
        post({ type: 'diff', diff: d, markdown: diffMarkdown(d) });
        break;
      }
      case 'apply': {
        const { preset, conflicts } = merged(msg.presets);
        const d = diffPreset(preset, await takeSnapshot(), conv, { catalogL3: catalogL3() });
        if (conflicts.length || d.errors.length) {
          post({ type: 'error', message: 'Запись остановлена: в диффе есть ошибки. Исправьте пресет или добавьте зависимости.' });
          break;
        }
        const plan = buildPlan(preset, d, msg.approvals);
        if (!planSize(plan) && !plan.createCollections.length) {
          post({ type: 'error', message: 'Нечего записывать: всё уже есть в файле.' });
          break;
        }
        const report = await applyPlan(plan, conv, (done, total, label) => post({ type: 'progress', done, total, label }));
        post({ type: 'applied', report, markdown: applyMarkdown(report) });
        break;
      }
      case 'docs-export': {
        const ix = new SnapIndex(await takeSnapshot(), conv);
        post({ type: 'docs', files: docsFiles(ix, conv, msg.docIds, msg.tokenComponents, msg.extra) });
        break;
      }
      case 'build': {
        const report = await runBuild(BUILDS, msg.items, (done, total, label) => post({ type: 'progress', done, total, label }));
        post({ type: 'built', report });
        break;
      }
      case 'save-conventions':
        await figma.clientStorage.setAsync(STORAGE_KEY, msg.conventions);
        break;
      case 'resize':
        figma.ui.resize(Math.max(480, msg.width), Math.max(480, msg.height));
        break;
    }
  } catch (e) {
    post({ type: 'error', message: (e as Error).message ?? String(e) });
  }
};
