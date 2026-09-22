# Токены: Link

Пресет: `presets/link.tokens.json`. Источник: `input/tokens/variables.json`. Аналог: `—`.

Статус проверки: **OK** · L2 новых: 43 · L3: 60 · текстовых стилей: 8

## Заметки

- Пресет снят с текущей системы; проверена сверка с индексом один к одному.

## Новые токены L2 (`2. General`)

| Токен | light | dark | scopes |
|---|---|---|---|
| `border/link/focus-bold` | `border/2` | `border/2` | STROKE_FLOAT |
| `border/link/focus-regular` | `border/1` | `border/1` | STROKE_FLOAT |
| `gap/link/l` | `space/6` | `space/6` | GAP |
| `gap/link/m` | `space/4` | `space/4` | GAP |
| `gap/link/s` | `space/2` | `space/2` | GAP |
| `gap/link/xl` | `space/8` | `space/8` | GAP |
| `radius/link/box` | `radius/0` | `radius/0` | CORNER_RADIUS |
| `radius/link/focus/l` | `radius/12` | `radius/12` | CORNER_RADIUS |
| `radius/link/focus/m` | `radius/7` | `radius/9` | CORNER_RADIUS |
| `radius/link/focus/s` | `radius/7` | `radius/7` | CORNER_RADIUS |
| `radius/link/focus/xl` | `radius/14` | `radius/14` | CORNER_RADIUS |
| `size/link/l` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `size/link/l-icon` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `size/link/m` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `size/link/m-icon` | `size/16` | `size/16` | WIDTH_HEIGHT |
| `size/link/s` | `size/16` | `size/16` | WIDTH_HEIGHT |
| `size/link/s-icon` | `size/14` | `size/14` | WIDTH_HEIGHT |
| `size/link/xl` | `size/28` | `size/28` | WIDTH_HEIGHT |
| `size/link/xl-icon` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `space/link/x/l` | `space/0` | `space/0` | GAP |
| `space/link/x/m` | `space/0` | `space/0` | GAP |
| `space/link/x/s` | `space/0` | `space/0` | GAP |
| `space/link/x/xl` | `space/0` | `space/0` | GAP |
| `space/link/y/l` | `space/0` | `space/0` | GAP |
| `space/link/y/m` | `space/0` | `space/0` | GAP |
| `space/link/y/s` | `space/0` | `space/0` | GAP |
| `space/link/y/xl` | `space/0` | `space/0` | GAP |
| `typography/link/l/letter-spacing` | `font/letter-spacing/0` | `font/letter-spacing/0` | LETTER_SPACING |
| `typography/link/l/line-height` | `font/line-height/24` | `font/line-height/24` | LINE_HEIGHT |
| `typography/link/l/size` | `font/size/16` | `font/size/16` | FONT_SIZE |
| `typography/link/l/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |
| `typography/link/m/letter-spacing` | `font/letter-spacing/0` | `font/letter-spacing/0` | LETTER_SPACING |
| `typography/link/m/line-height` | `font/line-height/20` | `font/line-height/20` | LINE_HEIGHT |
| `typography/link/m/size` | `font/size/14` | `font/size/14` | FONT_SIZE |
| `typography/link/m/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |
| `typography/link/s/letter-spacing` | `font/letter-spacing/0` | `font/letter-spacing/0` | LETTER_SPACING |
| `typography/link/s/line-height` | `font/line-height/16` | `font/line-height/16` | LINE_HEIGHT |
| `typography/link/s/size` | `font/size/12` | `font/size/12` | FONT_SIZE |
| `typography/link/s/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |
| `typography/link/xl/letter-spacing` | `font/letter-spacing/0` | `font/letter-spacing/0` | LETTER_SPACING |
| `typography/link/xl/line-height` | `font/line-height/28` | `font/line-height/28` | LINE_HEIGHT |
| `typography/link/xl/size` | `font/size/18` | `font/size/18` | FONT_SIZE |
| `typography/link/xl/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |

## Токены L3 (`3. Components`)

