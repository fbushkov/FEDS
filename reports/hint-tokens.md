# Токены: Hint

Пресет: `presets/hint.tokens.json`. Источник: `input/backlog/hint.md`. Аналог: `simple-select`.

Статус проверки: **OK** · L2 новых: 29 · L3: 48 · текстовых стилей: 3

## Новые токены L2 (`2. General`)

| Токен | light | dark | scopes |
|---|---|---|---|
| `size/hint/width/s` | `size/240` | `size/240` | WIDTH_HEIGHT |
| `size/hint/width/m` | `320` | `320` | WIDTH_HEIGHT |
| `space/hint/x` | `space/16` | `space/16` | GAP |
| `space/hint/y` | `space/16` | `space/16` | GAP |
| `space/hint/offset` | `space/4` | `space/4` | GAP |
| `gap/hint/container` | `space/16` | `space/16` | GAP |
| `gap/hint/content` | `space/4` | `space/4` | GAP |
| `gap/hint/header` | `space/8` | `space/8` | GAP |
| `gap/hint/footer` | `space/8` | `space/8` | GAP |
| `gap/hint/indicator` | `space/4` | `space/4` | GAP |
| `radius/hint/container` | `radius/8` | `radius/8` | CORNER_RADIUS |
| `radius/hint/media` | `radius/4` | `radius/4` | CORNER_RADIUS |
| `border/hint/container` | `border/1` | `border/1` | STROKE_FLOAT |
| `size/hint/close/box` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `size/hint/indicator/dot` | `size/6` | `size/6` | WIDTH_HEIGHT |
| `size/hint/tail/width` | `size/8` | `size/8` | WIDTH_HEIGHT |
| `size/hint/tail/height` | `size/4` | `size/4` | WIDTH_HEIGHT |
| `typography/hint/title/size` | `font/size/16` | `font/size/16` | FONT_SIZE |
| `typography/hint/title/line-height` | `font/line-height/24` | `font/line-height/24` | LINE_HEIGHT |
| `typography/hint/title/letter-spacing` | `font/letter-spacing/0` | `font/letter-spacing/0` | LETTER_SPACING |
| `typography/hint/title/weight` | `font/weight/600` | `font/weight/600` | FONT_WEIGHT |
| `typography/hint/text/size` | `font/size/14` | `font/size/14` | FONT_SIZE |
| `typography/hint/text/line-height` | `font/line-height/20` | `font/line-height/20` | LINE_HEIGHT |
| `typography/hint/text/letter-spacing` | `font/letter-spacing/10` | `font/letter-spacing/10` | LETTER_SPACING |
| `typography/hint/text/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |
| `typography/hint/counter/size` | `font/size/12` | `font/size/12` | FONT_SIZE |
| `typography/hint/counter/line-height` | `font/line-height/16` | `font/line-height/16` | LINE_HEIGHT |
| `typography/hint/counter/letter-spacing` | `font/letter-spacing/25` | `font/letter-spacing/25` | LETTER_SPACING |
| `typography/hint/counter/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |

## Токены L3 (`3. Components`)

