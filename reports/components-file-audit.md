# Аудит файла «Компоненты · Базовые» (2026-09-21, только чтение)

Файл `gaygUVaeJabe7eDT5rYYm4`, 13 страниц компонентов и `.Technical Components`. Ничего не изменено. Скрипты: `tools/figma/audit-bindings.js`, `tools/figma/scan-page.js`.

## Главный вывод

**Файл компонентов не принял обновления библиотеки.** В нём остались старые имена переменных и стилей. Библиотеку («Элементы · Основа стилей») с тех пор переименовали, а часть переменных удалили. Figma хранит в файле-потребителе имена той версии библиотеки, которая была принята последней. Сверка по ключам (`key`) показала:

- **Переименованные** (ключ тот же, имя в библиотеке новое): привязки работают, но после принятия обновления имена исправятся сами.
- **Удалённые** (ключа больше нет в библиотеке): компоненты держат «осиротевшие» ссылки со значениями из кэша. После обновления библиотеки такие привязки сломаются, значения окажутся без переменной.

Что сделать (решение за автором): открыть файл компонентов → Assets → Libraries → принять обновления «Элементы · Основа стилей». Затем перепривязать удалённые переменные (таблица 2).

## 1. Переименованные в библиотеке (исправятся после принятия обновления)

| Сейчас в файле компонентов | Стало в библиотеке | Где |
|---|---|---|
| `typography/{button,badge,chip,link,divider,radiobutton,switch}/{XL,L,M,S}/…/{letterSpacing,fontSize,lineHeight,fontWeight}` | `typography/{…}/{xl,l,m,s}/…/{letter-spacing,size,line-height,weight}` | текстовые слои Button, Badge, Chip, Link, Divider, Radio, Switch |
| `typography/priority_Indicator/{S,M}/…` | `typography/priority-indicator/{s,m}/…` | Priority Indicator › Name |
| `chip/text/soft/disebled/{base,base-inverse,blue,green,red,yellow,purple}` | `chip/text/soft/disabled/…` | Chip, State=Disabled |
| `button/textBtn/{secondary,tertiary,inverse}/bg/default` | `button/text-button/…/bg/default` | Chip › X-icon, Select › Open-Close, Field › Label › Info, Input › Clear |
| `effects/switch/knob/{spread,x,y,blur}/L` | `effects/switch/knob/…/l` | Switch › Knob (через эффект-стиль) |
| `- color/transparent-black/50` | `color/transparent-black/50` | Switch › Knob (цвет тени, L1) |
| `size/field/label/horizontal/{S,M,L}` | `size/field/label/horizontal/{s,m,l}` | Field / Horizontal › Label (ширина; это **L2 напрямую**, без L3) |
| Текстовые стили `typography/action/button/{XL,L,M,S}` и аналоги у badge, chip, link, divider, radiobutton, switch | `…/{xl,l,m,s}` | все текстовые слои |

## 2. Удалённые из библиотеки (нужна перепривязка)

| Переменная в файле компонентов | Коллекция | Использований | Где |
|---|---|---|---|
| `button/size/text/icon-XL` | 3. Components | 42 | Button / Icon Only › Icon (height) |
| `avatar/size/{XXXL,XL,M,S,XS}/box-group-radius-{circle,square}` (10 переменных) | 3. Components | 2 280 | _ Avatar-Group / * › group (радиусы) |
| `checkbox/size/M/name_container-Y-top` | 3. Components | 48 | Checkbox / Left / M, Right / M › Text (paddingTop) |
| `chip/size/{M,S}/icon_x` | 3. Components | 672 | Chip › X-icon (height) |
| `link/size/{XL,L,M,S}/border` | 3. Components | 384 + 396 в Field | Link / Inline, Standalone (обводка); Field › Label › Link |
| Эффект-стиль `shadow-xs` | — | — | Checkbox / Card, Radio / Card, Switch / Card |

Кандидаты на замену есть в текущей библиотеке: `avatar/size/{s}/box-group-radius-*`, `link/size/{s}/focus-border`, `button/size/{s}/icon`. Точное соответствие утверждает автор.

## 3. Токены чужого компонента (нарушение правила «компонент → свой L3»)

| Компонент › слой | Привязан к | Использований |
|---|---|---|
| Badge › Counter, Status (обводка) | `avatar/size/l/counter-border`, `avatar/size/l/status-border` | 784 |
| Checkbox › Text › Name (обводка) | `badge/size/m/box-border` | 192 |
| Priority Indicator (обводка) | `chip/size/s/box-border`, `badge/size/m/box-border` | 168 |
| Status / * (обводка) | `badge/size/m/box-border` | 1 040 |
| Radio › Error, Avatar Container, Text | `checkbox/size/main/{m,l}/…`, `badge/size/m/box-border` | ~550 |
| Switch › Error, Text | `checkbox/size/main/m/box-icon-{x,y}`, `badge/size/m/box-border` | 384 |
| Avatar / Button-X › Text | `button/size/xl/box` | 6 |

## 4. Несовпадение размера (видно в вариантах по умолчанию, список не полный)

- Checkbox / Left / L › Container, Avatar Container → `checkbox/size/main/m/box-container-xy` (должно быть `l`).
- Select / Button / M → `itemSpacing = field/size/select/s/button/container-gap` (должно быть `m`); Dropdown Items / M → `strokeW = …/s/button/container-border`.
- Field / Vertical, Size=L › Input → `field/size/input/m/radius`, `…/m/border`.

## 5. Захардкоженные значения (без переменных)

| Компонент › слой | Значения | Шт. |
|---|---|---|
| Checkbox / Left, Right (M и L) › Text | itemSpacing 10/12, paddingTop/Bottom 7/8 | 126 |
| Checkbox / * / M › Focus Ring | radius 6 | часть из 126 |
| Radio / * › Text | itemSpacing 10/12, padding 7/8 | 80 |
| Radio / * / M › Radiobutton | strokeWeight 1 | в составе 80 |
| Radio / * / L › Focus Ring | цвет обводки без переменной | в составе 80 |
| Switch / * › Text | itemSpacing 10/12, padding 6–8 | 48 |
| Priority Indicator › Icon, Text | radius 999 | 8 |
| _ Select / Dropdown / S, State=Loading | paddingTop 2 | 1 |
| .Spetification / Blocks (техн.) | отступы, радиусы, текст без стиля | 62 |

## 6. Допустимые исключения (не ошибки)

- `color/static/border/brand/firm` (обводка) и `color/bg/section/main` (фон) на рамке **component set** — это оформление набора на холсте, а не часть компонента.
- `effects/select/*` и L1 `color/transparent-black/*` на Dropdown — приходят из эффект-стиля `effect/select/*` (эффект-стили отложены).
- `typography/*` L2 на текстовых слоях — так устроена система: стиль привязан к L2, L3 для типографики нет.
