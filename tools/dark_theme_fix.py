"""FEDS: исправление тёмной темы (колонка dark в `2. General`) по WCAG 2.1 AA.

Что делает (только режим dark; light, имена и связи L3 → L2 → L1 не меняются):
  A. Насыщенные заливки (кнопки Primary/Danger, Status/Badge hard): в dark фон темнеет до ступени,
     на которой белый текст ≥ 4.5:1 (hover/pressed — следующие ступени). Жёлтый — тёмный текст на жёлтом.
  B. Calm/soft-цвета действий и visited: вместо полупрозрачных копий light — светлые сплошные ступени.
  C. Рамки контролов: ≥ 3:1 к поверхности (WCAG 1.4.11); Outline Secondary получает рамку контрола.
  D. Шкала полупрозрачного текста в dark: soft/light/visited читаются (≥ 4.5:1).
  E. Мягкие Status/Badge: текст на мягком фоне ≥ 4.5:1.
  Новый L2 `color/action/{text,indicator}/base/on-bold/*` — белый поверх насыщенной заливки в обеих темах
  (раньше кнопки брали `inverse-hard`, который в dark становится чёрным).
Каждое изменение помечается в пресете `change: {was, approved}`; валидатор и дифф плагина показывают его как «отличается».

Запуск: python tools/dark_theme_fix.py [--dry]
"""
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WHY = "2026-09-21, тёмная тема: контраст WCAG AA"
IDX = {x["name"]: x for x in json.load(open(ROOT / "analysis/token-index.json", encoding="utf-8"))}
SYS_PATH = ROOT / "presets/_system.tokens.json"
SYS = json.load(open(SYS_PATH, encoding="utf-8"))
L2 = {t["name"]: t for t in SYS["l2"]}
SURFACE_DARK = "color/neutral/900"   # color/bg/section/main в dark
INVERSE_DARK = "color/neutral/0"     # color/bg/section/inverse-main в dark


def rgba(n):
    m = re.findall(r"[\d.]+", IDX[n]["modes"]["mode_1"])
    return [float(m[0]) / 255, float(m[1]) / 255, float(m[2]) / 255, float(m[3]) if len(m) > 3 else 1.0]


def lum(c):
    f = lambda x: x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4  # noqa: E731
    return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2])


def blend(fg, bg):
    return [fg[i] * fg[3] + bg[i] * (1 - fg[3]) for i in range(3)] + [1.0]


def contrast(fg, bg, base=SURFACE_DARK):
    b = blend(rgba(bg), rgba(base))
    la, lb = sorted([lum(blend(rgba(fg), b)), lum(b)], reverse=True)
    return (la + 0.05) / (lb + 0.05)


def dark(n):
    return L2[n]["values"]["dark"]


def first(steps, ok):
    for s in steps:
        if s in IDX and ok(s):
            return s
    raise SystemExit(f"нет подходящей ступени среди {steps}")


CHANGES = {}   # L2 → новый dark


def put(name, value):
    if name in L2 and dark(name) != value:
        CHANGES[name] = value


# A. насыщенные заливки с белым текстом
def bold(prefix, hue, states):
    steps = [f"color/{hue}/{n}" for n in (500, 550, 600, 650, 700, 750)]
    s0 = steps.index(first(steps, lambda s: contrast("color/neutral/0", s) >= 4.5))
    for i, st in enumerate(states):
        put(f"{prefix}/{st}", steps[min(s0 + i, len(steps) - 1)])


bold("color/action/bg/brand/medium", "brand", ["default", "hover", "pressed"])
bold("color/action/bg/danger/medium", "red", ["default", "hover", "pressed"])
for hue in ["brand", "blue", "red", "purple", "green"]:
    bold(f"color/status/{hue}/medium", hue, ["default", "hover", "active"])
# жёлтый: белый текст на жёлтом не читается ни в одной теме — тёмный текст (как warning во всех крупных ДС)
put("color/status/yellow/medium/on", "color/neutral/900")
put("color/status/yellow/medium/on-secondary", "color/transparent-black/700")
put("color/status/yellow/medium/active", "color/yellow/450")

