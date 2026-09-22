// Отладочный вход: тот же сборщик и та же запись токенов, что в плагине, для прогона в тестовом файле через Figma MCP.
import { buildPlan, diffPreset, mergePresets } from '../core/diff';
import { DEFAULT_CONVENTIONS } from '../core/types';
import { applyPlan } from '../figma/apply';
import { buildSet } from '../figma/builder';
import { Library } from '../figma/library';
import { runBuild } from '../figma/run-build';
import { takeSnapshot } from '../figma/scan';
import { renderSpec } from '../figma/spec';

(globalThis as unknown as Record<string, unknown>).FEDS = {
  runBuild, buildSet, Library, renderSpec, mergePresets, diffPreset, buildPlan, applyPlan, takeSnapshot, DEFAULT_CONVENTIONS,
};