| Токен | → L2 | light | dark | scope |
|---|---|---|---|---|
| `link/danger/icon/default` | `color/action/indicator/danger/firm/default` | rgba(240,48,48,1.00) | rgba(242,68,68,1.00) | SHAPE_FILL |
| `link/danger/icon/disabled` | `color/action/indicator/danger/firm/disabled` | rgba(240,48,48,0.40) | rgba(240,48,48,0.40) | SHAPE_FILL |
| `link/danger/icon/hover` | `color/action/indicator/danger/firm/hover` | rgba(219,44,44,1.00) | rgba(242,87,87,1.00) | SHAPE_FILL |
| `link/danger/icon/pressed` | `color/action/indicator/danger/firm/pressed` | rgba(199,36,36,1.00) | rgba(242,107,107,1.00) | SHAPE_FILL |
| `link/danger/text/default` | `color/action/text/danger/firm/default` | rgba(240,48,48,1.00) | rgba(242,68,68,1.00) | TEXT_FILL |
| `link/danger/text/disabled` | `color/action/text/danger/firm/disabled` | rgba(240,48,48,0.50) | rgba(240,48,48,0.50) | TEXT_FILL |
| `link/danger/text/hover` | `color/action/text/danger/firm/hover` | rgba(219,44,44,1.00) | rgba(242,87,87,1.00) | TEXT_FILL |
| `link/danger/text/pressed` | `color/action/text/danger/firm/pressed` | rgba(199,36,36,1.00) | rgba(242,107,107,1.00) | TEXT_FILL |
| `link/danger/text/visited` | `color/action/text/danger/firm/visited` | rgba(240,48,48,0.60) | rgba(240,48,48,0.60) | TEXT_FILL |
| `link/focus-ring` | `color/static/focus/brand` | rgba(39,129,243,1.00) | rgba(61,142,244,1.00) | STROKE_COLOR |
| `link/main/icon/default` | `color/action/indicator/brand/firm/default` | rgba(39,129,243,1.00) | rgba(61,142,244,1.00) | SHAPE_FILL |
| `link/main/icon/disabled` | `color/action/indicator/brand/firm/disabled` | rgba(39,129,243,0.50) | rgba(39,129,243,0.50) | SHAPE_FILL |
| `link/main/icon/hover` | `color/action/indicator/brand/firm/hover` | rgba(35,116,219,1.00) | rgba(82,154,245,1.00) | SHAPE_FILL |
| `link/main/icon/pressed` | `color/action/indicator/brand/firm/pressed` | rgba(31,103,194,1.00) | rgba(104,167,247,1.00) | SHAPE_FILL |
| `link/main/text/default` | `color/action/text/brand/firm/default` | rgba(39,129,243,1.00) | rgba(61,142,244,1.00) | TEXT_FILL |
| `link/main/text/disabled` | `color/action/text/brand/firm/disabled` | rgba(39,129,243,0.50) | rgba(39,129,243,0.50) | TEXT_FILL |
| `link/main/text/hover` | `color/action/text/brand/firm/hover` | rgba(35,116,219,1.00) | rgba(82,154,245,1.00) | TEXT_FILL |
| `link/main/text/pressed` | `color/action/text/brand/firm/pressed` | rgba(31,103,194,1.00) | rgba(104,167,247,1.00) | TEXT_FILL |
| `link/main/text/visited` | `color/action/text/brand/firm/visited` | rgba(39,129,243,0.60) | rgba(39,129,243,0.60) | TEXT_FILL |
| `link/secondary/icon/default` | `color/action/indicator/base/medium/default` | rgba(0,0,0,0.60) | rgba(255,255,255,0.70) | SHAPE_FILL |
| `link/secondary/icon/disabled` | `color/action/indicator/base/medium/disabled` | rgba(0,0,0,0.30) | rgba(255,255,255,0.30) | SHAPE_FILL |
| `link/secondary/icon/hover` | `color/action/indicator/base/medium/hover` | rgba(0,0,0,0.85) | rgba(255,255,255,0.90) | SHAPE_FILL |
| `link/secondary/icon/pressed` | `color/action/indicator/base/medium/pressed` | rgba(0,0,0,0.85) | rgba(255,255,255,0.90) | SHAPE_FILL |
| `link/secondary/text/default` | `color/action/text/base/medium/default` | rgba(0,0,0,0.60) | rgba(255,255,255,0.70) | TEXT_FILL |
| `link/secondary/text/disabled` | `color/action/text/base/medium/disabled` | rgba(0,0,0,0.35) | rgba(255,255,255,0.35) | TEXT_FILL |
| `link/secondary/text/hover` | `color/action/text/base/medium/hover` | rgba(0,0,0,0.85) | rgba(255,255,255,1.00) | TEXT_FILL |
| `link/secondary/text/pressed` | `color/action/text/base/medium/pressed` | rgba(0,0,0,0.85) | rgba(255,255,255,1.00) | TEXT_FILL |
| `link/secondary/text/visited` | `color/action/text/base/medium/visited` | rgba(0,0,0,0.45) | rgba(255,255,255,0.45) | TEXT_FILL |
| `link/size/l/box` | `size/link/l` | 24 | 24 | WIDTH_HEIGHT |
| `link/size/l/focus-border` | `border/link/focus-bold` | 2 | 2 | STROKE_FLOAT |
| `link/size/l/focus-radius` | `radius/link/focus/l` | 12 | 12 | CORNER_RADIUS |
| `link/size/l/gap` | `gap/link/l` | 6 | 6 | GAP |
| `link/size/l/icon` | `size/link/l-icon` | 20 | 20 | WIDTH_HEIGHT |
| `link/size/l/radius` | `radius/link/box` | 0 | 0 | CORNER_RADIUS |
| `link/size/l/x` | `space/link/x/l` | 0 | 0 | GAP |
| `link/size/l/y` | `space/link/y/l` | 0 | 0 | GAP |
| `link/size/m/box` | `size/link/m` | 20 | 20 | WIDTH_HEIGHT |
| `link/size/m/focus-border` | `border/link/focus-regular` | 1 | 1 | STROKE_FLOAT |
| `link/size/m/focus-radius` | `radius/link/focus/m` | 7 | 9 | CORNER_RADIUS |
| `link/size/m/gap` | `gap/link/m` | 4 | 4 | GAP |
| `link/size/m/icon` | `size/link/m-icon` | 16 | 16 | WIDTH_HEIGHT |
| `link/size/m/radius` | `radius/link/box` | 0 | 0 | CORNER_RADIUS |
| `link/size/m/x` | `space/link/x/m` | 0 | 0 | GAP |
| `link/size/m/y` | `space/link/y/m` | 0 | 0 | GAP |
| `link/size/s/box` | `size/link/s` | 16 | 16 | WIDTH_HEIGHT |
| `link/size/s/focus-border` | `border/link/focus-regular` | 1 | 1 | STROKE_FLOAT |
| `link/size/s/focus-radius` | `radius/link/focus/s` | 7 | 7 | CORNER_RADIUS |
| `link/size/s/gap` | `gap/link/s` | 2 | 2 | GAP |
| `link/size/s/icon` | `size/link/s-icon` | 14 | 14 | WIDTH_HEIGHT |
| `link/size/s/radius` | `radius/link/box` | 0 | 0 | CORNER_RADIUS |
| `link/size/s/x` | `space/link/x/s` | 0 | 0 | GAP |
| `link/size/s/y` | `space/link/y/s` | 0 | 0 | GAP |
| `link/size/xl/box` | `size/link/xl` | 28 | 28 | WIDTH_HEIGHT |
| `link/size/xl/focus-border` | `border/link/focus-bold` | 2 | 2 | STROKE_FLOAT |
| `link/size/xl/focus-radius` | `radius/link/focus/xl` | 14 | 14 | CORNER_RADIUS |
| `link/size/xl/gap` | `gap/link/xl` | 8 | 8 | GAP |
| `link/size/xl/icon` | `size/link/xl-icon` | 24 | 24 | WIDTH_HEIGHT |
| `link/size/xl/radius` | `radius/link/box` | 0 | 0 | CORNER_RADIUS |
| `link/size/xl/x` | `space/link/x/xl` | 0 | 0 | GAP |
| `link/size/xl/y` | `space/link/y/xl` | 0 | 0 | GAP |

