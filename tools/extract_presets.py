"""FEDS: пресеты из текущей системы — база (L1 + общий L2) и 13 готовых компонентов.

Нужны, чтобы плагин мог:
  • собрать систему с нуля в пустом файле (system → компоненты);
  • сверить и дополнить существующий файл (повторный запуск = 0 изменений).

Источник: analysis/token-index.json (из input/tokens/variables.json) + tools/scope_rules.py + tools/text-styles.tsv.
Запуск: python tools/extract_presets.py   → presets/_system.tokens.json, presets/{component}.tokens.json
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import scope_rules  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
INDEX = json.loads((ROOT / "analysis" / "token-index.json").read_text(encoding="utf-8"))
BY_REF = {v["ref"]: v for v in INDEX}

# Готовые компоненты: пресет → (заголовок, страница Figma, источник документации)
COMPONENTS = {
    "avatar": ("Avatar", "input/builds/avatar/avatar-avatar-group.md"),
    "badge": ("Badge", "input/builds/badge/badge.md"),
    "button": ("Button", "input/builds/button/button.md"),
    "checkbox": ("Checkbox", "input/builds/checkbox/checkboxcheckboxcard.md"),
    "chip": ("Chip", "input/builds/chip/chip.md"),
    "divider": ("Divider", "input/builds/divider/divider.md"),
    "link": ("Link", "input/builds/link/link.md"),
    "priority-indicator": ("Priority Indicator", "input/builds/priority-indicator/priority-indicator.md"),
    "radiobutton": ("Radiobutton", "input/builds/radiobutton/radiobuttonradiobuttoncard.md"),
    "status": ("Status", "input/builds/status/status.md"),
    "switch": ("Switch", "input/builds/switch/switchtoggle.md"),
    "field": ("Input, Text Area, Field", "input/builds/field/field.md"),
    "field-select": ("SimpleSelect", "input/builds/simple-select/select.md"),
}
SIZE_ROOTS = {"size", "space", "gap", "radius", "border", "effects", "typography"}
WEIGHT_STYLE = {"Regular": 400, "Medium": 500, "SemiBold": 600, "Bold": 700}


def l3_owner(name):
    s = name.split("/")
    if s[0] != "field":
        return s[0]
    if s[1] == "select" or (s[1] == "size" and len(s) > 2 and s[2] == "select"):
        return "field-select"
    return "field"


def l2_owner(name):
    s = name.split("/")
    if s[0] in SIZE_ROOTS and len(s) > 1:
        comp = s[1]
        if comp == "field":
            return "field-select" if len(s) > 2 and s[2] == "select" else "field"
        if comp in COMPONENTS:
            return comp
    return "system"


def vtype(v):
    return "COLOR" if v["type"] == "color" else "FLOAT"


def target_name(val):
    return BY_REF[val]["name"] if isinstance(val, str) and val.startswith("{") else None


def hex_color(rgba):
    """Непрозрачный цвет — #rrggbb; полупрозрачный — rgba() с точной альфой (hex её округляет)."""
    r, g, b, a = [float(x) for x in rgba[5:-1].split(",")]
    if a >= 1:
        return "#" + "".join(f"{int(c):02x}" for c in (r, g, b))
    return f"rgba({int(r)},{int(g)},{int(b)},{a:g})"


def l1_item(v):
    val = v["modes"]["mode_1"]
    value = hex_color(val) if isinstance(val, str) and val.startswith("rgba") else val
    return {"name": v["name"], "type": vtype(v), "value": value, "scopes": scope_rules.scopes(1, v["name"], vtype(v)),
            "hidden": scope_rules.hidden(1, v["name"]), "description": v["description"]}


def l2_item(v, exceptions):
    vals = {}
    for m in ("light", "dark"):
        raw = v["modes"][m]
        vals[m] = target_name(raw) if target_name(raw) else raw
        if not target_name(raw):
            exceptions.append({"token": v["name"], "reason": "сырое значение в L2 (так в текущем файле)"})
    item = {"name": v["name"], "type": vtype(v), "scopes": scope_rules.scopes(2, v["name"], vtype(v)), "values": vals,
            "hidden": scope_rules.hidden(2, v["name"]), "description": v["description"]}
    return item


