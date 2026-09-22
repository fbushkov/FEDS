# Формат пресета токенов: `presets/{component}.tokens.json`

Один файл на компонент. Плагин FEDS читает эти файлы, строит дифф с файлом Figma и дописывает токены. Проверка: `python tools/feds_tokens.py validate presets/{component}.tokens.json` (отчёт в `reports/{component}-tokens.md`).

```jsonc
{
  "component": "tooltip",            // корень L3, kebab-case
  "roots": ["tooltip"],              // корни L3, которые пресет может создавать (по умолчанию [component]);
                                     // для семейства полей: "component": "field-combobox", "roots": ["field"]
  "title": "Tooltip",                // имя для Figma (Title Case)
  "kind": "component",               // component | block
  "analog": "badge",                 // ближайший готовый компонент, чью грамматику повторяем
  "source": "input/backlog/tooltip.md",
  "origin": "new",                   // new — новый компонент; existing — снят с текущей системы
  "prefixes": ["tooltip/"],          // необязательно: явные префиксы L3 пресета (для поиска «лишних»)

  "axes":   { "Size": ["M", "S"], "Inverse": ["False", "True"] },  // оси будущего компонента (для сборки)
  "parts":  ["container", "text", "tail"],                           // части анатомии

  "l2": [                            // НОВЫЕ переменные `2. General` (только если в системе нет подходящих)
    {
      "name": "space/tooltip/x",
      "type": "FLOAT",               // COLOR | FLOAT
      "scopes": ["GAP"],
      "values": { "light": "space/8", "dark": "space/8" },   // имя примитива L1; число — только с записью в exceptions
      "description": "Tooltip — горизонтальный отступ контейнера"
    }
  ],

  "l3": [                            // переменные `3. Components`, каждая — алиас на L2
    {
      "name": "tooltip/bg",
      "type": "COLOR",
      "alias": "color/bg/raised/inverse-main",   // имя существующей L2 или L2 из блока "l2"
      "scopes": ["FRAME_FILL"],
      "description": "Tooltip — фон контейнера"
    }
  ],

  "textStyles": [                    // текстовые стили, если их нет в файле
    {
      "name": "typography/tooltip/text",
      "fontFamily": "Roboto",
      "fontStyle": "Regular",        // Regular | Medium | SemiBold | Bold — должно совпадать с weight
      "vars": {
        "fontSize": "typography/tooltip/text/size",
        "lineHeight": "typography/tooltip/text/line-height",
        "letterSpacing": "typography/tooltip/text/letter-spacing",
        "fontWeight": "typography/tooltip/text/weight"
      }
    }
  ],

  "contrast": [                      // пары для проверки контраста в light и dark
    { "fg": "tooltip/text", "bg": "tooltip/bg", "kind": "text" }            // text ≥ 4.5, graphic ≥ 3
  ],

  "exceptions": [                    // отступления от правил: L3 → L1, сырое значение в L2
    { "token": "size/tooltip/max-width", "reason": "в L1 нет size/320" }
  ],

  "decisions": ["Почему выбрана та или иная семантика; расхождения с документацией"]
}
```

## Правила

1. **Грамматика FEroom — закон.** Документация в `input/backlog/*.md` писалась под другую схему (`space/overlay/*`, `typography/body/small`, «inverse-токенов нет»). Из неё берутся только **значения, части, состояния и поведение**. Имена строятся по `analysis/token-architecture.md`.
2. **Цвет L3** — только алиас на существующую семантику `color/*` L2. Новый цвет в L2 — крайний случай с обоснованием в `decisions`.
3. **Размеры** — новые L2 по грамматике `{size|space|gap|radius|border}/{component}/…` → примитив L1. Если в системе уже есть L2 с тем же смыслом и значением у аналога, **всё равно** создаётся свой L2 компонента (так устроены все 12 готовых компонентов).
4. **Типографика** — L2 `typography/{component}/{size?}/{slot}/{size|line-height|letter-spacing|weight}` → `font/*` L1, плюс текстовый стиль. Имя стиля: `typography/action/{component}/…` для интерактивных, `typography/{component}/…` для остальных. L3 для типографики не создаётся.
5. **Инверсия** — как у аналога: вариант `inverse`, сегмент `*-inverse` или часть `inverse-*`; алиасы на `inverse-*` L2.
6. **Scopes** — ровно один по таблице `analysis/figma-conventions.md` (у L3 цвета — по части: bg → FRAME_FILL, text → TEXT_FILL, icon → SHAPE_FILL, border → STROKE_COLOR).
7. **Эффекты и тени** — не создаём (решение автора), в `decisions` указываем, какой эффект-стиль понадобится.
8. **codeSyntax** — не заполняем.

## Пресеты базы и готовых компонентов

`presets/_system.tokens.json` и пресеты 13 готовых компонентов генерирует `python tools/extract_presets.py` из `input/tokens/variables.json`. Вручную их не правят. У базы есть блок `"l1"`: `{ name, type, value, scopes, hidden }`, где `value` — `#rrggbb`, `rgba(r,g,b,a)` или число. Зависимости между пресетами (`requires`) плагин вычисляет сам по ссылкам L3 → L2 → L1.
