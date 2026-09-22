# Токены: Checkbox

Пресет: `presets/checkbox.tokens.json`. Источник: `input/tokens/variables.json`. Аналог: `—`.

Статус проверки: **OK** · L2 новых: 60 · L3: 110 · текстовых стилей: 4

## Заметки

- L3 `checkbox/checked/icon/default`: изменение одобрено (2026-09-21, тёмная тема: контраст WCAG AA): color/action/indicator/base/inverse-hard/default → color/action/indicator/base/on-bold/default
- L3 `checkbox/checked/icon/hover`: изменение одобрено (2026-09-21, тёмная тема: контраст WCAG AA): color/action/indicator/base/inverse-hard/default → color/action/indicator/base/on-bold/hover
- L3 `checkbox/checked/icon/pressed`: изменение одобрено (2026-09-21, тёмная тема: контраст WCAG AA): color/action/indicator/base/inverse-hard/default → color/action/indicator/base/on-bold/pressed
- Пресет снят с текущей системы; проверена сверка с индексом один к одному.

## Новые токены L2 (`2. General`)

| Токен | light | dark | scopes |
|---|---|---|---|
| `border/checkbox/box/l` | `border/1` | `border/1` | STROKE_FLOAT |
| `border/checkbox/box/m` | `border/1` | `border/1` | STROKE_FLOAT |
| `border/checkbox/card` | `border/1` | `border/1` | STROKE_FLOAT |
| `border/checkbox/focus/l` | `border/2` | `border/2` | STROKE_FLOAT |
| `border/checkbox/focus/m` | `border/1` | `border/1` | STROKE_FLOAT |
| `gap/checkbox/checkbox-text/l` | `space/10` | `space/10` | GAP |
| `gap/checkbox/checkbox-text/m` | `space/6` | `space/6` | GAP |
| `gap/checkbox/text-interline/l` | `space/0` | `space/0` | GAP |
| `gap/checkbox/text-interline/m` | `space/0` | `space/0` | GAP |
| `radius/checkbox/box/l` | `radius/5` | `radius/5` | CORNER_RADIUS |
| `radius/checkbox/box/m` | `radius/4` | `radius/4` | CORNER_RADIUS |
| `radius/checkbox/card` | `radius/12` | `radius/12` | CORNER_RADIUS |
| `radius/checkbox/focus/l` | `radius/8` | `radius/8` | CORNER_RADIUS |
| `radius/checkbox/focus/m` | `radius/6` | `radius/6` | CORNER_RADIUS |
| `size/checkbox/box-container/l` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `size/checkbox/box-container/m` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `size/checkbox/box/l` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `size/checkbox/box/m` | `size/16` | `size/16` | WIDTH_HEIGHT |
| `size/checkbox/icon/card/l` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `size/checkbox/icon/card/m` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `size/checkbox/icon/check/l` | `size/16` | `size/16` | WIDTH_HEIGHT |
| `size/checkbox/icon/check/m` | `size/13` | `size/13` | WIDTH_HEIGHT |
| `space/checkbox/box/x/l` | `space/2` | `space/2` | GAP |
| `space/checkbox/box/x/m` | `space/1` | `space/1` | GAP |
| `space/checkbox/box/y/l` | `space/2` | `space/2` | GAP |
| `space/checkbox/box/y/l-check-bottom` | `space/1` | `space/1` | GAP |
| `space/checkbox/box/y/l-check-top` | `space/3` | `space/3` | GAP |
| `space/checkbox/box/y/m` | `space/1` | `space/1` | GAP |
| `space/checkbox/box/y/m-check-bottom` | `space/1` | `space/1` | GAP |
| `space/checkbox/box/y/m-check-top` | `space/2` | `space/2` | GAP |
| `space/checkbox/card/x/l` | `space/16` | `space/16` | GAP |
| `space/checkbox/card/x/m` | `space/12` | `space/12` | GAP |
| `space/checkbox/card/y/l-bottom` | `space/16` | `space/16` | GAP |
| `space/checkbox/card/y/l-icon-text` | `space/36` | `space/36` | GAP |
| `space/checkbox/card/y/l-top` | `space/16` | `space/16` | GAP |
| `space/checkbox/card/y/m-bottom` | `space/12` | `space/12` | GAP |
| `space/checkbox/card/y/m-icon-text` | `space/28` | `space/28` | GAP |
| `space/checkbox/card/y/m-top` | `space/12` | `space/12` | GAP |
| `space/checkbox/container/xy-l` | `space/2` | `space/2` | GAP |
| `space/checkbox/container/xy-m` | `space/2` | `space/2` | GAP |
| `space/checkbox/text-container/x/l` | `space/0` | `space/0` | GAP |
| `space/checkbox/text-container/x/m` | `space/0` | `space/0` | GAP |
| `space/checkbox/text-container/y/l` | `space/0` | `space/0` | GAP |
| `space/checkbox/text-container/y/m` | `space/0` | `space/0` | GAP |
| `typography/checkbox/l/description/letter-spacing` | `font/letter-spacing/10` | `font/letter-spacing/10` | LETTER_SPACING |
| `typography/checkbox/l/description/line-height` | `font/line-height/20` | `font/line-height/20` | LINE_HEIGHT |
| `typography/checkbox/l/description/size` | `font/size/14` | `font/size/14` | FONT_SIZE |
| `typography/checkbox/l/description/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |
| `typography/checkbox/l/name/letter-spacing` | `font/letter-spacing/0` | `font/letter-spacing/0` | LETTER_SPACING |
| `typography/checkbox/l/name/line-height` | `font/line-height/24` | `font/line-height/24` | LINE_HEIGHT |
| `typography/checkbox/l/name/size` | `font/size/16` | `font/size/16` | FONT_SIZE |
| `typography/checkbox/l/name/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |
| `typography/checkbox/m/description/letter-spacing` | `font/letter-spacing/10` | `font/letter-spacing/10` | LETTER_SPACING |
| `typography/checkbox/m/description/line-height` | `font/line-height/20` | `font/line-height/20` | LINE_HEIGHT |
| `typography/checkbox/m/description/size` | `font/size/14` | `font/size/14` | FONT_SIZE |
| `typography/checkbox/m/description/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |
| `typography/checkbox/m/name/letter-spacing` | `font/letter-spacing/10` | `font/letter-spacing/10` | LETTER_SPACING |
| `typography/checkbox/m/name/line-height` | `font/line-height/20` | `font/line-height/20` | LINE_HEIGHT |
| `typography/checkbox/m/name/size` | `font/size/14` | `font/size/14` | FONT_SIZE |
| `typography/checkbox/m/name/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |

