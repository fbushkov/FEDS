# Токены: Alert

Пресет: `presets/alert.tokens.json`. Источник: `input/backlog/alert.md`. Аналог: `status`.

Статус проверки: **OK** · L2 новых: 36 · L3: 68 · текстовых стилей: 4

## Новые токены L2 (`2. General`)

| Токен | light | dark | scopes |
|---|---|---|---|
| `border/alert/m` | `border/1` | `border/1` | STROKE_FLOAT |
| `border/alert/s` | `border/1` | `border/1` | STROKE_FLOAT |
| `gap/alert/actions/m` | `space/8` | `space/8` | GAP |
| `gap/alert/actions/s` | `space/4` | `space/4` | GAP |
| `gap/alert/close/m` | `space/8` | `space/8` | GAP |
| `gap/alert/close/s` | `space/8` | `space/8` | GAP |
| `gap/alert/icon/m` | `space/12` | `space/12` | GAP |
| `gap/alert/icon/s` | `space/8` | `space/8` | GAP |
| `gap/alert/title/m` | `space/4` | `space/4` | GAP |
| `gap/alert/title/s` | `space/4` | `space/4` | GAP |
| `radius/alert/m` | `radius/8` | `radius/8` | CORNER_RADIUS |
| `radius/alert/s` | `radius/6` | `radius/6` | CORNER_RADIUS |
| `size/alert/icon/m` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `size/alert/icon/s` | `size/16` | `size/16` | WIDTH_HEIGHT |
| `space/alert/x/m` | `space/16` | `space/16` | GAP |
| `space/alert/x/s` | `space/12` | `space/12` | GAP |
| `space/alert/y/m` | `space/16` | `space/16` | GAP |
| `space/alert/y/s` | `space/12` | `space/12` | GAP |
| `typography/alert/m/description/letter-spacing` | `font/letter-spacing/10` | `font/letter-spacing/10` | LETTER_SPACING |
| `typography/alert/m/description/line-height` | `font/line-height/20` | `font/line-height/20` | LINE_HEIGHT |
| `typography/alert/m/description/size` | `font/size/14` | `font/size/14` | FONT_SIZE |
| `typography/alert/m/description/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |
| `typography/alert/m/title/letter-spacing` | `font/letter-spacing/10` | `font/letter-spacing/10` | LETTER_SPACING |
| `typography/alert/m/title/line-height` | `font/line-height/20` | `font/line-height/20` | LINE_HEIGHT |
| `typography/alert/m/title/size` | `font/size/14` | `font/size/14` | FONT_SIZE |
| `typography/alert/m/title/weight` | `font/weight/600` | `font/weight/600` | FONT_WEIGHT |
| `typography/alert/s/description/letter-spacing` | `font/letter-spacing/25` | `font/letter-spacing/25` | LETTER_SPACING |
| `typography/alert/s/description/line-height` | `font/line-height/16` | `font/line-height/16` | LINE_HEIGHT |
| `typography/alert/s/description/size` | `font/size/12` | `font/size/12` | FONT_SIZE |
| `typography/alert/s/description/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |
| `typography/alert/s/title/letter-spacing` | `font/letter-spacing/25` | `font/letter-spacing/25` | LETTER_SPACING |
| `typography/alert/s/title/line-height` | `font/line-height/16` | `font/line-height/16` | LINE_HEIGHT |
| `typography/alert/s/title/size` | `font/size/12` | `font/size/12` | FONT_SIZE |
| `typography/alert/s/title/weight` | `font/weight/600` | `font/weight/600` | FONT_WEIGHT |
| `gap/alert/action/m` | `space/8` | `space/8` | GAP |
| `gap/alert/action/s` | `space/8` | `space/8` | GAP |

## Токены L3 (`3. Components`)

