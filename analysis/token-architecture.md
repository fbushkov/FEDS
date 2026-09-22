# Архитектура токенов FEroom (разбор `input/tokens/variables.json`)

Первичный разбор, сделанный при создании проекта. Сырые данные — `analysis/token-report.md` и `analysis/token-index.json` (`python tools/analyze_tokens.py`). Агент `feds-system-analyst` дополняет этот файл после изучения документации и сборок.

## Сводка

| Коллекция | Режимы | Переменных | На что ссылается |
|---|---|---|---|
| `1. Primitives` | `Mode 1` | 643 (color 337, number 302, fontWeight 4) | сырые значения |
| `2. General` | `light`, `dark` | 2261 (number 1206, color 949, fontWeight 106) | 4520 ссылок, все → L1 |
| `3. Components` | `Mode 1` | 1987 (color 1059, number 928) | 1987 ссылок, все → L2 |

- Битых алиасов: **0**. Ссылок через уровень или вверх: **0**.
- Единственное значение без алиаса выше L1: `2. General / number` = 0 (служебная переменная, выяснить назначение).
- Тема (light/dark) живёт **только в L2**: 690 переменных L2 отличаются по режимам. L3 одномодовый и наследует тему через алиас.
- Описания: L2 — 653 из 2261, L3 — 38 из 1987. Новые токены должны получать описание.
- В экспорте **нет** scopes и codeSyntax — их плагин читает из Figma напрямую (F1). До этого соглашения по scopes/codeSyntax неизвестны.

## L1 — Primitives

- `color/{hue}/{step}` — hue: `neutral, brand, blue, green, purple, red, yellow`; шаг 0…1000 (~31 шаг).
- `color/transparent-{hue}/{step}` — прозрачные варианты (`black`, `white`, `brand`, `blue`, …).
- Числовые шкалы: `size/{n}`, `space/{n}`, `space/negative/-{n}`, `radius/{n}` (+ `999`), `border/{n}`, `blur/{n}`, `opacity/{n}`, `elevation/{n}`, `z-index/{name}`, `motion/duration/{ms}`.
- Типографика: `font/size/*`, `font/line-height/*`, `font/letter-spacing/*` (есть отрицательные), `font/weight/*`.
- Тени: `shadow/{blur|offset-x|offset-y|spread}/*`.

## L2 — General

### Цвет (семантика, light/dark)

| Корень | Формула | Значения сегментов |
|---|---|---|
| `color/action` | `color/action/{part}/{role}/{emphasis}/{state}` | part: `bg, border, indicator, text`; role: `base, brand, danger, info, success, warning`; emphasis: `calm, controls, firm, ghost, hard, light, medium, pure, quiet, soft…` + пары `inverse-*`; state: `default, hover, pressed, selected, disabled, read-only, visited, inverse-selected, brand` |
| `color/static` | `color/static/{part}/{role}/{tone}`, `color/static/bg/{solid\|transparent}/{hue}/{emphasis}`, `color/static/bg/transparent/accent/{hue}/{emphasis}`, `color/static/{divider\|focus}/{tone}` | неинтерактивные цвета: текст, иконки, обводки, фоны, разделители, фокус |
| `color/status` | `color/status/{hue}/{emphasis}/{slot}` | hue: `base, blue, brand, green, purple, red, yellow`; slot: `default, hover, active, on, on-brand, on-secondary, border, border-*` |
| `color/surface` | `color/surface/{base\|brand}/{emphasis?}/{state}` | state: `default, hover, pressed, selected, disabled` |
| `color/bg` | `color/bg/{page\|section\|raised\|overlay}/{tone}` | фоны страниц и слоёв, есть `inverse-*` |

### Размеры и типографика компонентов (в L2!)

Формулы — корень, затем имя компонента:

- `size/{component}/{size}` или `size/{component}/{part}/{size}` — например `size/button/m`, `size/badge/icon/m`.
- `space/{component}/{x|y}/{size}` — например `space/button/x/m`.
- `gap/{component}/{size}` и `gap/{component}/{part}/{size}`.
- `radius/{component}/{size}`, `radius/{component}/focus/{size}`.
- `border/{component}/{kind}` — например `border/button/outline`, `border/button/focus-bold`.
- `typography/{component}/{size}/{letter-spacing|line-height|size|weight}`.
- `effects/{component}/{part?}/{blur|spread|x|y}/{size}` — пока только `select`, `switch`.
- Общая типографика: `typography/{page|section|content}/…`.

