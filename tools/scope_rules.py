"""FEDS: правило scopes и публикации для переменных FEroom.

То же правило продублировано в tools/figma/scope-rules.js (для сверки с файлом).
Расхождения реального файла с правилом лежат в tools/scope-overrides.json и имеют приоритет.
"""
import json
import re
from pathlib import Path

OVERRIDES_FILE = Path(__file__).with_name("scope-overrides.json")
_OVR = json.loads(OVERRIDES_FILE.read_text(encoding="utf-8")) if OVERRIDES_FILE.exists() else {"scopes": {}, "hidden": {}}

FILL_PARTS = {"bg", "inverse-bg", "box", "box-group", "knob", "counter"}
TEXT_PARTS = {"text", "inverse-text", "label", "name", "description", "hint", "inverse-hint"}
SHAPE_PARTS = {"icon", "inverse-icon", "indicator", "status", "validation-icons", "leading-icon", "loading",
               "loader-icon", "inverse-loader-icon"}
STROKE_PARTS = {"border", "inverse-border", "line", "focus-ring", "inverse-focus-ring", "focus", "spacer", "divider"}
GAP_RE = re.compile(r"(^|-)(x|y|xy|gap|padding|top|bottom|left|right|horizontal|vertical)$|^(x|y|xy)-|-text$")
TRANSPARENT_NO_SCOPE = re.compile(r"^color/transparent-(brand|red|green|yellow|blue|purple)/")


def rule_scopes(level, name, vtype):
    s = name.split("/")
    if level == 1:
        if vtype == "COLOR":
            return [] if TRANSPARENT_NO_SCOPE.match(name) else ["ALL_FILLS", "EFFECT_COLOR", "STROKE_COLOR"]
        root = s[0]
        if root == "font":
            return {"size": ["FONT_SIZE"], "line-height": ["LINE_HEIGHT"], "weight": ["FONT_WEIGHT"],
                    "letter-spacing": ["LETTER_SPACING", "PARAGRAPH_INDENT"]}.get(s[1], [])
        return {"size": ["WIDTH_HEIGHT"], "space": ["GAP"], "radius": ["CORNER_RADIUS"], "border": ["STROKE_FLOAT"],
                "opacity": ["EFFECT_FLOAT", "OPACITY", "STROKE_FLOAT", "TEXT_CONTENT"]}.get(root, ["EFFECT_FLOAT"])
    if level == 2:
        root = s[0]
        if root == "color":
            g = "/".join(s[:3])
            if g in ("color/action/bg", "color/static/bg") or s[1] in ("bg", "surface"):
                return ["FRAME_FILL"]
            if g in ("color/action/text", "color/static/text"):
                return ["TEXT_FILL"]
            if g in ("color/action/border", "color/static/border", "color/static/focus"):
                return ["STROKE_COLOR"]
            if g in ("color/action/indicator", "color/static/indicator"):
                return ["SHAPE_FILL"]
            if g == "color/static/divider":
                return ["FRAME_FILL", "SHAPE_FILL"]
            if s[1] == "status":
                if s[-1].startswith("on"):
                    return ["ALL_FILLS"]
                return ["STROKE_COLOR"] if "border" in s[-1] else ["FRAME_FILL"]
            return ["FRAME_FILL"]
        if root == "typography":
            return {"size": ["FONT_SIZE"], "line-height": ["LINE_HEIGHT"], "letter-spacing": ["LETTER_SPACING"],
                    "weight": ["FONT_WEIGHT"]}.get(s[-1], [])
        return {"space": ["GAP"], "gap": ["GAP"], "size": ["WIDTH_HEIGHT"], "radius": ["CORNER_RADIUS"],
                "border": ["STROKE_FLOAT"], "effects": ["EFFECT_FLOAT"]}.get(root, ["ALL_SCOPES"])
    # level 3
    if vtype == "COLOR":
        if len(s) > 1 and s[1] == "loading":
            return ["FRAME_FILL"]
        if s[-1].startswith("text-"):
            return ["TEXT_FILL"]
        for seg in reversed(s[1:]):
            if seg in FILL_PARTS:
                return ["FRAME_FILL"]
            if seg in TEXT_PARTS:
                return ["TEXT_FILL"]
            if seg in SHAPE_PARTS:
                return ["SHAPE_FILL"]
            if seg in STROKE_PARTS:
                return ["STROKE_COLOR"]
        return ["SHAPE_FILL"] if s[-1] == "error" else ["FRAME_FILL"]
    last = s[-1]
    if "radius" in last:
        return ["CORNER_RADIUS"]
    if "border" in last:
        return ["STROKE_FLOAT"]
    if GAP_RE.search(last) or last.startswith("gap"):
        return ["GAP"]
    return ["WIDTH_HEIGHT"]


def rule_hidden(level, name):
    """Публикация: L1 скрыт, L3 опубликован, L2 — по группам (сверено с файлом, ~7 расхождений в color/static/bg/solid)."""
    if level == 1:
        return True
    if level == 3:
        return False
    s = name.split("/")
    if s[0] == "color":
        return s[1] in ("action", "status") or name.startswith("color/static/bg/") or             name in ("color/surface/brand/pressed", "color/surface/brand/hover", "color/surface/brand/selected")
    if s[0] == "typography":
        return len(s) < 2 or s[1] != "avatar"
    return (s[0] in ("radius", "border", "size") and len(s) > 1 and s[1] in ("button", "link")) or name.startswith("size/field/")


def scopes(level, name, vtype):
    return _OVR["scopes"].get(name) or rule_scopes(level, name, vtype)


def hidden(level, name):
    return _OVR["hidden"].get(name, rule_hidden(level, name))
