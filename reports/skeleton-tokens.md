# Токены: Skeleton

Пресет: `presets/skeleton.tokens.json`. Источник: `input/backlog/skeleton.md`. Аналог: `avatar`.

Статус проверки: **OK** · L2 новых: 22 · L3: 36 · текстовых стилей: 0

## Новые токены L2 (`2. General`)

| Токен | light | dark | scopes |
|---|---|---|---|
| `size/skeleton/line/s` | `size/16` | `size/16` | WIDTH_HEIGHT |
| `size/skeleton/line/m` | `size/20` | `size/20` | WIDTH_HEIGHT |
| `size/skeleton/line/l` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `size/skeleton/line/xl` | `size/28` | `size/28` | WIDTH_HEIGHT |
| `gap/skeleton/line` | `space/4` | `space/4` | GAP |
| `radius/skeleton/line` | `radius/999` | `radius/999` | CORNER_RADIUS |
| `size/skeleton/circle/s` | `size/16` | `size/16` | WIDTH_HEIGHT |
| `size/skeleton/circle/m` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `size/skeleton/circle/l` | `size/32` | `size/32` | WIDTH_HEIGHT |
| `size/skeleton/circle/xl` | `size/48` | `size/48` | WIDTH_HEIGHT |
| `size/skeleton/circle/2xl` | `size/64` | `size/64` | WIDTH_HEIGHT |
| `radius/skeleton/circle` | `radius/999` | `radius/999` | CORNER_RADIUS |
| `radius/skeleton/block/image` | `radius/8` | `radius/8` | CORNER_RADIUS |
| `radius/skeleton/block/card` | `radius/12` | `radius/12` | CORNER_RADIUS |
| `size/skeleton/block/control-s` | `size/24` | `size/24` | WIDTH_HEIGHT |
| `radius/skeleton/block/control-s` | `radius/4` | `radius/4` | CORNER_RADIUS |
| `size/skeleton/block/control-m` | `size/32` | `size/32` | WIDTH_HEIGHT |
| `radius/skeleton/block/control-m` | `radius/6` | `radius/6` | CORNER_RADIUS |
| `size/skeleton/block/control-l` | `size/40` | `size/40` | WIDTH_HEIGHT |
| `radius/skeleton/block/control-l` | `radius/8` | `radius/8` | CORNER_RADIUS |
| `size/skeleton/block/control-xl` | `size/48` | `size/48` | WIDTH_HEIGHT |
| `radius/skeleton/block/control-xl` | `radius/10` | `radius/10` | CORNER_RADIUS |

## Токены L3 (`3. Components`)

