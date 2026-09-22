import { hexToRgba } from '../core/color';
import type { ApplyReport, Conventions, Plan, PresetL1, PresetL2, PresetTextStyle } from '../core/types';

type Progress = (done: number, total: number, label: string) => void;

/** Публикация новых L2 — как у соседей в файле: типографика и цвет скрыты, размеры опубликованы. */
function hiddenL2(name: string): boolean {
  const root = name.split('/')[0];
  return root === 'typography' || root === 'color';
}

/** Варианты написания начертания: в файле встречается и «SemiBold», и «Semi Bold». */
function styleCandidates(style: string): string[] {
  const s = style.trim();
  return [...new Set([s, s.replace(/([a-z])([A-Z])/g, '$1 $2'), s.replace(/\s+/g, '')])];
}

/**
 * Запись плана в файл. Вся запись — один шаг отмены: commitUndo до и после.
 * Существующее меняется/удаляется только если попало в план по явному разрешению.
 */
export async function applyPlan(plan: Plan, conv: Conventions, progress: Progress): Promise<ApplyReport> {
  const report: ApplyReport = { component: plan.component, created: [], updated: [], removed: [], skipped: [], styles: [], warnings: [], errors: [] };
  figma.commitUndo();

  const cols = await figma.variables.getLocalVariableCollectionsAsync();
  const col = (n: string) => cols.find((c) => c.name === n);
  // Недостающие коллекции создаются (сборка с нуля). Существующие не меняются.
  const ensure = (name: string, modes: string[]): VariableCollection => {
    const found = col(name);
    if (found) return found;
    const c = figma.variables.createVariableCollection(name);
    c.renameMode(c.modes[0].modeId, modes[0]);
    for (const m of modes.slice(1)) c.addMode(m);
    cols.push(c);
    report.created.push(`коллекция «${name}» (${modes.join(', ')})`);
    return c;
  };
  const l1 = plan.createCollections.includes(conv.collections.l1) ? ensure(conv.collections.l1, ['Mode 1']) : col(conv.collections.l1);
  const l2 = plan.createCollections.includes(conv.collections.l2) ? ensure(conv.collections.l2, [conv.modes.light, conv.modes.dark]) : col(conv.collections.l2);
  const l3 = plan.createCollections.includes(conv.collections.l3) ? ensure(conv.collections.l3, ['Mode 1']) : col(conv.collections.l3);
  if (!l1 || !l2 || !l3) {
    report.errors.push('Не найдены коллекции уровней. Проверьте настройки.');
    return report;
  }
  const light = l2.modes.find((m) => m.name === conv.modes.light)?.modeId;
  const dark = l2.modes.find((m) => m.name === conv.modes.dark)?.modeId;
  if (!light || !dark) {
    report.errors.push(`В «${l2.name}» нет режимов ${conv.modes.light}/${conv.modes.dark}.`);
    return report;
  }

  const all = await figma.variables.getLocalVariablesAsync();
  const byName = (c: VariableCollection) => new Map(all.filter((v) => v.variableCollectionId === c.id).map((v) => [v.name, v]));
  const m1 = byName(l1);
  const m2 = byName(l2);
  const m3 = byName(l3);

  const total = plan.createL1.length + plan.updateL1.length + plan.createL2.length + plan.updateL2.length + plan.createL3.length + plan.updateL3.length + plan.remove.length + plan.createStyles.length;
  let done = 0;
  const tick = (label: string) => {
    done++;
    if (done % 10 === 0 || done === total) progress(done, total, label);
  };

  const setL1Value = (v: Variable, t: PresetL1) => {
    const val = t.type === 'COLOR' && typeof t.value === 'string' ? hexToRgba(t.value) : t.value;
    if (val === undefined) throw new Error(`неверное значение ${t.value}`);
    v.setValueForMode(l1.defaultModeId, val as VariableValue);
  };

  for (const t of plan.createL1) {
    try {
      if (m1.has(t.name)) { report.skipped.push(t.name); continue; }
      const v = figma.variables.createVariable(t.name, l1, t.type);
      v.scopes = t.scopes as VariableScope[];
      v.description = t.description ?? '';
      v.hiddenFromPublishing = t.hidden ?? true;
      setL1Value(v, t);
      m1.set(t.name, v);
      report.created.push(t.name);
    } catch (e) {
      report.errors.push(`L1 ${t.name}: ${(e as Error).message}`);
    }
    tick(t.name);
  }

  for (const t of plan.updateL1) {
    try {
      const v = m1.get(t.name);
      if (!v) throw new Error('не найдена');
      setL1Value(v, t);
      v.scopes = t.scopes as VariableScope[];
      report.updated.push(t.name);
    } catch (e) {
      report.errors.push(`L1 ${t.name}: ${(e as Error).message}`);
    }
    tick(t.name);
  }

  const setL2Values = (v: Variable, t: PresetL2) => {
    for (const [modeId, val] of [[light, t.values.light], [dark, t.values.dark]] as const) {
      if (typeof val === 'number') v.setValueForMode(modeId, val);
      else {
        const p = m1.get(val);
        if (!p) throw new Error(`примитив ${val} не найден`);
        v.setValueForMode(modeId, figma.variables.createVariableAlias(p));
      }
    }
  };

  for (const t of plan.createL2) {
    try {
      if (m2.has(t.name)) { report.skipped.push(t.name); continue; }
      const v = figma.variables.createVariable(t.name, l2, t.type);
      v.scopes = t.scopes as VariableScope[];
      v.description = t.description ?? '';
      v.hiddenFromPublishing = t.hidden ?? hiddenL2(t.name);
      setL2Values(v, t);
      m2.set(t.name, v);
      report.created.push(t.name);
    } catch (e) {
      report.errors.push(`L2 ${t.name}: ${(e as Error).message}`);
    }
    tick(t.name);
  }

  for (const t of plan.updateL2) {
    try {
      const v = m2.get(t.name);
      if (!v) throw new Error('не найдена');
      setL2Values(v, t);
      v.scopes = t.scopes as VariableScope[];
      report.updated.push(t.name);
    } catch (e) {
      report.errors.push(`L2 ${t.name}: ${(e as Error).message}`);
    }
    tick(t.name);
  }

  const aliasTarget = (name: string, token: string) => {
    const t = m2.get(name) ?? (plan.exceptions.includes(token) ? m1.get(name) : undefined);
    if (!t) throw new Error(`цель алиаса ${name} не найдена`);
    return figma.variables.createVariableAlias(t);
  };

  for (const t of plan.createL3) {
    try {
      if (m3.has(t.name)) { report.skipped.push(t.name); continue; }
      const v = figma.variables.createVariable(t.name, l3, t.type);
      v.scopes = t.scopes as VariableScope[];
      v.description = t.description ?? '';
      v.setValueForMode(l3.defaultModeId, aliasTarget(t.alias, t.name));
      m3.set(t.name, v);
      report.created.push(t.name);
    } catch (e) {
      report.errors.push(`L3 ${t.name}: ${(e as Error).message}`);
    }
    tick(t.name);
  }

  for (const t of plan.updateL3) {
    try {
      const v = m3.get(t.name);
      if (!v) throw new Error('не найдена');
      v.setValueForMode(l3.defaultModeId, aliasTarget(t.alias, t.name));
      v.scopes = t.scopes as VariableScope[];
      report.updated.push(t.name);
    } catch (e) {
      report.errors.push(`L3 ${t.name}: ${(e as Error).message}`);
    }
    tick(t.name);
  }

  for (const r of plan.remove) {
    try {
      const v = await figma.variables.getVariableByIdAsync(r.id);
      if (v) { v.remove(); report.removed.push(r.name); }
    } catch (e) {
      report.errors.push(`Удаление ${r.name}: ${(e as Error).message}`);
    }
    tick(r.name);
  }

  if (plan.createStyles.length) await createStyles(plan.createStyles, m2, report, tick);

  figma.commitUndo();
  return report;
}

