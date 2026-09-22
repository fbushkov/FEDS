"""FEDS: описания сборки Checkbox и Radiobutton — повтор устройства из файла «Компоненты · Базовые»
по имени токенов библиотеки (эталон — библиотека, docs/build-rules.md).

Отличия от файла (решения автора 22.09.2026):
- без вшитого Avatar: слот Avatar и свойство Avatar убраны (аватар рядом с выбором — композиция, а не часть контрола);
- Loading — экземпляры Skeleton / Line вместо полос с числовыми размерами («Загрузка = Skeleton»);
- отступы текста — токены библиотеки `text-container-*` вместо устаревшего `checkbox/size/M/name_container-Y-top`;
- тень карточки не собирается: эффект-стили не проработаны.

Используется из tools/gen_build.py.
"""

STATES = ["Default", "Hover", "Pressed", "Disabled", "Loading"]
SIZES = ["M", "L"]
INV = {"from": "Inverse", "map": {"False": "", "True": "inverse-"}}
# межстрочный интервал текста → высота Skeleton / Line (M: 20 и 20; L: имя 24, описание 20)
SK_NAME = {"M": "M", "L": "L"}
SK_DESC = {"M": "M", "L": "M"}

KIND = {
    "checkbox": {
        "title": "Checkbox", "set": "Checkbox", "gap": "checkbox-text-gap",
        "box_pad_off": ("box-icon-x", "box-icon-y", "box-icon-y"),           # (x, top, bottom) без отметки
        "box_pad_on": ("box-check-y-top", "box-check-y-top", "box-check-y-bottom"),  # с отметкой (как в файле)
        "mark": "icon",
    },
    "radiobutton": {
        "title": "Radiobutton", "set": "Radio", "gap": "radio-text-gap",
        "box_pad_off": ("box-xy", "box-xy", "box-xy"),
        "box_pad_on": ("box-xy", "box-xy", "box-xy"),
        "mark": "dot",
    },
}

DESC = {
    "checkbox": ("Интерактивный элемент множественного выбора: любое количество независимых вариантов, подтверждение условия, "
                 "управление выбором дочерних элементов (Indeterminate)."),
    "radiobutton": "Выбор одного варианта из группы взаимоисключающих. Если можно выбрать несколько — Checkbox.",
}


def by(axis, mapping):
    return {"by": axis, "map": mapping}


