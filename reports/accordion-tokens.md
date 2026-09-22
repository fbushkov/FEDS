# Токены: Accordion

Пресет: `presets/accordion.tokens.json`. Источник: `input/backlog/accordion.md`. Аналог: `button`.

Статус проверки: **OK** · L2 новых: 36 · L3: 56 · текстовых стилей: 4

## Новые токены L2 (`2. General`)

| Токен | light | dark | scopes |
|---|---|---|---|
| `space/accordion/header/x/s` | `space/12` | `space/12` | GAP |
| `space/accordion/header/y/s` | `space/12` | `space/12` | GAP |
| `gap/accordion/header/s` | `space/8` | `space/8` | GAP |
| `size/accordion/icon/s` | `size/16` | `size/16` | WIDTH_HEIGHT |
| `space/accordion/panel/x/s` | `space/12` | `space/12` | GAP |
| `space/accordion/panel/y/s-bottom` | `space/12` | `space/12` | GAP |
| `gap/accordion/cards/s` | `space/8` | `space/8` | GAP |
| `border/accordion/focus/s` | `border/2` | `border/2` | STROKE_FLOAT |
| `radius/accordion/focus/s` | `radius/4` | `radius/4` | CORNER_RADIUS |
| `space/accordion/header/x/m` | `space/16` | `space/16` | GAP |
| `space/accordion/header/y/m` | `space/16` | `space/16` | GAP |
| `gap/accordion/header/m` | `space/12` | `space/12` | GAP |
| `size/accordion/icon/m` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `space/accordion/panel/x/m` | `space/16` | `space/16` | GAP |
| `space/accordion/panel/y/m-bottom` | `space/16` | `space/16` | GAP |
| `gap/accordion/cards/m` | `space/8` | `space/8` | GAP |
| `border/accordion/focus/m` | `border/2` | `border/2` | STROKE_FLOAT |
| `radius/accordion/focus/m` | `radius/4` | `radius/4` | CORNER_RADIUS |
| `radius/accordion/container` | `radius/12` | `radius/12` | CORNER_RADIUS |
| `border/accordion/container` | `border/1` | `border/1` | STROKE_FLOAT |
| `typography/accordion/s/title/size` | `font/size/14` | `font/size/14` | FONT_SIZE |
| `typography/accordion/s/title/line-height` | `font/line-height/20` | `font/line-height/20` | LINE_HEIGHT |
| `typography/accordion/s/title/letter-spacing` | `font/letter-spacing/0` | `font/letter-spacing/0` | LETTER_SPACING |
| `typography/accordion/s/title/weight` | `font/weight/600` | `font/weight/600` | FONT_WEIGHT |
| `typography/accordion/s/panel/size` | `font/size/14` | `font/size/14` | FONT_SIZE |
| `typography/accordion/s/panel/line-height` | `font/line-height/20` | `font/line-height/20` | LINE_HEIGHT |
| `typography/accordion/s/panel/letter-spacing` | `font/letter-spacing/0` | `font/letter-spacing/0` | LETTER_SPACING |
| `typography/accordion/s/panel/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |
| `typography/accordion/m/title/size` | `font/size/16` | `font/size/16` | FONT_SIZE |
| `typography/accordion/m/title/line-height` | `font/line-height/24` | `font/line-height/24` | LINE_HEIGHT |
| `typography/accordion/m/title/letter-spacing` | `font/letter-spacing/0` | `font/letter-spacing/0` | LETTER_SPACING |
| `typography/accordion/m/title/weight` | `font/weight/600` | `font/weight/600` | FONT_WEIGHT |
| `typography/accordion/m/panel/size` | `font/size/16` | `font/size/16` | FONT_SIZE |
| `typography/accordion/m/panel/line-height` | `font/line-height/24` | `font/line-height/24` | LINE_HEIGHT |
| `typography/accordion/m/panel/letter-spacing` | `font/letter-spacing/0` | `font/letter-spacing/0` | LETTER_SPACING |
| `typography/accordion/m/panel/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |

## Токены L3 (`3. Components`)