| Токен | → L2 | light | dark | scope |
|---|---|---|---|---|
| `alert/bg/error` | `color/status/red/soft/default` | rgba(240,48,48,0.07) | rgba(240,48,48,0.10) | FRAME_FILL |
| `alert/bg/info` | `color/status/blue/soft/default` | rgba(53,117,221,0.07) | rgba(53,117,221,0.10) | FRAME_FILL |
| `alert/bg/inverse-error` | `color/static/bg/transparent/accent/red/light` | rgba(240,48,48,0.10) | rgba(240,48,48,0.10) | FRAME_FILL |
| `alert/bg/inverse-info` | `color/static/bg/transparent/accent/blue/light` | rgba(53,117,221,0.10) | rgba(53,117,221,0.10) | FRAME_FILL |
| `alert/bg/inverse-success` | `color/static/bg/transparent/accent/green/light` | rgba(69,161,84,0.12) | rgba(69,161,84,0.12) | FRAME_FILL |
| `alert/bg/inverse-warning` | `color/static/bg/transparent/accent/yellow/light` | rgba(172,148,28,0.11) | rgba(172,148,28,0.11) | FRAME_FILL |
| `alert/bg/success` | `color/status/green/soft/default` | rgba(69,161,84,0.09) | rgba(69,161,84,0.12) | FRAME_FILL |
| `alert/bg/warning` | `color/status/yellow/soft/default` | rgba(172,148,28,0.08) | rgba(172,148,28,0.11) | FRAME_FILL |
| `alert/border/error` | `color/static/border/danger/firm` | rgba(240,48,48,1.00) | rgba(242,68,68,1.00) | STROKE_COLOR |
| `alert/border/info` | `color/static/border/info/firm` | rgba(59,130,246,1.00) | rgba(79,142,247,1.00) | STROKE_COLOR |
| `alert/border/inverse-error` | `color/static/border/danger/inverse-firm` | rgba(242,68,68,1.00) | rgba(240,48,48,1.00) | STROKE_COLOR |
| `alert/border/inverse-info` | `color/static/border/info/inverse-firm` | rgba(79,142,247,1.00) | rgba(59,130,246,1.00) | STROKE_COLOR |
| `alert/border/inverse-success` | `color/static/border/success/inverse-hard` | rgba(166,217,174,1.00) | rgba(46,107,56,1.00) | STROKE_COLOR |
| `alert/border/inverse-warning` | `color/static/border/warning/inverse-hard` | rgba(235,220,145,1.00) | rgba(129,111,21,1.00) | STROKE_COLOR |
| `alert/border/success` | `color/static/border/success/hard` | rgba(46,107,56,1.00) | rgba(166,217,174,1.00) | STROKE_COLOR |
| `alert/border/warning` | `color/static/border/warning/hard` | rgba(129,111,21,1.00) | rgba(235,220,145,1.00) | STROKE_COLOR |
| `alert/icon/error` | `color/static/indicator/danger/firm` | rgba(240,48,48,1.00) | rgba(242,68,68,1.00) | SHAPE_FILL |
| `alert/icon/info` | `color/static/indicator/info/firm` | rgba(59,130,246,1.00) | rgba(79,142,247,1.00) | SHAPE_FILL |
| `alert/icon/inverse-error` | `color/static/indicator/danger/inverse-firm` | rgba(242,68,68,1.00) | rgba(240,48,48,1.00) | SHAPE_FILL |
| `alert/icon/inverse-info` | `color/static/indicator/info/inverse-firm` | rgba(79,142,247,1.00) | rgba(59,130,246,1.00) | SHAPE_FILL |
| `alert/icon/inverse-success` | `color/static/indicator/success/inverse-hard` | rgba(166,217,174,1.00) | rgba(46,107,56,1.00) | SHAPE_FILL |
| `alert/icon/inverse-warning` | `color/static/indicator/warning/inverse-hard` | rgba(235,220,145,1.00) | rgba(129,111,21,1.00) | SHAPE_FILL |
| `alert/icon/success` | `color/static/indicator/success/hard` | rgba(46,107,56,1.00) | rgba(166,217,174,1.00) | SHAPE_FILL |
| `alert/icon/warning` | `color/static/indicator/warning/hard` | rgba(129,111,21,1.00) | rgba(235,220,145,1.00) | SHAPE_FILL |
| `alert/size/m/actions-gap` | `gap/alert/actions/m` | 8 | 8 | GAP |
| `alert/size/m/border` | `border/alert/m` | 1 | 1 | STROKE_FLOAT |
| `alert/size/m/close-gap` | `gap/alert/close/m` | 8 | 8 | GAP |
| `alert/size/m/icon` | `size/alert/icon/m` | 20 | 20 | WIDTH_HEIGHT |
| `alert/size/m/icon-gap` | `gap/alert/icon/m` | 12 | 12 | GAP |
| `alert/size/m/radius` | `radius/alert/m` | 8 | 8 | CORNER_RADIUS |
| `alert/size/m/title-gap` | `gap/alert/title/m` | 4 | 4 | GAP |
| `alert/size/m/x` | `space/alert/x/m` | 16 | 16 | GAP |
| `alert/size/m/y` | `space/alert/y/m` | 16 | 16 | GAP |
| `alert/size/s/actions-gap` | `gap/alert/actions/s` | 4 | 4 | GAP |
| `alert/size/s/border` | `border/alert/s` | 1 | 1 | STROKE_FLOAT |
| `alert/size/s/close-gap` | `gap/alert/close/s` | 8 | 8 | GAP |
| `alert/size/s/icon` | `size/alert/icon/s` | 16 | 16 | WIDTH_HEIGHT |
| `alert/size/s/icon-gap` | `gap/alert/icon/s` | 8 | 8 | GAP |
| `alert/size/s/radius` | `radius/alert/s` | 6 | 6 | CORNER_RADIUS |
| `alert/size/s/title-gap` | `gap/alert/title/s` | 4 | 4 | GAP |
| `alert/size/s/x` | `space/alert/x/s` | 12 | 12 | GAP |
| `alert/size/s/y` | `space/alert/y/s` | 12 | 12 | GAP |
| `alert/text/description` | `color/static/text/base/hard` | rgba(0,0,0,0.85) | rgba(255,255,255,1.00) | TEXT_FILL |
| `alert/text/inverse-description` | `color/static/text/base/inverse-hard` | rgba(255,255,255,1.00) | rgba(0,0,0,0.85) | TEXT_FILL |
| `alert/text/inverse-title` | `color/static/text/base/inverse-hard` | rgba(255,255,255,1.00) | rgba(0,0,0,0.85) | TEXT_FILL |
| `alert/text/title` | `color/static/text/base/hard` | rgba(0,0,0,0.85) | rgba(255,255,255,1.00) | TEXT_FILL |
| `alert/size/m/action-gap` | `gap/alert/action/m` | 8 | 8 | GAP |
| `alert/size/s/action-gap` | `gap/alert/action/s` | 8 | 8 | GAP |
| `alert/default/bg` | `color/bg/raised/main` | rgba(255,255,255,1.00) | rgba(31,31,31,1.00) | FRAME_FILL, SHAPE_FILL |
| `alert/default/inverse-bg` | `color/bg/raised/inverse-main` | rgba(31,31,31,1.00) | rgba(255,255,255,1.00) | FRAME_FILL, SHAPE_FILL |
| `alert/default/border` | `color/static/border/base/low` | rgba(0,0,0,0.20) | rgba(255,255,255,0.20) | STROKE_COLOR |
| `alert/default/inverse-border` | `color/static/border/base/inverse-low` | rgba(255,255,255,0.20) | rgba(0,0,0,0.20) | STROKE_COLOR |
| `alert/bold/bg/info` | `color/status/blue/bold/default` | None | None | FRAME_FILL, SHAPE_FILL |
| `alert/bold/text/info` | `color/status/blue/bold/on` | None | None | TEXT_FILL |
| `alert/bold/description/info` | `color/status/blue/bold/on-secondary` | None | None | TEXT_FILL |
| `alert/bold/icon/info` | `color/status/blue/bold/on` | None | None | SHAPE_FILL, STROKE_COLOR |
| `alert/bold/bg/success` | `color/status/green/bold/default` | None | None | FRAME_FILL, SHAPE_FILL |
| `alert/bold/text/success` | `color/status/green/bold/on` | None | None | TEXT_FILL |
| `alert/bold/description/success` | `color/status/green/bold/on-secondary` | None | None | TEXT_FILL |
| `alert/bold/icon/success` | `color/status/green/bold/on` | None | None | SHAPE_FILL, STROKE_COLOR |
| `alert/bold/bg/warning` | `color/status/yellow/bold/default` | None | None | FRAME_FILL, SHAPE_FILL |
| `alert/bold/text/warning` | `color/status/yellow/bold/on` | None | None | TEXT_FILL |
| `alert/bold/description/warning` | `color/status/yellow/bold/on-secondary` | None | None | TEXT_FILL |
| `alert/bold/icon/warning` | `color/status/yellow/bold/on` | None | None | SHAPE_FILL, STROKE_COLOR |
| `alert/bold/bg/error` | `color/status/red/bold/default` | None | None | FRAME_FILL, SHAPE_FILL |
| `alert/bold/text/error` | `color/status/red/bold/on` | None | None | TEXT_FILL |
| `alert/bold/description/error` | `color/status/red/bold/on-secondary` | None | None | TEXT_FILL |
| `alert/bold/icon/error` | `color/status/red/bold/on` | None | None | SHAPE_FILL, STROKE_COLOR |

