# Токены: Badge

Пресет: `presets/badge.tokens.json`. Источник: `input/tokens/variables.json`. Аналог: `—`.

Статус проверки: **OK** · L2 новых: 56 · L3: 121 · текстовых стилей: 4

## Заметки

- Пресет снят с текущей системы; проверена сверка с индексом один к одному.

## Новые токены L2 (`2. General`)

| Токен | light | dark | scopes |
|---|---|---|---|
| `border/badge/box/m` | `border/1` | `border/1` | STROKE_FLOAT |
| `border/badge/box/s` | `border/1` | `border/1` | STROKE_FLOAT |
| `border/badge/focus/m` | `border/2` | `border/2` | STROKE_FLOAT |
| `border/badge/focus/s` | `border/1` | `border/1` | STROKE_FLOAT |
| `gap/badge/m` | `space/2` | `space/2` | GAP |
| `gap/badge/s` | `space/2` | `space/2` | GAP |
| `radius/badge/box/circle` | `radius/999` | `radius/999` | CORNER_RADIUS |
| `radius/badge/box/m-square` | `radius/4` | `radius/4` | CORNER_RADIUS |
| `radius/badge/box/s-square` | `radius/3` | `radius/3` | CORNER_RADIUS |
| `radius/badge/counter/circle` | `radius/999` | `radius/999` | CORNER_RADIUS |
| `radius/badge/focus/circle` | `radius/999` | `radius/999` | CORNER_RADIUS |
| `radius/badge/focus/m` | `radius/6` | `radius/6` | CORNER_RADIUS |
| `radius/badge/focus/s` | `radius/5` | `radius/5` | CORNER_RADIUS |
| `radius/badge/status/circle` | `radius/999` | `radius/999` | CORNER_RADIUS |
| `size/badge/box/m` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `size/badge/box/s` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `size/badge/counter/m` | `size/14` | `size/14` | WIDTH_HEIGHT |
| `size/badge/counter/s` | `size/12` | `size/12` | WIDTH_HEIGHT |
| `size/badge/icon/m` | `size/16` | `size/16` | WIDTH_HEIGHT |
| `size/badge/icon/s` | `size/12` | `size/12` | WIDTH_HEIGHT |
| `size/badge/status/m-box` | `size/12` | `size/12` | WIDTH_HEIGHT |
| `size/badge/status/m-icon` | `size/6` | `size/6` | WIDTH_HEIGHT |
| `size/badge/status/s-box` | `size/10` | `size/10` | WIDTH_HEIGHT |
| `size/badge/status/s-icon` | `size/5` | `size/5` | WIDTH_HEIGHT |
| `space/badge/box/x/m` | `space/6` | `space/6` | GAP |
| `space/badge/box/x/m-icon` | `space/4` | `space/4` | GAP |
| `space/badge/box/x/s` | `space/4` | `space/4` | GAP |
| `space/badge/box/x/s-icon` | `space/4` | `space/4` | GAP |
| `space/badge/box/y/m` | `space/4` | `space/4` | GAP |
| `space/badge/box/y/m-icon` | `space/4` | `space/4` | GAP |
| `space/badge/box/y/s` | `space/3` | `space/3` | GAP |
| `space/badge/box/y/s-icon` | `space/4` | `space/4` | GAP |
| `space/badge/counter/x/m` | `space/4` | `space/4` | GAP |
| `space/badge/counter/x/s` | `space/3` | `space/3` | GAP |
| `space/badge/counter/y/m-bottom` | `space/1` | `space/1` | GAP |
| `space/badge/counter/y/m-top` | `space/2` | `space/2` | GAP |
| `space/badge/counter/y/s-bottom` | `space/0` | `space/0` | GAP |
| `space/badge/counter/y/s-top` | `space/2` | `space/2` | GAP |
| `space/badge/text/m-x` | `space/2` | `space/2` | GAP |
| `space/badge/text/s-x` | `space/2` | `space/2` | GAP |
| `typography/badge/m/counter/letter-spacing` | `font/letter-spacing/0` | `font/letter-spacing/0` | LETTER_SPACING |
| `typography/badge/m/counter/line-height` | `font/line-height/11` | `font/line-height/11` | LINE_HEIGHT |
| `typography/badge/m/counter/size` | `font/size/10` | `font/size/10` | FONT_SIZE |
| `typography/badge/m/counter/weight` | `font/weight/600` | `font/weight/600` | FONT_WEIGHT |
| `typography/badge/m/name/letter-spacing` | `font/letter-spacing/0` | `font/letter-spacing/0` | LETTER_SPACING |
| `typography/badge/m/name/line-height` | `font/line-height/16` | `font/line-height/16` | LINE_HEIGHT |
| `typography/badge/m/name/size` | `font/size/14` | `font/size/14` | FONT_SIZE |
| `typography/badge/m/name/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |
| `typography/badge/s/counter/letter-spacing` | `font/letter-spacing/0` | `font/letter-spacing/0` | LETTER_SPACING |
| `typography/badge/s/counter/line-height` | `font/line-height/10` | `font/line-height/10` | LINE_HEIGHT |
| `typography/badge/s/counter/size` | `font/size/10` | `font/size/10` | FONT_SIZE |
| `typography/badge/s/counter/weight` | `font/weight/600` | `font/weight/600` | FONT_WEIGHT |
| `typography/badge/s/name/letter-spacing` | `font/letter-spacing/0` | `font/letter-spacing/0` | LETTER_SPACING |
| `typography/badge/s/name/line-height` | `font/line-height/14` | `font/line-height/14` | LINE_HEIGHT |
| `typography/badge/s/name/size` | `font/size/12` | `font/size/12` | FONT_SIZE |
| `typography/badge/s/name/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |

