// F6: спецификация на живых экземплярах по шаблону готовых спецификаций FEroom (docs/build-rules.md, раздел 3).
import type { SpecCard, SpecColumn, SpecDef, SpecItem } from '../core/build';
import { findVariant, setProps } from './builder';
import { boundPaint, type Library } from './library';

interface Ctx { lib: Library; warnings: Set<string> }

const T = {
  bgFrame: 'color/bg/section/main',
  bgColumn: 'color/bg/section/secondary',
  bgCard: 'color/bg/section/main',
  bgCardInverse: 'color/bg/section/inverse-main',
  textHard: 'color/static/text/base/hard',
  textFirm: 'color/static/text/base/firm',
  textHardInv: 'color/static/text/base/inverse-hard',
  textFirmInv: 'color/static/text/base/inverse-firm',
};

async function fill(ctx: Ctx, name: string): Promise<Paint[]> {
  const p = await boundPaint(ctx.lib, name);
  if (!p) ctx.warnings.add(`спецификация: нет переменной ${name}`);
  return p ? [p] : [];
}

function stack(name: string, dir: 'H' | 'V', gap: number, pad = 0): FrameNode {
  const f = figma.createFrame();
  f.name = name;
  f.layoutMode = dir === 'H' ? 'HORIZONTAL' : 'VERTICAL';
  f.itemSpacing = gap;
  f.paddingTop = f.paddingBottom = f.paddingLeft = f.paddingRight = pad;
  f.fills = [];
  f.clipsContent = false;
  f.layoutSizingHorizontal = 'HUG';
  f.layoutSizingVertical = 'HUG';
  return f;
}

async function text(ctx: Ctx, chars: string, style: string, color: string, width?: number): Promise<TextNode> {
  const t = figma.createText();
  const s = await ctx.lib.textStyle(style);
  if (s) await t.setTextStyleIdAsync(s.id);
  else {
    await ctx.lib.font({ family: 'Roboto', style: 'Regular' });
    t.fontName = { family: 'Roboto', style: 'Regular' };
    ctx.warnings.add(`спецификация: нет стиля ${style}`);
  }
  t.characters = chars;
  t.fills = await fill(ctx, color);
  if (width) {
    t.resize(width, t.height);
    t.textAutoResize = 'HEIGHT';
  }
  return t;
}

async function instanceOf(ctx: Ctx, it: SpecItem): Promise<SceneNode | null> {
  const set = await ctx.lib.set(it.set);
  const comp = set ? findVariant(set, it.variant) : null;
  if (!comp) {
    ctx.warnings.add(`спецификация: нет варианта ${it.set} / ${JSON.stringify(it.variant)}`);
    return null;
  }
  const inst = comp.createInstance();
  if (it.props) await setProps(ctx.lib, inst, it.props);
  for (const [name, props] of Object.entries(it.nested ?? {})) {
    const nested = inst.exposedInstances.find((x) => x.name === name);
    if (nested) await setProps(ctx.lib, nested, props);
    else ctx.warnings.add(`спецификация: у ${it.set} нет открытого экземпляра ${name}`);
  }
  if (it.width) {
    inst.resize(it.width, inst.height);
    // подпись в фиксированной ширине должна обрезаться, а не вылезать
    for (const t of inst.findAll((n) => n.type === 'TEXT') as TextNode[]) {
      if (t.textTruncation === 'ENDING' && t.parent === inst) t.layoutSizingHorizontal = 'FILL';
    }
    if (inst.layoutMode !== 'NONE') inst.layoutSizingVertical = 'HUG';
  }
  return inst;
}

async function card(ctx: Ctx, c: SpecCard, width?: number): Promise<FrameNode> {
  const inv = !!c.inverse;
  const f = stack(c.title ?? 'Card', 'V', 32, 32);
  f.fills = await fill(ctx, inv ? T.bgCardInverse : T.bgCard);
  f.cornerRadius = 8;
  if (c.title || c.description) {
    const head = stack('Text', 'V', 16);
    f.appendChild(head);
    if (c.title) head.appendChild(await text(ctx, c.title, 'typography/section/default', inv ? T.textHardInv : T.textHard));
    if (c.description) head.appendChild(await text(ctx, c.description, 'typography/content/body/default', inv ? T.textFirmInv : T.textFirm, width ? width - 64 : 256));
  }
  for (const it of c.items) {
    const inst = await instanceOf(ctx, it);
    if (!inst) continue;
    if (it.label) {
      const row = stack(it.label, 'V', 16);
      row.appendChild(await text(ctx, it.label, 'typography/content/body/default', inv ? T.textFirmInv : T.textHard));
      row.appendChild(inst);
      f.appendChild(row);
    } else f.appendChild(inst);
  }
  if (width) {
    f.resize(width, f.height);
    f.layoutSizingHorizontal = 'FIXED';
    f.layoutSizingVertical = 'HUG';
  }
  return f;
}

async function column(ctx: Ctx, col: SpecColumn): Promise<FrameNode> {
  const f = stack(col.title, 'V', 24, 40);
  f.fills = await fill(ctx, T.bgColumn);
  f.cornerRadius = 8;
  f.appendChild(await text(ctx, col.title, 'typography/section/title', T.textHard));
  if (col.description) f.appendChild(await text(ctx, col.description, 'typography/content/body/default', T.textFirm, (col.width ?? 320)));
  const cardWidth = col.grid ? undefined : col.width ?? 320;
  if (col.grid && col.grid > 1) {
    const grid = stack('Content', 'H', 32);
    const lanes = Array.from({ length: col.grid }, (_, i) => stack(`Lane ${i + 1}`, 'V', 32));
    lanes.forEach((l) => grid.appendChild(l));
    for (let i = 0; i < col.cards.length; i++) lanes[i % col.grid].appendChild(await card(ctx, col.cards[i]));
    f.appendChild(grid);
  } else {
    const list = stack('Content', 'V', 32);
    for (const c of col.cards) list.appendChild(await card(ctx, c, cardWidth));
    f.appendChild(list);
  }
  return f;
}

/** Секция «Спецификация»: белая подложка, разделы-колонки, карточки с живыми экземплярами. */
export async function renderSpec(lib: Library, spec: SpecDef, page: PageNode, x: number, y: number, warnings: Set<string>): Promise<SectionNode> {
  const ctx: Ctx = { lib, warnings };
  const frame = stack('Спецификация', 'V', 40, 80);
  frame.fills = await fill(ctx, T.bgFrame);
  frame.cornerRadius = 24;
  const head = stack('Header', 'V', 16);
  head.appendChild(await text(ctx, spec.title, 'typography/page/title', T.textHard));
  if (spec.description) head.appendChild(await text(ctx, spec.description, 'typography/content/body/default', T.textFirm, 720));
  frame.appendChild(head);
  const content = stack('Content', 'H', 40);
  content.counterAxisAlignItems = 'MIN';
  for (const col of spec.columns) content.appendChild(await column(ctx, col));
  frame.appendChild(content);

  const section = figma.createSection();
  section.name = 'Спецификация';
  page.appendChild(section);
  section.appendChild(frame);
  frame.x = 100;
  frame.y = 100;
  section.resizeWithoutConstraints(frame.width + 200, frame.height + 200);
  section.x = x;
  section.y = y;
  return section;
}
