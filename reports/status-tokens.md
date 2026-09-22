# Токены: Status

Пресет: `presets/status.tokens.json`. Источник: `input/tokens/variables.json`. Аналог: `—`.

Статус проверки: **OK** · L2 новых: 41 · L3: 91 · текстовых стилей: 2

## Заметки

- Пресет снят с текущей системы; проверена сверка с индексом один к одному.

## Новые токены L2 (`2. General`)

| Токен | light | dark | scopes |
|---|---|---|---|
| `gap/status/box/l` | `space/3` | `space/3` | GAP |
| `gap/status/box/m` | `space/2` | `space/2` | GAP |
| `gap/status/unboxed/l` | `space/4` | `space/4` | GAP |
| `gap/status/unboxed/m` | `space/1` | `space/1` | GAP |
| `radius/status/circle` | `radius/999` | `radius/999` | CORNER_RADIUS |
| `radius/status/icon-marker` | `radius/999` | `radius/999` | CORNER_RADIUS |
| `radius/status/l-square` | `radius/5` | `radius/5` | CORNER_RADIUS |
| `radius/status/m-square` | `radius/4` | `radius/4` | CORNER_RADIUS |
| `radius/status/unboxed` | `radius/0` | `radius/0` | CORNER_RADIUS |
| `size/status/avatar-box/l` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `size/status/avatar-box/m` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `size/status/box/l` | `size/28` | `size/28` | WIDTH_HEIGHT |
| `size/status/box/m` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `size/status/dot/l` | `size/9` | `size/9` | WIDTH_HEIGHT |
| `size/status/dot/m` | `size/7` | `size/7` | WIDTH_HEIGHT |
| `size/status/icon-box/l` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `size/status/icon-box/m` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `size/status/icon/l` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `size/status/icon/m` | `size/16` | `size/16` | WIDTH_HEIGHT |
| `size/status/marker/l` | `size/8` | `size/8` | WIDTH_HEIGHT |
| `size/status/marker/m` | `size/6` | `size/6` | WIDTH_HEIGHT |
| `size/status/unboxed/l` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `size/status/unboxed/m` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `space/status/box/x/l` | `space/11` | `space/11` | GAP |
| `space/status/box/x/l-icon` | `space/5` | `space/5` | GAP |
| `space/status/box/x/l-unboxed` | `space/0` | `space/0` | GAP |
| `space/status/box/x/m` | `space/9` | `space/9` | GAP |
| `space/status/box/x/m-icon` | `space/4` | `space/4` | GAP |
| `space/status/box/x/m-unboxed` | `space/0` | `space/0` | GAP |
| `space/status/box/y/l` | `space/2` | `space/2` | GAP |
| `space/status/box/y/l-unboxed` | `space/0` | `space/0` | GAP |
| `space/status/box/y/m` | `space/2` | `space/2` | GAP |
| `space/status/box/y/m-unboxed` | `space/0` | `space/0` | GAP |
| `typography/status/l/letter-spacing` | `font/letter-spacing/0` | `font/letter-spacing/0` | LETTER_SPACING |
| `typography/status/l/line-height` | `font/line-height/24` | `font/line-height/24` | LINE_HEIGHT |
| `typography/status/l/size` | `font/size/16` | `font/size/16` | FONT_SIZE |
| `typography/status/l/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |
| `typography/status/m/letter-spacing` | `font/letter-spacing/10` | `font/letter-spacing/10` | LETTER_SPACING |
| `typography/status/m/line-height` | `font/line-height/20` | `font/line-height/20` | LINE_HEIGHT |
| `typography/status/m/size` | `font/size/14` | `font/size/14` | FONT_SIZE |
| `typography/status/m/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |

## Токены L3 (`3. Components`)