## Текстовые стили

| Стиль | Шрифт | Переменные |
|---|---|---|
| `typography/alert/m/title` | Roboto SemiBold | `typography/alert/m/title/size`, `typography/alert/m/title/line-height`, `typography/alert/m/title/letter-spacing`, `typography/alert/m/title/weight` |
| `typography/alert/m/description` | Roboto Regular | `typography/alert/m/description/size`, `typography/alert/m/description/line-height`, `typography/alert/m/description/letter-spacing`, `typography/alert/m/description/weight` |
| `typography/alert/s/title` | Roboto SemiBold | `typography/alert/s/title/size`, `typography/alert/s/title/line-height`, `typography/alert/s/title/letter-spacing`, `typography/alert/s/title/weight` |
| `typography/alert/s/description` | Roboto Regular | `typography/alert/s/description/size`, `typography/alert/s/description/line-height`, `typography/alert/s/description/letter-spacing`, `typography/alert/s/description/weight` |

## Контраст

| Передний план | Фон | Режим | Контраст | Норма | |
|---|---|---|---|---|---|
| `alert/text/title` | `alert/bg/info` | light | 14.10 | 4.5 | ✅ |
| `alert/text/title` | `alert/bg/info` | dark | 14.90 | 4.5 | ✅ |
| `alert/text/description` | `alert/bg/info` | light | 14.10 | 4.5 | ✅ |
| `alert/text/description` | `alert/bg/info` | dark | 14.90 | 4.5 | ✅ |
| `alert/icon/info` | `alert/bg/info` | light | 3.37 | 3.0 | ✅ |
| `alert/icon/info` | `alert/bg/info` | dark | 4.64 | 3.0 | ✅ |
| `alert/border/info` | `alert/bg/info` | light | 3.37 | 3.0 | ✅ |
| `alert/border/info` | `alert/bg/info` | dark | 4.64 | 3.0 | ✅ |
| `alert/text/inverse-title` | `alert/bg/inverse-info` | light | 14.90 | 4.5 | ✅ |
| `alert/text/inverse-title` | `alert/bg/inverse-info` | dark | 13.68 | 4.5 | ✅ |
| `alert/text/inverse-description` | `alert/bg/inverse-info` | light | 14.90 | 4.5 | ✅ |
| `alert/text/inverse-description` | `alert/bg/inverse-info` | dark | 13.68 | 4.5 | ✅ |
| `alert/icon/inverse-info` | `alert/bg/inverse-info` | light | 4.64 | 3.0 | ✅ |
| `alert/icon/inverse-info` | `alert/bg/inverse-info` | dark | 3.25 | 3.0 | ✅ |
| `alert/border/inverse-info` | `alert/bg/inverse-info` | light | 4.64 | 3.0 | ✅ |
| `alert/border/inverse-info` | `alert/bg/inverse-info` | dark | 3.25 | 3.0 | ✅ |
| `alert/text/title` | `alert/bg/success` | light | 14.04 | 4.5 | ✅ |
| `alert/text/title` | `alert/bg/success` | dark | 13.99 | 4.5 | ✅ |
| `alert/text/description` | `alert/bg/success` | light | 14.04 | 4.5 | ✅ |
| `alert/text/description` | `alert/bg/success` | dark | 13.99 | 4.5 | ✅ |
| `alert/icon/success` | `alert/bg/success` | light | 5.84 | 3.0 | ✅ |
| `alert/icon/success` | `alert/bg/success` | dark | 8.77 | 3.0 | ✅ |
| `alert/border/success` | `alert/bg/success` | light | 5.84 | 3.0 | ✅ |
| `alert/border/success` | `alert/bg/success` | dark | 8.77 | 3.0 | ✅ |
| `alert/text/inverse-title` | `alert/bg/inverse-success` | light | 13.99 | 4.5 | ✅ |
| `alert/text/inverse-title` | `alert/bg/inverse-success` | dark | 13.70 | 4.5 | ✅ |
| `alert/text/inverse-description` | `alert/bg/inverse-success` | light | 13.99 | 4.5 | ✅ |
| `alert/text/inverse-description` | `alert/bg/inverse-success` | dark | 13.70 | 4.5 | ✅ |
| `alert/icon/inverse-success` | `alert/bg/inverse-success` | light | 8.77 | 3.0 | ✅ |
| `alert/icon/inverse-success` | `alert/bg/inverse-success` | dark | 5.66 | 3.0 | ✅ |
| `alert/border/inverse-success` | `alert/bg/inverse-success` | light | 8.77 | 3.0 | ✅ |
| `alert/border/inverse-success` | `alert/bg/inverse-success` | dark | 5.66 | 3.0 | ✅ |
| `alert/text/title` | `alert/bg/warning` | light | 14.22 | 4.5 | ✅ |
| `alert/text/title` | `alert/bg/warning` | dark | 14.03 | 4.5 | ✅ |
| `alert/text/description` | `alert/bg/warning` | light | 14.22 | 4.5 | ✅ |
| `alert/text/description` | `alert/bg/warning` | dark | 14.03 | 4.5 | ✅ |
| `alert/icon/warning` | `alert/bg/warning` | light | 4.61 | 3.0 | ✅ |
| `alert/icon/warning` | `alert/bg/warning` | dark | 10.14 | 3.0 | ✅ |
| `alert/border/warning` | `alert/bg/warning` | light | 4.61 | 3.0 | ✅ |
| `alert/border/warning` | `alert/bg/warning` | dark | 10.14 | 3.0 | ✅ |
| `alert/text/inverse-title` | `alert/bg/inverse-warning` | light | 14.03 | 4.5 | ✅ |
| `alert/text/inverse-title` | `alert/bg/inverse-warning` | dark | 13.90 | 4.5 | ✅ |
| `alert/text/inverse-description` | `alert/bg/inverse-warning` | light | 14.03 | 4.5 | ✅ |
| `alert/text/inverse-description` | `alert/bg/inverse-warning` | dark | 13.90 | 4.5 | ✅ |
| `alert/icon/inverse-warning` | `alert/bg/inverse-warning` | light | 10.14 | 3.0 | ✅ |
| `alert/icon/inverse-warning` | `alert/bg/inverse-warning` | dark | 4.48 | 3.0 | ✅ |
| `alert/border/inverse-warning` | `alert/bg/inverse-warning` | light | 10.14 | 3.0 | ✅ |
| `alert/border/inverse-warning` | `alert/bg/inverse-warning` | dark | 4.48 | 3.0 | ✅ |
| `alert/text/title` | `alert/bg/error` | light | 13.95 | 4.5 | ✅ |
| `alert/text/title` | `alert/bg/error` | dark | 15.20 | 4.5 | ✅ |
| `alert/text/description` | `alert/bg/error` | light | 13.95 | 4.5 | ✅ |
| `alert/text/description` | `alert/bg/error` | dark | 15.20 | 4.5 | ✅ |
| `alert/icon/error` | `alert/bg/error` | light | 3.67 | 3.0 | ✅ |
| `alert/icon/error` | `alert/bg/error` | dark | 4.12 | 3.0 | ✅ |
| `alert/border/error` | `alert/bg/error` | light | 3.67 | 3.0 | ✅ |
| `alert/border/error` | `alert/bg/error` | dark | 4.12 | 3.0 | ✅ |
| `alert/text/inverse-title` | `alert/bg/inverse-error` | light | 15.20 | 4.5 | ✅ |
| `alert/text/inverse-title` | `alert/bg/inverse-error` | dark | 13.48 | 4.5 | ✅ |
| `alert/text/inverse-description` | `alert/bg/inverse-error` | light | 15.20 | 4.5 | ✅ |
| `alert/text/inverse-description` | `alert/bg/inverse-error` | dark | 13.48 | 4.5 | ✅ |
| `alert/icon/inverse-error` | `alert/bg/inverse-error` | light | 4.12 | 3.0 | ✅ |
| `alert/icon/inverse-error` | `alert/bg/inverse-error` | dark | 3.52 | 3.0 | ✅ |
| `alert/border/inverse-error` | `alert/bg/inverse-error` | light | 4.12 | 3.0 | ✅ |
| `alert/border/inverse-error` | `alert/bg/inverse-error` | dark | 3.52 | 3.0 | ✅ |

