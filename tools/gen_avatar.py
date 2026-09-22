"""FEDS: описание сборки Avatar — повтор устройства из файла «Компоненты · Базовые» (страница Avatar, 46 элементов)
по именам токенов библиотеки (эталон — библиотека, docs/build-rules.md).

Состав (как в файле):
  _ Avatar / {2xl…s} / Circle | Square     — сам аватар: Style (Image, Soft, Filled) × Type × Color;
  _ Avatar / Status / {size}               — точка статуса (Online, Offline, Busy, Away, Other (blue));
  _ Avatar / Counter / {size}              — бейдж-счётчик (у S — точка без цифры), одиночный компонент;
  _ Avatar / button_X / {size}             — крестик удаления (нет у S), одиночный компонент;
  _ Avatar-Group / {size} / Circle|Square  — аватар в группе: кольцо-разделитель (Grouped), свои цвета box-group;
  _ Avatar-Group / {size} / Circle-сounter | Square-сounter — «+N» группы (имя с кириллической «с» — как в файле);
  Avatar                                   — публичный: Type (Default, Badge, Button-X) × Squared × Size, статус, имя, описание;
  Avatar-Group                             — публичный: Squared × Size, до 7 аватаров и «+N».

Форма — по философии форм (docs, input/docs/filosofiya-form.md): Circle — человек, Square — объект (компания, проект, команда,
интеграция, файл, бот); наполнение (фото, инициалы, иконка) на форму не влияет.
Отличия от файла: фото — встроенная заглушка (замените своим изображением); кольцо группы — на радиусе аватара
(в файле — устаревший `~S/box-group-radius-*`); смещения статуса и бейджа — как в файле, числами.
"""

SIZES = ["2xl", "xl", "l", "m", "s"]
SHAPES = ["Circle", "Square"]
COLORS = ["Base", "Blue", "Red", "Green", "Yellow", "Purple", "Inverse"]
ENTITY = {"Интеграции": "blocks", "Файл": "file", "Боты": "bot", "Компания": "building2", "Проекты": "folder-kanban", "Команда": "users-group"}
PERSON_TYPES = ["Photo", "Counter", "Initials", "Loading", "User Icon", "Plus"]
FOCUS = {"2xl": 4, "xl": 4, "l": 3, "m": 3, "s": 2}
STATUS_POS = {("s", "Circle"): (12, 12), ("s", "Square"): (13, 13), ("m", "Circle"): (18, 19), ("m", "Square"): (20, 20),
              ("l", "Circle"): (24, 25), ("l", "Square"): (27, 27), ("xl", "Circle"): (36, 38), ("xl", "Square"): (41, 41),
              ("2xl", "Circle"): (49, 49), ("2xl", "Square"): (53, 53)}
BADGE_POS = {("s", "Circle"): (11, 0), ("s", "Square"): (11, -1), "m": (13, -3), "l": (18, -3), "xl": (31, -3), "2xl": (42, -3)}
BUTTON_X_POS = {"m": (13, -3), "l": (19, -3), "xl": (31, -3), "2xl": (43, -3)}
STATUS = {"Online": "online", "Offline": "offline", "Busy": "busy", "Away": "away", "Other (blue)": "notification"}


def by(axis, mapping):
    return {"by": axis, "map": mapping}


def low(c):
    return c.lower()


def text_color(style, color):
    """Текст и иконка в цвет роли: Soft — цвет роли, Filled — светлый; Inverse — наоборот (для тёмных поверхностей)."""
    if style == "Filled":
        return "base" if color == "Inverse" else "base-inverse"
    return "base-inverse" if color == "Inverse" else low(color)


