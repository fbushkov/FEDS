"""FEDS: описание сборки Chip — повтор устройства из файла «Компоненты · Базовые» по именам токенов библиотеки.

Устройство (разбор файла 22.09.2026, только чтение):
- наборы Chip / Circle и Chip / Squared по 420 вариантов: State × Size × (обычный | Avatar | Group) × Color × Filled;
- Avatar и Group не сочетаются; Avatar — экземпляр `_ Avatar / {s} / Circle|Square` той же формы, что и чип
  (однородная группа — одна форма, docs/filosofiya-form);
- Group — «Название: Элемент»: Head с двоеточием и Content вторичным цветом;
- крестик — системная Button / Icon Only (не своя кнопка): тип по виду и цвету, как в файле;
- Disabled — без крестика и кольца фокуса; Loading — подложка без рамки, содержимое прозрачное (ширина сохраняется),
  аватар — Type Loading. Это та же форма, что у Skeleton: пилюля/плашка на месте чипа.

Отличия от файла: имена токенов — библиотеки (`chip/text/*/disabled`, а не `disebled`; высота крестика — размер Button,
устаревшего `chip/size/M/icon_x` в библиотеке нет).

Используется из tools/gen_build.py.
"""

STATES = ["Default", "Hover", "Pressed / Selected", "Disabled", "Loading"]
SIZES = ["M", "S"]
COLORS = ["Gray", "Blue", "Red", "Green", "Yellow", "Purple", "White"]
COLOR_TOKEN = {"Gray": "base", "Blue": "blue", "Red": "red", "Green": "green", "Yellow": "yellow", "Purple": "purple", "White": "base-inverse"}
SHAPES = {"Circle": ("circle", "Circle"), "Squared": ("square", "Square")}

# Button / Icon Only для крестика: (Filled, Color) → Type (как в файле)
X_TYPE = {}
for c in COLORS:
    X_TYPE[f"False|{c}"] = {"Blue": "Primary", "Red": "Danger", "White": "Inverse-primary"}.get(c, "Secondary")
    # на заливке: светлая иконка, на жёлтой и белой — тёмная (контраст AA); у цветных заливок тема закреплена светлой
    # (заливки одинаковы в обеих темах, а Inverse-primary в тёмной теме тёмный — как у Alert Bold)
    X_TYPE[f"True|{c}"] = "Secondary" if c in ("White", "Yellow") else "Inverse-primary"

DESC = ("Компактный элемент: выбранное значение, фильтр, тег или сущность. Может содержать иконку или аватар, "
        "подсказку, счётчик и кнопку удаления. Group — «Название: значение» для фильтров.")


def by(axis, mapping):
    return {"by": axis, "map": mapping}


