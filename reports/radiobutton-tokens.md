# Токены: Radiobutton

Пресет: `presets/radiobutton.tokens.json`. Источник: `input/tokens/variables.json`. Аналог: `—`.

Статус проверки: **OK** · L2 новых: 53 · L3: 106 · текстовых стилей: 4

## Заметки

- L3 `radiobutton/checked/icon/default`: изменение одобрено (2026-09-21, тёмная тема: контраст WCAG AA): color/action/indicator/base/inverse-hard/default → color/action/indicator/base/on-bold/default
- L3 `radiobutton/checked/icon/hover`: изменение одобрено (2026-09-21, тёмная тема: контраст WCAG AA): color/action/indicator/base/inverse-hard/default → color/action/indicator/base/on-bold/hover
- L3 `radiobutton/checked/icon/pressed`: изменение одобрено (2026-09-21, тёмная тема: контраст WCAG AA): color/action/indicator/base/inverse-hard/default → color/action/indicator/base/on-bold/pressed
- Пресет снят с текущей системы; проверена сверка с индексом один к одному.

## Новые токены L2 (`2. General`)

| Токен | light | dark | scopes |
|---|---|---|---|
| `border/radiobutton/box/l` | `border/1` | `border/1` | STROKE_FLOAT |
| `border/radiobutton/box/m` | `border/1` | `border/1` | STROKE_FLOAT |
| `border/radiobutton/card` | `border/1` | `border/1` | STROKE_FLOAT |
| `border/radiobutton/focus/l` | `border/2` | `border/2` | STROKE_FLOAT |
| `border/radiobutton/focus/m` | `border/1` | `border/1` | STROKE_FLOAT |
| `gap/radiobutton/radio-text/l` | `space/10` | `space/10` | GAP |
| `gap/radiobutton/radio-text/m` | `space/6` | `space/6` | GAP |
| `gap/radiobutton/text-interline/l` | `space/0` | `space/0` | GAP |
| `gap/radiobutton/text-interline/m` | `space/0` | `space/0` | GAP |
| `radius/radiobutton/box` | `radius/999` | `radius/999` | CORNER_RADIUS |
| `radius/radiobutton/card` | `radius/12` | `radius/12` | CORNER_RADIUS |
| `radius/radiobutton/focus` | `radius/999` | `radius/999` | CORNER_RADIUS |
| `radius/radiobutton/icon` | `radius/999` | `radius/999` | CORNER_RADIUS |
| `size/radiobutton/box-container/l` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `size/radiobutton/box-container/m` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `size/radiobutton/box/l` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `size/radiobutton/box/m` | `size/16` | `size/16` | WIDTH_HEIGHT |
| `size/radiobutton/icon/card/l` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `size/radiobutton/icon/card/m` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `size/radiobutton/icon/radio/l` | `size/10` | `size/10` | WIDTH_HEIGHT |
| `size/radiobutton/icon/radio/m` | `size/8` | `size/8` | WIDTH_HEIGHT |
| `space/radiobutton/box/xy-l` | `space/5` | `space/5` | GAP |
| `space/radiobutton/box/xy-m` | `space/4` | `space/4` | GAP |
| `space/radiobutton/card/x/l` | `space/16` | `space/16` | GAP |
| `space/radiobutton/card/x/m` | `space/12` | `space/12` | GAP |
| `space/radiobutton/card/y/l-bottom` | `space/16` | `space/16` | GAP |
| `space/radiobutton/card/y/l-icon-text` | `space/36` | `space/36` | GAP |
| `space/radiobutton/card/y/l-top` | `space/16` | `space/16` | GAP |
| `space/radiobutton/card/y/m-bottom` | `space/12` | `space/12` | GAP |
| `space/radiobutton/card/y/m-icon-text` | `space/28` | `space/28` | GAP |
| `space/radiobutton/card/y/m-top` | `space/12` | `space/12` | GAP |
| `space/radiobutton/container/xy-l` | `space/2` | `space/2` | GAP |
| `space/radiobutton/container/xy-m` | `space/2` | `space/2` | GAP |
| `space/radiobutton/text-container/x/l` | `space/0` | `space/0` | GAP |
| `space/radiobutton/text-container/x/m` | `space/0` | `space/0` | GAP |
| `space/radiobutton/text-container/y/l` | `space/0` | `space/0` | GAP |
| `space/radiobutton/text-container/y/m` | `space/0` | `space/0` | GAP |
| `typography/radiobutton/l/description/letter-spacing` | `font/letter-spacing/10` | `font/letter-spacing/10` | LETTER_SPACING |
| `typography/radiobutton/l/description/line-height` | `font/line-height/20` | `font/line-height/20` | LINE_HEIGHT |
| `typography/radiobutton/l/description/size` | `font/size/14` | `font/size/14` | FONT_SIZE |
| `typography/radiobutton/l/description/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |
| `typography/radiobutton/l/name/letter-spacing` | `font/letter-spacing/0` | `font/letter-spacing/0` | LETTER_SPACING |
| `typography/radiobutton/l/name/line-height` | `font/line-height/24` | `font/line-height/24` | LINE_HEIGHT |
| `typography/radiobutton/l/name/size` | `font/size/16` | `font/size/16` | FONT_SIZE |
| `typography/radiobutton/l/name/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |
| `typography/radiobutton/m/description/letter-spacing` | `font/letter-spacing/10` | `font/letter-spacing/10` | LETTER_SPACING |
| `typography/radiobutton/m/description/line-height` | `font/line-height/20` | `font/line-height/20` | LINE_HEIGHT |
| `typography/radiobutton/m/description/size` | `font/size/14` | `font/size/14` | FONT_SIZE |
| `typography/radiobutton/m/description/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |
| `typography/radiobutton/m/name/letter-spacing` | `font/letter-spacing/10` | `font/letter-spacing/10` | LETTER_SPACING |
| `typography/radiobutton/m/name/line-height` | `font/line-height/20` | `font/line-height/20` | LINE_HEIGHT |
| `typography/radiobutton/m/name/size` | `font/size/14` | `font/size/14` | FONT_SIZE |
| `typography/radiobutton/m/name/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |

