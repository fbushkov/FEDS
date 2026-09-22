"""FEDS: исправление светлой темы (колонка light в `2. General`) до порогов WCAG 2.1 AA.

Пара к tools/dark_theme_fix.py: те же правила, ступени подбираются расчётом контраста на белой поверхности
(`color/bg/section/main` в light = neutral/0; inverse-поверхность = neutral/900). Меняется только колонка light;
dark, имена и связи L3 → L2 → L1 не трогаются. Каждое изменение помечается `change: {was, approved}`.

  A. Насыщенные заливки с белым текстом (кнопки, Status/Badge/Chip hard) — ступень, где белый ≥ 4.5:1;
     жёлтый — тёмный текст.
  B. firm / calm / visited (текст и иконки brand, danger) — сплошные ступени ≥ 4.5 (текст) и ≥ 3 (иконки)
     на поверхности и на soft-заливках во всех состояниях; иконка той же ступени, что текст.
  C. Рамки: контролы ≥ 3:1 (WCAG 1.4.11), calm-рамки ≥ 3:1.
  D. Полупрозрачный текст: soft / light / visited ≥ 4.5; inverse-soft на тёмной поверхности ≥ 4.5.
  E. Текст на мягких Status/Badge ≥ 4.5; второй уровень текста на насыщенных — ≥ 4.5.

Запуск: python tools/light_theme_fix.py [--dry]
"""
import importlib.util
import io
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("dtf", ROOT / "tools/dark_theme_fix.py")
dtf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dtf)
contrast, first, IDX = dtf.contrast, dtf.first, dtf.IDX
WHY = "2026-09-21, светлая тема: контраст WCAG AA (минимальные пороги)"
SYS_PATH = ROOT / "presets/_system.tokens.json"
SYS = json.load(open(SYS_PATH, encoding="utf-8"))
L2 = {t["name"]: t for t in SYS["l2"]}
S, INV = "color/neutral/0", "color/neutral/900"   # поверхность раздела и inverse-поверхность в light
CHANGES = {}


def light(n):
    """Действующее значение light: с учётом уже подобранных в этом прогоне."""
    return CHANGES.get(n, L2[n]["values"]["light"])


def put(name, value):
    if name in L2 and light(name) != value:
        CHANGES[name] = value


def c(fg, bg, base=S):
    return contrast(fg, bg, base)


def steps(hue, nums):
    return [f"color/{hue}/{n}" for n in nums]


W = lambda n: f"color/transparent-white/{n}"  # noqa: E731
B = lambda n: f"color/transparent-black/{n}"  # noqa: E731

# A. насыщенные заливки с белым текстом
def bold(prefix, hue, states):
    st = steps(hue, (500, 550, 600, 650, 700, 750, 800))
    i = st.index(first(st, lambda s: c("color/neutral/0", s) >= 4.5))
    for k, name in enumerate(states):
        put(f"{prefix}/{name}", st[min(i + k, len(st) - 1)])


bold("color/action/bg/brand/medium", "brand", ["default", "hover", "pressed"])
bold("color/action/bg/danger/medium", "red", ["default", "hover", "pressed"])
for hue in ["brand", "blue", "red", "purple", "green"]:
    bold(f"color/status/{hue}/medium", hue, ["default", "hover", "active"])
put("color/status/yellow/medium/on", "color/neutral/900")
put("color/status/yellow/medium/on-secondary", B(700))
for hue in ["brand", "blue", "red", "purple", "green"]:
    put(f"color/status/{hue}/medium/on-secondary",
        first([W(900), W(950), "color/neutral/0"], lambda s: c(s, light(f"color/status/{hue}/medium/default")) >= 4.5))

# B. firm / calm / visited: каждое состояние — своя ступень, проверенная на своей подложке
#    (default — на поверхности и soft-подложке в покое, hover — на hover, pressed — на pressed)
for hue, fam in [("brand", "brand"), ("red", "danger")]:
    st = steps(hue, (500, 550, 600, 650, 700, 750, 800))
    pick = {}
    lo = 0
    for state in ("default", "hover", "pressed"):
        g = light(f"color/action/bg/{fam}/light/{state}")
        s_ = first(st[lo:], lambda s: min(c(s, S), c(s, g)) >= 4.5)
        pick[state] = s_
        lo = min(st.index(s_) + 1, len(st) - 1)   # hover темнее default, pressed темнее hover
    for kind in ("text", "indicator"):
        for state in ("default", "hover", "pressed"):
            put(f"color/action/{kind}/{fam}/firm/{state}", pick[state])
            put(f"color/action/{kind}/{fam}/calm/{state}", pick[state])
    i = st.index(pick["default"])
    for v in ("firm", "calm"):
        put(f"color/action/text/{fam}/{v}/visited", st[min(i + 2, 6)])
    bd = first(steps(hue, (400, 450, 500, 550)), lambda s: c(s, S) >= 3)
    k = [400, 450, 500, 550].index(int(bd.rsplit("/", 1)[1]))
    put(f"color/action/border/{fam}/calm/default", bd)
    put(f"color/action/border/{fam}/calm/hover", f"color/{hue}/{[400, 450, 500, 550][min(k + 1, 3)]}")
    put(f"color/action/border/{fam}/calm/pressed", f"color/{hue}/{[450, 500, 550, 600][min(k + 1, 3)]}")