| Токен | → L2 | light | dark | scope |
|---|---|---|---|---|
| `accordion/header/bg/default` | `color/action/bg/base/ghost/default` | rgba(0,0,0,0.00) | rgba(255,255,255,0.00) | FRAME_FILL |
| `accordion/header/bg/hover` | `color/action/bg/base/ghost/hover` | rgba(0,0,0,0.03) | rgba(255,255,255,0.03) | FRAME_FILL |
| `accordion/header/bg/pressed` | `color/action/bg/base/ghost/pressed` | rgba(0,0,0,0.07) | rgba(255,255,255,0.07) | FRAME_FILL |
| `accordion/header/bg/disabled` | `color/action/bg/base/ghost/disabled` | rgba(0,0,0,0.00) | rgba(255,255,255,0.00) | FRAME_FILL |
| `accordion/header/text/default` | `color/action/text/base/hard/default` | rgba(0,0,0,0.85) | rgba(255,255,255,1.00) | TEXT_FILL |
| `accordion/header/text/hover` | `color/action/text/base/hard/default` | rgba(0,0,0,0.85) | rgba(255,255,255,1.00) | TEXT_FILL |
| `accordion/header/text/pressed` | `color/action/text/base/hard/default` | rgba(0,0,0,0.85) | rgba(255,255,255,1.00) | TEXT_FILL |
| `accordion/header/text/disabled` | `color/action/text/base/hard/disabled` | rgba(0,0,0,0.35) | rgba(255,255,255,0.35) | TEXT_FILL |
| `accordion/header/icon/default` | `color/action/indicator/base/medium/default` | rgba(0,0,0,0.60) | rgba(255,255,255,0.70) | SHAPE_FILL |
| `accordion/header/icon/hover` | `color/action/indicator/base/medium/hover` | rgba(0,0,0,0.85) | rgba(255,255,255,0.90) | SHAPE_FILL |
| `accordion/header/icon/pressed` | `color/action/indicator/base/medium/pressed` | rgba(0,0,0,0.85) | rgba(255,255,255,0.90) | SHAPE_FILL |
| `accordion/header/icon/disabled` | `color/action/indicator/base/medium/disabled` | rgba(0,0,0,0.30) | rgba(255,255,255,0.30) | SHAPE_FILL |
| `accordion/header/inverse-bg/default` | `color/action/bg/base/inverse-ghost/default` | rgba(255,255,255,0.00) | rgba(0,0,0,0.00) | FRAME_FILL |
| `accordion/header/inverse-bg/hover` | `color/action/bg/base/inverse-ghost/hover` | rgba(255,255,255,0.03) | rgba(0,0,0,0.03) | FRAME_FILL |
| `accordion/header/inverse-bg/pressed` | `color/action/bg/base/inverse-ghost/pressed` | rgba(255,255,255,0.07) | rgba(0,0,0,0.07) | FRAME_FILL |
| `accordion/header/inverse-bg/disabled` | `color/action/bg/base/inverse-ghost/disabled` | rgba(255,255,255,0.00) | rgba(0,0,0,0.00) | FRAME_FILL |
| `accordion/header/inverse-text/default` | `color/action/text/base/inverse-hard/default` | rgba(255,255,255,1.00) | rgba(0,0,0,0.85) | TEXT_FILL |
| `accordion/header/inverse-text/hover` | `color/action/text/base/inverse-hard/default` | rgba(255,255,255,1.00) | rgba(0,0,0,0.85) | TEXT_FILL |
| `accordion/header/inverse-text/pressed` | `color/action/text/base/inverse-hard/default` | rgba(255,255,255,1.00) | rgba(0,0,0,0.85) | TEXT_FILL |
| `accordion/header/inverse-text/disabled` | `color/action/text/base/inverse-hard/disabled` | rgba(255,255,255,0.35) | rgba(0,0,0,0.35) | TEXT_FILL |
| `accordion/header/inverse-icon/default` | `color/action/indicator/base/inverse-medium/default` | rgba(255,255,255,0.70) | rgba(0,0,0,0.60) | SHAPE_FILL |
| `accordion/header/inverse-icon/hover` | `color/action/indicator/base/inverse-medium/hover` | rgba(255,255,255,0.90) | rgba(0,0,0,0.85) | SHAPE_FILL |
| `accordion/header/inverse-icon/pressed` | `color/action/indicator/base/inverse-medium/pressed` | rgba(255,255,255,0.90) | rgba(0,0,0,0.85) | SHAPE_FILL |
| `accordion/header/inverse-icon/disabled` | `color/action/indicator/base/inverse-medium/disabled` | rgba(255,255,255,0.30) | rgba(0,0,0,0.30) | SHAPE_FILL |
| `accordion/panel/text` | `color/static/text/base/hard` | rgba(0,0,0,0.85) | rgba(255,255,255,1.00) | TEXT_FILL |
| `accordion/panel/inverse-text` | `color/static/text/base/inverse-hard` | rgba(255,255,255,1.00) | rgba(0,0,0,0.85) | TEXT_FILL |
| `accordion/boxed/border` | `color/static/border/base/light` | rgba(0,0,0,0.10) | rgba(255,255,255,0.10) | STROKE_COLOR |
| `accordion/boxed/inverse-border` | `color/static/border/base/inverse-light` | rgba(255,255,255,0.10) | rgba(0,0,0,0.10) | STROKE_COLOR |
| `accordion/cards/bg` | `color/static/bg/transparent/base/weak` | rgba(0,0,0,0.03) | rgba(255,255,255,0.03) | FRAME_FILL |
| `accordion/cards/border` | `color/static/border/base/light` | rgba(0,0,0,0.10) | rgba(255,255,255,0.10) | STROKE_COLOR |
| `accordion/cards/inverse-bg` | `color/static/bg/transparent/base/inverse-weak` | rgba(255,255,255,0.03) | rgba(0,0,0,0.03) | FRAME_FILL |
| `accordion/cards/inverse-border` | `color/static/border/base/inverse-light` | rgba(255,255,255,0.10) | rgba(0,0,0,0.10) | STROKE_COLOR |
| `accordion/focus-ring` | `color/static/focus/brand` | rgba(39,129,243,1.00) | rgba(61,142,244,1.00) | STROKE_COLOR |
| `accordion/inverse-focus-ring` | `color/static/focus/inverse-brand` | rgba(61,142,244,1.00) | rgba(39,129,243,1.00) | STROKE_COLOR |
| `accordion/size/s/x` | `space/accordion/header/x/s` | 12 | 12 | GAP |
| `accordion/size/s/y` | `space/accordion/header/y/s` | 12 | 12 | GAP |
| `accordion/size/s/gap` | `gap/accordion/header/s` | 8 | 8 | GAP |
| `accordion/size/s/icon` | `size/accordion/icon/s` | 16 | 16 | WIDTH_HEIGHT |
| `accordion/size/s/panel-x` | `space/accordion/panel/x/s` | 12 | 12 | GAP |
| `accordion/size/s/panel-y-bottom` | `space/accordion/panel/y/s-bottom` | 12 | 12 | GAP |
| `accordion/size/s/cards-gap` | `gap/accordion/cards/s` | 8 | 8 | GAP |
| `accordion/size/s/container-radius` | `radius/accordion/container` | 12 | 12 | CORNER_RADIUS |
| `accordion/size/s/container-border` | `border/accordion/container` | 1 | 1 | STROKE_FLOAT |
| `accordion/size/s/focus-border` | `border/accordion/focus/s` | 2 | 2 | STROKE_FLOAT |
| `accordion/size/s/focus-radius` | `radius/accordion/focus/s` | 4 | 4 | CORNER_RADIUS |
| `accordion/size/m/x` | `space/accordion/header/x/m` | 16 | 16 | GAP |
| `accordion/size/m/y` | `space/accordion/header/y/m` | 16 | 16 | GAP |
| `accordion/size/m/gap` | `gap/accordion/header/m` | 12 | 12 | GAP |
| `accordion/size/m/icon` | `size/accordion/icon/m` | 20 | 20 | WIDTH_HEIGHT |
| `accordion/size/m/panel-x` | `space/accordion/panel/x/m` | 16 | 16 | GAP |
| `accordion/size/m/panel-y-bottom` | `space/accordion/panel/y/m-bottom` | 16 | 16 | GAP |
| `accordion/size/m/cards-gap` | `gap/accordion/cards/m` | 8 | 8 | GAP |
| `accordion/size/m/container-radius` | `radius/accordion/container` | 12 | 12 | CORNER_RADIUS |
| `accordion/size/m/container-border` | `border/accordion/container` | 1 | 1 | STROKE_FLOAT |
| `accordion/size/m/focus-border` | `border/accordion/focus/m` | 2 | 2 | STROKE_FLOAT |
| `accordion/size/m/focus-radius` | `radius/accordion/focus/m` | 4 | 4 | CORNER_RADIUS |

