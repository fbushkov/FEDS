# Токены: Dropdown — часть Select, Combobox, Multiselect

Пресет: `presets/field-dropdown.tokens.json`. Источник: `input/backlog/dropdown.md`. Аналог: `field/select`.

Статус проверки: **OK** · L2 новых: 45 · L3: 25 · текстовых стилей: 6

## Новые токены L2 (`2. General`)

| Токен | light | dark | scopes |
|---|---|---|---|
| `border/field/select/option/focus/s` | `border/1` | `border/1` | STROKE_FLOAT |
| `radius/field/select/option/focus/s` | `radius/6` | `radius/6` | CORNER_RADIUS |
| `gap/field/select/option/text/s` | `space/0` | `space/0` | GAP |
| `size/field/select/option/checkbox/s` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `space/field/select/option/checkbox/s` | `space/0` | `space/0` | GAP |
| `gap/field/select/dropdown/loader/s` | `space/4` | `space/4` | GAP |
| `border/field/select/option/focus/m` | `border/2` | `border/2` | STROKE_FLOAT |
| `radius/field/select/option/focus/m` | `radius/8` | `radius/8` | CORNER_RADIUS |
| `gap/field/select/option/text/m` | `space/0` | `space/0` | GAP |
| `size/field/select/option/checkbox/m` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `space/field/select/option/checkbox/m` | `space/0` | `space/0` | GAP |
| `gap/field/select/dropdown/loader/m` | `space/6` | `space/6` | GAP |
| `border/field/select/option/focus/l` | `border/2` | `border/2` | STROKE_FLOAT |
| `radius/field/select/option/focus/l` | `radius/10` | `radius/10` | CORNER_RADIUS |
| `gap/field/select/option/text/l` | `space/0` | `space/0` | GAP |
| `size/field/select/option/checkbox/l` | `size/28` | `size/28` | WIDTH_HEIGHT |
| `space/field/select/option/checkbox/l` | `space/2` | `space/2` | GAP |
| `gap/field/select/dropdown/loader/l` | `space/8` | `space/8` | GAP |
| `typography/field/select/option-description/s/size` | `font/size/12` | `font/size/12` | FONT_SIZE |
| `typography/field/select/option-description/s/line-height` | `font/line-height/16` | `font/line-height/16` | LINE_HEIGHT |
| `typography/field/select/option-description/s/letter-spacing` | `font/letter-spacing/25` | `font/letter-spacing/25` | LETTER_SPACING |
| `typography/field/select/option-description/s/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |
| `typography/field/select/option-description/m/size` | `font/size/14` | `font/size/14` | FONT_SIZE |
| `typography/field/select/option-description/m/line-height` | `font/line-height/20` | `font/line-height/20` | LINE_HEIGHT |
| `typography/field/select/option-description/m/letter-spacing` | `font/letter-spacing/10` | `font/letter-spacing/10` | LETTER_SPACING |
| `typography/field/select/option-description/m/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |
| `typography/field/select/option-description/l/size` | `font/size/16` | `font/size/16` | FONT_SIZE |
| `typography/field/select/option-description/l/line-height` | `font/line-height/24` | `font/line-height/24` | LINE_HEIGHT |
| `typography/field/select/option-description/l/letter-spacing` | `font/letter-spacing/0` | `font/letter-spacing/0` | LETTER_SPACING |
| `typography/field/select/option-description/l/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |
| `typography/field/select/option-match/s/size` | `font/size/14` | `font/size/14` | FONT_SIZE |
| `typography/field/select/option-match/s/line-height` | `font/line-height/20` | `font/line-height/20` | LINE_HEIGHT |
| `typography/field/select/option-match/s/letter-spacing` | `font/letter-spacing/10` | `font/letter-spacing/10` | LETTER_SPACING |
| `typography/field/select/option-match/s/weight` | `font/weight/600` | `font/weight/600` | FONT_WEIGHT |
| `typography/field/select/option-match/m/size` | `font/size/16` | `font/size/16` | FONT_SIZE |
| `typography/field/select/option-match/m/line-height` | `font/line-height/24` | `font/line-height/24` | LINE_HEIGHT |
| `typography/field/select/option-match/m/letter-spacing` | `font/letter-spacing/0` | `font/letter-spacing/0` | LETTER_SPACING |
| `typography/field/select/option-match/m/weight` | `font/weight/600` | `font/weight/600` | FONT_WEIGHT |
| `typography/field/select/option-match/l/size` | `font/size/18` | `font/size/18` | FONT_SIZE |
| `typography/field/select/option-match/l/line-height` | `font/line-height/28` | `font/line-height/28` | LINE_HEIGHT |
| `typography/field/select/option-match/l/letter-spacing` | `font/letter-spacing/0` | `font/letter-spacing/0` | LETTER_SPACING |
| `typography/field/select/option-match/l/weight` | `font/weight/600` | `font/weight/600` | FONT_WEIGHT |
| `size/field/select/dropdown/empty/s` | `size/192` | `size/192` | WIDTH_HEIGHT |
| `size/field/select/dropdown/empty/m` | `size/240` | `size/240` | WIDTH_HEIGHT |
| `size/field/select/dropdown/empty/l` | `size/256` | `size/256` | WIDTH_HEIGHT |

## Токены L3 (`3. Components`)

| Токен | → L2 | light | dark | scope |
|---|---|---|---|---|
| `field/select/dropdown/option/text/description` | `color/static/text/base/medium` | rgba(0,0,0,0.60) | rgba(255,255,255,0.70) | TEXT_FILL |
| `field/select/dropdown/option/text/inverse-description` | `color/static/text/base/inverse-medium` | rgba(255,255,255,0.70) | rgba(0,0,0,0.60) | TEXT_FILL |
| `field/select/dropdown/option/focus-ring` | `color/static/focus/brand` | rgba(39,129,243,1.00) | rgba(61,142,244,1.00) | STROKE_COLOR |
| `field/select/dropdown/option/inverse-focus-ring` | `color/static/focus/inverse-brand` | rgba(61,142,244,1.00) | rgba(39,129,243,1.00) | STROKE_COLOR |
| `field/size/select/s/option/focus-border` | `border/field/select/option/focus/s` | 1 | 1 | STROKE_FLOAT |
| `field/size/select/s/option/focus-radius` | `radius/field/select/option/focus/s` | 6 | 6 | CORNER_RADIUS |
| `field/size/select/s/option/text-gap` | `gap/field/select/option/text/s` | 0 | 0 | GAP |
| `field/size/select/s/option/checkbox-box` | `size/field/select/option/checkbox/s` | 20 | 20 | WIDTH_HEIGHT |
| `field/size/select/s/option/checkbox-xy` | `space/field/select/option/checkbox/s` | 0 | 0 | GAP |
| `field/size/select/s/dropdown-box/loader-gap` | `gap/field/select/dropdown/loader/s` | 4 | 4 | GAP |
| `field/size/select/m/option/focus-border` | `border/field/select/option/focus/m` | 2 | 2 | STROKE_FLOAT |
| `field/size/select/m/option/focus-radius` | `radius/field/select/option/focus/m` | 8 | 8 | CORNER_RADIUS |
| `field/size/select/m/option/text-gap` | `gap/field/select/option/text/m` | 0 | 0 | GAP |
| `field/size/select/m/option/checkbox-box` | `size/field/select/option/checkbox/m` | 24 | 24 | WIDTH_HEIGHT |
| `field/size/select/m/option/checkbox-xy` | `space/field/select/option/checkbox/m` | 0 | 0 | GAP |
| `field/size/select/m/dropdown-box/loader-gap` | `gap/field/select/dropdown/loader/m` | 6 | 6 | GAP |
| `field/size/select/l/option/focus-border` | `border/field/select/option/focus/l` | 2 | 2 | STROKE_FLOAT |
| `field/size/select/l/option/focus-radius` | `radius/field/select/option/focus/l` | 10 | 10 | CORNER_RADIUS |
| `field/size/select/l/option/text-gap` | `gap/field/select/option/text/l` | 0 | 0 | GAP |
| `field/size/select/l/option/checkbox-box` | `size/field/select/option/checkbox/l` | 28 | 28 | WIDTH_HEIGHT |
| `field/size/select/l/option/checkbox-xy` | `space/field/select/option/checkbox/l` | 2 | 2 | GAP |
| `field/size/select/l/dropdown-box/loader-gap` | `gap/field/select/dropdown/loader/l` | 8 | 8 | GAP |
| `field/size/select/s/dropdown-box/empty-height` | `size/field/select/dropdown/empty/s` | 192 | 192 | WIDTH_HEIGHT |
| `field/size/select/m/dropdown-box/empty-height` | `size/field/select/dropdown/empty/m` | 240 | 240 | WIDTH_HEIGHT |
| `field/size/select/l/dropdown-box/empty-height` | `size/field/select/dropdown/empty/l` | 256 | 256 | WIDTH_HEIGHT |

## Текстовые стили

| Стиль | Шрифт | Переменные |
|---|---|---|
| `typography/field/select/option-description/s` | Roboto Regular | `typography/field/select/option-description/s/size`, `typography/field/select/option-description/s/line-height`, `typography/field/select/option-description/s/letter-spacing`, `typography/field/select/option-description/s/weight` |
| `typography/field/select/option-description/m` | Roboto Regular | `typography/field/select/option-description/m/size`, `typography/field/select/option-description/m/line-height`, `typography/field/select/option-description/m/letter-spacing`, `typography/field/select/option-description/m/weight` |
| `typography/field/select/option-description/l` | Roboto Regular | `typography/field/select/option-description/l/size`, `typography/field/select/option-description/l/line-height`, `typography/field/select/option-description/l/letter-spacing`, `typography/field/select/option-description/l/weight` |
| `typography/field/select/option-match/s` | Roboto SemiBold | `typography/field/select/option-match/s/size`, `typography/field/select/option-match/s/line-height`, `typography/field/select/option-match/s/letter-spacing`, `typography/field/select/option-match/s/weight` |
| `typography/field/select/option-match/m` | Roboto SemiBold | `typography/field/select/option-match/m/size`, `typography/field/select/option-match/m/line-height`, `typography/field/select/option-match/m/letter-spacing`, `typography/field/select/option-match/m/weight` |
| `typography/field/select/option-match/l` | Roboto SemiBold | `typography/field/select/option-match/l/size`, `typography/field/select/option-match/l/line-height`, `typography/field/select/option-match/l/letter-spacing`, `typography/field/select/option-match/l/weight` |

## Контраст

| Передний план | Фон | Режим | Контраст | Норма | |
|---|---|---|---|---|---|
| `field/select/dropdown/option/text/description` | `field/select/dropdown/container/base` | light | 5.74 | 4.5 | ✅ |
| `field/select/dropdown/option/text/description` | `field/select/dropdown/container/base` | dark | 8.66 | 4.5 | ✅ |
| `field/select/dropdown/option/text/description` | `field/select/dropdown/option/bg/active` | light | 5.54 | 4.5 | ✅ |
| `field/select/dropdown/option/text/description` | `field/select/dropdown/option/bg/active` | dark | 7.96 | 4.5 | ✅ |
| `field/select/dropdown/option/text/description` | `field/select/dropdown/option/bg/hover` | light | 5.63 | 4.5 | ✅ |
| `field/select/dropdown/option/text/description` | `field/select/dropdown/option/bg/hover` | dark | 8.16 | 4.5 | ✅ |
| `field/select/dropdown/option/text/inverse-description` | `field/select/dropdown/container/inverse-base` | light | 9.18 | 4.5 | ✅ |
| `field/select/dropdown/option/text/inverse-description` | `field/select/dropdown/container/inverse-base` | dark | 5.74 | 4.5 | ✅ |
| `field/select/dropdown/option/text/inverse-description` | `field/select/dropdown/option/bg/inverse-active` | light | 7.68 | 4.5 | ✅ |
| `field/select/dropdown/option/text/inverse-description` | `field/select/dropdown/option/bg/inverse-active` | dark | 5.32 | 4.5 | ✅ |
| `field/select/dropdown/option/text/value` | `field/select/dropdown/option/bg/active` | light | 13.75 | 4.5 | ✅ |
| `field/select/dropdown/option/text/value` | `field/select/dropdown/option/bg/active` | dark | 14.74 | 4.5 | ✅ |
| `field/select/dropdown/option/text/value` | `field/select/dropdown/option/bg/active-hover` | light | 12.48 | 4.5 | ✅ |
| `field/select/dropdown/option/text/value` | `field/select/dropdown/option/bg/active-hover` | dark | 12.91 | 4.5 | ✅ |
| `field/select/dropdown/option/text/inverse-value` | `field/select/dropdown/option/bg/inverse-active` | light | 14.11 | 4.5 | ✅ |
| `field/select/dropdown/option/text/inverse-value` | `field/select/dropdown/option/bg/inverse-active` | dark | 12.48 | 4.5 | ✅ |
| `field/select/dropdown/option/focus-ring` | `field/select/dropdown/container/base` | light | 3.80 | 3.0 | ✅ |
| `field/select/dropdown/option/focus-ring` | `field/select/dropdown/container/base` | dark | 5.00 | 3.0 | ✅ |
| `field/select/dropdown/option/focus-ring` | `field/select/dropdown/option/bg/active` | light | 3.38 | 3.0 | ✅ |
| `field/select/dropdown/option/focus-ring` | `field/select/dropdown/option/bg/active` | dark | 4.47 | 3.0 | ✅ |
| `field/select/dropdown/option/inverse-focus-ring` | `field/select/dropdown/container/inverse-base` | light | 5.44 | 3.0 | ✅ |
| `field/select/dropdown/option/inverse-focus-ring` | `field/select/dropdown/container/inverse-base` | dark | 3.80 | 3.0 | ✅ |
| `field/select/dropdown/option/inverse-focus-ring` | `field/select/dropdown/option/bg/inverse-active` | light | 4.28 | 3.0 | ✅ |
| `field/select/dropdown/option/inverse-focus-ring` | `field/select/dropdown/option/bg/inverse-active` | dark | 2.99 | 3.0 | ⚠️ |
| `field/select/dropdown/option/indicator/icon` | `field/select/dropdown/option/bg/active` | light | 2.62 | 3.0 | ⚠️ |
| `field/select/dropdown/option/indicator/icon` | `field/select/dropdown/option/bg/active` | dark | 2.98 | 3.0 | ⚠️ |
| `field/select/dropdown/container/hint` | `field/select/dropdown/container/base` | light | 3.35 | 4.5 | ⚠️ |
| `field/select/dropdown/container/hint` | `field/select/dropdown/container/base` | dark | 4.40 | 4.5 | ⚠️ |
| `field/select/dropdown/container/inverse-hint` | `field/select/dropdown/container/inverse-base` | light | 4.50 | 4.5 | ✅ |
| `field/select/dropdown/container/inverse-hint` | `field/select/dropdown/container/inverse-base` | dark | 3.35 | 4.5 | ⚠️ |

## Решения и допущения

- Покрытие: существующие токены SimpleSelect (`field/select/dropdown/*`, `field/size/select/{s}/dropdown-box/*`, `field/size/select/{s}/option/*`, типографика `typography/field/select/option|option-title/{s}`) покрывают контейнер, Empty/Loading (hint, loader), фон пунктов по состояниям, Selected (`active*`), Check Indicator, Leading Icon, Label, Group Title и Read Only. Пресет содержит только недостающее для dropdown.md.
- Отдельный корень `field/dropdown` не заводим: Dropdown уже живёт в `field/select/dropdown` и собран приватными наборами `_ Select / Dropdown` и `_ Select / Dropdown Items`. Новые токены дописываются в те же ветки (`field/select/dropdown/option/*`, `field/size/select/{s}/option|dropdown-box/*`, L2 `*/field/select/option|dropdown/*`). Combobox и Multiselect используют этот Dropdown экземпляром и своих токенов списка не имеют. Переименование в `field/dropdown` — только по запросу автора.
- Словарь: в токенах FEroom `active` = Selected (выбранный пункт: `option/bg/active`, `active-hover`, `active-disabled`). Active из документа (клавиатурная навигация) — новый индикатор `option/focus-ring` (внутренняя обводка) с размерами `option/focus-border|focus-radius`; так Selected + Active = фон `active` + обводка, как требует документ.
- Read Only пункта = существующие `option/bg/disabled`, `option/text/disabled`, `option/leading-icon/read-only`, для выбранного — `option/bg/active-disabled` и `option/indicator/icon-disabled`.
- Description: цвет `color/static/text/base/medium` (вторичный, контраст ≥ 4.5 на фоне списка и на Selected), кегль на ступень меньше Label (значения как у `typography/field/hint/{s}`): S 12/16, M 14/20, L 16/24. Новые L2 `typography/field/select/option-description/{s}/*` и стили.
- Подсветка совпадения — полужирным начертанием (SemiBold 600), цвет Label не меняется (WCAG 1.4.1). Новые L2 `typography/field/select/option-match/{s}/*` и стили; применяются к диапазону текста в Label.
- Multi: Checkbox — экземпляр компонента Checkbox (S-пункт → Checkbox M, M и L → Checkbox L), своих цветов нет. Рамка `option/checkbox-box` = 20/24/28 выровнена с `leading-icon-box`, чтобы Checkbox и Leading Icon стояли на одной сетке.
- Loading: Spinner (`dropdown-box/loader`, существующий) + текст «Загрузка…» цветом `container/hint` и стилем option; новый только зазор `dropdown-box/loader-gap` 4/6/8 (как `gap-trailing` поля).
- Divider, Scroll, Tooltip — экземпляры своих компонентов, токенов не требуют. Пункты Create и Select All — вариант Value (Leading Icon «+» и Checkbox соответственно), новых цветов нет.
- Максимальная высота (10 пунктов + отступы контейнера) — вычисляемая величина: S 10×32+2×2, M 10×40+2×3, L 10×48+2×4. Отдельный L2 не заводим, в L1 нет подходящих значений.
- Эффекты не создаём: тень контейнера — существующий эффект-стиль `effect/select/{regular|inverse}/{S|M|L}`. Скругление и обводка контейнера Dropdown в токенах select отсутствуют — вопрос автору.
- Контраст, accepted: `option/inverse-focus-ring` на `option/bg/inverse-active` в dark = 2.99 (граница 3.0). Другой семантики фокуса бренда в шкале `color/static/focus` нет (brand / inverse-brand — единственная пара); на фоне контейнера без Selected норма выполняется.
- Контраст, accepted: Check Indicator `option/indicator/icon` (существующий токен select, `color/static/indicator/brand/medium`, 0.8) на Selected-фоне `option/bg/active` = 2.62 light / 2.98 dark < 3. Токен не меняем; Selected дополнительно передаётся фоном и `aria-selected`. Кандидат на замену — непрозрачный бренд (`color/static/indicator/brand/firm`); вопрос автору.
- Контраст, accepted: `field/select/dropdown/container/hint` («Ничего не найдено», «Загрузка…») — существующий токен select (`color/static/text/base/light`), не меняем; вопрос автору.
