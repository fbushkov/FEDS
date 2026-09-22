# Соглашения файла-источника (прочитано из Figma 2026-09-21)

Файл: **F · DS · Элементы · Основа стилей**, key `niGA0qBFtb0PXKEIJIBrLe`. В нём переменные, стили и иконки. Компоненты находятся в другом файле — **F · DS · Компоненты · Базовые** (ссылку нужно получить у автора).

По ТЗ токены и стили создаются только здесь, а компоненты собираются в файле компонентов.

## Коллекции

| Коллекция | ID | Переменных | Режимы | Скрыты от публикации |
|---|---|---|---|---|
| 1. Primitives | `VariableCollectionId:303:22` | 643 | Mode 1 | все 643 |
| 2. General | `VariableCollectionId:390:13` | 2261 | light, dark | 1132 (см. ниже) |
| 3. Components | `VariableCollectionId:390:14` | 1987 | Mode 1 | 0 — все опубликованы |

Данные совпадают с `input/tokens/variables.json`.

## codeSyntax

**Ни у одной переменной (0 из 4891) codeSyntax не заполнен.** Решение автора (2026-09-21): **не заполняем**, требование ТЗ F3 про codeSyntax пока не действует.

## Scopes — правило для новых токенов

Правило однозначное: у каждой переменной L2 и L3 ровно один scope (кроме отмеченных случаев).

### L3 `3. Components`, цвет — по сегменту части
| Часть | Scope |
|---|---|
| `bg`, `inverse-bg`, `box`, `box-group`, `knob`, `counter` | `FRAME_FILL` |
| `text`, `inverse-text`, `label`, `name`, `description` | `TEXT_FILL` |
| `icon`, `inverse-icon`, `indicator`, статусные точки (`status/*`) | `SHAPE_FILL` (2 исключения icon → `FRAME_FILL`) |
| `border`, `inverse-border`, `line`, `focus-ring`, `focus`, `spacer` | `STROKE_COLOR` |

### L3, числа — по имени prop
| prop | Scope |
|---|---|
| `x`, `y`, `xy`, `gap`, `*-x`, `*-y`, `*-gap`, `*-x-left/right`, `*-y-top/bottom`, `padding` | `GAP` |
| `radius`, `*-radius`, `radius-circle/square/none`, `focus-radius-*` | `CORNER_RADIUS` |
| `border`, `*-border`, `border-{fill,outline,text,focus}` | `STROKE_FLOAT` |
| `box`, `icon`, `*-box`, `*-icon`, `height`, `width`, `container`, `counter`, `knob`, `dot`, `loader` | `WIDTH_HEIGHT` |

### L2 `2. General` — по корню
| Корень | Scope |
|---|---|
| `color/action/bg`, `color/bg/*`, `color/surface/*`, `color/static/bg` | `FRAME_FILL` |
| `color/action/text`, `color/static/text` | `TEXT_FILL` |
| `color/action/border`, `color/static/border`, `color/static/focus` | `STROKE_COLOR` |
| `color/action/indicator`, `color/static/indicator` | `SHAPE_FILL` |
| `color/static/divider` | `FRAME_FILL, SHAPE_FILL` |
| `color/status/*` | по слоту: `FRAME_FILL` / `ALL_FILLS` / `STROKE_COLOR` |
| `space/*`, `gap/*` | `GAP` |
| `size/*` | `WIDTH_HEIGHT` |
| `radius/*` | `CORNER_RADIUS` |
| `border/*` | `STROKE_FLOAT` |
| `typography/*/size`, `line-height`, `letter-spacing`, `weight` | `FONT_SIZE`, `LINE_HEIGHT`, `LETTER_SPACING`, `FONT_WEIGHT` |
| `effects/*` | `EFFECT_FLOAT` |
| `number` | `ALL_SCOPES` (единственная переменная с этим scope, не трогаем) |

## Публикация (`hiddenFromPublishing`)

- L1 — скрыты все.
- L3 — опубликованы все.
- L2 — смешанно. Скрыты: `color/action/*` (400), `color/status/*` (173), часть `color/static` (75), `typography` 336 из 424, `size` 124 из 234, `radius` 14, `border` 7. Правило «что скрывать в L2» выведет `feds-system-analyst`. Предварительно: семантика, которую используют только через L3, скрыта.

## Текстовые стили (110)

- Имя стиля: `typography/{group}/{component}/{size}/{slot?}`, где group — `action` для интерактивных (button, chip, link, checkbox, radiobutton, switch). У остальных group нет: `typography/avatar/…`, `typography/badge/…`, `typography/field/…`, `typography/status/…`, `typography/divider/…`, общие `typography/page|section|content/…`.
- Каждый стиль привязан к 4 переменным L2: `fontSize`, `lineHeight`, `letterSpacing`, `fontWeight` → `typography/{component}/{size}/{prop}`. Пример: стиль `typography/action/button/m` → `typography/button/m/size`, `/line-height`, `/letter-spacing`, `/weight`.
- Шрифт — Roboto. Начертания: Regular, SemiBold, Bold (именно `SemiBold` без пробела — проверять через `listAvailableFontsAsync`).
- Отклонения в именах (не исправляем): `typography/priority_Indicator/*`, `option_title`.

**Итог:** типографика компонента = L2 `typography/{component}/…` + текстовый стиль, привязанный к этим переменным. L3 для типографики не создаётся.

## Эффект-стили (59)

- Привязаны к переменным только 8: `effect/select/{regular|inverse}/{S|M|L}` и `effect/switch/knob/{M|L}`. Числа идут из L2 `effects/{component}/{prop}/{size}`, **цвет — напрямую из L1** (`color/transparent-black/120`). Это существующее исключение «стиль → L1».
- Остальные 51 (`effect/elevation/*`, `focus/*`, `button/*`, `card/*`, `input/*`, `glow/*`, `backdrop/*`, …) имеют захардкоженные значения, без переменных.
- Размер в имени — заглавными (`S`/`M`/`L`), не как в токенах.

## Paint-стили (21)

Только изображения аватаров (`Avatar/Female/…`, `Avatar/Male/…`) и `↳ Select Image`. Цветовых paint-стилей нет — цвет только через переменные.

## Иконки (страница `Icons`, 727:6)

- 1855 иконок-компонентов 24×24 (набор Lucide), имена kebab-case (`search`, `user-plus`), без группировки через `/`.
- Устройство: `COMPONENT` 24×24 → один `VECTOR` «Union» (20×20, constraints SCALE). Заливка привязана к L2 `color/static/indicator/base/hard`.
- В `description` — ключевые слова для поиска (`filter, find, lookup, magnify, search`).
- В компоненте цвет иконки переопределяется заливкой «Union» → L3 `{component}/…/icon/{state}` (scope `SHAPE_FILL`).
- Служебные наборы: `Cursor` (5 вариантов), `Hint / Default` (2), `_ Scroll` (18: Position × Size × Inverse), рамки-размеры `4х4…48x48`.
- В имени `4х4` — кириллическая «х»: учитывать при поиске.

## Проблемы для отчёта (ничего не исправлено)

1. codeSyntax пуст у всех переменных (расходится с ТЗ).
2. 51 эффект-стиль не привязан к переменным.
3. Эффект-стили select/switch берут цвет из L1, минуя L2.
4. Нарушения kebab-case в именах стилей: `priority_Indicator`, `option_title`, размеры `S/M/L`.
5. `2. General / number` — `ALL_SCOPES`, сырое значение 0.
6. Опечатка `box-uncheked` в L3.