async function createStyles(styles: PresetTextStyle[], m2: Map<string, Variable>, report: ApplyReport, tick: (l: string) => void) {
  const existing = new Set((await figma.getLocalTextStylesAsync()).map((s) => s.name));
  const fonts = await figma.listAvailableFontsAsync();
  for (const s of styles) {
    try {
      if (existing.has(s.name)) { report.skipped.push(s.name); continue; }
      const family = s.fontFamily ?? 'Roboto';
      const style = styleCandidates(s.fontStyle ?? 'Regular').find((c) => fonts.some((f) => f.fontName.family === family && f.fontName.style === c));
      if (!style) throw new Error(`шрифт ${family} ${s.fontStyle} недоступен`);
      await figma.loadFontAsync({ family, style });
      const ts = figma.createTextStyle();
      ts.name = s.name;
      ts.fontName = { family, style };
      const bind: [VariableBindableTextField, string][] = [
        ['fontSize', s.vars.fontSize], ['lineHeight', s.vars.lineHeight], ['letterSpacing', s.vars.letterSpacing], ['fontWeight', s.vars.fontWeight],
      ];
      for (const [field, name] of bind) {
        const v = m2.get(name);
        if (!v) { report.warnings.push(`Стиль ${s.name}: нет переменной ${name}, ${field} не привязан`); continue; }
        ts.setBoundVariable(field, v);
      }
      report.styles.push(s.name);
    } catch (e) {
      report.errors.push(`Стиль ${s.name}: ${(e as Error).message}`);
    }
    tick(s.name);
  }
}