def chip_set(shape):
    radius, avatar_shape = SHAPES[shape]
    z = "chip/size/{s}"
    live = ["Default", "Hover", "Pressed / Selected", "Loading"]
    loading_hidden = by("State", {"Loading": 0})

    def text(name, chars, part, tone, refs=None):
        # tone: main | secondary; Disabled — свой цвет
        return {"type": "text", "name": name, **({"refs": refs} if refs else {}),
                "text": {"chars": chars, "style": f"typography/action/chip/{{s}}/{part}", "fontStyle": "Regular",
                         "fill": f"chip/text/{{f}}/{{t_{tone}}}/{{c}}"}}

    counter = {
        "type": "frame", "name": "Counter", "refs": {"visible": "Counter"},
        "layout": {"dir": "H", "pl": f"{z}/counter-x", "pr": f"{z}/counter-x", "pt": f"{z}/counter-y-top", "pb": f"{z}/counter-y-bottom",
                   "align": "MIN", "counter": "CENTER", "w": "HUG", "h": "HUG"},
    }
    plain = [
        {**text("Additional", "Подсказка", "description", "secondary", {"visible": "Hint Text", "characters": "↳ Hint"}), "when": {"Group": "False"}},
        {"type": "frame", "name": "Content", "when": {"Group": "False"},
         "layout": {"dir": "H", "gap": f"{z}/counter-gap", "align": "MIN", "counter": "CENTER", "w": "HUG", "h": "HUG"},
         "children": [
             text("Name", "Название", "name", "main", {"characters": "↳ Name"}),
             {**counter, "children": [text("+", ", +", "name", "main"), text("Num", "1", "name", "main", {"characters": "↳ Num"})]},
         ]},
    ]
    group = [
        {"type": "frame", "name": "Head", "when": {"Group": "True"},
         "layout": {"dir": "H", "align": "CENTER", "counter": "CENTER", "w": "HUG", "h": "HUG"},
         "children": [text("Head", "Название", "head", "main", {"characters": "↳ Head"}), text(":", ":", "head", "main")]},
        {"type": "frame", "name": "Content", "when": {"Group": "True"},
         "layout": {"dir": "H", "gap": f"{z}/counter-gap", "align": "MIN", "counter": "CENTER", "w": "HUG", "h": "HUG"},
         "children": [
             text("Content", "Элемент", "name", "secondary", {"characters": "↳ Content"}),
             {**counter, "children": [text("+", ", +", "name", "secondary"), text("Num", "1", "name", "secondary", {"characters": "↳ Num"})]},
         ]},
    ]
    root = {
        "type": "frame", "name": "root",
        "layout": {"dir": "H", "gap": f"{z}/box-gap",
                   "pl": by("Avatar", {"False": f"{z}/box-x", "True": f"{z}/box-avatar-x"}), "pr": f"{z}/box-x",
                   "pt": by("Avatar", {"False": f"{z}/box-y", "True": f"{z}/box-avatar-y"}),
                   "pb": by("Avatar", {"False": f"{z}/box-y", "True": f"{z}/box-avatar-y"}),
                   "align": "MIN", "counter": "CENTER", "w": "HUG", "h": "FIXED"},
        "height": f"{z}/box", "radius": f"{z}/box-radius-{radius}",
        "fill": "chip/bg/{f}/{c}/{stb}",
        "stroke": {"color": by("State", {"Loading": "", **{st: "chip/border/{f}/{c}/{sts}" for st in STATES[:4]}}),
                   "weight": f"{z}/box-border", "align": "INSIDE"},
        "children": [
            {"type": "rect", "name": "Focus Ring", "when": {"State": live}, "abs": "focus", "offset": 3,
             "visible": False, "refs": {"visible": "Focused"}, "radius": f"{z}/focus-radius-{radius}",
             "stroke": {"color": "chip/border/focus", "weight": f"{z}/focus-border", "align": "INSIDE"}},
            {"type": "icon", "name": "Icon", "when": {"Avatar": "False"}, "opacity": loading_hidden,
             "refs": {"visible": "Icon", "mainComponent": "↳ Icon"},
             "icon": {"name": "circle", "size": f"{z}/icon", "color": "chip/icon/{fi}/{c}"}},
            {"type": "instance", "name": "Avatar", "when": {"Avatar": "True"},
             "instance": {"set": f"_ Avatar / {{s}} / {avatar_shape}",
                          "variant": {"Style": "Image", "Type": "{at}", "Color": "{ac}"}, "props": {}}},
            {"type": "frame", "name": "Text", "opacity": loading_hidden,
             "layout": {"dir": "H", "gap": f"{z}/text-gap",
                        "pl": by("Avatar", {"False": f"{z}/text-x", "True": f"{z}/text-avatar-x"}), "pr": f"{z}/text-x",
                        "pt": f"{z}/text-y-top", "pb": f"{z}/text-y-bottom", "align": "MIN", "counter": "CENTER", "w": "HUG", "h": "HUG"},
             "children": plain + group},
            {"type": "instance", "name": "X-icon", "when": {"State": live}, "opacity": loading_hidden, "refs": {"visible": "X-icon"},
             "theme": "{xth}",
             "instance": {"set": "Button / Icon Only", "variant": {"Size": "{S}", "Type": "{xt}", "State": "Default", "Loading": "False"},
                          "props": {"↳ Icon": "icon:x"}}},
        ],
    }
    return {
        "name": f"Chip / {shape}", "description": DESC,
        "axes": [{"name": "State", "values": STATES}, {"name": "Size", "values": SIZES},
                 {"name": "Avatar", "values": ["False", "True"]}, {"name": "Group", "values": ["False", "True"]},
                 {"name": "Color", "values": COLORS}, {"name": "Filled", "values": ["False", "True"]}],
        "exclude": [{"Avatar": "True", "Group": "True"}],
        "grid": {"columns": "State", "blocks": "Size", "rows": ["Filled", "Avatar", "Group", "Color"],
                 "split": {"axis": "Color", "values": ["White"]}},
        "a11y": {"exempt": {"State": ["Disabled", "Loading"]},
                 "surfaces": {"axis": "Color", "map": {"White": ["color/bg/section/inverse-main"]}},
                 "reason": "Disabled — недоступный элемент (WCAG 1.4.3 не требует контраста), Loading — содержимое скрыто"},
        "vars": {
            "s": {"from": "Size", "case": "lower"}, "S": {"from": "Size"},
            "f": {"from": "Filled", "map": {"False": "soft", "True": "hard"}},
            "c": {"from": "Color", "map": COLOR_TOKEN},
            "stb": {"from": "State", "map": {"Default": "default", "Hover": "hover", "Pressed / Selected": "active", "Disabled": "default", "Loading": "default"}},
            "sts": {"from": "State", "map": {"Default": "default", "Hover": "hover", "Pressed / Selected": "active", "Disabled": "disabled", "Loading": "default"}},
            "fi": {"from": ["Filled", "State"], "map": {f"{fl}|{st}": ("hard" if fl == "True" else "soft") + ("-disabled" if st == "Disabled" else "")
                                                         for fl in ("False", "True") for st in STATES}},
            "t_main": {"from": "State", "map": {**{st: "main" for st in STATES}, "Disabled": "disabled"}},
            "t_secondary": {"from": "State", "map": {**{st: "secondary" for st in STATES}, "Disabled": "disabled"}},
            "at": {"from": "State", "map": {**{st: "Photo" for st in STATES}, "Loading": "Loading"}},
            "ac": {"from": "State", "map": {**{st: "Blue" for st in STATES}, "Loading": "Base"}},
            "xt": {"from": ["Filled", "Color"], "map": X_TYPE},
            # цветные заливки Filled одинаковы в обеих темах — крестик берёт значения светлой; Gray и White следуют теме
            "xth": {"from": ["Filled", "Color"], "map": {f"{fl}|{c}": ("light" if fl == "True" and c not in ("Gray", "White") else "")
                                                          for fl in ("False", "True") for c in COLORS}},
        },
        "props": [
            {"name": "↳ Hint", "type": "TEXT", "default": "Подсказка"},
            {"name": "Hint Text", "type": "BOOLEAN", "default": True},
            {"name": "↳ Name", "type": "TEXT", "default": "Название"},
            {"name": "Icon", "type": "BOOLEAN", "default": True},
            {"name": "↳ Icon", "type": "INSTANCE_SWAP", "default": "circle"},
            {"name": "X-icon", "type": "BOOLEAN", "default": True},
            {"name": "Counter", "type": "BOOLEAN", "default": True},
            {"name": "↳ Num", "type": "TEXT", "default": "1"},
            {"name": "Focused", "type": "BOOLEAN", "default": False},
            {"name": "↳ Content", "type": "TEXT", "default": "Элемент"},
            {"name": "↳ Head", "type": "TEXT", "default": "Название"},
        ],
        "root": root,
    }