def control_set(kind, side, size):
    k = KIND[kind]
    s = size.lower()
    z = f"{kind}/size/main/{s}"
    checkbox = kind == "checkbox"
    on = {"Checked": "True"}
    # отметка: Checked (и Indeterminate у Checkbox)
    axes = [{"name": "Checked", "values": ["False", "True"]}]
    if checkbox:
        axes.append({"name": "Indeterminate", "values": ["False", "True"]})
    axes += [{"name": "State", "values": STATES}, {"name": "Inverse", "values": ["False", "True"]}]
    exclude = [{"Checked": "False", "Indeterminate": "True"}] if checkbox else []

    def pad(which):
        x, top, bottom = k[which]
        return {"pl": f"{z}/{x}", "pr": f"{z}/{x}", "pt": f"{z}/{top}", "pb": f"{z}/{bottom}"}

    box_pad = {key: by("Checked", {"False": pad("box_pad_off")[key], "True": pad("box_pad_on")[key]}) for key in ("pl", "pr", "pt", "pb")}
    not_loading = {"State": ["Default", "Hover", "Pressed", "Disabled"]}
    if checkbox:
        mark = [
            {"type": "icon", "name": "check", "when": {**on, "Indeterminate": "False", **not_loading},
             "icon": {"name": "check", "size": f"{z}/icon", "color": f"{kind}/checked/{{i}}icon/{{st}}"}},
            {"type": "icon", "name": "minus", "when": {**on, "Indeterminate": "True", **not_loading},
             "icon": {"name": "minus", "size": f"{z}/icon", "color": f"{kind}/checked/{{i}}icon/{{st}}"}},
        ]
    else:
        mark = [{"type": "rect", "name": "Dot", "when": {**on, **not_loading}, "width": f"{z}/icon", "height": f"{z}/icon",
                 "radius": f"{z}/icon-radius", "fill": f"{kind}/checked/{{i}}icon/{{st}}"}]
    box = {
        "type": "frame", "name": k["title"] if kind == "checkbox" else "Radiobutton",
        "layout": {"dir": "V", **box_pad, "align": "CENTER", "counter": "CENTER", "w": "FIXED", "h": "FIXED"},
        "width": f"{z}/box", "height": f"{z}/box", "radius": f"{z}/box-radius",
        # Loading — заливка загрузки без рамки; остальное — по отметке и состоянию
        "fill": by("State", {**{st: f"{kind}/{{chk}}/{{i}}bg/{{st}}" for st in STATES[:4]}, "Loading": f"{kind}/loading/{{i}}box-{{lb}}"}),
        "stroke": {"color": by("State", {**{st: f"{kind}/{{chk}}/{{i}}border/{{st}}" for st in STATES[:4]}, "Loading": ""}),
                   "weight": f"{z}/box-border", "align": "INSIDE"},
        "children": mark,
    }
    error = [
        # Error / Mandatory: красная рамка поверх бокса и звёздочка справа (как в файле) — только без отметки
        {"type": "rect", "name": "Error", "when": {"Checked": "False", "State": ["Default", "Hover", "Pressed"]}, "abs": "focus",
         "offset": -2, "visible": False, "refs": {"visible": "Error / Mandatory"}, "radius": f"{z}/box-radius",
         "stroke": {"color": f"{kind}/unchecked/{{i}}border/error", "weight": f"{z}/box-border", "align": "INSIDE"}},
        {"type": "icon", "name": "*", "when": {"Checked": "False", "State": ["Default", "Hover", "Pressed"]}, "abs": "after", "offset": 1,
         "visible": False, "refs": {"visible": "Error / Mandatory"},
         "icon": {"name": "asterisk", "size": 6, "color": f"{kind}/unchecked/error"}},
    ]
    container = {
        "type": "frame", "name": "Container",
        "layout": {"dir": "H", "px": f"{z}/box-container-xy", "py": f"{z}/box-container-xy", "align": "CENTER", "counter": "CENTER", "w": "HUG", "h": "FIXED"},
        "height": f"{z}/box-container",
        "children": [
            box, *error,
            {"type": "rect", "name": "Focus Ring", "when": {"State": ["Default", "Hover", "Pressed", "Loading"]}, "abs": "focus", "offset": 1,
             "visible": False, "refs": {"visible": "Focused"}, "radius": f"{z}/focus-radius",
             "stroke": {"color": f"{kind}/focus-ring", "weight": f"{z}/focus-border", "align": "INSIDE"}},
        ],
    }
    text_style = lambda part: f"typography/action/{kind}/{s}/{part}"  # noqa: E731
    text = {
        "type": "frame", "name": "Text", "w": "FILL", "refs": {"visible": "Text"},
        "layout": {"dir": "V", "gap": f"{z}/text-interline-gap", "px": f"{z}/text-container-x", "py": f"{z}/text-container-y",
                   "align": "MIN", "counter": "MIN", "w": "FILL", "h": "HUG"},
        "children": [
            {"type": "text", "name": "Name", "when": not_loading, "refs": {"characters": "↳ Name"}, "w": "FILL",
             "text": {"chars": "Name", "style": text_style("name"), "fontStyle": "Regular", "fill": by("State", {**{st: f"{kind}/text/{{i}}name" for st in STATES}, "Disabled": f"{kind}/text/{{i}}disabled"}), "wrap": True}},
            {"type": "text", "name": "Description", "when": not_loading, "refs": {"visible": "Description", "characters": "↳ Description"}, "w": "FILL",
             "text": {"chars": "Description", "style": text_style("description"), "fontStyle": "Regular", "fill": by("State", {**{st: f"{kind}/text/{{i}}description" for st in STATES}, "Disabled": f"{kind}/text/{{i}}disabled"}), "wrap": True}},
            # Loading: Skeleton вместо текста
            {"type": "instance", "name": "Name", "when": {"State": "Loading"}, "width": 48,
             "instance": {"set": "Skeleton / Line", "variant": {"Size": SK_NAME[size], "Inverse": "{I}"}, "props": {}}},
            {"type": "instance", "name": "Description", "when": {"State": "Loading"}, "width": 72, "refs": {"visible": "Description"},
             "instance": {"set": "Skeleton / Line", "variant": {"Size": SK_DESC[size], "Inverse": "{I}"}, "props": {}}},
        ],
    }
    children = [container, text] if side == "Left" else [text, container]
    vars_ = {
        "i": INV, "I": {"from": "Inverse"},
        "st": {"from": "State", "case": "lower"},
        "chk": {"from": "Checked", "map": {"False": "unchecked", "True": "checked"}},
        "lb": {"from": "Checked", "map": {"False": "uncheked", "True": "checked"}},  # имя токена библиотеки (опечатка не чинится)
    }
    root = {
        "type": "frame", "name": "root",
        "layout": {"dir": "H", "gap": f"{z}/{k['gap']}", "align": "MIN", "counter": "MIN", "w": "FIXED", "h": "HUG"},
        "width": 160, "children": children,
    }
    return {
        "name": f"{k['set']} / {side} / {size}", "description": DESC[kind],
        "axes": axes, "exclude": exclude,
        "grid": {"columns": "State", "rows": [a["name"] for a in axes if a["name"] in ("Checked", "Indeterminate")], "split": "Inverse"},
        "a11y": {"exempt": {"State": "Loading"}, "reason": "Loading — скелетон вместо текста, читать нечего"},
        "vars": vars_,
        "props": [
            {"name": "Text", "type": "BOOLEAN", "default": True},
            {"name": "Description", "type": "BOOLEAN", "default": True},
            {"name": "↳ Name", "type": "TEXT", "default": "Name"},
            {"name": "↳ Description", "type": "TEXT", "default": "Description"},
            {"name": "Focused", "type": "BOOLEAN", "default": False},
            {"name": "Error / Mandatory", "type": "BOOLEAN", "default": False},
        ],
        "root": root,
    }


