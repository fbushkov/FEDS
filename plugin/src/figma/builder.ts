// F7: сборка мастер-компонента по описанию presets/{c}.build.json (правило — docs/build-rules.md).
import { collectRefs, expandSet, gridSlots, type BuildDef, type RNode, type RVal, type SetDef } from '../core/build';
import { boundPaint, type Library, type Owner } from './library';
import { PHOTO_PLACEHOLDER } from './placeholder';

type Refs = NonNullable<RNode['refs']>;
interface Ctx { lib: Library; refs: { node: SceneNode; refs: Refs }[]; expose: InstanceNode[]; warnings: Set<string> }

const ALIGN: Record<string, 'MIN' | 'CENTER' | 'MAX' | 'SPACE_BETWEEN'> = { MIN: 'MIN', CENTER: 'CENTER', MAX: 'MAX', SPACE_BETWEEN: 'SPACE_BETWEEN' };

async function num(ctx: Ctx, node: SceneNode, field: VariableBindableNodeField, val: RVal | undefined) {
  if (val === undefined) return;
  if (typeof val === 'number') {
    // ширина и высота экземпляра только для чтения — через resize (иконка числового размера)
    if ((field === 'width' || field === 'height') && 'resize' in node) {
      const n = node as SceneNode & LayoutMixin;
      if (field === 'width') n.resize(val, n.height); else n.resize(n.width, val);
    } else (node as unknown as Record<string, number>)[field] = val;
    return;
  }
  const v = await ctx.lib.variable(val);
  if (!v) {
    ctx.warnings.add(`нет переменной ${val}`);
    return;
  }
  try {
    node.setBoundVariable(field, v);
  } catch (e) {
    // размер по содержимому (HUG) не всегда принимает привязку — фиксируем ось и повторяем
    const l = node as SceneNode & LayoutMixin;
    if (field === 'height' && 'layoutSizingVertical' in l) l.layoutSizingVertical = 'FIXED';
    else if (field === 'width' && 'layoutSizingHorizontal' in l) l.layoutSizingHorizontal = 'FIXED';
    else throw e;
    node.setBoundVariable(field, v);
  }
}

async function radius(ctx: Ctx, node: SceneNode, val: RVal | undefined) {
  for (const f of ['topLeftRadius', 'topRightRadius', 'bottomLeftRadius', 'bottomRightRadius'] as const) await num(ctx, node, f, val);
}

async function paint(ctx: Ctx, name: RVal | undefined): Promise<Paint[]> {
  // пустое значение по оси — слоя краски нет (например, рамка бокса в Loading)
  if (name === undefined || name === '') return [];
  // фото аватара (Type=Photo): встроенная заглушка, дизайнер заменяет её своим изображением
  if (String(name).startsWith('image:')) {
    const img = figma.createImage(figma.base64Decode(PHOTO_PLACEHOLDER));
    return [{ type: 'IMAGE', imageHash: img.hash, scaleMode: 'FILL' }];
  }
  const p = await boundPaint(ctx.lib, String(name));
  if (!p) ctx.warnings.add(`нет переменной ${name}`);
  return p ? [p] : [];
}

async function applyCommon(ctx: Ctx, node: SceneNode, rn: RNode) {
  node.name = rn.name;
  if ('fills' in node && (rn.type === 'frame' || rn.type === 'rect')) (node as GeometryMixin).fills = await paint(ctx, rn.fill);
  if (rn.radius !== undefined) await radius(ctx, node, rn.radius);
  if (rn.stroke && 'strokes' in node) {
    const g = node as GeometryMixin & MinimalStrokesMixin;
    g.strokes = await paint(ctx, rn.stroke.color);
    g.strokeAlign = rn.stroke.align as 'INSIDE' | 'OUTSIDE' | 'CENTER';
    if (rn.stroke.dash) g.dashPattern = rn.stroke.dash;
    for (const f of ['strokeTopWeight', 'strokeBottomWeight', 'strokeLeftWeight', 'strokeRightWeight'] as const) await num(ctx, node, f, rn.stroke.weight);
  }
  if (rn.opacity !== undefined) await num(ctx, node, 'opacity', rn.opacity);
  if (rn.shadow && 'effects' in node) await shadow(ctx, node as BlendMixin, rn.shadow);
  if (rn.visible === false) node.visible = false;
  if (rn.theme) {
    // закреплённая тема (Alert Bold): вложенные кнопки берут значения этой темы при любой теме страницы
    const t = await ctx.lib.theme(rn.theme);
    if (t) node.setExplicitVariableModeForCollection(t.collection, t.modeId);
    else ctx.warnings.add(`нет режима ${rn.theme} у коллекции 2. General`);
  }
  if (rn.refs) ctx.refs.push({ node, refs: rn.refs });
}