def chip():
    base = "Chip / Circle"

    def v(state="Default", size="M", avatar="False", group="False", color="Blue", filled="False"):
        return {"State": state, "Size": size, "Avatar": avatar, "Group": group, "Color": color, "Filled": filled}

    def it(set_, variant, props=None, label=None):
        x = {"set": set_, "variant": variant}
        if props:
            x["props"] = props
        if label:
            x["label"] = label
        return x

    simple = {"Hint Text": False, "Counter": False}
    spec = {
        "title": "Chip", "description": DESC,
        "columns": [
            {"title": "Форма", "width": 360, "cards": [
                {"title": "Circle", "description": "Люди и их выбор: участники, упоминания, пользовательские теги", "items": [it("Chip / Circle", v(avatar="True"), simple)]},
                {"title": "Squared", "description": "Система и объекты: фильтры, статусы, категории, проекты. В одной группе — одна форма",
                 "items": [it("Chip / Squared", v(), simple)]}]},
            {"title": "Размер", "width": 360, "cards": [
                {"title": "M", "description": "Стандартный: поля выбора, фильтры, карточки", "items": [it(base, v(size="M"), simple)]},
                {"title": "S", "description": "Плотные таблицы, списки, поле Multiselect размера S и M", "items": [it(base, v(size="S"), simple)]}]},
            {"title": "Вид и цвет", "width": 360, "cards": [
                {"title": "Soft", "items": [it(base, v(color=c), simple) for c in COLORS[:6]]},
                {"title": "Filled", "description": "Акцент: выбранный фильтр, важная метка", "items": [it(base, v(color=c, filled="True"), simple) for c in COLORS[:6]]}]},
            {"title": "Конфигурация", "width": 360, "cards": [
                {"title": "Иконка", "items": [it(base, v(), simple)]},
                {"title": "Аватар", "items": [it(base, v(avatar="True"), simple)]},
                {"title": "Подсказка и счётчик", "items": [it(base, v())]},
                {"title": "Group", "description": "«Название: значение» — фильтр со значением; счётчик — сколько ещё значений",
                 "items": [it("Chip / Squared", v(group="True"))]},
                {"title": "Без удаления", "description": "Только для чтения: метка без действия", "items": [it(base, v(), {**simple, "X-icon": False})]}]},
            {"title": "Состояния", "width": 360, "cards": [
                {"title": "Mouse", "items": [it(base, v(state=st), simple, st) for st in STATES[:4]]},
                {"title": "Keyboard", "items": [it(base, v(), {**simple, "Focused": True}, "Focused")]},
                {"title": "Loading", "description": "Значение загружается: форма чипа без содержимого", "items": [it(base, v(state="Loading"), simple), it(base, v(state="Loading", avatar="True"), simple)]}]},
            {"title": "Инверсия", "width": 360, "cards": [
                {"title": "White", "description": "На тёмных поверхностях — цвет White", "inverse": True,
                 "items": [it(base, v(color="White"), simple), it(base, v(color="White", filled="True"), simple)]}]},
        ],
    }
    return {
        "component": "chip", "title": "Chip", "page": "Components / Chip", "origin": "existing",
        "requires": ["avatar", "button"],
        "notes": [
            "Повтор Chip из файла «Компоненты · Базовые»: Circle и Squared по 420 вариантов, оси и свойства как в файле, имена токенов — библиотеки.",
            "Avatar — экземпляр `_ Avatar / {s} / Circle|Square` той же формы; крестик — Button / Icon Only (тип по виду и цвету, как в файле).",
            "Disabled — без крестика и фокуса; Loading — форма чипа без содержимого.",
        ],
        "sets": [chip_set("Circle"), chip_set("Squared")],
        "spec": spec,
    }
