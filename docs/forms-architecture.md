# Архитектура полей форм: семейства Input и Select

*(21.09.2026; основа — текущие Input, Field и SimpleSelect файла «Компоненты · Базовые»; композиция сверена с Atlassian Text field, Select и Form)*

## Решение
Пользователь выбирает из двух **семейств**, а не из десятка наборов:

| Семейство | Публикуется | Режим Field | Разновидности |
|---|---|---|---|
| **Select** | `Select` | None · Vertical · Horizontal | Select (сделано) · далее Combobox, Multiselect на том же списке |
| **Input** | `Input` | None · Vertical · Horizontal | Text · Text Area · Password · Search · Email · URL · Phone · Currency · Number |

**Field не публикуется.** Это не компонент, а режим семейства (свойство `Field`):
- **None** — только контрол: фильтры, строки таблиц, плотные панели; доступное имя задаётся в коде;
- **Vertical** — Label сверху, Description и сообщение проверки снизу (основной режим форм);
- **Horizontal** — колонка Label слева (`field/size/label/{s}/horizontal`), контрол и Description справа.

**Dropdown не публикуется.** Это механика списка: общий пресет токенов `field-dropdown` (вид `part`) и приватные части `_ Select / Dropdown`, `_ Select / Dropdown Items`. В каталоге плагина Dropdown не выбирается отдельно — его подключают Select, Combobox и Multiselect.

## Семейство Select (собрано)
| Набор | Публикуется | Оси | Вариантов |
|---|---|---|---|
| `Select` | да | Field × Type (Base/Error/Warning/Success) × Size (S/M/L) × Open × Inverse | 144 |
| `_ Select / Button / {S,M,L}` | нет | Filled × State (8) × Inverse | 32 × 3 |
| `_ Select / Dropdown / {S,M,L}` | нет | State (Default/Empty/Loading) × Inverse | 6 × 3 |
| `_ Select / Dropdown Items / {S,M,L}` | нет | Active × State × Type (Option/Group Title/Divider) × Inverse | 24 × 3 |

- Контрол и список — вложенные экземпляры, открытые наружу: в экземпляре `Select` меняются Filled, State, значение, Leading Icon, Loading контрола и State списка.
- Type — одно свойство для Field и контрола: рамка и маркер контрола, сообщение проверки под ним.
- Список: Default — пункты, высота по содержимому; Empty («Ничего не найдено») и Loading — панель той же ширины и своей высоты (`field/size/select/{s}/dropdown-box/empty-height`: 192 · 240 · 256), подсказка и загрузка по центру, как в макетах.
- Open = True показывает список под контролом в потоке (как `Select` Open=True в файле); в продукте список — всплывающий слой.
- Свойства Field: `Label`, `↳ Label`, `+ Required (*)`, `+ Add. Text`, `↳ Add. Text`, `Description Zone`, `↳ Hint`, `↳ Message`, `+ Extra Space`.
- Части Field собираются внутри семейства из токенов `field/*` — те же, что у Input; приватные `_ Field / …` не нужны.

## Семейство Input (план, после согласования)
Та же схема, что у Select:
- публикуется `Input` с осями `Field` (None/Vertical/Horizontal) × `Type` × `Size` × `Inverse` и осью разновидности `Kind` (Text, Text Area, Password, Search, Email, URL, Phone, Currency, Number);
- контролы разновидностей — приватные наборы `_ Input / {Kind} / {S,M,L}` (повтор текущих `Input / {S} - {Type}`, `Text Area`, `Field / Password` и других);
- если `Kind` × 3 режима × 4 типа × 3 размера × 2 инверсии превышает лимит 400 вариантов набора, семейство делится по `Kind` на наборы `Input / Text`, `Input / Password` и т. д. с одинаковыми осями Field и Type.

Открытые вопросы для согласования:
1. Один набор `Input` с осью `Kind` или наборы по разновидностям (`Input / Text`, `Input / Password`…)? Рекомендация — по разновидностям: у Password, Search и Currency свои части (глаз, лупа, валюта), общие только Field и контейнер.
2. Номер и Counter (`+ Counter (A/N)`) — только у Text и Text Area.
3. Существующие публикуемые `Field / Vertical`, `Field / Horizontal`, `Field / Password` и др. в файле компонентов после перехода скрываются от публикации (префикс `_` или `hiddenFromPublishing`) — это меняет актуальный файл и делается только по решению автора.
