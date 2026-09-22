import type { Analysis } from '../core/analyze';
import type { CatalogStatus } from '../core/diff';
import type { ApplyReport, Conventions, DiffResult, DiffRow, Preset } from '../core/types';
import type { BuildMeta, DocMeta, ExportFile, ToMain, ToUI } from '../messages';
import type { BuildReport } from '../figma/run-build';
import { makeZip } from './zip';

// ---------------------------------------------------------------- состояние
type Step = 'analyze' | 'pick' | 'tokens' | 'docs' | 'build' | 'report';

const STEPS: { id: Step; label: string; soon?: boolean }[] = [
  { id: 'analyze', label: '1 · Анализ' },
  { id: 'pick', label: '2 · Компоненты' },
  { id: 'tokens', label: '3 · Токены' },
  { id: 'docs', label: '4 · Документация' },
  { id: 'build', label: '5 · Сборка' },
  { id: 'report', label: '6 · Отчёт' },
];

const STATUS_LABEL: Record<string, string> = {
  add: 'добавится', same: 'совпадает', changed: 'отличается', extra: 'лишний', blocked: 'заблокирован',
};
const LEVEL_LABEL = (l: DiffRow['level']) => (l === 'style' ? 'стиль' : 'L' + l);

const S = {
  step: 'pick' as Step,
  fileName: '',
  version: '',
  presets: [] as Preset[],
  docs: [] as DocMeta[],
  statuses: new Map<string, CatalogStatus>(),
  statusBusy: false,
  conv: null as Conventions | null,
  sel: new Set<string>(),
  analysis: null as Analysis | null,
  analysisMd: '',
  diff: null as DiffResult | null,
  diffMd: '',
  filter: 'all' as string,
  change: new Set<string>(),
  remove: new Set<string>(),
  busy: '' as string,
  progress: null as { done: number; total: number } | null,
  report: null as ApplyReport | null,
  reportMd: '',
  error: '',
  modal: null as null | 'settings' | 'confirm',
  docSel: new Set<string>(),
  docTokens: true,
  docMode: 'zip' as 'zip' | 'single' | 'one',
  builds: [] as BuildMeta[],
  buildSel: new Set<string>(),
  /** Для каждого компонента: собирать мастер и/или спецификацию. По умолчанию — оба. */
  buildOpts: new Map<string, { master: boolean; spec: boolean }>(),
  buildReport: null as BuildReport | null,
};

const send = (m: ToMain) => parent.postMessage({ pluginMessage: m }, '*');

// ---------------------------------------------------------------- утилиты
function esc(s: unknown): string {
  return String(s ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]!));
}

function saveBlob(name: string, blob: Blob) {
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = name;
  a.click();
  setTimeout(() => URL.revokeObjectURL(a.href), 2000);
}

const saveText = (name: string, text: string) => saveBlob(name, new Blob([text], { type: 'text/markdown;charset=utf-8' }));

const byComp = (c: string) => S.presets.find((p) => p.component === c);
const groupOf = (p: Preset) => (p.kind === 'system' ? 'system' : p.origin === 'existing' ? 'existing' : 'new');

/** Выбор + зависимости, которых ещё нет в файле. */
function effective(): { list: Preset[]; auto: string[] } {
  const out = new Set<string>();
  const auto: string[] = [];
  const visit = (c: string, isAuto: boolean) => {
    if (out.has(c)) return;
    const p = byComp(c);
    if (!p) return;
    if (isAuto) {
      const st = S.statuses.get(c);
      if (st && st.state === 'in-file') return;
      auto.push(c);
    }
    out.add(c);
    for (const r of p.requires ?? []) visit(r, true);
  };
  for (const c of S.sel) visit(c, false);
  // порядок: система → готовые → новые
  const order = { system: 0, existing: 1, new: 2 } as const;
  const list = [...out].map((c) => byComp(c)!).sort((a, b) => order[groupOf(a)] - order[groupOf(b)]);
  return { list, auto };
}

function count(p: Preset) {
  return `${p.l1?.length ? `L1 ${p.l1.length} · ` : ''}L2 ${p.l2?.length ?? 0} · L3 ${p.l3.length}`;
}

function badge(c: string): string {
  const st = S.statuses.get(c);
  if (!st) return S.statusBusy ? '<span class="st same">…</span>' : '';
  switch (st.state) {
    case 'in-file': return `<span class="st add" title="Все токены уже в файле">✓ в файле</span>`;
    case 'absent': return `<span class="st extra">нет в файле</span>`;
    case 'partial': return `<span class="st changed" title="Есть ${st.same} из ${st.total}">частично · +${st.add}</span>`;
    case 'differs': return `<span class="st blocked" title="Отличается ${st.changed}">отличается · ${st.changed}</span>`;
  }
}

