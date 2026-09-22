# FEDS — что куда положить

Правила проекта — [CLAUDE.md](CLAUDE.md). ТЗ — [docs/TZ.md](docs/TZ.md).

## Заполняете вы (`input/`)

| Папка | Что положить | Формат и имена |
|---|---|---|
| `input/tokens/` | Экспорт переменных. `variables.json` уже лежит. Если есть экспорт со scopes/codeSyntax, текстовые и эффект-стили — сюда же. | `variables.json`, `text-styles.json`, `effect-styles.json` |
| `input/docs/` | Документация готовых компонентов — одна папка на компонент. | `input/docs/button/button.md` (+ картинки рядом) |
| `input/specs/` | Спецификации готовых компонентов: скриншоты фреймов спецификации (анатомия, размеры, отступы, состояния), при наличии — текст. | `input/specs/button/01-anatomy.png`, `02-sizes.png`… |
| `input/builds/` | Сборки: скриншоты component set, панели свойств (пропсы), слоёв, auto layout; по возможности — скриншот с выделенными переменными на слое. | `input/builds/button/variants.png`, `props.png`, `layers.png` |
| `input/figma-exports/` | Необязательно: ссылка на файл Figma, JSON-выгрузки узлов, `.fig`. | любой |
| `input/backlog/` | Новые компоненты и блоки, которые нужно создать. Список по приоритету — в `backlog.md`, материалы — в папке компонента (см. ниже). | `input/backlog/backlog.md` + `input/backlog/{component}/…` |
| `input/conventions/` | Правила, которых нет в файле: как называете варианты, порядок пропсов, правила страниц, ревью. | `.md` |

Папки компонентов (13, по страницам Figma): `avatar`, `badge`, `button`, `checkbox`, `chip`, `divider`, `link`, `priority-indicator`, `radiobutton`, `status`, `switch`, `field` (страница «Input, Text Area, Field»), `simple-select`.

### Новый компонент: `input/backlog/{component}/`

`{component}` — имя в kebab-case, как будущий корень токена (`tabs`, `tooltip`, `multiselect`). Для семейства полей ввода — `field-{подкомпонент}`: токены пойдут в `field/{подкомпонент}/…`.

```
input/backlog/{component}/
├── docs.md       — документация, черновик или готовая (по структуре input/docs/*)
├── spec/         — спецификация: скриншоты или .md, если уже есть
├── refs/         — референсы, наброски, скриншоты из продукта и аналогов
└── notes.md      — что известно: варианты, состояния, размеры, где используется
```

Обязательно только `docs.md` или `notes.md`. Всё остальное — если есть.

## Заполняют агенты

| Папка | Содержимое |
|---|---|
| `analysis/` | Разбор системы: `token-architecture.md`, `token-report.md`, `token-index.json`, паттерны компонентов |
| `presets/` | JSON-пресеты компонентов (F2) |
| `contracts/` | Контракты `.md` (F5) |
| `specs-out/` | Спецификации новых компонентов (F6) |
| `plugin/` | Код плагина (фаза 3) |
| `reports/` | Отчёты QA, диффы токенов |
| `tools/` | Скрипты: `analyze_tokens.py` |