| Токен | → L2 | light | dark | scope |
|---|---|---|---|---|
| `skeleton/shape/bg` | `color/static/bg/transparent/base/light` | rgba(0,0,0,0.10) | rgba(255,255,255,0.10) | FRAME_FILL |
| `skeleton/shape/inverse-bg` | `color/static/bg/transparent/base/inverse-light` | rgba(255,255,255,0.10) | rgba(0,0,0,0.10) | FRAME_FILL |
| `skeleton/shimmer/bg` | `color/static/bg/transparent/base/mild` | rgba(0,0,0,0.05) | rgba(255,255,255,0.05) | FRAME_FILL |
| `skeleton/shimmer/inverse-bg` | `color/static/bg/transparent/base/inverse-mild` | rgba(255,255,255,0.05) | rgba(0,0,0,0.05) | FRAME_FILL |
| `skeleton/size/line/s/height` | `size/skeleton/line/s` | 16 | 16 | WIDTH_HEIGHT |
| `skeleton/size/line/s/gap` | `gap/skeleton/line` | 4 | 4 | GAP |
| `skeleton/size/line/s/radius` | `radius/skeleton/line` | 999 | 999 | CORNER_RADIUS |
| `skeleton/size/line/m/height` | `size/skeleton/line/m` | 20 | 20 | WIDTH_HEIGHT |
| `skeleton/size/line/m/gap` | `gap/skeleton/line` | 4 | 4 | GAP |
| `skeleton/size/line/m/radius` | `radius/skeleton/line` | 999 | 999 | CORNER_RADIUS |
| `skeleton/size/line/l/height` | `size/skeleton/line/l` | 24 | 24 | WIDTH_HEIGHT |
| `skeleton/size/line/l/gap` | `gap/skeleton/line` | 4 | 4 | GAP |
| `skeleton/size/line/l/radius` | `radius/skeleton/line` | 999 | 999 | CORNER_RADIUS |
| `skeleton/size/line/xl/height` | `size/skeleton/line/xl` | 28 | 28 | WIDTH_HEIGHT |
| `skeleton/size/line/xl/gap` | `gap/skeleton/line` | 4 | 4 | GAP |
| `skeleton/size/line/xl/radius` | `radius/skeleton/line` | 999 | 999 | CORNER_RADIUS |
| `skeleton/size/circle/s/box` | `size/skeleton/circle/s` | 16 | 16 | WIDTH_HEIGHT |
| `skeleton/size/circle/s/radius` | `radius/skeleton/circle` | 999 | 999 | CORNER_RADIUS |
| `skeleton/size/circle/m/box` | `size/skeleton/circle/m` | 24 | 24 | WIDTH_HEIGHT |
| `skeleton/size/circle/m/radius` | `radius/skeleton/circle` | 999 | 999 | CORNER_RADIUS |
| `skeleton/size/circle/l/box` | `size/skeleton/circle/l` | 32 | 32 | WIDTH_HEIGHT |
| `skeleton/size/circle/l/radius` | `radius/skeleton/circle` | 999 | 999 | CORNER_RADIUS |
| `skeleton/size/circle/xl/box` | `size/skeleton/circle/xl` | 48 | 48 | WIDTH_HEIGHT |
| `skeleton/size/circle/xl/radius` | `radius/skeleton/circle` | 999 | 999 | CORNER_RADIUS |
| `skeleton/size/circle/2xl/box` | `size/skeleton/circle/2xl` | 64 | 64 | WIDTH_HEIGHT |
| `skeleton/size/circle/2xl/radius` | `radius/skeleton/circle` | 999 | 999 | CORNER_RADIUS |
| `skeleton/size/block/image/radius` | `radius/skeleton/block/image` | 8 | 8 | CORNER_RADIUS |
| `skeleton/size/block/card/radius` | `radius/skeleton/block/card` | 12 | 12 | CORNER_RADIUS |
| `skeleton/size/block/control-s/height` | `size/skeleton/block/control-s` | 24 | 24 | WIDTH_HEIGHT |
| `skeleton/size/block/control-s/radius` | `radius/skeleton/block/control-s` | 4 | 4 | CORNER_RADIUS |
| `skeleton/size/block/control-m/height` | `size/skeleton/block/control-m` | 32 | 32 | WIDTH_HEIGHT |
| `skeleton/size/block/control-m/radius` | `radius/skeleton/block/control-m` | 6 | 6 | CORNER_RADIUS |
| `skeleton/size/block/control-l/height` | `size/skeleton/block/control-l` | 40 | 40 | WIDTH_HEIGHT |
| `skeleton/size/block/control-l/radius` | `radius/skeleton/block/control-l` | 8 | 8 | CORNER_RADIUS |
| `skeleton/size/block/control-xl/height` | `size/skeleton/block/control-xl` | 48 | 48 | WIDTH_HEIGHT |
| `skeleton/size/block/control-xl/radius` | `radius/skeleton/block/control-xl` | 10 | 10 | CORNER_RADIUS |

## Контраст