/** Тень на переменных (как у списка Select в файле компонентов): каждое поле эффекта привязано к L2. */
async function shadow(ctx: Ctx, node: BlendMixin, s: NonNullable<RNode['shadow']>) {
  let e: Effect = { type: 'DROP_SHADOW', color: { r: 0, g: 0, b: 0, a: 0.12 }, offset: { x: 0, y: 4 }, radius: 8, spread: 0,
    visible: true, blendMode: 'NORMAL', showShadowBehindNode: false } as DropShadowEffect;
  const fields: [VariableBindableEffectField, RVal | undefined][] = [['offsetX', s.x], ['offsetY', s.y], ['radius', s.blur], ['spread', s.spread], ['color', s.color]];
  for (const [field, v] of fields) {
    if (typeof v !== 'string') continue;
    const variable = await ctx.lib.variable(v);
    if (variable) e = figma.variables.setBoundVariableForEffect(e, field, variable);
    else ctx.warnings.add(`нет переменной ${v}`);
  }
  node.effects = [e];
}

async function bindTypography(ctx: Ctx, t: TextNode, base: string, fontStyle = 'Regular') {
  // Прямая привязка к L2 `typography/…` без текстового стиля (решение автора: стили для компонентов не создаём).
  const font = { family: 'Roboto', style: fontStyle };
  try { await ctx.lib.font(font); } catch { await ctx.lib.font({ family: 'Roboto', style: 'Regular' }); font.style = 'Regular'; }
  t.fontName = font;
  const fields: [VariableBindableTextField, string][] = [['fontSize', 'size'], ['lineHeight', 'line-height'], ['letterSpacing', 'letter-spacing'], ['fontWeight', 'weight']];
  for (const [field, suffix] of fields) {
    const v = await ctx.lib.variable(`${base}/${suffix}`);
    if (v) t.setBoundVariable(field, v);
    else ctx.warnings.add(`нет переменной ${base}/${suffix}`);
  }
}

async function makeText(ctx: Ctx, rn: RNode): Promise<TextNode> {
  const t = figma.createText();
  if (rn.text?.typography) {
    await bindTypography(ctx, t, rn.text.typography, rn.text.fontStyle);
  } else {
    const style = rn.text?.style ? await ctx.lib.textStyle(rn.text.style) : null;
    if (style) await t.setTextStyleIdAsync(style.id);
    else if (rn.text?.style) await bindTypography(ctx, t, rn.text.style.replace('/action/', '/'), rn.text.fontStyle);
    else { await ctx.lib.font({ family: 'Roboto', style: 'Regular' }); t.fontName = { family: 'Roboto', style: 'Regular' }; }
  }
  t.characters = rn.text?.chars ?? '';
  t.fills = await paint(ctx, rn.text?.fill);
  if (rn.text?.truncate) {
    t.textAutoResize = 'WIDTH_AND_HEIGHT';
    t.textTruncation = 'ENDING';
    t.maxLines = 1;
  }
  return t;
}

async function makeIcon(ctx: Ctx, rn: RNode): Promise<SceneNode> {
  const comp = await ctx.lib.icon(rn.icon!.name);
  if (!comp) {
    ctx.warnings.add(`нет иконки ${rn.icon!.name}`);
    return figma.createFrame();
  }
  const inst = comp.createInstance();
  if (rn.icon?.size !== undefined) {
    await num(ctx, inst, 'width', rn.icon.size);
    await num(ctx, inst, 'height', rn.icon.size);
  }
  if (rn.icon?.color !== undefined) {
    const vec = inst.findOne((n) => 'fills' in n && Array.isArray(n.fills) && n.fills.length > 0) as GeometryMixin | null;
    if (vec) vec.fills = await paint(ctx, rn.icon.color);
  }
  return inst;
}