## Текстовые стили

| Стиль | Шрифт | Переменные |
|---|---|---|
| `typography/action/link/regular/xl` | Roboto Regular | `typography/link/xl/size`, `typography/link/xl/line-height`, `typography/link/xl/letter-spacing`, `typography/link/xl/weight` |
| `typography/action/link/regular/l` | Roboto Regular | `typography/link/l/size`, `typography/link/l/line-height`, `typography/link/l/letter-spacing`, `typography/link/l/weight` |
| `typography/action/link/regular/m` | Roboto Regular | `typography/link/m/size`, `typography/link/m/line-height`, `typography/link/m/letter-spacing`, `typography/link/m/weight` |
| `typography/action/link/regular/s` | Roboto Regular | `typography/link/s/size`, `typography/link/s/line-height`, `typography/link/s/letter-spacing`, `typography/link/s/weight` |
| `typography/action/link/underline/xl` | Roboto Regular | `typography/link/xl/size`, `typography/link/xl/line-height`, `typography/link/xl/letter-spacing`, `typography/link/xl/weight` |
| `typography/action/link/underline/l` | Roboto Regular | `typography/link/l/size`, `typography/link/l/line-height`, `typography/link/l/letter-spacing`, `typography/link/l/weight` |
| `typography/action/link/underline/m` | Roboto Regular | `typography/link/m/size`, `typography/link/m/line-height`, `typography/link/m/letter-spacing`, `typography/link/m/weight` |
| `typography/action/link/underline/s` | Roboto Regular | `typography/link/s/size`, `typography/link/s/line-height`, `typography/link/s/letter-spacing`, `typography/link/s/weight` |

## Решения и допущения

- Пресет снят с текущей системы: повторная запись в исходный файл должна дать 0 изменений.