def card_set(kind):
    k = KIND[kind]
    z = f"{kind}/size/card"
    inner = {"Left": "Left", "Right": "Right", "Right+Icon": "Right"}
    variant = {"Checked": "False", **({"Indeterminate": "False"} if kind == "checkbox" else {}), "State": "Default", "Inverse": "{I}"}
    return {
        "name": f"{k['set']} / Card", "description": f"{k['title']} в карточке: вся карточка — активная область. Для выбора, которому нужна подробная подпись.",
        "axes": [{"name": "Type", "values": ["Left", "Right", "Right+Icon"]}, {"name": "Size", "values": ["L", "M"]},
                 {"name": "Inverse", "values": ["False", "True"]}],
        "exclude": [], "grid": {"columns": "Type", "rows": ["Size"], "split": "Inverse"},
        "vars": {"s": {"from": "Size", "case": "lower"}, "S": {"from": "Size"}, "i": INV, "I": {"from": "Inverse"},
                 "side": {"from": "Type", "map": inner}},
        "props": [{"name": "↳ Icon", "type": "INSTANCE_SWAP", "default": "circle"}],
        "root": {
            "type": "frame", "name": "root",
            "layout": {"dir": "V", "px": f"{z}/{{s}}/x", "pt": f"{z}/{{s}}/y-top", "pb": f"{z}/{{s}}/y-bottom",
                       "align": "MIN", "counter": "MIN", "w": "FIXED", "h": "HUG"},
            "width": 240, "radius": f"{z}/radius", "fill": f"{kind}/card/{{i}}bg",
            "stroke": {"color": f"{kind}/card/{{i}}border", "weight": f"{z}/border", "align": "INSIDE"},
            "children": [
                # Right+Icon: иконка сверху, текст начинается после отступа icon-text (в файле — абсолютная иконка)
                {"type": "frame", "name": "Icon", "when": {"Type": "Right+Icon"},
                 "layout": {"dir": "H", "align": "MIN", "counter": "MIN", "w": "HUG", "h": "FIXED"}, "height": f"{z}/{{s}}/icon-text",
                 "children": [{"type": "icon", "name": "Icon", "refs": {"mainComponent": "↳ Icon"},
                               "icon": {"name": "circle", "size": f"{z}/{{s}}/icon", "color": f"{kind}/card/{{i}}icon"}}]},
                {"type": "instance", "name": k["title"], "expose": True, "w": "FILL",
                 "instance": {"set": f"{k['set']} / {{side}} / {{S}}", "variant": variant, "props": {}}},
            ],
        },
    }