def avatar_set(size, shape, group=False):
    s = size
    z = f"avatar/size/{s}"
    types = PERSON_TYPES + (list(ENTITY) if shape == "Square" else [])
    if group:
        types = ["Photo", "Initials", "Loading"] + (list(ENTITY) if shape == "Square" else [])
    box = "box-group" if group else "box"
    rad = "circle" if shape == "Circle" else "square"
    others = [t for t in types if t not in ("Photo", "Counter", "Loading")]
    exclude = [
        {"Style": "Image", "Type": others},
        {"Type": "Photo", "Style": ["Soft", "Filled"]},
        {"Type": "Photo", "Color": [c for c in COLORS if c != "Blue"]},
        {"Type": [t for t in ("Counter", "Loading") if t in types], "Style": "Soft"},
        {"Type": [t for t in ("Counter", "Loading") if t in types], "Color": [c for c in COLORS if c != "Base"]},
    ]
    if group:
        exclude.append({"Style": "Soft", "Color": "Inverse"})  # у box-group/soft нет inverse — как в файле
    text_types = {"Initials", "Counter"}
    # заливка, рамка и цвет текста зависят от стиля и цвета (21 сочетание), фото и загрузка — от типа
    sc = [f"{st}|{c}" for st in ("Image", "Soft", "Filled") for c in COLORS]
    fillc = {k: (f"avatar/{box}/soft/base" if k.startswith("Image") else
                 f"avatar/{box}/{'soft' if k.startswith('Soft') else 'hard'}/{low(k.split('|')[1])}") for k in sc}
    if group:
        strokec = {k: ("avatar/box-group/border/inverse" if k.startswith("Filled") else "avatar/box-group/border/base") for k in sc}
    else:
        strokec = {k: ("avatar/box/border/hard" if (k.startswith("Filled") and not k.endswith("Inverse")) else "avatar/box/border/soft") for k in sc}
    inkc = {k: text_color("Filled" if k.startswith("Filled") else "Soft", k.split("|")[1]) for k in sc}
    fill_t = by("Type", {t: ("image:photo" if t == "Photo" else "{fillc}") for t in types})
    stroke_t = by("Type", {t: ("" if (t == "Loading" and not group) else "{strokec}") for t in types})
    children = [
        {"type": "rect", "name": "focus", "abs": "focus", "offset": FOCUS[s], "visible": False, "refs": {"visible": "Focused"},
         "radius": f"{z}/focus-radius-{rad}",
         "stroke": {"color": f"avatar/{box}/border/focus", "weight": f"{z}/focus-border", "align": "INSIDE"}},
    ]
    if group:
        children.insert(0, {"type": "rect", "name": "group", "abs": "focus", "offset": 0, "visible": False, "refs": {"visible": "Grouped"},
                            "radius": f"{z}/box-radius-{rad}",
                            "stroke": {"color": "avatar/box-group/border/spacer", "weight": f"{z}/box-group-border", "align": "OUTSIDE"}})
    children.append({"type": "text", "name": "Initials", "when": {"Type": "Initials"}, "refs": {"characters": "↳ Initials"},
                     "text": {"chars": "СА", "style": f"typography/avatar/{s}/initials", "fontStyle": "Bold", "fill": "avatar/text/{ink}"}})
    if not group and s != "s":
        children.append({"type": "frame", "name": "Text Area", "when": {"Type": "Counter"},
                         "layout": {"dir": "H", "align": "CENTER", "counter": "CENTER", "w": "HUG", "h": "HUG"}, "children": [
                             {"type": "text", "name": "+", "text": {"chars": "+", "style": f"typography/avatar/{s}/more", "fontStyle": "Medium", "fill": "avatar/text/{ink}"}},
                             {"type": "text", "name": "99", "refs": {"characters": "↳ Num"},
                              "text": {"chars": "99", "style": f"typography/avatar/{s}/more", "fontStyle": "Medium", "fill": "avatar/text/{ink}"}}]})
    icons = {"User Icon": ("user2", "box-icon-user"), "Plus": ("plus", "box-icon-plus"), **{t: (i, "box-icon-plus") for t, i in ENTITY.items()}}
    for ty, (icon, tok) in icons.items():
        if ty in types:
            children.append({"type": "icon", "name": icon, "when": {"Type": ty},
                             "icon": {"name": icon, "size": f"{z}/{tok}", "color": "avatar/icon/{ink}"}})
    pad_text = {"pl": f"{z}/box-text-x", "pr": f"{z}/box-text-x", "pt": f"{z}/box-text-y-top", "pb": f"{z}/box-text-y-bottom"}
    pad_box = {"pl": f"{z}/box-xy", "pr": f"{z}/box-xy", "pt": f"{z}/box-xy", "pb": f"{z}/box-xy"}
    pads = {k: by("Type", {t: (pad_text if t in text_types else pad_box)[k] for t in types}) for k in ("pl", "pr", "pt", "pb")}
    props = [{"name": "Focused", "type": "BOOLEAN", "default": False}]
    if group:
        props.append({"name": "Grouped", "type": "BOOLEAN", "default": False})
    props.append({"name": "↳ Initials", "type": "TEXT", "default": "СА"})
    if not group and s != "s":
        props.append({"name": "↳ Num", "type": "TEXT", "default": "99"})
    name = f"_ Avatar-Group / {s} / {shape}" if group else f"_ Avatar / {s} / {shape}"
    return {
        "name": name,
        "description": ("Аватар в группе: кольцо-разделитель Grouped. " if group else "") +
                       ("Circle — человек (пользователь, автор, участник)." if shape == "Circle" else
                        "Square — объект: компания, проект, команда, интеграция, файл, бот.") + " Приватная часть Avatar.",
        "axes": [{"name": "Style", "values": ["Image", "Soft", "Filled"]}, {"name": "Type", "values": types}, {"name": "Color", "values": COLORS}],
        "exclude": exclude,
        "grid": {"columns": "Color", "blocks": "Style", "rows": ["Type"], "split": {"axis": "Color", "values": ["Inverse"]}},
        "a11y": {"exempt": {"Type": ["Photo", "Loading"]}, "reason": "Photo — изображение, Loading — заглушка без содержимого"},
        "vars": {"ink": {"from": ["Style", "Color"], "map": inkc}, "fillc": {"from": ["Style", "Color"], "map": fillc},
                 "strokec": {"from": ["Style", "Color"], "map": strokec}},
        "props": props,
        "root": {
            "type": "frame", "name": "root",
            "layout": {"dir": "H", **pads, "align": "CENTER", "counter": "CENTER", "w": "FIXED", "h": "FIXED"},
            "width": f"{z}/box", "height": f"{z}/box", "radius": f"{z}/box-radius-{rad}", "fill": fill_t,
            "stroke": {"color": stroke_t, "weight": f"{z}/box-border", "align": "INSIDE"},
            "children": children,
        },
    }


