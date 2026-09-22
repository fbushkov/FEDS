# Токены: Divider

Пресет: `presets/divider.tokens.json`. Источник: `input/tokens/variables.json`. Аналог: `—`.

Статус проверки: **OK** · L2 новых: 41 · L3: 44 · текстовых стилей: 2

## Заметки

- Пресет снят с текущей системы; проверена сверка с индексом один к одному.

## Новые токены L2 (`2. General`)

| Токен | light | dark | scopes |
|---|---|---|---|
| `border/divider/l` | `border/3` | `border/3` | STROKE_FLOAT |
| `border/divider/m` | `border/2` | `border/2` | STROKE_FLOAT |
| `border/divider/s` | `border/1` | `border/1` | STROKE_FLOAT |
| `gap/divider/m` | `space/0` | `space/0` | GAP |
| `gap/divider/s` | `space/0` | `space/0` | GAP |
| `gap/divider/xs` | `space/0` | `space/0` | GAP |
| `radius/divider/circle` | `radius/999` | `radius/999` | CORNER_RADIUS |
| `radius/divider/none` | `radius/0` | `radius/0` | CORNER_RADIUS |
| `size/divider/label/m` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `size/divider/label/s` | `size/16` | `size/16` | WIDTH_HEIGHT |
| `size/divider/padding/12` | `size/12` | `size/12` | WIDTH_HEIGHT |
| `size/divider/padding/16` | `size/16` | `size/16` | WIDTH_HEIGHT |
| `size/divider/padding/20` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `size/divider/padding/24` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `size/divider/padding/32` | `size/32` | `size/32` | WIDTH_HEIGHT |
| `size/divider/padding/4` | `size/4` | `size/4` | WIDTH_HEIGHT |
| `size/divider/padding/40` | `size/40` | `size/40` | WIDTH_HEIGHT |
| `size/divider/padding/8` | `size/8` | `size/8` | WIDTH_HEIGHT |
| `size/divider/thickness/l` | `size/3` | `size/3` | WIDTH_HEIGHT |
| `size/divider/thickness/m` | `size/2` | `size/2` | WIDTH_HEIGHT |
| `size/divider/thickness/s` | `size/1` | `size/1` | WIDTH_HEIGHT |
| `space/divider/box/x/m` | `space/0` | `space/0` | GAP |
| `space/divider/box/x/s` | `space/0` | `space/0` | GAP |
| `space/divider/box/x/xs` | `space/0` | `space/0` | GAP |
| `space/divider/box/y/m` | `space/0` | `space/0` | GAP |
| `space/divider/box/y/s` | `space/0` | `space/0` | GAP |
| `space/divider/box/y/xs` | `space/0` | `space/0` | GAP |
| `space/divider/label/x/m` | `space/12` | `space/12` | GAP |
| `space/divider/label/x/s` | `space/8` | `space/8` | GAP |
| `space/divider/label/y/m-bottom` | `space/0` | `space/0` | GAP |
| `space/divider/label/y/m-top` | `space/0` | `space/0` | GAP |
| `space/divider/label/y/s-bottom` | `space/0` | `space/0` | GAP |
| `space/divider/label/y/s-top` | `space/0` | `space/0` | GAP |
| `typography/divider/m/letter-spacing` | `font/letter-spacing/10` | `font/letter-spacing/10` | LETTER_SPACING |
| `typography/divider/m/line-height` | `font/line-height/20` | `font/line-height/20` | LINE_HEIGHT |
| `typography/divider/m/size` | `font/size/14` | `font/size/14` | FONT_SIZE |
| `typography/divider/m/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |
| `typography/divider/s/letter-spacing` | `font/letter-spacing/25` | `font/letter-spacing/25` | LETTER_SPACING |
| `typography/divider/s/line-height` | `font/line-height/16` | `font/line-height/16` | LINE_HEIGHT |
| `typography/divider/s/size` | `font/size/12` | `font/size/12` | FONT_SIZE |
| `typography/divider/s/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |

## Токены L3 (`3. Components`)

