import type { Analysis } from './core/analyze';
import type { CatalogStatus } from './core/diff';
import type { Approvals, ApplyReport, Conventions, DiffResult, Preset } from './core/types';
import type { BuildItem, BuildReport } from './figma/run-build';

export interface BuildMeta {
  component: string; title: string; origin?: string; page?: string; requires: string[]; notes: string[];
  sets: { name: string; variants: number }[]; specColumns: string[];
}

export interface DocMeta { id: string; title: string; component: string; group: 'existing' | 'new'; source: string }
export interface ExportFile { name: string; content: string }

/** UI → main */
export type ToMain =
  | { type: 'init' }
  | { type: 'analyze' }
  | { type: 'catalog' }
  | { type: 'diff'; presets: Preset[] }
  | { type: 'apply'; presets: Preset[]; approvals: Approvals }
  | { type: 'docs-export'; docIds: string[]; tokenComponents: string[]; extra: Preset[] }
  | { type: 'build'; items: BuildItem[] }
  | { type: 'save-conventions'; conventions: Conventions }
  | { type: 'resize'; width: number; height: number };

/** main → UI */
export type ToUI =
  | { type: 'init'; presets: Preset[]; docs: DocMeta[]; builds: BuildMeta[]; conventions: Conventions; fileName: string; version: string }
  | { type: 'built'; report: BuildReport }
  | { type: 'analysis'; analysis: Analysis; markdown: string }
  | { type: 'catalog'; statuses: CatalogStatus[] }
  | { type: 'diff'; diff: DiffResult; markdown: string }
  | { type: 'progress'; done: number; total: number; label: string }
  | { type: 'applied'; report: ApplyReport; markdown: string }
  | { type: 'docs'; files: ExportFile[] }
  | { type: 'error'; message: string };