// ---------------------------------------------------------------- экраны
function viewAnalyze(): string {
  const a = S.analysis;
  if (!a) {
    return `<div class="empty"><p>Плагин прочитает коллекции, переменные и стили файла и покажет проблемы. Ничего не изменится.</p>
      <button class="btn primary" data-act="analyze" ${S.busy ? 'disabled' : ''}>${S.busy === 'analyze' ? 'Анализ…' : 'Проанализировать файл'}</button></div>`;
  }
  const issues = a.issues.map((i) => `<details><summary>${esc(i.title)}: <b>${i.items.length}</b></summary>
      <div>${i.items.length ? i.items.slice(0, 300).map((x) => `<div class="mono">${esc(x)}</div>`).join('') : '<p>Нет</p>'}</div></details>`).join('');
  return `
    ${a.missing.length ? `<div class="box warn">Нет коллекций: ${a.missing.map(esc).join(', ')}. Если файл пустой — выберите «Систему» на шаге 2, коллекции будут созданы.</div>` : ''}
    <div class="stats">
      ${a.collections.filter((c) => c.level !== '—').map((c) => `<div class="stat"><b>${c.count}</b>${esc(c.level)} · ${esc(c.name)}<br><span class="mono">${esc(c.modes.join(', '))}</span></div>`).join('')}
      <div class="stat"><b>${a.textStyles}</b>текстовых стилей</div>
      <div class="stat"><b>${a.effectStyles}</b>эффект-стилей</div>
      <div class="stat"><b>${a.inversePairs.pairs}</b>пар inverse-*</div>
    </div>
    <h3>Компоненты в L3 (${a.componentRoots.length})</h3>
    <div class="chips">${a.componentRoots.map((r) => `<span class="chip">${esc(r.root)} · ${r.count}</span>`).join('')}</div>
    <h3>Проблемы</h3>${issues}
    <h3>Словарь L2</h3>
    ${a.grammar.map((g) => `<details><summary class="mono">${esc(g.root)} · ${g.count}</summary><div>${g.segments.map((s, i) => `<div><b>${i + 1}:</b> <span class="mono">${esc(s.join(', '))}</span></div>`).join('')}</div></details>`).join('')}`;
}

function viewPick(): string {
  const groups: [string, string, string][] = [
    ['system', 'База системы', 'Примитивы L1 и общий L2 (цвет, общая типографика). Нужна для сборки в пустом файле.'],
    ['existing', 'Готовые компоненты', 'Сняты с текущей системы. В исходном файле — «в файле»; в другом файле — добавятся.'],
    ['new', 'Новые компоненты', 'Токены по документации backlog. Добавляются в существующую систему.'],
  ];
  const { auto } = effective();
  // части (Dropdown у Select, Combobox, Multiselect) не выбираются отдельно — их подключают владельцы
  const rows = (g: string) => S.presets.filter((p) => groupOf(p) === g && p.kind !== 'part').map((p) => {
    const on = S.sel.has(p.component);
    const isAuto = auto.includes(p.component);
    return `<label class="row ${on ? 'on' : ''}">
      <input type="checkbox" data-act="pick" data-c="${esc(p.component)}" ${on ? 'checked' : ''}>
      <span class="grow"><b>${esc(p.title ?? p.component)}</b> <span class="mono muted">${esc(p.component)}</span>
        ${isAuto ? '<span class="st same">зависимость</span>' : ''}<br>
        <span class="muted">${count(p)}${p.requires?.length ? ` · требует: ${p.requires.map(esc).join(', ')}` : ''}</span></span>
      ${badge(p.component)}</label>`;
  }).join('');
  return `
    <p>Плагин сравнивает каждый пресет с файлом: что уже есть, что можно добавить. Существующие переменные без вашего разрешения не меняются.</p>
    ${S.presets.length === 0 ? '<div class="empty">Каталог пуст</div>' : ''}
    ${groups.map(([id, title, hint]) => `
      <div class="group"><div class="group-head"><h3>${title}</h3>
        <button class="link" data-act="pick-group" data-g="${id}">выбрать всё</button>
        <button class="link" data-act="unpick-group" data-g="${id}">снять</button></div>
        <p>${hint}</p>${rows(id)}</div>`).join('')}
    ${auto.length ? `<div class="box warn">Добавлены зависимости, которых нет в файле: ${auto.map(esc).join(', ')}</div>` : ''}
    <div style="margin-top:8px"><label class="btn" style="display:inline-flex;align-items:center">Загрузить свой пресет JSON…<input type="file" accept=".json" id="file" hidden></label></div>`;
}