# C. рамки контролов ≥ 3:1
ctrl = first([B(n) for n in (300, 350, 400, 450, 500, 550)], lambda s: c(s, S) >= 3)
n0 = int(ctrl.rsplit("/", 1)[1])
put("color/action/border/base/controls/default", ctrl)
put("color/action/border/base/controls/hover", B(n0 + 100))
put("color/action/border/base/controls/pressed", B(n0 + 200))

# D. полупрозрачный текст
soft = first([B(n) for n in (350, 400, 450, 500, 550, 600)], lambda s: c(s, S) >= 4.5)
ns = int(soft.rsplit("/", 1)[1])
put("color/static/text/base/soft", soft)
put("color/static/text/base/light", B(ns + 50))
put("color/action/text/base/medium/visited", B(ns + 50))
inv = first([W(n) for n in (350, 400, 450, 500, 550, 600)], lambda s: c(s, INV, INV) >= 4.5)
put("color/static/text/base/inverse-soft", inv)
put("color/static/indicator/base/inverse-soft", inv)

# E. мягкие Status/Badge
for hue in ["brand", "blue", "red", "purple", "green", "yellow"]:
    bg = f"color/status/{hue}/soft/default"
    if bg not in L2:
        continue
    for part in ("on", "on-secondary"):
        n = f"color/status/{hue}/soft/{part}"
        if n in L2 and c(light(n), light(bg)) < 4.5:
            put(n, first(steps(hue, (550, 600, 650, 700, 750, 800)), lambda s: c(s, light(bg)) >= 4.5))


# F. точечные пары «цвет → его фон» (по L3 компонентов): цвет усиливается ступенями до порога
PRESETS = {p.stem.replace(".tokens", ""): json.load(open(p, encoding="utf-8")) for p in (ROOT / "presets").glob("*.tokens.json")}
ALIAS = {t["name"]: t["alias"] for d in PRESETS.values() for t in d.get("l3", [])}


def stronger(fg, bg, need):
    """Следующие ступени той же семьи: прозрачные — плотнее, цветные — темнее (light)."""
    fam, n = fg.rsplit("/", 1)
    ladder = [50, 70, 100, 120, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 725, 750, 775, 800, 850, 900, 950]
    cands = [f"{fam}/{k}" for k in ladder if k > int(n)]
    return first(cands, lambda s: c(s, bg) >= need)


PAIRS = [  # (L3 цвета, L3 фона или None — поверхность, порог)
    ("chip/text/hard/secondary/base", "chip/bg/hard/base/default", 4.5),
    ("chip/text/soft/secondary/base", "chip/bg/soft/base/default", 4.5),
    ("chip/text/hard/secondary/base-inverse", "chip/bg/hard/base-inverse/default", 4.5),
    ("field/input/leading/icon", None, 3),
    ("field/select/dropdown/option/indicator/icon", None, 3),
    ("priority-indicator/icon/minor", "priority-indicator/bg/minor", 3),
    ("priority-indicator/icon/medium", "priority-indicator/bg/medium", 3),
    ("priority-indicator/icon/high", "priority-indicator/bg/high", 3),
    ("priority-indicator/icon/low", "priority-indicator/bg/low", 3),
]
for fg3, bg3, need in PAIRS:
    fg2 = ALIAS[fg3]
    bgv = light(ALIAS[bg3]) if bg3 else S
    if c(light(fg2), bgv) < need:
        put(fg2, stronger(light(fg2), bgv, need))

# L3 кнопок: в hover/pressed текст и иконка берут ступень своего состояния, а не firm/default
BTN = ROOT / "presets/button.tokens.json"
BTN_D = json.load(open(BTN, encoding="utf-8"))
L3_CHANGES = {}
for t in BTN_D["l3"]:
    state = t["name"].rsplit("/", 1)[1]
    for fam in ("brand", "danger"):
        for kind in ("text", "indicator"):
            if state in ("hover", "pressed") and t["alias"] == f"color/action/{kind}/{fam}/firm/default":
                L3_CHANGES[t["name"]] = f"color/action/{kind}/{fam}/firm/{state}"


def main():
    for n, v in sorted(L3_CHANGES.items()):
        print(f"L3 {n:48} → {v}")
    for n, v in sorted(CHANGES.items()):
        print(f"L2 {n:48} light {L2[n]['values']['light']:32} → {v}")
    if "--dry" in sys.argv:
        return
    for n, v in CHANGES.items():
        t = L2[n]
        was = (t.get("change") or {}).get("was") or dict(t["values"])
        t["values"] = {**t["values"], "light": v}
        t["change"] = {"was": was, "approved": (t.get("change") or {}).get("approved", WHY) + ("" if WHY in (t.get("change") or {}).get("approved", "") else "; " + WHY)}
    io.open(SYS_PATH, "w", encoding="utf-8").write(json.dumps(SYS, ensure_ascii=False, indent=2) + "\n")
    for t in BTN_D["l3"]:
        if t["name"] in L3_CHANGES:
            t["change"] = {"was": (t.get("change") or {}).get("was", t["alias"]), "approved": WHY}
            t["alias"] = L3_CHANGES[t["name"]]
    io.open(BTN, "w", encoding="utf-8").write(json.dumps(BTN_D, ensure_ascii=False, indent=2) + "\n")
    print(f"L2 изменено (light): {len(CHANGES)}, L3 кнопок: {len(L3_CHANGES)}")


if __name__ == "__main__":
    main()
