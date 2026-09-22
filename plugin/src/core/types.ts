// Общие типы ядра FEDS. Ядро не зависит от `figma` и тестируется в Node.

export type VarType = 'COLOR' | 'FLOAT' | 'STRING' | 'BOOLEAN';

export interface RGBA { r: number; g: number; b: number; a: number }

/** Значение переменной в одном режиме: ссылка на другую переменную или сырое значение. */
export type ModeValue =
  | { kind: 'alias'; id: string }
  | { kind: 'value'; value: number | string | boolean | RGBA };

export interface SnapVariable {
  id: string;
  name: string;
  collectionId: string;
  type: VarType;
  scopes: string[];
  hidden: boolean;
  description: string;
  remote: boolean;
  /** modeId → значение */
  values: Record<string, ModeValue>;
}

export interface SnapCollection {
  id: string;
  name: string;
  modes: { id: string; name: string }[];
  defaultModeId: string;
}

export interface SnapStyle { id: string; name: string; kind: 'TEXT' | 'EFFECT'; boundVars?: Record<string, string> }

/** Плоский снимок файла: всё, что нужно ядру для анализа и диффа. */
export interface Snapshot {
  collections: SnapCollection[];
  variables: SnapVariable[];
  styles: SnapStyle[];
  components?: { name: string; page: string }[];
}

export interface Conventions {
  collections: { l1: string; l2: string; l3: string };
  modes: { light: string; dark: string };
  segment: string; // регулярка сегмента имени
}

export const DEFAULT_CONVENTIONS: Conventions = {
  collections: { l1: '1. Primitives', l2: '2. General', l3: '3. Components' },
  modes: { light: 'light', dark: 'dark' },
  segment: '^-?[a-z0-9]+(-[a-z0-9]+)*$',
};

// ---------------------------------------------------------------- пресет
export interface PresetL1 {
  name: string;
  type: 'COLOR' | 'FLOAT';
  /** Цвет — hex (#rrggbb или #rrggbbaa), число — как есть. */
  value: string | number;
  scopes: string[];
  hidden?: boolean;
  description?: string;
}

export interface PresetL2 {
  name: string;
  type: 'COLOR' | 'FLOAT';
  scopes: string[];
  /** Имя примитива L1 или сырое число (только с записью в exceptions). */
  values: { light: string | number; dark: string | number };
  hidden?: boolean;
  description?: string;
  /** Одобренное изменение: прежние значения (null — новый L2 в существующей системе) и причина. */
  change?: { was: { light: string | number; dark: string | number } | null; approved: string };
}

export interface PresetL3 {
  name: string;
  type: 'COLOR' | 'FLOAT';
  alias: string;
  scopes: string[];
  description?: string;
  /** Одобренное автором изменение существующего токена: прежний алиас и причина. В диффе — «отличается», записывается только с подтверждением. */
  change?: { was: string | null; approved: string };
}

export interface PresetTextStyle {
  name: string;
  fontFamily?: string;
  fontStyle?: string;
  vars: { fontSize: string; lineHeight: string; letterSpacing: string; fontWeight: string };
}

export interface Preset {
  component: string;
  roots?: string[];
  /** Явные префиксы L3, которыми владеет пресет (для поиска «лишних»). */
  prefixes?: string[];
  /** existing — снят с текущей системы; new — новый компонент. */
  origin?: 'existing' | 'new';
  /** Путь к исходной документации в проекте. */
  doc?: string;
  /** Пресеты, чьи L2 нужны этому пресету (вычисляется при сборке каталога). */
  requires?: string[];
  title?: string;
  kind?: 'component' | 'block' | 'system' | 'part';
  /** Для kind = part: чья это часть. Часть не показывается в каталоге отдельно, её подключают владельцы. */
  partOf?: string[];
  /** Пресеты, которые подключаются вместе с этим явно (сверх вычисленных по L2): например, общий список Dropdown. */
  includes?: string[];
  analog?: string;
  source?: string;
  axes?: Record<string, string[]>;
  parts?: string[];
  l1?: PresetL1[];
  l2?: PresetL2[];
  l3: PresetL3[];
  textStyles?: PresetTextStyle[];
  contrast?: { fg: string; bg: string; kind: 'text' | 'graphic'; over?: string; accepted?: boolean }[];
  exceptions?: { token: string; reason: string }[];
  decisions?: string[];
}

// ---------------------------------------------------------------- дифф
export type DiffStatus = 'add' | 'same' | 'changed' | 'extra' | 'blocked';

export interface DiffRow {
  level: 1 | 2 | 3 | 'style';
  name: string;
  status: DiffStatus;
  /** Что будет (для add/changed) */
  target?: string;
  /** Что сейчас (для changed/extra) */
  current?: string;
  reasons?: string[];
  existingId?: string;
}

export interface ContrastRow { fg: string; bg: string; mode: string; ratio: number; need: number; ok: boolean; accepted: boolean }

export interface DiffResult {
  component: string;
  /** Коллекции, которых нет в файле и которые будут созданы. */
  createCollections: string[];
  rows: DiffRow[];
  errors: string[];
  warnings: string[];
  contrast: ContrastRow[];
}

/** Что пользователь разрешил сверх безопасного добавления. */
export interface Approvals { change: string[]; remove: string[] }

export interface Plan {
  component: string;
  createCollections: string[];
  createL1: PresetL1[];
  updateL1: PresetL1[];
  createL2: PresetL2[];
  updateL2: PresetL2[];
  createL3: PresetL3[];
  updateL3: PresetL3[];
  remove: { id: string; name: string }[];
  createStyles: PresetTextStyle[];
  exceptions: string[];
}

export interface ApplyReport {
  component: string;
  created: string[];
  updated: string[];
  removed: string[];
  skipped: string[];
  styles: string[];
  warnings: string[];
  errors: string[];
}
