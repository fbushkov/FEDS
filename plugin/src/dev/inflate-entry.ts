// Отладочный вход: распаковка сжатых (zlib + base64) пакетов для прогона в тестовом файле через Figma MCP.
import { strFromU8, unzlibSync } from 'fflate';

(globalThis as unknown as Record<string, unknown>).FEDS_INFLATE = (b64: string): string => strFromU8(unzlibSync(figma.base64Decode(b64)));