function rowHtml(r: DiffRow): string {
  const key = r.name;
  const box = r.status === 'changed'
    ? `<input type="checkbox" data-act="toggle-change" data-name="${esc(key)}" ${S.change.has(key) ? 'checked' : ''} title="Разрешить изменить">`
    : r.status === 'extra'
      ? `<input type="checkbox" data-act="toggle-remove" data-name="${esc(key)}" ${S.remove.has(key) ? 'checked' : ''} title="Разрешить удалить">`
      : '';
  const what = r.status === 'changed' ? (r.reasons ?? []).join('; ') : r.status === 'extra' ? `сейчас → ${r.current ?? ''}` : r.target ?? '';
  return `<tr><td>${box}</td><td><span class="st ${r.status}">${STATUS_LABEL[r.status]}</span></td>
    <td>${LEVEL_LABEL(r.level)}</td><td class="mono">${esc(r.name)}</td><td class="mono">${esc(what)}</td></tr>`;
}

function viewTokens(): string {
  if (!S.sel.size) return `<div class="empty">Сначала выберите компоненты на шаге 2.</div>`;
  const d = S.diff;
  if (!d) return `<div class="empty"><button class="btn primary" data-act="diff" ${S.busy ? 'disabled' : ''}>${S.busy === 'diff' ? 'Сравниваю…' : 'Построить дифф'}</button></div>`;
  const by = (s: string) => d.rows.filter((r) => r.status === s).length;
  const filters = [['all', 'Все', d.rows.length], ['add', 'Добавится', by('add')], ['same', 'Совпадает', by('same')],
    ['changed', 'Отличается', by('changed')], ['extra', 'Лишние', by('extra')], ['blocked', 'Заблокировано', by('blocked')]]
    .filter(([id, , n]) => id === 'all' || (n as number) > 0);
  const rows = d.rows.filter((r) => S.filter === 'all' || r.status === S.filter);
  const shown = rows.slice(0, 1500);
  const bad = d.contrast.filter((c) => !c.ok);
  const lv = (l: DiffRow['level']) => d.rows.filter((r) => r.level === l && r.status === 'add').length;
  return `
    <div class="stats">
      <div class="stat"><b>${lv(1)}</b>L1 добавится</div><div class="stat"><b>${lv(2)}</b>L2 добавится</div>
      <div class="stat"><b>${lv(3)}</b>L3 добавится</div>
      <div class="stat"><b>${by('same')}</b>уже есть и совпадает</div>
    </div>
    ${d.createCollections.length ? `<div class="box warn">Будут созданы коллекции: ${d.createCollections.map(esc).join(', ')}</div>` : ''}
    ${d.errors.length ? `<div class="box err"><b>Ошибки (${d.errors.length}) — запись заблокирована</b><ul>${d.errors.slice(0, 50).map((e) => `<li>${esc(e)}</li>`).join('')}</ul></div>` : ''}
    ${d.warnings.length ? `<details><summary>⚠️ Предупреждения: <b>${d.warnings.length}</b></summary><div>${d.warnings.map((e) => `<div>${esc(e)}</div>`).join('')}</div></details>` : ''}
    ${d.contrast.length ? `<details><summary>Контраст: ${d.contrast.length - bad.length} из ${d.contrast.length} пар в норме</summary><div><table>
      <tr><th>Передний план</th><th>Фон</th><th>Режим</th><th>Контраст</th><th></th></tr>
      ${d.contrast.map((c) => `<tr><td class="mono">${esc(c.fg)}</td><td class="mono">${esc(c.bg)}</td><td>${c.mode}</td><td>${c.ratio.toFixed(2)} / ${c.need}</td><td>${c.ok ? '✅' : c.accepted ? '☑️ принято' : '⚠️'}</td></tr>`).join('')}
      </table></div></details>` : ''}
    ${(by('changed') || by('extra')) ? `<div class="box warn">Существующие переменные не меняются и не удаляются, пока вы не отметите их галочкой. Отмеченные попадут в запись после отдельного подтверждения.</div>` : ''}
    <div class="chips">${filters.map(([id, label, n]) => `<button class="chip ${S.filter === id ? 'on' : ''}" data-act="filter" data-f="${id}">${label} · ${n}</button>`).join('')}</div>
    <table><tr><th></th><th>Статус</th><th>Ур.</th><th>Имя</th><th>Значение / причина</th></tr>${shown.map(rowHtml).join('')}</table>
    ${rows.length > shown.length ? `<p>Показаны первые ${shown.length} из ${rows.length}. Полный список — «Скачать дифф .md».</p>` : ''}`;
}