# B. calm и visited: сплошные светлые ступени вместо полупрозрачных копий light
for hue, fam in [("brand", "brand"), ("red", "danger")]:
    txt = lambda n: first([f"color/{hue}/{s}" for s in (350, 300, 250)], lambda s: contrast(s, SURFACE_DARK) >= n)  # noqa: E731
    put(f"color/action/text/{fam}/calm/default", txt(4.5))
    put(f"color/action/text/{fam}/calm/hover", f"color/{hue}/300")
    put(f"color/action/text/{fam}/calm/visited", txt(4.5))
    put(f"color/action/text/{fam}/firm/visited", txt(4.5))
    put(f"color/action/indicator/{fam}/calm/default", txt(3))
    put(f"color/action/indicator/{fam}/calm/hover", f"color/{hue}/300")
    put(f"color/action/border/{fam}/calm/default", first([f"color/{hue}/{s}" for s in (600, 550, 500)], lambda s: contrast(s, SURFACE_DARK) >= 3))
    put(f"color/action/border/{fam}/calm/hover", f"color/{hue}/500")
    put(f"color/action/border/{fam}/calm/pressed", f"color/{hue}/450")   # в dark стояло transparent-blue — опечатка

# C. рамки контролов ≥ 3:1
w = lambda n: f"color/transparent-white/{n}"  # noqa: E731
b = lambda n: f"color/transparent-black/{n}"  # noqa: E731
ctrl = first([w(n) for n in (300, 350, 400, 450)], lambda s: contrast(s, SURFACE_DARK) >= 3)
k = [300, 350, 400, 450, 500, 550, 600, 650].index(int(ctrl.rsplit("/", 1)[1]))
put("color/action/border/base/controls/default", ctrl)
put("color/action/border/base/controls/hover", w([300, 350, 400, 450, 500, 550, 600, 650][k + 2]))
put("color/action/border/base/controls/pressed", w([300, 350, 400, 450, 500, 550, 600, 650][k + 4]))

# D. шкала полупрозрачного текста в dark
soft = first([w(n) for n in (350, 400, 450, 500, 550)], lambda s: contrast(s, SURFACE_DARK) >= 4.5)
put("color/static/text/base/soft", soft)
put("color/static/text/base/light", w(int(soft.rsplit("/", 1)[1]) + 50))         # light остаётся сильнее soft
put("color/action/text/base/medium/visited", w(int(soft.rsplit("/", 1)[1]) + 50))
inv = first([b(n) for n in (350, 400, 450, 500, 550, 600)], lambda s: contrast(s, INVERSE_DARK, INVERSE_DARK) >= 4.5)
put("color/static/text/base/inverse-soft", inv)
put("color/static/indicator/base/inverse-soft", inv)
put("color/static/text/base/inverse-light", b(int(inv.rsplit("/", 1)[1]) + 50))   # light сильнее soft, как в прямой шкале

# E. мягкие Status/Badge: текст на мягком фоне
for hue in ["brand", "blue", "red", "purple", "green", "yellow"]:
    bg = f"color/status/{hue}/soft/default"
    if bg not in L2:
        continue
    bgv = dark(bg)
    for part, need in [("on", 4.5), ("on-secondary", 4.5)]:
        n = f"color/status/{hue}/soft/{part}"
        if n in L2 and contrast(dark(n), bgv) < need:
            put(n, first([f"color/{hue}/{s}" for s in (450, 400, 350, 300, 250, 200)], lambda s: contrast(s, bgv) >= need))

# F. firm (текст и иконки brand/danger): каждое состояние — своя ступень на своей soft-подложке и на поверхности
#    (кнопки в hover/pressed берут firm/{state}, см. tools/light_theme_fix.py); в dark hover/pressed светлее default;
#    иконка той же ступени, что текст
for hue, fam in [("brand", "brand"), ("red", "danger")]:
    steps = [f"color/{hue}/{n}" for n in (450, 400, 350, 300, 250, 200)]
    lo = 0
    for state in ("default", "hover", "pressed"):
        g = dark(f"color/action/bg/{fam}/light/{state}")
        s_ = first(steps[lo:], lambda s: min(contrast(s, SURFACE_DARK), contrast(s, g)) >= 4.5)
        lo = min(steps.index(s_) + 1, len(steps) - 1)
        for kind in ("text", "indicator"):
            put(f"color/action/{kind}/{fam}/firm/{state}", s_)
            if state == "pressed":
                put(f"color/action/{kind}/{fam}/calm/pressed", s_)
# текст второго уровня на насыщенных Chip/Status
for hue in ["brand", "blue", "red", "purple", "green"]:
    put(f"color/status/{hue}/medium/on-secondary",
        first([w(900), w(950), "color/neutral/0"], lambda s: contrast(s, dark(f"color/status/{hue}/medium/default")) >= 4.5))