## Токены L3 (`3. Components`)

| Токен | → L2 | light | dark | scope |
|---|---|---|---|---|
| `badge/bg/hard/base` | `color/status/base/heavy/default` | rgba(107,107,107,1.00) | rgba(224,224,224,1.00) | FRAME_FILL |
| `badge/bg/hard/base-inverse` | `color/status/base/pure/default` | rgba(255,255,255,1.00) | rgba(31,31,31,1.00) | FRAME_FILL |
| `badge/bg/hard/blue` | `color/status/blue/medium/default` | rgba(59,130,246,1.00) | rgba(79,142,247,1.00) | FRAME_FILL |
| `badge/bg/hard/green` | `color/status/green/medium/default` | rgba(69,161,84,1.00) | rgba(77,179,93,1.00) | FRAME_FILL |
| `badge/bg/hard/purple` | `color/status/purple/medium/default` | rgba(132,77,187,1.00) | rgba(144,95,194,1.00) | FRAME_FILL |
| `badge/bg/hard/red` | `color/status/red/medium/default` | rgba(240,48,48,1.00) | rgba(242,68,68,1.00) | FRAME_FILL |
| `badge/bg/hard/yellow` | `color/status/yellow/medium/default` | rgba(193,166,32,1.00) | rgba(215,185,35,1.00) | FRAME_FILL |
| `badge/bg/soft/base` | `color/status/base/soft/default` | rgba(0,0,0,0.07) | rgba(255,255,255,0.07) | FRAME_FILL |
| `badge/bg/soft/base-inverse` | `color/status/base/inverse-soft/default` | rgba(255,255,255,0.07) | rgba(0,0,0,0.07) | FRAME_FILL |
| `badge/bg/soft/blue` | `color/status/blue/soft/default` | rgba(53,117,221,0.07) | rgba(53,117,221,0.10) | FRAME_FILL |
| `badge/bg/soft/green` | `color/status/green/soft/default` | rgba(69,161,84,0.09) | rgba(69,161,84,0.12) | FRAME_FILL |
| `badge/bg/soft/purple` | `color/status/purple/soft/default` | rgba(119,69,168,0.07) | rgba(119,69,168,0.10) | FRAME_FILL |
| `badge/bg/soft/red` | `color/status/red/soft/default` | rgba(240,48,48,0.07) | rgba(240,48,48,0.10) | FRAME_FILL |
| `badge/bg/soft/yellow` | `color/status/yellow/soft/default` | rgba(172,148,28,0.08) | rgba(172,148,28,0.11) | FRAME_FILL |
| `badge/border/focus` | `color/static/focus/brand` | rgba(39,129,243,1.00) | rgba(61,142,244,1.00) | STROKE_COLOR |
| `badge/border/hard` | `color/static/border/base/inverse-mild` | rgba(255,255,255,0.05) | rgba(0,0,0,0.05) | STROKE_COLOR |
| `badge/border/hard-inverse` | `color/static/border/base/mild` | rgba(0,0,0,0.05) | rgba(255,255,255,0.05) | STROKE_COLOR |
| `badge/border/soft` | `color/static/border/base/mild` | rgba(0,0,0,0.05) | rgba(255,255,255,0.05) | STROKE_COLOR |
| `badge/border/soft-inverse` | `color/static/border/base/inverse-mild` | rgba(255,255,255,0.05) | rgba(0,0,0,0.05) | STROKE_COLOR |
| `badge/counter/hard/base` | `color/status/base/heavy/on` | rgba(255,255,255,1.00) | rgba(61,61,61,1.00) | FRAME_FILL |
| `badge/counter/hard/base-inverse` | `color/status/base/soft/on` | rgba(61,61,61,1.00) | rgba(255,255,255,1.00) | FRAME_FILL |
| `badge/counter/hard/blue` | `color/status/blue/medium/on` | rgba(255,255,255,1.00) | rgba(255,255,255,1.00) | FRAME_FILL |
| `badge/counter/hard/green` | `color/status/green/medium/on` | rgba(255,255,255,1.00) | rgba(255,255,255,1.00) | FRAME_FILL |
| `badge/counter/hard/purple` | `color/status/purple/medium/on` | rgba(255,255,255,1.00) | rgba(255,255,255,1.00) | FRAME_FILL |
| `badge/counter/hard/red` | `color/status/red/medium/on` | rgba(255,255,255,1.00) | rgba(255,255,255,1.00) | FRAME_FILL |
| `badge/counter/hard/text-base` | `color/static/text/base/hard` | rgba(0,0,0,0.85) | rgba(255,255,255,1.00) | TEXT_FILL |
| `badge/counter/hard/text-base-inverse` | `color/static/text/base/inverse-hard` | rgba(255,255,255,1.00) | rgba(0,0,0,0.85) | TEXT_FILL |
| `badge/counter/hard/text-blue` | `color/static/text/palette/blue` | rgba(35,78,148,1.00) | rgba(157,192,250,1.00) | TEXT_FILL |
| `badge/counter/hard/text-green` | `color/static/text/palette/green` | rgba(46,107,56,1.00) | rgba(166,217,174,1.00) | TEXT_FILL |
| `badge/counter/hard/text-purple` | `color/static/text/palette/purple` | rgba(79,46,112,1.00) | rgba(193,166,221,1.00) | TEXT_FILL |
| `badge/counter/hard/text-red` | `color/static/text/palette/red` | rgba(156,25,25,1.00) | rgba(244,146,146,1.00) | TEXT_FILL |
| `badge/counter/hard/text-yellow` | `color/static/text/palette/yellow` | rgba(129,111,21,1.00) | rgba(235,220,145,1.00) | TEXT_FILL |
| `badge/counter/hard/yellow` | `color/status/yellow/medium/on` | rgba(255,255,255,1.00) | rgba(255,255,255,1.00) | FRAME_FILL |
| `badge/counter/soft/base` | `color/status/base/soft/on` | rgba(61,61,61,1.00) | rgba(255,255,255,1.00) | FRAME_FILL |
| `badge/counter/soft/base-inverse` | `color/status/base/heavy/on` | rgba(255,255,255,1.00) | rgba(61,61,61,1.00) | FRAME_FILL |
| `badge/counter/soft/blue` | `color/status/blue/soft/on` | rgba(59,130,246,1.00) | rgba(79,142,247,1.00) | FRAME_FILL |
| `badge/counter/soft/green` | `color/status/green/soft/on` | rgba(69,161,84,1.00) | rgba(77,179,93,1.00) | FRAME_FILL |
| `badge/counter/soft/purple` | `color/status/purple/soft/on` | rgba(132,77,187,1.00) | rgba(144,95,194,1.00) | FRAME_FILL |
| `badge/counter/soft/red` | `color/status/red/soft/on` | rgba(240,48,48,1.00) | rgba(242,68,68,1.00) | FRAME_FILL |
| `badge/counter/soft/text-base` | `color/static/text/base/inverse-hard` | rgba(255,255,255,1.00) | rgba(0,0,0,0.85) | TEXT_FILL |
| `badge/counter/soft/text-inverse` | `color/static/text/base/hard` | rgba(0,0,0,0.85) | rgba(255,255,255,1.00) | TEXT_FILL |
| `badge/counter/soft/yellow` | `color/status/yellow/soft/on` | rgba(193,166,32,1.00) | rgba(215,185,35,1.00) | FRAME_FILL |
| `badge/icon/hard/base` | `color/status/base/heavy/on` | rgba(255,255,255,1.00) | rgba(61,61,61,1.00) | SHAPE_FILL |
| `badge/icon/hard/base-inverse` | `color/status/base/soft/on` | rgba(61,61,61,1.00) | rgba(255,255,255,1.00) | SHAPE_FILL |
| `badge/icon/hard/blue` | `color/status/blue/medium/on` | rgba(255,255,255,1.00) | rgba(255,255,255,1.00) | SHAPE_FILL |
| `badge/icon/hard/green` | `color/status/green/medium/on` | rgba(255,255,255,1.00) | rgba(255,255,255,1.00) | SHAPE_FILL |
| `badge/icon/hard/purple` | `color/status/purple/medium/on` | rgba(255,255,255,1.00) | rgba(255,255,255,1.00) | SHAPE_FILL |
| `badge/icon/hard/red` | `color/status/red/medium/on` | rgba(255,255,255,1.00) | rgba(255,255,255,1.00) | SHAPE_FILL |
| `badge/icon/hard/yellow` | `color/status/yellow/medium/on` | rgba(255,255,255,1.00) | rgba(255,255,255,1.00) | SHAPE_FILL |
| `badge/icon/soft/base` | `color/status/base/soft/on` | rgba(61,61,61,1.00) | rgba(255,255,255,1.00) | SHAPE_FILL |
| `badge/icon/soft/base-inverse` | `color/status/base/heavy/on` | rgba(255,255,255,1.00) | rgba(61,61,61,1.00) | SHAPE_FILL |
| `badge/icon/soft/blue` | `color/status/blue/soft/on` | rgba(59,130,246,1.00) | rgba(79,142,247,1.00) | SHAPE_FILL |
| `badge/icon/soft/green` | `color/status/green/soft/on` | rgba(69,161,84,1.00) | rgba(77,179,93,1.00) | SHAPE_FILL |
| `badge/icon/soft/purple` | `color/status/purple/soft/on` | rgba(132,77,187,1.00) | rgba(144,95,194,1.00) | SHAPE_FILL |
| `badge/icon/soft/red` | `color/status/red/soft/on` | rgba(240,48,48,1.00) | rgba(242,68,68,1.00) | SHAPE_FILL |
| `badge/icon/soft/yellow` | `color/status/yellow/soft/on` | rgba(193,166,32,1.00) | rgba(215,185,35,1.00) | SHAPE_FILL |
| `badge/size/m/box` | `size/badge/box/m` | 24 | 24 | WIDTH_HEIGHT |
| `badge/size/m/box-border` | `border/badge/box/m` | 1 | 1 | STROKE_FLOAT |
| `badge/size/m/box-gap` | `gap/badge/m` | 2 | 2 | GAP |
| `badge/size/m/box-icon-x` | `space/badge/box/x/m-icon` | 4 | 4 | GAP |
| `badge/size/m/box-icon-y` | `space/badge/box/y/m-icon` | 4 | 4 | GAP |
| `badge/size/m/box-radius-circle` | `radius/badge/box/circle` | 999 | 999 | CORNER_RADIUS |
| `badge/size/m/box-radius-square` | `radius/badge/box/m-square` | 4 | 4 | CORNER_RADIUS |
| `badge/size/m/box-x` | `space/badge/box/x/m` | 6 | 6 | GAP |
| `badge/size/m/box-y` | `space/badge/box/y/m` | 4 | 4 | GAP |
| `badge/size/m/counter` | `size/badge/counter/m` | 14 | 14 | WIDTH_HEIGHT |
| `badge/size/m/counter-radius` | `radius/badge/counter/circle` | 999 | 999 | CORNER_RADIUS |
| `badge/size/m/counter-x` | `space/badge/counter/x/m` | 4 | 4 | GAP |
| `badge/size/m/counter-y-bottom` | `space/badge/counter/y/m-bottom` | 1 | 1 | GAP |
| `badge/size/m/counter-y-top` | `space/badge/counter/y/m-top` | 2 | 2 | GAP |
| `badge/size/m/focus-border` | `border/badge/focus/m` | 2 | 2 | STROKE_FLOAT |
| `badge/size/m/focus-radius-circle` | `radius/badge/focus/circle` | 999 | 999 | CORNER_RADIUS |
| `badge/size/m/focus-radius-square` | `radius/badge/focus/m` | 6 | 6 | CORNER_RADIUS |
| `badge/size/m/icon` | `size/badge/icon/m` | 16 | 16 | WIDTH_HEIGHT |
| `badge/size/m/status-box` | `size/badge/status/m-box` | 12 | 12 | WIDTH_HEIGHT |
| `badge/size/m/status-icon` | `size/badge/status/m-icon` | 6 | 6 | WIDTH_HEIGHT |
| `badge/size/m/status-radius` | `radius/badge/status/circle` | 999 | 999 | CORNER_RADIUS |
| `badge/size/m/text-padding` | `space/badge/text/m-x` | 2 | 2 | GAP |
| `badge/size/s/box` | `size/badge/box/s` | 20 | 20 | WIDTH_HEIGHT |
| `badge/size/s/box-border` | `border/badge/box/s` | 1 | 1 | STROKE_FLOAT |
| `badge/size/s/box-gap` | `gap/badge/s` | 2 | 2 | GAP |
| `badge/size/s/box-icon-x` | `space/badge/box/x/s-icon` | 4 | 4 | GAP |
| `badge/size/s/box-icon-y` | `space/badge/box/y/s-icon` | 4 | 4 | GAP |
| `badge/size/s/box-radius-circle` | `radius/badge/box/circle` | 999 | 999 | CORNER_RADIUS |
| `badge/size/s/box-radius-square` | `radius/badge/box/s-square` | 3 | 3 | CORNER_RADIUS |
| `badge/size/s/box-x` | `space/badge/box/x/s` | 4 | 4 | GAP |
| `badge/size/s/box-y` | `space/badge/box/y/s` | 3 | 3 | GAP |
| `badge/size/s/counter` | `size/badge/counter/s` | 12 | 12 | WIDTH_HEIGHT |
| `badge/size/s/counter-radius` | `radius/badge/counter/circle` | 999 | 999 | CORNER_RADIUS |
| `badge/size/s/counter-x` | `space/badge/counter/x/s` | 3 | 3 | GAP |
| `badge/size/s/counter-y-bottom` | `space/badge/counter/y/s-bottom` | 0 | 0 | GAP |
| `badge/size/s/counter-y-top` | `space/badge/counter/y/s-top` | 2 | 2 | GAP |
| `badge/size/s/focus-border` | `border/badge/focus/s` | 1 | 1 | STROKE_FLOAT |
| `badge/size/s/focus-radius-circle` | `radius/badge/focus/circle` | 999 | 999 | CORNER_RADIUS |
| `badge/size/s/focus-radius-square` | `radius/badge/focus/s` | 5 | 5 | CORNER_RADIUS |
| `badge/size/s/icon` | `size/badge/icon/s` | 12 | 12 | WIDTH_HEIGHT |
| `badge/size/s/status-box` | `size/badge/status/s-box` | 10 | 10 | WIDTH_HEIGHT |
| `badge/size/s/status-icon` | `size/badge/status/s-icon` | 5 | 5 | WIDTH_HEIGHT |
| `badge/size/s/status-radius` | `radius/badge/status/circle` | 999 | 999 | CORNER_RADIUS |
| `badge/size/s/text-padding` | `space/badge/text/s-x` | 2 | 2 | GAP |
| `badge/status/base` | `color/status/base/soft/on` | rgba(61,61,61,1.00) | rgba(255,255,255,1.00) | SHAPE_FILL |
| `badge/status/base-inverse` | `color/status/base/heavy/on` | rgba(255,255,255,1.00) | rgba(61,61,61,1.00) | SHAPE_FILL |
| `badge/status/blue` | `color/status/blue/soft/on` | rgba(59,130,246,1.00) | rgba(79,142,247,1.00) | SHAPE_FILL |
| `badge/status/green` | `color/status/green/soft/on` | rgba(69,161,84,1.00) | rgba(77,179,93,1.00) | SHAPE_FILL |
| `badge/status/purple` | `color/status/purple/soft/on` | rgba(132,77,187,1.00) | rgba(144,95,194,1.00) | SHAPE_FILL |
| `badge/status/red` | `color/status/red/soft/on` | rgba(240,48,48,1.00) | rgba(242,68,68,1.00) | SHAPE_FILL |
| `badge/status/yellow` | `color/status/yellow/soft/on` | rgba(193,166,32,1.00) | rgba(215,185,35,1.00) | SHAPE_FILL |
| `badge/text/hard/base` | `color/status/base/heavy/on` | rgba(255,255,255,1.00) | rgba(61,61,61,1.00) | TEXT_FILL |
| `badge/text/hard/base-inverse` | `color/status/base/soft/on` | rgba(61,61,61,1.00) | rgba(255,255,255,1.00) | TEXT_FILL |
| `badge/text/hard/blue` | `color/status/blue/medium/on` | rgba(255,255,255,1.00) | rgba(255,255,255,1.00) | TEXT_FILL |
| `badge/text/hard/green` | `color/status/green/medium/on` | rgba(255,255,255,1.00) | rgba(255,255,255,1.00) | TEXT_FILL |
| `badge/text/hard/purple` | `color/status/purple/medium/on` | rgba(255,255,255,1.00) | rgba(255,255,255,1.00) | TEXT_FILL |
| `badge/text/hard/red` | `color/status/red/medium/on` | rgba(255,255,255,1.00) | rgba(255,255,255,1.00) | TEXT_FILL |
| `badge/text/hard/yellow` | `color/status/yellow/medium/on` | rgba(255,255,255,1.00) | rgba(255,255,255,1.00) | TEXT_FILL |
| `badge/text/soft/base` | `color/status/base/soft/on` | rgba(61,61,61,1.00) | rgba(255,255,255,1.00) | TEXT_FILL |
| `badge/text/soft/base-inverse` | `color/status/base/heavy/on` | rgba(255,255,255,1.00) | rgba(61,61,61,1.00) | TEXT_FILL |
| `badge/text/soft/blue` | `color/status/blue/soft/on` | rgba(59,130,246,1.00) | rgba(79,142,247,1.00) | TEXT_FILL |
| `badge/text/soft/green` | `color/status/green/soft/on` | rgba(69,161,84,1.00) | rgba(77,179,93,1.00) | TEXT_FILL |
| `badge/text/soft/purple` | `color/status/purple/soft/on` | rgba(132,77,187,1.00) | rgba(144,95,194,1.00) | TEXT_FILL |
| `badge/text/soft/red` | `color/status/red/soft/on` | rgba(240,48,48,1.00) | rgba(242,68,68,1.00) | TEXT_FILL |
| `badge/text/soft/yellow` | `color/status/yellow/soft/on` | rgba(193,166,32,1.00) | rgba(215,185,35,1.00) | TEXT_FILL |

## Текстовые стили

| Стиль | Шрифт | Переменные |
|---|---|---|
| `typography/badge/s/name` | Roboto Regular | `typography/badge/s/name/size`, `typography/badge/s/name/line-height`, `typography/badge/s/name/letter-spacing`, `typography/badge/s/name/weight` |
| `typography/badge/s/counter` | Roboto SemiBold | `typography/badge/s/counter/size`, `typography/badge/s/counter/line-height`, `typography/badge/s/counter/letter-spacing`, `typography/badge/s/counter/weight` |
| `typography/badge/m/name` | Roboto Regular | `typography/badge/m/name/size`, `typography/badge/m/name/line-height`, `typography/badge/m/name/letter-spacing`, `typography/badge/m/name/weight` |
| `typography/badge/m/counter` | Roboto SemiBold | `typography/badge/m/counter/size`, `typography/badge/m/counter/line-height`, `typography/badge/m/counter/letter-spacing`, `typography/badge/m/counter/weight` |

## Решения и допущения

- Пресет снят с текущей системы: повторная запись в исходный файл должна дать 0 изменений.