function viewDocs(): string {
  const groups: [string, string][] = [['existing', 'Готовые компоненты'], ['new', 'Новые компоненты']];
  const list = (g: string) => S.docs.filter((d) => d.group === g).map((d) => {
    const p = byComp(d.component);
    return `<label class="row ${S.docSel.has(d.id) ? 'on' : ''}"><input type="checkbox" data-act="doc" data-id="${esc(d.id)}" ${S.docSel.has(d.id) ? 'checked' : ''}>
      <span class="grow"><b>${esc(d.title)}</b> <span class="muted">· ${esc(p?.title ?? d.component)}</span><br><span class="mono muted">${esc(d.source)}</span></span>
      <button class="link" data-act="doc-one" data-id="${esc(d.id)}">скачать .md</button></label>`;
  }).join('');
  return `
    <p>Документация компонентов в Markdown. Можно выгрузить всё или выборочно: архивом по папкам или одним файлом. К документам добавляются таблицы токенов с реальными значениями light / dark из текущего файла.</p>
    <div class="chips">
      <button class="chip" data-act="doc-all">Выбрать все (${S.docs.length})</button>
      <button class="chip" data-act="doc-none">Снять выбор</button>
      <button class="chip" data-act="doc-from-sel">Как на шаге 2</button>
    </div>
    <label class="row"><input type="checkbox" data-act="doc-tokens" ${S.docTokens ? 'checked' : ''}><span class="grow">Добавить таблицы токенов (L3 → L2 → значения, L2 компонента, текстовые стили)</span></label>
    ${groups.map(([g, t]) => `<div class="group"><div class="group-head"><h3>${t}</h3>
      <button class="link" data-act="doc-group" data-g="${g}">выбрать всё</button></div>${list(g)}</div>`).join('')}`;
}

const optsOf = (c: string) => {
  if (!S.buildOpts.has(c)) S.buildOpts.set(c, { master: true, spec: true });
  return S.buildOpts.get(c)!;
};

function viewBuild(): string {
  const rows = S.builds.map((b) => {
    const on = S.buildSel.has(b.component);
    const o = optsOf(b.component);
    const variants = b.sets.reduce((n, x) => n + x.variants, 0);
    const kind = b.origin === 'existing' ? '<span class="st same">повтор текущей сборки</span>' : '<span class="st add">новый компонент</span>';
    const req = b.requires.length ? `<br><span class="muted">использует экземпляры: ${b.requires.map(esc).join(', ')} — отметьте их тоже, если их ещё нет в файле</span>` : '';
    const notes = b.notes.length ? `<details><summary>Правила и допущения</summary><div>${b.notes.map((n) => `<div>${esc(n)}</div>`).join('')}</div></details>` : '';
    const toggles = `<div class="chips" style="margin:6px 0 0">
        <button class="chip ${o.master ? 'on' : ''}" data-act="bopt" data-c="${esc(b.component)}" data-k="master">${o.master ? '✓ ' : ''}Компонент · ${variants} вар.</button>
        <button class="chip ${o.spec ? 'on' : ''}" data-act="bopt" data-c="${esc(b.component)}" data-k="spec">${o.spec ? '✓ ' : ''}Спецификация · ${b.specColumns.length} разд.</button></div>`;
    return `<div class="row ${on ? 'on' : ''}"><input type="checkbox" data-act="bsel" data-c="${esc(b.component)}" ${on ? 'checked' : ''}>
      <span class="grow"><b>${esc(b.title)}</b> ${kind}<br>
      <span class="muted">${b.sets.map((x) => `${esc(x.name)} · ${x.variants}`).join(' · ')}</span>
      <br><span class="muted">Спецификация: ${b.specColumns.map(esc).join(' · ')}</span>${req}${toggles}${notes}</span></div>`;
  }).join('');
  return `<p>Сборка по единому правилу FEroom (docs/build-rules.md): наборы и варианты, свойства, auto layout; все цвета, отступы, радиусы, размеры и типографика — через переменные. Спецификация собирается на живых экземплярах сразу после компонента. Каждый компонент — на новой странице, существующие страницы не меняются. Отмена — один Ctrl+Z.</p>
    <div class="box warn">Нужны токены компонента в этом файле или в подключённой библиотеке. Для нового компонента (Alert) сначала запишите токены на шаге 3. Если чего-то не хватает, плагин ничего не создаст и покажет список.</div>
    ${rows || '<div class="empty">Описаний сборки нет</div>'}`;
}