| Токен | → L2 | light | dark | scope |
|---|---|---|---|---|
| `divider/label/dark` | `color/static/text/base/hard` | rgba(0,0,0,0.85) | rgba(255,255,255,1.00) | TEXT_FILL |
| `divider/label/light` | `color/static/text/base/light` | rgba(0,0,0,0.45) | rgba(255,255,255,0.45) | TEXT_FILL |
| `divider/label/middle` | `color/static/text/base/medium` | rgba(0,0,0,0.60) | rgba(255,255,255,0.70) | TEXT_FILL |
| `divider/line/intense` | `color/static/border/base/low` | rgba(0,0,0,0.20) | rgba(255,255,255,0.20) | STROKE_COLOR |
| `divider/line/regular` | `color/static/border/base/light` | rgba(0,0,0,0.10) | rgba(255,255,255,0.10) | STROKE_COLOR |
| `divider/line/strong` | `color/static/border/base/quiet` | rgba(0,0,0,0.15) | rgba(255,255,255,0.15) | STROKE_COLOR |
| `divider/line/subtle` | `color/static/border/base/mild` | rgba(0,0,0,0.05) | rgba(255,255,255,0.05) | STROKE_COLOR |
| `divider/size/label/m/box` | `size/divider/label/m` | 20 | 20 | WIDTH_HEIGHT |
| `divider/size/label/m/x` | `space/divider/label/x/m` | 12 | 12 | GAP |
| `divider/size/label/m/y-bottom` | `space/divider/label/y/m-bottom` | 0 | 0 | GAP |
| `divider/size/label/m/y-top` | `space/divider/label/y/m-top` | 0 | 0 | GAP |
| `divider/size/label/s/box` | `size/divider/label/s` | 16 | 16 | WIDTH_HEIGHT |
| `divider/size/label/s/x` | `space/divider/label/x/s` | 8 | 8 | GAP |
| `divider/size/label/s/y-bottom` | `space/divider/label/y/s-bottom` | 0 | 0 | GAP |
| `divider/size/label/s/y-top` | `space/divider/label/y/s-top` | 0 | 0 | GAP |
| `divider/size/m/border` | `border/divider/l` | 3 | 3 | STROKE_FLOAT |
| `divider/size/m/box` | `size/divider/thickness/l` | 3 | 3 | WIDTH_HEIGHT |
| `divider/size/m/gap` | `gap/divider/m` | 0 | 0 | GAP |
| `divider/size/m/radius-circle` | `radius/divider/circle` | 999 | 999 | CORNER_RADIUS |
| `divider/size/m/radius-none` | `radius/divider/none` | 0 | 0 | CORNER_RADIUS |
| `divider/size/m/x` | `space/divider/box/x/m` | 0 | 0 | GAP |
| `divider/size/m/y` | `space/divider/box/y/m` | 0 | 0 | GAP |
| `divider/size/padding/12` | `size/divider/padding/12` | 12 | 12 | WIDTH_HEIGHT |
| `divider/size/padding/16` | `size/divider/padding/16` | 16 | 16 | WIDTH_HEIGHT |
| `divider/size/padding/20` | `size/divider/padding/20` | 20 | 20 | WIDTH_HEIGHT |
| `divider/size/padding/24` | `size/divider/padding/24` | 24 | 24 | WIDTH_HEIGHT |
| `divider/size/padding/32` | `size/divider/padding/32` | 32 | 32 | WIDTH_HEIGHT |
| `divider/size/padding/4` | `size/divider/padding/4` | 4 | 4 | WIDTH_HEIGHT |
| `divider/size/padding/40` | `size/divider/padding/40` | 40 | 40 | WIDTH_HEIGHT |
| `divider/size/padding/8` | `size/divider/padding/8` | 8 | 8 | WIDTH_HEIGHT |
| `divider/size/s/border` | `border/divider/m` | 2 | 2 | STROKE_FLOAT |
| `divider/size/s/box` | `size/divider/thickness/m` | 2 | 2 | WIDTH_HEIGHT |
| `divider/size/s/gap` | `gap/divider/s` | 0 | 0 | GAP |
| `divider/size/s/radius-circle` | `radius/divider/circle` | 999 | 999 | CORNER_RADIUS |
| `divider/size/s/radius-none` | `radius/divider/none` | 0 | 0 | CORNER_RADIUS |
| `divider/size/s/x` | `space/divider/box/x/s` | 0 | 0 | GAP |
| `divider/size/s/y` | `space/divider/box/y/s` | 0 | 0 | GAP |
| `divider/size/xs/border` | `border/divider/s` | 1 | 1 | STROKE_FLOAT |
| `divider/size/xs/box` | `size/divider/thickness/s` | 1 | 1 | WIDTH_HEIGHT |
| `divider/size/xs/gap` | `gap/divider/xs` | 0 | 0 | GAP |
| `divider/size/xs/radius-circle` | `radius/divider/circle` | 999 | 999 | CORNER_RADIUS |
| `divider/size/xs/radius-none` | `radius/divider/none` | 0 | 0 | CORNER_RADIUS |
| `divider/size/xs/x` | `space/divider/box/x/xs` | 0 | 0 | GAP |
| `divider/size/xs/y` | `space/divider/box/y/xs` | 0 | 0 | GAP |

## Текстовые стили

| Стиль | Шрифт | Переменные |
|---|---|---|
| `typography/divider/m` | Roboto Regular | `typography/divider/m/size`, `typography/divider/m/line-height`, `typography/divider/m/letter-spacing`, `typography/divider/m/weight` |
| `typography/divider/s` | Roboto Regular | `typography/divider/s/size`, `typography/divider/s/line-height`, `typography/divider/s/letter-spacing`, `typography/divider/s/weight` |

## Решения и допущения

- Пресет снят с текущей системы: повторная запись в исходный файл должна дать 0 изменений.