def selection(kind):
    k = KIND[kind]
    title = k["title"]
    base = f"{k['set']} / Left / M"
    checkbox = kind == "checkbox"

    def v(checked="False", st="Default", inv="False", ind="False"):
        x = {"Checked": checked, "State": st, "Inverse": inv}
        if checkbox:
            x["Indeterminate"] = ind
        return x

    def it(set_, variant, props=None, label=None, width=None):
        x = {"set": set_, "variant": variant}
        if props:
            x["props"] = props
        if label:
            x["label"] = label
        if width:
            x["width"] = width
        return x

    only_name = {"Description": False}
    logic = [("Unchecked", v()), ("Checked", v("True"))] + ([("Indeterminate", v("True", ind="True"))] if checkbox else [])
    spec = {
        "title": title, "description": DESC[kind],
        "columns": [
            {"title": "Логическое состояние", "width": 360, "cards": [
                {"title": n, "items": [it(base, x, only_name)]} for n, x in logic]},
            {"title": "Размер", "width": 360, "cards": [
                {"title": "M", "description": "Стандартный: формы, таблицы, фильтры, плотные списки", "items": [it(f"{k['set']} / Left / M", v("True"))]},
                {"title": "L", "description": "Крупная типографика, длинные подписи, увеличенная активная область", "items": [it(f"{k['set']} / Left / L", v("True"))]}]},
            {"title": "Направление", "width": 360, "cards": [
                {"title": "Left", "description": "Стандарт для форм, списков и фильтров", "items": [it(f"{k['set']} / Left / M", v("True"))]},
                {"title": "Right", "description": "Строки и списки с элементами управления справа", "items": [it(f"{k['set']} / Right / M", v("True"))]}]},
            {"title": "Конфигурация", "width": 360, "cards": [
                {"title": "Текст", "items": [it(base, v("True"), only_name)]},
                {"title": "Текст + описание", "items": [it(base, v("True"))]},
                {"title": "Без видимого текста", "description": "Только в таблицах, когда контекст задан строкой или колонкой", "items": [it(base, v("True"), {"Text": False})]}]},
            {"title": "Состояния", "width": 360, "cards": [
                {"title": "Mouse", "items": [it(base, v("True", st), only_name, st) for st in ["Default", "Hover", "Pressed", "Disabled"]]},
                {"title": "Keyboard", "items": [it(base, v("True"), {**only_name, "Focused": True}, "Focused")]},
                {"title": "Loading", "description": "Значение загружается: Skeleton вместо подписи, взаимодействие недоступно", "items": [it(base, v("False", "Loading"))]},
                {"title": "Error / Mandatory", "description": "Обязательный выбор не сделан — после проверки формы", "items": [it(base, v(), {**only_name, "Error / Mandatory": True})]}]},
            {"title": "Карточка", "width": 360, "cards": [
                {"title": t, "items": [it(f"{k['set']} / Card", {"Type": t, "Size": "M", "Inverse": "False"})]} for t in ["Left", "Right", "Right+Icon"]]},
            {"title": "Инверсия", "width": 360, "cards": [
                {"title": "Inverse", "description": "На тёмных поверхностях — светлые inverse-токены", "inverse": True,
                 "items": [it(base, v("True", inv="True")), it(base, v(inv="True")), it(f"{k['set']} / Card", {"Type": "Left", "Size": "M", "Inverse": "True"})]}]},
        ],
    }
    sets = [control_set(kind, side, size) for side in ("Left", "Right") for size in SIZES] + [card_set(kind)]
    return {
        "component": kind, "title": title, "page": f"Components / {title}", "origin": "existing",
        "requires": ["skeleton"],
        "notes": [
            f"Повтор {title} из файла «Компоненты · Базовые»: Left / Right × M / L и Card, оси и свойства как в файле, имена токенов — библиотеки.",
            "Без вшитого Avatar (решение автора 22.09.2026): аватар рядом с выбором — композиция, а не часть контрола.",
            "Loading — экземпляры Skeleton / Line вместо полос с числовыми размерами («Загрузка = Skeleton»).",
            "Error / Mandatory — рамка ошибки поверх бокса и звёздочка (иконка asterisk), только у неотмеченного варианта, как в файле.",
            "Тень карточки не собирается: эффект-стили не проработаны (решение автора).",
        ],
        "sets": sets,
        "spec": spec,
    }
