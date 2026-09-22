# Ошибки в именах: полные пути (файл «Элементы · Основа стилей»)

Стили хранятся не в коллекциях переменных, а в локальных стилях файла: Assets → Local styles → Text / Effect / Paint. Путь стиля — это его папки через `/`.

Ничего не исправлено. Автор разрешил пока не трогать эффект-стили: они ещё не проработаны.

## 1. Текстовые стили (Local styles → Text styles)

| Полный путь стиля | Что не так | Как в переменных |
|---|---|---|
| `typography / priority_Indicator / m` | подчёркивание и заглавная в сегменте | `2. General / typography / priority-indicator / m / …` |
| `typography / priority_Indicator / s` | то же | `2. General / typography / priority-indicator / s / …` |
| `typography / field / select / option_title / l` | подчёркивание | `2. General / typography / field / select / option-title / l / …` |
| `typography / field / select / option_title / m` | то же | то же |
| `typography / field / select / option_title / s` | то же | то же |


## 2. Эффект-стили (Local styles → Effect styles) — отложено автором

| Полный путь стиля | Что не так |
|---|---|
| `effect / select / regular / S`, `/ M`, `/ L` | размер заглавной; в переменных `effects/select/*/s|m|l` |
| `effect / select / inverse / S`, `/ M`, `/ L` | то же |
| `effect / switch / knob / M`, `/ L` | то же; в переменных `effects/switch/knob/*/m|l` |
| корень `effect/…` у всех 59 стилей | в переменных корень `effects/…` (мн. число) |
| `effect / select / *` | цвет тени привязан к L1 `1. Primitives / color / transparent-black / 120` в обход L2 |
| 51 стиль (`effect/elevation/*`, `effect/focus/*`, `effect/button/*` и др.) | значения без переменных |

## 3. Paint-стили (Local styles → Color styles)

Это изображения, а не токены. Отмечено для полноты:
- `Avatar / Female / {Имя Фамилия}` и `Avatar / Male / {Имя Фамилия}` (20 шт.) — PascalCase и кириллица.
- `↳ Select Image` — служебный символ в имени.

## 4. Переменные (коллекции)

| Коллекция | Полный путь | Что не так |
|---|---|---|
| `3. Components` | `checkbox / loading / box-uncheked` | опечатка: unchecked |
| `3. Components` | `checkbox / loading / inverse-box-uncheked` | то же |
| `3. Components` | `radiobutton / loading / box-uncheked` | то же |
| `3. Components` | `radiobutton / loading / inverse-box-uncheked` | то же |
| `2. General` | `number` | корневая переменная без группы, scope `ALL_SCOPES`, сырое значение 0 (отложено) |

## 5. Иконки (страница Icons)

- Компонент `4х4`: в имени кириллическая «х» вместо латинской «x». У остальных рамок-размеров (`8x8` … `48x48`) латиница.
