# Аудит контраста по токенам (FEDS)

Режимы: light, dark. Текст ≥ 4.5, иконки ≥ 3. Disabled не проверяется. Эвристика по грамматике L3 (`tools/audit_contrast.py`).

Нарушений: **0**

| Компонент | Токен | Режим | Контраст | Нужно | L2 сейчас | Фон |
|---|---|---|---|---|---|---|

## Проверено вручную (эвристика берёт не тот фон)

| Токен | Режим | Причина |
|---|---|---|
| `avatar/button-x/icon` | dark | кнопка-крестик на подложке аватара, не на поверхности |
| `avatar/status/text` | dark | текст статуса на цветной точке аватара |
| `avatar/button-x/icon` | light | кнопка-крестик на подложке аватара, не на поверхности |
| `avatar/status/text` | light | текст статуса на цветной точке аватара |
| `checkbox/loading/icon` | dark | декоративный трек спиннера; бегущая часть — отдельный токен |
| `checkbox/loading/icon` | light | декоративный трек спиннера; бегущая часть — отдельный токен |
| `radiobutton/loading/icon` | dark | декоративный трек спиннера |
| `radiobutton/loading/icon` | light | декоративный трек спиннера |
| `status/loading/icon` | dark | декоративный трек спиннера |
| `status/loading/icon` | light | декоративный трек спиннера |
| `switch/on/icon/default` | dark | иконка на ползунке (knob), а не на треке |
| `switch/off/icon/pressed` | dark | иконка на ползунке (knob), а не на треке |
| `switch/on/icon/hover` | dark | иконка на ползунке (knob), а не на треке |
| `switch/on/icon/pressed` | light | иконка на ползунке (knob), а не на треке |
| `switch/on/icon/hover` | light | иконка на ползунке (knob), а не на треке |
| `switch/on/icon/default` | light | иконка на ползунке (knob), а не на треке |
| `switch/off/icon/pressed` | light | иконка на ползунке (knob), а не на треке |