**Важно:** L3 ссылается только на `color`, `size`, `space`, `gap`, `radius`, `border` из L2. `typography/*` и `effects/*` L2 в L3 не проксируются — они привязываются к текстовым/эффект-стилям и слоям напрямую. Подтвердить на сборках.

## L3 — Components

Готовых компонентов 13 (страницы Figma-файла «F · DS · Компоненты · Базовые»), корней L3 — 12:

| Страница Figma | Корень L3 | Токенов |
|---|---|---|
| Avatar | `avatar` | 207 |
| Badge | `badge` | 121 |
| Button | `button` | 333 |
| Checkbox | `checkbox` | 110 |
| Chip | `chip` | 213 |
| Divider | `divider` | 44 |
| Link | `link` | 60 |
| Priority Indicator | `priority-indicator` | 66 |
| Radiobutton | `radiobutton` | 106 |
| Status | `status` | 91 |
| Switch | `switch` | 122 |
| Input, Text Area, Field | `field/{input,label,description,counter}`, `field/size/{input,text-area,label,description,field}` | 296 |
| SimpleSelect | `field/select/*`, `field/size/select/*` | 218 |

Вывод: семейство полей ввода делит один корень `field`, а подкомпоненты различаются вторым сегментом. Новые компоненты этого семейства (например, Multiselect, Combobox, Datepicker) нужно добавлять как `field/{subcomponent}/…` и `field/size/{subcomponent}/…`, а не заводить новый корень.

### Цвет

`{component}/{variant…}/{part}/{state}`:

- `button/{fill|outline|text-button}/{primary|primary-soft|secondary|tertiary|ghost|danger|danger-soft|inverse}/{bg|border|text|icon}/{default|hover|pressed|disabled}`
  - пример: `button/fill/primary/bg/hover` → `color/action/bg/brand/medium/hover`.
- `chip/{bg|border|text}/{hard|soft}/{color}/{state}`.
- `checkbox|radiobutton|switch/{checked|unchecked|on|off}/{part}/{state}` — инверсия внутри сегмента части: `inverse-bg`, `inverse-border`, `inverse-icon`.
- Короткая форма для неинтерактивных: `{component}/{part}/{variant}` — `priority-indicator/bg/critical`, `divider/line/strong`.
- Служебные: `{component}/focus-ring` (или `focus`, `border/focus`), `loading/*`, `text/*`.

### Размеры

`{component}/size/{size}/{prop}`, с подразделом при нескольких частях: `{component}/size/{part}/{size}/{prop}`.

- `button/size/m/x` → `space/button/x/m`.
- `switch/size/card/l/box-x`, `field/size/input/m/…`.
- Словарь `prop`: `box`, `x`, `y`, `gap`, `radius`, `border`, `icon`, `focus-border`, `focus-radius`, `box-radius-circle|square`, `box-icon-x|y`, `counter-*`, `*-gap`.

### Инверсия

Не режимы, а отдельные токены: в L2 — emphasis/tone `inverse-*`, в L3 — вариант `inverse` (`button/fill/inverse/…`), сегмент `*-inverse` (`badge/border/base-inverse`) или часть `inverse-*` (`switch/on/inverse-bg/default`). Для нового компонента выбирается форма, которая используется у ближайшего по типу существующего компонента.

### Известные особенности, которые нельзя «чинить» без запроса

- Опечатка `box-uncheked` (4 переменные у checkbox/radiobutton).
- Порядок сегментов у разных компонентов разный (`chip/bg/hard/…` против `button/fill/primary/bg/…`) — новые компоненты берут порядок у ближайшего аналога.
- Формы фокуса разные: `focus-ring`, `focus`, `border/focus`.

## Открытые вопросы (закрыть после изучения `input/`)

1. ~~Какой компонент 13-й~~ — SimpleSelect, токены внутри `field/select`.
2. ~~Scopes и codeSyntax~~ — прочитаны из Figma: один scope на переменную, codeSyntax пуст везде. См. `analysis/figma-conventions.md`.
3. ~~Стили~~ — 110 текстовых (привязаны к L2 `typography/*`), 59 эффект-стилей (8 привязаны к `effects/*`, остальные захардкожены). См. `analysis/figma-conventions.md`.
4. Назначение `2. General / number` — отложено автором, не трогаем.
5. Правило выбора формы инверсии и формы фокуса для новых компонентов.
