# Токены: SimpleSelect

Пресет: `presets/field-select.tokens.json`. Источник: `input/tokens/variables.json`. Аналог: `—`.

Статус проверки: **OK** · L2 новых: 177 · L3: 218 · текстовых стилей: 12

## Заметки

- L3 `field/select/dropdown/option/indicator/icon`: изменение одобрено (2026-09-21, галочка выбранного пункта: контраст ≥ 3:1 на подложке выбранного (WCAG 1.4.11)): color/static/indicator/brand/medium → color/static/indicator/brand/hard
- L3 `field/select/dropdown/option/indicator/inverse-icon`: изменение одобрено (2026-09-21, галочка выбранного пункта: контраст ≥ 3:1 на подложке выбранного (WCAG 1.4.11)): color/static/indicator/brand/inverse-firm → color/static/indicator/brand/inverse-hard
- L3 `field/select/leading-icon/inverse-inactive`: изменение одобрено (2026-09-21, контраст WCAG на inverse-поверхности; иконка в цвет текста): color/static/indicator/base/inverse-soft → color/static/indicator/base/inverse-medium
- L3 `field/select/text/inverse-inactive`: изменение одобрено (2026-09-21, контраст WCAG на inverse-поверхности; иконка в цвет текста): color/static/text/base/inverse-soft → color/static/text/base/inverse-medium
- L3 `field/select/validation-icons/error`: изменение одобрено (2026-09-21, contrast WCAG (light и dark), иконка в цвет текста): color/static/indicator/danger/firm → color/static/indicator/danger/hard
- L3 `field/select/validation-icons/inverse-error`: изменение одобрено (2026-09-21, контраст WCAG на inverse-поверхности; иконка в цвет текста): color/static/indicator/danger/inverse-firm → color/static/indicator/danger/inverse-hard
- L3 `field/select/validation-icons/inverse-success`: изменение одобрено (2026-09-21, контраст WCAG на inverse-поверхности; иконка в цвет текста): color/static/indicator/success/inverse-firm → color/static/indicator/success/inverse-hard
- L3 `field/select/validation-icons/inverse-warning`: изменение одобрено (2026-09-21, контраст WCAG на inverse-поверхности; иконка в цвет текста): color/static/indicator/warning/inverse-firm → color/static/indicator/warning/inverse-hard
- L3 `field/select/validation-icons/success`: изменение одобрено (2026-09-21, contrast WCAG (light и dark), иконка в цвет текста): color/static/indicator/success/firm → color/static/indicator/success/hard
- L3 `field/select/validation-icons/warning`: изменение одобрено (2026-09-21, contrast WCAG (light и dark), иконка в цвет текста): color/static/indicator/warning/firm → color/static/indicator/warning/hard
- Пресет снят с текущей системы; проверена сверка с индексом один к одному.

## Новые токены L2 (`2. General`)