export function findVariant(set: Owner, variant: Record<string, string>): ComponentNode | null {
  if (set.type === 'COMPONENT') return set;
  return (set.children as ComponentNode[]).find((c) => Object.entries(variant).every(([k, v]) => c.variantProperties?.[k] === v)) ?? null;
}

/** Свойства экземпляра по коротким именам («Label», «↳ Icon»); значение «icon:x» — подмена на иконку. */
export async function setProps(lib: Library, inst: InstanceNode, props: Record<string, string | boolean>) {
  const defs = inst.componentProperties;
  const out: Record<string, string | boolean> = {};
  for (const [short, val] of Object.entries(props)) {
    const key = Object.keys(defs).find((k) => k.split('#')[0] === short);
    if (!key) continue;
    if (typeof val === 'string' && val.startsWith('icon:')) {
      const c = await lib.icon(val.slice(5));
      // подмена на ту же иконку сбрасывает её цвет и размер в Figma — пропускаем
      if (c && defs[key].value !== c.id) out[key] = c.id;
    } else out[key] = val;
  }
  if (Object.keys(out).length) inst.setProperties(out);
}

async function makeInstance(ctx: Ctx, rn: RNode): Promise<SceneNode> {
  const spec = rn.instance!;
  const set = await ctx.lib.set(spec.set);
  const comp = set ? findVariant(set, spec.variant) : null;
  if (!comp) {
    ctx.warnings.add(`нет варианта ${spec.set} / ${JSON.stringify(spec.variant)}`);
    return figma.createFrame();
  }
  const inst = comp.createInstance();
  await setProps(ctx.lib, inst, spec.props);
  if (rn.expose) ctx.expose.push(inst);
  return inst;
}