function viewSoon(what: string): string {
  return `<div class="empty"><p><b>${what}</b> — следующий этап.</p><p>Сейчас плагин собирает и дополняет трёхуровневую систему токенов, стили и документацию. Сборка компонента и спецификации появятся после проектирования архитектуры сборки для новых компонентов.</p></div>`;
}

function viewBuildReport(): string {
  const b = S.buildReport;
  if (!b) return '';
  const list = (t: string, xs: string[], open = false) => (xs.length ? `<details ${open ? 'open' : ''}><summary>${t}: <b>${xs.length}</b></summary><div>${xs.map((x) => `<div class="mono">${esc(x)}</div>`).join('')}</div></details>` : '');
  const head = b.errors.length ? 'Сборка не выполнена: не хватает ресурсов. В файле ничего не создано.' : `Готово. Страницы: ${b.pages.map(esc).join(', ')}. Отмена — один Ctrl+Z.`;
  return `<h3>Сборка</h3><div class="box ${b.errors.length ? 'err' : 'ok'}">${head}</div>
    ${b.sets.length ? `<div class="stats">${b.sets.map((x) => `<div class="stat"><b>${x.variants}</b>${esc(x.name)}</div>`).join('')}</div>` : ''}
    ${b.specs.length ? `<p>Спецификации: ${b.specs.map(esc).join(', ')}</p>` : ''}
    ${list('Ошибки', b.errors, true)}${list('Предупреждения', b.warnings)}`;
}

function viewReport(): string {
  const r = S.report;
  if (!r) return viewBuildReport() || `<div class="empty">Отчёт появится после записи токенов или сборки.</div>`;
  const sec = (t: string, xs: string[], open = false) => (xs.length ? `<details ${open ? 'open' : ''}><summary>${t}: <b>${xs.length}</b></summary><div>${xs.slice(0, 2000).map((x) => `<div class="mono">${esc(x)}</div>`).join('')}</div></details>` : '');
  return `
    <div class="box ${r.errors.length ? 'err' : 'ok'}">${r.errors.length ? 'Запись завершена с ошибками.' : 'Запись завершена. Отменить всё целиком — Ctrl+Z (Cmd+Z) один раз.'}</div>
    <div class="stats"><div class="stat"><b>${r.created.length}</b>создано</div><div class="stat"><b>${r.updated.length}</b>изменено</div>
      <div class="stat"><b>${r.removed.length}</b>удалено</div><div class="stat"><b>${r.styles.length}</b>стилей</div><div class="stat"><b>${r.skipped.length}</b>пропущено</div></div>
    ${sec('Ошибки', r.errors, true)}${sec('Предупреждения', r.warnings)}${sec('Создано', r.created)}${sec('Изменено', r.updated)}${sec('Удалено', r.removed)}${sec('Стили', r.styles)}${sec('Пропущено', r.skipped)}
    <p style="margin-top:12px">Проверка идемпотентности: повторный дифф должен показать только «совпадает».</p>
    <button class="btn" data-act="recheck">Проверить повторно</button>${viewBuildReport()}`;
}

function viewModal(): string {
  if (S.modal === 'settings' && S.conv) {
    const c = S.conv;
    return `<div class="modal-bg"><div class="modal"><h2>Настройки соглашений</h2>
      <label class="field">Коллекция уровня 1<input type="text" id="c-l1" value="${esc(c.collections.l1)}"></label>
      <label class="field">Коллекция уровня 2<input type="text" id="c-l2" value="${esc(c.collections.l2)}"></label>
      <label class="field">Коллекция уровня 3<input type="text" id="c-l3" value="${esc(c.collections.l3)}"></label>
      <label class="field">Режим light / dark в уровне 2<span style="display:flex;gap:6px"><input type="text" id="m-l" value="${esc(c.modes.light)}"><input type="text" id="m-d" value="${esc(c.modes.dark)}"></span></label>
      <label class="field">Регулярка сегмента имени<input type="text" id="seg" value="${esc(c.segment)}"></label>
      <div class="actions"><button class="btn" data-act="close">Отмена</button><button class="btn primary" data-act="save-settings">Сохранить</button></div></div></div>`;
  }
  if (S.modal === 'confirm') {
    return `<div class="modal-bg"><div class="modal"><h2>Изменить существующее?</h2>
      <p>Помимо добавления будет изменено: <b>${S.change.size}</b>, удалено: <b>${S.remove.size}</b> существующих переменных.</p>
      <div class="mono" style="max-height:160px;overflow:auto">${[...S.change].map((n) => `~ ${esc(n)}`).concat([...S.remove].map((n) => `− ${esc(n)}`)).join('<br>')}</div>
      <div class="actions"><button class="btn" data-act="close">Отмена</button><button class="btn primary" data-act="apply-confirmed">Записать</button></div></div></div>`;
  }
  return '';
}

