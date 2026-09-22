# Токены: Popover

Пресет: `presets/popover.tokens.json`. Источник: `input/backlog/popover.md`. Аналог: `simple-select`.

Статус проверки: **OK** · L2 новых: 23 · L3: 49 · текстовых стилей: 2

## Новые токены L2 (`2. General`)

| Токен | light | dark | scopes |
|---|---|---|---|
| `size/popover/width/s` | `size/240` | `size/240` | WIDTH_HEIGHT |
| `size/popover/width/m` | `320` | `320` | WIDTH_HEIGHT |
| `size/popover/width/l` | `400` | `400` | WIDTH_HEIGHT |
| `space/popover/x` | `space/16` | `space/16` | GAP |
| `space/popover/y` | `space/16` | `space/16` | GAP |
| `space/popover/wrapper` | `space/8` | `space/8` | GAP |
| `space/popover/offset` | `space/4` | `space/4` | GAP |
| `gap/popover/container` | `space/8` | `space/8` | GAP |
| `gap/popover/header` | `space/8` | `space/8` | GAP |
| `gap/popover/footer` | `space/8` | `space/8` | GAP |
| `radius/popover/container` | `radius/8` | `radius/8` | CORNER_RADIUS |
| `border/popover/container` | `border/1` | `border/1` | STROKE_FLOAT |
| `size/popover/close/box` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `size/popover/tail/width` | `size/8` | `size/8` | WIDTH_HEIGHT |
| `size/popover/tail/height` | `size/4` | `size/4` | WIDTH_HEIGHT |
| `typography/popover/title/size` | `font/size/16` | `font/size/16` | FONT_SIZE |
| `typography/popover/title/line-height` | `font/line-height/24` | `font/line-height/24` | LINE_HEIGHT |
| `typography/popover/title/letter-spacing` | `font/letter-spacing/0` | `font/letter-spacing/0` | LETTER_SPACING |
| `typography/popover/title/weight` | `font/weight/600` | `font/weight/600` | FONT_WEIGHT |
| `typography/popover/text/size` | `font/size/14` | `font/size/14` | FONT_SIZE |
| `typography/popover/text/line-height` | `font/line-height/20` | `font/line-height/20` | LINE_HEIGHT |
| `typography/popover/text/letter-spacing` | `font/letter-spacing/10` | `font/letter-spacing/10` | LETTER_SPACING |
| `typography/popover/text/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |

## Токены L3 (`3. Components`)

| Токен | → L2 | light | dark | scope |
|---|---|---|---|---|
| `popover/bg` | `color/bg/raised/main` | rgba(255,255,255,1.00) | rgba(31,31,31,1.00) | FRAME_FILL |
| `popover/inverse-bg` | `color/bg/raised/inverse-main` | rgba(31,31,31,1.00) | rgba(255,255,255,1.00) | FRAME_FILL |
| `popover/border` | `color/static/border/base/light` | rgba(0,0,0,0.10) | rgba(255,255,255,0.10) | STROKE_COLOR |
| `popover/inverse-border` | `color/static/border/base/inverse-light` | rgba(255,255,255,0.10) | rgba(0,0,0,0.10) | STROKE_COLOR |
| `popover/tail` | `color/bg/raised/main` | rgba(255,255,255,1.00) | rgba(31,31,31,1.00) | SHAPE_FILL |
| `popover/inverse-tail` | `color/bg/raised/inverse-main` | rgba(31,31,31,1.00) | rgba(255,255,255,1.00) | SHAPE_FILL |
| `popover/text/title` | `color/static/text/base/hard` | rgba(0,0,0,0.85) | rgba(255,255,255,1.00) | TEXT_FILL |
| `popover/inverse-text/title` | `color/static/text/base/inverse-hard` | rgba(255,255,255,1.00) | rgba(0,0,0,0.85) | TEXT_FILL |
| `popover/text/body` | `color/static/text/base/firm` | rgba(0,0,0,0.75) | rgba(255,255,255,0.90) | TEXT_FILL |
| `popover/inverse-text/body` | `color/static/text/base/inverse-firm` | rgba(255,255,255,0.90) | rgba(0,0,0,0.75) | TEXT_FILL |
| `popover/size/s/width` | `size/popover/width/s` | 240 | 240 | WIDTH_HEIGHT |
| `popover/size/s/x` | `space/popover/x` | 16 | 16 | GAP |
| `popover/size/s/y` | `space/popover/y` | 16 | 16 | GAP |
| `popover/size/s/wrapper-xy` | `space/popover/wrapper` | 8 | 8 | GAP |
| `popover/size/s/gap` | `gap/popover/container` | 8 | 8 | GAP |
| `popover/size/s/header-gap` | `gap/popover/header` | 8 | 8 | GAP |
| `popover/size/s/footer-gap` | `gap/popover/footer` | 8 | 8 | GAP |
| `popover/size/s/radius` | `radius/popover/container` | 8 | 8 | CORNER_RADIUS |
| `popover/size/s/border` | `border/popover/container` | 1 | 1 | STROKE_FLOAT |
| `popover/size/s/close-box` | `size/popover/close/box` | 24 | 24 | WIDTH_HEIGHT |
| `popover/size/s/tail-width` | `size/popover/tail/width` | 8 | 8 | WIDTH_HEIGHT |
| `popover/size/s/tail-height` | `size/popover/tail/height` | 4 | 4 | WIDTH_HEIGHT |
| `popover/size/s/offset` | `space/popover/offset` | 4 | 4 | GAP |
| `popover/size/m/width` | `size/popover/width/m` | 320 | 320 | WIDTH_HEIGHT |
| `popover/size/m/x` | `space/popover/x` | 16 | 16 | GAP |
| `popover/size/m/y` | `space/popover/y` | 16 | 16 | GAP |
| `popover/size/m/wrapper-xy` | `space/popover/wrapper` | 8 | 8 | GAP |
| `popover/size/m/gap` | `gap/popover/container` | 8 | 8 | GAP |
| `popover/size/m/header-gap` | `gap/popover/header` | 8 | 8 | GAP |
| `popover/size/m/footer-gap` | `gap/popover/footer` | 8 | 8 | GAP |
| `popover/size/m/radius` | `radius/popover/container` | 8 | 8 | CORNER_RADIUS |
| `popover/size/m/border` | `border/popover/container` | 1 | 1 | STROKE_FLOAT |
| `popover/size/m/close-box` | `size/popover/close/box` | 24 | 24 | WIDTH_HEIGHT |
| `popover/size/m/tail-width` | `size/popover/tail/width` | 8 | 8 | WIDTH_HEIGHT |
| `popover/size/m/tail-height` | `size/popover/tail/height` | 4 | 4 | WIDTH_HEIGHT |
| `popover/size/m/offset` | `space/popover/offset` | 4 | 4 | GAP |
| `popover/size/l/width` | `size/popover/width/l` | 400 | 400 | WIDTH_HEIGHT |
| `popover/size/l/x` | `space/popover/x` | 16 | 16 | GAP |
| `popover/size/l/y` | `space/popover/y` | 16 | 16 | GAP |
| `popover/size/l/wrapper-xy` | `space/popover/wrapper` | 8 | 8 | GAP |
| `popover/size/l/gap` | `gap/popover/container` | 8 | 8 | GAP |
| `popover/size/l/header-gap` | `gap/popover/header` | 8 | 8 | GAP |
| `popover/size/l/footer-gap` | `gap/popover/footer` | 8 | 8 | GAP |
| `popover/size/l/radius` | `radius/popover/container` | 8 | 8 | CORNER_RADIUS |
| `popover/size/l/border` | `border/popover/container` | 1 | 1 | STROKE_FLOAT |
| `popover/size/l/close-box` | `size/popover/close/box` | 24 | 24 | WIDTH_HEIGHT |
| `popover/size/l/tail-width` | `size/popover/tail/width` | 8 | 8 | WIDTH_HEIGHT |
| `popover/size/l/tail-height` | `size/popover/tail/height` | 4 | 4 | WIDTH_HEIGHT |
| `popover/size/l/offset` | `space/popover/offset` | 4 | 4 | GAP |

## Текстовые стили

| Стиль | Шрифт | Переменные |
|---|---|---|
| `typography/popover/title` | Roboto SemiBold | `typography/popover/title/size`, `typography/popover/title/line-height`, `typography/popover/title/letter-spacing`, `typography/popover/title/weight` |
| `typography/popover/text` | Roboto Regular | `typography/popover/text/size`, `typography/popover/text/line-height`, `typography/popover/text/letter-spacing`, `typography/popover/text/weight` |

## Контраст

| Передний план | Фон | Режим | Контраст | Норма | |
|---|---|---|---|---|---|
| `popover/text/title` | `popover/bg` | light | 15.08 | 4.5 | ✅ |
| `popover/text/title` | `popover/bg` | dark | 16.48 | 4.5 | ✅ |
| `popover/text/body` | `popover/bg` | light | 10.41 | 4.5 | ✅ |
| `popover/text/body` | `popover/bg` | dark | 13.53 | 4.5 | ✅ |
| `popover/inverse-text/title` | `popover/inverse-bg` | light | 16.48 | 4.5 | ✅ |
| `popover/inverse-text/title` | `popover/inverse-bg` | dark | 15.08 | 4.5 | ✅ |
| `popover/inverse-text/body` | `popover/inverse-bg` | light | 13.53 | 4.5 | ✅ |
| `popover/inverse-text/body` | `popover/inverse-bg` | dark | 10.41 | 4.5 | ✅ |
| `popover/border` | `popover/bg` | light | 1.25 | 3.0 | ⚠️ |
| `popover/border` | `popover/bg` | dark | 1.35 | 3.0 | ⚠️ |
| `popover/inverse-border` | `popover/inverse-bg` | light | 1.35 | 3.0 | ⚠️ |
| `popover/inverse-border` | `popover/inverse-bg` | dark | 1.25 | 3.0 | ⚠️ |

## Исключения

- `size/popover/width/m` — в L1 нет size/320; ближайший size/256 ломает шкалу ширин 240 · 320 · 400
- `size/popover/width/l` — в L1 нет size/400; ближайшего примитива нет (максимум шкалы size/* — 256)

## Решения и допущения

- Имена из backlog-документа (`space/overlay/*`, `size/overlay/*`, `radius/{c}` без размера, `typography/body/*`, `typography/heading/*`, `shadow/*`, `color/layer/*`) в FEroom отсутствуют — взяты только значения. Имена построены по грамматике FEroom: корень L3 компонента и собственные L2 `{size|space|gap|radius|border}/{component}/…`, `typography/{component}/…`.
- Инверсия — токенами, а не режимом dark на фрейме (расхождение с документом: «инверсия через dark-режим, inverse-токенов нет»). В FEroom инверсия — сегменты `inverse-*` (CLAUDE.md). Форма — часть `inverse-*` (`inverse-bg`, `inverse-text`, `inverse-border`) как у checkbox/switch и Dropdown у Select (`field/select/dropdown/container/inverse-base`); неинтерактивным оверлеям состояния не нужны, поэтому сегмента state нет. Алиасы — на `inverse-*` L2.
- Поверхность — `color/bg/raised/main` / `inverse-main`: в описании L2 автора `color/bg/raised/*` — «Панель, карточка, popover, tooltip». Dropdown у Select использует `color/static/bg/solid/base/pure` / `inverse-pure`: в light/dark `pure` = `raised/main` (neutral/0 · neutral/900), `inverse-pure` темнее на шаг (neutral/925 против 900).
- Хвостик — отдельная часть с отдельным цветом `tail` (scope SHAPE_FILL, т.к. это вектор) и размерами `tail-width` (основание 8) и `tail-height` (вылет 4). Обводка хвостика — тот же `{c}/border`. Правило «хвостик не ближе к углу, чем длина основания» — поведение, отдельного токена нет (равно `tail-width`).
- Размеры, не зависящие от размера компонента, заведены в L2 без суффикса размера (прецедент: `radius/divider/circle`, `radius/badge/box/circle` на все размеры); в L3 каждый размер получает полный набор `{c}/size/{s}/{prop}`.
- Зазор до триггера (4) заведён как `offset` (GAP): в сборке он нужен только в спецификации и примерах позиционирования.
- Тени не создаём (эффект-стили отложены автором). z-index (`z-index/tooltip` 1700, `z-index/popover` 1500 — есть в L1) и задержки анимации — не переменные сборки Figma, в пресет не входят.
- Размеры L1: 320 и 400 в `1. Primitives` нет (`size/*`: …240, 256 — дальше нет). Ближайший 256 меняет ширину на 20% и ломает шкалу 240 · 320 · 400 — поэтому сырое значение в L2 с записью в exceptions. L1 не трогаем.
- codeSyntax не заполняется (решение автора 2026-09-21). L3 публикуются (как все L3); публикацию новых L2 решает плагин по правилу соседей: размеры и типографика компонентов в основном скрыты.
- Ось Size = ширина панели S 240 · M 320 · L 400 (документ: «не ось размера контрола»). В L3 у каждого размера полный набор, но от ширины зависит только `width`; отступы, gap, радиус и типографика общие (L2 без суффикса размера, типографика `typography/popover/{title|text}/*` без размера).
- Два отступа: `x`/`y` = 16 для панели с заголовком и действиями (открытый вопрос документа закрыт в пользу 16) и `wrapper-xy` = 8 для панели-обёртки, у содержимого которой свои отступы.
- Кнопка закрытия и кнопки футера — экземпляры Button (Icon Only / Filled / Text), ссылка — экземпляр Link; их цвета и размеры не дублируются. Свои токены: зона кнопки закрытия `close-box` = 24 (WCAG 2.5.8), `header-gap` (заголовок ↔ закрытие) и `footer-gap` (между кнопками) = 8 — в документе не заданы, взят вертикальный ритм 8. Для Inverse=True внутри используются Inverse-типы Button.
- Текстовые стили `typography/popover/title` (16/24, SemiBold, LS 0) и `typography/popover/text` (14/20, Regular, LS 0.1) — без группы `action`: сами текстовые слоты неинтерактивны, действия несут собственные стили Button/Link. LS по шкале FEroom: 16 → 0, 14 → 0.1.
- Цвета текста: заголовок `color/static/text/base/hard` (15.1 : 1), текст `firm` (10.4 : 1); инверсные — `inverse-hard` / `inverse-firm`.
- Эффект-стиль понадобится: `effect/popover/{regular|inverse}` — тень 0 · 8 · 16 · −2 (по документу), числа в L2 `effects/popover/{x|y|blur|spread}`. Не создаётся до решения автора. Для Loading/Empty используются экземпляры Spinner/Skeleton — своих токенов нет.
