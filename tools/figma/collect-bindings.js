// FEDS: read-only сбор всех привязанных переменных и стилей на странице файла компонентов.
// Выход: v = ["key|name", ...], s = ["key|name", ...]. Подставить PAGE_ID.
const PAGE_ID = '__PAGE__';
const page = await figma.getNodeByIdAsync(PAGE_ID);
await figma.setCurrentPageAsync(page);
const vIds = new Set(), sIds = new Set();
function grab(n) {
  const bv = n.boundVariables || {};
  for (const a of Object.values(bv)) for (const x of (Array.isArray(a) ? a : [a])) if (x && x.id) vIds.add(x.id);
  for (const p of ['fills', 'strokes']) if (p in n && Array.isArray(n[p])) n[p].forEach(f => f.boundVariables && f.boundVariables.color && vIds.add(f.boundVariables.color.id));
  if ('effects' in n && Array.isArray(n.effects)) n.effects.forEach(e => Object.values(e.boundVariables || {}).forEach(x => x && x.id && vIds.add(x.id)));
  for (const k of ['textStyleId', 'effectStyleId', 'fillStyleId', 'strokeStyleId']) if (k in n && typeof n[k] === 'string' && n[k]) sIds.add(n[k]);
}
function walk(n) { grab(n); if (n.type !== 'INSTANCE' && 'children' in n) n.children.forEach(walk); }
const owners = page.findAllWithCriteria({ types: ['COMPONENT_SET', 'COMPONENT'] }).filter(n => n.type === 'COMPONENT_SET' || n.parent.type !== 'COMPONENT_SET');
owners.forEach(walk);
const v = [], s = [];
for (const id of vIds) { const x = await figma.variables.getVariableByIdAsync(id); v.push(x ? x.key.slice(0, 12) + '|' + x.name : 'MISSING|' + id); }
for (const id of sIds) { const x = await figma.getStyleByIdAsync(id); s.push(x ? x.key.slice(0, 12) + '|' + x.name + (x.remote ? '' : '|LOCAL') : 'MISSING|' + id); }
return { page: page.name, owners: owners.length, v: v.sort(), s: s.sort() };
