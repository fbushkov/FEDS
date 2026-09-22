// Поиск ресурсов для сборки: сначала локальные в файле, затем подключённая библиотека.
// Переменные — через teamLibrary (опубликованные), стили и иконки — по ключам src/library-keys.json.
import keys from '../library-keys.json';

/** Владелец вариантов: набор или одиночный компонент без осей. */
export type Owner = ComponentSetNode | ComponentNode;

export class Library {
  private vars = new Map<string, Variable>();
  private libVars?: Map<string, string>;
  private styles = new Map<string, TextStyle | null>();
  private icons = new Map<string, ComponentNode | null>();
  private sets = new Map<string, Owner>();
  private fonts = new Set<string>();
  readonly missing = { variables: new Set<string>(), styles: new Set<string>(), icons: new Set<string>(), sets: new Set<string>() };

  async init() {
    for (const v of await figma.variables.getLocalVariablesAsync()) if (!this.vars.has(v.name)) this.vars.set(v.name, v);
  }

  private async libraryIndex(): Promise<Map<string, string>> {
    if (this.libVars) return this.libVars;
    this.libVars = new Map();
    try {
      const cols = await figma.teamLibrary.getAvailableLibraryVariableCollectionsAsync();
      for (const c of cols) {
        for (const v of await figma.teamLibrary.getVariablesInLibraryCollectionAsync(c.key)) {
          if (!this.libVars.has(v.name)) this.libVars.set(v.name, v.key);
        }
      }
    } catch {
      /* библиотеки недоступны — работаем только с локальными */
    }
    return this.libVars;
  }

  async variable(name: string): Promise<Variable | null> {
    const local = this.vars.get(name);
    if (local) return local;
    const key = (await this.libraryIndex()).get(name);
    if (key) {
      try {
        const v = await figma.variables.importVariableByKeyAsync(key);
        this.vars.set(name, v);
        return v;
      } catch { /* нет доступа */ }
    }
    this.missing.variables.add(name);
    return null;
  }

  async textStyle(name: string): Promise<TextStyle | null> {
    if (this.styles.has(name)) return this.styles.get(name)!;
    let s: TextStyle | null = (await figma.getLocalTextStylesAsync()).find((x) => x.name === name) ?? null;
    const key = (keys.styles as Record<string, string>)[name];
    if (!s && key) {
      try { s = await figma.importStyleByKeyAsync(key) as TextStyle; } catch { s = null; }
    }
    if (s) await this.font(s.fontName);
    else this.missing.styles.add(name);
    this.styles.set(name, s);
    return s;
  }

  async font(f: FontName) {
    const k = f.family + '|' + f.style;
    if (this.fonts.has(k)) return;
    await figma.loadFontAsync(f);
    this.fonts.add(k);
  }

  private iconPage?: PageNode | null;

  async icon(name: string): Promise<ComponentNode | null> {
    if (this.icons.has(name)) return this.icons.get(name)!;
    if (this.iconPage === undefined) {
      this.iconPage = figma.root.children.find((p) => p.name.trim().toLowerCase() === 'icons') ?? null;
      if (this.iconPage) await this.iconPage.loadAsync();
    }
    let c: ComponentNode | null = null;
    if (this.iconPage) {
      c = this.iconPage.findOne((n) => n.type === 'COMPONENT' && n.name === name && n.parent?.type !== 'COMPONENT_SET') as ComponentNode | null;
    }
    const key = (keys.icons as Record<string, string>)[name];
    if (!c && key) {
      try { c = await figma.importComponentByKeyAsync(key); } catch { c = null; }
    }
    if (!c) this.missing.icons.add(name);
    this.icons.set(name, c);
    return c;
  }

  private themes = new Map<string, { collection: VariableCollection; modeId: string } | null>();

  /** Режим темы коллекции `2. General` (light / dark) — для закрепления темы на узле (explicit mode). */
  async theme(name: 'light' | 'dark'): Promise<{ collection: VariableCollection; modeId: string } | null> {
    if (this.themes.has(name)) return this.themes.get(name)!;
    const probe = await this.variable('color/bg/section/main');
    const collection = probe ? await figma.variables.getVariableCollectionByIdAsync(probe.variableCollectionId) : null;
    const mode = collection?.modes.find((m) => m.name.trim().toLowerCase() === name);
    const out = collection && mode ? { collection, modeId: mode.modeId } : null;
    this.themes.set(name, out);
    return out;
  }

  register(set: Owner) {
    this.sets.set(set.name, set);
  }

  /** Набор: только что собранный этим запуском или существующий в файле. */
  async set(name: string): Promise<Owner | null> {
    if (this.sets.has(name)) return this.sets.get(name)!;
    for (const page of figma.root.children) {
      await page.loadAsync();
      // набор вариантов или одиночный компонент (не вариант набора)
      const found = page.findAllWithCriteria({ types: ['COMPONENT_SET', 'COMPONENT'] })
        .find((s) => s.name === name && (s.type === 'COMPONENT_SET' || s.parent?.type !== 'COMPONENT_SET')) as Owner | undefined;
      if (found) {
        this.sets.set(name, found);
        return found;
      }
    }
    this.missing.sets.add(name);
    return null;
  }
}

export function solidPaint(): SolidPaint {
  return { type: 'SOLID', color: { r: 0.5, g: 0.5, b: 0.5 } };
}

export async function boundPaint(lib: Library, name: string): Promise<SolidPaint | null> {
  const v = await lib.variable(name);
  return v ? figma.variables.setBoundVariableForPaint(solidPaint(), 'color', v) : null;
}