function footer(): string {
  if (S.progress) {
    const pct = S.progress.total ? Math.round((S.progress.done / S.progress.total) * 100) : 0;
    return `<div class="progress"><i style="width:${pct}%"></i></div><span>${S.progress.done} / ${S.progress.total}</span>`;
  }
  switch (S.step) {
    case 'analyze':
      return S.analysis ? `<button class="btn" data-act="analyze">Обновить</button><button class="btn" data-act="dl-analysis">Скачать отчёт .md</button><span class="spacer"></span><button class="btn primary" data-act="go" data-s="pick">Далее</button>` : '';
    case 'pick': {
      const { list } = effective();
      return `<button class="btn" data-act="catalog" ${S.statusBusy ? 'disabled' : ''}>${S.statusBusy ? 'Проверяю…' : 'Обновить статусы'}</button><span class="spacer"></span>
        <span class="muted">выбрано: ${S.sel.size}${list.length > S.sel.size ? ` (+${list.length - S.sel.size} зав.)` : ''}</span>
        <button class="btn primary" data-act="go" data-s="tokens" ${S.sel.size ? '' : 'disabled'}>Далее: дифф</button>`;
    }
    case 'tokens': {
      if (!S.diff) return '';
      const n = S.diff.rows.filter((r) => r.status === 'add').length + S.change.size + S.remove.size;
      return `<button class="btn" data-act="diff">Обновить дифф</button><button class="btn" data-act="dl-diff">Скачать дифф .md</button><span class="spacer"></span>
        <button class="btn primary" data-act="apply" ${S.diff.errors.length || (!n && !S.diff.createCollections.length) || S.busy ? 'disabled' : ''}>${S.busy === 'apply' ? 'Записываю…' : `Записать в файл (${n})`}</button>`;
    }
    case 'docs':
      return `<span class="muted">выбрано документов: ${S.docSel.size}</span><span class="spacer"></span>
        <button class="btn" data-act="doc-export" data-m="single" ${S.docSel.size ? '' : 'disabled'}>Одним .md</button>
        <button class="btn primary" data-act="doc-export" data-m="zip" ${S.docSel.size ? '' : 'disabled'}>Скачать .zip</button>`;
    case 'build': {
      const picked = S.builds.filter((b) => S.buildSel.has(b.component));
      const n = picked.reduce((m, b) => m + (optsOf(b.component).master ? b.sets.reduce((k, x) => k + x.variants, 0) : 0), 0);
      const specs = picked.filter((b) => optsOf(b.component).spec).length;
      const ok = picked.some((b) => optsOf(b.component).master || optsOf(b.component).spec) && !S.busy;
      return `<span class="muted">компонентов: ${picked.length} · вариантов: ${n} · спецификаций: ${specs}</span><span class="spacer"></span>
        <button class="btn primary" data-act="build" ${ok ? '' : 'disabled'}>${S.busy === 'build' ? 'Собираю…' : 'Собрать'}</button>`;
    }
    case 'report':
      return S.report ? `<button class="btn" data-act="dl-report">Скачать отчёт .md</button>` : '';
    default:
      return '';
  }
}