## Токены L3 (`3. Components`)

| Токен | → L2 | light | dark | scope |
|---|---|---|---|---|
| `checkbox/card/bg` | `color/static/bg/transparent/base/ghost` | rgba(0,0,0,0.00) | rgba(255,255,255,0.00) | FRAME_FILL |
| `checkbox/card/border` | `color/static/border/base/soft` | rgba(0,0,0,0.07) | rgba(255,255,255,0.07) | STROKE_COLOR |
| `checkbox/card/icon` | `color/static/indicator/base/hard` | rgba(0,0,0,0.85) | rgba(255,255,255,1.00) | SHAPE_FILL |
| `checkbox/card/inverse-bg` | `color/static/bg/transparent/base/ghost` | rgba(0,0,0,0.00) | rgba(255,255,255,0.00) | FRAME_FILL |
| `checkbox/card/inverse-border` | `color/static/border/base/inverse-light` | rgba(255,255,255,0.10) | rgba(0,0,0,0.10) | STROKE_COLOR |
| `checkbox/card/inverse-icon` | `color/static/indicator/base/inverse-hard` | rgba(255,255,255,1.00) | rgba(0,0,0,0.85) | SHAPE_FILL |
| `checkbox/checked/bg/default` | `color/action/bg/brand/medium/default` | rgba(39,129,243,1.00) | rgba(61,142,244,1.00) | FRAME_FILL |
| `checkbox/checked/bg/disabled` | `color/action/bg/brand/medium/disabled` | rgba(39,129,243,0.50) | rgba(39,129,243,0.50) | FRAME_FILL |
| `checkbox/checked/bg/hover` | `color/action/bg/brand/medium/hover` | rgba(35,116,219,1.00) | rgba(82,154,245,1.00) | FRAME_FILL |
| `checkbox/checked/bg/pressed` | `color/action/bg/brand/medium/pressed` | rgba(31,103,194,1.00) | rgba(104,167,247,1.00) | FRAME_FILL |
| `checkbox/checked/border/default` | `color/action/border/base/ghost/default` | rgba(0,0,0,0.00) | rgba(255,255,255,0.00) | STROKE_COLOR |
| `checkbox/checked/border/disabled` | `color/action/border/base/ghost/default` | rgba(0,0,0,0.00) | rgba(255,255,255,0.00) | STROKE_COLOR |
| `checkbox/checked/border/hover` | `color/action/border/base/ghost/default` | rgba(0,0,0,0.00) | rgba(255,255,255,0.00) | STROKE_COLOR |
| `checkbox/checked/border/pressed` | `color/action/border/base/ghost/default` | rgba(0,0,0,0.00) | rgba(255,255,255,0.00) | STROKE_COLOR |
| `checkbox/checked/icon/default` | `color/action/indicator/base/on-bold/default` | None | None | SHAPE_FILL |
| `checkbox/checked/icon/disabled` | `color/action/indicator/base/inverse-hard/default` | rgba(255,255,255,1.00) | rgba(0,0,0,0.85) | SHAPE_FILL |
| `checkbox/checked/icon/hover` | `color/action/indicator/base/on-bold/hover` | None | None | SHAPE_FILL |
| `checkbox/checked/icon/pressed` | `color/action/indicator/base/on-bold/pressed` | None | None | SHAPE_FILL |
| `checkbox/checked/inverse-bg/default` | `color/action/bg/base/inverse/default` | rgba(255,255,255,1.00) | rgba(31,31,31,1.00) | FRAME_FILL |
| `checkbox/checked/inverse-bg/disabled` | `color/action/bg/base/inverse/disabled` | rgba(255,255,255,0.25) | rgba(0,0,0,0.10) | FRAME_FILL |
| `checkbox/checked/inverse-bg/hover` | `color/action/bg/base/inverse/hover` | rgba(235,235,235,1.00) | rgba(61,61,61,1.00) | FRAME_FILL |
| `checkbox/checked/inverse-bg/pressed` | `color/action/bg/base/inverse/pressed` | rgba(224,224,224,1.00) | rgba(77,77,77,1.00) | FRAME_FILL |
| `checkbox/checked/inverse-border/default` | `color/action/border/base/inverse-ghost/default` | rgba(255,255,255,0.00) | rgba(0,0,0,0.00) | STROKE_COLOR |
| `checkbox/checked/inverse-border/disabled` | `color/action/border/base/inverse-ghost/default` | rgba(255,255,255,0.00) | rgba(0,0,0,0.00) | STROKE_COLOR |
| `checkbox/checked/inverse-border/hover` | `color/action/border/base/inverse-ghost/default` | rgba(255,255,255,0.00) | rgba(0,0,0,0.00) | STROKE_COLOR |
| `checkbox/checked/inverse-border/pressed` | `color/action/border/base/inverse-ghost/default` | rgba(255,255,255,0.00) | rgba(0,0,0,0.00) | STROKE_COLOR |
| `checkbox/checked/inverse-icon/default` | `color/action/indicator/brand/hard/default` | rgba(23,77,146,1.00) | rgba(147,192,249,1.00) | SHAPE_FILL |
| `checkbox/checked/inverse-icon/disabled` | `color/action/indicator/base/inverse-hard/disabled` | rgba(255,255,255,0.30) | rgba(0,0,0,0.30) | SHAPE_FILL |
| `checkbox/checked/inverse-icon/hover` | `color/action/indicator/brand/hard/default` | rgba(23,77,146,1.00) | rgba(147,192,249,1.00) | SHAPE_FILL |
| `checkbox/checked/inverse-icon/pressed` | `color/action/indicator/brand/hard/default` | rgba(23,77,146,1.00) | rgba(147,192,249,1.00) | SHAPE_FILL |
| `checkbox/focus-ring` | `color/static/focus/brand` | rgba(39,129,243,1.00) | rgba(61,142,244,1.00) | STROKE_COLOR |
| `checkbox/loading/box-checked` | `color/static/bg/transparent/accent/brand/medium` | rgba(39,129,243,0.50) | rgba(39,129,243,0.50) | FRAME_FILL |
| `checkbox/loading/box-uncheked` | `color/static/bg/transparent/base/light` | rgba(0,0,0,0.10) | rgba(255,255,255,0.10) | FRAME_FILL |
| `checkbox/loading/description` | `color/static/bg/transparent/base/mild` | rgba(0,0,0,0.05) | rgba(255,255,255,0.05) | FRAME_FILL |
| `checkbox/loading/icon` | `color/static/bg/transparent/base/light` | rgba(0,0,0,0.10) | rgba(255,255,255,0.10) | FRAME_FILL |
| `checkbox/loading/inverse-box-checked` | `color/static/bg/transparent/base/inverse-light` | rgba(255,255,255,0.10) | rgba(0,0,0,0.10) | FRAME_FILL |
| `checkbox/loading/inverse-box-uncheked` | `color/static/bg/transparent/base/inverse-light` | rgba(255,255,255,0.10) | rgba(0,0,0,0.10) | FRAME_FILL |
| `checkbox/loading/inverse-description` | `color/static/bg/transparent/base/inverse-mild` | rgba(255,255,255,0.05) | rgba(0,0,0,0.05) | FRAME_FILL |
| `checkbox/loading/inverse-icon` | `color/static/bg/transparent/base/inverse-light` | rgba(255,255,255,0.10) | rgba(0,0,0,0.10) | FRAME_FILL |
| `checkbox/loading/inverse-name` | `color/static/bg/transparent/base/inverse-light` | rgba(255,255,255,0.10) | rgba(0,0,0,0.10) | FRAME_FILL |
| `checkbox/loading/name` | `color/static/bg/transparent/base/light` | rgba(0,0,0,0.10) | rgba(255,255,255,0.10) | FRAME_FILL |
| `checkbox/size/card/border` | `border/checkbox/card` | 1 | 1 | STROKE_FLOAT |
| `checkbox/size/card/l/icon` | `size/checkbox/icon/card/l` | 24 | 24 | WIDTH_HEIGHT |
| `checkbox/size/card/l/icon-text` | `space/checkbox/card/y/l-icon-text` | 36 | 36 | GAP |
| `checkbox/size/card/l/x` | `space/checkbox/card/x/l` | 16 | 16 | GAP |
| `checkbox/size/card/l/y-bottom` | `space/checkbox/card/y/l-bottom` | 16 | 16 | GAP |
| `checkbox/size/card/l/y-top` | `space/checkbox/card/y/l-top` | 16 | 16 | GAP |
| `checkbox/size/card/m/icon` | `size/checkbox/icon/card/m` | 20 | 20 | WIDTH_HEIGHT |
| `checkbox/size/card/m/icon-text` | `space/checkbox/card/y/m-icon-text` | 28 | 28 | GAP |
| `checkbox/size/card/m/x` | `space/checkbox/card/x/m` | 12 | 12 | GAP |
| `checkbox/size/card/m/y-bottom` | `space/checkbox/card/y/m-bottom` | 12 | 12 | GAP |
| `checkbox/size/card/m/y-top` | `space/checkbox/card/y/m-top` | 12 | 12 | GAP |
| `checkbox/size/card/radius` | `radius/checkbox/card` | 12 | 12 | CORNER_RADIUS |
| `checkbox/size/main/l/box` | `size/checkbox/box/l` | 20 | 20 | WIDTH_HEIGHT |
| `checkbox/size/main/l/box-border` | `border/checkbox/box/l` | 1 | 1 | STROKE_FLOAT |
| `checkbox/size/main/l/box-check-y-bottom` | `space/checkbox/box/y/l-check-bottom` | 1 | 1 | GAP |
| `checkbox/size/main/l/box-check-y-top` | `space/checkbox/box/y/l-check-top` | 3 | 3 | GAP |
| `checkbox/size/main/l/box-container` | `size/checkbox/box-container/l` | 24 | 24 | WIDTH_HEIGHT |
| `checkbox/size/main/l/box-container-xy` | `space/checkbox/container/xy-l` | 2 | 2 | GAP |
| `checkbox/size/main/l/box-icon-x` | `space/checkbox/box/x/l` | 2 | 2 | GAP |
| `checkbox/size/main/l/box-icon-y` | `space/checkbox/box/y/l` | 2 | 2 | GAP |
| `checkbox/size/main/l/box-radius` | `radius/checkbox/box/l` | 5 | 5 | CORNER_RADIUS |
| `checkbox/size/main/l/checkbox-text-gap` | `gap/checkbox/checkbox-text/l` | 10 | 10 | GAP |
| `checkbox/size/main/l/focus-border` | `border/checkbox/focus/l` | 2 | 2 | STROKE_FLOAT |
| `checkbox/size/main/l/focus-radius` | `radius/checkbox/focus/l` | 8 | 8 | CORNER_RADIUS |
| `checkbox/size/main/l/icon` | `size/checkbox/icon/check/l` | 16 | 16 | WIDTH_HEIGHT |
| `checkbox/size/main/l/text-container-x` | `space/checkbox/text-container/x/l` | 0 | 0 | GAP |
| `checkbox/size/main/l/text-container-y` | `space/checkbox/text-container/y/l` | 0 | 0 | GAP |
| `checkbox/size/main/l/text-interline-gap` | `gap/checkbox/text-interline/l` | 0 | 0 | GAP |
| `checkbox/size/main/m/box` | `size/checkbox/box/m` | 16 | 16 | WIDTH_HEIGHT |
| `checkbox/size/main/m/box-border` | `border/checkbox/box/m` | 1 | 1 | STROKE_FLOAT |
| `checkbox/size/main/m/box-check-y-bottom` | `space/checkbox/box/y/m-check-bottom` | 1 | 1 | GAP |
| `checkbox/size/main/m/box-check-y-top` | `space/checkbox/box/y/m-check-top` | 2 | 2 | GAP |
| `checkbox/size/main/m/box-container` | `size/checkbox/box-container/m` | 20 | 20 | WIDTH_HEIGHT |
| `checkbox/size/main/m/box-container-xy` | `space/checkbox/container/xy-m` | 2 | 2 | GAP |
| `checkbox/size/main/m/box-icon-x` | `space/checkbox/box/x/m` | 1 | 1 | GAP |
| `checkbox/size/main/m/box-icon-y` | `space/checkbox/box/y/m` | 1 | 1 | GAP |
| `checkbox/size/main/m/box-radius` | `radius/checkbox/box/m` | 4 | 4 | CORNER_RADIUS |
| `checkbox/size/main/m/checkbox-text-gap` | `gap/checkbox/checkbox-text/m` | 6 | 6 | GAP |
| `checkbox/size/main/m/focus-border` | `border/checkbox/focus/m` | 1 | 1 | STROKE_FLOAT |
| `checkbox/size/main/m/focus-radius` | `radius/checkbox/focus/m` | 6 | 6 | CORNER_RADIUS |
| `checkbox/size/main/m/icon` | `size/checkbox/icon/check/m` | 13 | 13 | WIDTH_HEIGHT |
| `checkbox/size/main/m/text-container-x` | `space/checkbox/text-container/x/m` | 0 | 0 | GAP |
| `checkbox/size/main/m/text-container-y` | `space/checkbox/text-container/y/m` | 0 | 0 | GAP |
| `checkbox/size/main/m/text-interline-gap` | `gap/checkbox/text-interline/m` | 0 | 0 | GAP |
| `checkbox/text/description` | `color/static/text/base/medium` | rgba(0,0,0,0.60) | rgba(255,255,255,0.70) | TEXT_FILL |
| `checkbox/text/disabled` | `color/static/text/base/light` | rgba(0,0,0,0.45) | rgba(255,255,255,0.45) | TEXT_FILL |
| `checkbox/text/inverse-description` | `color/static/text/base/inverse-medium` | rgba(255,255,255,0.70) | rgba(0,0,0,0.60) | TEXT_FILL |
| `checkbox/text/inverse-disabled` | `color/static/text/base/inverse-light` | rgba(255,255,255,0.45) | rgba(0,0,0,0.45) | TEXT_FILL |
| `checkbox/text/inverse-name` | `color/static/text/base/inverse-hard` | rgba(255,255,255,1.00) | rgba(0,0,0,0.85) | TEXT_FILL |
| `checkbox/text/name` | `color/static/text/base/hard` | rgba(0,0,0,0.85) | rgba(255,255,255,1.00) | TEXT_FILL |
| `checkbox/unchecked/bg/default` | `color/action/bg/base/controls/default` | rgba(0,0,0,0.00) | rgba(255,255,255,0.00) | FRAME_FILL |
| `checkbox/unchecked/bg/disabled` | `color/action/bg/base/controls/disabled` | rgba(0,0,0,0.10) | rgba(255,255,255,0.07) | FRAME_FILL |
| `checkbox/unchecked/bg/hover` | `color/action/bg/base/controls/hover` | rgba(0,0,0,0.07) | rgba(255,255,255,0.07) | FRAME_FILL |
| `checkbox/unchecked/bg/pressed` | `color/action/bg/base/controls/pressed` | rgba(0,0,0,0.12) | rgba(255,255,255,0.12) | FRAME_FILL |
| `checkbox/unchecked/border/default` | `color/action/border/base/controls/default` | rgba(0,0,0,0.30) | rgba(255,255,255,0.30) | STROKE_COLOR |
| `checkbox/unchecked/border/disabled` | `color/action/border/base/controls/disabled` | rgba(0,0,0,0.00) | rgba(255,255,255,0.00) | STROKE_COLOR |
| `checkbox/unchecked/border/error` | `color/static/border/danger/firm` | rgba(240,48,48,1.00) | rgba(242,68,68,1.00) | STROKE_COLOR |
| `checkbox/unchecked/border/hover` | `color/action/border/base/controls/hover` | rgba(0,0,0,0.40) | rgba(255,255,255,0.40) | STROKE_COLOR |
| `checkbox/unchecked/border/pressed` | `color/action/border/base/controls/pressed` | rgba(0,0,0,0.50) | rgba(255,255,255,0.50) | STROKE_COLOR |
| `checkbox/unchecked/error` | `color/static/bg/solid/red/medium` | rgba(240,48,48,1.00) | rgba(242,68,68,1.00) | SHAPE_FILL |
| `checkbox/unchecked/inverse-bg/default` | `color/action/bg/base/inverse-controls/default` | rgba(255,255,255,0.00) | rgba(0,0,0,0.00) | FRAME_FILL |
| `checkbox/unchecked/inverse-bg/disabled` | `color/action/bg/base/inverse-controls/disabled` | rgba(255,255,255,0.07) | rgba(0,0,0,0.10) | FRAME_FILL |
| `checkbox/unchecked/inverse-bg/hover` | `color/action/bg/base/inverse-controls/hover` | rgba(255,255,255,0.07) | rgba(0,0,0,0.07) | FRAME_FILL |
| `checkbox/unchecked/inverse-bg/pressed` | `color/action/bg/base/inverse-controls/pressed` | rgba(255,255,255,0.12) | rgba(0,0,0,0.12) | FRAME_FILL |
| `checkbox/unchecked/inverse-border/default` | `color/action/border/base/inverse-controls/default` | rgba(255,255,255,0.35) | rgba(0,0,0,0.30) | STROKE_COLOR |
| `checkbox/unchecked/inverse-border/disabled` | `color/action/border/base/inverse-controls/disabled` | rgba(255,255,255,0.00) | rgba(0,0,0,0.00) | STROKE_COLOR |
| `checkbox/unchecked/inverse-border/error` | `color/static/border/danger/inverse-firm` | rgba(242,68,68,1.00) | rgba(240,48,48,1.00) | STROKE_COLOR |
| `checkbox/unchecked/inverse-border/hover` | `color/action/border/base/inverse-controls/hover` | rgba(255,255,255,0.45) | rgba(0,0,0,0.40) | STROKE_COLOR |
| `checkbox/unchecked/inverse-border/pressed` | `color/action/border/base/inverse-controls/pressed` | rgba(255,255,255,0.55) | rgba(0,0,0,0.50) | STROKE_COLOR |

## Текстовые стили

| Стиль | Шрифт | Переменные |
|---|---|---|
| `typography/action/checkbox/l/name` | Roboto Regular | `typography/checkbox/l/name/size`, `typography/checkbox/l/name/line-height`, `typography/checkbox/l/name/letter-spacing`, `typography/checkbox/l/name/weight` |
| `typography/action/checkbox/l/description` | Roboto Regular | `typography/checkbox/l/description/size`, `typography/checkbox/l/description/line-height`, `typography/checkbox/l/description/letter-spacing`, `typography/checkbox/l/description/weight` |
| `typography/action/checkbox/m/name` | Roboto Regular | `typography/checkbox/m/name/size`, `typography/checkbox/m/name/line-height`, `typography/checkbox/m/name/letter-spacing`, `typography/checkbox/m/name/weight` |
| `typography/action/checkbox/m/description` | Roboto Regular | `typography/checkbox/m/description/size`, `typography/checkbox/m/description/line-height`, `typography/checkbox/m/description/letter-spacing`, `typography/checkbox/m/description/weight` |

## Решения и допущения

- Пресет снят с текущей системы: повторная запись в исходный файл должна дать 0 изменений.