def group_counter(size, shape):
    s = size
    z = f"avatar/size/{s}"
    rad = "circle" if shape == "Circle" else "square"
    kids = [
        {"type": "rect", "name": "group", "abs": "focus", "offset": 0, "radius": f"{z}/box-radius-{rad}",
         "stroke": {"color": "avatar/box-group/border/spacer", "weight": f"{z}/box-group-border", "align": "OUTSIDE"}},
        {"type": "rect", "name": "focus", "abs": "focus", "offset": FOCUS[s] + 1, "visible": False, "refs": {"visible": "Focused"},
         "radius": f"{z}/focus-radius-{rad}", "stroke": {"color": "avatar/box-group/border/focus", "weight": f"{z}/focus-border", "align": "INSIDE"}},
    ]
    props = [{"name": "Focused", "type": "BOOLEAN", "default": False}]
    if s != "s":
        ink = by("Style", {"Filled": "avatar/text/base-inverse", "Soft": "avatar/text/base"})
        kids.append({"type": "frame", "name": "Text Area", "layout": {"dir": "H", "align": "CENTER", "counter": "CENTER", "w": "HUG", "h": "HUG"}, "children": [
            {"type": "text", "name": "+", "text": {"chars": "+", "style": f"typography/avatar/{s}/more", "fontStyle": "Medium", "fill": ink}},
            {"type": "text", "name": "99", "refs": {"characters": "↳ Num"}, "text": {"chars": "99", "style": f"typography/avatar/{s}/more", "fontStyle": "Medium", "fill": ink}}]})
        props.append({"name": "↳ Num", "type": "TEXT", "default": "99"})
    return {
        "name": f"_ Avatar-Group / {s} / {shape}-сounter", "description": "«+N» — остальные участники группы. Приватная часть Avatar.",
        "axes": [{"name": "Style", "values": ["Filled", "Soft"]}], "exclude": [], "grid": {"columns": "Style", "rows": []},
        "props": props,
        "root": {"type": "frame", "name": "root",
                 "layout": {"dir": "H", "pl": f"{z}/box-text-x", "pr": f"{z}/box-text-x", "pt": f"{z}/box-text-y-top", "pb": f"{z}/box-text-y-bottom",
                            "align": "CENTER", "counter": "CENTER", "w": "FIXED", "h": "FIXED"},
                 "width": f"{z}/box", "height": f"{z}/box", "radius": f"{z}/box-radius-{rad}",
                 "fill": by("Style", {"Filled": "avatar/box-group/hard/base", "Soft": "avatar/box-group/soft/base"}),
                 "stroke": {"color": by("Style", {"Filled": "avatar/box-group/border/inverse", "Soft": "avatar/box-group/border/base"}),
                            "weight": f"{z}/box-border", "align": "INSIDE"},
                 "children": kids},
    }


