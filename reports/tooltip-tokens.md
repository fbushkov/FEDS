# Токены: Tooltip

Пресет: `presets/tooltip.tokens.json`. Источник: `input/backlog/tooltip.md`. Аналог: `simple-select`.

Статус проверки: **OK** · L2 новых: 12 · L3: 16 · текстовых стилей: 1

## Новые токены L2 (`2. General`)

| Токен | light | dark | scopes |
|---|---|---|---|
| `space/tooltip/x` | `space/8` | `space/8` | GAP |
| `space/tooltip/y` | `space/4` | `space/4` | GAP |
| `space/tooltip/offset` | `space/4` | `space/4` | GAP |
| `radius/tooltip/container` | `radius/6` | `radius/6` | CORNER_RADIUS |
| `border/tooltip/container` | `border/1` | `border/1` | STROKE_FLOAT |
| `size/tooltip/max-width` | `320` | `320` | WIDTH_HEIGHT |
| `size/tooltip/tail/width` | `size/8` | `size/8` | WIDTH_HEIGHT |
| `size/tooltip/tail/height` | `size/4` | `size/4` | WIDTH_HEIGHT |
| `typography/tooltip/text/size` | `font/size/12` | `font/size/12` | FONT_SIZE |
| `typography/tooltip/text/line-height` | `font/line-height/16` | `font/line-height/16` | LINE_HEIGHT |
| `typography/tooltip/text/letter-spacing` | `font/letter-spacing/25` | `font/letter-spacing/25` | LETTER_SPACING |
| `typography/tooltip/text/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |

## Токены L3 (`3. Components`)

| Токен | → L2 | light | dark | scope |
|---|---|---|---|---|
| `tooltip/bg` | `color/bg/raised/main` | rgba(255,255,255,1.00) | rgba(31,31,31,1.00) | FRAME_FILL |
| `tooltip/inverse-bg` | `color/bg/raised/inverse-main` | rgba(31,31,31,1.00) | rgba(255,255,255,1.00) | FRAME_FILL |
| `tooltip/border` | `color/static/border/base/light` | rgba(0,0,0,0.10) | rgba(255,255,255,0.10) | STROKE_COLOR |
| `tooltip/inverse-border` | `color/static/border/base/inverse-light` | rgba(255,255,255,0.10) | rgba(0,0,0,0.10) | STROKE_COLOR |
| `tooltip/tail` | `color/bg/raised/main` | rgba(255,255,255,1.00) | rgba(31,31,31,1.00) | SHAPE_FILL |
| `tooltip/inverse-tail` | `color/bg/raised/inverse-main` | rgba(31,31,31,1.00) | rgba(255,255,255,1.00) | SHAPE_FILL |
| `tooltip/text` | `color/static/text/base/hard` | rgba(0,0,0,0.85) | rgba(255,255,255,1.00) | TEXT_FILL |
| `tooltip/inverse-text` | `color/static/text/base/inverse-hard` | rgba(255,255,255,1.00) | rgba(0,0,0,0.85) | TEXT_FILL |
| `tooltip/size/m/x` | `space/tooltip/x` | 8 | 8 | GAP |
| `tooltip/size/m/y` | `space/tooltip/y` | 4 | 4 | GAP |
| `tooltip/size/m/offset` | `space/tooltip/offset` | 4 | 4 | GAP |
| `tooltip/size/m/radius` | `radius/tooltip/container` | 6 | 6 | CORNER_RADIUS |
| `tooltip/size/m/border` | `border/tooltip/container` | 1 | 1 | STROKE_FLOAT |
| `tooltip/size/m/max-width` | `size/tooltip/max-width` | 320 | 320 | WIDTH_HEIGHT |
| `tooltip/size/m/tail-width` | `size/tooltip/tail/width` | 8 | 8 | WIDTH_HEIGHT |
| `tooltip/size/m/tail-height` | `size/tooltip/tail/height` | 4 | 4 | WIDTH_HEIGHT |

## Текстовые стили

| Стиль | Шрифт | Переменные |
|---|---|---|
| `typography/tooltip/text` | Roboto Regular | `typography/tooltip/text/size`, `typography/tooltip/text/line-height`, `typography/tooltip/text/letter-spacing`, `typography/tooltip/text/weight` |

## Контраст

| Передний план | Фон | Режим | Контраст | Норма | |
|---|---|---|---|---|---|
| `tooltip/text` | `tooltip/bg` | light | 15.08 | 4.5 | ✅ |
| `tooltip/text` | `tooltip/bg` | dark | 16.48 | 4.5 | ✅ |
| `tooltip/inverse-text` | `tooltip/inverse-bg` | light | 16.48 | 4.5 | ✅ |
| `tooltip/inverse-text` | `tooltip/inverse-bg` | dark | 15.08 | 4.5 | ✅ |
| `tooltip/border` | `tooltip/bg` | light | 1.25 | 3.0 | ⚠️ |
| `tooltip/border` | `tooltip/bg` | dark | 1.35 | 3.0 | ⚠️ |
| `tooltip/inverse-border` | `tooltip/inverse-bg` | light | 1.35 | 3.0 | ⚠️ |
| `tooltip/inverse-border` | `tooltip/inverse-bg` | dark | 1.25 | 3.0 | ⚠️ |

## Исключения

- `size/tooltip/max-width` — в L1 нет size/320; ближайший size/256 меняет максимальную ширину на 20% и расходится с шириной M у Popover/Hint (320)

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
- Оси размера нет (один тултип на все триггеры). Чтобы сохранить грамматику `{c}/size/{s}/{prop}`, единственный размер назван `m`; ось Size в компоненте не выводится. Типографика — без размера: `typography/tooltip/text/*`.
- Регулярный тултип — светлая поверхность `color/bg/raised/main` (в описании L2 автора tooltip указан у `raised/main`, но не у `raised/inverse-main`; документ тоже описывает тултип в цвете режима). Inverse=True — `raised/inverse-main` для тёмных поверхностей. Если нужен классический тёмный тултип на светлом интерфейсе — поменять алиасы `bg/tail` ↔ `inverse-bg/inverse-tail` и `text` ↔ `inverse-text` (см. открытые вопросы).
- Обводка 1 px добавлена, хотя в документе у Tooltip её нет: светлая поверхность `raised/main` совпадает с `bg/page/main` (контраст 1.00 в обоих режимах), а в dark тень почти не видна. Сборщик может скрыть обводку, токены остаются.
- Текст — 12/16, 400, LS 0.25 (значения `typography/body/small`): в FEroom 12-кегль всегда идёт с `font/letter-spacing/25` (ср. `typography/content/label/caption`). Стиль `typography/tooltip/text` без группы `action` — тултип неинтерактивен.
- Цвет текста — `color/static/text/base/hard` / `inverse-hard` (15.1 / 16.5 : 1).
- Эффект-стиль понадобится: `effect/tooltip/{regular|inverse}` — тень 0 · 2 · 8 · 0 (по документу), числа в L2 `effects/tooltip/{x|y|blur|spread}` по образцу `effects/select/*`. Не создаётся до решения автора.
- Задержки открытия/закрытия (300 / 100 мс) и z-index 1700 — поведение для кода, не переменные сборки.
