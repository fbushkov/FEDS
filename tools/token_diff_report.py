"""FEDS: HTML-отчёт «что изменилось в токенах» — исходная библиотека FEroom против текущих пресетов.

Исходная версия — снимок библиотеки «F · DS · Элементы · Основа стилей» (analysis/token-index.json).
Актуальная — пресеты presets/*.tokens.json (то, что плагин записывает в файл).

Запуск: python tools/token_diff_report.py [путь.html]   (по умолчанию — на рабочий стол)
"""
import datetime
import glob
import html
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.home() / "Desktop" / "FEroom-tokens-diff.html"

IDX = json.load(open(ROOT / "analysis/token-index.json", encoding="utf-8"))
BY = {x["name"]: x for x in IDX}
PRESETS = [json.load(open(f, encoding="utf-8")) for f in sorted(glob.glob(str(ROOT / "presets/*.tokens.json")))]


def tgt(x):
    """Алиасы токена по режимам; сырое значение (без алиаса) — как есть."""
    return dict(x.get("targets") or {m: (v if not isinstance(v, str) else "= " + v) for m, v in x["modes"].items()})


TITLE = {p["component"]: p.get("title", p["component"]) for p in PRESETS}


def l1_rgba(name):
    x = BY.get(name)
    if not x or x["level"] != 1:
        return None
    v = list(x["modes"].values())[0]
    return v if isinstance(v, str) and v.startswith("rgba") else None


def norm(v):
    """Цвет L1 в одном виде (снимок — rgba, пресет — hex), чтобы сравнивать значения, а не запись."""
    if isinstance(v, str) and v.startswith("#"):
        h = v[1:]
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        a = int(h[6:8], 16) / 255 if len(h) == 8 else 1
        return (r, g, b, round(a, 2))
    if isinstance(v, str) and v.startswith("rgba"):
        r, g, b, a = [float(x) for x in v[5:-1].split(",")]
        return (int(r), int(g), int(b), round(a, 2))
    return v


def l1_value(name):
    x = BY.get(name)
    return list(x["modes"].values())[0] if x and x["level"] == 1 else None


# текущие L2: библиотека + пресеты (пресеты перекрывают)
CUR_L2 = {x["name"]: tgt(x) for x in IDX if x["level"] == 2}
for p in PRESETS:
    for t in p.get("l2", []):
        CUR_L2[t["name"]] = dict(t["values"])
ORIG_L2 = {x["name"]: tgt(x) for x in IDX if x["level"] == 2}


def resolve(l2, mode, table):
    v = table.get(l2, {}).get(mode)
    return v


def swatch(l1):
    c = l1_rgba(l1) if l1 else None
    return c


def row_l2(name, before, after, t, owner, reason):
    return {"name": name, "type": t, "owner": owner, "reason": reason or "",
            "before": {m: {"ref": before.get(m) if before else None, "c": swatch(before.get(m)) if before else None,
                           "v": None if (before and swatch(before.get(m))) else (l1_value(before.get(m)) if before else None)} for m in ("light", "dark")},
            "after": {m: {"ref": after.get(m), "c": swatch(after.get(m)), "v": None if swatch(after.get(m)) else l1_value(after.get(m))} for m in ("light", "dark")}}


def row_l3(name, before, after, t, owner, reason):
    def res(alias, table):
        if not alias:
            return None
        if BY.get(alias, {}).get("level") == 1:  # явное исключение L3 → L1
            return {m: {"l1": alias, "c": swatch(alias), "v": None if swatch(alias) else l1_value(alias)} for m in ("light", "dark")}
        return {m: {"l1": resolve(alias, m, table), "c": swatch(resolve(alias, m, table)),
                    "v": None if swatch(resolve(alias, m, table)) else l1_value(resolve(alias, m, table))} for m in ("light", "dark")}
    return {"name": name, "type": t, "owner": owner, "reason": reason or "",
            "before": {"alias": before, "res": res(before, ORIG_L2)}, "after": {"alias": after, "res": res(after, CUR_L2)}}


