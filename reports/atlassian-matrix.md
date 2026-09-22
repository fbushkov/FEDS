# FEroom ↔ Atlassian Design System: матрица соответствий

Сверка по конструктиву (части, поведение, назначение), а не по названиям. Источник: каталог atlassian.design/components (21.09.2026); наш список — 13 готовых компонентов (файл «Компоненты · Базовые»), поля ввода из `input/builds`, 12 компонентов backlog и 6 пресетов полей.

Условные обозначения: **=** совпадает по конструктиву · **≈** совпадает частично (см. комментарий) · **—** нет аналога.

## 1. Совпадают по конструктиву, но называются иначе

| FEroom | Atlassian | Совпадение | Что взять из Atlassian |
|---|---|---|---|
| **Alert** | Flag + Section message | ≈ | Сделано 21.09: виды Subtle / Default / Bold, сворачивание Bold, группа уведомлений, правила закрытия и таймера |
| **Hint** | Spotlight (Onboarding) | = | Шаги тура («1 из 3»), затемнение вокруг якоря (Blanket), кнопки «Далее / Пропустить» |
| **Status** | Lozenge | = | Два веса (subtle / bold) = наши soft / hard; максимальная длина и обрезка |
| **Badge** (цветные метки с иконкой) | Tag (цветной) · Lozenge | ≈ | У Atlassian Badge — только числовой счётчик; наш Badge ближе к Tag. Счётчик у нас — Counter внутри Chip и Field |
| **Chip** | Tag + Tag group | ≈ | Tag group: раскладка и перенос набора меток; удаляемый Tag = наш Chip с X-icon |
| **Switch** | Toggle | = | Размеры regular / large, иконки в ползунке |
| **Radiobutton** | Radio (Radio group) | = | Группа как отдельная сущность с общим Label и ошибкой |
| **Input · Search · Password · Number** | Text field (типы) | ≈ | У Atlassian это один Text field с элементами до и после; у нас — отдельные наборы на общих токенах `field/*` |
| **Field** | Form (Field, Label, Helper, Error) | = | Form: группы полей, обязательные поля, сводка ошибок |
| **Select** (SimpleSelect) · **Multiselect** · **Combobox** | Select (single, multi, searchable, async) | ≈ | У Atlassian один компонент с режимами; у нас три — это нормально, общий слой — Dropdown |
| **Dropdown** | Dropdown menu · Menu | = | Menu как самостоятельный список действий; группы и разделители пунктов |
| **Popover** | Popup · Inline dialog | = | Popup — базовый слой для всех всплывающих (Dropdown, Hint, Popover) |
| **Tooltip** | Tooltip | = | Задержка показа, позиционирование |
| **Banner** | Banner | = | Виды warning / error / announcement; закрепление сверху |
| **Skeleton** | Skeleton | = | — |
| **Breadcrumbs** | Breadcrumbs | = | Сворачивание середины в «…» |
| **Link** | Link · Anchor | = | — |
| **Avatar** (в т. ч. группа) | Avatar · Avatar group | = | Avatar group: стопка / сетка, «+N» |
| **Button** (Filled, Outline, Text, Icon) | Button · Icon button · Split button | = | Split button (кнопка + меню) у нас нет |
| **Accordion** | — (в ADS нет; Expand в Confluence) | — | — |
| **Divider** | — (в ADS разделитель — свойство Box) | — | — |
| **Priority Indicator** | — (иконки приоритета Jira) | — | — |
| **Focus** (часть каждого контрола) | Focus ring | = | У нас — слой Focus Ring в каждом компоненте, отдельного компонента не нужно |
| Спиннер внутри Button / Select | Spinner | ≈ | Самостоятельного Spinner у нас нет (см. раздел 3) |

## 2. Наши компоненты, которых нет в ADS
Accordion, Divider, Priority Indicator, Number Input, Password Input, Search Input (в ADS — режимы Text field), Chip как фильтр-метка.

## 3. Не учтены в нашем списке (есть в ADS)

| Компонент ADS | Тип у нас | Зачем | Приоритет |
|---|---|---|---|
| Modal dialog + Blanket | компонент + служебный слой | Задачи, требующие ответа; упоминается в документах Alert, Hint, Popover | Высокий |
| Tabs | компонент | Переключение разделов страницы | Высокий |
| Spinner | компонент | Ожидание без известной структуры (страница, модальное окно) — правило загрузки уже на него ссылается | Высокий |
| Empty state | блок | Нет данных; упоминается в документе Alert | Высокий |
| Progress bar | компонент | Прогресс системного процесса | Средний |
| Pagination | компонент | Большие списки и таблицы | Средний |
| Table · Dynamic table · Table tree | блоки | Данные: сортировка, пагинация, вложенность | Средний |
| Menu (самостоятельный) | компонент | Список действий вне Select; основа Dropdown | Средний |
| Date time picker + Calendar | компоненты | Выбор даты и времени | Средний |
| Progress tracker · Progress indicator | компоненты | Шаги мастера (Stepper) и точки карусели | Средний |
| Drawer · Panel | блоки | Боковые панели | Средний |
| Page header · Heading | блок · типографика | Заголовок страницы с хлебными крошками и действиями | Средний |
| Inline message | компонент | Иконка-триггер с коротким сообщением по клику | Низкий |
| Inline edit | компонент | Чтение и правка на месте | Низкий |
| Range (Slider) | компонент | Выбор значения на шкале | Низкий |
| Tag group | блок | Раскладка набора Chip | Низкий |
| Comment | блок | Обсуждения | Низкий |
| Code | компонент | Фрагменты кода в тексте | Низкий |
| Date label | компонент | Дата со статусом (просрочено, скоро) | Низкий |
| Tile · Object · Logo · Image | медиа | Представление сущностей и брендов | Низкий |
| Navigation system / Side navigation | блок | Навигация приложения | По задаче продукта |

## 4. Как пользоваться матрицей
- Новый компонент собирается по модели `docs/build-rules.md` 2b: токены FEroom → композиция по ADS (части, виды, поведение) → документация → правила сборки и проверки.
- Название берём наше (Alert, Hint, Status), конструктив — от аналога ADS.
- Если аналог ADS шире (как Flag), расширяем свойства существующего компонента (Appearance), а не заводим второй компонент.