def l3_item(v):
    return {"name": v["name"], "type": vtype(v), "alias": target_name(v["modes"]["mode_1"]),
            "scopes": scope_rules.scopes(3, v["name"], vtype(v)), "description": v["description"]}


def text_styles():
    out = []
    for line in (ROOT / "tools" / "text-styles.tsv").read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        name, style, base = line.split("\t")
        out.append({"name": name, "fontFamily": "Roboto", "fontStyle": style, "vars": {
            "fontSize": f"{base}/size", "lineHeight": f"{base}/line-height",
            "letterSpacing": f"{base}/letter-spacing", "fontWeight": f"{base}/weight"}})
    return out


def dedupe(items):
    seen, out = set(), []
    for x in items:
        key = json.dumps(x, sort_keys=True, ensure_ascii=False)
        if key not in seen:
            seen.add(key)
            out.append(x)
    return out


def main():
    presets = {c: {"l2": [], "l3": [], "textStyles": [], "exceptions": []} for c in COMPONENTS}
    system = {"l1": [], "l2": [], "textStyles": [], "exceptions": []}

    for v in sorted(INDEX, key=lambda x: x["name"]):
        if v["level"] == 1:
            system["l1"].append(l1_item(v))
        elif v["level"] == 2:
            owner = l2_owner(v["name"])
            bucket = system if owner == "system" else presets[owner]
            bucket["l2"].append(l2_item(v, bucket["exceptions"]))
        else:
            presets[l3_owner(v["name"])]["l3"].append(l3_item(v))

    for st in text_styles():
        owner = l2_owner(st["vars"]["fontSize"])
        (system if owner == "system" else presets[owner])["textStyles"].append(st)

    out_dir = ROOT / "presets"
    common = {"origin": "existing", "source": "input/tokens/variables.json"}
    sys_preset = {
        "component": "system", "title": "Система: L1 + общий L2", "kind": "system", **common,
        "decisions": [
            "Базовый слой для сборки с нуля: все примитивы `1. Primitives` и общий `2. General` (цвет, общая типографика).",
            "Размеры и типографика компонентов лежат в пресетах компонентов (`size|space|gap|radius|border|typography/{component}/…`).",
            "scopes и публикация восстановлены правилом tools/scope_rules.py + исключения tools/scope-overrides.json.",
            "Эффект-стили не входят (отложены автором). codeSyntax не заполняется.",
        ],
        "l1": system["l1"], "l2": system["l2"], "l3": [], "textStyles": system["textStyles"],
        "exceptions": dedupe(system["exceptions"]),
    }
    (out_dir / "_system.tokens.json").write_text(json.dumps(sys_preset, ensure_ascii=False, indent=1), encoding="utf-8")

    for comp, (title, src) in COMPONENTS.items():
        p = presets[comp]
        preset = {
            "component": comp, "title": title, "kind": "component", **common, "doc": src,
            "roots": ["field"] if comp.startswith("field") else [comp],
            "prefixes": ["field/select/", "field/size/select/"] if comp == "field-select" else
            ([f"field/{x}/" for x in ("input", "label", "description", "counter")] +
             [f"field/size/{x}/" for x in ("input", "text-area", "label", "description", "field")]) if comp == "field" else [comp + "/"],
            "decisions": ["Пресет снят с текущей системы: повторная запись в исходный файл должна дать 0 изменений."],
            "l2": p["l2"], "l3": p["l3"], "textStyles": p["textStyles"], "exceptions": dedupe(p["exceptions"]),
        }
        (out_dir / f"{comp}.tokens.json").write_text(json.dumps(preset, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"{comp:20} L2 {len(p['l2']):4}  L3 {len(p['l3']):4}  стилей {len(p['textStyles'])}")
    print(f"{'system':20} L1 {len(system['l1'])}  L2 {len(system['l2'])}  стилей {len(system['textStyles'])}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
