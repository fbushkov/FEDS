# Токены: Banner

Пресет: `presets/banner.tokens.json`. Источник: `input/backlog/banner.md`. Аналог: `status`.

Статус проверки: **OK** · L2 новых: 18 · L3: 38 · текстовых стилей: 2

## Новые токены L2 (`2. General`)

| Токен | light | dark | scopes |
|---|---|---|---|
| `border/banner/m` | `border/1` | `border/1` | STROKE_FLOAT |
| `gap/banner/actions/m` | `space/8` | `space/8` | GAP |
| `gap/banner/close/m` | `space/8` | `space/8` | GAP |
| `gap/banner/icon/m` | `space/12` | `space/12` | GAP |
| `gap/banner/title/m` | `space/4` | `space/4` | GAP |
| `radius/banner/full-bleed` | `radius/0` | `radius/0` | CORNER_RADIUS |
| `radius/banner/inset` | `radius/12` | `radius/12` | CORNER_RADIUS |
| `size/banner/icon/m` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `space/banner/x/m` | `space/16` | `space/16` | GAP |
| `space/banner/y/m` | `space/16` | `space/16` | GAP |
| `typography/banner/m/description/letter-spacing` | `font/letter-spacing/10` | `font/letter-spacing/10` | LETTER_SPACING |
| `typography/banner/m/description/line-height` | `font/line-height/20` | `font/line-height/20` | LINE_HEIGHT |
| `typography/banner/m/description/size` | `font/size/14` | `font/size/14` | FONT_SIZE |
| `typography/banner/m/description/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |
| `typography/banner/m/title/letter-spacing` | `font/letter-spacing/10` | `font/letter-spacing/10` | LETTER_SPACING |
| `typography/banner/m/title/line-height` | `font/line-height/20` | `font/line-height/20` | LINE_HEIGHT |
| `typography/banner/m/title/size` | `font/size/14` | `font/size/14` | FONT_SIZE |
| `typography/banner/m/title/weight` | `font/weight/600` | `font/weight/600` | FONT_WEIGHT |

## Токены L3 (`3. Components`)

| Токен | → L2 | light | dark | scope |
|---|---|---|---|---|
| `banner/bg/error` | `color/status/red/soft/default` | rgba(240,48,48,0.07) | rgba(240,48,48,0.10) | FRAME_FILL |
| `banner/bg/info` | `color/status/blue/soft/default` | rgba(53,117,221,0.07) | rgba(53,117,221,0.10) | FRAME_FILL |
| `banner/bg/inverse-error` | `color/static/bg/transparent/accent/red/light` | rgba(240,48,48,0.10) | rgba(240,48,48,0.10) | FRAME_FILL |
| `banner/bg/inverse-info` | `color/static/bg/transparent/accent/blue/light` | rgba(53,117,221,0.10) | rgba(53,117,221,0.10) | FRAME_FILL |
| `banner/bg/inverse-success` | `color/static/bg/transparent/accent/green/light` | rgba(69,161,84,0.12) | rgba(69,161,84,0.12) | FRAME_FILL |
| `banner/bg/inverse-warning` | `color/static/bg/transparent/accent/yellow/light` | rgba(172,148,28,0.11) | rgba(172,148,28,0.11) | FRAME_FILL |
| `banner/bg/success` | `color/status/green/soft/default` | rgba(69,161,84,0.09) | rgba(69,161,84,0.12) | FRAME_FILL |
| `banner/bg/warning` | `color/status/yellow/soft/default` | rgba(172,148,28,0.08) | rgba(172,148,28,0.11) | FRAME_FILL |
| `banner/border/error` | `color/static/border/danger/firm` | rgba(240,48,48,1.00) | rgba(242,68,68,1.00) | STROKE_COLOR |
| `banner/border/info` | `color/static/border/info/firm` | rgba(59,130,246,1.00) | rgba(79,142,247,1.00) | STROKE_COLOR |
| `banner/border/inverse-error` | `color/static/border/danger/inverse-firm` | rgba(242,68,68,1.00) | rgba(240,48,48,1.00) | STROKE_COLOR |
| `banner/border/inverse-info` | `color/static/border/info/inverse-firm` | rgba(79,142,247,1.00) | rgba(59,130,246,1.00) | STROKE_COLOR |
| `banner/border/inverse-success` | `color/static/border/success/inverse-hard` | rgba(166,217,174,1.00) | rgba(46,107,56,1.00) | STROKE_COLOR |
| `banner/border/inverse-warning` | `color/static/border/warning/inverse-hard` | rgba(235,220,145,1.00) | rgba(129,111,21,1.00) | STROKE_COLOR |
| `banner/border/success` | `color/static/border/success/hard` | rgba(46,107,56,1.00) | rgba(166,217,174,1.00) | STROKE_COLOR |
| `banner/border/warning` | `color/static/border/warning/hard` | rgba(129,111,21,1.00) | rgba(235,220,145,1.00) | STROKE_COLOR |
| `banner/icon/error` | `color/static/indicator/danger/firm` | rgba(240,48,48,1.00) | rgba(242,68,68,1.00) | SHAPE_FILL |
| `banner/icon/info` | `color/static/indicator/info/firm` | rgba(59,130,246,1.00) | rgba(79,142,247,1.00) | SHAPE_FILL |
| `banner/icon/inverse-error` | `color/static/indicator/danger/inverse-firm` | rgba(242,68,68,1.00) | rgba(240,48,48,1.00) | SHAPE_FILL |
| `banner/icon/inverse-info` | `color/static/indicator/info/inverse-firm` | rgba(79,142,247,1.00) | rgba(59,130,246,1.00) | SHAPE_FILL |
| `banner/icon/inverse-success` | `color/static/indicator/success/inverse-hard` | rgba(166,217,174,1.00) | rgba(46,107,56,1.00) | SHAPE_FILL |
| `banner/icon/inverse-warning` | `color/static/indicator/warning/inverse-hard` | rgba(235,220,145,1.00) | rgba(129,111,21,1.00) | SHAPE_FILL |
| `banner/icon/success` | `color/static/indicator/success/hard` | rgba(46,107,56,1.00) | rgba(166,217,174,1.00) | SHAPE_FILL |
| `banner/icon/warning` | `color/static/indicator/warning/hard` | rgba(129,111,21,1.00) | rgba(235,220,145,1.00) | SHAPE_FILL |
| `banner/size/m/actions-gap` | `gap/banner/actions/m` | 8 | 8 | GAP |
| `banner/size/m/border` | `border/banner/m` | 1 | 1 | STROKE_FLOAT |
| `banner/size/m/close-gap` | `gap/banner/close/m` | 8 | 8 | GAP |
| `banner/size/m/icon` | `size/banner/icon/m` | 20 | 20 | WIDTH_HEIGHT |
| `banner/size/m/icon-gap` | `gap/banner/icon/m` | 12 | 12 | GAP |
| `banner/size/m/radius-full-bleed` | `radius/banner/full-bleed` | 0 | 0 | CORNER_RADIUS |
| `banner/size/m/radius-inset` | `radius/banner/inset` | 12 | 12 | CORNER_RADIUS |
| `banner/size/m/title-gap` | `gap/banner/title/m` | 4 | 4 | GAP |
| `banner/size/m/x` | `space/banner/x/m` | 16 | 16 | GAP |
| `banner/size/m/y` | `space/banner/y/m` | 16 | 16 | GAP |
| `banner/text/description` | `color/static/text/base/medium` | rgba(0,0,0,0.60) | rgba(255,255,255,0.70) | TEXT_FILL |
| `banner/text/inverse-description` | `color/static/text/base/inverse-medium` | rgba(255,255,255,0.70) | rgba(0,0,0,0.60) | TEXT_FILL |
| `banner/text/inverse-title` | `color/static/text/base/inverse-hard` | rgba(255,255,255,1.00) | rgba(0,0,0,0.85) | TEXT_FILL |
| `banner/text/title` | `color/static/text/base/hard` | rgba(0,0,0,0.85) | rgba(255,255,255,1.00) | TEXT_FILL |

## Текстовые стили

| Стиль | Шрифт | Переменные |
|---|---|---|
| `typography/banner/m/title` | Roboto SemiBold | `typography/banner/m/title/size`, `typography/banner/m/title/line-height`, `typography/banner/m/title/letter-spacing`, `typography/banner/m/title/weight` |
| `typography/banner/m/description` | Roboto Regular | `typography/banner/m/description/size`, `typography/banner/m/description/line-height`, `typography/banner/m/description/letter-spacing`, `typography/banner/m/description/weight` |

## Контраст

| Передний план | Фон | Режим | Контраст | Норма | |
|---|---|---|---|---|---|
| `banner/text/title` | `banner/bg/info` | light | 14.10 | 4.5 | ✅ |
| `banner/text/title` | `banner/bg/info` | dark | 14.90 | 4.5 | ✅ |
| `banner/text/description` | `banner/bg/info` | light | 5.59 | 4.5 | ✅ |
| `banner/text/description` | `banner/bg/info` | dark | 8.03 | 4.5 | ✅ |
| `banner/icon/info` | `banner/bg/info` | light | 3.37 | 3.0 | ✅ |
| `banner/icon/info` | `banner/bg/info` | dark | 4.64 | 3.0 | ✅ |
| `banner/border/info` | `banner/bg/info` | light | 3.37 | 3.0 | ✅ |
| `banner/border/info` | `banner/bg/info` | dark | 4.64 | 3.0 | ✅ |
| `banner/text/inverse-title` | `banner/bg/inverse-info` | light | 14.90 | 4.5 | ✅ |
| `banner/text/inverse-title` | `banner/bg/inverse-info` | dark | 13.68 | 4.5 | ✅ |
| `banner/text/inverse-description` | `banner/bg/inverse-info` | light | 8.03 | 4.5 | ✅ |
| `banner/text/inverse-description` | `banner/bg/inverse-info` | dark | 5.53 | 4.5 | ✅ |
| `banner/icon/inverse-info` | `banner/bg/inverse-info` | light | 4.64 | 3.0 | ✅ |
| `banner/icon/inverse-info` | `banner/bg/inverse-info` | dark | 3.25 | 3.0 | ✅ |
| `banner/border/inverse-info` | `banner/bg/inverse-info` | light | 4.64 | 3.0 | ✅ |
| `banner/border/inverse-info` | `banner/bg/inverse-info` | dark | 3.25 | 3.0 | ✅ |
| `banner/text/title` | `banner/bg/success` | light | 14.04 | 4.5 | ✅ |
| `banner/text/title` | `banner/bg/success` | dark | 13.99 | 4.5 | ✅ |
| `banner/text/description` | `banner/bg/success` | light | 5.58 | 4.5 | ✅ |
| `banner/text/description` | `banner/bg/success` | dark | 7.66 | 4.5 | ✅ |
| `banner/icon/success` | `banner/bg/success` | light | 5.84 | 3.0 | ✅ |
| `banner/icon/success` | `banner/bg/success` | dark | 8.77 | 3.0 | ✅ |
| `banner/border/success` | `banner/bg/success` | light | 5.84 | 3.0 | ✅ |
| `banner/border/success` | `banner/bg/success` | dark | 8.77 | 3.0 | ✅ |
| `banner/text/inverse-title` | `banner/bg/inverse-success` | light | 13.99 | 4.5 | ✅ |
| `banner/text/inverse-title` | `banner/bg/inverse-success` | dark | 13.70 | 4.5 | ✅ |
| `banner/text/inverse-description` | `banner/bg/inverse-success` | light | 7.66 | 4.5 | ✅ |
| `banner/text/inverse-description` | `banner/bg/inverse-success` | dark | 5.53 | 4.5 | ✅ |
| `banner/icon/inverse-success` | `banner/bg/inverse-success` | light | 8.77 | 3.0 | ✅ |
| `banner/icon/inverse-success` | `banner/bg/inverse-success` | dark | 5.66 | 3.0 | ✅ |
| `banner/border/inverse-success` | `banner/bg/inverse-success` | light | 8.77 | 3.0 | ✅ |
| `banner/border/inverse-success` | `banner/bg/inverse-success` | dark | 5.66 | 3.0 | ✅ |
| `banner/text/title` | `banner/bg/warning` | light | 14.22 | 4.5 | ✅ |
| `banner/text/title` | `banner/bg/warning` | dark | 14.03 | 4.5 | ✅ |
| `banner/text/description` | `banner/bg/warning` | light | 5.61 | 4.5 | ✅ |
| `banner/text/description` | `banner/bg/warning` | dark | 7.68 | 4.5 | ✅ |
| `banner/icon/warning` | `banner/bg/warning` | light | 4.61 | 3.0 | ✅ |
| `banner/icon/warning` | `banner/bg/warning` | dark | 10.14 | 3.0 | ✅ |
| `banner/border/warning` | `banner/bg/warning` | light | 4.61 | 3.0 | ✅ |
| `banner/border/warning` | `banner/bg/warning` | dark | 10.14 | 3.0 | ✅ |
| `banner/text/inverse-title` | `banner/bg/inverse-warning` | light | 14.03 | 4.5 | ✅ |
| `banner/text/inverse-title` | `banner/bg/inverse-warning` | dark | 13.90 | 4.5 | ✅ |
| `banner/text/inverse-description` | `banner/bg/inverse-warning` | light | 7.68 | 4.5 | ✅ |
| `banner/text/inverse-description` | `banner/bg/inverse-warning` | dark | 5.56 | 4.5 | ✅ |
| `banner/icon/inverse-warning` | `banner/bg/inverse-warning` | light | 10.14 | 3.0 | ✅ |
| `banner/icon/inverse-warning` | `banner/bg/inverse-warning` | dark | 4.48 | 3.0 | ✅ |
| `banner/border/inverse-warning` | `banner/bg/inverse-warning` | light | 10.14 | 3.0 | ✅ |
| `banner/border/inverse-warning` | `banner/bg/inverse-warning` | dark | 4.48 | 3.0 | ✅ |
| `banner/text/title` | `banner/bg/error` | light | 13.95 | 4.5 | ✅ |
| `banner/text/title` | `banner/bg/error` | dark | 15.20 | 4.5 | ✅ |
| `banner/text/description` | `banner/bg/error` | light | 5.57 | 4.5 | ✅ |
| `banner/text/description` | `banner/bg/error` | dark | 8.14 | 4.5 | ✅ |
| `banner/icon/error` | `banner/bg/error` | light | 3.67 | 3.0 | ✅ |
| `banner/icon/error` | `banner/bg/error` | dark | 4.12 | 3.0 | ✅ |
| `banner/border/error` | `banner/bg/error` | light | 3.67 | 3.0 | ✅ |
| `banner/border/error` | `banner/bg/error` | dark | 4.12 | 3.0 | ✅ |
| `banner/text/inverse-title` | `banner/bg/inverse-error` | light | 15.20 | 4.5 | ✅ |
| `banner/text/inverse-title` | `banner/bg/inverse-error` | dark | 13.48 | 4.5 | ✅ |
| `banner/text/inverse-description` | `banner/bg/inverse-error` | light | 8.14 | 4.5 | ✅ |
| `banner/text/inverse-description` | `banner/bg/inverse-error` | dark | 5.50 | 4.5 | ✅ |
| `banner/icon/inverse-error` | `banner/bg/inverse-error` | light | 4.12 | 3.0 | ✅ |
| `banner/icon/inverse-error` | `banner/bg/inverse-error` | dark | 3.52 | 3.0 | ✅ |
| `banner/border/inverse-error` | `banner/bg/inverse-error` | light | 4.12 | 3.0 | ✅ |
| `banner/border/inverse-error` | `banner/bg/inverse-error` | dark | 3.52 | 3.0 | ✅ |

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
- Banner: размер в документе один; в именах он записан как `m` (`banner/size/m/*`, `typography/banner/m/*`), чтобы сохранить грамматику `{c}/size/{s}/{prop}` и совпасть по шагу с Alert M. Ось Size в компонент не выводится.
- Banner: варианты ширины Inset (радиус 12) и Full bleed (радиус 0) → `radius/banner/inset` → `radius/12`, `radius/banner/full-bleed` → `radius/0`; L3 `banner/size/m/radius-inset|radius-full-bleed` (форма как `box-radius-circle|square`). Документ предлагал общий `radius/card` — в FEroom у компонента свои L2.
- Banner Full bleed: обводка только снизу — задаётся сборкой (толщины сторон 0/0/0/`banner/size/m/border`), отдельный токен не нужен.
- Banner: пояснение — `color/static/text/base/medium` (документ: `text/neutral/secondary`), заголовок — `base/hard`.
- Banner: `z-index/banner` = 1200 (закрепление) — свойство кода, не переменная Figma; в пресет не входит.
- Banner: толщина обводки 1 (документ толщину не задаёт) → `border/1`.
- Замена по контрасту: `banner/icon/success`: `color/static/indicator/success/firm` не даёт 3:1 к фону → `color/static/indicator/success/hard`
- Замена по контрасту: `banner/border/success`: `color/static/border/success/firm` не даёт 3:1 к фону → `color/static/border/success/hard`
- Замена по контрасту: `banner/icon/inverse-success`: `color/static/indicator/success/inverse-firm` не даёт 3:1 к фону → `color/static/indicator/success/inverse-hard`
- Замена по контрасту: `banner/border/inverse-success`: `color/static/border/success/inverse-firm` не даёт 3:1 к фону → `color/static/border/success/inverse-hard`
- Замена по контрасту: `banner/icon/warning`: `color/static/indicator/warning/firm` не даёт 3:1 к фону → `color/static/indicator/warning/hard`
- Замена по контрасту: `banner/border/warning`: `color/static/border/warning/firm` не даёт 3:1 к фону → `color/static/border/warning/hard`
- Замена по контрасту: `banner/icon/inverse-warning`: `color/static/indicator/warning/inverse-firm` не даёт 3:1 к фону → `color/static/indicator/warning/inverse-hard`
- Замена по контрасту: `banner/border/inverse-warning`: `color/static/border/warning/inverse-firm` не даёт 3:1 к фону → `color/static/border/warning/inverse-hard`