def status_set(size):
    z = f"avatar/size/{size}"
    return {
        "name": f"_ Avatar / Status / {size}", "description": "Статус присутствия на аватаре. Приватная часть Avatar.",
        "axes": [{"name": "State", "values": list(STATUS)}], "exclude": [], "grid": {"columns": "State", "rows": []},
        "a11y": {"exempt": {"State": list(STATUS)}, "reason": "Точка статуса без текста: сигнал, дублируется подписью"},
        "vars": {"c": {"from": "State", "map": STATUS}}, "props": [],
        "root": {"type": "frame", "name": "root", "layout": {"dir": "V", "align": "MIN", "counter": "MIN", "w": "FIXED", "h": "FIXED"},
                 "width": f"{z}/status", "height": f"{z}/status", "radius": f"{z}/status-radius", "fill": "avatar/status/{c}",
                 "stroke": {"color": "avatar/status/spacer", "weight": f"{z}/status-border", "align": "OUTSIDE"}, "children": []},
    }


def counter_comp(size):
    z = f"avatar/size/{size}"
    root = {"type": "frame", "name": "root", "radius": f"{z}/counter-radius", "fill": "avatar/status/counter",
            "stroke": {"color": "avatar/status/spacer", "weight": f"{z}/counter-border", "align": "OUTSIDE"}, "children": []}
    props = []
    if size == "s":  # у S бейдж — точка без цифры
        root.update({"layout": {"dir": "H", "align": "CENTER", "counter": "CENTER", "w": "FIXED", "h": "FIXED"},
                     "width": f"{z}/counter", "height": f"{z}/counter"})
    else:
        root.update({"layout": {"dir": "H", "pl": f"{z}/counter-x", "pr": f"{z}/counter-x", "pt": f"{z}/counter-y-top", "pb": f"{z}/counter-y-bottom",
                                "align": "CENTER", "counter": "CENTER", "w": "HUG", "h": "FIXED"},
                     "height": f"{z}/counter", "minW": f"{z}/counter"})
        root["children"] = [{"type": "text", "name": "1", "refs": {"characters": "Num of messages"},
                             "text": {"chars": "1", "style": f"typography/avatar/{size}/counter", "fontStyle": "SemiBold", "fill": "avatar/status/text"}}]
        props = [{"name": "Num of messages", "type": "TEXT", "default": "1"}]
    return {"name": f"_ Avatar / Counter / {size}", "description": "Бейдж-счётчик на аватаре. Приватная часть Avatar.",
            "axes": [], "exclude": [], "props": props, "root": root}


def button_x(size):
    z = f"avatar/size/{size}"
    return {"name": f"_ Avatar / button_X / {size}", "description": "Удаление аватара из выбора (например, участника). Приватная часть Avatar.",
            "axes": [], "exclude": [], "props": [{"name": "Focused", "type": "BOOLEAN", "default": False}],
            "root": {"type": "frame", "name": "root",
                     "layout": {"dir": "H", "px": f"{z}/button-x-xy", "py": f"{z}/button-x-xy", "align": "CENTER", "counter": "CENTER", "w": "FIXED", "h": "FIXED"},
                     "width": f"{z}/button-x", "height": f"{z}/button-x", "radius": f"{z}/button-x-radius", "fill": "avatar/button-x/box",
                     "stroke": {"color": "avatar/status/spacer", "weight": f"{z}/button-x-border", "align": "OUTSIDE"},
                     "children": [
                         {"type": "icon", "name": "x", "icon": {"name": "x", "size": f"{z}/button-x-icon", "color": "avatar/button-x/icon"}},
                         {"type": "rect", "name": "focus", "abs": "focus", "offset": 2, "visible": False, "refs": {"visible": "Focused"},
                          "radius": f"{z}/focus-radius-circle", "stroke": {"color": "avatar/box/border/focus", "weight": f"{z}/focus-border", "align": "INSIDE"}}]}}


