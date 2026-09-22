import { buildOrder, expandSet, type BuildDef } from '../core/build';
import { buildSet, precheck } from './builder';
import { boundPaint, Library } from './library';
import { renderSpec } from './spec';

export interface BuildReport {
  pages: string[];
  sets: { component: string; name: string; variants: number }[];
  specs: string[];
  warnings: string[];
  errors: string[];
}

function uniquePageName(base: string): string {
  const names = new Set(figma.root.children.map((p) => p.name));
  if (!names.has(base)) return base;
  let i = 2;
  while (names.has(`${base} (${i})`)) i++;
  return `${base} (${i})`;
}

/**
 * F7 + F6: сборка компонентов и спецификаций. Всё проверяется заранее; при нехватке ресурсов ничего не создаётся.
 * Каждый компонент — на своей новой странице; существующие страницы не меняются. Вся запись — один шаг отмены.
 */
export interface BuildItem { component: string; master: boolean; spec: boolean }

export async function runBuild(all: BuildDef[], picks: BuildItem[],
  progress: (done: number, total: number, label: string) => void): Promise<BuildReport> {
  const report: BuildReport = { pages: [], sets: [], specs: [], warnings: [], errors: [] };
  const lib = new Library();
  await lib.init();
  const pickOf = new Map(picks.map((p) => [p.component, p]));
  const ordered = buildOrder(all.filter((d) => pickOf.has(d.component)));
  const items = ordered.map((def) => ({ def, master: pickOf.get(def.component)!.master, spec: pickOf.get(def.component)!.spec }));
  const building = new Set(items.filter((i) => i.master).flatMap((i) => i.def.sets.map((s) => s.name)));
  const pre = await precheck(lib, items, building);
  if (pre.errors.length) {
    report.errors = pre.errors;
    return report;
  }
  report.warnings.push(...pre.warnings);

  const total = items.filter((i) => i.master).reduce((n, i) => n + i.def.sets.reduce((m, s) => m + expandSet(s).length, 0), 0);
  let done = 0;
  const warnings = new Set<string>();
  const tick = () => { done++; if (done % 12 === 0 || done === total) progress(done, total, 'варианты'); };

  figma.commitUndo();
  for (const { def, master: withMaster, spec: withSpec } of items) {
    const opts = { master: withMaster, spec: withSpec };
    const page = figma.createPage();
    page.name = uniquePageName(opts.master ? def.page ?? `Components / ${def.title}` : `${def.page ?? def.title} — спецификация`);
    report.pages.push(page.name);
    await figma.setCurrentPageAsync(page);

    let right = 0;
    if (opts.master) {
      const master = figma.createFrame();
      master.name = `${def.title}. Мастер`;
      master.layoutMode = 'HORIZONTAL';
      master.itemSpacing = 80;
      master.paddingTop = master.paddingBottom = master.paddingLeft = master.paddingRight = 100;
      master.layoutSizingHorizontal = 'HUG';
      master.layoutSizingVertical = 'HUG';
      const bg = await boundPaint(lib, 'color/bg/page/inverse-main');
      master.fills = bg ? [bg] : [];
      page.appendChild(master);
      for (const set of def.sets) {
        const wrap = figma.createFrame();
        wrap.name = set.name;
        wrap.layoutMode = 'VERTICAL';
        wrap.itemSpacing = 40;
        wrap.paddingTop = wrap.paddingBottom = wrap.paddingLeft = wrap.paddingRight = 40;
        wrap.cornerRadius = 16;
        const wb = await boundPaint(lib, 'color/bg/section/inverse-secondary');
        wrap.fills = wb ? [wb] : [];
        master.appendChild(wrap);
        wrap.layoutSizingHorizontal = 'HUG';
        wrap.layoutSizingVertical = 'HUG';
        const title = figma.createText();
        const st = await lib.textStyle('typography/section/title');
        if (st) await title.setTextStyleIdAsync(st.id);
        else { await lib.font({ family: 'Roboto', style: 'Regular' }); title.fontName = { family: 'Roboto', style: 'Regular' }; }
        title.characters = set.name;
        const tf = await boundPaint(lib, 'color/static/text/base/inverse-hard');
        title.fills = tf ? [tf] : [];
        wrap.appendChild(title);
        const s = await buildSet(lib, set, wrap, warnings, tick);
        report.sets.push({ component: def.component, name: s.name, variants: s.type === 'COMPONENT_SET' ? s.children.length : 1 });
      }
      right = master.width + 200;
    }
    if (opts.spec && def.spec) {
      await renderSpec(lib, def.spec, page, right, 0, warnings);
      report.specs.push(def.title);
    }
    figma.viewport.scrollAndZoomIntoView(page.children);
  }
  figma.commitUndo();
  report.warnings.push(...warnings);
  return report;
}
