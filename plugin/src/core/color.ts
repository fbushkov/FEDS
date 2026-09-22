import type { RGBA } from './types';

/** Цвет пресета: #rrggbb, #rrggbbaa или rgba(r,g,b,a) (r,g,b 0–255, a 0–1). */
export function hexToRgba(hex: string): RGBA | undefined {
  const rg = hex.trim().match(/^rgba?\(\s*([\d.]+)\s*,\s*([\d.]+)\s*,\s*([\d.]+)\s*(?:,\s*([\d.]+)\s*)?\)$/i);
  if (rg) return { r: +rg[1] / 255, g: +rg[2] / 255, b: +rg[3] / 255, a: rg[4] === undefined ? 1 : +rg[4] };
  const m = hex.trim().match(/^#([0-9a-f]{6})([0-9a-f]{2})?$/i);
  if (!m) return undefined;
  const n = parseInt(m[1], 16);
  return { r: ((n >> 16) & 255) / 255, g: ((n >> 8) & 255) / 255, b: (n & 255) / 255, a: m[2] ? parseInt(m[2], 16) / 255 : 1 };
}

export function rgbaToHex(c: RGBA): string {
  const h = (x: number) => Math.round(x * 255).toString(16).padStart(2, '0');
  const a = c.a ?? 1;
  return `#${h(c.r)}${h(c.g)}${h(c.b)}${a < 0.999 ? h(a) : ''}`;
}

/** Совпадение цветов с допуском в один шаг 8-битного канала. */
export function sameColor(a: RGBA, b: RGBA): boolean {
  const eps = 1 / 255 + 1e-6;
  return Math.abs(a.r - b.r) <= eps && Math.abs(a.g - b.g) <= eps && Math.abs(a.b - b.b) <= eps && Math.abs((a.a ?? 1) - (b.a ?? 1)) <= eps;
}