## Токены L3 (`3. Components`)

| Токен | → L2 | light | dark | scope |
|---|---|---|---|---|
| `radiobutton/card/bg` | `color/static/bg/transparent/base/ghost` | rgba(0,0,0,0.00) | rgba(255,255,255,0.00) | FRAME_FILL |
| `radiobutton/card/border` | `color/static/border/base/soft` | rgba(0,0,0,0.07) | rgba(255,255,255,0.07) | STROKE_COLOR |
| `radiobutton/card/icon` | `color/static/indicator/base/hard` | rgba(0,0,0,0.85) | rgba(255,255,255,1.00) | SHAPE_FILL |
| `radiobutton/card/inverse-bg` | `color/static/bg/transparent/base/ghost` | rgba(0,0,0,0.00) | rgba(255,255,255,0.00) | FRAME_FILL |
| `radiobutton/card/inverse-border` | `color/static/border/base/inverse-light` | rgba(255,255,255,0.10) | rgba(0,0,0,0.10) | STROKE_COLOR |
| `radiobutton/card/inverse-icon` | `color/static/indicator/base/inverse-hard` | rgba(255,255,255,1.00) | rgba(0,0,0,0.85) | SHAPE_FILL |
| `radiobutton/checked/bg/default` | `color/action/bg/brand/medium/default` | rgba(39,129,243,1.00) | rgba(61,142,244,1.00) | FRAME_FILL |
| `radiobutton/checked/bg/disabled` | `color/action/bg/brand/medium/disabled` | rgba(39,129,243,0.50) | rgba(39,129,243,0.50) | FRAME_FILL |
| `radiobutton/checked/bg/hover` | `color/action/bg/brand/medium/hover` | rgba(35,116,219,1.00) | rgba(82,154,245,1.00) | FRAME_FILL |
| `radiobutton/checked/bg/pressed` | `color/action/bg/brand/medium/pressed` | rgba(31,103,194,1.00) | rgba(104,167,247,1.00) | FRAME_FILL |
| `radiobutton/checked/border/default` | `color/action/border/base/ghost/default` | rgba(0,0,0,0.00) | rgba(255,255,255,0.00) | STROKE_COLOR |
| `radiobutton/checked/border/disabled` | `color/action/border/base/ghost/default` | rgba(0,0,0,0.00) | rgba(255,255,255,0.00) | STROKE_COLOR |
| `radiobutton/checked/border/hover` | `color/action/border/base/ghost/default` | rgba(0,0,0,0.00) | rgba(255,255,255,0.00) | STROKE_COLOR |
| `radiobutton/checked/border/pressed` | `color/action/border/base/ghost/default` | rgba(0,0,0,0.00) | rgba(255,255,255,0.00) | STROKE_COLOR |
| `radiobutton/checked/icon/default` | `color/action/indicator/base/on-bold/default` | None | None | SHAPE_FILL |
| `radiobutton/checked/icon/disabled` | `color/action/indicator/base/inverse-hard/default` | rgba(255,255,255,1.00) | rgba(0,0,0,0.85) | SHAPE_FILL |
| `radiobutton/checked/icon/hover` | `color/action/indicator/base/on-bold/hover` | None | None | SHAPE_FILL |
| `radiobutton/checked/icon/pressed` | `color/action/indicator/base/on-bold/pressed` | None | None | SHAPE_FILL |
| `radiobutton/checked/inverse-bg/default` | `color/action/bg/base/inverse/default` | rgba(255,255,255,1.00) | rgba(31,31,31,1.00) | FRAME_FILL |
| `radiobutton/checked/inverse-bg/disabled` | `color/action/bg/base/inverse/disabled` | rgba(255,255,255,0.25) | rgba(0,0,0,0.10) | FRAME_FILL |
| `radiobutton/checked/inverse-bg/hover` | `color/action/bg/base/inverse/hover` | rgba(235,235,235,1.00) | rgba(61,61,61,1.00) | FRAME_FILL |
| `radiobutton/checked/inverse-bg/pressed` | `color/action/bg/base/inverse/pressed` | rgba(224,224,224,1.00) | rgba(77,77,77,1.00) | FRAME_FILL |
| `radiobutton/checked/inverse-border/default` | `color/action/border/base/inverse-ghost/default` | rgba(255,255,255,0.00) | rgba(0,0,0,0.00) | STROKE_COLOR |
| `radiobutton/checked/inverse-border/disabled` | `color/action/border/base/inverse-ghost/default` | rgba(255,255,255,0.00) | rgba(0,0,0,0.00) | STROKE_COLOR |
| `radiobutton/checked/inverse-border/hover` | `color/action/border/base/inverse-ghost/default` | rgba(255,255,255,0.00) | rgba(0,0,0,0.00) | STROKE_COLOR |
| `radiobutton/checked/inverse-border/pressed` | `color/action/border/base/inverse-ghost/default` | rgba(255,255,255,0.00) | rgba(0,0,0,0.00) | STROKE_COLOR |
| `radiobutton/checked/inverse-icon/default` | `color/action/indicator/brand/hard/default` | rgba(23,77,146,1.00) | rgba(147,192,249,1.00) | SHAPE_FILL |
| `radiobutton/checked/inverse-icon/disabled` | `color/action/indicator/base/inverse-hard/disabled` | rgba(255,255,255,0.30) | rgba(0,0,0,0.30) | SHAPE_FILL |
| `radiobutton/checked/inverse-icon/hover` | `color/action/indicator/brand/hard/default` | rgba(23,77,146,1.00) | rgba(147,192,249,1.00) | SHAPE_FILL |
| `radiobutton/checked/inverse-icon/pressed` | `color/action/indicator/brand/hard/default` | rgba(23,77,146,1.00) | rgba(147,192,249,1.00) | SHAPE_FILL |
| `radiobutton/focus-ring` | `color/static/focus/brand` | rgba(39,129,243,1.00) | rgba(61,142,244,1.00) | STROKE_COLOR |
| `radiobutton/loading/box-checked` | `color/static/bg/transparent/accent/brand/medium` | rgba(39,129,243,0.50) | rgba(39,129,243,0.50) | FRAME_FILL |
| `radiobutton/loading/box-uncheked` | `color/static/bg/transparent/base/light` | rgba(0,0,0,0.10) | rgba(255,255,255,0.10) | FRAME_FILL |
| `radiobutton/loading/description` | `color/static/bg/transparent/base/mild` | rgba(0,0,0,0.05) | rgba(255,255,255,0.05) | FRAME_FILL |
| `radiobutton/loading/icon` | `color/static/bg/transparent/base/light` | rgba(0,0,0,0.10) | rgba(255,255,255,0.10) | FRAME_FILL |
| `radiobutton/loading/inverse-box-checked` | `color/static/bg/transparent/base/inverse-light` | rgba(255,255,255,0.10) | rgba(0,0,0,0.10) | FRAME_FILL |
| `radiobutton/loading/inverse-box-uncheked` | `color/static/bg/transparent/base/inverse-light` | rgba(255,255,255,0.10) | rgba(0,0,0,0.10) | FRAME_FILL |
| `radiobutton/loading/inverse-description` | `color/static/bg/transparent/base/inverse-mild` | rgba(255,255,255,0.05) | rgba(0,0,0,0.05) | FRAME_FILL |
| `radiobutton/loading/inverse-icon` | `color/static/bg/transparent/base/inverse-light` | rgba(255,255,255,0.10) | rgba(0,0,0,0.10) | FRAME_FILL |
| `radiobutton/loading/inverse-name` | `color/static/bg/transparent/base/inverse-light` | rgba(255,255,255,0.10) | rgba(0,0,0,0.10) | FRAME_FILL |
| `radiobutton/loading/name` | `color/static/bg/transparent/base/light` | rgba(0,0,0,0.10) | rgba(255,255,255,0.10) | FRAME_FILL |
| `radiobutton/size/card/border` | `border/checkbox/card` | 1 | 1 | STROKE_FLOAT |
| `radiobutton/size/card/l/icon` | `size/radiobutton/icon/card/l` | 24 | 24 | WIDTH_HEIGHT |
| `radiobutton/size/card/l/icon-text` | `space/radiobutton/card/y/l-icon-text` | 36 | 36 | GAP |
| `radiobutton/size/card/l/x` | `space/radiobutton/card/x/l` | 16 | 16 | GAP |
| `radiobutton/size/card/l/y-bottom` | `space/radiobutton/card/y/l-bottom` | 16 | 16 | GAP |
| `radiobutton/size/card/l/y-top` | `space/radiobutton/card/y/l-top` | 16 | 16 | GAP |
| `radiobutton/size/card/m/icon` | `size/radiobutton/icon/card/m` | 20 | 20 | WIDTH_HEIGHT |
| `radiobutton/size/card/m/icon-text` | `space/radiobutton/card/y/m-icon-text` | 28 | 28 | GAP |
| `radiobutton/size/card/m/x` | `space/radiobutton/card/x/m` | 12 | 12 | GAP |
| `radiobutton/size/card/m/y-bottom` | `space/radiobutton/card/y/m-bottom` | 12 | 12 | GAP |
| `radiobutton/size/card/m/y-top` | `space/radiobutton/card/y/m-top` | 12 | 12 | GAP |
| `radiobutton/size/card/radius` | `radius/checkbox/card` | 12 | 12 | CORNER_RADIUS |
| `radiobutton/size/main/l/box` | `size/radiobutton/box/l` | 20 | 20 | WIDTH_HEIGHT |
| `radiobutton/size/main/l/box-border` | `border/radiobutton/box/l` | 1 | 1 | STROKE_FLOAT |
| `radiobutton/size/main/l/box-container` | `size/radiobutton/box-container/l` | 24 | 24 | WIDTH_HEIGHT |
| `radiobutton/size/main/l/box-container-xy` | `space/radiobutton/container/xy-l` | 2 | 2 | GAP |
| `radiobutton/size/main/l/box-radius` | `radius/radiobutton/box` | 999 | 999 | CORNER_RADIUS |
| `radiobutton/size/main/l/box-xy` | `space/radiobutton/box/xy-l` | 5 | 5 | GAP |
| `radiobutton/size/main/l/focus-border` | `border/radiobutton/focus/l` | 2 | 2 | STROKE_FLOAT |
| `radiobutton/size/main/l/focus-radius` | `radius/radiobutton/focus` | 999 | 999 | CORNER_RADIUS |
| `radiobutton/size/main/l/icon` | `size/radiobutton/icon/radio/l` | 10 | 10 | WIDTH_HEIGHT |
| `radiobutton/size/main/l/icon-radius` | `radius/radiobutton/icon` | 999 | 999 | CORNER_RADIUS |
| `radiobutton/size/main/l/radio-text-gap` | `gap/radiobutton/radio-text/l` | 10 | 10 | GAP |
| `radiobutton/size/main/l/text-container-x` | `space/radiobutton/text-container/x/l` | 0 | 0 | GAP |
| `radiobutton/size/main/l/text-container-y` | `space/radiobutton/text-container/y/l` | 0 | 0 | GAP |
| `radiobutton/size/main/l/text-interline-gap` | `gap/radiobutton/text-interline/l` | 0 | 0 | GAP |
| `radiobutton/size/main/m/box` | `size/radiobutton/box/m` | 16 | 16 | WIDTH_HEIGHT |
| `radiobutton/size/main/m/box-border` | `border/radiobutton/box/m` | 1 | 1 | STROKE_FLOAT |
| `radiobutton/size/main/m/box-container` | `size/radiobutton/box-container/m` | 20 | 20 | WIDTH_HEIGHT |
| `radiobutton/size/main/m/box-container-xy` | `space/radiobutton/container/xy-m` | 2 | 2 | GAP |
| `radiobutton/size/main/m/box-radius` | `radius/radiobutton/box` | 999 | 999 | CORNER_RADIUS |
| `radiobutton/size/main/m/box-xy` | `space/radiobutton/box/xy-m` | 4 | 4 | GAP |
| `radiobutton/size/main/m/focus-border` | `border/radiobutton/focus/m` | 1 | 1 | STROKE_FLOAT |
| `radiobutton/size/main/m/focus-radius` | `radius/radiobutton/focus` | 999 | 999 | CORNER_RADIUS |
| `radiobutton/size/main/m/icon` | `size/radiobutton/icon/radio/m` | 8 | 8 | WIDTH_HEIGHT |
| `radiobutton/size/main/m/icon-radius` | `radius/radiobutton/icon` | 999 | 999 | CORNER_RADIUS |
| `radiobutton/size/main/m/radio-text-gap` | `gap/radiobutton/radio-text/m` | 6 | 6 | GAP |
| `radiobutton/size/main/m/text-container-x` | `space/radiobutton/text-container/x/m` | 0 | 0 | GAP |
| `radiobutton/size/main/m/text-container-y` | `space/radiobutton/text-container/y/m` | 0 | 0 | GAP |
| `radiobutton/size/main/m/text-interline-gap` | `gap/radiobutton/text-interline/m` | 0 | 0 | GAP |
| `radiobutton/text/description` | `color/static/text/base/medium` | rgba(0,0,0,0.60) | rgba(255,255,255,0.70) | TEXT_FILL |
| `radiobutton/text/disabled` | `color/static/text/base/light` | rgba(0,0,0,0.45) | rgba(255,255,255,0.45) | TEXT_FILL |
| `radiobutton/text/inverse-description` | `color/static/text/base/inverse-medium` | rgba(255,255,255,0.70) | rgba(0,0,0,0.60) | TEXT_FILL |
| `radiobutton/text/inverse-disabled` | `color/static/text/base/inverse-light` | rgba(255,255,255,0.45) | rgba(0,0,0,0.45) | TEXT_FILL |
| `radiobutton/text/inverse-name` | `color/static/text/base/inverse-hard` | rgba(255,255,255,1.00) | rgba(0,0,0,0.85) | TEXT_FILL |
| `radiobutton/text/name` | `color/static/text/base/hard` | rgba(0,0,0,0.85) | rgba(255,255,255,1.00) | TEXT_FILL |
| `radiobutton/unchecked/bg/default` | `color/action/bg/base/controls/default` | rgba(0,0,0,0.00) | rgba(255,255,255,0.00) | FRAME_FILL |
| `radiobutton/unchecked/bg/disabled` | `color/action/bg/base/controls/disabled` | rgba(0,0,0,0.10) | rgba(255,255,255,0.07) | FRAME_FILL |
| `radiobutton/unchecked/bg/hover` | `color/action/bg/base/controls/hover` | rgba(0,0,0,0.07) | rgba(255,255,255,0.07) | FRAME_FILL |
| `radiobutton/unchecked/bg/pressed` | `color/action/bg/base/controls/pressed` | rgba(0,0,0,0.12) | rgba(255,255,255,0.12) | FRAME_FILL |
| `radiobutton/unchecked/border/default` | `color/action/border/base/controls/default` | rgba(0,0,0,0.30) | rgba(255,255,255,0.30) | STROKE_COLOR |
| `radiobutton/unchecked/border/disabled` | `color/action/border/base/controls/disabled` | rgba(0,0,0,0.00) | rgba(255,255,255,0.00) | STROKE_COLOR |
| `radiobutton/unchecked/border/error` | `color/static/border/danger/firm` | rgba(240,48,48,1.00) | rgba(242,68,68,1.00) | STROKE_COLOR |
| `radiobutton/unchecked/border/hover` | `color/action/border/base/controls/hover` | rgba(0,0,0,0.40) | rgba(255,255,255,0.40) | STROKE_COLOR |
| `radiobutton/unchecked/border/pressed` | `color/action/border/base/controls/pressed` | rgba(0,0,0,0.50) | rgba(255,255,255,0.50) | STROKE_COLOR |
| `radiobutton/unchecked/error` | `color/static/bg/solid/red/medium` | rgba(240,48,48,1.00) | rgba(242,68,68,1.00) | SHAPE_FILL |
| `radiobutton/unchecked/inverse-bg/default` | `color/action/bg/base/inverse-controls/default` | rgba(255,255,255,0.00) | rgba(0,0,0,0.00) | FRAME_FILL |
| `radiobutton/unchecked/inverse-bg/disabled` | `color/action/bg/base/inverse-controls/disabled` | rgba(255,255,255,0.07) | rgba(0,0,0,0.10) | FRAME_FILL |
| `radiobutton/unchecked/inverse-bg/hover` | `color/action/bg/base/inverse-controls/hover` | rgba(255,255,255,0.07) | rgba(0,0,0,0.07) | FRAME_FILL |
| `radiobutton/unchecked/inverse-bg/pressed` | `color/action/bg/base/inverse-controls/pressed` | rgba(255,255,255,0.12) | rgba(0,0,0,0.12) | FRAME_FILL |
| `radiobutton/unchecked/inverse-border/default` | `color/action/border/base/inverse-controls/default` | rgba(255,255,255,0.35) | rgba(0,0,0,0.30) | STROKE_COLOR |
| `radiobutton/unchecked/inverse-border/disabled` | `color/action/border/base/inverse-controls/disabled` | rgba(255,255,255,0.00) | rgba(0,0,0,0.00) | STROKE_COLOR |
| `radiobutton/unchecked/inverse-border/error` | `color/static/border/danger/inverse-firm` | rgba(242,68,68,1.00) | rgba(240,48,48,1.00) | STROKE_COLOR |
| `radiobutton/unchecked/inverse-border/hover` | `color/action/border/base/inverse-controls/hover` | rgba(255,255,255,0.45) | rgba(0,0,0,0.40) | STROKE_COLOR |
| `radiobutton/unchecked/inverse-border/pressed` | `color/action/border/base/inverse-controls/pressed` | rgba(255,255,255,0.55) | rgba(0,0,0,0.50) | STROKE_COLOR |

## Текстовые стили

| Стиль | Шрифт | Переменные |
|---|---|---|
| `typography/action/radiobutton/l/name` | Roboto Regular | `typography/radiobutton/l/name/size`, `typography/radiobutton/l/name/line-height`, `typography/radiobutton/l/name/letter-spacing`, `typography/radiobutton/l/name/weight` |
| `typography/action/radiobutton/l/description` | Roboto Regular | `typography/radiobutton/l/description/size`, `typography/radiobutton/l/description/line-height`, `typography/radiobutton/l/description/letter-spacing`, `typography/radiobutton/l/description/weight` |
| `typography/action/radiobutton/m/name` | Roboto Regular | `typography/radiobutton/m/name/size`, `typography/radiobutton/m/name/line-height`, `typography/radiobutton/m/name/letter-spacing`, `typography/radiobutton/m/name/weight` |
| `typography/action/radiobutton/m/description` | Roboto Regular | `typography/radiobutton/m/description/size`, `typography/radiobutton/m/description/line-height`, `typography/radiobutton/m/description/letter-spacing`, `typography/radiobutton/m/description/weight` |

## Решения и допущения

- Пресет снят с текущей системы: повторная запись в исходный файл должна дать 0 изменений.
