import type { RGBA } from './types';

function channel(x: number): number {
  return x <= 0.03928 ? x / 12.92 : Math.pow((x + 0.055) / 1.055, 2.4);
}

export function luminance(c: RGBA): number {
  return 0.2126 * channel(c.r) + 0.7152 * channel(c.g) + 0.0722 * channel(c.b);
}

/** Наложение полупрозрачного цвета на непрозрачный фон. */
export function blend(fg: RGBA, bg: RGBA): RGBA {
  const a = fg.a ?? 1;
  return { r: fg.r * a + bg.r * (1 - a), g: fg.g * a + bg.g * (1 - a), b: fg.b * a + bg.b * (1 - a), a: 1 };
}

export function contrastRatio(fg: RGBA, bg: RGBA): number {
  const [hi, lo] = [luminance(fg), luminance(bg)].sort((a, b) => b - a);
  return (hi + 0.05) / (lo + 0.05);
}

/** Контраст с учётом прозрачности: фон кладётся на подложку, текст — на результат. */
export function effectiveContrast(fg: RGBA, bg: RGBA, base: RGBA = { r: 1, g: 1, b: 1, a: 1 }): number {
  const solidBg = blend(bg, base);
  return contrastRatio(blend(fg, solidBg), solidBg);
}