function render() {
  const body = {
    analyze: viewAnalyze, pick: viewPick, tokens: viewTokens, docs: viewDocs,
    build: viewBuild, report: viewReport,
  }[S.step]();
  const main = document.querySelector('main');
  const scroll = main ? main.scrollTop : 0;
  document.getElementById('app')!.innerHTML = `
    <header><span class="title">FEDS</span><span class="file">${esc(S.fileName)}</span>
      <span class="mono" style="color:var(--text3)">v${esc(S.version)}</span><button class="icon-btn" data-act="settings" title="Настройки">⚙</button></header>
    <nav>${STEPS.map((s) => `<button class="${S.step === s.id ? 'active' : ''}" data-act="go" data-s="${s.id}">${s.label}${s.soon ? '<span class="soon">скоро</span>' : ''}</button>`).join('')}</nav>
    <main>${S.error ? `<div class="box err">${esc(S.error)}</div>` : ''}${body}</main>
    <footer>${footer()}</footer>${viewModal()}`;
  const m2 = document.querySelector('main');
  if (m2) m2.scrollTop = scroll;
  const file = document.getElementById('file') as HTMLInputElement | null;
  if (file) file.onchange = () => loadFile(file);
}

async function loadFile(input: HTMLInputElement) {
  const f = input.files?.[0];
  if (!f) return;
  try {
    const data = JSON.parse(await f.text());
    const list: Preset[] = Array.isArray(data) ? data : [data];
    for (const p of list) {
      if (!p.component || !Array.isArray(p.l3)) throw new Error('в файле нет полей component и l3');
      p.origin = p.origin ?? 'new';
      const i = S.presets.findIndex((x) => x.component === p.component);
      if (i >= 0) S.presets[i] = p;
      else S.presets.push(p);
      S.sel.add(p.component);
    }
    S.diff = null;
    S.error = '';
  } catch (e) {
    S.error = `Не удалось прочитать JSON: ${(e as Error).message}`;
  }
  render();
}

function requestDiff() {
  if (!S.sel.size) return;
  S.busy = 'diff';
  send({ type: 'diff', presets: effective().list });
}

function exportDocs(mode: 'zip' | 'single' | 'one', ids: string[]) {
  S.docMode = mode;
  const comps = S.docTokens ? [...new Set(ids.map((id) => S.docs.find((d) => d.id === id)?.component).filter(Boolean) as string[])] : [];
  const extra = S.presets.filter((p) => !p.origin || p.origin === 'new');
  S.busy = 'docs';
  send({ type: 'docs-export', docIds: ids, tokenComponents: comps, extra });
}

function receiveDocs(files: ExportFile[]) {
  const stamp = new Date().toISOString().slice(0, 10);
  if (S.docMode === 'zip') {
    saveBlob(`FEDS-docs-${stamp}.zip`, makeZip(files.map((f) => ({ name: `FEDS-docs/${f.name}`, content: f.content }))));
  } else if (S.docMode === 'single') {
    saveText(`FEDS-docs-${stamp}.md`, files.map((f) => f.content).join('\n\n---\n\n'));
  } else {
    const doc = files.find((f) => f.name !== 'README.md');
    const all = files.filter((f) => f.name !== 'README.md').map((f) => f.content).join('\n\n---\n\n');
    saveText(`${doc?.name.split('/').pop() ?? 'doc.md'}`, all);
  }
}

