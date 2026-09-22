// FEDS: read-only аудит привязок на странице файла компонентов. Подставить PAGE_ID и ROOTS (корни L3 этого компонента).
// Проверки: старые имена (A-Z, _, camelCase), привязки не к своему L3 (чужой компонент, L2/L1 напрямую), стили.
const PAGE_ID = '__PAGE__';
const ROOTS = __ROOTS__;
const page = await figma.getNodeByIdAsync(PAGE_ID);
await figma.setCurrentPageAsync(page);
const vc = new Map();
async function vinfo(id) {
  if (!vc.has(id)) { const v = await figma.variables.getVariableByIdAsync(id); let col = '?'; if (v) { const c = await figma.variables.getVariableCollectionByIdAsync(v.variableCollectionId); col = c ? c.name[0] : '?'; } vc.set(id, v ? { n: v.name, k: v.key.slice(0, 12), c: col } : { n: 'MISSING', k: id, c: '?' }); }
  return vc.get(id);
}
const bad = /[A-Z_]|textBtn|disebled|^- /;
const stale = new Map(), foreign = new Map(), styles = new Map();
let total = new Set();
function path(n, root) { const p = []; let x = n; while (x && x !== root && p.length < 4) { p.unshift(x.name); x = x.parent; } return p.join('>'); }
async function note(map, key, where) { if (!map.has(key)) map.set(key, { where, count: 0 }); map.get(key).count++; }
async function grab(n, owner) {
  const ids = [];
  const bv = n.boundVariables || {};
  for (const [prop, a] of Object.entries(bv)) for (const x of (Array.isArray(a) ? a : [a])) if (x && x.id) ids.push([prop, x.id]);
  for (const p of ['fills', 'strokes']) if (p in n && Array.isArray(n[p])) n[p].forEach(f => f.boundVariables && f.boundVariables.color && ids.push([p, f.boundVariables.color.id]));
  if ('effects' in n && Array.isArray(n.effects)) n.effects.forEach(e => Object.entries(e.boundVariables || {}).forEach(([k, x]) => x && x.id && ids.push(['effect.' + k, x.id])));
  for (const [prop, id] of ids) {
    const v = await vinfo(id); total.add(v.k);
    const where = owner.name + ' :: ' + path(n, owner) + ' .' + prop;
    if (bad.test(v.n) || v.n === 'MISSING') await note(stale, v.k + '|' + v.c + '|' + v.n, where);
    else if (n.type !== 'INSTANCE') {
      const root = v.n.split('/')[0];
      const own = v.c === '3' && ROOTS.includes(root);
      const typo = v.c === '2' && v.n.startsWith('typography/') && n.type === 'TEXT';
      if (!own && !typo) await note(foreign, v.c + '|' + v.n, where);
    }
  }
  for (const k of ['textStyleId', 'effectStyleId', 'fillStyleId', 'strokeStyleId']) if (k in n && typeof n[k] === 'string' && n[k]) {
    const s = await figma.getStyleByIdAsync(n[k]); const nm = s ? s.name : 'MISSING';
    await note(styles, (s ? s.key.slice(0, 12) : '-') + '|' + nm + (s && !s.remote ? '|LOCAL' : ''), owner.name + ' :: ' + path(n, owner));
  }
}
async function walk(n, owner) { await grab(n, owner); if (n.type !== 'INSTANCE' && 'children' in n) for (const c of n.children) await walk(c, owner); }
const owners = page.findAllWithCriteria({ types: ['COMPONENT_SET', 'COMPONENT'] }).filter(n => n.type === 'COMPONENT_SET' || n.parent.type !== 'COMPONENT_SET');
for (const o of owners) await walk(o, o);
const fmt = m => [...m.entries()].map(([k, v]) => k + ' ×' + v.count + ' @ ' + v.where);
return { page: page.name, owners: owners.length, distinctVars: total.size, stale: fmt(stale), foreign: fmt(foreign), styles: [...styles.keys()] };