| Токен | light | dark | scopes |
|---|---|---|---|
| `border/field/select/button/l` | `border/1` | `border/1` | STROKE_FLOAT |
| `border/field/select/button/m` | `border/1` | `border/1` | STROKE_FLOAT |
| `border/field/select/button/s` | `border/1` | `border/1` | STROKE_FLOAT |
| `border/field/select/focus/l` | `border/2` | `border/2` | STROKE_FLOAT |
| `border/field/select/focus/m` | `border/2` | `border/2` | STROKE_FLOAT |
| `border/field/select/focus/s` | `border/1` | `border/1` | STROKE_FLOAT |
| `gap/field/select/button-dropdown/l` | `space/4` | `space/4` | GAP |
| `gap/field/select/button-dropdown/m` | `space/4` | `space/4` | GAP |
| `gap/field/select/button-dropdown/s` | `space/4` | `space/4` | GAP |
| `gap/field/select/button/l` | `space/0` | `space/0` | GAP |
| `gap/field/select/button/m` | `space/0` | `space/0` | GAP |
| `gap/field/select/button/s` | `space/0` | `space/0` | GAP |
| `gap/field/select/dropdown/l` | `space/0` | `space/0` | GAP |
| `gap/field/select/dropdown/m` | `space/0` | `space/0` | GAP |
| `gap/field/select/dropdown/s` | `space/0` | `space/0` | GAP |
| `gap/field/select/option/l` | `space/0` | `space/0` | GAP |
| `gap/field/select/option/m` | `space/0` | `space/0` | GAP |
| `gap/field/select/option/s` | `space/0` | `space/0` | GAP |
| `gap/field/select/text/l` | `space/0` | `space/0` | GAP |
| `gap/field/select/text/m` | `space/0` | `space/0` | GAP |
| `gap/field/select/text/s` | `space/0` | `space/0` | GAP |
| `gap/field/select/trailing/l` | `space/8` | `space/8` | GAP |
| `gap/field/select/trailing/m` | `space/6` | `space/6` | GAP |
| `gap/field/select/trailing/s` | `space/4` | `space/4` | GAP |
| `radius/field/select/button/l` | `radius/10` | `radius/10` | CORNER_RADIUS |
| `radius/field/select/button/m` | `radius/8` | `radius/8` | CORNER_RADIUS |
| `radius/field/select/button/s` | `radius/6` | `radius/6` | CORNER_RADIUS |
| `radius/field/select/focus/l` | `radius/12` | `radius/12` | CORNER_RADIUS |
| `radius/field/select/focus/m` | `radius/10` | `radius/10` | CORNER_RADIUS |
| `radius/field/select/focus/s` | `radius/8` | `radius/8` | CORNER_RADIUS |
| `radius/field/select/option/l` | `radius/10` | `radius/10` | CORNER_RADIUS |
| `radius/field/select/option/m` | `radius/8` | `radius/8` | CORNER_RADIUS |
| `radius/field/select/option/s` | `radius/6` | `radius/6` | CORNER_RADIUS |
| `size/field/select/action/l` | `size/28` | `size/28` | WIDTH_HEIGHT |
| `size/field/select/action/m` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `size/field/select/action/s` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `size/field/select/button/l` | `size/48` | `size/48` | WIDTH_HEIGHT |
| `size/field/select/button/m` | `size/40` | `size/40` | WIDTH_HEIGHT |
| `size/field/select/button/s` | `size/32` | `size/32` | WIDTH_HEIGHT |
| `size/field/select/leading/icon-box/l` | `size/28` | `size/28` | WIDTH_HEIGHT |
| `size/field/select/leading/icon-box/m` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `size/field/select/leading/icon-box/s` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `size/field/select/leading/icon/l` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `size/field/select/leading/icon/m` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `size/field/select/leading/icon/s` | `size/16` | `size/16` | WIDTH_HEIGHT |
| `size/field/select/loading/icon-box/l` | `size/28` | `size/28` | WIDTH_HEIGHT |
| `size/field/select/loading/icon-box/m` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `size/field/select/loading/icon-box/s` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `size/field/select/loading/icon/l` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `size/field/select/loading/icon/m` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `size/field/select/loading/icon/s` | `size/16` | `size/16` | WIDTH_HEIGHT |
| `size/field/select/option/container/l` | `size/48` | `size/48` | WIDTH_HEIGHT |
| `size/field/select/option/container/m` | `size/40` | `size/40` | WIDTH_HEIGHT |
| `size/field/select/option/container/s` | `size/32` | `size/32` | WIDTH_HEIGHT |
| `size/field/select/option/indicator/icon-box/l` | `size/28` | `size/28` | WIDTH_HEIGHT |
| `size/field/select/option/indicator/icon-box/m` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `size/field/select/option/indicator/icon-box/s` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `size/field/select/option/indicator/icon/l` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `size/field/select/option/indicator/icon/m` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `size/field/select/option/indicator/icon/s` | `size/16` | `size/16` | WIDTH_HEIGHT |
| `size/field/select/option/leading/icon-box/l` | `size/28` | `size/28` | WIDTH_HEIGHT |
| `size/field/select/option/leading/icon-box/m` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `size/field/select/option/leading/icon-box/s` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `size/field/select/option/leading/icon/l` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `size/field/select/option/leading/icon/m` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `size/field/select/option/leading/icon/s` | `size/16` | `size/16` | WIDTH_HEIGHT |
| `size/field/select/option/loader/l` | `size/32` | `size/32` | WIDTH_HEIGHT |
| `size/field/select/option/loader/m` | `size/28` | `size/28` | WIDTH_HEIGHT |
| `size/field/select/option/loader/s` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `size/field/select/validation-markers/icon-box/l` | `size/28` | `size/28` | WIDTH_HEIGHT |
| `size/field/select/validation-markers/icon-box/m` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `size/field/select/validation-markers/icon-box/s` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `size/field/select/validation-markers/icon/l` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `size/field/select/validation-markers/icon/m` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `size/field/select/validation-markers/icon/s` | `size/16` | `size/16` | WIDTH_HEIGHT |
| `space/field/select/action/l` | `space/2` | `space/2` | GAP |
| `space/field/select/action/m` | `space/2` | `space/2` | GAP |
| `space/field/select/action/s` | `space/2` | `space/2` | GAP |
| `space/field/select/button/x/l` | `space/10` | `space/10` | GAP |
| `space/field/select/button/x/m` | `space/8` | `space/8` | GAP |
| `space/field/select/button/x/s` | `space/6` | `space/6` | GAP |
| `space/field/select/button/y/l` | `space/10` | `space/10` | GAP |
| `space/field/select/button/y/m` | `space/8` | `space/8` | GAP |
| `space/field/select/button/y/s` | `space/6` | `space/6` | GAP |
| `space/field/select/dropdown/x/l` | `space/2` | `space/2` | GAP |
| `space/field/select/dropdown/x/m` | `space/2` | `space/2` | GAP |
| `space/field/select/dropdown/x/s` | `space/2` | `space/2` | GAP |
| `space/field/select/dropdown/y/l` | `space/4` | `space/4` | GAP |
| `space/field/select/dropdown/y/m` | `space/3` | `space/3` | GAP |
| `space/field/select/dropdown/y/s` | `space/2` | `space/2` | GAP |
| `space/field/select/leading-icon/l` | `space/2` | `space/2` | GAP |
| `space/field/select/leading-icon/m` | `space/2` | `space/2` | GAP |
| `space/field/select/leading-icon/s` | `space/2` | `space/2` | GAP |
| `space/field/select/loading-icon/l` | `space/2` | `space/2` | GAP |
| `space/field/select/loading-icon/m` | `space/2` | `space/2` | GAP |
| `space/field/select/loading-icon/s` | `space/2` | `space/2` | GAP |
| `space/field/select/option/container/x/l` | `space/10` | `space/10` | GAP |
| `space/field/select/option/container/x/m` | `space/8` | `space/8` | GAP |
| `space/field/select/option/container/x/s` | `space/6` | `space/6` | GAP |
| `space/field/select/option/container/y/l` | `space/10` | `space/10` | GAP |
| `space/field/select/option/container/y/m` | `space/8` | `space/8` | GAP |
| `space/field/select/option/container/y/s` | `space/6` | `space/6` | GAP |
| `space/field/select/option/indicator/l` | `space/2` | `space/2` | GAP |
| `space/field/select/option/indicator/m` | `space/2` | `space/2` | GAP |
| `space/field/select/option/indicator/s` | `space/2` | `space/2` | GAP |
| `space/field/select/option/leading-icon/l` | `space/2` | `space/2` | GAP |
| `space/field/select/option/leading-icon/m` | `space/2` | `space/2` | GAP |
| `space/field/select/option/leading-icon/s` | `space/2` | `space/2` | GAP |
| `space/field/select/option/text/x/l-left` | `space/4` | `space/4` | GAP |
| `space/field/select/option/text/x/l-right` | `space/2` | `space/2` | GAP |
| `space/field/select/option/text/x/m-left` | `space/4` | `space/4` | GAP |
| `space/field/select/option/text/x/m-right` | `space/2` | `space/2` | GAP |
| `space/field/select/option/text/x/s-left` | `space/4` | `space/4` | GAP |
| `space/field/select/option/text/x/s-right` | `space/2` | `space/2` | GAP |
| `space/field/select/option/text/y/l` | `space/0` | `space/0` | GAP |
| `space/field/select/option/text/y/m` | `space/0` | `space/0` | GAP |
| `space/field/select/option/text/y/s` | `space/0` | `space/0` | GAP |
| `space/field/select/text/x/l-left` | `space/4` | `space/4` | GAP |
| `space/field/select/text/x/l-right` | `space/2` | `space/2` | GAP |
| `space/field/select/text/x/m-left` | `space/4` | `space/4` | GAP |
| `space/field/select/text/x/m-right` | `space/2` | `space/2` | GAP |
| `space/field/select/text/x/s-left` | `space/4` | `space/4` | GAP |
| `space/field/select/text/x/s-right` | `space/2` | `space/2` | GAP |
| `space/field/select/text/y/l` | `space/0` | `space/0` | GAP |
| `space/field/select/text/y/m` | `space/0` | `space/0` | GAP |
| `space/field/select/text/y/s` | `space/0` | `space/0` | GAP |
| `space/field/select/validation-icon/l` | `space/2` | `space/2` | GAP |
| `space/field/select/validation-icon/m` | `space/2` | `space/2` | GAP |
| `space/field/select/validation-icon/s` | `space/2` | `space/2` | GAP |
| `typography/field/select/hint/l/letter-spacing` | `font/letter-spacing/0` | `font/letter-spacing/0` | LETTER_SPACING |
| `typography/field/select/hint/l/line-height` | `font/line-height/28` | `font/line-height/28` | LINE_HEIGHT |
| `typography/field/select/hint/l/size` | `font/size/18` | `font/size/18` | FONT_SIZE |
| `typography/field/select/hint/l/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |
| `typography/field/select/hint/m/letter-spacing` | `font/letter-spacing/0` | `font/letter-spacing/0` | LETTER_SPACING |
| `typography/field/select/hint/m/line-height` | `font/line-height/24` | `font/line-height/24` | LINE_HEIGHT |
| `typography/field/select/hint/m/size` | `font/size/16` | `font/size/16` | FONT_SIZE |
| `typography/field/select/hint/m/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |
| `typography/field/select/hint/s/letter-spacing` | `font/letter-spacing/10` | `font/letter-spacing/10` | LETTER_SPACING |
| `typography/field/select/hint/s/line-height` | `font/line-height/20` | `font/line-height/20` | LINE_HEIGHT |
| `typography/field/select/hint/s/size` | `font/size/14` | `font/size/14` | FONT_SIZE |
| `typography/field/select/hint/s/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |
| `typography/field/select/option-title/l/letter-spacing` | `font/letter-spacing/0` | `font/letter-spacing/0` | LETTER_SPACING |
| `typography/field/select/option-title/l/line-height` | `font/line-height/28` | `font/line-height/28` | LINE_HEIGHT |
| `typography/field/select/option-title/l/size` | `font/size/18` | `font/size/18` | FONT_SIZE |
| `typography/field/select/option-title/l/weight` | `font/weight/500` | `font/weight/500` | FONT_WEIGHT |
| `typography/field/select/option-title/m/letter-spacing` | `font/letter-spacing/0` | `font/letter-spacing/0` | LETTER_SPACING |
| `typography/field/select/option-title/m/line-height` | `font/line-height/24` | `font/line-height/24` | LINE_HEIGHT |
| `typography/field/select/option-title/m/size` | `font/size/16` | `font/size/16` | FONT_SIZE |
| `typography/field/select/option-title/m/weight` | `font/weight/500` | `font/weight/500` | FONT_WEIGHT |
| `typography/field/select/option-title/s/letter-spacing` | `font/letter-spacing/10` | `font/letter-spacing/10` | LETTER_SPACING |
| `typography/field/select/option-title/s/line-height` | `font/line-height/20` | `font/line-height/20` | LINE_HEIGHT |
| `typography/field/select/option-title/s/size` | `font/size/14` | `font/size/14` | FONT_SIZE |
| `typography/field/select/option-title/s/weight` | `font/weight/500` | `font/weight/500` | FONT_WEIGHT |
| `typography/field/select/option/l/letter-spacing` | `font/letter-spacing/0` | `font/letter-spacing/0` | LETTER_SPACING |
| `typography/field/select/option/l/line-height` | `font/line-height/28` | `font/line-height/28` | LINE_HEIGHT |
| `typography/field/select/option/l/size` | `font/size/18` | `font/size/18` | FONT_SIZE |
| `typography/field/select/option/l/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |
| `typography/field/select/option/m/letter-spacing` | `font/letter-spacing/0` | `font/letter-spacing/0` | LETTER_SPACING |
| `typography/field/select/option/m/line-height` | `font/line-height/24` | `font/line-height/24` | LINE_HEIGHT |
| `typography/field/select/option/m/size` | `font/size/16` | `font/size/16` | FONT_SIZE |
| `typography/field/select/option/m/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |
| `typography/field/select/option/s/letter-spacing` | `font/letter-spacing/10` | `font/letter-spacing/10` | LETTER_SPACING |
| `typography/field/select/option/s/line-height` | `font/line-height/20` | `font/line-height/20` | LINE_HEIGHT |
| `typography/field/select/option/s/size` | `font/size/14` | `font/size/14` | FONT_SIZE |
| `typography/field/select/option/s/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |
| `typography/field/select/text/l/letter-spacing` | `font/letter-spacing/0` | `font/letter-spacing/0` | LETTER_SPACING |
| `typography/field/select/text/l/line-height` | `font/line-height/28` | `font/line-height/28` | LINE_HEIGHT |
| `typography/field/select/text/l/size` | `font/size/18` | `font/size/18` | FONT_SIZE |
| `typography/field/select/text/l/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |
| `typography/field/select/text/m/letter-spacing` | `font/letter-spacing/0` | `font/letter-spacing/0` | LETTER_SPACING |
| `typography/field/select/text/m/line-height` | `font/line-height/24` | `font/line-height/24` | LINE_HEIGHT |
| `typography/field/select/text/m/size` | `font/size/16` | `font/size/16` | FONT_SIZE |
| `typography/field/select/text/m/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |
| `typography/field/select/text/s/letter-spacing` | `font/letter-spacing/10` | `font/letter-spacing/10` | LETTER_SPACING |
| `typography/field/select/text/s/line-height` | `font/line-height/20` | `font/line-height/20` | LINE_HEIGHT |
| `typography/field/select/text/s/size` | `font/size/14` | `font/size/14` | FONT_SIZE |
| `typography/field/select/text/s/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |

## Токены L3 (`3. Components`)

| Токен | → L2 | light | dark | scope |
|---|---|---|---|---|
| `field/select/bg/default` | `color/action/bg/base/pure/default` | rgba(255,255,255,1.00) | rgba(31,31,31,1.00) | FRAME_FILL |
| `field/select/bg/disabled` | `color/action/bg/base/pure/disabled` | rgba(0,0,0,0.03) | rgba(255,255,255,0.03) | FRAME_FILL |
| `field/select/bg/hover` | `color/action/bg/base/pure/hover` | rgba(0,0,0,0.03) | rgba(255,255,255,0.03) | FRAME_FILL |
| `field/select/bg/inverse-default` | `color/action/bg/base/inverse-pure/default` | rgba(31,31,31,1.00) | rgba(255,255,255,1.00) | FRAME_FILL |
| `field/select/bg/inverse-disabled` | `color/action/bg/base/inverse-pure/disabled` | rgba(255,255,255,0.03) | rgba(0,0,0,0.03) | FRAME_FILL |
| `field/select/bg/inverse-hover` | `color/action/bg/base/inverse-pure/hover` | rgba(255,255,255,0.03) | rgba(0,0,0,0.03) | FRAME_FILL |
| `field/select/bg/inverse-pressed` | `color/action/bg/base/inverse-pure/pressed` | rgba(255,255,255,0.07) | rgba(0,0,0,0.07) | FRAME_FILL |
| `field/select/bg/inverse-read-only` | `color/action/bg/base/inverse-pure/default` | rgba(31,31,31,1.00) | rgba(255,255,255,1.00) | FRAME_FILL |
| `field/select/bg/pressed` | `color/action/bg/base/pure/pressed` | rgba(0,0,0,0.07) | rgba(255,255,255,0.07) | FRAME_FILL |
| `field/select/bg/read-only` | `color/action/bg/base/pure/default` | rgba(255,255,255,1.00) | rgba(31,31,31,1.00) | FRAME_FILL |
| `field/select/border/default` | `color/action/border/base/soft/default` | rgba(0,0,0,0.15) | rgba(255,255,255,0.15) | STROKE_COLOR |
| `field/select/border/disabled` | `color/action/border/base/soft/disabled` | rgba(0,0,0,0.00) | rgba(255,255,255,0.00) | STROKE_COLOR |
| `field/select/border/error` | `color/action/border/danger/calm/selected` | rgba(240,48,48,1.00) | rgba(242,68,68,1.00) | STROKE_COLOR |
| `field/select/border/hover` | `color/action/border/base/soft/hover` | rgba(0,0,0,0.20) | rgba(255,255,255,0.25) | STROKE_COLOR |
| `field/select/border/inverse-default` | `color/action/border/base/inverse-soft/default` | rgba(255,255,255,0.20) | rgba(0,0,0,0.15) | STROKE_COLOR |
| `field/select/border/inverse-disabled` | `color/action/border/base/inverse-soft/disabled` | rgba(255,255,255,0.00) | rgba(0,0,0,0.00) | STROKE_COLOR |
| `field/select/border/inverse-error` | `color/action/border/danger/calm/inverse-selected` | rgba(242,68,68,1.00) | rgba(240,48,48,1.00) | STROKE_COLOR |
| `field/select/border/inverse-hover` | `color/action/border/base/inverse-soft/hover` | rgba(255,255,255,0.30) | rgba(0,0,0,0.25) | STROKE_COLOR |
| `field/select/border/inverse-pressed` | `color/action/border/base/inverse-soft/pressed` | rgba(255,255,255,0.35) | rgba(0,0,0,0.30) | STROKE_COLOR |
| `field/select/border/inverse-read-only` | `color/action/border/base/inverse-soft/read-only` | rgba(255,255,255,0.12) | rgba(0,0,0,0.10) | STROKE_COLOR |
| `field/select/border/inverse-success` | `color/action/border/success/calm/inverse-selected` | rgba(77,179,93,1.00) | rgba(69,161,84,1.00) | STROKE_COLOR |
| `field/select/border/inverse-warning` | `color/action/border/warning/calm/inverse-selected` | rgba(215,185,35,1.00) | rgba(193,166,32,1.00) | STROKE_COLOR |
| `field/select/border/pressed` | `color/action/border/base/soft/pressed` | rgba(0,0,0,0.25) | rgba(255,255,255,0.30) | STROKE_COLOR |
| `field/select/border/read-only` | `color/action/border/base/soft/read-only` | rgba(0,0,0,0.10) | rgba(255,255,255,0.10) | STROKE_COLOR |
| `field/select/border/success` | `color/action/border/success/calm/selected` | rgba(69,161,84,1.00) | rgba(77,179,93,1.00) | STROKE_COLOR |
| `field/select/border/warning` | `color/action/border/warning/calm/selected` | rgba(193,166,32,1.00) | rgba(215,185,35,1.00) | STROKE_COLOR |
| `field/select/dropdown/container/base` | `color/static/bg/solid/base/pure` | rgba(255,255,255,1.00) | rgba(31,31,31,1.00) | FRAME_FILL |
| `field/select/dropdown/container/hint` | `color/static/text/base/light` | rgba(0,0,0,0.45) | rgba(255,255,255,0.45) | TEXT_FILL |
| `field/select/dropdown/container/inverse-base` | `color/static/bg/solid/base/inverse-pure` | rgba(23,23,23,1.00) | rgba(255,255,255,1.00) | FRAME_FILL |
| `field/select/dropdown/container/inverse-hint` | `color/static/text/base/inverse-light` | rgba(255,255,255,0.45) | rgba(0,0,0,0.45) | TEXT_FILL |
| `field/select/dropdown/container/inverse-loader-icon` | `color/static/indicator/base/inverse-medium` | rgba(255,255,255,0.70) | rgba(0,0,0,0.60) | SHAPE_FILL |
| `field/select/dropdown/container/loader-icon` | `color/static/indicator/base/medium` | rgba(0,0,0,0.60) | rgba(255,255,255,0.70) | SHAPE_FILL |
| `field/select/dropdown/option/bg/active` | `color/action/bg/brand/light/default` | rgba(39,129,243,0.10) | rgba(39,129,243,0.10) | FRAME_FILL |
| `field/select/dropdown/option/bg/active-disabled` | `color/action/bg/brand/light/disabled` | rgba(0,0,0,0.03) | rgba(255,255,255,0.03) | FRAME_FILL |
| `field/select/dropdown/option/bg/active-hover` | `color/action/bg/brand/light/hover` | rgba(39,129,243,0.20) | rgba(39,129,243,0.20) | FRAME_FILL |
| `field/select/dropdown/option/bg/default` | `color/action/bg/base/ghost/default` | rgba(0,0,0,0.00) | rgba(255,255,255,0.00) | FRAME_FILL |
| `field/select/dropdown/option/bg/disabled` | `color/action/bg/base/ghost/disabled` | rgba(0,0,0,0.00) | rgba(255,255,255,0.00) | FRAME_FILL |
| `field/select/dropdown/option/bg/hover` | `color/action/bg/base/ghost/hover` | rgba(0,0,0,0.03) | rgba(255,255,255,0.03) | FRAME_FILL |
| `field/select/dropdown/option/bg/inverse-active` | `color/action/bg/brand/calm/default` | rgba(39,129,243,0.20) | rgba(39,129,243,0.20) | FRAME_FILL |
| `field/select/dropdown/option/bg/inverse-active-disabled` | `color/action/bg/base/inverse-pure/disabled` | rgba(255,255,255,0.03) | rgba(0,0,0,0.03) | FRAME_FILL |
| `field/select/dropdown/option/bg/inverse-active-hover` | `color/action/bg/brand/calm/hover` | rgba(39,129,243,0.30) | rgba(39,129,243,0.30) | FRAME_FILL |
| `field/select/dropdown/option/bg/inverse-default` | `color/action/bg/base/inverse-ghost/default` | rgba(255,255,255,0.00) | rgba(0,0,0,0.00) | FRAME_FILL |
| `field/select/dropdown/option/bg/inverse-disabled` | `color/action/bg/base/inverse-ghost/disabled` | rgba(255,255,255,0.00) | rgba(0,0,0,0.00) | FRAME_FILL |
| `field/select/dropdown/option/bg/inverse-hover` | `color/action/bg/base/inverse-ghost/hover` | rgba(255,255,255,0.03) | rgba(0,0,0,0.03) | FRAME_FILL |
| `field/select/dropdown/option/bg/inverse-pressed` | `color/action/bg/base/inverse-ghost/pressed` | rgba(255,255,255,0.07) | rgba(0,0,0,0.07) | FRAME_FILL |
| `field/select/dropdown/option/bg/pressed` | `color/action/bg/base/ghost/pressed` | rgba(0,0,0,0.07) | rgba(255,255,255,0.07) | FRAME_FILL |
| `field/select/dropdown/option/divider/inverse` | `color/static/bg/transparent/base/inverse-light` | rgba(255,255,255,0.10) | rgba(0,0,0,0.10) | STROKE_COLOR |
| `field/select/dropdown/option/indicator/icon` | `color/static/indicator/brand/hard` | rgba(23,77,146,1.00) | rgba(147,192,249,1.00) | SHAPE_FILL |
| `field/select/dropdown/option/indicator/icon-disabled` | `color/static/indicator/brand/calm` | rgba(39,129,243,0.60) | rgba(39,129,243,0.60) | SHAPE_FILL |
| `field/select/dropdown/option/indicator/inverse-icon` | `color/static/indicator/brand/inverse-hard` | rgba(147,192,249,1.00) | rgba(23,77,146,1.00) | SHAPE_FILL |
| `field/select/dropdown/option/indicator/inverse-icon-disabled` | `color/static/indicator/brand/calm` | rgba(39,129,243,0.60) | rgba(39,129,243,0.60) | SHAPE_FILL |
| `field/select/dropdown/option/leading-icon/icon` | `color/static/indicator/base/hard` | rgba(0,0,0,0.85) | rgba(255,255,255,1.00) | SHAPE_FILL |
| `field/select/dropdown/option/leading-icon/inverse-icon` | `color/static/indicator/base/inverse-hard` | rgba(255,255,255,1.00) | rgba(0,0,0,0.85) | SHAPE_FILL |
| `field/select/dropdown/option/leading-icon/inverse-read-only` | `color/static/indicator/base/inverse-soft` | rgba(255,255,255,0.35) | rgba(0,0,0,0.35) | SHAPE_FILL |
| `field/select/dropdown/option/leading-icon/read-only` | `color/static/indicator/base/soft` | rgba(0,0,0,0.35) | rgba(255,255,255,0.35) | SHAPE_FILL |
| `field/select/dropdown/option/text/disabled` | `color/static/text/base/soft` | rgba(0,0,0,0.35) | rgba(255,255,255,0.35) | TEXT_FILL |
| `field/select/dropdown/option/text/inverse-disabled` | `color/static/text/base/inverse-soft` | rgba(255,255,255,0.35) | rgba(0,0,0,0.35) | TEXT_FILL |
| `field/select/dropdown/option/text/inverse-value` | `color/static/text/base/inverse-hard` | rgba(255,255,255,1.00) | rgba(0,0,0,0.85) | TEXT_FILL |
| `field/select/dropdown/option/text/value` | `color/static/text/base/hard` | rgba(0,0,0,0.85) | rgba(255,255,255,1.00) | TEXT_FILL |
| `field/select/focus-ring` | `color/static/focus/brand` | rgba(39,129,243,1.00) | rgba(61,142,244,1.00) | STROKE_COLOR |
| `field/select/inverse-focus-ring` | `color/static/focus/inverse-brand` | rgba(61,142,244,1.00) | rgba(39,129,243,1.00) | STROKE_COLOR |
| `field/select/leading-icon/disabled` | `color/static/indicator/base/soft` | rgba(0,0,0,0.35) | rgba(255,255,255,0.35) | SHAPE_FILL |
| `field/select/leading-icon/inactive` | `color/static/indicator/base/soft` | rgba(0,0,0,0.35) | rgba(255,255,255,0.35) | SHAPE_FILL |
| `field/select/leading-icon/inactive-disabled` | `color/static/indicator/base/mild` | rgba(0,0,0,0.25) | rgba(255,255,255,0.25) | SHAPE_FILL |
| `field/select/leading-icon/inverse-disabled` | `color/static/indicator/base/inverse-soft` | rgba(255,255,255,0.35) | rgba(0,0,0,0.35) | SHAPE_FILL |
| `field/select/leading-icon/inverse-inactive` | `color/static/indicator/base/inverse-medium` | rgba(255,255,255,0.70) | rgba(0,0,0,0.60) | SHAPE_FILL |
| `field/select/leading-icon/inverse-inactive-disabled` | `color/static/indicator/base/inverse-mild` | rgba(255,255,255,0.25) | rgba(0,0,0,0.25) | SHAPE_FILL |
| `field/select/leading-icon/inverse-read-only` | `color/static/indicator/base/inverse-light` | rgba(255,255,255,0.45) | rgba(0,0,0,0.45) | SHAPE_FILL |
| `field/select/leading-icon/inverse-value` | `color/static/indicator/base/inverse-hard` | rgba(255,255,255,1.00) | rgba(0,0,0,0.85) | SHAPE_FILL |
| `field/select/leading-icon/read-only` | `color/static/indicator/base/light` | rgba(0,0,0,0.45) | rgba(255,255,255,0.50) | SHAPE_FILL |
| `field/select/leading-icon/value` | `color/static/indicator/base/hard` | rgba(0,0,0,0.85) | rgba(255,255,255,1.00) | SHAPE_FILL |
| `field/select/loading/inverse-loading` | `color/static/indicator/base/inverse-light` | rgba(255,255,255,0.45) | rgba(0,0,0,0.45) | SHAPE_FILL |
| `field/select/loading/loading` | `color/static/indicator/base/light` | rgba(0,0,0,0.45) | rgba(255,255,255,0.50) | SHAPE_FILL |
| `field/select/text/disabled` | `color/static/text/base/soft` | rgba(0,0,0,0.35) | rgba(255,255,255,0.35) | TEXT_FILL |
| `field/select/text/inactive` | `color/static/text/base/soft` | rgba(0,0,0,0.35) | rgba(255,255,255,0.35) | TEXT_FILL |
| `field/select/text/inactive-disabled` | `color/static/text/base/mild` | rgba(0,0,0,0.25) | rgba(255,255,255,0.25) | TEXT_FILL |
| `field/select/text/inverse-disabled` | `color/static/text/base/inverse-soft` | rgba(255,255,255,0.35) | rgba(0,0,0,0.35) | TEXT_FILL |
| `field/select/text/inverse-inactive` | `color/static/text/base/inverse-medium` | rgba(255,255,255,0.70) | rgba(0,0,0,0.60) | TEXT_FILL |
| `field/select/text/inverse-inactive-disabled` | `color/static/text/base/inverse-mild` | rgba(255,255,255,0.25) | rgba(0,0,0,0.25) | TEXT_FILL |
| `field/select/text/inverse-read-only` | `color/static/text/base/inverse-medium` | rgba(255,255,255,0.70) | rgba(0,0,0,0.60) | TEXT_FILL |
| `field/select/text/inverse-value` | `color/static/text/base/inverse-hard` | rgba(255,255,255,1.00) | rgba(0,0,0,0.85) | TEXT_FILL |
| `field/select/text/read-only` | `color/static/text/base/medium` | rgba(0,0,0,0.60) | rgba(255,255,255,0.70) | TEXT_FILL |
| `field/select/text/value` | `color/static/text/base/hard` | rgba(0,0,0,0.85) | rgba(255,255,255,1.00) | TEXT_FILL |
| `field/select/validation-icons/error` | `color/static/indicator/danger/hard` | rgba(156,25,25,1.00) | rgba(244,146,146,1.00) | SHAPE_FILL |
| `field/select/validation-icons/inverse-error` | `color/static/indicator/danger/inverse-hard` | rgba(244,146,146,1.00) | rgba(156,25,25,1.00) | SHAPE_FILL |
| `field/select/validation-icons/inverse-success` | `color/static/indicator/success/inverse-hard` | rgba(166,217,174,1.00) | rgba(46,107,56,1.00) | SHAPE_FILL |
| `field/select/validation-icons/inverse-warning` | `color/static/indicator/warning/inverse-hard` | rgba(235,220,145,1.00) | rgba(129,111,21,1.00) | SHAPE_FILL |
| `field/select/validation-icons/success` | `color/static/indicator/success/hard` | rgba(46,107,56,1.00) | rgba(166,217,174,1.00) | SHAPE_FILL |
| `field/select/validation-icons/warning` | `color/static/indicator/warning/hard` | rgba(129,111,21,1.00) | rgba(235,220,145,1.00) | SHAPE_FILL |
| `field/size/select/l/button-dropdown-gap` | `gap/field/select/button-dropdown/l` | 4 | 4 | GAP |
| `field/size/select/l/button/action-box` | `size/field/select/action/l` | 28 | 28 | WIDTH_HEIGHT |
| `field/size/select/l/button/action-xy` | `space/field/select/action/l` | 2 | 2 | GAP |
| `field/size/select/l/button/container` | `size/field/select/button/l` | 48 | 48 | WIDTH_HEIGHT |
| `field/size/select/l/button/container-border` | `border/field/select/button/l` | 1 | 1 | STROKE_FLOAT |
| `field/size/select/l/button/container-gap` | `gap/field/select/button/l` | 0 | 0 | GAP |
| `field/size/select/l/button/container-radius` | `radius/field/select/button/l` | 10 | 10 | CORNER_RADIUS |
| `field/size/select/l/button/container-x` | `space/field/select/button/x/l` | 10 | 10 | GAP |
| `field/size/select/l/button/container-y` | `space/field/select/button/y/l` | 10 | 10 | GAP |
| `field/size/select/l/button/focus-border` | `border/field/select/focus/l` | 2 | 2 | STROKE_FLOAT |
| `field/size/select/l/button/focus-radius` | `radius/field/select/focus/l` | 12 | 12 | CORNER_RADIUS |
| `field/size/select/l/button/leading-icon` | `size/field/select/leading/icon/l` | 24 | 24 | WIDTH_HEIGHT |
| `field/size/select/l/button/leading-icon-box` | `size/field/select/leading/icon-box/l` | 28 | 28 | WIDTH_HEIGHT |
| `field/size/select/l/button/leading-icon-xy` | `space/field/select/leading-icon/l` | 2 | 2 | GAP |
| `field/size/select/l/button/loading-icon` | `size/field/select/loading/icon/l` | 24 | 24 | WIDTH_HEIGHT |
| `field/size/select/l/button/loading-icon-box` | `size/field/select/loading/icon-box/l` | 28 | 28 | WIDTH_HEIGHT |
| `field/size/select/l/button/loading-icon-xy` | `space/field/select/loading-icon/l` | 2 | 2 | GAP |
| `field/size/select/l/button/text-gap` | `gap/field/select/text/l` | 0 | 0 | GAP |
| `field/size/select/l/button/text-x-left` | `space/field/select/text/x/l-left` | 4 | 4 | GAP |
| `field/size/select/l/button/text-x-right` | `space/field/select/text/x/l-right` | 2 | 2 | GAP |
| `field/size/select/l/button/text-y` | `space/field/select/text/y/l` | 0 | 0 | GAP |
| `field/size/select/l/button/trailing-gap` | `gap/field/select/trailing/l` | 8 | 8 | GAP |
| `field/size/select/l/button/validation-icon` | `size/field/select/validation-markers/icon/l` | 24 | 24 | WIDTH_HEIGHT |
| `field/size/select/l/button/validation-icon-box` | `size/field/select/validation-markers/icon-box/l` | 28 | 28 | WIDTH_HEIGHT |
| `field/size/select/l/button/validation-icon-xy` | `space/field/select/validation-icon/l` | 2 | 2 | GAP |
| `field/size/select/l/dropdown-box/container-gap` | `gap/field/select/dropdown/l` | 0 | 0 | GAP |
| `field/size/select/l/dropdown-box/container-x` | `space/field/select/dropdown/x/l` | 2 | 2 | GAP |
| `field/size/select/l/dropdown-box/container-y` | `space/field/select/dropdown/y/l` | 4 | 4 | GAP |
| `field/size/select/l/dropdown-box/loader` | `size/field/select/option/loader/l` | 32 | 32 | WIDTH_HEIGHT |
| `field/size/select/l/option/container` | `size/field/select/option/container/l` | 48 | 48 | WIDTH_HEIGHT |
| `field/size/select/l/option/container-gap` | `gap/field/select/option/l` | 0 | 0 | GAP |
| `field/size/select/l/option/container-radius` | `radius/field/select/option/l` | 10 | 10 | CORNER_RADIUS |
| `field/size/select/l/option/container-x` | `space/field/select/option/container/x/l` | 10 | 10 | GAP |
| `field/size/select/l/option/container-y` | `space/field/select/option/container/y/l` | 10 | 10 | GAP |
| `field/size/select/l/option/indicator-icon` | `size/field/select/option/indicator/icon/l` | 24 | 24 | WIDTH_HEIGHT |
| `field/size/select/l/option/indicator-icon-box` | `size/field/select/option/indicator/icon-box/l` | 28 | 28 | WIDTH_HEIGHT |
| `field/size/select/l/option/indicator-icon-xy` | `space/field/select/option/indicator/l` | 2 | 2 | GAP |
| `field/size/select/l/option/leading-icon` | `size/field/select/leading/icon/l` | 24 | 24 | WIDTH_HEIGHT |
| `field/size/select/l/option/leading-icon-box` | `size/field/select/leading/icon-box/l` | 28 | 28 | WIDTH_HEIGHT |
| `field/size/select/l/option/leading-icon-xy` | `space/field/select/leading-icon/l` | 2 | 2 | GAP |
| `field/size/select/l/option/text-x-left` | `space/field/select/option/text/x/l-left` | 4 | 4 | GAP |
| `field/size/select/l/option/text-x-right` | `space/field/select/option/text/x/l-right` | 2 | 2 | GAP |
| `field/size/select/l/option/text-y` | `space/field/select/option/text/y/l` | 0 | 0 | GAP |
| `field/size/select/m/button-dropdown-gap` | `gap/field/select/button-dropdown/m` | 4 | 4 | GAP |
| `field/size/select/m/button/action-box` | `size/field/select/action/m` | 24 | 24 | WIDTH_HEIGHT |
| `field/size/select/m/button/action-xy` | `space/field/select/action/m` | 2 | 2 | GAP |
| `field/size/select/m/button/container` | `size/field/select/button/m` | 40 | 40 | WIDTH_HEIGHT |
| `field/size/select/m/button/container-border` | `border/field/select/button/m` | 1 | 1 | STROKE_FLOAT |
| `field/size/select/m/button/container-gap` | `gap/field/select/button/m` | 0 | 0 | GAP |
| `field/size/select/m/button/container-radius` | `radius/field/select/button/m` | 8 | 8 | CORNER_RADIUS |
| `field/size/select/m/button/container-x` | `space/field/select/button/x/m` | 8 | 8 | GAP |
| `field/size/select/m/button/container-y` | `space/field/select/button/y/m` | 8 | 8 | GAP |
| `field/size/select/m/button/focus-border` | `border/field/select/focus/m` | 2 | 2 | STROKE_FLOAT |
| `field/size/select/m/button/focus-radius` | `radius/field/select/focus/m` | 10 | 10 | CORNER_RADIUS |
| `field/size/select/m/button/leading-icon` | `size/field/select/leading/icon/m` | 20 | 20 | WIDTH_HEIGHT |
| `field/size/select/m/button/leading-icon-box` | `size/field/select/leading/icon-box/m` | 24 | 24 | WIDTH_HEIGHT |
| `field/size/select/m/button/leading-icon-xy` | `space/field/select/leading-icon/m` | 2 | 2 | GAP |
| `field/size/select/m/button/loading-icon` | `size/field/select/loading/icon/m` | 20 | 20 | WIDTH_HEIGHT |
| `field/size/select/m/button/loading-icon-box` | `size/field/select/loading/icon-box/m` | 24 | 24 | WIDTH_HEIGHT |
| `field/size/select/m/button/loading-icon-xy` | `space/field/select/loading-icon/m` | 2 | 2 | GAP |
| `field/size/select/m/button/text-gap` | `gap/field/select/text/m` | 0 | 0 | GAP |
| `field/size/select/m/button/text-x-left` | `space/field/select/text/x/m-left` | 4 | 4 | GAP |
| `field/size/select/m/button/text-x-right` | `space/field/select/text/x/m-right` | 2 | 2 | GAP |
| `field/size/select/m/button/text-y` | `space/field/select/text/y/m` | 0 | 0 | GAP |
| `field/size/select/m/button/trailing-gap` | `gap/field/select/trailing/m` | 6 | 6 | GAP |
| `field/size/select/m/button/validation-icon` | `size/field/select/validation-markers/icon/m` | 20 | 20 | WIDTH_HEIGHT |
| `field/size/select/m/button/validation-icon-box` | `size/field/select/validation-markers/icon-box/m` | 24 | 24 | WIDTH_HEIGHT |
| `field/size/select/m/button/validation-icon-xy` | `space/field/select/validation-icon/m` | 2 | 2 | GAP |
| `field/size/select/m/dropdown-box/container-gap` | `gap/field/select/dropdown/m` | 0 | 0 | GAP |
| `field/size/select/m/dropdown-box/container-x` | `space/field/select/dropdown/x/m` | 2 | 2 | GAP |
| `field/size/select/m/dropdown-box/container-y` | `space/field/select/dropdown/y/m` | 3 | 3 | GAP |
| `field/size/select/m/dropdown-box/loader` | `size/field/select/option/loader/m` | 28 | 28 | WIDTH_HEIGHT |
| `field/size/select/m/option/container` | `size/field/select/option/container/m` | 40 | 40 | WIDTH_HEIGHT |
| `field/size/select/m/option/container-gap` | `gap/field/select/option/m` | 0 | 0 | GAP |
| `field/size/select/m/option/container-radius` | `radius/field/select/option/m` | 8 | 8 | CORNER_RADIUS |
| `field/size/select/m/option/container-x` | `space/field/select/option/container/x/m` | 8 | 8 | GAP |
| `field/size/select/m/option/container-y` | `space/field/select/option/container/y/m` | 8 | 8 | GAP |
| `field/size/select/m/option/indicator-icon` | `size/field/select/option/indicator/icon/m` | 20 | 20 | WIDTH_HEIGHT |
| `field/size/select/m/option/indicator-icon-box` | `size/field/select/option/indicator/icon-box/m` | 24 | 24 | WIDTH_HEIGHT |
| `field/size/select/m/option/indicator-icon-xy` | `space/field/select/option/indicator/m` | 2 | 2 | GAP |
| `field/size/select/m/option/leading-icon` | `size/field/select/leading/icon/m` | 20 | 20 | WIDTH_HEIGHT |
| `field/size/select/m/option/leading-icon-box` | `size/field/select/leading/icon-box/m` | 24 | 24 | WIDTH_HEIGHT |
| `field/size/select/m/option/leading-icon-xy` | `space/field/select/leading-icon/m` | 2 | 2 | GAP |
| `field/size/select/m/option/text-x-left` | `space/field/select/option/text/x/m-left` | 4 | 4 | GAP |
| `field/size/select/m/option/text-x-right` | `space/field/select/option/text/x/m-right` | 2 | 2 | GAP |
| `field/size/select/m/option/text-y` | `space/field/select/option/text/y/m` | 0 | 0 | GAP |
| `field/size/select/s/button-dropdown-gap` | `gap/field/select/button-dropdown/s` | 4 | 4 | GAP |
| `field/size/select/s/button/action-box` | `size/field/select/action/s` | 20 | 20 | WIDTH_HEIGHT |
| `field/size/select/s/button/action-xy` | `space/field/select/action/s` | 2 | 2 | GAP |
| `field/size/select/s/button/container` | `size/field/select/button/s` | 32 | 32 | WIDTH_HEIGHT |
| `field/size/select/s/button/container-border` | `border/field/select/button/s` | 1 | 1 | STROKE_FLOAT |
| `field/size/select/s/button/container-gap` | `gap/field/select/button/s` | 0 | 0 | GAP |
| `field/size/select/s/button/container-radius` | `radius/field/select/button/s` | 6 | 6 | CORNER_RADIUS |
| `field/size/select/s/button/container-x` | `space/field/select/button/x/s` | 6 | 6 | GAP |
| `field/size/select/s/button/container-y` | `space/field/select/button/y/s` | 6 | 6 | GAP |
| `field/size/select/s/button/focus-border` | `border/field/select/focus/s` | 1 | 1 | STROKE_FLOAT |
| `field/size/select/s/button/focus-radius` | `radius/field/select/focus/s` | 8 | 8 | CORNER_RADIUS |
| `field/size/select/s/button/leading-icon` | `size/field/select/leading/icon/s` | 16 | 16 | WIDTH_HEIGHT |
| `field/size/select/s/button/leading-icon-box` | `size/field/select/leading/icon-box/s` | 20 | 20 | WIDTH_HEIGHT |
| `field/size/select/s/button/leading-icon-xy` | `space/field/select/leading-icon/s` | 2 | 2 | GAP |
| `field/size/select/s/button/loading-icon` | `size/field/select/loading/icon/s` | 16 | 16 | WIDTH_HEIGHT |
| `field/size/select/s/button/loading-icon-box` | `size/field/select/loading/icon-box/s` | 20 | 20 | WIDTH_HEIGHT |
| `field/size/select/s/button/loading-icon-xy` | `space/field/select/loading-icon/s` | 2 | 2 | GAP |
| `field/size/select/s/button/text-gap` | `gap/field/select/text/s` | 0 | 0 | GAP |
| `field/size/select/s/button/text-x-left` | `space/field/select/text/x/s-left` | 4 | 4 | GAP |
| `field/size/select/s/button/text-x-right` | `space/field/select/text/x/s-right` | 2 | 2 | GAP |
| `field/size/select/s/button/text-y` | `space/field/select/text/y/s` | 0 | 0 | GAP |
| `field/size/select/s/button/trailing-gap` | `gap/field/select/trailing/s` | 4 | 4 | GAP |
| `field/size/select/s/button/validation-icon` | `size/field/select/validation-markers/icon/s` | 16 | 16 | WIDTH_HEIGHT |
| `field/size/select/s/button/validation-icon-box` | `size/field/select/validation-markers/icon-box/s` | 20 | 20 | WIDTH_HEIGHT |
| `field/size/select/s/button/validation-icon-xy` | `space/field/select/validation-icon/s` | 2 | 2 | GAP |
| `field/size/select/s/dropdown-box/container-gap` | `gap/field/select/dropdown/s` | 0 | 0 | GAP |
| `field/size/select/s/dropdown-box/container-x` | `space/field/select/dropdown/x/s` | 2 | 2 | GAP |
| `field/size/select/s/dropdown-box/container-y` | `space/field/select/dropdown/y/s` | 2 | 2 | GAP |
| `field/size/select/s/dropdown-box/loader` | `size/field/select/option/loader/s` | 24 | 24 | WIDTH_HEIGHT |
| `field/size/select/s/option/container` | `size/field/select/option/container/s` | 32 | 32 | WIDTH_HEIGHT |
| `field/size/select/s/option/container-gap` | `gap/field/select/option/s` | 0 | 0 | GAP |
| `field/size/select/s/option/container-radius` | `radius/field/select/option/s` | 6 | 6 | CORNER_RADIUS |
| `field/size/select/s/option/container-x` | `space/field/select/option/container/x/s` | 6 | 6 | GAP |
| `field/size/select/s/option/container-y` | `space/field/select/option/container/y/s` | 6 | 6 | GAP |
| `field/size/select/s/option/indicator-icon` | `size/field/select/option/indicator/icon/s` | 16 | 16 | WIDTH_HEIGHT |
| `field/size/select/s/option/indicator-icon-box` | `size/field/select/option/indicator/icon-box/s` | 20 | 20 | WIDTH_HEIGHT |
| `field/size/select/s/option/indicator-icon-xy` | `space/field/select/option/indicator/s` | 2 | 2 | GAP |
| `field/size/select/s/option/leading-icon` | `size/field/select/leading/icon/s` | 16 | 16 | WIDTH_HEIGHT |
| `field/size/select/s/option/leading-icon-box` | `size/field/select/leading/icon-box/s` | 20 | 20 | WIDTH_HEIGHT |
| `field/size/select/s/option/leading-icon-xy` | `space/field/select/leading-icon/s` | 2 | 2 | GAP |
| `field/size/select/s/option/text-x-left` | `space/field/select/option/text/x/s-left` | 4 | 4 | GAP |
| `field/size/select/s/option/text-x-right` | `space/field/select/option/text/x/s-right` | 2 | 2 | GAP |
| `field/size/select/s/option/text-y` | `space/field/select/option/text/y/s` | 0 | 0 | GAP |

## Текстовые стили

| Стиль | Шрифт | Переменные |
|---|---|---|
| `typography/field/select/text/l` | Roboto Regular | `typography/field/select/text/l/size`, `typography/field/select/text/l/line-height`, `typography/field/select/text/l/letter-spacing`, `typography/field/select/text/l/weight` |
| `typography/field/select/text/m` | Roboto Regular | `typography/field/select/text/m/size`, `typography/field/select/text/m/line-height`, `typography/field/select/text/m/letter-spacing`, `typography/field/select/text/m/weight` |
| `typography/field/select/text/s` | Roboto Regular | `typography/field/select/text/s/size`, `typography/field/select/text/s/line-height`, `typography/field/select/text/s/letter-spacing`, `typography/field/select/text/s/weight` |
| `typography/field/select/option/l` | Roboto Regular | `typography/field/select/option/l/size`, `typography/field/select/option/l/line-height`, `typography/field/select/option/l/letter-spacing`, `typography/field/select/option/l/weight` |
| `typography/field/select/option/m` | Roboto Regular | `typography/field/select/option/m/size`, `typography/field/select/option/m/line-height`, `typography/field/select/option/m/letter-spacing`, `typography/field/select/option/m/weight` |
| `typography/field/select/option/s` | Roboto Regular | `typography/field/select/option/s/size`, `typography/field/select/option/s/line-height`, `typography/field/select/option/s/letter-spacing`, `typography/field/select/option/s/weight` |
| `typography/field/select/option_title/l` | Roboto Medium | `typography/field/select/option-title/l/size`, `typography/field/select/option-title/l/line-height`, `typography/field/select/option-title/l/letter-spacing`, `typography/field/select/option-title/l/weight` |
| `typography/field/select/option_title/m` | Roboto Medium | `typography/field/select/option-title/m/size`, `typography/field/select/option-title/m/line-height`, `typography/field/select/option-title/m/letter-spacing`, `typography/field/select/option-title/m/weight` |
| `typography/field/select/option_title/s` | Roboto Medium | `typography/field/select/option-title/s/size`, `typography/field/select/option-title/s/line-height`, `typography/field/select/option-title/s/letter-spacing`, `typography/field/select/option-title/s/weight` |
| `typography/field/select/hint/l` | Roboto Regular | `typography/field/select/hint/l/size`, `typography/field/select/hint/l/line-height`, `typography/field/select/hint/l/letter-spacing`, `typography/field/select/hint/l/weight` |
| `typography/field/select/hint/m` | Roboto Regular | `typography/field/select/hint/m/size`, `typography/field/select/hint/m/line-height`, `typography/field/select/hint/m/letter-spacing`, `typography/field/select/hint/m/weight` |
| `typography/field/select/hint/s` | Roboto Regular | `typography/field/select/hint/s/size`, `typography/field/select/hint/s/line-height`, `typography/field/select/hint/s/letter-spacing`, `typography/field/select/hint/s/weight` |

## Решения и допущения

- Пресет снят с текущей системы: повторная запись в исходный файл должна дать 0 изменений.
