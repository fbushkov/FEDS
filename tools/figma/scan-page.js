// FEDS: read-only разбор страницы файла компонентов (для use_figma). Подставить PAGE_ID.
const PAGE_ID = '__PAGE__';
const page = await figma.getNodeByIdAsync(PAGE_ID);
await figma.setCurrentPageAsync(page);
const vc = new Map();
async function vn(id) { if (!vc.has(id)) { const v = await figma.variables.getVariableByIdAsync(id); vc.set(id, v ? v.name : '?'); } return vc.get(id); }
const sc = new Map();
async function sn(id) { if (!id || typeof id !== 'string') return null; if (!sc.has(id)) { const s = await figma.getStyleByIdAsync(id); sc.set(id, s ? s.name : '?'); } return sc.get(id); }
const hard = { count: 0, ex: [] };
function flag(n, what) { hard.count++; if (hard.ex.length < 12) hard.ex.push(n.name + ':' + what); }
async function binds(n, check) {
  const out = []; const bv = n.boundVariables || {};
  for (const [k, a] of Object.entries(bv)) {
    if (k === 'fills' || k === 'strokes' || k === 'effects' || k === 'textRangeFills') continue;
    for (const x of (Array.isArray(a) ? a : [a])) if (x && x.id) out.push(k + '=' + await vn(x.id));
  }
  for (const p of ['fills', 'strokes']) if (p in n && Array.isArray(n[p])) for (const f of n[p]) {
    if (f.visible === false) continue;
    if (f.boundVariables && f.boundVariables.color) out.push(p[0] + '=' + await vn(f.boundVariables.color.id));
    else if (f.type === 'SOLID') { out.push(p[0] + '=HARD'); if (check) flag(n, p); }
    else if (f.type === 'IMAGE') out.push(p[0] + '=IMAGE');
  }
  const m = Object.fromEntries(out.filter(x => !x.startsWith('f=') && !x.startsWith('s=')).map(x => x.split('=')));
  const rest = out.filter(x => x.startsWith('f=') || x.startsWith('s='));
  const merged = [];
  const grp = (keys, label) => { const vals = keys.map(k => m[k]); if (vals.every(v => v) && vals.every(v => v === vals[0])) { merged.push(label + '=' + vals[0]); keys.forEach(k => delete m[k]); } };
  grp(['topLeftRadius', 'topRightRadius', 'bottomLeftRadius', 'bottomRightRadius'], 'radius');
  grp(['strokeTopWeight', 'strokeBottomWeight', 'strokeLeftWeight', 'strokeRightWeight'], 'strokeW');
  grp(['paddingLeft', 'paddingRight'], 'px'); grp(['paddingTop', 'paddingBottom'], 'py');
  if (n.type === 'TEXT') for (const k of ['letterSpacing', 'fontSize', 'lineHeight', 'fontWeight', 'fontFamily', 'fontStyle']) delete m[k];
  out.length = 0; out.push(...merged, ...Object.entries(m).map(([k, v]) => k + '=' + v), ...rest);
  if (n.type === 'TEXT') { const s = await sn(n.textStyleId); out.push('ts=' + (s || 'NONE')); if (!s && check) flag(n, 'textStyle'); }
  if ('effectStyleId' in n && n.effectStyleId) out.push('es=' + await sn(n.effectStyleId));
  if (check && n.type !== 'INSTANCE') {
    if ('layoutMode' in n && n.layoutMode !== 'NONE') {
      for (const k of ['itemSpacing', 'paddingLeft', 'paddingRight', 'paddingTop', 'paddingBottom']) if (n[k] && !bv[k]) flag(n, k + '=' + n[k]);
    }
    if ('cornerRadius' in n && typeof n.cornerRadius === 'number' && n.cornerRadius > 0 && !bv.topLeftRadius && !bv.cornerRadius) flag(n, 'radius=' + n.cornerRadius);
    if ('strokes' in n && n.strokes.length && typeof n.strokeWeight === 'number' && !bv.strokeWeight && !bv.strokeTopWeight) flag(n, 'strokeWeight=' + n.strokeWeight);
  }
  return out;
}
function lay(n) {
  if (!('layoutMode' in n) || n.layoutMode === 'NONE') return '';
  return ' {' + n.layoutMode[0] + ' ' + (n.primaryAxisAlignItems || '')[0] + (n.counterAxisAlignItems || '')[0] + (n.layoutWrap === 'WRAP' ? ' wrap' : '') + '}';
}
function sz(n) { return ('layoutSizingHorizontal' in n) ? ' [' + n.layoutSizingHorizontal[0] + n.layoutSizingVertical[0] + (n.minWidth ? ' minW' + n.minWidth : '') + (n.maxWidth ? ' maxW' + n.maxWidth : '') + ']' : ''; }
async function tree(n, d, lines, maxD) {
  let line = '  '.repeat(d) + n.name + ' <' + n.type + '>' + lay(n) + sz(n) + (n.visible === false ? ' HIDDEN' : '');
  if (n.componentPropertyReferences) { const r = Object.entries(n.componentPropertyReferences).map(([k, v]) => k + '→' + v.split('#')[0]); if (r.length) line += ' refs(' + r.join(',') + ')'; }
  if (n.type === 'INSTANCE') { const m = await n.getMainComponentAsync(); line += ' ⇒ ' + (m ? (m.parent && m.parent.type === 'COMPONENT_SET' ? m.parent.name + ' / ' + m.name : m.name) + (m.remote ? ' (lib)' : '') : '?'); }
  const b = await binds(n, false); if (b.length) line += ' :: ' + b.join('; ');
  lines.push(line);
  if (n.type !== 'INSTANCE' && 'children' in n && d < maxD) for (const c of n.children.slice(0, 14)) await tree(c, d + 1, lines, maxD);
}
async function scanAll(n) { await binds(n, true); if (n.type !== 'INSTANCE' && 'children' in n) for (const c of n.children) await scanAll(c); }
const res = { page: page.name, top: page.children.map(n => n.name + ' <' + n.type + '> ' + n.id).slice(0, 40), sets: [] };
const owners = page.findAllWithCriteria({ types: ['COMPONENT_SET', 'COMPONENT'] }).filter(n => n.type === 'COMPONENT_SET' || n.parent.type !== 'COMPONENT_SET');
for (const s of owners.slice(0, 25)) {
  const defs = Object.entries(s.componentPropertyDefinitions).map(([k, v]) => k.split('#')[0] + ':' + v.type[0] + (v.variantOptions ? '[' + v.variantOptions.join('|') + ']' : '') + '=' + (typeof v.defaultValue === 'string' && v.defaultValue.length > 20 ? '…' : v.defaultValue) + (v.preferredValues ? ' pref' + v.preferredValues.length : ''));
  const variant = s.type === 'COMPONENT_SET' ? (s.defaultVariant || s.children[0]) : s;
  const lines = []; await tree(variant, 0, lines, 7);
  hard.count = 0; hard.ex = [];
  for (const v of (s.type === 'COMPONENT_SET' ? s.children : [s])) await scanAll(v);
  res.sets.push({ name: s.name, id: s.id, type: s.type, variants: s.type === 'COMPONENT_SET' ? s.children.length : 1, desc: (s.description || '').slice(0, 160), props: defs, defaultTree: lines.join('\n'), hardcoded: hard.count, hardEx: hard.ex });
}
res.ownersTotal = owners.length;
return res;
