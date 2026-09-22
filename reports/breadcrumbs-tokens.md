# Токены: Breadcrumbs

Пресет: `presets/breadcrumbs.tokens.json`. Источник: `input/backlog/breadcrumbs.md`. Аналог: `link`.

Статус проверки: **OK** · L2 новых: 12 · L3: 17 · текстовых стилей: 1

## Новые токены L2 (`2. General`)

| Токен | light | dark | scopes |
|---|---|---|---|
| `size/breadcrumbs/m` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `gap/breadcrumbs/m` | `space/4` | `space/4` | GAP |
| `size/breadcrumbs/separator/m` | `size/12` | `size/12` | WIDTH_HEIGHT |
| `size/breadcrumbs/overflow/m` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `size/breadcrumbs/overflow/m-icon` | `size/16` | `size/16` | WIDTH_HEIGHT |
| `radius/breadcrumbs/overflow/m` | `radius/4` | `radius/4` | CORNER_RADIUS |
| `radius/breadcrumbs/focus/m` | `radius/7` | `radius/7` | CORNER_RADIUS |
| `border/breadcrumbs/focus/m` | `border/1` | `border/1` | STROKE_FLOAT |
| `typography/breadcrumbs/m/current/size` | `font/size/14` | `font/size/14` | FONT_SIZE |
| `typography/breadcrumbs/m/current/line-height` | `font/line-height/20` | `font/line-height/20` | LINE_HEIGHT |
| `typography/breadcrumbs/m/current/letter-spacing` | `font/letter-spacing/0` | `font/letter-spacing/0` | LETTER_SPACING |
| `typography/breadcrumbs/m/current/weight` | `font/weight/400` | `font/weight/400` | FONT_WEIGHT |

## Токены L3 (`3. Components`)

| Токен | → L2 | light | dark | scope |
|---|---|---|---|---|
| `breadcrumbs/separator/icon` | `color/static/indicator/base/light` | rgba(0,0,0,0.45) | rgba(255,255,255,0.50) | SHAPE_FILL |
| `breadcrumbs/current/text` | `color/static/text/base/hard` | rgba(0,0,0,0.85) | rgba(255,255,255,1.00) | TEXT_FILL |
| `breadcrumbs/overflow/bg/default` | `color/action/bg/base/ghost/default` | rgba(0,0,0,0.00) | rgba(255,255,255,0.00) | FRAME_FILL |
| `breadcrumbs/overflow/bg/hover` | `color/action/bg/base/ghost/hover` | rgba(0,0,0,0.03) | rgba(255,255,255,0.03) | FRAME_FILL |
| `breadcrumbs/overflow/bg/pressed` | `color/action/bg/base/ghost/pressed` | rgba(0,0,0,0.07) | rgba(255,255,255,0.07) | FRAME_FILL |
| `breadcrumbs/overflow/icon/default` | `color/action/indicator/base/medium/default` | rgba(0,0,0,0.60) | rgba(255,255,255,0.70) | SHAPE_FILL |
| `breadcrumbs/overflow/icon/hover` | `color/action/indicator/base/medium/hover` | rgba(0,0,0,0.85) | rgba(255,255,255,0.90) | SHAPE_FILL |
| `breadcrumbs/overflow/icon/pressed` | `color/action/indicator/base/medium/pressed` | rgba(0,0,0,0.85) | rgba(255,255,255,0.90) | SHAPE_FILL |
| `breadcrumbs/focus-ring` | `color/static/focus/brand` | rgba(39,129,243,1.00) | rgba(61,142,244,1.00) | STROKE_COLOR |
| `breadcrumbs/size/m/box` | `size/breadcrumbs/m` | 24 | 24 | WIDTH_HEIGHT |
| `breadcrumbs/size/m/gap` | `gap/breadcrumbs/m` | 4 | 4 | GAP |
| `breadcrumbs/size/m/separator-icon` | `size/breadcrumbs/separator/m` | 12 | 12 | WIDTH_HEIGHT |
| `breadcrumbs/size/m/overflow-box` | `size/breadcrumbs/overflow/m` | 20 | 20 | WIDTH_HEIGHT |
| `breadcrumbs/size/m/overflow-icon` | `size/breadcrumbs/overflow/m-icon` | 16 | 16 | WIDTH_HEIGHT |
| `breadcrumbs/size/m/overflow-radius` | `radius/breadcrumbs/overflow/m` | 4 | 4 | CORNER_RADIUS |
| `breadcrumbs/size/m/focus-border` | `border/breadcrumbs/focus/m` | 1 | 1 | STROKE_FLOAT |
| `breadcrumbs/size/m/focus-radius` | `radius/breadcrumbs/focus/m` | 7 | 7 | CORNER_RADIUS |

## Текстовые стили

| Стиль | Шрифт | Переменные |
|---|---|---|
| `typography/action/breadcrumbs/m/current` | Roboto Regular | `typography/breadcrumbs/m/current/size`, `typography/breadcrumbs/m/current/line-height`, `typography/breadcrumbs/m/current/letter-spacing`, `typography/breadcrumbs/m/current/weight` |

## Контраст

