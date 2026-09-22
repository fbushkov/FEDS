"""FEDS: аудит контраста по токенам всех пресетов (light и dark).

Пары строятся по грамматике L3: текст/иконка ↔ фон того же варианта и состояния
(сегмент части text|icon|indicator заменяется на bg). Если своего фона нет (ghost, ссылка,
иконка на поверхности) — фоном считается поверхность раздела: `color/bg/section/main`
или `color/bg/section/inverse-main` для токенов с `inverse`. Disabled не проверяется (WCAG 1.4.3).
Полупрозрачный фон кладётся на поверхность, цвет — на результат.

Запуск: python tools/audit_contrast.py [--mode dark|light|all]  →  reports/contrast-audit.md
Это эвристика по токенам; точная проверка по слоям — plugin/tests/a11y.test.ts для описаний сборки.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = {x["name"]: x for x in json.load(open(ROOT / "analysis/token-index.json", encoding="utf-8"))}
FG = {"text": 4.5, "label": 4.5, "icon": 3.0, "indicator": 3.0}
# проверено вручную: эвристика берёт не тот фон
KNOWN = {
    "avatar/button-x/icon": "кнопка-крестик на подложке аватара, не на поверхности",
    "avatar/status/text": "текст статуса на цветной точке аватара",
    "checkbox/loading/icon": "декоративный трек спиннера; бегущая часть — отдельный токен",
    "radiobutton/loading/icon": "декоративный трек спиннера",
    "status/loading/icon": "декоративный трек спиннера",
    "switch/on/icon/default": "иконка на ползунке (knob), а не на треке",
    "switch/on/icon/hover": "иконка на ползунке (knob), а не на треке",
    "switch/on/icon/pressed": "иконка на ползунке (knob), а не на треке",
    "switch/off/icon/pressed": "иконка на ползунке (knob), а не на треке",
}
# on-bold стоит на насыщенной заливке (Filled Primary), а не на поверхности раздела: его проверяет
# plugin/tests/a11y.test.ts по слоям на фоне варианта (в том числе кнопки внутри Alert — на подложке Alert)
EXEMPT = re.compile(r"disabled|placeholder-disabled|inactive-disabled|spacer|shadow|focus|on-bold")


def rgba(s):
    m = re.findall(r"[\d.]+", s)
    return [float(m[0]) / 255, float(m[1]) / 255, float(m[2]) / 255, float(m[3]) if len(m) > 3 else 1.0]


def lum(c):
    f = lambda x: x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4  # noqa: E731
    return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2])


def blend(fg, bg):
    a = fg[3]
    return [fg[i] * a + bg[i] * (1 - a) for i in range(3)] + [1.0]


def ratio(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True)
    return (la + 0.05) / (lb + 0.05)


def load_l3():
    l3 = {}
    comp = {}
    for f in sorted((ROOT / "presets").glob("*.tokens.json")):
        p = json.load(open(f, encoding="utf-8"))
        for t in p.get("l3", []):
            if t.get("type", "COLOR") == "COLOR":
                l3[t["name"]] = t["alias"]
                comp[t["name"]] = p["component"]
        for t in p.get("l2", []):
            # значения L2 из пресетов перекрывают индекс библиотеки: проверяется то, что будет записано
            INDEX[t["name"]] = {"level": 2, "name": t["name"], "targets": t["values"]}
    return l3, comp


L3, COMP = load_l3()


def resolve(name, mode):
    alias = L3.get(name, name)
    x = INDEX.get(alias)
    if not x:
        return None
    if x.get("level") == 1:
        return rgba(x["modes"]["mode_1"])
    t = (x.get("targets") or {}).get(mode)
    p = INDEX.get(t)
    return rgba(p["modes"]["mode_1"]) if p and "modes" in p else None


def audit(modes):
    rows = []
    for name in L3:
        segs = name.split("/")
        part = next((i for i, s in enumerate(segs) if s in FG), None)
        if part is None or EXEMPT.search(name):
            continue
        inverse = "inverse" in name
        surface = "color/bg/section/inverse-main" if inverse else "color/bg/section/main"
        bg_name = "/".join(segs[:part] + ["bg"] + segs[part + 1:])
        if bg_name not in L3:
            # иконка с ролью (…/icon/primary/default → …/bg/default); текст с уровнем (chip/text/hard/main/base → chip/bg/hard/base/default)
            cands = ["/".join(segs[:part] + ["bg"] + segs[-1:])]
            rest = [x for x in segs[part + 1:] if x not in ("main", "secondary")]
            cands += ["/".join(segs[:part] + ["bg"] + rest), "/".join(segs[:part] + ["bg"] + rest + ["default"])]
            bg_name = next((c for c in cands if c in L3), None)
        for mode in modes:
            base = resolve(surface, mode)
            fg = resolve(name, mode)
            if not base or not fg:
                continue
            bg = blend(resolve(bg_name, mode), base) if bg_name and resolve(bg_name, mode) else base
            r = ratio(blend(fg, bg), bg)
            need = FG[segs[part]]
            if r < need:
                rows.append((COMP[name], name, mode, r, need, L3[name], bg_name or surface))
    return rows


def main():
    mode = sys.argv[sys.argv.index("--mode") + 1] if "--mode" in sys.argv else "all"
    modes = ["light", "dark"] if mode == "all" else [mode]
    rows_all = sorted(audit(modes), key=lambda r: (r[0], r[2], r[3]))
    known = [r for r in rows_all if r[1] in KNOWN]
    rows = [r for r in rows_all if r[1] not in KNOWN]
    out = ["# Аудит контраста по токенам (FEDS)", "",
           f"Режимы: {', '.join(modes)}. Текст ≥ 4.5, иконки ≥ 3. Disabled не проверяется. Эвристика по грамматике L3 (`tools/audit_contrast.py`).", "",
           f"Нарушений: **{len(rows)}**", "",
           "| Компонент | Токен | Режим | Контраст | Нужно | L2 сейчас | Фон |", "|---|---|---|---|---|---|---|"]
    out += [f"| {c} | `{n}` | {m} | {r:.2f} | {nd} | `{a}` | `{b}` |" for c, n, m, r, nd, a, b in rows]
    out += ["", "## Проверено вручную (эвристика берёт не тот фон)", "", "| Токен | Режим | Причина |", "|---|---|---|"]
    out += [f"| `{n}` | {m} | {KNOWN[n]} |" for c, n, m, r, nd, a, b in known]
    (ROOT / "reports/contrast-audit.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    by = {}
    for r in rows:
        by.setdefault((r[0], r[2]), []).append(r)
    for k, v in sorted(by.items()):
        print(f"{k[0]:20} {k[1]:5} {len(v):3}  worst {min(x[3] for x in v):.2f}")
    print("итого", len(rows))


if __name__ == "__main__":
    main()