| Токен | → L2 | light | dark | scope |
|---|---|---|---|---|
| `status/bg/hard/brand` | `color/status/brand/medium/default` | rgba(39,129,243,1.00) | rgba(61,142,244,1.00) | FRAME_FILL |
| `status/bg/hard/error` | `color/status/red/medium/default` | rgba(240,48,48,1.00) | rgba(242,68,68,1.00) | FRAME_FILL |
| `status/bg/hard/info` | `color/status/blue/medium/default` | rgba(59,130,246,1.00) | rgba(79,142,247,1.00) | FRAME_FILL |
| `status/bg/hard/neutral` | `color/status/base/heavy/default` | rgba(107,107,107,1.00) | rgba(224,224,224,1.00) | FRAME_FILL |
| `status/bg/hard/pending` | `color/status/purple/medium/default` | rgba(132,77,187,1.00) | rgba(144,95,194,1.00) | FRAME_FILL |
| `status/bg/hard/success` | `color/status/green/medium/default` | rgba(69,161,84,1.00) | rgba(77,179,93,1.00) | FRAME_FILL |
| `status/bg/hard/warning` | `color/status/yellow/medium/default` | rgba(193,166,32,1.00) | rgba(215,185,35,1.00) | FRAME_FILL |
| `status/bg/soft/brand` | `color/status/brand/soft/default` | rgba(39,129,243,0.05) | rgba(39,129,243,0.10) | FRAME_FILL |
| `status/bg/soft/error` | `color/status/red/soft/default` | rgba(240,48,48,0.07) | rgba(240,48,48,0.10) | FRAME_FILL |
| `status/bg/soft/info` | `color/status/blue/soft/default` | rgba(53,117,221,0.07) | rgba(53,117,221,0.10) | FRAME_FILL |
| `status/bg/soft/neutral` | `color/status/base/soft/default` | rgba(0,0,0,0.07) | rgba(255,255,255,0.07) | FRAME_FILL |
| `status/bg/soft/pending` | `color/status/purple/soft/default` | rgba(119,69,168,0.07) | rgba(119,69,168,0.10) | FRAME_FILL |
| `status/bg/soft/success` | `color/status/green/soft/default` | rgba(69,161,84,0.09) | rgba(69,161,84,0.12) | FRAME_FILL |
| `status/bg/soft/warning` | `color/status/yellow/soft/default` | rgba(172,148,28,0.08) | rgba(172,148,28,0.11) | FRAME_FILL |
| `status/icon/hard/brand` | `color/status/brand/medium/on` | rgba(255,255,255,1.00) | rgba(255,255,255,1.00) | SHAPE_FILL |
| `status/icon/hard/error` | `color/status/red/medium/on` | rgba(255,255,255,1.00) | rgba(255,255,255,1.00) | SHAPE_FILL |
| `status/icon/hard/info` | `color/status/blue/medium/on` | rgba(255,255,255,1.00) | rgba(255,255,255,1.00) | SHAPE_FILL |
| `status/icon/hard/neutral` | `color/status/base/heavy/on` | rgba(255,255,255,1.00) | rgba(61,61,61,1.00) | SHAPE_FILL |
| `status/icon/hard/pending` | `color/status/purple/medium/on` | rgba(255,255,255,1.00) | rgba(255,255,255,1.00) | SHAPE_FILL |
| `status/icon/hard/success` | `color/status/green/medium/on` | rgba(255,255,255,1.00) | rgba(255,255,255,1.00) | SHAPE_FILL |
| `status/icon/hard/warning` | `color/status/yellow/medium/on` | rgba(255,255,255,1.00) | rgba(255,255,255,1.00) | SHAPE_FILL |
| `status/icon/soft/brand` | `color/status/brand/soft/on` | rgba(39,129,243,1.00) | rgba(61,142,244,1.00) | SHAPE_FILL |
| `status/icon/soft/error` | `color/status/red/soft/on` | rgba(240,48,48,1.00) | rgba(242,68,68,1.00) | SHAPE_FILL |
| `status/icon/soft/info` | `color/status/blue/soft/on` | rgba(59,130,246,1.00) | rgba(79,142,247,1.00) | SHAPE_FILL |
| `status/icon/soft/neutral` | `color/status/base/soft/on` | rgba(61,61,61,1.00) | rgba(255,255,255,1.00) | SHAPE_FILL |
| `status/icon/soft/pending` | `color/status/purple/soft/on` | rgba(132,77,187,1.00) | rgba(144,95,194,1.00) | SHAPE_FILL |
| `status/icon/soft/success` | `color/status/green/soft/on` | rgba(69,161,84,1.00) | rgba(77,179,93,1.00) | SHAPE_FILL |
| `status/icon/soft/warning` | `color/status/yellow/soft/on` | rgba(193,166,32,1.00) | rgba(215,185,35,1.00) | SHAPE_FILL |
| `status/icon/status/brand` | `color/status/brand/soft/on` | rgba(39,129,243,1.00) | rgba(61,142,244,1.00) | SHAPE_FILL |
| `status/icon/status/error` | `color/status/red/soft/on` | rgba(240,48,48,1.00) | rgba(242,68,68,1.00) | SHAPE_FILL |
| `status/icon/status/info` | `color/status/blue/soft/on` | rgba(59,130,246,1.00) | rgba(79,142,247,1.00) | SHAPE_FILL |
| `status/icon/status/inverse-neutral` | `color/status/base/heavy/on-secondary` | rgba(255,255,255,0.70) | rgba(0,0,0,0.60) | SHAPE_FILL |
| `status/icon/status/neutral` | `color/status/base/soft/on` | rgba(61,61,61,1.00) | rgba(255,255,255,1.00) | SHAPE_FILL |
| `status/icon/status/pending` | `color/status/purple/soft/on` | rgba(132,77,187,1.00) | rgba(144,95,194,1.00) | SHAPE_FILL |
| `status/icon/status/success` | `color/status/green/soft/on` | rgba(69,161,84,1.00) | rgba(77,179,93,1.00) | SHAPE_FILL |
| `status/icon/status/warning` | `color/status/yellow/soft/on` | rgba(193,166,32,1.00) | rgba(215,185,35,1.00) | SHAPE_FILL |
| `status/loading/icon` | `color/static/bg/transparent/base/light` | rgba(0,0,0,0.10) | rgba(255,255,255,0.10) | SHAPE_FILL |
| `status/loading/inverse-icon` | `color/static/bg/transparent/base/inverse-light` | rgba(255,255,255,0.10) | rgba(0,0,0,0.10) | SHAPE_FILL |
| `status/loading/inverse-name` | `color/static/bg/transparent/base/inverse-light` | rgba(255,255,255,0.10) | rgba(0,0,0,0.10) | FRAME_FILL |
| `status/loading/name` | `color/static/bg/transparent/base/light` | rgba(0,0,0,0.10) | rgba(255,255,255,0.10) | FRAME_FILL |
| `status/size/l/avatar-box` | `size/status/avatar-box/l` | 24 | 24 | WIDTH_HEIGHT |
| `status/size/l/box` | `size/status/box/l` | 28 | 28 | WIDTH_HEIGHT |
| `status/size/l/box-gap` | `gap/status/box/l` | 3 | 3 | GAP |
| `status/size/l/box-icon-x` | `space/status/box/x/l-icon` | 5 | 5 | GAP |
| `status/size/l/box-radius-circle` | `radius/status/circle` | 999 | 999 | CORNER_RADIUS |
| `status/size/l/box-radius-square` | `radius/status/l-square` | 5 | 5 | CORNER_RADIUS |
| `status/size/l/box-x` | `space/status/box/x/l` | 11 | 11 | GAP |
| `status/size/l/box-y` | `space/status/box/y/l` | 2 | 2 | GAP |
| `status/size/l/dot` | `size/status/dot/l` | 9 | 9 | WIDTH_HEIGHT |
| `status/size/l/icon` | `size/status/icon/l` | 20 | 20 | WIDTH_HEIGHT |
| `status/size/l/icon-box` | `size/status/icon-box/l` | 24 | 24 | WIDTH_HEIGHT |
| `status/size/l/marker` | `size/status/marker/l` | 8 | 8 | WIDTH_HEIGHT |
| `status/size/l/marker-radius` | `radius/status/icon-marker` | 999 | 999 | CORNER_RADIUS |
| `status/size/l/unboxed` | `size/status/unboxed/l` | 24 | 24 | WIDTH_HEIGHT |
| `status/size/l/unboxed-gap` | `gap/status/unboxed/l` | 4 | 4 | GAP |
| `status/size/l/unboxed-radius` | `radius/status/unboxed` | 0 | 0 | CORNER_RADIUS |
| `status/size/l/unboxed-x` | `space/status/box/x/l-unboxed` | 0 | 0 | GAP |
| `status/size/l/unboxed-y` | `space/status/box/y/l-unboxed` | 0 | 0 | GAP |
| `status/size/m/avatar-box` | `size/status/avatar-box/m` | 20 | 20 | WIDTH_HEIGHT |
| `status/size/m/box` | `size/status/box/m` | 24 | 24 | WIDTH_HEIGHT |
| `status/size/m/box-gap` | `gap/status/box/m` | 2 | 2 | GAP |
| `status/size/m/box-icon-x` | `space/status/box/x/m-icon` | 4 | 4 | GAP |
| `status/size/m/box-radius-circle` | `radius/status/circle` | 999 | 999 | CORNER_RADIUS |
| `status/size/m/box-radius-square` | `radius/status/m-square` | 4 | 4 | CORNER_RADIUS |
| `status/size/m/box-x` | `space/status/box/x/m` | 9 | 9 | GAP |
| `status/size/m/box-y` | `space/status/box/y/m` | 2 | 2 | GAP |
| `status/size/m/dot` | `size/status/dot/m` | 7 | 7 | WIDTH_HEIGHT |
| `status/size/m/icon` | `size/status/icon/m` | 16 | 16 | WIDTH_HEIGHT |
| `status/size/m/icon-box` | `size/status/icon-box/m` | 20 | 20 | WIDTH_HEIGHT |
| `status/size/m/marker` | `size/status/marker/m` | 6 | 6 | WIDTH_HEIGHT |
| `status/size/m/marker-radius` | `radius/status/icon-marker` | 999 | 999 | CORNER_RADIUS |
| `status/size/m/unboxed` | `size/status/unboxed/m` | 20 | 20 | WIDTH_HEIGHT |
| `status/size/m/unboxed-gap` | `gap/status/unboxed/m` | 1 | 1 | GAP |
| `status/size/m/unboxed-radius` | `radius/status/unboxed` | 0 | 0 | CORNER_RADIUS |
| `status/size/m/unboxed-x` | `space/status/box/x/m-unboxed` | 0 | 0 | GAP |
| `status/size/m/unboxed-y` | `space/status/box/y/m-unboxed` | 0 | 0 | GAP |
| `status/text/hard/brand` | `color/status/brand/medium/on` | rgba(255,255,255,1.00) | rgba(255,255,255,1.00) | TEXT_FILL |
| `status/text/hard/error` | `color/status/red/medium/on` | rgba(255,255,255,1.00) | rgba(255,255,255,1.00) | TEXT_FILL |
| `status/text/hard/info` | `color/status/blue/medium/on` | rgba(255,255,255,1.00) | rgba(255,255,255,1.00) | TEXT_FILL |
| `status/text/hard/neutral` | `color/status/base/heavy/on` | rgba(255,255,255,1.00) | rgba(61,61,61,1.00) | TEXT_FILL |
| `status/text/hard/pending` | `color/status/purple/medium/on` | rgba(255,255,255,1.00) | rgba(255,255,255,1.00) | TEXT_FILL |
| `status/text/hard/success` | `color/status/green/medium/on` | rgba(255,255,255,1.00) | rgba(255,255,255,1.00) | TEXT_FILL |
| `status/text/hard/warning` | `color/status/yellow/medium/on` | rgba(255,255,255,1.00) | rgba(255,255,255,1.00) | TEXT_FILL |
| `status/text/inverse` | `color/status/base/heavy/on` | rgba(255,255,255,1.00) | rgba(61,61,61,1.00) | TEXT_FILL |
| `status/text/soft/brand` | `color/status/brand/soft/on` | rgba(39,129,243,1.00) | rgba(61,142,244,1.00) | TEXT_FILL |
| `status/text/soft/error` | `color/status/red/soft/on` | rgba(240,48,48,1.00) | rgba(242,68,68,1.00) | TEXT_FILL |
| `status/text/soft/info` | `color/status/blue/soft/on` | rgba(59,130,246,1.00) | rgba(79,142,247,1.00) | TEXT_FILL |
| `status/text/soft/neutral` | `color/status/base/soft/on` | rgba(61,61,61,1.00) | rgba(255,255,255,1.00) | TEXT_FILL |
| `status/text/soft/pending` | `color/status/purple/soft/on` | rgba(132,77,187,1.00) | rgba(144,95,194,1.00) | TEXT_FILL |
| `status/text/soft/success` | `color/status/green/soft/on` | rgba(69,161,84,1.00) | rgba(77,179,93,1.00) | TEXT_FILL |
| `status/text/soft/warning` | `color/status/yellow/soft/on` | rgba(193,166,32,1.00) | rgba(215,185,35,1.00) | TEXT_FILL |

## Текстовые стили

| Стиль | Шрифт | Переменные |
|---|---|---|
| `typography/status/l` | Roboto Regular | `typography/status/l/size`, `typography/status/l/line-height`, `typography/status/l/letter-spacing`, `typography/status/l/weight` |
| `typography/status/m` | Roboto Regular | `typography/status/m/size`, `typography/status/m/line-height`, `typography/status/m/letter-spacing`, `typography/status/m/weight` |

## Решения и допущения

- Пресет снят с текущей системы: повторная запись в исходный файл должна дать 0 изменений.
