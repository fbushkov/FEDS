// Отладочная сборка для MCP: только спецификация (меньше кода на вызов).
import { Library } from '../figma/library';
import { renderSpec } from '../figma/spec';
import { buildSet } from '../figma/builder';

(globalThis as unknown as { FEDS: unknown }).FEDS = { Library, renderSpec, buildSet };