def pos_by(table_fn):
    """Координаты по размеру и форме (Squared) — числами, как в файле."""
    x, y = {}, {}
    for s in SIZES:
        for sq in ("False", "True"):
            p = table_fn(s, "Square" if sq == "True" else "Circle")
            if p:
                x[f"{s}|{sq}"], y[f"{s}|{sq}"] = p
    return x, y


def public_avatar():
    sx, sy = pos_by(lambda s, sh: STATUS_POS[(s, sh)])
    bx, byy = pos_by(lambda s, sh: BADGE_POS.get((s, sh)) or BADGE_POS.get(s))
    xx, xy = pos_by(lambda s, sh: BUTTON_X_POS.get(s))
    vars_ = {"s": {"from": "Size"}, "shape": {"from": "Squared", "map": {"False": "Circle", "True": "Square"}},
             "stx": {"from": ["Size", "Squared"], "map": {k: str(v) for k, v in sx.items()}},
             "sty": {"from": ["Size", "Squared"], "map": {k: str(v) for k, v in sy.items()}},
             "bdx": {"from": ["Size", "Squared"], "map": {k: str(v) for k, v in bx.items()}},
             "bdy": {"from": ["Size", "Squared"], "map": {k: str(v) for k, v in byy.items()}},
             "bxx": {"from": ["Size", "Squared"], "map": {k: str(v) for k, v in xx.items()}},
             "bxy": {"from": ["Size", "Squared"], "map": {k: str(v) for k, v in xy.items()}}}
    z = "avatar/size/{s}"
    return {
        "name": "Avatar",
        "description": "Аватар идентифицирует человека или сущность. Circle — человек, Squared — объект. Фото, инициалы или иконка; статус; бейдж или крестик; имя и описание.",
        "axes": [{"name": "Type", "values": ["Default", "Badge", "Button-X"]}, {"name": "Squared", "values": ["False", "True"]},
                 {"name": "Size", "values": SIZES}],
        "exclude": [],  # Button-X у S есть в файле, но без крестика (у S его нет)
        "grid": {"columns": "Size", "blocks": "Squared", "rows": ["Type"]},
        "vars": vars_,
        "props": [{"name": "Status", "type": "BOOLEAN", "default": True}, {"name": "Text", "type": "BOOLEAN", "default": True},
                  {"name": "↳ Name", "type": "TEXT", "default": "Name"}, {"name": "↳ Description", "type": "TEXT", "default": "Description"},
                  {"name": "Description", "type": "BOOLEAN", "default": True}],
        "root": {
            "type": "frame", "name": "root", "layout": {"dir": "H", "gap": f"{z}/name-box-gap", "align": "MIN", "counter": "CENTER", "w": "HUG", "h": "HUG"},
            "children": [
                {"type": "frame", "name": "Container", "layout": {"dir": "H", "align": "MIN", "counter": "MIN", "w": "HUG", "h": "HUG"}, "children": [
                    {"type": "instance", "name": "Avatar", "expose": True,
                     "instance": {"set": "_ Avatar / {s} / {shape}", "variant": {"Style": "Image", "Type": "Photo", "Color": "Blue"}, "props": {}}},
                    {"type": "instance", "name": "Status", "abs": "at", "pos": {"x": "{stx}", "y": "{sty}"}, "refs": {"visible": "Status"},
                     "instance": {"set": "_ Avatar / Status / {s}", "variant": {"State": "Online"}, "props": {}}},
                    {"type": "instance", "name": "Badge", "when": {"Type": "Badge"}, "abs": "at", "pos": {"x": "{bdx}", "y": "{bdy}"},
                     "instance": {"set": "_ Avatar / Counter / {s}", "variant": {}, "props": {}}},
                    {"type": "instance", "name": "Button-X", "when": {"Type": "Button-X", "Size": ["2xl", "xl", "l", "m"]}, "abs": "at", "pos": {"x": "{bxx}", "y": "{bxy}"},
                     "instance": {"set": "_ Avatar / button_X / {s}", "variant": {}, "props": {}}},
                ]},
                {"type": "frame", "name": "Text", "refs": {"visible": "Text"},
                 "layout": {"dir": "V", "gap": by("Size", {s: (f"avatar/size/{s}/name-description-gap" if s != "s" else 0) for s in SIZES}),
                            "align": "CENTER", "counter": "MIN", "w": "HUG", "h": "HUG"},
                 "children": [
                     {"type": "text", "name": "Name", "refs": {"characters": "↳ Name"},
                      "text": {"chars": "Name", "style": "typography/avatar/{s}/name", "fontStyle": "Regular", "fill": "avatar/text/name"}},
                     {"type": "text", "name": "Description", "when": {"Size": ["2xl", "xl", "l", "m"]}, "refs": {"visible": "Description", "characters": "↳ Description"},
                      "text": {"chars": "Description", "style": "typography/avatar/{s}/description", "fontStyle": "Regular", "fill": "avatar/text/description"}}]},
            ],
        },
    }