// ---------------------------------------------------------------- события
document.addEventListener('click', (ev) => {
  const el = (ev.target as HTMLElement).closest('[data-act]') as HTMLElement | null;
  if (!el || (el as HTMLButtonElement).disabled) return;
  const act = el.dataset.act;
  S.error = '';
  switch (act) {
    case 'go':
      S.step = el.dataset.s as Step;
      if (S.step === 'tokens' && S.sel.size && !S.diff && !S.busy) requestDiff();
      break;
    case 'analyze': S.busy = 'analyze'; send({ type: 'analyze' }); break;
    case 'catalog': S.statusBusy = true; send({ type: 'catalog' }); break;
    case 'pick': {
      const c = el.dataset.c!;
      S.sel.has(c) ? S.sel.delete(c) : S.sel.add(c);
      S.diff = null; S.change.clear(); S.remove.clear();
      break;
    }
    case 'pick-group':
      S.presets.filter((p) => groupOf(p) === el.dataset.g).forEach((p) => S.sel.add(p.component));
      S.diff = null;
      break;
    case 'unpick-group':
      S.presets.filter((p) => groupOf(p) === el.dataset.g).forEach((p) => S.sel.delete(p.component));
      S.diff = null;
      break;
    case 'diff': requestDiff(); break;
    case 'filter': S.filter = el.dataset.f!; break;
    case 'toggle-change': { const n = el.dataset.name!; S.change.has(n) ? S.change.delete(n) : S.change.add(n); break; }
    case 'toggle-remove': { const n = el.dataset.name!; S.remove.has(n) ? S.remove.delete(n) : S.remove.add(n); break; }
    case 'apply':
      if (S.change.size || S.remove.size) S.modal = 'confirm';
      else doApply();
      break;
    case 'apply-confirmed': S.modal = null; doApply(); break;
    case 'recheck': S.step = 'tokens'; S.diff = null; requestDiff(); break;
    case 'bsel': { const c = el.dataset.c!; S.buildSel.has(c) ? S.buildSel.delete(c) : S.buildSel.add(c); break; }
    case 'bopt': {
      const o = optsOf(el.dataset.c!);
      const k = el.dataset.k as 'master' | 'spec';
      o[k] = !o[k];
      S.buildSel.add(el.dataset.c!);
      break;
    }
    case 'build': {
      const items = S.builds.filter((b) => S.buildSel.has(b.component)).map((b) => ({ component: b.component, ...optsOf(b.component) }))
        .filter((i) => i.master || i.spec);
      S.busy = 'build';
      S.progress = items.some((i) => i.master) ? { done: 0, total: 1 } : null;
      send({ type: 'build', items });
      break;
    }
    case 'doc': { const id = el.dataset.id!; S.docSel.has(id) ? S.docSel.delete(id) : S.docSel.add(id); break; }
    case 'doc-all': S.docs.forEach((d) => S.docSel.add(d.id)); break;
    case 'doc-none': S.docSel.clear(); break;
    case 'doc-group': S.docs.filter((d) => d.group === el.dataset.g).forEach((d) => S.docSel.add(d.id)); break;
    case 'doc-from-sel': S.docSel = new Set(S.docs.filter((d) => S.sel.has(d.component)).map((d) => d.id)); break;
    case 'doc-tokens': S.docTokens = !S.docTokens; break;
    case 'doc-one': ev.preventDefault(); exportDocs('one', [el.dataset.id!]); return;
    case 'doc-export': exportDocs(el.dataset.m as 'zip' | 'single', [...S.docSel]); break;
    case 'dl-analysis': saveText('feds-analysis.md', S.analysisMd); break;
    case 'dl-diff': saveText('feds-diff.md', S.diffMd); break;
    case 'dl-report': saveText('feds-report.md', S.reportMd); break;
    case 'settings': S.modal = 'settings'; break;
    case 'close': S.modal = null; break;
    case 'save-settings': {
      const v = (id: string) => (document.getElementById(id) as HTMLInputElement).value.trim();
      S.conv = { collections: { l1: v('c-l1'), l2: v('c-l2'), l3: v('c-l3') }, modes: { light: v('m-l'), dark: v('m-d') }, segment: v('seg') };
      send({ type: 'save-conventions', conventions: S.conv });
      S.modal = null; S.analysis = null; S.diff = null;
      S.statusBusy = true; send({ type: 'catalog' });
      break;
    }
    default: return;
  }
  render();
});

function doApply() {
  S.busy = 'apply';
  S.progress = { done: 0, total: 1 };
  send({ type: 'apply', presets: effective().list, approvals: { change: [...S.change], remove: [...S.remove] } });
}

window.onmessage = (ev: MessageEvent) => {
  const msg = ev.data.pluginMessage as ToUI;
  if (!msg) return;
  switch (msg.type) {
    case 'init':
      S.presets = msg.presets; S.docs = msg.docs; S.builds = msg.builds; S.conv = msg.conventions; S.fileName = msg.fileName; S.version = msg.version;
      S.statusBusy = true; send({ type: 'catalog' });
      break;
    case 'analysis': S.analysis = msg.analysis; S.analysisMd = msg.markdown; S.busy = ''; break;
    case 'catalog': S.statuses = new Map(msg.statuses.map((s) => [s.component, s])); S.statusBusy = false; break;
    case 'diff': S.diff = msg.diff; S.diffMd = msg.markdown; S.busy = ''; break;
    case 'progress': S.progress = { done: msg.done, total: msg.total }; break;
    case 'applied':
      S.report = msg.report; S.reportMd = msg.markdown; S.busy = ''; S.progress = null;
      S.diff = null; S.change.clear(); S.remove.clear(); S.step = 'report';
      S.statusBusy = true; send({ type: 'catalog' });
      break;
    case 'docs': S.busy = ''; receiveDocs(msg.files); break;
    case 'built': S.buildReport = msg.report; S.busy = ''; S.progress = null; S.step = 'report'; break;
    case 'error': S.error = msg.message; S.busy = ''; S.progress = null; S.statusBusy = false; break;
  }
  render();
};

render();
send({ type: 'init' });