## Текстовые стили

| Стиль | Шрифт | Переменные |
|---|---|---|
| `typography/action/accordion/s/title` | Roboto SemiBold | `typography/accordion/s/title/size`, `typography/accordion/s/title/line-height`, `typography/accordion/s/title/letter-spacing`, `typography/accordion/s/title/weight` |
| `typography/action/accordion/s/panel` | Roboto Regular | `typography/accordion/s/panel/size`, `typography/accordion/s/panel/line-height`, `typography/accordion/s/panel/letter-spacing`, `typography/accordion/s/panel/weight` |
| `typography/action/accordion/m/title` | Roboto SemiBold | `typography/accordion/m/title/size`, `typography/accordion/m/title/line-height`, `typography/accordion/m/title/letter-spacing`, `typography/accordion/m/title/weight` |
| `typography/action/accordion/m/panel` | Roboto Regular | `typography/accordion/m/panel/size`, `typography/accordion/m/panel/line-height`, `typography/accordion/m/panel/letter-spacing`, `typography/accordion/m/panel/weight` |

## Контраст

| Передний план | Фон | Режим | Контраст | Норма | |
|---|---|---|---|---|---|
| `accordion/header/text/default` | `accordion/header/bg/default` | light | 15.08 | 4.5 | ✅ |
| `accordion/header/text/default` | `accordion/header/bg/default` | dark | 16.48 | 4.5 | ✅ |
| `accordion/header/icon/default` | `accordion/header/bg/default` | light | 5.74 | 3.0 | ✅ |
| `accordion/header/icon/default` | `accordion/header/bg/default` | dark | 8.66 | 3.0 | ✅ |
| `accordion/header/inverse-text/default` | `accordion/header/inverse-bg/default` | light | 16.48 | 4.5 | ✅ |
| `accordion/header/inverse-text/default` | `accordion/header/inverse-bg/default` | dark | 15.08 | 4.5 | ✅ |
| `accordion/header/inverse-icon/default` | `accordion/header/inverse-bg/default` | light | 8.66 | 3.0 | ✅ |
| `accordion/header/inverse-icon/default` | `accordion/header/inverse-bg/default` | dark | 5.74 | 3.0 | ✅ |
| `accordion/header/text/hover` | `accordion/header/bg/hover` | light | 14.33 | 4.5 | ✅ |
| `accordion/header/text/hover` | `accordion/header/bg/hover` | dark | 15.19 | 4.5 | ✅ |
| `accordion/header/icon/hover` | `accordion/header/bg/hover` | light | 14.33 | 3.0 | ✅ |
| `accordion/header/icon/hover` | `accordion/header/bg/hover` | dark | 12.54 | 3.0 | ✅ |
| `accordion/header/inverse-text/hover` | `accordion/header/inverse-bg/hover` | light | 15.19 | 4.5 | ✅ |
| `accordion/header/inverse-text/hover` | `accordion/header/inverse-bg/hover` | dark | 14.33 | 4.5 | ✅ |
| `accordion/header/inverse-icon/hover` | `accordion/header/inverse-bg/hover` | light | 12.54 | 3.0 | ✅ |
| `accordion/header/inverse-icon/hover` | `accordion/header/inverse-bg/hover` | dark | 14.33 | 3.0 | ✅ |
| `accordion/header/text/pressed` | `accordion/header/bg/pressed` | light | 13.35 | 4.5 | ✅ |
| `accordion/header/text/pressed` | `accordion/header/bg/pressed` | dark | 13.45 | 4.5 | ✅ |
| `accordion/header/icon/pressed` | `accordion/header/bg/pressed` | light | 13.35 | 3.0 | ✅ |
| `accordion/header/icon/pressed` | `accordion/header/bg/pressed` | dark | 11.20 | 3.0 | ✅ |
| `accordion/header/inverse-text/pressed` | `accordion/header/inverse-bg/pressed` | light | 13.45 | 4.5 | ✅ |
| `accordion/header/inverse-text/pressed` | `accordion/header/inverse-bg/pressed` | dark | 13.35 | 4.5 | ✅ |
| `accordion/header/inverse-icon/pressed` | `accordion/header/inverse-bg/pressed` | light | 11.20 | 3.0 | ✅ |
| `accordion/header/inverse-icon/pressed` | `accordion/header/inverse-bg/pressed` | dark | 13.35 | 3.0 | ✅ |
| `accordion/header/text/disabled` | `accordion/header/bg/disabled` | light | 2.44 | 4.5 | ⚠️ |
| `accordion/header/text/disabled` | `accordion/header/bg/disabled` | dark | 3.20 | 4.5 | ⚠️ |
| `accordion/header/icon/disabled` | `accordion/header/bg/disabled` | light | 2.11 | 3.0 | ⚠️ |
| `accordion/header/icon/disabled` | `accordion/header/bg/disabled` | dark | 2.71 | 3.0 | ⚠️ |
| `accordion/header/inverse-text/disabled` | `accordion/header/inverse-bg/disabled` | light | 3.20 | 4.5 | ⚠️ |
| `accordion/header/inverse-text/disabled` | `accordion/header/inverse-bg/disabled` | dark | 2.44 | 4.5 | ⚠️ |
| `accordion/header/inverse-icon/disabled` | `accordion/header/inverse-bg/disabled` | light | 2.71 | 3.0 | ⚠️ |
| `accordion/header/inverse-icon/disabled` | `accordion/header/inverse-bg/disabled` | dark | 2.11 | 3.0 | ⚠️ |
| `accordion/panel/text` | `accordion/cards/bg` | light | 14.33 | 4.5 | ✅ |
| `accordion/panel/text` | `accordion/cards/bg` | dark | 15.19 | 4.5 | ✅ |
| `accordion/header/text/default` | `accordion/cards/bg` | light | 14.33 | 4.5 | ✅ |
| `accordion/header/text/default` | `accordion/cards/bg` | dark | 15.19 | 4.5 | ✅ |
| `accordion/header/icon/default` | `accordion/cards/bg` | light | 5.63 | 3.0 | ✅ |
| `accordion/header/icon/default` | `accordion/cards/bg` | dark | 8.16 | 3.0 | ✅ |
| `accordion/panel/inverse-text` | `accordion/cards/inverse-bg` | light | 15.19 | 4.5 | ✅ |
| `accordion/panel/inverse-text` | `accordion/cards/inverse-bg` | dark | 14.33 | 4.5 | ✅ |
| `accordion/header/inverse-text/default` | `accordion/cards/inverse-bg` | light | 15.19 | 4.5 | ✅ |
| `accordion/header/inverse-text/default` | `accordion/cards/inverse-bg` | dark | 14.33 | 4.5 | ✅ |
| `accordion/boxed/border` | `color/bg/page/main` | light | 1.25 | 3.0 | ⚠️ |
| `accordion/boxed/border` | `color/bg/page/main` | dark | 1.35 | 3.0 | ⚠️ |
| `accordion/cards/border` | `accordion/cards/bg` | light | 1.25 | 3.0 | ⚠️ |
| `accordion/cards/border` | `accordion/cards/bg` | dark | 1.37 | 3.0 | ⚠️ |
| `accordion/boxed/inverse-border` | `color/bg/page/inverse-main` | light | 1.35 | 3.0 | ⚠️ |
| `accordion/boxed/inverse-border` | `color/bg/page/inverse-main` | dark | 1.25 | 3.0 | ⚠️ |
| `accordion/focus-ring` | `color/bg/page/main` | light | 3.80 | 3.0 | ✅ |
| `accordion/focus-ring` | `color/bg/page/main` | dark | 5.00 | 3.0 | ✅ |
| `accordion/inverse-focus-ring` | `color/bg/page/inverse-main` | light | 5.00 | 3.0 | ✅ |
| `accordion/inverse-focus-ring` | `color/bg/page/inverse-main` | dark | 3.80 | 3.0 | ✅ |