def public_group():
    kids = [{"type": "instance", "name": str(k), **({"refs": {"visible": str(k)}} if k > 1 else {}),
             "instance": {"set": "_ Avatar-Group / {s} / {shape}", "variant": {"Style": "Image", "Type": "Photo", "Color": "Blue"},
                          "props": {"Grouped": True}}} for k in range(1, 8)]
    kids.append({"type": "instance", "name": "Counter", "refs": {"visible": "Counter"},
                 "instance": {"set": "_ Avatar-Group / {s} / {shape}-сounter", "variant": {"Style": "Soft"}, "props": {}}})
    return {
        "name": "Avatar-Group", "description": "Группа аватаров: участники проекта, чата, задачи. До 7 видимых и «+N». Не смешивайте Soft и Filled в одной группе.",
        "axes": [{"name": "Squared", "values": ["False", "True"]}, {"name": "Size", "values": SIZES}], "exclude": [],
        "grid": {"columns": "Size", "rows": ["Squared"]},
        "vars": {"s": {"from": "Size"}, "shape": {"from": "Squared", "map": {"False": "Circle", "True": "Square"}}},
        "props": [{"name": "Counter", "type": "BOOLEAN", "default": True}, *[{"name": str(k), "type": "BOOLEAN", "default": True} for k in range(2, 8)]],
        "root": {"type": "frame", "name": "root", "layout": {"dir": "H", "gap": "avatar/size/{s}/box-group-gap", "align": "MIN", "counter": "CENTER", "w": "HUG", "h": "HUG"},
                 "children": kids},
    }