/** Узел по развёрнутому шаблону. Корень варианта — ComponentNode. */
async function makeNode(ctx: Ctx, rn: RNode, isRoot = false): Promise<SceneNode> {
  let node: SceneNode;
  switch (rn.type) {
    case 'text': node = await makeText(ctx, rn); break;
    case 'rect': node = figma.createRectangle(); break;
    case 'icon': node = await makeIcon(ctx, rn); break;
    case 'instance': node = await makeInstance(ctx, rn); break;
    default: {
      const f = isRoot ? figma.createComponent() : figma.createFrame();
      f.clipsContent = false;
      if (rn.layout) {
        const l = rn.layout;
        f.layoutMode = l.dir === 'H' ? 'HORIZONTAL' : 'VERTICAL';
        f.primaryAxisAlignItems = ALIGN[l.align] ?? 'MIN';
        f.counterAxisAlignItems = (ALIGN[l.counter] ?? 'MIN') as 'MIN' | 'CENTER' | 'MAX';
        await num(ctx, f, 'itemSpacing', l.gap);
        await num(ctx, f, 'paddingTop', l.pt);
        await num(ctx, f, 'paddingBottom', l.pb);
        await num(ctx, f, 'paddingLeft', l.pl);
        await num(ctx, f, 'paddingRight', l.pr);
      }
      node = f;
    }
  }
  await applyCommon(ctx, node, rn);
  // прямоугольник своего размера (точка Radiobutton): ширина и высота на переменных
  if (rn.type === 'rect' && !rn.abs) {
    if (typeof rn.width === 'number' || typeof rn.height === 'number') (node as RectangleNode).resize(Number(rn.width ?? node.width), Number(rn.height ?? node.height));
    if (typeof rn.width === 'string') await num(ctx, node, 'width', rn.width);
    if (typeof rn.height === 'string') await num(ctx, node, 'height', rn.height);
  }
  // вложенный экземпляр своей ширины (полосы Skeleton в Loading: имя короче описания)
  if (rn.type === 'instance' && typeof rn.width === 'number') (node as InstanceNode).resize(rn.width, (node as InstanceNode).height);

  if (rn.type === 'frame') {
    const f = node as FrameNode;
    const kids: [SceneNode, RNode][] = [];
    for (const c of rn.children) {
      const k = await makeNode(ctx, c);
      f.appendChild(k);
      kids.push([k, c]);
    }
    const l = rn.layout;
    if (l) {
      if (l.w === 'HUG') f.layoutSizingHorizontal = 'HUG';
      if (l.h === 'HUG') f.layoutSizingVertical = 'HUG';
    }
    if (typeof rn.width === 'number') { f.resize(rn.width, f.height); f.layoutSizingHorizontal = 'FIXED'; }
    else if (rn.width !== undefined) await num(ctx, f, 'width', rn.width);
    if (typeof rn.height === 'number') f.resize(f.width, rn.height);
    else if (rn.height !== undefined) await num(ctx, f, 'height', rn.height);
    // ограничения ширины (счётчик аватара не уже своей высоты)
    if (rn.minW !== undefined) await num(ctx, f, 'minWidth', rn.minW);
    if (rn.maxW !== undefined) await num(ctx, f, 'maxWidth', rn.maxW);
    // дети: заполнение по ширине и перенос текста
    for (const [k, c] of kids) {
      if ((c.w === 'FILL' || c.layout?.w === 'FILL') && 'layoutSizingHorizontal' in k) k.layoutSizingHorizontal = 'FILL';
      if (c.type === 'text' && c.text?.wrap) (k as TextNode).textAutoResize = 'HEIGHT';
    }
    // Абсолютные слои: сначала все выводятся из потока, и только потом измеряется родитель.
    // Иначе HUG-родитель считает их ширину, а после вывода сжимается, и позиции уезжают.
    const absKids = kids.filter(([, c]) => c.abs);
    for (const [k] of absKids) (k as SceneNode & LayoutMixin).layoutPositioning = 'ABSOLUTE';
    const W = f.width, H = f.height;
    for (const [k, c] of absKids) {
      const lk = k as SceneNode & LayoutMixin & ConstraintMixin;
      if (c.abs === 'focus') {
        const o = c.offset ?? 4;
        lk.resize(W + 2 * o, H + 2 * o);
        lk.x = -o; lk.y = -o;
        lk.constraints = { horizontal: 'STRETCH', vertical: 'STRETCH' };
        f.insertChild(0, k);
      } else if (c.abs === 'center') {
        lk.x = (W - lk.width) / 2; lk.y = (H - lk.height) / 2;
        lk.constraints = { horizontal: 'CENTER', vertical: 'CENTER' };
      } else if (c.abs === 'stretch-x') {
        lk.resize(W, lk.height);
        lk.x = 0; lk.y = (H - lk.height) / 2;
        lk.constraints = { horizontal: 'STRETCH', vertical: 'CENTER' };
      } else if (c.abs === 'at') {
        const p = c.pos ?? { x: 0, y: 0 };
        lk.x = p.x; lk.y = p.y;
        lk.constraints = { horizontal: p.x > W / 2 ? 'MAX' : 'MIN', vertical: p.y > H / 2 ? 'MAX' : 'MIN' };
      } else if (c.abs === 'after') {
        lk.x = W + (c.offset ?? 0); lk.y = 0;
        lk.constraints = { horizontal: 'MAX', vertical: 'MIN' };
      }
    }
  }
  return node;
}

// ---------------------------------------------------------------- набор
const GRID = { pad: 80, gapX: 40, gapY: 20, block: 60 };