| Передний план | Фон | Режим | Контраст | Норма | |
|---|---|---|---|---|---|
| `skeleton/shape/bg` | `color/bg/page/main` | light | 1.25 | 3.0 | ⚠️ |
| `skeleton/shape/bg` | `color/bg/page/main` | dark | 1.35 | 3.0 | ⚠️ |
| `skeleton/shape/bg` | `color/bg/page/tertiary` | light | 1.25 | 3.0 | ⚠️ |
| `skeleton/shape/bg` | `color/bg/page/tertiary` | dark | 1.37 | 3.0 | ⚠️ |
| `skeleton/shape/inverse-bg` | `color/bg/page/inverse-main` | light | 1.35 | 3.0 | ⚠️ |
| `skeleton/shape/inverse-bg` | `color/bg/page/inverse-main` | dark | 1.25 | 3.0 | ⚠️ |
| `skeleton/shimmer/bg` | `skeleton/shape/bg` | light | 1.11 | 3.0 | ⚠️ |
| `skeleton/shimmer/bg` | `skeleton/shape/bg` | dark | 1.17 | 3.0 | ⚠️ |

## Решения и допущения

- Цвет фигуры — `color/static/bg/transparent/base/light` (10 %): ровно та же семантика, что у встроенных заглушек загрузки FEroom (switch/loading/name, checkbox/loading/icon, status/loading/name). Документ предлагает `color/static/bg/neutral/subtle` — такого имени в FEroom нет. Прозрачная семантика выбрана вместо solid (`color/static/bg/solid/base/soft`), потому что заглушка стоит и на page/main, и на page/tertiary, и в карточках — прозрачная работает на любом нейтральном фоне.
- Блик мерцания — `color/static/bg/transparent/base/mild` (5 %): полоса слабее фигуры и в light, и в dark (одна прозрачная шкала, без ссылки на L1 `color/transparent-white/*`, о которой предупреждает документ). Исключение L3 → L1 не нужно. Сама анимация (shimmer, цикл 1000 мс, reduced-motion) не создаётся — motion-токенов в FEroom нет; `motion/duration/loop`, `motion/delay/loading-show|loading-min` из документа — вопрос к автору, не к токенам компонента.
- Инверсия: документ говорит «в dark те же имена, отдельного варианта нет» — это про тему (light/dark), она приходит через L2. Для тёмных поверхностей в светлой теме FEroom использует части `inverse-*` (как switch/loading/inverse-name → color/static/bg/transparent/base/inverse-light) — заведены `skeleton/shape/inverse-bg` и `skeleton/shimmer/inverse-bg`, ось Inverse.
- Оси размера у компонента нет (документ): размер — у каждой формы свой. В L3 форма — подраздел: `skeleton/size/{line|circle|block}/{size}/{prop}` (как divider/size/label/m/*). Line S/M/L/XL = 16/20/24/28 — интерлиньяжи текста 12/16, 14/20, 16/24, 18/28 (как typography/link/{s…xl}); Circle S…2XL = 16/24/32/48/64 — диаметры Avatar (size/avatar/box/*); Block Control S…XL = высоты и скругления Button S…XL (24/32/40/48 и 4/6/8/10); Block Image — 8, Block Card — 12 (высота блока свободная).
- Скругление строки — полное 999 (документ: `radius/full`, альтернатива «кирпичики» 4 — меняется одно значение `radius/skeleton/line`). Промежуток строк абзаца 4 (`space/stack/tight` документа) — `gap/skeleton/line`.
- Имена документа `typography/helper|body/*/line-height`, `size/entity/*`, `radius/image`, `radius/card`, `radius/control/*`, `size/control/*`, `radius/full` в FEroom отсутствуют — заведены свои L2 компонента по грамматике (правило 3 формата: даже при совпадении значений с аналогом создаётся свой L2).
- Доли ширины строк (40 · 60 · 100 %) — не токены, правило сборки.
- Текстовых стилей нет (в заглушке нет текста). Эффект-стилей и теней нет.
- Контраст фигура/фон ≈ 1,2 : 1 — принят сознательно (accepted): фигуры декоративны, WCAG 1.4.11 не применяется (решение 10 документа).