| Токен | → L2 | light | dark | scope |
|---|---|---|---|---|
| `hint/bg` | `color/bg/raised/main` | rgba(255,255,255,1.00) | rgba(31,31,31,1.00) | FRAME_FILL |
| `hint/inverse-bg` | `color/bg/raised/inverse-main` | rgba(31,31,31,1.00) | rgba(255,255,255,1.00) | FRAME_FILL |
| `hint/border` | `color/static/border/base/light` | rgba(0,0,0,0.10) | rgba(255,255,255,0.10) | STROKE_COLOR |
| `hint/inverse-border` | `color/static/border/base/inverse-light` | rgba(255,255,255,0.10) | rgba(0,0,0,0.10) | STROKE_COLOR |
| `hint/tail` | `color/bg/raised/main` | rgba(255,255,255,1.00) | rgba(31,31,31,1.00) | SHAPE_FILL |
| `hint/inverse-tail` | `color/bg/raised/inverse-main` | rgba(31,31,31,1.00) | rgba(255,255,255,1.00) | SHAPE_FILL |
| `hint/text/title` | `color/static/text/base/hard` | rgba(0,0,0,0.85) | rgba(255,255,255,1.00) | TEXT_FILL |
| `hint/inverse-text/title` | `color/static/text/base/inverse-hard` | rgba(255,255,255,1.00) | rgba(0,0,0,0.85) | TEXT_FILL |
| `hint/text/body` | `color/static/text/base/firm` | rgba(0,0,0,0.75) | rgba(255,255,255,0.90) | TEXT_FILL |
| `hint/inverse-text/body` | `color/static/text/base/inverse-firm` | rgba(255,255,255,0.90) | rgba(0,0,0,0.75) | TEXT_FILL |
| `hint/text/counter` | `color/static/text/base/medium` | rgba(0,0,0,0.60) | rgba(255,255,255,0.70) | TEXT_FILL |
| `hint/inverse-text/counter` | `color/static/text/base/inverse-medium` | rgba(255,255,255,0.70) | rgba(0,0,0,0.60) | TEXT_FILL |
| `hint/indicator/active` | `color/static/indicator/brand/firm` | rgba(39,129,243,1.00) | rgba(61,142,244,1.00) | SHAPE_FILL |
| `hint/indicator/default` | `color/static/indicator/base/light` | rgba(0,0,0,0.45) | rgba(255,255,255,0.50) | SHAPE_FILL |
| `hint/inverse-indicator/active` | `color/static/indicator/brand/inverse-firm` | rgba(61,142,244,1.00) | rgba(39,129,243,1.00) | SHAPE_FILL |
| `hint/inverse-indicator/default` | `color/static/indicator/base/inverse-light` | rgba(255,255,255,0.45) | rgba(0,0,0,0.45) | SHAPE_FILL |
| `hint/size/s/width` | `size/hint/width/s` | 240 | 240 | WIDTH_HEIGHT |
| `hint/size/s/x` | `space/hint/x` | 16 | 16 | GAP |
| `hint/size/s/y` | `space/hint/y` | 16 | 16 | GAP |
| `hint/size/s/gap` | `gap/hint/container` | 16 | 16 | GAP |
| `hint/size/s/content-gap` | `gap/hint/content` | 4 | 4 | GAP |
| `hint/size/s/header-gap` | `gap/hint/header` | 8 | 8 | GAP |
| `hint/size/s/footer-gap` | `gap/hint/footer` | 8 | 8 | GAP |
| `hint/size/s/indicator-gap` | `gap/hint/indicator` | 4 | 4 | GAP |
| `hint/size/s/indicator` | `size/hint/indicator/dot` | 6 | 6 | WIDTH_HEIGHT |
| `hint/size/s/radius` | `radius/hint/container` | 8 | 8 | CORNER_RADIUS |
| `hint/size/s/media-radius` | `radius/hint/media` | 4 | 4 | CORNER_RADIUS |
| `hint/size/s/border` | `border/hint/container` | 1 | 1 | STROKE_FLOAT |
| `hint/size/s/close-box` | `size/hint/close/box` | 24 | 24 | WIDTH_HEIGHT |
| `hint/size/s/tail-width` | `size/hint/tail/width` | 8 | 8 | WIDTH_HEIGHT |
| `hint/size/s/tail-height` | `size/hint/tail/height` | 4 | 4 | WIDTH_HEIGHT |
| `hint/size/s/offset` | `space/hint/offset` | 4 | 4 | GAP |
| `hint/size/m/width` | `size/hint/width/m` | 320 | 320 | WIDTH_HEIGHT |
| `hint/size/m/x` | `space/hint/x` | 16 | 16 | GAP |
| `hint/size/m/y` | `space/hint/y` | 16 | 16 | GAP |
| `hint/size/m/gap` | `gap/hint/container` | 16 | 16 | GAP |
| `hint/size/m/content-gap` | `gap/hint/content` | 4 | 4 | GAP |
| `hint/size/m/header-gap` | `gap/hint/header` | 8 | 8 | GAP |
| `hint/size/m/footer-gap` | `gap/hint/footer` | 8 | 8 | GAP |
| `hint/size/m/indicator-gap` | `gap/hint/indicator` | 4 | 4 | GAP |
| `hint/size/m/indicator` | `size/hint/indicator/dot` | 6 | 6 | WIDTH_HEIGHT |
| `hint/size/m/radius` | `radius/hint/container` | 8 | 8 | CORNER_RADIUS |
| `hint/size/m/media-radius` | `radius/hint/media` | 4 | 4 | CORNER_RADIUS |
| `hint/size/m/border` | `border/hint/container` | 1 | 1 | STROKE_FLOAT |
| `hint/size/m/close-box` | `size/hint/close/box` | 24 | 24 | WIDTH_HEIGHT |
| `hint/size/m/tail-width` | `size/hint/tail/width` | 8 | 8 | WIDTH_HEIGHT |
| `hint/size/m/tail-height` | `size/hint/tail/height` | 4 | 4 | WIDTH_HEIGHT |
| `hint/size/m/offset` | `space/hint/offset` | 4 | 4 | GAP |

## Текстовые стили

| Стиль | Шрифт | Переменные |
|---|---|---|
| `typography/hint/title` | Roboto SemiBold | `typography/hint/title/size`, `typography/hint/title/line-height`, `typography/hint/title/letter-spacing`, `typography/hint/title/weight` |
| `typography/hint/text` | Roboto Regular | `typography/hint/text/size`, `typography/hint/text/line-height`, `typography/hint/text/letter-spacing`, `typography/hint/text/weight` |
| `typography/hint/counter` | Roboto Regular | `typography/hint/counter/size`, `typography/hint/counter/line-height`, `typography/hint/counter/letter-spacing`, `typography/hint/counter/weight` |

## Контраст