## Решения и допущения

- Аналог — button (Button / Fill / Ghost): строка заголовка — кнопка без фона, поэтому фон состояний `color/action/bg/base/ghost/*`, название `color/action/text/base/hard/*` (на hover/pressed текст не меняется, меняется фон — как у button/fill/ghost), стрелка `color/action/indicator/base/medium/*` (вторичная, как link/secondary/icon). Имена документа `color/action/bg/neutral/ghost/*`, `color/static/text/neutral/primary`, `color/static/icon/neutral/secondary`, `color/static/focus-ring/brand/default` в FEroom не существуют — заменены ближайшей семантикой FEroom.
- Порядок сегментов L3: `accordion/{part}/{state}` для строки заголовка (`accordion/header/{bg|text|icon}/{state}`), короткая форма `accordion/{view}/{part}` для неинтерактивных частей (`accordion/boxed/border`, `accordion/cards/bg`), фокус — `accordion/focus-ring` (как button, link, switch).
- Инверсия: документ её не описывает, но в FEroom у компонентов, которые ставятся на тёмные поверхности (switch, checkbox, field/select), есть ось Inverse. Форма — часть `inverse-*` (как switch: `switch/off/inverse-bg/*`, `switch/card/inverse-border`), алиасы на `inverse-*` L2 (`inverse-ghost`, `inverse-hard`, `inverse-medium`, `color/static/focus/inverse-brand` — как field/select/inverse-focus-ring).
- Разделитель между секциями — экземпляр Divider (Horizontal, Thickness XS, Color Regular: divider/line/regular → color/static/border/base/light, 1 px). Свои токены линии не заводятся. Рамка Boxed и обводка Cards взяты с той же семантикой (`color/static/border/base/light`), чтобы рамка и линии совпадали по тону.
- Два размера S и M по документу. Числа документа: отступы строки 12·16, промежуток название↔стрелка 8·12, стрелка 16·20, скругление карточки 12, промежуток между карточками 8, линия 1. Имена `space/card/padding*`, `space/inline/default`, `space/control/gap/m`, `radius/card`, `space/stack/default`, `border/width/divider`, `size/icon/{m,l}` в FEroom не существуют — заведены свои L2 компонента по грамматике (`space/accordion/header/{x|y}/{s|m}`, `gap/accordion/header/{s|m}`, `size/accordion/icon/{s|m}`, `radius/accordion/container`, `gap/accordion/cards/{s|m}`, `border/accordion/container`).
- Отступы панели документ не задаёт: принято, что горизонтальный отступ и нижний отступ панели равны отступам строки заголовка (12·16), верхний — 0 (панель продолжает строку заголовка). Если стрелка стоит слева, выравнивание текста панели по названию — правило сборки (отступ = x + icon + gap), отдельного токена нет.
- Высота строки заголовка не фиксируется (документ): токена `box` нет, высота = интерлиньяж + 2·y (S: 20+24 = 44, M: 24+32 = 56), минимальная зона нажатия 24 × 24 выполняется.
- Кольцо фокуса: документ задаёт только цвет. Толщина 2 (как у крупных контролов: border/button/focus-bold, border/badge/focus/m), скругление 4 — кольцо рисуется внутри строки заголовка (слой Focus Ring, absolute, FILL×FILL). Для Cards/Boxed скругление углов кольца у первой и последней секции — открытый вопрос.
- Типографика: `typography/accordion/{s|m}/{title|panel}/*` — название 14/20 и 16/24, 600 (SemiBold), текст панели 14/20 и 16/24, 400; трекинг 0, как у button и link. Имена документа `typography/heading/{group,subsection}`, `typography/body/{ui,reading}` в FEroom отсутствуют. Текстовые стили — `typography/action/accordion/{s|m}/{title|panel}` (группа action: заголовок — интерактивный элемент; все стили компонента в одной группе, как у chip). L3 для типографики не создаётся.
- Подсветка раскрытой секции (`…/ghost/selected`) не заведена: документ называет её необязательной, состояние передаёт стрелка. При необходимости — `accordion/header/bg/expanded` → `color/action/bg/base/ghost/selected`.
- Анимация раскрытия (200 мс, поворот стрелки) и тени не создаются: motion-токенов в FEroom нет, эффект-стили автор не прорабатывал. Для Cards эффект-стиль не нужен (фон + обводка).
- Badge и Status в строке заголовка — экземпляры своих компонентов, их токены не дублируются.