## Решения и допущения

- Грамматика: короткая форма неинтерактивного компонента, как у Status — `{c}/{part}/{variant}`; части bg, border, icon, text. Размеры — `{c}/size/{s}/{prop}` → свои L2 `space|gap|size|radius|border/{c}/…`.
- Роли: info · success · warning · error. Документ называет четвёртую роль `danger`; в L3 взято имя `error`, как у Status и Field (`status/*/error`, `field/description/*/error`). В L2 роль идёт в семантику `color/static/*/danger/*`. Роль brand не заводится (документ). Neutral в документе нет — не заводится.
- Соответствие оттенков как у Status: info → blue, success → green, warning → yellow, error → red.
- Фон (regular) — `color/status/{hue}/soft/default`, тот же, что у Status Soft и Badge Soft. Документ предлагал `color/layer/card|page/{role}/subtle` — такого корня в FEroom нет.
- Инверсия — по образцу Field (`field/description/*/inverse-{role}`) и Status (`status/text/inverse`): отдельные L3 с сегментом `inverse-{role}` / `inverse-title`, алиасы на `inverse-*` L2 (`color/static/{text,indicator,border}/…/inverse-firm|inverse-hard`). Документ пишет «Inverse наследует режим фрейма, отдельного варианта нет, inverse-токенов нет» — в FEroom тема приходит через light/dark, а тёмная поверхность внутри светлой темы — через `inverse-*`, поэтому нужна ось Inverse = False/True.
- Фон inverse: у цветных `color/status/{hue}` нет `inverse-soft`, а у `color/bg/*` нет blue/yellow. Взят `color/static/bg/transparent/accent/{hue}/light` (прозрачный тон 10–12 %, одинаков в light/dark) — полупрозрачная заливка корректно ложится и на тёмную, и на светлую инверсную поверхность. Новый цвет в L2 не создавался.
- Иконка роли — `color/static/indicator/{role}/firm`, обводка — `color/static/border/{role}/firm`; там, где firm не даёт 3:1 к фону, взят следующий шаг той же шкалы `hard` (см. список замен ниже). Документ требует обводку ≥ 3:1 (`color/static/border/{role}/default`) — в FEroom шага default нет.
- Заголовок и текст нейтральные (`color/static/text/base/*`), одинаковые для всех ролей — роль несут иконка, фон и обводка (WCAG 1.4.1).
- Вложенные действия — экземпляры Button и Link, кнопка закрытия — экземпляр Button Icon Only (на inverse — тип Inverse-secondary). Их токены не дублируются; ссылки в сводке ошибок — экземпляры Link.
- Типографика: L2 `typography/{c}/{size}/{title|description}/{size|line-height|letter-spacing|weight}` → `font/*`, стили `typography/{c}/{size}/{slot}` без группы action (компонент неинтерактивный, `interactive: false`). Межбуквенный интервал по соглашению FEroom для этих кеглей: 14/20 → 0.1 (`font/letter-spacing/10`), 12/16 → 0.25 (`font/letter-spacing/25`) — как у `typography/content/label/*`, `field/*`. Документ интервал не задаёт. Начертание заголовка 600 → Roboto SemiBold.
- Слоты текста названы `title` и `description` (как Name/Description у Checkbox, Chip, Avatar); документ называет их «Заголовок» и «Текст».
- Эффекты и тени не создаются: Alert/Banner лежат в потоке и тени не требуют.
- codeSyntax не заполняется (решение автора). L3 публикуются (как все L3). Правило скрытия L2 от публикации ещё не выведено (figma-conventions.md) — флаг не задаётся в пресете, решает плагин по правилу аналитика.
- Все L2 размеров ссылаются на существующие примитивы L1, исключений (сырых значений, L3 → L1) нет. `gap/*` → `space/*` L1, как у `gap/status/*`.
- Alert: два размера S и M по документу (размер S в документе — открытый вопрос, числа 12/8 взяты из «Решений для согласования»).
- Alert: скругление S 6 / M 8 → `radius/alert/{s,m}` → `radius/6`, `radius/8`.
- Alert: основной текст — `color/static/text/base/hard` (документ: `text/neutral/primary`). У Banner пояснение — `base/medium` (документ: `neutral/secondary`); расхождение сохранено по документам.
- Alert: промежуток текст ↔ действия S 4 / M 8, контент ↔ закрытие 8 / 8, заголовок ↔ текст 4 / 4 — из таблицы размеров документа.
- Alert: толщина обводки 1 (документ толщину не задаёт) → `border/1`.
- Замена по контрасту: `alert/icon/success`: `color/static/indicator/success/firm` не даёт 3:1 к фону → `color/static/indicator/success/hard`
- Замена по контрасту: `alert/border/success`: `color/static/border/success/firm` не даёт 3:1 к фону → `color/static/border/success/hard`
- Замена по контрасту: `alert/icon/inverse-success`: `color/static/indicator/success/inverse-firm` не даёт 3:1 к фону → `color/static/indicator/success/inverse-hard`
- Замена по контрасту: `alert/border/inverse-success`: `color/static/border/success/inverse-firm` не даёт 3:1 к фону → `color/static/border/success/inverse-hard`
- Замена по контрасту: `alert/icon/warning`: `color/static/indicator/warning/firm` не даёт 3:1 к фону → `color/static/indicator/warning/hard`
- Замена по контрасту: `alert/border/warning`: `color/static/border/warning/firm` не даёт 3:1 к фону → `color/static/border/warning/hard`
- Замена по контрасту: `alert/icon/inverse-warning`: `color/static/indicator/warning/inverse-firm` не даёт 3:1 к фону → `color/static/indicator/warning/inverse-hard`
- Замена по контрасту: `alert/border/inverse-warning`: `color/static/border/warning/inverse-firm` не даёт 3:1 к фону → `color/static/border/warning/inverse-hard`
- Добавлено при проектировании сборки (2026-09-21): `alert/size/{s}/action-gap` → `gap/alert/action/{s}` = 8 — зазор между двумя действиями; в документе не задан, без токена значение было бы захардкожено.
