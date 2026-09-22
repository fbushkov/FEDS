"""FEDS: описания сборки и спецификации (presets/{component}.build.json) по правилу docs/build-rules.md.

Button — повтор текущей сборки из файла «Компоненты · Базовые» (6 наборов, 924 варианта).
Alert — новый компонент, собранный по тому же правилу.

Запуск: python tools/gen_build.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_selection import selection  # noqa: E402
from gen_avatar import avatar  # noqa: E402
from gen_chip import chip  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def by(axis, mapping):
    return {"by": axis, "map": mapping}


# ---------------------------------------------------------------- Button
SIZES = ["XL", "L", "M", "S"]
STATES = ["Default", "Hover", "Pressed", "Disabled"]
FILL_TYPES = ["Primary", "Secondary", "Primary-soft", "Ghost", "Danger", "Danger-soft"]
AXES_TAIL = [{"name": "State", "values": STATES}, {"name": "Loading", "values": ["False", "True"]}]
EXCLUDE = [{"State": "Disabled", "Loading": "True"}]
GRID = {"columns": "Type", "blocks": "Size", "rows": ["Loading", "State"]}
LOADING_OPACITY = by("Loading", {"False": 1, "True": 0})
FOCUS_BIG = by("Size", {"XL": 4, "L": 4, "M": 3, "S": 3})
BASE_VARS = {"s": {"from": "Size", "case": "lower"}, "t": {"from": "Type", "case": "lower"}, "st": {"from": "State", "case": "lower"}}
DESC = ("Кнопка инициирует действие пользователя. Это самый частый интерактивный элемент — критично использовать её "
        "последовательно по всему продукту, чтобы пользователь понимал приоритет и тип действия.")


def focus_ring(offset):
    return {"type": "rect", "name": "Focus Ring", "when": {"State": ["Default", "Hover", "Pressed"]}, "abs": "focus",
            "offset": offset, "visible": False, "refs": {"visible": "Focused"},
            "radius": "button/size/{s}/radius-focus",
            "stroke": {"color": "button/focus-ring", "weight": "button/size/{s}/border-focus", "align": "INSIDE"}}


def icon(name, prop_icon, prop_visible, color, opacity=LOADING_OPACITY):
    refs = {"mainComponent": prop_icon}
    if prop_visible:
        refs["visible"] = prop_visible
    return {"type": "icon", "name": name, "icon": {"name": "circle", "size": "button/size/{s}/icon", "color": color},
            "refs": refs, "opacity": opacity}


def label_set(name, kind, types, sizes, focus, extra_vars=None, icon_color=None):
    """Наборы с подписью: Filled, Outline, Text."""
    k = sizes
    icon_color = icon_color or f"button/{kind}/{{t}}/icon/{{st}}"
    text_color = f"button/{kind}/{{t}}/text/{{st}}"
    root = {
        "type": "frame", "name": "root",
        "layout": {"dir": "H", "gap": f"button/size/{{s}}/{k['gap']}", "px": f"button/size/{{s}}/{k['x']}",
                   "py": f"button/size/{{s}}/{k['y']}", "align": "CENTER", "counter": "CENTER", "w": "HUG", "h": "HUG"},
        "radius": f"button/size/{{s}}/{k['radius']}",
        "fill": f"button/{kind}/{{t}}/bg/{{st}}",
        "stroke": {"color": f"button/{kind}/{{t}}/border/{{st}}", "weight": f"button/size/{{s}}/{k['border']}", "align": "INSIDE"},
        "children": [
            focus_ring(focus),
            icon("Left Icon", "↳ Icon L", "Left Icon", icon_color),
            {"type": "text", "name": "Действие", "refs": {"characters": "Label"}, "opacity": LOADING_OPACITY,
             "text": {"chars": "Действие", "style": "typography/action/button/{s}", "fill": text_color, "truncate": True}},
            icon("Right Icon", "↳ Icon R", "Right Icon", icon_color),
            {"type": "icon", "name": "Loading", "when": {"Loading": "True", "State": "Default"}, "abs": "center",
             "icon": {"name": "loader", "size": "button/size/{s}/icon", "color": icon_color}},
            {"type": "frame", "name": "Cancel", "when": {"Loading": "True", "State": ["Hover", "Pressed"]}, "abs": "stretch-x",
             "layout": {"dir": "H", "gap": f"button/size/{{s}}/{k['gap']}", "pl": "button/size/{s}/x-icon-button",
                        "pr": "button/size/{s}/x-icon-button", "align": "CENTER", "counter": "CENTER", "w": "FIXED", "h": "HUG"},
             "children": [
                 {"type": "icon", "name": "Cancel", "icon": {"name": "x", "size": "button/size/{s}/icon", "color": icon_color}},
                 {"type": "text", "name": "Отменить",
                  "text": {"chars": "Отменить", "style": "typography/action/button/{s}", "fill": text_color, "truncate": True}},
             ]},
        ],
    }
    if k.get("box"):
        root["height"] = "button/size/{s}/box"
    return {
        "name": name, "description": DESC,
        "axes": [{"name": "Size", "values": SIZES}, {"name": "Type", "values": types}, *AXES_TAIL],
        "exclude": EXCLUDE,
        "grid": {**GRID, **({"split": {"axis": "Type", "values": [t for t in types if t.startswith("Inverse")]}} if any(t.startswith("Inverse") for t in types) else {})},
        "vars": {**BASE_VARS, **(extra_vars or {})},
        "props": [
            {"name": "Label", "type": "TEXT", "default": "Действие"},
            {"name": "Left Icon", "type": "BOOLEAN", "default": True},
            {"name": "Right Icon", "type": "BOOLEAN", "default": True},
            {"name": "↳ Icon L", "type": "INSTANCE_SWAP", "default": "circle"},
            {"name": "↳ Icon R", "type": "INSTANCE_SWAP", "default": "circle"},
            {"name": "Focused", "type": "BOOLEAN", "default": False},
        ],
        "root": root,
    }


def icon_set(name, fill, icon_color, types, sizes, focus, stroke_color=None, vars_=None):
    """Наборы только с иконкой: Icon - Filled, Icon - Outline, Icon Only."""
    k = sizes
    root = {
        "type": "frame", "name": "root",
        "layout": {"dir": "H", "gap": f"button/size/{{s}}/{k['gap']}", "px": f"button/size/{{s}}/{k['x']}",
                   "py": f"button/size/{{s}}/{k['y']}", "align": "CENTER", "counter": "CENTER", "w": "HUG", "h": "HUG"},
        "radius": f"button/size/{{s}}/{k['radius']}", "fill": fill,
        "stroke": {"weight": f"button/size/{{s}}/{k['border']}", "align": "INSIDE", **({"color": stroke_color} if stroke_color else {})},
        "children": [
            focus_ring(focus),
            icon("Icon", "↳ Icon", None, icon_color),
            {"type": "icon", "name": "Loading", "when": {"Loading": "True", "State": "Default"}, "abs": "center",
             "icon": {"name": "loader", "size": "button/size/{s}/icon", "color": icon_color}},
            {"type": "icon", "name": "Cancel", "when": {"Loading": "True", "State": ["Hover", "Pressed"]}, "abs": "center",
             "icon": {"name": "x", "size": "button/size/{s}/icon", "color": icon_color}},
        ],
    }
    if k.get("box"):
        root["height"] = "button/size/{s}/box"
    return {
        "name": name, "description": DESC,
        "axes": [{"name": "Size", "values": SIZES}, {"name": "Type", "values": types}, *AXES_TAIL],
        "exclude": EXCLUDE,
        "grid": {**GRID, **({"split": {"axis": "Type", "values": [t for t in types if t.startswith("Inverse")]}} if any(t.startswith("Inverse") for t in types) else {})},
        "vars": {**BASE_VARS, **(vars_ or {})},
        "props": [
            {"name": "↳ Icon", "type": "INSTANCE_SWAP", "default": "circle"},
            {"name": "Focused", "type": "BOOLEAN", "default": False},
        ],
        "root": root,
    }


BOX = {"gap": "gap", "x": "x", "y": "y", "radius": "radius", "box": True}
TEXT = {"gap": "gap-text", "x": "x-text", "y": "y-text", "radius": "radius-text", "border": "border-text"}
ICON_BOX = {"gap": "gap", "x": "x-icon-button", "y": "y", "radius": "radius", "box": True}
ICON_ONLY_T = {"Primary": "primary", "Secondary": "secondary", "Tertiary": "tertiary", "Danger": "danger",
               "Inverse-primary": "inverse", "Inverse-secondary": "inverse"}
ICON_ONLY_IC = {"Primary": "primary/icon", "Secondary": "secondary/icon", "Tertiary": "tertiary/icon", "Danger": "danger/icon",
                "Inverse-primary": "inverse/icon/primary", "Inverse-secondary": "inverse/icon/secondary"}

# Inverse — вид кнопки для тёмных и насыщенных поверхностей (docs/build-rules.md 2.9): Filled — светлая заливка и тёмный текст,
# Outline — светлые рамка и текст, Text — только светлый текст. Им пользуются все компоненты с кнопками (Alert и др.).
FILL_TYPES_INV = [*FILL_TYPES, "Inverse"]
TEXT_TYPES = ["Primary", "Secondary", "Danger", "Inverse"]
TEXT_ICON = {"Primary": "primary/icon", "Secondary": "secondary/icon", "Danger": "danger/icon", "Inverse": "inverse/icon/primary"}

LBL = {"Label": "Сохранить изменения", "Left Icon": False, "Right Icon": False}


def item(set_, variant, props=None, label=None, width=None):
    x = {"set": set_, "variant": variant}
    if props:
        x["props"] = props
    if label:
        x["label"] = label
    if width:
        x["width"] = width
    return x


def v(size="XL", type_="Primary", state="Default", loading="False"):
    return {"Size": size, "Type": type_, "State": state, "Loading": loading}


def button_spec():
    type_desc = [("Primary", "Главное позитивное действие"), ("Primary-soft", "Важное позитивное действие"),
                 ("Secondary", "Альтернативное действие"), ("Ghost", "Дополнительное действие"),
                 ("Danger", "Необратимое действие"), ("Danger-soft", "Деструктивное действие")]
    size_desc = [("XL", "Не перегруженные интерфейсы"), ("L", "Основной вариант, для большинства интерфейсов"),
                 ("M", "Интерфейсы, где много информации и действий"), ("S", "Для секций в интерфейсах, где недостаточно пространства и много информации")]
    states = [("Default", "Default", "False"), ("Hover", "Hover", "False"), ("Pressed", "Pressed", "False"),
              ("Loading - Default", "Default", "True"), ("Loading - Hover", "Hover", "True"),
              ("Loading - Pressed", "Pressed", "True"), ("Disabled", "Disabled", "False")]
    focus_lists = []
    for s in SIZES:
        focus_lists.append({"title": s, "items": [
            item("Button / Filled", v(s), {**LBL, "Focused": True}, "Fill"),
            item("Button / Outline", v(s), {**LBL, "Focused": True}, "Outline"),
            item("Button / Text", v(s), {**LBL, "Focused": True}, "Text")]})
    return {
        "title": "Спецификация", "description": "Технические характеристики компонента",
        "columns": [
            {"title": "Вид", "cards": [
                {"title": "Fill", "description": "Главное действие", "items": [item("Button / Filled", v(), LBL)]},
                {"title": "Outline", "description": "Важное, но не главное действие", "items": [item("Button / Outline", v(), LBL)]},
                {"title": "Text", "description": "Второстепенные действия", "items": [item("Button / Text", v(), LBL)]}]},
            {"title": "Тип", "cards": [{"title": t.replace("-", " ").title().replace("Soft", "Soft"), "description": d,
                                          "items": [item("Button / Filled", v("XL", t), LBL)]} for t, d in type_desc]},
            {"title": "Размер", "cards": [{"title": s, "description": d, "items": [item("Button / Filled", v(s), LBL)]} for s, d in size_desc]},
            {"title": "Содержание", "cards": [
                {"title": "Текст", "items": [item("Button / Filled", v("L"), LBL)]},
                {"title": "Текст + иконка слева", "items": [item("Button / Filled", v("L"), {**LBL, "Left Icon": True})]},
                {"title": "Текст + иконка справа", "items": [item("Button / Filled", v("L"), {**LBL, "Right Icon": True})]},
                {"title": "Только иконка", "items": [item("Button / Icon - Filled", v("L"))]}]},
            {"title": "Corner Case", "cards": [
                {"title": "Default", "description": "Длинная подпись обрезается многоточием", "items": [item("Button / Filled", v("L"), LBL, width=140)]},
                {"title": "Loading", "description": "Отмена действия при наведении", "items": [item("Button / Filled", v("L", "Primary", "Hover", "True"), LBL, width=100)]}]},
            {"title": "Инверсия", "cards": [
                {"title": "Inverse", "inverse": True,
                 "description": "Тёмные и насыщенные поверхности: Filled — главное действие, Outline — альтернативное, Text — ссылки, «Назад», закрытие",
                 "items": [item("Button / Filled", v("L", "Inverse"), LBL, "Filled"), item("Button / Outline", v("L", "Inverse"), LBL, "Outline"),
                           item("Button / Text", v("L", "Inverse"), LBL, "Text")]}]},
            {"title": "Focus", "grid": 2, "cards": focus_lists},
            {"title": "Взаимодействие", "grid": 2, "cards": [
                {"title": "Mouse", "items": [item("Button / Filled", v("XL", "Primary", st, ld), LBL, lbl) for lbl, st, ld in states]},
                {"title": "Keyboard", "items": [item("Button / Filled", v("XL", "Primary", st, ld), {**LBL, "Focused": st != "Disabled"}, lbl) for lbl, st, ld in states]}]},
        ],
    }


def button():
    fill_focus = FOCUS_BIG
    return {
        "component": "button", "title": "Button", "page": "Components / Button", "origin": "existing",
        "notes": [
            "Повтор текущей сборки: 6 наборов, оси, свойства, слои и привязки как в файле «Компоненты · Базовые».",
            "Нормализовано: надпись «Отменить» использует стиль своего размера (в файле у всех размеров стоит XL).",
            "Иконке задаются ширина и высота через `button/size/{s}/icon` (в файле привязана только высота).",
            "Icon Only: типы Inverse-primary и Inverse-secondary стоят на тёмной правой части набора, как в файле.",
            "Новое: тип Inverse у Filled, Icon - Filled, Outline, Icon - Outline и Text — кнопки для тёмных и насыщенных поверхностей "
            "(Filled — светлая заливка и тёмный текст, Outline — светлые рамка и текст, Text — светлый текст). Стоят на тёмной правой части набора. "
            "Компоненты с кнопками используют эти типы, а не свои кнопки.",
        ],
        "sets": [
            label_set("Button / Filled", "fill", FILL_TYPES_INV, {**BOX, "border": "border-fill"}, fill_focus),
            icon_set("Button / Icon - Filled", "button/fill/{t}/bg/{st}", "button/fill/{t}/icon/{st}", FILL_TYPES_INV,
                     {**ICON_BOX, "border": "border-fill"}, fill_focus, "button/fill/{t}/border/{st}"),
            label_set("Button / Outline", "outline", FILL_TYPES_INV, {**BOX, "border": "border-outline"}, fill_focus),
            icon_set("Button / Icon - Outline", "button/outline/{t}/bg/{st}", "button/outline/{t}/icon/{st}", FILL_TYPES_INV,
                     {**ICON_BOX, "border": "border-outline"}, fill_focus, "button/outline/{t}/border/{st}"),
            label_set("Button / Text", "text-button", TEXT_TYPES, TEXT, 3, {"ti": {"from": "Type", "map": TEXT_ICON}},
                      "button/text-button/{ti}/{st}"),
            icon_set("Button / Icon Only", "button/text-button/{t}/bg/{st}", "button/text-button/{ic}/{st}",
                     list(ICON_ONLY_T), {**TEXT}, 3, None,
                     {"t": {"from": "Type", "map": ICON_ONLY_T}, "ic": {"from": "Type", "map": ICON_ONLY_IC}}),
        ],
        "spec": button_spec(),
    }


# ---------------------------------------------------------------- Alert
# Композиция по Atlassian Flag + Section message (docs/build-rules.md 2.8, input/backlog/alert.md «Вид»):
#   Subtle  — сообщение в потоке блока (тонированная подложка роли; бывший единственный вид Alert),
#   Default — карточка-уведомление (Flag default): нейтральная поверхность, иконка роли, закрытие, действия-ссылки,
#   Bold    — насыщенная заливка роли (Flag bold): не закрывается, сворачивается, действия — кнопки поверх заливки.
ROLES = ["Info", "Success", "Warning", "Error"]
ROLE_ICON = {"Info": "info", "Success": "circle-check", "Warning": "triangle-alert", "Error": "circle-alert"}
APPEARANCES = ["Subtle", "Default", "Bold"]


def _amap(fn):
    """Карта значений по (Appearance, Inverse, Role) для vars с тремя осями."""
    return {f"{a}|{i}|{r}": fn(a, i == "True", r.lower()) for a in APPEARANCES for i in ("False", "True") for r in ROLES}


def alert():
    size_to_button = {"M": "M", "S": "S"}
    inv = lambda i: "inverse-" if i else ""  # noqa: E731
    vars_ = {
        "s": {"from": "Size", "case": "lower"}, "S": {"from": "Size"},
        "ico": {"from": "Role", "map": ROLE_ICON},
        "bg": {"from": ["Appearance", "Inverse", "Role"], "map": _amap(
            lambda a, i, r: f"alert/bg/{inv(i)}{r}" if a == "Subtle" else f"alert/default/{inv(i)}bg" if a == "Default" else f"alert/bold/bg/{r}")},
        "bd": {"from": ["Appearance", "Inverse", "Role"], "map": _amap(
            lambda a, i, r: f"alert/border/{inv(i)}{r}" if a == "Subtle" else f"alert/default/{inv(i)}border" if a == "Default" else f"alert/bold/bg/{r}")},
        "ic": {"from": ["Appearance", "Inverse", "Role"], "map": _amap(
            lambda a, i, r: f"alert/bold/icon/{r}" if a == "Bold" else f"alert/icon/{inv(i)}{r}")},
        "tt": {"from": ["Appearance", "Inverse", "Role"], "map": _amap(
            lambda a, i, r: f"alert/bold/text/{r}" if a == "Bold" else f"alert/text/{inv(i)}title")},
        "td": {"from": ["Appearance", "Inverse", "Role"], "map": _amap(
            lambda a, i, r: f"alert/bold/description/{r}" if a == "Bold" else f"alert/text/{inv(i)}description")},
        # Действия — обычные кнопки системы (docs/build-rules.md 2.9): Subtle — Outline + Text, Default — ссылки Text.
        # На тёмной поверхности (Inverse) и на насыщенной заливке Bold — тип Inverse; на жёлтой заливке (Warning Bold)
        # белое не читается (WCAG), там обычные тёмные Secondary. Bold закрепляет светлую тему: заливка одна в обеих темах.
        "aset": {"from": "Appearance", "map": {"Subtle": "Outline", "Default": "Text", "Bold": "Text"}},
        "a1": {"from": ["Appearance", "Inverse", "Role"], "map": _amap(
            lambda a, i, r: ("Secondary" if r == "warning" else "Inverse") if a == "Bold"
            else "Inverse" if i else "Secondary" if a == "Subtle" else "Primary")},
        "a2": {"from": ["Appearance", "Inverse", "Role"], "map": _amap(
            lambda a, i, r: ("Secondary" if r == "warning" else "Inverse") if a == "Bold" else "Inverse" if i else "Secondary")},
        "exp": {"from": "Role", "map": {"Info": "Inverse-primary", "Success": "Inverse-primary", "Warning": "Secondary", "Error": "Inverse-primary"}},
        "chev": {"from": "Expanded", "map": {"True": "chevron-up", "False": "chevron-down"}},
    }

    def action(name, t, label, extra=None):
        return {"type": "instance", "name": name, "expose": True, **(extra or {}), "instance": {
            "set": "Button / {aset}" if name == "Action" else "Button / Text",
            "variant": {"Size": by("Size", size_to_button), "Type": t, "State": "Default", "Loading": "False"},
            "props": {"Label": label, "Left Icon": False, "Right Icon": False}}}
    root = {
        "type": "frame", "name": "root",
        "layout": {"dir": "H", "gap": "alert/size/{s}/icon-gap", "px": "alert/size/{s}/x", "py": "alert/size/{s}/y",
                   "align": "MIN", "counter": "MIN", "w": "FIXED", "h": "HUG"},
        "width": 480,
        "radius": "alert/size/{s}/radius", "fill": "{bg}",
        "theme": by("Appearance", {"Subtle": "", "Default": "", "Bold": "light"}),
        "stroke": {"color": "{bd}", "weight": "alert/size/{s}/border", "align": "INSIDE"},
        "children": [
            {"type": "icon", "name": "Icon", "icon": {"name": "{ico}", "size": "alert/size/{s}/icon", "color": "{ic}"}},
            {"type": "frame", "name": "Body", "layout": {"dir": "H", "gap": "alert/size/{s}/close-gap", "align": "MIN", "counter": "MIN", "w": "FILL", "h": "HUG"},
             "children": [
                 {"type": "frame", "name": "Content", "layout": {"dir": "V", "gap": "alert/size/{s}/actions-gap", "align": "MIN", "counter": "MIN", "w": "FILL", "h": "HUG"},
                  "children": [
                      {"type": "frame", "name": "Text", "layout": {"dir": "V", "gap": "alert/size/{s}/title-gap", "align": "MIN", "counter": "MIN", "w": "FILL", "h": "HUG"},
                       "children": [
                           {"type": "text", "name": "Title", "refs": {"visible": "Title", "characters": "↳ Title"}, "w": "FILL",
                            "text": {"chars": "Заголовок сообщения", "typography": "typography/alert/{s}/title", "fontStyle": "SemiBold", "fill": "{tt}", "wrap": True}},
                           {"type": "text", "name": "Description", "when": {"Expanded": "True"}, "refs": {"characters": "↳ Description"}, "w": "FILL",
                            "text": {"chars": "Текст сообщения: что произошло и что сделать дальше.", "typography": "typography/alert/{s}/description",
                                     "fontStyle": "Regular", "fill": "{td}", "wrap": True}},
                       ]},
                      {"type": "frame", "name": "Actions", "when": {"Expanded": "True"}, "refs": {"visible": "Actions"},
                       "layout": {"dir": "H", "gap": "alert/size/{s}/action-gap", "align": "MIN", "counter": "CENTER", "w": "HUG", "h": "HUG"},
                       "children": [action("Action", "{a1}", "Действие"),
                                    action("Second Action", "{a2}", "Подробнее", {"refs": {"visible": "Second Action"}})]},
                  ]},
                 # Subtle и Default закрываются; Bold не закрывается (важное сообщение), а сворачивается шевроном
                 {"type": "instance", "name": "Close", "when": {"Appearance": ["Subtle", "Default"]}, "refs": {"visible": "Close"}, "instance": {
                     "set": "Button / Icon Only",
                     "variant": {"Size": by("Size", size_to_button), "Type": by("Inverse", {"False": "Secondary", "True": "Inverse-secondary"}),
                                 "State": "Default", "Loading": "False"},
                     "props": {"↳ Icon": "icon:x"}}},
                 {"type": "instance", "name": "Expand", "when": {"Appearance": "Bold"}, "instance": {
                     "set": "Button / Icon Only",
                     "variant": {"Size": by("Size", size_to_button), "Type": "{exp}", "State": "Default", "Loading": "False"},
                     "props": {"↳ Icon": "icon:{chev}"}}},
             ]},
        ],
    }

    def av(role="Info", size="M", inverse="False", appearance="Subtle", expanded="True"):
        return {"Appearance": appearance, "Role": role, "Size": size, "Inverse": inverse, "Expanded": expanded}
    full = {"Title": True, "Actions": True, "Close": True}
    A = lambda values, props=full, width=480, **kw: {**item("Alert", values, props, width=width), **kw}  # noqa: E731
    spec = {
        "title": "Alert",
        "description": "Сообщение о результате или состоянии: в потоке блока (Subtle), карточкой-уведомлением (Default) или насыщенной плашкой для важного (Bold). Роль передаётся иконкой, цветом и текстом — не только цветом.",
        "columns": [
            {"title": "Вид", "width": 560, "cards": [
                {"title": "Subtle", "description": "В потоке блока: форма, карточка, панель. Остаётся, пока причина не исчезла. Закрывается, если сообщение не критично",
                 "items": [A(av("Info"))]},
                {"title": "Default", "description": "Уведомление о событии поверх интерфейса, в группе справа или слева снизу. Нейтральная карточка, иконка роли, закрытие, действия — ссылки",
                 "items": [A(av("Success", appearance="Default"))]},
                {"title": "Bold", "description": "Важное: успех, предупреждение, ошибка, загрузка. Не закрывается, пока причина не устранена; дополнительный текст раскрывается",
                 "items": [A(av("Error", appearance="Bold"))]}]},
            {"title": "Роль", "width": 560, "cards": [
                {"title": r, "description": d, "items": [A(av(r, appearance="Bold"))]} for r, d in
                [("Info", "Дополнительная информация, не требующая действия; также загрузка"),
                 ("Success", "Действие завершено; предложите открыть созданное"),
                 ("Warning", "До действия со значительными последствиями. Не скрывается сам. Текст тёмный: белый на жёлтом не читается"),
                 ("Error", "Что-то пошло не так: объясните, что случилось и что сделать. Не скрывается сам")]]},
            {"title": "Раскрытие", "width": 560, "cards": [
                {"title": "Свёрнут", "description": "Только заголовок и шеврон: не перегружает экран", "items": [A(av("Warning", appearance="Bold", expanded="False"))]},
                {"title": "Раскрыт", "description": "Текст и до двух действий", "items": [A(av("Warning", appearance="Bold"))]}]},
            {"title": "Размер", "width": 560, "cards": [
                {"title": "M", "description": "Стандартный: форма, основная колонка, уведомления", "items": [A(av("Info", "M"))]},
                {"title": "S", "description": "Плотное окружение: карточка, строка таблицы, popover", "items": [A(av("Info", "S"), width=400)]}]},
            {"title": "Содержание", "width": 560, "cards": [
                {"title": "Только заголовок", "description": "Заголовок обязателен и кратко называет причину", "items": [A(av(appearance="Default"), {"Actions": False, "Close": True})]},
                {"title": "Заголовок + текст", "items": [A(av(), {"Title": True, "Actions": False, "Close": True})]},
                {"title": "С действиями", "description": "Не больше двух действий; подпись говорит, куда ведёт («Права доступа», а не «Подробнее»)",
                 "items": [A(av(appearance="Default"), {"Title": True, "Actions": True, "Second Action": True, "Close": True})]}]},
            {"title": "Группа", "width": 560, "cards": [
                {"title": "Стопка уведомлений", "description": "Новое сверху; после закрытия поднимается следующее. Закрываемые и незакрываемые в одной стопке не смешиваются",
                 "items": [A(av("Success", appearance="Default"), {"Actions": False, "Close": True}),
                           A(av("Info", appearance="Default"), {"Actions": False, "Close": True}),
                           A(av("Info", appearance="Default"), {"Actions": False, "Close": True})]}]},
            {"title": "Инверсия", "width": 560, "cards": [
                {"title": "Inverse", "description": "Subtle и Default на тёмных поверхностях. Bold — насыщенный на любой поверхности", "inverse": True,
                 "items": [A(av("Info", inverse="True")), A(av("Error", inverse="True")), A(av("Success", inverse="True", appearance="Default"))]}]},
            {"title": "Загрузка", "width": 560, "cards": [
                {"title": "Загрузка действия", "description": "После нажатия в Loading переходит только кнопка действия; иконка роли, текст и закрытие статичны",
                 "items": [A(av("Info"), nested={"Action": {"Loading": "True"}})]}]},
            {"title": "Corner Case", "width": 560, "cards": [
                {"title": "Длинный текст", "description": "Заголовок и текст переносятся; очень длинное сообщение — ссылка на страницу, Banner или Modal",
                 "items": [A(av("Warning", appearance="Bold"), {**full, "↳ Description": "У двух участников нет доступа к проекту. Они не увидят изменения, пока администратор не выдаст права. Запросите доступ или удалите участников из списка."})]}]},
        ],
    }
    return {
        "component": "alert", "title": "Alert", "page": "Components / Alert", "origin": "new",
        "requires": ["button"],
        "notes": [
            "Композиция по Atlassian Flag и Section message: Appearance Subtle (в потоке), Default (карточка-уведомление, закрывается), Bold (насыщенная, не закрывается, сворачивается).",
            "Alert неинтерактивен: у него нет Hover, Pressed, Focus и своей загрузки — состояния у кнопок внутри. Skeleton в Alert не входит.",
            "Действия — кнопки системы (Subtle: Outline + Text; Default: ссылки Text Primary и Secondary). На тёмной поверхности и на заливке Bold — тип Inverse (Outline Inverse, Text Inverse, шеврон Icon Only Inverse-primary); на жёлтой заливке Warning Bold белое не проходит WCAG, там тёмные Secondary. Своих кнопок у Alert нет.",
            "Bold закрепляет светлую тему `2. General` (explicit mode): заливка роли одинакова в обеих темах, поэтому инверсные кнопки внутри всегда светлые. В коде — `data-theme=\"light\"` на плашке Bold.",
            "Bold использует новые L2 `color/status/{hue}/bold/*`: текст ≥ 4.5:1 в обеих темах; жёлтый — тёмный текст.",
            "Тень карточки Default не собирается: эффект-стили не проработаны (решение автора); вместо неё рамка `alert/default/border`.",
            "Аватар вместо иконки в Default (уведомления о действиях людей) — следующий шаг: нужен собранный Avatar.",
        ],
        "sets": [{
            "name": "Alert",
            "description": "Сообщение о результате или состоянии: Subtle — в потоке блока, Default — карточка-уведомление, Bold — насыщенная для важного.",
            "axes": [{"name": "Appearance", "values": APPEARANCES}, {"name": "Role", "values": ROLES}, {"name": "Size", "values": ["M", "S"]},
                     {"name": "Inverse", "values": ["False", "True"]}, {"name": "Expanded", "values": ["True", "False"]}],
            "exclude": [{"Appearance": ["Subtle", "Default"], "Expanded": "False"}, {"Appearance": "Bold", "Inverse": "True"}],
            "grid": {"columns": "Size", "blocks": "Appearance", "rows": ["Role", "Expanded"], "split": "Inverse"},
            "vars": vars_,
            "props": [
                {"name": "Title", "type": "BOOLEAN", "default": True},
                {"name": "↳ Title", "type": "TEXT", "default": "Заголовок сообщения"},
                {"name": "↳ Description", "type": "TEXT", "default": "Текст сообщения: что произошло и что сделать дальше."},
                {"name": "Actions", "type": "BOOLEAN", "default": False},
                {"name": "Second Action", "type": "BOOLEAN", "default": False},
                {"name": "Close", "type": "BOOLEAN", "default": True},
            ],
            "root": root,
        }],
        "spec": spec,
    }


# ---------------------------------------------------------------- Skeleton
def skeleton():
    inv = {"b": {"from": "Inverse", "map": {"False": "bg", "True": "inverse-bg"}}}
    shape = lambda size_key, extra=None: {  # noqa: E731
        "type": "frame", "name": "root", "fill": "skeleton/shape/{b}", **(extra or {})}
    line = {
        "name": "Skeleton / Line", "description": "Строка-заглушка текста: высота равна интерлиньяжу строки, которую она заменяет. Ширина — доля области: заголовок ~40 %, строки абзаца — 100 %, последняя — ~60 %.",
        "axes": [{"name": "Size", "values": ["S", "M", "L", "XL"]}, {"name": "Inverse", "values": ["False", "True"]}],
        "exclude": [], "grid": {"columns": "Size", "rows": [], "split": "Inverse"},
        "vars": {"s": {"from": "Size", "case": "lower"}, **inv}, "props": [],
        "root": shape("line", {"width": 240, "height": "skeleton/size/line/{s}/height", "radius": "skeleton/size/line/{s}/radius"}),
    }
    circle = {
        "name": "Skeleton / Circle", "description": "Круг-заглушка аватара: диаметр равен размеру заменяемого аватара.",
        "axes": [{"name": "Size", "values": ["S", "M", "L", "XL", "2XL"]}, {"name": "Inverse", "values": ["False", "True"]}],
        "exclude": [], "grid": {"columns": "Size", "rows": [], "split": "Inverse"},
        "vars": {"s": {"from": "Size", "case": "lower"}, **inv}, "props": [],
        "root": shape("circle", {"width": "skeleton/size/circle/{s}/box", "height": "skeleton/size/circle/{s}/box", "radius": "skeleton/size/circle/{s}/radius"}),
    }
    btype = {"Control S": "control-s", "Control M": "control-m", "Control L": "control-l", "Control XL": "control-xl", "Image": "image", "Card": "card"}
    block = {
        "name": "Skeleton / Block", "description": "Блок-заглушка: контрол (высота и скругление как у Button S…XL), изображение или карточка.",
        "axes": [{"name": "Type", "values": list(btype)}, {"name": "Inverse", "values": ["False", "True"]}],
        "exclude": [], "grid": {"columns": "Type", "rows": [], "split": "Inverse"},
        "vars": {"k": {"from": "Type", "map": btype}, **inv}, "props": [],
        "root": shape("block", {
            "width": by("Type", {"Control S": 120, "Control M": 140, "Control L": 160, "Control XL": 180, "Image": 240, "Card": 320}),
            "height": by("Type", {"Control S": "skeleton/size/block/control-s/height", "Control M": "skeleton/size/block/control-m/height",
                                  "Control L": "skeleton/size/block/control-l/height", "Control XL": "skeleton/size/block/control-xl/height",
                                  "Image": 160, "Card": 200}),
            "radius": "skeleton/size/block/{k}/radius"}),
    }
    L = lambda size, w, inv_="False": item("Skeleton / Line", {"Size": size, "Inverse": inv_}, width=w)  # noqa: E731
    spec = {
        "title": "Skeleton", "description": "Временная заглушка на месте содержимого известной структуры, которое загружается: строки текста, круги аватаров, блоки изображений и карточек. Когда данные пришли, заглушка заменяется содержимым без сдвига раскладки.",
        "columns": [
            {"title": "Строка", "width": 400, "cards": [
                {"title": s, "description": d, "items": [L(s, 240)]} for s, d in
                [("S", "Интерлиньяж 16: подписи, мелкий текст"), ("M", "Интерлиньяж 20: основной текст интерфейса"),
                 ("L", "Интерлиньяж 24: текст для чтения"), ("XL", "Интерлиньяж 28: заголовки")]]},
            {"title": "Круг", "cards": [{"title": "Аватар", "description": "Диаметр как у аватара S…2XL",
                                         "items": [item("Skeleton / Circle", {"Size": s, "Inverse": "False"}, label=s) for s in ["S", "M", "L", "XL", "2XL"]]}]},
            {"title": "Блок", "width": 400, "cards": [
                {"title": "Контрол", "description": "Высота и скругление как у Button S…XL",
                 "items": [item("Skeleton / Block", {"Type": t, "Inverse": "False"}, label=t) for t in ["Control S", "Control M", "Control L", "Control XL"]]},
                {"title": "Изображение и карточка", "items": [item("Skeleton / Block", {"Type": t, "Inverse": "False"}, label=t) for t in ["Image", "Card"]]}]},
            {"title": "Применение", "width": 560, "cards": [
                {"title": "Абзац", "description": "3 строки, последняя короче (100 · 100 · 60 %)", "items": [L("M", 480), L("M", 480), L("M", 288)]},
                {"title": "Заголовок с подзаголовком", "description": "1 строка 40 % и 1 строка 60 %", "items": [L("XL", 192), L("M", 288)]}]},
            {"title": "Инверсия", "width": 400, "cards": [
                {"title": "Inverse", "description": "На тёмных поверхностях", "inverse": True,
                 "items": [L("M", 240, "True"), item("Skeleton / Circle", {"Size": "L", "Inverse": "True"}), item("Skeleton / Block", {"Type": "Control L", "Inverse": "True"})]}]},
        ],
    }
    return {
        "component": "skeleton", "title": "Skeleton", "page": "Components / Skeleton", "origin": "new",
        "notes": [
            "Единое правило: загрузка данных в любом компоненте — экземпляры Skeleton, повторяющие раскладку содержимого (docs/build-rules.md, раздел 2). Ожидание внутри контрола (кнопка отправляет форму) — спиннер в контроле, как у Button.",
            "Три набора по форме: Line (S…XL), Circle (S…2XL), Block (Control S…XL, Image, Card). Инверсные варианты — на тёмной правой половине.",
            "Ширина — свойство экземпляра (доля области), в мастере стоит ширина по умолчанию. Анимация мерцания в Figma не собирается: токены блика `skeleton/shimmer/*` — для разработки.",
        ],
        "sets": [line, circle, block],
        "spec": spec,
    }


# ---------------------------------------------------------------- Select в Field
SEL_SIZES = ["S", "M", "L"]
SEL_STATES = ["Default", "Hover", "Pressed", "Disabled", "Read Only", "Error", "Warning", "Success"]
SEL_IO = {"S": "M", "M": "L", "L": "XL"}          # размер Button / Icon Only внутри контрола — как в файле
SEL_FOCUS = {"S": 2, "M": 4, "L": 4}
VALIDATION_ICON = {"Error": "alert-circle", "Warning": "alert-triangle", "Success": "circle-check"}
INV = {"from": "Inverse", "map": {"False": "", "True": "inverse-"}}


def select_button(size):
    """Select / Button / {S,M,L}: повтор контрола из файла «Компоненты · Базовые» (32 варианта)."""
    z = f"field/size/select/{size.lower()}/button"
    active = ["Default", "Hover", "Pressed", "Error", "Warning", "Success"]

    def io(name, icon_name):
        return {"type": "instance", "name": name, "instance": {
            "set": "Button / Icon Only",
            "variant": {"Size": SEL_IO[size], "Type": by("Inverse", {"False": "Secondary", "True": "Inverse-primary"}),
                        "State": by("State", {s: ("Disabled" if s in ("Disabled", "Read Only") else "Default") for s in SEL_STATES}),
                        "Loading": "False"},
            "props": {"↳ Icon": f"icon:{icon_name}"}}}

    def box(name, pad, h, children, when=None, refs=None):
        return {"type": "frame", "name": name, **({"when": when} if when else {}), **({"refs": refs} if refs else {}),
                "layout": {"dir": "H", "px": f"{z}/{pad}", "py": f"{z}/{pad}", "align": "CENTER", "counter": "CENTER", "w": "HUG", "h": "HUG"},
                "height": f"{z}/{h}", "children": children}

    def text_node(filled, prop, chars):
        return {"type": "text", "name": "Name", "when": {"Filled": filled}, "refs": {"characters": prop}, "w": "FILL",
                "text": {"chars": chars, "typography": f"typography/field/select/text/{size.lower()}", "fontStyle": "Regular",
                         "fill": "field/select/text/{i}{tx}", "truncate": True}}

    root = {
        "type": "frame", "name": "root",
        "layout": {"dir": "H", "gap": f"{z}/container-gap", "px": f"{z}/container-x", "py": f"{z}/container-y",
                   "align": "MIN", "counter": "CENTER", "w": "FIXED", "h": "HUG"},
        "width": 320, "height": f"{z}/container", "radius": f"{z}/container-radius",
        "fill": "field/select/bg/{i}{bgs}",
        "stroke": {"color": "field/select/border/{i}{st}", "weight": f"{z}/container-border", "align": "INSIDE"},
        "children": [
            {"type": "rect", "name": "Focus", "when": {"State": [s for s in SEL_STATES if s != "Disabled"]}, "abs": "focus",
             "offset": SEL_FOCUS[size], "visible": False, "refs": {"visible": "Focused"},
             "radius": f"{z}/focus-radius", "stroke": {"color": "field/select/{i}focus-ring", "weight": f"{z}/focus-border", "align": "INSIDE"}},
            box("Leading_icon", "leading-icon-xy", "leading-icon-box",
                [{"type": "icon", "name": "Icon", "icon": {"name": "circle", "size": f"{z}/leading-icon", "color": "field/select/leading-icon/{i}{tx}"}}],
                refs={"visible": "Leading Icon"}),
            {"type": "frame", "name": "Text", "w": "FILL",
             "layout": {"dir": "H", "gap": f"{z}/text-gap", "pl": f"{z}/text-x-left", "pr": f"{z}/text-x-right", "py": f"{z}/text-y",
                        "align": "MIN", "counter": "CENTER", "w": "FILL", "h": "HUG"},
             "children": [text_node("True", "↳ Value", "Значение"), text_node("False", "↳ Inactive", "Не выбрано")]},
            {"type": "frame", "name": "Trailing",
             "layout": {"dir": "H", "gap": f"{z}/trailing-gap", "align": "MAX", "counter": "CENTER", "w": "HUG", "h": "HUG"},
             "children": [
                 box("Validation Marker", "validation-icon-xy", "validation-icon-box",
                     [{"type": "icon", "name": "Icon", "icon": {"name": "{vi}", "size": f"{z}/validation-icon", "color": "field/select/validation-icons/{i}{st}"}}],
                     when={"State": ["Error", "Warning", "Success"]}, refs={"visible": "Validation Marker"}),
                 box("Clear", "action-xy", "action-box", [io("X", "x")],
                     when={"Filled": "True", "State": active}, refs={"visible": "Clear"}),
                 box("Loading", "loading-icon-xy", "loading-icon-box",
                     [{"type": "icon", "name": "Icon", "icon": {"name": "loader-circle", "size": f"{z}/loading-icon", "color": "field/select/loading/{i}loading"}}],
                     when={"State": ["Default", "Hover", "Pressed"]}, refs={"visible": "Loading"}),
                 box("Action", "action-xy", "action-box", [io("Open-Close", "chevron-down")]),
             ]},
        ],
    }
    st_map = {s: s.lower().replace(" ", "-") for s in SEL_STATES}
    return {
        "name": f"_ Select / Button / {size}",
        "description": "Контрол Select: выбранное значение и кнопка открытия списка. Приватная часть семейства Select.",
        "axes": [{"name": "Filled", "values": ["False", "True"]}, {"name": "State", "values": SEL_STATES}, {"name": "Inverse", "values": ["False", "True"]}],
        "exclude": [], "grid": {"columns": "State", "rows": ["Filled"], "split": "Inverse"},
        "vars": {
            "i": INV,
            "st": {"from": "State", "map": st_map},
            "bgs": {"from": "State", "map": {**{s: "default" for s in SEL_STATES}, "Hover": "hover", "Pressed": "pressed",
                                             "Disabled": "disabled", "Read Only": "read-only"}},
            # текст и ведущая иконка — одна пара токенов в каждом состоянии
            "tx": {"from": ["Filled", "State"], "map": {
                **{f"True|{s}": "value" for s in SEL_STATES}, "True|Disabled": "disabled", "True|Read Only": "read-only",
                **{f"False|{s}": "inactive" for s in SEL_STATES}, "False|Disabled": "inactive-disabled"}},  # Read Only читаем: не Disabled
            "vi": {"from": "State", "map": {s: VALIDATION_ICON.get(s, "circle") for s in SEL_STATES}},
        },
        "props": [
            {"name": "Leading Icon", "type": "BOOLEAN", "default": True},
            {"name": "↳ Inactive", "type": "TEXT", "default": "Не выбрано"},
            {"name": "↳ Value", "type": "TEXT", "default": "Значение"},
            {"name": "Clear", "type": "BOOLEAN", "default": True},
            {"name": "Loading", "type": "BOOLEAN", "default": False},
            {"name": "Focused", "type": "BOOLEAN", "default": False},
            {"name": "Validation Marker", "type": "BOOLEAN", "default": True},
        ],
        "root": root,
    }


FIELD_MSG = {"Error": "Выберите значение из списка", "Warning": "Значение устарело, проверьте его", "Success": "Значение сохранено"}
FIELD_MODES = ["None", "Vertical", "Horizontal"]   # Field не публикуется отдельно: это режим семейства (docs/forms-architecture.md)


def _text(name, chars, typo, fill, refs, **kw):
    return {"type": "text", "name": name, "refs": refs, **({"w": kw.pop("w")} if "w" in kw else {}),
            **({"visible": kw.pop("visible")} if "visible" in kw else {}),
            "text": {"chars": chars, "typography": typo, "fontStyle": "Regular", "fill": fill, **kw}}


def _row(name, gap, children, when=None, refs=None, pad=None, dir_="H", w="FILL", extra=None):
    lay = {"dir": dir_, "gap": gap, "align": "MIN", "counter": "MIN", "w": w, "h": "HUG"}
    if pad:
        lay.update({"pl": f"{pad}/x-left", "pr": f"{pad}/x-right", "pt": f"{pad}/y-top", "pb": f"{pad}/y-bottom"})
    return {"type": "frame", "name": name, "w": w, **({"when": when} if when else {}), **({"refs": refs} if refs else {}),
            "layout": lay, **(extra or {}), "children": children}


def field_parts():
    """Части Field (как в Field / Vertical и Field / Horizontal у Input): Label, Description, Extra Space.
    Общие для семейств Select и Input; в режиме Field = None не показываются."""
    title = {"type": "frame", "name": "Title+",
             "layout": {"dir": "H", "gap": "field/size/label/{s}/gap-text-asterisk", "align": "MIN", "counter": "MIN", "w": "HUG", "h": "HUG"},
             "children": [
                 _text("Label", "Заголовок", "typography/field/label/title/{s}", "field/label/{i}primary", {"characters": "↳ Label"}, truncate=True),
                 _text("*", "*", "typography/field/label/title/{s}", "field/label/{i}requirement", {"visible": "+ Required (*)"}, visible=False),
             ]}
    add = lambda: _text("Additional Text", "(доп. текст)", "typography/field/label/additional/{s}", "field/label/{i}additional",  # noqa: E731
                        {"visible": "+ Add. Text", "characters": "↳ Add. Text"}, visible=False, truncate=True)
    label_v = _row("Label", "field/size/label/{s}/gap-left-right", [title, add()], when={"Field": "Vertical"},
                   refs={"visible": "Label"}, pad="field/size/label/{s}")
    # горизонтально: колонка Label фиксированной ширины, отступ сверху выравнивает её по контролу
    label_h = {"type": "frame", "name": "Label", "when": {"Field": "Horizontal"}, "refs": {"visible": "Label"},
               "layout": {"dir": "V", "gap": "field/size/label/{s}/gap-vertical", "pl": "field/size/label/{s}/x-left",
                          "pr": "field/size/label/{s}/x-right", "pt": "field/size/label/{s}/horizontal-y",
                          "align": "MIN", "counter": "MIN", "w": "FIXED", "h": "HUG"},
               "width": "field/size/label/{s}/horizontal", "children": [dict(title), add()]}
    description = _row("Description", "field/size/description/{s}/gap-left-right", [
        _row("Hint", "field/size/description/{s}/gap-icon-text", [
            _text("Text", "Подсказка", "typography/field/hint/{s}", "field/description/text/{i}hint", {"characters": "↳ Hint"}, w="FILL", wrap=True),
        ], when={"Type": "Base"}),
        _row("{T}", "field/size/description/{s}/gap-icon-text", [
            {"type": "frame", "name": "Icon",
             "layout": {"dir": "H", "px": "field/size/description/{s}/hint-icon-x", "py": "field/size/description/{s}/hint-icon-y",
                        "align": "CENTER", "counter": "CENTER", "w": "HUG", "h": "HUG"},
             "height": "field/size/description/{s}/hint-icon-box",
             "children": [{"type": "icon", "name": "Icon", "icon": {"name": "{vi}", "size": "field/size/description/{s}/hint-icon",
                                                                   "color": "field/description/icon/{i}{t}"}}]},
            _text("Text", "{msg}", "typography/field/hint/{s}", "field/description/text/{i}{t}", {"characters": "↳ Message"}, w="FILL", wrap=True),
        ], when={"Type": ["Error", "Warning", "Success"]}),
    ], when={"Field": ["Vertical", "Horizontal"]}, refs={"visible": "Description Zone"}, pad="field/size/description/{s}")
    extra = {"type": "frame", "name": "Extra Space", "when": {"Field": ["Vertical", "Horizontal"]}, "visible": False,
             "refs": {"visible": "+ Extra Space"}, "w": "FILL", "layout": {"dir": "V", "align": "MIN", "counter": "MIN", "w": "FILL", "h": "HUG"},
             "height": "field/size/field/extraspace/{s}", "children": []}
    return label_v, label_h, description, extra


FIELD_PROPS = [
    {"name": "Label", "type": "BOOLEAN", "default": True},
    {"name": "↳ Label", "type": "TEXT", "default": "Заголовок"},
    {"name": "+ Required (*)", "type": "BOOLEAN", "default": False},
    {"name": "+ Add. Text", "type": "BOOLEAN", "default": False},
    {"name": "↳ Add. Text", "type": "TEXT", "default": "(доп. текст)"},
    {"name": "Description Zone", "type": "BOOLEAN", "default": True},
    {"name": "↳ Hint", "type": "TEXT", "default": "Подсказка"},
    {"name": "↳ Message", "type": "TEXT", "default": "Сообщение проверки"},
    {"name": "+ Extra Space", "type": "BOOLEAN", "default": False},
]


def field_vars():
    return {"s": {"from": "Size", "case": "lower"}, "S": {"from": "Size"}, "I": {"from": "Inverse"}, "i": INV,
            # в системе у M — `gap`, у S и L — `gap-vertical` (как в Field / Vertical; не переименовываем)
            "fg": {"from": "Size", "map": {"S": "gap-vertical", "M": "gap", "L": "gap-vertical"}},
            "t": {"from": "Type", "case": "lower"}, "T": {"from": "Type"},
            "vi": {"from": "Type", "map": {"Base": "circle", **VALIDATION_ICON}},
            "msg": {"from": "Type", "map": {"Base": "", **FIELD_MSG}}}


def field_root(body_children, widths):
    """Корень семейства: направление и отступы зависят от режима Field."""
    label_v, label_h, description, extra = field_parts()
    pad = lambda k: by("Field", {"None": 0, "Vertical": f"field/size/field/base/{{s}}/{k}", "Horizontal": f"field/size/field/base/{{s}}/{k}"})  # noqa: E731
    body = {"type": "frame", "name": "Body", "w": "FILL",
            "layout": {"dir": "V", "gap": "field/size/field/base/{s}/{fg}", "align": "MIN", "counter": "MIN", "w": "FILL", "h": "HUG"},
            "children": [*body_children, description, extra]}
    return {
        "type": "frame", "name": "root",
        "layout": {"dir": by("Field", {"None": "V", "Vertical": "V", "Horizontal": "H"}),
                   "gap": by("Field", {"None": 0, "Vertical": "field/size/field/base/{s}/{fg}", "Horizontal": "field/size/field/base/{s}/gap-horizontal"}),
                   "pl": pad("x-left"), "pr": pad("x-right"), "pt": pad("y-top"), "pb": pad("y-bottom"),
                   "align": "MIN", "counter": "MIN", "w": "FIXED", "h": "HUG"},
        "width": by("Field", widths),
        "children": [label_v, label_h, body],
    }


# ---------------------------------------------------------------- Select: список (механика, не отдельный компонент)
def dropdown_items(size):
    """_ Select / Dropdown Items / {S}: пункт списка — Option, Group Title, Divider (как в файле, 24 варианта)."""
    z = f"field/size/select/{size.lower()}/option"
    opt = {"Type": "Option"}
    root = {
        "type": "frame", "name": "root",
        "layout": {"dir": "H", "gap": f"{z}/container-gap", "px": f"{z}/container-x", "py": f"{z}/container-y",
                   "align": "MIN", "counter": "CENTER", "w": "FIXED", "h": "HUG"},
        "width": 320, "height": by("Type", {"Option": f"{z}/container"}), "radius": f"{z}/container-radius",
        "fill": "field/select/dropdown/option/bg/{i}{bgk}",
        "children": [
            {"type": "rect", "name": "Focus", "when": {"Type": ["Option", "Group Title"], "State": ["Default", "Hover", "Pressed"]}, "abs": "focus",
             "offset": 0, "visible": False, "refs": {"visible": "Focused"}, "radius": f"{z}/focus-radius",
             "stroke": {"color": "field/select/dropdown/option/{i}focus-ring", "weight": f"{z}/focus-border", "align": "INSIDE"}},
            {"type": "frame", "name": "Leading_icon", "when": opt, "refs": {"visible": "Leading Icon"},
             "layout": {"dir": "H", "px": f"{z}/leading-icon-xy", "py": f"{z}/leading-icon-xy", "align": "CENTER", "counter": "CENTER", "w": "HUG", "h": "HUG"},
             "height": f"{z}/leading-icon-box",
             "children": [{"type": "icon", "name": "Icon", "icon": {"name": "circle", "size": f"{z}/leading-icon", "color": "field/select/dropdown/option/leading-icon/{i}{lt}"}}]},
            {"type": "frame", "name": "Text", "when": {"Type": ["Option", "Group Title"]}, "w": "FILL",
             "layout": {"dir": "H", "pl": f"{z}/text-x-left", "pr": f"{z}/text-x-right", "py": f"{z}/text-y", "align": "MIN", "counter": "CENTER", "w": "FILL", "h": "HUG"},
             "children": [
                 {"type": "text", "name": "Name", "when": opt, "refs": {"characters": "↳ Value"}, "w": "FILL",
                  "text": {"chars": "Значение", "typography": f"typography/field/select/option/{size.lower()}", "fontStyle": "Regular",
                           "fill": "field/select/dropdown/option/text/{i}{tx}", "truncate": True}},
                 {"type": "text", "name": "Name", "when": {"Type": "Group Title"}, "refs": {"characters": "↳ Group Title"}, "w": "FILL",
                  "text": {"chars": "Заголовок группы", "typography": f"typography/field/select/option-title/{size.lower()}", "fontStyle": "Medium",
                           "fill": "field/select/dropdown/option/text/{i}value", "truncate": True}},
             ]},
            {"type": "frame", "name": "Indicator", "when": {"Type": "Option", "Active": "True"}, "refs": {"visible": "Indicator"},
             "layout": {"dir": "H", "px": f"{z}/indicator-icon-xy", "py": f"{z}/indicator-icon-xy", "align": "CENTER", "counter": "CENTER", "w": "HUG", "h": "HUG"},
             "height": f"{z}/indicator-icon-box",
             "children": [{"type": "icon", "name": "Icon", "icon": {"name": "check", "size": f"{z}/indicator-icon", "color": "field/select/dropdown/option/indicator/{i}{ic}"}}]},
            {"type": "frame", "name": "Divider", "when": {"Type": "Divider"}, "w": "FILL", "height": 1,
             "layout": {"dir": "H", "align": "MIN", "counter": "MIN", "w": "FILL", "h": "FIXED"},
             "fill": {"by": "Inverse", "map": {"False": "divider/line/intense", "True": "field/select/dropdown/option/divider/inverse"}}, "children": []},
        ],
    }
    ro = lambda a, b: {f"{act}|{st}": (b if st == "Read Only" else a) for act in ("True", "False") for st in ("Default", "Hover", "Pressed", "Read Only")}  # noqa: E731
    return {
        "name": f"_ Select / Dropdown Items / {size}", "description": "Пункт списка Select: вариант, заголовок группы, разделитель. Приватная часть.",
        "axes": [{"name": "Active", "values": ["True", "False"]}, {"name": "State", "values": ["Default", "Hover", "Pressed", "Read Only"]},
                 {"name": "Type", "values": ["Option", "Group Title", "Divider"]}, {"name": "Inverse", "values": ["False", "True"]}],
        "exclude": [{"Type": ["Group Title", "Divider"], "State": ["Hover", "Pressed", "Read Only"]}],
        "a11y": {"exempt": {"State": "Read Only"}, "reason": "Read Only пункта — недоступный для выбора вариант (WCAG 1.4.3: неактивные элементы)"},
        "grid": {"columns": "State", "blocks": "Type", "rows": ["Active"], "split": "Inverse"},
        "vars": {
            "i": INV,
            "bgk": {"from": ["Active", "State"], "map": {"False|Default": "default", "False|Hover": "hover", "False|Pressed": "pressed", "False|Read Only": "disabled",
                                                        "True|Default": "active", "True|Hover": "active-hover", "True|Pressed": "active-hover", "True|Read Only": "active-disabled"}},
            "tx": {"from": ["Active", "State"], "map": ro("value", "disabled")},
            "lt": {"from": ["Active", "State"], "map": ro("icon", "read-only")},
            "ic": {"from": ["Active", "State"], "map": ro("icon", "icon-disabled")},
        },
        "props": [
            {"name": "Leading Icon", "type": "BOOLEAN", "default": False},
            {"name": "↳ Value", "type": "TEXT", "default": "Значение"},
            {"name": "Indicator", "type": "BOOLEAN", "default": True},
            {"name": "↳ Group Title", "type": "TEXT", "default": "Заголовок группы"},
            {"name": "Focused", "type": "BOOLEAN", "default": False},
        ],
        "root": root,
    }


DD_SLOTS = 8   # пунктов в списке; с третьего — видимость свойством (как 03…010 в файле)


def dropdown(size):
    """_ Select / Dropdown / {S}: панель списка — Default (пункты), Empty, Loading. Тень — переменные effects/select/*."""
    s = size.lower()
    z = f"field/size/select/{s}/dropdown-box"
    items = [{"type": "instance", "name": str(k), "when": {"State": "Default"}, "w": "FILL",
              **({"refs": {"visible": f"{k:02d}"}} if k >= 3 else {}),
              "instance": {"set": f"_ Select / Dropdown Items / {size}",
                           "variant": {"Active": "True" if k == 2 else "False", "State": "Default", "Type": "Option", "Inverse": "{I}"},
                           "props": {"↳ Value": ["Москва", "Санкт-Петербург", "Казань", "Новосибирск", "Екатеринбург", "Нижний Новгород", "Самара", "Омск"][k - 1]}}}
             for k in range(1, DD_SLOTS + 1)]
    root = {
        "type": "frame", "name": "root",
        "layout": {"dir": "V", "gap": f"{z}/container-gap", "px": f"{z}/container-x", "py": f"{z}/container-y",
                   "align": by("State", {"Default": "MIN", "Empty": "CENTER", "Loading": "CENTER"}), "counter": by("State", {"Default": "MIN", "Empty": "CENTER", "Loading": "CENTER"}),
                   "w": "FIXED", "h": "HUG"},
        # Empty и Loading — панель той же ширины, что список, своей высоты; подсказка и загрузка по центру (как в макетах)
        "width": 320, "height": by("State", {"Default": "", "Empty": f"{z}/empty-height", "Loading": f"{z}/empty-height"}),
        "radius": f"field/size/select/{s}/button/container-radius", "fill": "field/select/dropdown/container/{i}base",
        "shadow": {"x": f"effects/select/x/{s}", "y": f"effects/select/y/{s}", "blur": f"effects/select/blur/{s}",
                   "spread": f"effects/select/spread/{s}", "color": "color/transparent-black/120"},
        "children": [
            *items,
            {"type": "text", "name": "Hint", "when": {"State": "Empty"}, "refs": {"characters": "↳ Text"},
             "text": {"chars": "Ничего не найдено", "typography": f"typography/field/select/hint/{s}", "fontStyle": "Regular",
                      "fill": "field/select/dropdown/container/{i}hint"}},
            {"type": "icon", "name": "Loader", "when": {"State": "Loading"},
             "icon": {"name": "loader", "size": f"{z}/loader", "color": "field/select/dropdown/container/{i}loader-icon"}},
        ],
    }
    return {
        "name": f"_ Select / Dropdown / {size}", "description": "Список Select: пункты, пустой результат, загрузка вариантов. Приватная часть.",
        "axes": [{"name": "State", "values": ["Default", "Empty", "Loading"]}, {"name": "Inverse", "values": ["False", "True"]}],
        "exclude": [], "grid": {"columns": "State", "rows": [], "split": "Inverse"},
        "vars": {"i": INV, "I": {"from": "Inverse"}},
        "props": [{"name": "↳ Text", "type": "TEXT", "default": "Ничего не найдено"},
                  *[{"name": f"{k:02d}", "type": "BOOLEAN", "default": True} for k in range(3, DD_SLOTS + 1)]],
        "root": root,
    }


def select_family():
    """Select — единственный публикуемый набор семейства: Field (None / Vertical / Horizontal) × Type × Size × Open × Inverse."""
    t_map = {"Base": "Default", "Error": "Error", "Warning": "Warning", "Success": "Success"}
    control = {"type": "frame", "name": "Control", "w": "FILL",
               "layout": {"dir": "V", "gap": "field/size/select/{s}/button-dropdown-gap", "align": "MIN", "counter": "MIN", "w": "FILL", "h": "HUG"},
               "children": [
                   {"type": "instance", "name": "Select", "expose": True, "w": "FILL", "instance": {
                       "set": "_ Select / Button / {S}",
                       "variant": {"Filled": by("Open", {"False": "False", "True": "True"}), "State": by("Type", t_map), "Inverse": "{I}"},
                       # в открытом виде в контроле — выбранный в списке пункт
                       "props": {"Leading Icon": False, "Loading": False, "↳ Value": by("Open", {"False": "Значение", "True": "Санкт-Петербург"})}}},
                   {"type": "instance", "name": "Dropdown", "expose": True, "when": {"Open": "True"}, "w": "FILL", "instance": {
                       "set": "_ Select / Dropdown / {S}", "variant": {"State": "Default", "Inverse": "{I}"}, "props": {}}},
               ]}
    return {
        "name": "Select", "origin": "new",
        "description": "Выбор одного значения из списка. Field: None — только контрол; Vertical и Horizontal — в обёртке Field (Label, подсказка, сообщение проверки). Open — раскрытый список.",
        "axes": [{"name": "Field", "values": FIELD_MODES}, {"name": "Type", "values": list(t_map)}, {"name": "Size", "values": SEL_SIZES},
                 {"name": "Open", "values": ["False", "True"]}, {"name": "Inverse", "values": ["False", "True"]}],
        "exclude": [], "grid": {"columns": "Type", "blocks": "Field", "rows": ["Size", "Open"], "split": "Inverse"},
        "vars": field_vars(),
        "props": FIELD_PROPS,
        "root": field_root([control], {"None": 320, "Vertical": 360, "Horizontal": 520}),
    }


def select():
    def fam(field="Vertical", t="Base", size="M", open_="False", inv="False", props=None, label=None, nested=None, width=None):
        x = item("Select", {"Field": field, "Type": t, "Size": size, "Open": open_, "Inverse": inv}, props, label, width)
        if nested:
            x["nested"] = nested
        return x

    def sb(st="Default", filled="False", props=None, label=None):
        return item("_ Select / Button / M", {"Filled": filled, "State": st, "Inverse": "False"}, props, label)

    def opt(active="False", st="Default", typ="Option", label=None):
        return item("_ Select / Dropdown Items / M", {"Active": active, "State": st, "Type": typ, "Inverse": "False"}, None, label)

    filled = {"Select": {"Filled": "True", "↳ Value": "Москва"}}
    spec = {
        "title": "Select",
        "description": "Выбор одного значения из списка. Семейство: контрол, список и обёртка Field — одно свойство, а не отдельные компоненты. Field: None — контрол без подписей (таблицы, фильтры); Vertical — Label сверху; Horizontal — Label слева.",
        "columns": [
            {"title": "Field", "width": 640, "cards": [
                {"title": "None", "description": "Только контрол: фильтры, строки таблиц, плотные панели. Доступное имя задаётся в коде", "items": [fam("None")]},
                {"title": "Vertical", "description": "Label сверху, подсказка снизу — основной режим форм", "items": [fam("Vertical", props={"+ Required (*)": True})]},
                {"title": "Horizontal", "description": "Label слева — формы с устойчивой сеткой и достаточной шириной", "items": [fam("Horizontal")]}]},
            {"title": "Размер", "width": 440, "cards": [
                {"title": s, "description": d, "items": [fam(size=s)]} for s, d in
                [("S", "Плотные формы и таблицы"), ("M", "Основной размер форм"), ("L", "Крупные формы и мобильные сценарии")]]},
            {"title": "Проверка", "width": 440, "cards": [
                {"title": t, "description": d, "items": [fam(t=t, props={"↳ Message": FIELD_MSG[t]} if t != "Base" else None)]} for t, d in
                [("Base", "Без сообщения проверки"), ("Error", "Значение нужно исправить: сообщение объясняет, что сделать"),
                 ("Warning", "Значение допустимо, но требует внимания"), ("Success", "Подтверждение, когда оно полезно")]]},
            {"title": "Состояния контрола", "width": 440, "cards": [
                {"title": "Mouse и клавиатура",
                 "items": [sb(st, label=st) for st in ["Default", "Hover", "Pressed"]] +
                          [sb("Default", props={"Focused": True}, label="Focused"), sb("Disabled", label="Disabled"), sb("Read Only", "True", label="Read Only")]}]},
            {"title": "Список", "width": 440, "cards": [
                {"title": "Открыт", "description": "Список под контролом; выбранный пункт отмечен галочкой", "items": [fam("None", open_="True")]},
                {"title": "Пусто", "description": "Поиск не дал результатов", "items": [fam("None", open_="True", nested={"Dropdown": {"State": "Empty"}})]},
                {"title": "Загрузка вариантов", "description": "Список ждёт данные: спиннер внутри списка, контрол статичен", "items": [fam("None", open_="True", nested={"Dropdown": {"State": "Loading"}})]}]},
            {"title": "Пункты списка", "width": 440, "cards": [
                {"title": "Состояния пункта", "items": [opt(label="Default"), opt(st="Hover", label="Hover"), opt(st="Pressed", label="Pressed"),
                                                        opt("True", label="Выбран"), opt("True", "Read Only", label="Read Only")]},
                {"title": "Группы", "description": "Заголовок группы и разделитель", "items": [opt(typ="Group Title", label="Group Title"), opt(typ="Divider", label="Divider")]}]},
            {"title": "Содержание", "width": 440, "cards": [
                {"title": "Label", "description": "Обязательность и дополнительный текст", "items": [fam(props={"+ Required (*)": True, "+ Add. Text": True})]},
                {"title": "Без описания", "items": [fam(props={"Description Zone": False})]},
                {"title": "Заполнено, ведущая иконка", "items": [fam(nested={"Select": {"Leading Icon": True, "Filled": "True", "↳ Value": "Москва"}})]}]},
            {"title": "Corner Case", "width": 440, "cards": [
                {"title": "Длинное значение", "description": "Значение обрезается многоточием, полное — в Tooltip",
                 "items": [fam(nested={"Select": {"Filled": "True", "↳ Value": "Санкт-Петербург, Ленинградская область, Российская Федерация"}})]},
                {"title": "Длинное сообщение", "description": "Сообщение переносится и не обрезается",
                 "items": [fam(t="Error", props={"↳ Message": "Этот вариант недоступен для вашего тарифа. Выберите другой вариант или смените тариф в настройках"})]}]},
            {"title": "Инверсия", "width": 440, "cards": [
                {"title": "Inverse", "description": "На тёмных поверхностях: светлые токены inverse-* для текста, иконок, рамки и списка",
                 "inverse": True,
                 "items": [fam(inv="True", nested=filled), fam("None", open_="True", inv="True"),
                           fam(t="Error", inv="True", props={"↳ Message": FIELD_MSG["Error"]})]}]},
        ],
    }
    parts = [*(select_button(s) for s in SEL_SIZES), *(dropdown_items(s) for s in SEL_SIZES), *(dropdown(s) for s in SEL_SIZES)]
    return {
        "component": "select", "title": "Select", "page": "Components / Select", "origin": "existing",
        "requires": ["button"],
        "notes": [
            "Семейство Select: публикуется один набор `Select` (Field × Type × Size × Open × Inverse, 144 варианта). Части — приватные (`_`): контрол `_ Select / Button`, список `_ Select / Dropdown`, пункты `_ Select / Dropdown Items` (S, M, L).",
            "Контрол и список — повтор текущего SimpleSelect из файла (Select / Button, _ Select / Dropdown, _ Select / Dropdown Items), контрол стал приватным.",
            "Dropdown — механика Select (а также Combobox и Multiselect), а не отдельный компонент каталога.",
            "Field не публикуется отдельно: режим Field (None / Vertical / Horizontal) — свойство семейства; части Field те же, что у Input (docs/forms-architecture.md).",
            "Список открывается в потоке под контролом (как `Select` Open=True в файле); тень — переменные `effects/select/*`.",
        ],
        "exceptions": [{"token": "color/transparent-black/120",
                        "reason": "Цвет тени списка привязан к L1, как в файле компонентов: эффекты пока не проработаны (решение автора), своего L2 для тени нет."}],
        "sets": [*parts, select_family()],
        "spec": spec,
    }



def main():
    for d in (button(), alert(), skeleton(), select(), selection("checkbox"), selection("radiobutton"), avatar(), chip()):
        out = ROOT / "presets" / f"{d['component']}.build.json"
        out.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
        n = 0
        for s in d["sets"]:
            import itertools
            combos = list(itertools.product(*[a["values"] for a in s["axes"]]))
            names = [a["name"] for a in s["axes"]]
            hit = lambda v, val: v in val if isinstance(val, list) else v == val  # noqa: E731
            ok = [c for c in combos if not any(all(hit(dict(zip(names, c)).get(k), val) for k, val in ex.items()) for ex in s["exclude"])]
            n += len(ok)
            print(f"  {s['name']}: {len(ok)} вариантов")
        print(f"{out.relative_to(ROOT).as_posix()}: наборов {len(d['sets'])}, вариантов {n}")


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    main()