| Передний план | Фон | Режим | Контраст | Норма | |
|---|---|---|---|---|---|
| `hint/text/title` | `hint/bg` | light | 15.08 | 4.5 | ✅ |
| `hint/text/title` | `hint/bg` | dark | 16.48 | 4.5 | ✅ |
| `hint/text/body` | `hint/bg` | light | 10.41 | 4.5 | ✅ |
| `hint/text/body` | `hint/bg` | dark | 13.53 | 4.5 | ✅ |
| `hint/text/counter` | `hint/bg` | light | 5.74 | 4.5 | ✅ |
| `hint/text/counter` | `hint/bg` | dark | 8.66 | 4.5 | ✅ |
| `hint/indicator/active` | `hint/bg` | light | 3.80 | 3.0 | ✅ |
| `hint/indicator/active` | `hint/bg` | dark | 5.00 | 3.0 | ✅ |
| `hint/indicator/default` | `hint/bg` | light | 3.35 | 3.0 | ✅ |
| `hint/indicator/default` | `hint/bg` | dark | 5.10 | 3.0 | ✅ |
| `hint/inverse-text/title` | `hint/inverse-bg` | light | 16.48 | 4.5 | ✅ |
| `hint/inverse-text/title` | `hint/inverse-bg` | dark | 15.08 | 4.5 | ✅ |
| `hint/inverse-text/body` | `hint/inverse-bg` | light | 13.53 | 4.5 | ✅ |
| `hint/inverse-text/body` | `hint/inverse-bg` | dark | 10.41 | 4.5 | ✅ |
| `hint/inverse-text/counter` | `hint/inverse-bg` | light | 8.66 | 4.5 | ✅ |
| `hint/inverse-text/counter` | `hint/inverse-bg` | dark | 5.74 | 4.5 | ✅ |
| `hint/inverse-indicator/active` | `hint/inverse-bg` | light | 5.00 | 3.0 | ✅ |
| `hint/inverse-indicator/active` | `hint/inverse-bg` | dark | 3.80 | 3.0 | ✅ |
| `hint/inverse-indicator/default` | `hint/inverse-bg` | light | 4.40 | 3.0 | ✅ |
| `hint/inverse-indicator/default` | `hint/inverse-bg` | dark | 3.35 | 3.0 | ✅ |
| `hint/border` | `hint/bg` | light | 1.25 | 3.0 | ⚠️ |
| `hint/border` | `hint/bg` | dark | 1.35 | 3.0 | ⚠️ |
| `hint/inverse-border` | `hint/inverse-bg` | light | 1.35 | 3.0 | ⚠️ |
| `hint/inverse-border` | `hint/inverse-bg` | dark | 1.25 | 3.0 | ⚠️ |

## Исключения

- `size/hint/width/m` — в L1 нет size/320; ближайший size/256 расходится с шириной M у Popover и максимальной шириной Tooltip

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
- Ось Size = ширина панели S 240 · M 320 (L не предлагается документом). Как у Popover, от размера зависит только `width`.
- Раскладка: контейнер (отступ 16, gap 16) → [медиа] → текстовый блок (заголовок + закрытие в строке `header-gap` 8; заголовок ↔ текст `content-gap` 4) → футер (счётчик или точки + кнопки, `footer-gap` 8). Значения 4 и 16 — из документа (`space/stack/tight`, `space/stack/loose`); `header-gap`, `footer-gap`, `indicator-gap` = 4 и `media-radius` = 4 документом не заданы — предложены.
- Кнопки «Далее» / «Назад» / «Пропустить» / «Готово» и закрытие — экземпляры Button (Filled / Outline / Text / Icon Only) и Link; свои токены только у зоны закрытия `close-box` = 24.
- Текстовые стили `typography/hint/{title|text|counter}` без группы `action` — по аналогии с Popover: текстовые слоты неинтерактивны, действия несут стили Button/Link. Отдельный стиль для счётчика заведён, т.к. в FEroom стиль привязан к L2 компонента, а `typography/helper/default` из документа не существует.
- Счётчик — `color/static/text/base/medium` (5.7 / 8.7 : 1), по документу «secondary, не tertiary». Точки: текущая `color/static/indicator/brand/firm` (3.8 / 5.0 : 1), остальные `color/static/indicator/base/light` (3.35 / 5.1 : 1); диаметр 6 (значение `size/indicator/dot` из документа — в FEroom такого L2 нет).
- Роль у Hint нейтральная — та же поверхность `color/bg/raised/*`, что у Popover (документ: «обучение нейтрально»).
- Не входят в компонент (слои сценария тура): подсветка якоря (spotlight), затемнение (scrim — есть `color/bg/overlay/*`), маячок (beacon — отдельный компонент). Их токены не создаются.
- Эффект-стиль понадобится: `effect/hint/{regular|inverse}` — тень 0 · 8 · 16 · −2, как у Popover (можно переиспользовать `effect/popover/*`). Не создаётся до решения автора. z-index 1500/1400 и `motion/duration/*` — не переменные сборки.