async function layoutGrid(lib: Library, set: ComponentSetNode, def: SetDef, variants: ReturnType<typeof expandSet>) {
  const slots = gridSlots(def, variants);
  const byName = new Map((set.children as ComponentNode[]).map((c) => [c.name, c]));
  const colW: number[] = [];
  const rowH = new Map<string, number>();
  for (const v of variants) {
    const s = slots.get(v.name)!;
    const c = byName.get(v.name)!;
    colW[s.col] = Math.max(colW[s.col] ?? 0, c.width);
    const key = `${s.block}:${s.row}`;
    rowH.set(key, Math.max(rowH.get(key) ?? 0, c.height));
  }
  const blocks = Math.max(...[...slots.values()].map((s) => s.block)) + 1;
  const rowsIn = (b: number) => Math.max(...[...slots.values()].filter((s) => s.block === b).map((s) => s.row)) + 1;
  const rowY = new Map<string, number>();
  let y = GRID.pad;
  for (let b = 0; b < blocks; b++) {
    for (let r = 0; r < rowsIn(b); r++) {
      rowY.set(`${b}:${r}`, y);
      y += (rowH.get(`${b}:${r}`) ?? 0) + GRID.gapY;
    }
    y += GRID.block - GRID.gapY;
  }
  // колонки; вторая половина (split, например Inverse=True) отделена двойным отступом
  const firstOfHalf = new Map<number, number>();
  for (const s of slots.values()) firstOfHalf.set(s.half, Math.min(firstOfHalf.get(s.half) ?? Infinity, s.col));
  const colX: number[] = [];
  let x = GRID.pad;
  const bands: { half: number; x: number }[] = [];
  for (let c = 0; c < colW.length; c++) {
    const starts = [...firstOfHalf.entries()].find(([h, fc]) => h > 0 && fc === c);
    if (starts && c > 0) {
      x += 2 * GRID.pad - GRID.gapX;
      bands.push({ half: starts[0], x: x - GRID.pad });
    } else if (starts) bands.push({ half: starts[0], x: 0 });   // набор начинается сразу с подложки
    colX[c] = x;
    x += (colW[c] ?? 0) + GRID.gapX;
  }
  for (const v of variants) {
    const s = slots.get(v.name)!;
    const c = byName.get(v.name)!;
    c.x = colX[s.col];
    c.y = rowY.get(`${s.block}:${s.row}`)!;
  }
  const W = x - GRID.gapX + GRID.pad;
  set.resizeWithoutConstraints(W, y - GRID.block + GRID.pad);
  if (bands.length) {
    const drops = Object.values(def.grid?.backdrops ?? {});
    await bandFill(lib, set, bands.map((b) => ({ at: b.x / W, token: b.half === 1 ? 'color/bg/section/inverse-main' : drops[b.half - 2] })));
  }
}

/** Как в готовых наборах (Checkbox, Switch): светлая половина слева, тёмная — под инверсными вариантами,
 *  дальше — полосы-подложки для колонок, которые живут на своей заливке (grid.backdrops). Жёсткие границы градиента. */
async function bandFill(lib: Library, set: ComponentSetNode, bands: { at: number; token: string }[]) {
  const light = await lib.variable('color/bg/section/main');
  const stop = (position: number, color: RGBA, v: Variable | null): ColorStop =>
    (v ? { position, color, boundVariables: { color: figma.variables.createVariableAlias(v) } } : { position, color }) as ColorStop;
  const grey = { r: 0.5, g: 0.5, b: 0.5, a: 1 };
  const parts: { from: number; to: number; v: Variable | null }[] = [];
  let from = 0;
  let v: Variable | null = light;
  for (const b of bands) {
    parts.push({ from, to: b.at, v });
    from = Math.min(1, b.at + 0.0001);
    v = await lib.variable(b.token);
  }
  parts.push({ from, to: 1, v });
  const paintOf = (bind: boolean): GradientPaint => ({
    type: 'GRADIENT_LINEAR',
    gradientTransform: [[1, 0, 0], [0, 1, 0]],
    gradientStops: parts.flatMap((p) => [stop(p.from, grey, bind ? p.v : null), stop(p.to, grey, bind ? p.v : null)]),
  });
  try {
    set.fills = [paintOf(true)];
  } catch {
    set.fills = [paintOf(false)];
  }
}

export interface SetReport { name: string; variants: number }