# Priority Indicator: иконка на светлой подложке своего цвета
put("color/static/indicator/palette/red-low",
    first([f"color/red/{s}" for s in (550, 500, 450, 400, 350)],
          lambda s: contrast(s, dark("color/static/bg/transparent/accent/red/light")) >= 3))

# новый L2: белый поверх насыщенной заливки
NEW = []
for part, scope in [("text", ["TEXT_FILL"]), ("indicator", ["SHAPE_FILL", "STROKE_COLOR"])]:
    for st in ["default", "hover", "pressed"]:
        NEW.append({"name": f"color/action/{part}/base/on-bold/{st}", "type": "COLOR", "scopes": scope,
                    "values": {"light": "color/neutral/0", "dark": "color/neutral/0"}, "hidden": True,
                    "description": "Текст и иконки поверх насыщенной заливки (Primary, Danger): белые в обеих темах",
                    "change": {"was": None, "approved": WHY}})

# L3: кнопки с насыщенной заливкой — on-bold; Outline Secondary — рамка контрола
L3_CHANGES = {}
for kind in ["primary", "danger"]:
    for part, fam in [("text", "text"), ("icon", "indicator")]:
        for st in ["default", "hover", "pressed"]:
            L3_CHANGES[f"button/fill/{kind}/{part}/{st}"] = f"color/action/{fam}/base/on-bold/{st}"
        # Disabled тоже поверх заливки: on-bold/disabled (белый 45 %), а не inverse-hard (в dark — чёрный)
        L3_CHANGES[f"button/fill/{kind}/{part}/disabled"] = f"color/action/{fam}/base/on-bold/disabled"
for st in ["default", "hover", "pressed"]:
    L3_CHANGES[f"button/outline/secondary/border/{st}"] = f"color/action/border/base/controls/{st}"
# Danger-soft Hover: иконка была calm, текст firm — иконка в цвет текста (как у Primary-soft)
L3_CHANGES["button/fill/danger-soft/icon/hover"] = "color/action/indicator/danger/firm/hover"
# Checkbox/Radio: галочка и точка на насыщенной заливке — белые в обеих темах (inverse-hard в dark чёрный)
L3_OTHER = {c: {f"{c}/checked/icon/{st}": f"color/action/indicator/base/on-bold/{st}" for st in ["default", "hover", "pressed"]}
            for c in ["checkbox", "radiobutton"]}


def main():
    dry = "--dry" in sys.argv
    for n, v in sorted(CHANGES.items()):
        print(f"L2 {n:48} dark {dark(n):32} → {v}")
    for t in NEW:
        print(f"L2 NEW {t['name']}")
    if dry:
        return
    for n, v in CHANGES.items():
        t = L2[n]
        was = (t.get("change") or {}).get("was") or dict(t["values"])
        t["values"] = {**t["values"], "dark": v}
        t["change"] = {"was": was, "approved": WHY}
    names = {t["name"] for t in SYS["l2"]}
    SYS["l2"] += [t for t in NEW if t["name"] not in names]
    io.open(SYS_PATH, "w", encoding="utf-8").write(json.dumps(SYS, ensure_ascii=False, indent=2) + "\n")
    bp = ROOT / "presets/button.tokens.json"
    btn = json.load(open(bp, encoding="utf-8"))
    for t in btn["l3"]:
        if t["name"] in L3_CHANGES and t["alias"] != L3_CHANGES[t["name"]]:
            t["change"] = {"was": (t.get("change") or {}).get("was", t["alias"]), "approved": WHY}
            t["alias"] = L3_CHANGES[t["name"]]
    io.open(bp, "w", encoding="utf-8").write(json.dumps(btn, ensure_ascii=False, indent=2) + "\n")
    for comp, ch in L3_OTHER.items():
        cp = ROOT / f"presets/{comp}.tokens.json"
        d = json.load(open(cp, encoding="utf-8"))
        for t in d["l3"]:
            if t["name"] in ch and t["alias"] != ch[t["name"]]:
                t["change"] = {"was": (t.get("change") or {}).get("was", t["alias"]), "approved": WHY}
                t["alias"] = ch[t["name"]]
        io.open(cp, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    print(f"L2 изменено: {len(CHANGES)}, новых L2: {len(NEW)}, L3 кнопок: {len(L3_CHANGES)}")


if __name__ == "__main__":
    main()