def avatar():
    sets = []
    for s in SIZES:
        sets += [status_set(s), counter_comp(s)] + ([button_x(s)] if s != "s" else [])
    for s in SIZES:
        sets += [avatar_set(s, sh) for sh in SHAPES]
    for s in SIZES:
        sets += [avatar_set(s, sh, group=True) for sh in SHAPES] + [group_counter(s, sh) for sh in SHAPES]
    sets += [public_avatar(), public_group()]

    def av(t="Default", sq="False", size="m", props=None, label=None):
        x = {"set": "Avatar", "variant": {"Type": t, "Squared": sq, "Size": size}}
        if props:
            x["props"] = props
        if label:
            x["label"] = label
        return x

    def one(size, shape, style, typ, color, label=None, props=None):
        x = {"set": f"_ Avatar / {size} / {shape}", "variant": {"Style": style, "Type": typ, "Color": color}}
        if label:
            x["label"] = label
        if props:
            x["props"] = props
        return x

    no_text = {"Text": False, "Status": False}
    spec = {
        "title": "Avatar",
        "description": "Аватар идентифицирует человека или сущность. Форма — по природе носителя: Circle — человек, Square — объект. Наполнение (фото, инициалы, иконка) на форму не влияет.",
        "columns": [
            {"title": "Форма", "width": 360, "cards": [
                {"title": "Circle", "description": "Человек: пользователь, автор, участник", "items": [one("xl", "Circle", "Image", "Photo", "Blue"), one("xl", "Circle", "Soft", "Initials", "Blue")]},
                {"title": "Square", "description": "Объект: компания, проект, команда, интеграция, файл, бот", "items": [
                    one("xl", "Square", "Soft", "Компания", "Base", "Компания"), one("xl", "Square", "Soft", "Проекты", "Green", "Проект"),
                    one("xl", "Square", "Soft", "Интеграции", "Purple", "Интеграция"), one("xl", "Square", "Soft", "Боты", "Base", "Бот")]}]},
            {"title": "Наполнение", "width": 360, "cards": [
                {"title": "Приоритет", "description": "Фото → инициалы (1–2 буквы) → иконка User → Plus / +N для служебных функций",
                 "items": [one("l", "Circle", "Image", "Photo", "Blue", "Фото"), one("l", "Circle", "Soft", "Initials", "Blue", "Инициалы"),
                           one("l", "Circle", "Soft", "User Icon", "Base", "User"), one("l", "Circle", "Soft", "Plus", "Base", "Plus"),
                           one("l", "Circle", "Image", "Counter", "Base", "+N")]}]},
            {"title": "Стиль и цвет", "width": 360, "cards": [
                {"title": "Soft", "description": "Спокойный, по умолчанию", "items": [one("l", "Circle", "Soft", "Initials", c) for c in COLORS[:6]]},
                {"title": "Filled", "description": "Контрастный. Не смешивайте Soft и Filled в одной группе", "items": [one("l", "Circle", "Filled", "Initials", c) for c in COLORS[:6]]},
                {"title": "Inverse", "description": "На тёмных поверхностях", "inverse": True,
                 "items": [one("l", "Circle", "Soft", "Initials", "Inverse"), one("l", "Circle", "Filled", "Initials", "Inverse")]}]},
            {"title": "Размер", "width": 360, "cards": [
                {"title": s.upper(), "description": d, "items": [av(size=s)]} for s, d in
                [("2xl", "Профиль пользователя"), ("xl", "Карточки участников, крупные блоки"), ("l", "Шапка, навигация, профиль"),
                 ("m", "Списки, таблицы, карточки"), ("s", "Плотные интерфейсы, упоминания")]]},
            {"title": "Статус и бейдж", "width": 360, "cards": [
                {"title": "Статус", "description": "Online, Offline, Busy, Away, Other", "items": [
                    {"set": "_ Avatar / Status / xl", "variant": {"State": st}, "label": st} for st in STATUS]},
                {"title": "Badge", "description": "Счётчик непрочитанного", "items": [av("Badge", size="l", props={"Text": False})]},
                {"title": "Button-X", "description": "Удалить участника из выбора", "items": [av("Button-X", size="l", props={"Text": False})]}]},
            {"title": "Группа", "width": 360, "cards": [
                {"title": "Avatar-Group", "description": "На мобильных 3–4 видимых и счётчик", "items": [
                    {"set": "Avatar-Group", "variant": {"Squared": "False", "Size": "m"}},
                    {"set": "Avatar-Group", "variant": {"Squared": "True", "Size": "m"}}]}]},
            {"title": "Загрузка", "width": 360, "cards": [
                {"title": "Loading", "description": "Данные аватара ещё не пришли", "items": [one("l", "Circle", "Image", "Loading", "Base"), one("l", "Square", "Image", "Loading", "Base")]}]},
        ],
    }
    return {
        "component": "avatar", "title": "Avatar", "page": "Components / Avatar", "origin": "existing",
        "notes": [
            "Повтор Avatar из файла «Компоненты · Базовые»: 46 элементов (аватары 5 размеров × Circle/Square, статусы, счётчики, крестики, элементы группы и «+N», публичные Avatar и Avatar-Group), имена токенов — библиотеки.",
            "Форма по философии форм: Circle — человек, Square — объект; наполнение на форму не влияет.",
            "Фото — встроенная заглушка (замените своим изображением). Кольцо группы — на радиусе аватара (в файле — устаревший `~S/box-group-radius-*`).",
            "`_ Avatar / Counter` и `_ Avatar / button_X` — одиночные компоненты, как в файле.",
        ],
        "sets": sets,
        "spec": spec,
    }