added_l2, changed_l2, added_l3, changed_l3 = [], [], [], []
seen2, seen3 = set(), set()
l1_changed = []
for p in PRESETS:
    owner = p["component"]
    for t in p.get("l1", []):
        o = BY.get(t["name"])
        if o and norm(list(o["modes"].values())[0]) != norm(t.get("value")):
            l1_changed.append(t["name"])
    for t in p.get("l2", []):
        n = t["name"]
        if n in seen2:
            continue
        seen2.add(n)
        ch = t.get("change") or {}
        typ = t.get("type", "")
        if n not in BY:
            added_l2.append(row_l2(n, None, t["values"], typ, owner, ch.get("approved") or t.get("description", "")))
        else:
            before = tgt(BY[n])
            if before != t["values"]:
                changed_l2.append(row_l2(n, before, t["values"], typ, owner, ch.get("approved", "")))
    for t in p["l3"]:
        n = t["name"]
        if n in seen3:
            continue
        seen3.add(n)
        ch = t.get("change") or {}
        typ = t.get("type", "")
        if n not in BY:
            added_l3.append(row_l3(n, None, t["alias"], typ, owner, ch.get("approved") or t.get("description", "")))
        else:
            before = tgt(BY[n]).get("mode_1")
            if before != t["alias"]:
                changed_l3.append(row_l3(n, before, t["alias"], typ, owner, ch.get("approved", "")))

# L3, чьё значение изменилось косвенно — через изменённые L2
indirect = []
changed_l2_names = {r["name"] for r in changed_l2}
for p in PRESETS:
    for t in p["l3"]:
        if t["name"] in BY and tgt(BY[t["name"]]).get("mode_1") == t["alias"] and t["alias"] in changed_l2_names:
            indirect.append(t["name"])
indirect = sorted(set(indirect))

orig = Counter(x["level"] for x in IDX)
cur_names = {1: {x["name"] for x in IDX if x["level"] == 1}, 2: set(ORIG_L2) | {r["name"] for r in added_l2},
             3: {x["name"] for x in IDX if x["level"] == 3} | {r["name"] for r in added_l3}}
removed = {lvl: sorted({x["name"] for x in IDX if x["level"] == lvl} - cur_names[lvl]) for lvl in (1, 2, 3)}

groups_l2 = Counter("/".join(r["name"].split("/")[:2]) for r in changed_l2)
DATA = {
    "generated": datetime.date.today().isoformat(),
    "summary": {
        "l1": {"before": orig[1], "after": len(cur_names[1]), "added": 0, "changed": len(l1_changed)},
        "l2": {"before": orig[2], "after": len(cur_names[2]), "added": len(added_l2), "changed": len(changed_l2)},
        "l3": {"before": orig[3], "after": len(cur_names[3]), "added": len(added_l3), "changed": len(changed_l3), "indirect": len(indirect)},
    },
    "removed": removed,
    "changed_l2": changed_l2, "added_l2": added_l2, "changed_l3": changed_l3, "added_l3": added_l3,
    "indirect": indirect, "titles": TITLE,
    "orig_ns3": sorted({x["name"].split("/")[0] for x in IDX if x["level"] == 3}),
    "orig_g2": sorted({"/".join(x["name"].split("/")[:3]) for x in IDX if x["level"] == 2}),
    "origins": {p["component"]: p.get("origin", "new") for p in PRESETS},
}

TEMPLATE = (ROOT / "tools/token_diff_template.html").read_text(encoding="utf-8")
out = TEMPLATE.replace("/*DATA*/null", json.dumps(DATA, ensure_ascii=False).replace("</", "<\\/"))
OUT.write_text(out, encoding="utf-8")
print(f"{OUT}  L2: +{len(added_l2)} ~{len(changed_l2)}  L3: +{len(added_l3)} ~{len(changed_l3)} (косвенно {len(indirect)})  "
      f"удалено: L1 {len(removed[1])}, L2 {len(removed[2])}, L3 {len(removed[3])}; L1 изменено {len(l1_changed)}")
