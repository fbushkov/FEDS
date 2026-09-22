# Токены: Number Input

Пресет: `presets/field-number-input.tokens.json`. Источник: `input/builds/number-input.md`. Аналог: `field/input`.

Статус проверки: **OK** · L2 новых: 6 · L3: 6 · текстовых стилей: 0

## Новые токены L2 (`2. General`)

| Токен | light | dark | scopes |
|---|---|---|---|
| `size/field/number-input/stepper/s` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `size/field/number-input/stepper/m` | `size/28` | `size/28` | WIDTH_HEIGHT |
| `size/field/number-input/stepper/l` | `size/32` | `size/32` | WIDTH_HEIGHT |
| `gap/field/number-input/stepper/s` | `space/2` | `space/2` | GAP |
| `gap/field/number-input/stepper/m` | `space/2` | `space/2` | GAP |
| `gap/field/number-input/stepper/l` | `space/2` | `space/2` | GAP |

## Токены L3 (`3. Components`)

| Токен | → L2 | light | dark | scope |
|---|---|---|---|---|
| `field/size/number-input/s/stepper-box` | `size/field/number-input/stepper/s` | 24 | 24 | WIDTH_HEIGHT |
| `field/size/number-input/m/stepper-box` | `size/field/number-input/stepper/m` | 28 | 28 | WIDTH_HEIGHT |
| `field/size/number-input/l/stepper-box` | `size/field/number-input/stepper/l` | 32 | 32 | WIDTH_HEIGHT |
| `field/size/number-input/s/stepper-gap` | `gap/field/number-input/stepper/s` | 2 | 2 | GAP |
| `field/size/number-input/m/stepper-gap` | `gap/field/number-input/stepper/m` | 2 | 2 | GAP |
| `field/size/number-input/l/stepper-gap` | `gap/field/number-input/stepper/l` | 2 | 2 | GAP |

## Контраст

| Передний план | Фон | Режим | Контраст | Норма | |
|---|---|---|---|---|---|
| `field/input/text/value` | `field/input/bg/default` | light | 15.08 | 4.5 | ✅ |
| `field/input/text/value` | `field/input/bg/default` | dark | 16.48 | 4.5 | ✅ |
| `field/input/text/read-only` | `field/input/bg/read-only` | light | 5.74 | 4.5 | ✅ |
| `field/input/text/read-only` | `field/input/bg/read-only` | dark | 8.66 | 4.5 | ✅ |
| `field/input/text/inverse-value` | `field/input/bg/inverse-default` | light | 16.48 | 4.5 | ✅ |
| `field/input/text/inverse-value` | `field/input/bg/inverse-default` | dark | 15.08 | 4.5 | ✅ |
| `field/input/leading/text` | `field/input/bg/default` | light | 2.44 | 4.5 | ⚠️ |
| `field/input/leading/text` | `field/input/bg/default` | dark | 3.20 | 4.5 | ⚠️ |
| `field/input/text/placeholder` | `field/input/bg/default` | light | 2.44 | 4.5 | ⚠️ |
| `field/input/text/placeholder` | `field/input/bg/default` | dark | 3.20 | 4.5 | ⚠️ |
| `field/input/border/focused` | `field/input/bg/focused` | light | 3.80 | 3.0 | ✅ |
| `field/input/border/focused` | `field/input/bg/focused` | dark | 5.00 | 3.0 | ✅ |
| `field/input/border/error` | `field/input/bg/default` | light | 4.06 | 3.0 | ✅ |
| `field/input/border/error` | `field/input/bg/default` | dark | 4.46 | 3.0 | ✅ |
| `field/input/border/inverse-error` | `field/input/bg/inverse-default` | light | 4.46 | 3.0 | ✅ |
| `field/input/border/inverse-error` | `field/input/bg/inverse-default` | dark | 4.06 | 3.0 | ✅ |
| `field/input/validation-icons/error` | `field/input/bg/default` | light | 4.06 | 3.0 | ✅ |
| `field/input/validation-icons/error` | `field/input/bg/default` | dark | 4.46 | 3.0 | ✅ |

## Решения и допущения

- Number Input — наследник оболочки Input, как Password, Search, Email и Currency (они живут на field/input/* и field/size/input/* без своих копий). Поэтому цвета (фон, обводка, текст, Prefix/Suffix, каретка, State Icon, Spinner), высоты, отступы и типографика (стили typography/field/input/text|prefix|suffix/{s}) берутся из существующих токенов field/input, новых нет. Документ: «Высоты и отступы — как у Input того же размера».
- Новое — только группа кнопок − / + (Stepper): `field/size/number-input/{s}/stepper-box` и `stepper-gap`, по образцу `field/size/text-area/{s}/resizer*` (у Text Area свои токены есть только у уникальной части).
- Рамка − / + = 24 / 28 / 32 (S/M/L): требование документа (≥ 24 × 24, WCAG 2.2 2.5.8) и подписи макета Input для Clear (input.md, решение 5). Существующая `size/field/input/actions/s` = 20 меньше нормы, поэтому своя L2. В S кнопка 24 выше контентной зоны (32 − 2×6 = 20), но центрируется в контейнере фиксированной высоты 32 и не увеличивает поле.
- Кнопки − / + — экземпляры Icon Button (Type = Tertiary, как Clear): своих цветов у них нет, Disabled на границе min/max — состояние самого Icon Button. Clear у Number Input не используется.
- Порядок Trailing Zone: Suffix → − → + → State Icon / Spinner; зазор между элементами зоны — существующий `field/size/input/{s}/gap-trailing`, внутри пары − / + — `stepper-gap` (2).
- Currency: символ валюты — существующие Prefix/Suffix Input (`field/input/leading/text`, `field/size/input/{s}/prefix-*|suffix-*`, стили typography/field/input/prefix|suffix/{s}).
- Выравнивание по правому краю в таблице и табличные цифры (OpenType tnum) — свойства текстового слоя, переменными не задаются; решается при сборке.
- Контраст, accepted: Placeholder и Prefix/Suffix (`color/static/text/base/soft`) ниже 4.5 — существующие токены field/input, не меняем; вопрос к автору для всего семейства.
- Эффекты не нужны. Inverse — токены `inverse-*` field/input (как у Input).