export async function buildSet(lib: Library, def: SetDef, parent: FrameNode, warnings: Set<string>, tick: () => void): Promise<Owner> {
  const ctx: Ctx = { lib, refs: [], expose: [], warnings };
  const variants = expandSet(def);
  const comps: ComponentNode[] = [];
  for (const v of variants) {
    const c = (await makeNode(ctx, v.root, true)) as ComponentNode;
    c.name = v.name;
    parent.appendChild(c);
    comps.push(c);
    // вложенные экземпляры открывают свои свойства наружу (ТЗ F7), когда они уже внутри компонента
    for (const inst of ctx.expose.splice(0)) {
      try { inst.isExposedInstance = true; } catch (e) { warnings.add(`${def.name}: ${inst.name} — ${(e as Error).message}`); }
    }
    tick();
  }
  // без осей — одиночный компонент (как `_ Avatar / Counter / m` в файле), иначе набор вариантов
  const single = def.axes.length === 0;
  const set: Owner = single ? comps[0] : figma.combineAsVariants(comps, parent);
  set.name = def.name;
  if (def.description) set.description = def.description;
  if (set.type === 'COMPONENT_SET') {
    set.fills = await paint(ctx, 'color/bg/section/main');
    set.strokes = await paint(ctx, 'color/static/border/brand/firm');
    set.dashPattern = [10, 5];
    set.strokeWeight = 1;
    set.cornerRadius = 5;
  }

  // свойства компонента и ссылки слоёв на них
  const ids: Record<string, string> = {};
  for (const p of def.props) {
    if (p.type === 'INSTANCE_SWAP') {
      const icon = await lib.icon(String(p.default));
      if (!icon) { warnings.add(`свойство ${p.name}: нет иконки ${p.default}`); continue; }
      ids[p.name] = set.addComponentProperty(p.name, 'INSTANCE_SWAP', icon.id, { preferredValues: [{ type: 'COMPONENT', key: icon.key }] });
    } else {
      ids[p.name] = set.addComponentProperty(p.name, p.type, p.default);
    }
  }
  for (const { node, refs } of ctx.refs) {
    const map: Record<string, string> = {};
    for (const [field, prop] of Object.entries(refs)) if (prop && ids[prop]) map[field] = ids[prop];
    try {
      node.componentPropertyReferences = map as SceneNode['componentPropertyReferences'];
    } catch (e) {
      warnings.add(`${def.name}: ссылка на свойство (${Object.keys(map).join(', ')}) — ${(e as Error).message}`);
    }
  }
  if (set.type === 'COMPONENT_SET') await layoutGrid(lib, set, def, variants);
  lib.register(set);
  return set;
}

/** Проверка до записи. errors блокируют запись; warnings — нет (стиль заменяется привязкой к L2). */
export async function precheck(lib: Library, items: { def: BuildDef; master: boolean; spec: boolean }[], buildingSets: Set<string>) {
  const errors: string[] = [];
  const warnings: string[] = [];
  for (const { def: d, master, spec } of items) {
    const refs = collectRefs(d);
    if (master) {
      for (const v of refs.variables) if (!(await lib.variable(v))) errors.push(`${d.title}: нет переменной ${v} — сначала запишите токены (шаг 3) или опубликуйте библиотеку`);
      for (const s of refs.styles) if (!(await lib.textStyle(s))) warnings.push(`${d.title}: нет текстового стиля ${s} — типографика будет привязана к переменным L2`);
      for (const i of refs.icons) if (!(await lib.icon(i))) errors.push(`${d.title}: нет иконки ${i}`);
    }
    // вложенные наборы нужны мастеру, наборы спецификации — спецификации
    const nested = new Set<string>();
    if (master) for (const s of refs.sets) if (!d.sets.some((x) => x.name === s)) nested.add(s);
    if (spec) for (const c of d.spec?.columns ?? []) for (const card of c.cards) for (const it of card.items) nested.add(it.set);
    for (const s of nested) {
      if (buildingSets.has(s) || (await lib.set(s))) continue;
      const owner = items.find((x) => x.def.sets.some((y) => y.name === s));
      errors.push(owner || d.sets.some((x) => x.name === s)
        ? `${d.title}: набор «${s}» появится только при сборке компонента — включите «Компонент»`
        : `${d.title}: нет набора «${s}» — сначала соберите компонент, которому он принадлежит`);
    }
  }
  return { errors: [...new Set(errors)], warnings: [...new Set(warnings)] };
}

export { makeNode };
