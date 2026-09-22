# Устройство готовых компонентов (из файла «Компоненты · Базовые»)

Эталон для `feds-component-builder` и `feds-component-describer`. Снято скриптом `tools/figma/scan-page.js` 2026-09-21. Проблемы привязок — в `reports/components-file-audit.md`.

## Общие паттерны сборки (закон для новых компонентов)

1. **Страница компонента:** секции `{Имя}. Мастер` (или `Master`) и `Спецификация`. На странице Button есть ещё фреймы «Важная информация» и «История изменений».
2. **Разбиение на наборы.** Когда осей много, набор делится по оси формы или размера, и она уходит в имя набора: `Button / Filled`, `Button / Outline`, `Button / Text`, `Button / Icon - Outline`; `Checkbox / Left / M`, `Checkbox / Right / L`, `Checkbox / Card`; `Badge / Circle`, `Badge / Squared`. Самый большой набор — 420 вариантов (Chip).
3. **Порядок свойств:** сначала контентные (Text, Boolean, Instance swap с `↳`), затем `Focused` (Boolean), затем Variant-оси: `Size` → `Type`/`Color` → `State` → `Loading`/`Inverse`.
4. **Имена свойств:** Title Case. Вложенные значения — с префиксом `↳ ` (`↳ Icon`, `↳ Name`, `↳ Num`). Опциональные части в Field помечены префиксом `+ ` (`+ Hint`, `+ Link`, `+ Counter (A/N)`).
5. **Значения вариантов:** `False|True` для булевых осей в Variant (`Loading`, `Inverse`, `Filled`, `Checked`). Состояния — `Default|Hover|Pressed|Disabled` (+ `Loading`, `Pending`, `Read Only`, `Error|Warning|Success`, `Visited`).
6. **Фокус:** слой `Focus Ring` (RECTANGLE, absolute, FILL×FILL), скрыт, `visible → Focused`. Радиус и толщина → `{c}/size/{s}/focus-*`, обводка → `{c}/focus-ring`.
7. **Корень варианта:** auto layout, отступы, gap, радиус, толщина обводки и высота привязаны к `{c}/size/{s}/…`; заливка и обводка — к `{c}/{variant}/{bg|border}/{state}`.
8. **Иконки:** экземпляр иконки из библиотеки (по умолчанию `circle`), `height → {c}/size/{s}/icon`, свойство Instance swap `↳ Icon` с preferred values.
9. **Текст:** текстовый стиль `typography/{action/}{c}/{s}/{slot}` + заливка `{c}/…/text/{state}`, свойство Text для содержимого.
10. **Вложенные компоненты — только экземплярами:** Button (Icon Only) внутри Chip и Select, Avatar внутри Checkbox/Radio/Chip, Badge внутри Priority Indicator / Custom, Link внутри Field.
11. **Приватные части** — префикс `_`: `_ Avatar / …`, `_ Divider / Atom / …`, `_ Field / …`, `_ Select / Dropdown …`.
12. **Card-варианты** (Checkbox, Radio, Switch): отдельный набор `{C} / Card` с экземпляром основного компонента внутри.

## Компоненты

| Страница | Наборы (вариантов) | Оси и свойства |
|---|---|---|
| **Button** | Filled 168, Outline 168, Text 84, Icon - Filled 168, Icon - Outline 168, Icon Only 168 | Size XL/L/M/S · Type (Primary, Secondary, Primary-soft, Ghost, Danger, Danger-soft; у Text: Primary/Secondary/Danger; у Icon Only: + Tertiary, Inverse-primary, Inverse-secondary) · State Default/Hover/Pressed/Disabled · Loading · Label (T) · Left/Right Icon (B) + `↳ Icon L/R` (I) · Focused |
| **Badge** | Circle 70, Squared 70 | Size M/S · Filled · Color Grey/Blue/Red/Green/Yellow/Purple/White · Type Default/Icon + Text/Icon · Name (T), Counter (B), `↳ Num`, Icon (B), `↳ Icon`, Status (B) |
| **Checkbox** | Left/M 30, Left/L 30, Right/M 30, Right/L 30, Card 12 | Checked · Indeterminate · State (+Loading) · Inverse · Text/Description/Avatar (B) · `↳ Name`, `↳ Description` · Error / Mandatory · Focused |
| **Chip** | Circle 420, Squared 420 | State Default/Hover/Pressed / Selected/Disabled/Loading · Size M/S · Avatar · Group · Color Gray…White · Filled · Hint Text, Icon, X-icon, Counter (B) · `↳ Hint`, `↳ Name`, `↳ Icon`, `↳ Num`, `↳ Content`, `↳ Head` |
| **Divider** | Horizontal 24, Vertical 24; приватные: Atom / Padding_horizontal 8, Padding_vertical 8, Label 6 | Thickness XS/S/M · Color Subtle/Regular/Strong/Intense · Rounding · Label, Left/Right (Up/Down) Padding (B) |
| **Link** | Inline 48, Standalone 48 | Size XL/L/M/S · Type Main/Danger/Secondary · State (Inline: +Visited; Standalone: +Disabled) · `↳ Name` · Left/Right Icon у Standalone |
| **Priority Indicator** | Indicator / Priority 32, Indicator / Custom 4 | Status None/Minor/Low/Medium/High/Critical/Blocker/Loading · Colored · Size S/M · Text (B) |
| **Radiobutton** | Radio / Left/M, Left/L, Right/M, Right/L — по 20; Card 12 | как Checkbox без Indeterminate |
| **Status** | Circle 80, Square 80, Unboxed 32 | Size M/L · Filled · Type Dot-status/With Icon/Text Only · Color Neutral/Info/Error/Success/Warning/Pending/Brand · Loading · (Unboxed: Inverse) |
| **Switch** | Left/M, Left/L, Right/M, Right/L — по 24; Card 12 | On · State (+Pending, Loading) · Inverse · Icon-status, Text, Description (B) · Error / Mandatory · Focused |
| **Avatar** | 46 наборов: `_ Avatar / {s…2xl} / {Circle,Square}`, `_ Avatar-Group / …` (+ `-сounter`), Avatar / Button-X | Style Image/Soft/Filled · Type Photo/Initials/Loading/Интеграции/Файл/Боты/Компания/Проекты/Команда · Color · Grouped · Focused. Разобран не полностью. |
| **Input, Text Area, Field** | 74 набора: Field / Vertical 48, Horizontal 48; Field / Password 108, Search 66, Email 84, URL 90, Phone 90, Currency 90; Input / {S,M,L} - {Base,Error…}; Text Area; приватные `_ Field / …` | Type Base/Error/Warning/Success · Size S/M/L · Text Area · Inverse · `+ Counter`, `+ Extra Space`, `+ Hint`, `+ Link`, Label, Description Zone (B). Разобран не полностью. |
| **SimpleSelect** | Select / Button / {S,M,L} по 32; `_ Select / Dropdown Items / {S,M,L}` по 24; `_ Select / Dropdown / {S,M,L}` по 6 | Filled · State (8) · Inverse · Leading Icon, Clear, Loading, Validation Marker (B) · Dropdown: State Default/Empty/Loading, 03…010 (B) — видимость пунктов |

## Что уточнить при детальном анализе (feds-system-analyst)

- Полный разбор Avatar и Field/Input/Text Area (вывод обрезан по объёму).
- Где у Chip слоты `↳ Content` и `↳ Head` (режим Group).
- Правило деления на наборы: по какой оси делить и в каком порядке оси в имени набора.