| Передний план | Фон | Режим | Контраст | Норма | |
|---|---|---|---|---|---|
| `breadcrumbs/current/text` | `color/bg/page/main` | light | 15.08 | 4.5 | ✅ |
| `breadcrumbs/current/text` | `color/bg/page/main` | dark | 16.48 | 4.5 | ✅ |
| `breadcrumbs/separator/icon` | `color/bg/page/main` | light | 3.35 | 3.0 | ✅ |
| `breadcrumbs/separator/icon` | `color/bg/page/main` | dark | 5.10 | 3.0 | ✅ |
| `breadcrumbs/overflow/icon/default` | `breadcrumbs/overflow/bg/default` | light | 5.74 | 3.0 | ✅ |
| `breadcrumbs/overflow/icon/default` | `breadcrumbs/overflow/bg/default` | dark | 8.66 | 3.0 | ✅ |
| `breadcrumbs/overflow/icon/hover` | `breadcrumbs/overflow/bg/hover` | light | 14.33 | 3.0 | ✅ |
| `breadcrumbs/overflow/icon/hover` | `breadcrumbs/overflow/bg/hover` | dark | 12.54 | 3.0 | ✅ |
| `breadcrumbs/overflow/icon/pressed` | `breadcrumbs/overflow/bg/pressed` | light | 13.35 | 3.0 | ✅ |
| `breadcrumbs/overflow/icon/pressed` | `breadcrumbs/overflow/bg/pressed` | dark | 11.20 | 3.0 | ✅ |
| `link/secondary/text/default` | `color/bg/page/main` | light | 5.74 | 4.5 | ✅ |
| `link/secondary/text/default` | `color/bg/page/main` | dark | 8.66 | 4.5 | ✅ |
| `breadcrumbs/focus-ring` | `color/bg/page/main` | light | 3.80 | 3.0 | ✅ |
| `breadcrumbs/focus-ring` | `color/bg/page/main` | dark | 5.00 | 3.0 | ✅ |

## Решения и допущения

- Уровни пути — экземпляры Link / Standalone, Type Secondary, Size M, State Default/Hover/Pressed (+ Focused). Документ прямо строит уровень на Link, а все его числа совпадают с Link M: текст 14/20/400 (typography/link/m), иконка 16 (link/size/m/icon), цвета «вторичной» ссылки default 60 % → hover/pressed 85 % (link/secondary/text/* → color/action/text/base/medium/*), подчёркивание на hover — поведение Standalone Link. Свои токены ссылок не заводятся: только разделитель, текущая страница, кнопка «…», высота строки и промежуток. Иконка «дом» в корне и мобильный вариант «← Родитель» — Left Icon у того же Link.
- Документ: цвет ссылок `color/action/text/neutral/secondary/*`, текущей — `color/static/text/neutral/primary`, разделителя — `color/static/icon/neutral/tertiary`. В FEroom это `link/secondary/*` (через экземпляр), `color/static/text/base/hard` и `color/static/indicator/base/light` (45 %, ≥ 3 : 1 к фону в light и dark).
- Текущая страница — не ссылка, поэтому это собственный текстовый слой со статическим цветом и собственной типографикой `typography/breadcrumbs/m/current/*` (те же 14/20/400/0, что у typography/link/m — по правилу каждый компонент получает свой L2). Стиль `typography/action/breadcrumbs/m/current` (группа action: компонент интерактивный, как link).
- Кнопка «…» — собственная часть, а не экземпляр Button: у Button Icon Only наименьший размер S = 24 с отступами и другой формой, а в строке пути «…» должна быть по высоте равна ссылке Link M (20). Цвета — как у ghost-кнопки: фон `color/action/bg/base/ghost/*`, иконка `color/action/indicator/base/medium/*` (тот же тон, что link/secondary/icon, чтобы «…» не выделялась среди уровней). Иконка — `ellipsis` из набора Lucide. Disabled нет (документ).
- Разделитель — иконка `chevron-right` 12 (альтернатива «/» — значение свойства компонента, не токен). Отступ 4 с каждой стороны реализован промежутком auto layout `gap/breadcrumbs/m` = 4 между всеми элементами строки — между названиями получается 4 + 12 + 4.
- Высота строки 24 (`size/breadcrumbs/m`) — зона нажатия по вертикали; ссылка Link M (20) центрируется внутри. Имена документа `size/control/s`, `space/inline/tight`, `size/icon/xs`, `space/stack/default`, `space/focus-ring/offset` в FEroom не существуют — заведены свои L2. Отступ «крошки → заголовок страницы» (8) — правило раскладки страницы, токен не заводится.
- Кольцо фокуса кнопки «…»: толщина 1 и скругление 7 — как у Link M (border/link/focus-regular, radius/link/focus/m), чтобы в одной строке фокус ссылок и «…» выглядел одинаково. Документ просит 2 px — расхождение, открытый вопрос: менять ли фокус Link M целиком.
- Размер один (документ), но в именах сохранён сегмент `m` (`breadcrumbs/size/m/*`) — компактный вариант S (12/16, Link S) добавится без переименований.
- Инверсия: документ говорит «наследует режим фрейма, отдельного варианта нет»; в FEroom инверсия делается токенами `inverse-*`. Но у Link, из экземпляров которого состоит путь, инверсных токенов нет, поэтому ось Inverse у Breadcrumbs не заводится: свои inverse-токены разделителя и текущей страницы без инверсного Link дали бы нечитаемые ссылки. Появится вместе с инверсией Link.
- Меню скрытых уровней — Dropdown/Menu (отдельный компонент бэклога), его токены здесь не создаются. Tooltip для обрезанных названий — экземпляр Tooltip.
- Анимации и тени не создаются, эффект-стили не нужны.
