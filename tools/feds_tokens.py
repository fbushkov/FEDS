"""FEDS: запросы к системе токенов и проверка пресетов компонентов.

Команды:
  python tools/feds_tokens.py query <префикс> [--level 1|2|3] [--values]
      Показать переменные по префиксу имени (с разрешёнными значениями light/dark).
  python tools/feds_tokens.py validate presets/<component>.tokens.json [...]
      Проверить пресет: имена, ссылки, уровни, scopes, дубли, контраст. Пишет reports/<component>-tokens.md.
  python tools/feds_tokens.py validate-all
      Проверить все presets/*.tokens.json и проверить пересечения между ними.

Формат пресета: docs/preset-format.md.
"""
import glob
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "analysis" / "token-index.json"
SEGMENT = re.compile(r"^-?[a-z0-9]+(-[a-z0-9]+)*$")
TYPES = {"COLOR", "FLOAT"}
MODES = ("light", "dark")

# Допустимые scopes по корню/части (analysis/figma-conventions.md).
L2_SCOPES = {
    "space": ["GAP"], "gap": ["GAP"], "size": ["WIDTH_HEIGHT"], "radius": ["CORNER_RADIUS"],
    "border": ["STROKE_FLOAT"], "effects": ["EFFECT_FLOAT"],
}
TYPO_SCOPES = {"size": ["FONT_SIZE"], "line-height": ["LINE_HEIGHT"], "letter-spacing": ["LETTER_SPACING"], "weight": ["FONT_WEIGHT"]}
KNOWN_SCOPES = {
    "FRAME_FILL", "SHAPE_FILL", "TEXT_FILL", "ALL_FILLS", "STROKE_COLOR", "EFFECT_COLOR", "GAP", "WIDTH_HEIGHT",
    "CORNER_RADIUS", "STROKE_FLOAT", "EFFECT_FLOAT", "OPACITY", "FONT_SIZE", "LINE_HEIGHT", "LETTER_SPACING", "FONT_WEIGHT",
}


def load_index():
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    by_name = {}
    by_ref = {}
    for v in data:
        by_name[(v["level"], v["name"])] = v
        by_ref[v["ref"]] = v
    return data, by_name, by_ref


DATA, BY_NAME, BY_REF = load_index()


def _system_new_l2():
    """Новые L2 базы, одобренные автором (change.was = null): на них могут ссылаться пресеты компонентов."""
    p = ROOT / "presets" / "_system.tokens.json"
    if not p.exists():
        return {}
    d = json.loads(p.read_text(encoding="utf-8"))
    return {t["name"]: t for t in d.get("l2", []) if (t.get("change") or {}).get("was", 0) is None}


SYSTEM_NEW_L2 = _system_new_l2()


def find(name, level=None):
    if level:
        return BY_NAME.get((level, name))
    for lv in (3, 2, 1):
        if (lv, name) in BY_NAME:
            return BY_NAME[(lv, name)]
    return None


def resolve(var, mode):
    """Итоговое значение переменной в режиме light/dark (L1 и L3 одномодовые)."""
    seen = 0
    while seen < 10:
        seen += 1
        modes = var["modes"]
        val = modes.get(mode) if mode in modes else next(iter(modes.values()))
        if isinstance(val, str) and val.startswith("{"):
            var = BY_REF[val]
            continue
        return val
    return None


def parse_color(val):
    if isinstance(val, str) and val.startswith("rgba"):
        r, g, b, a = [float(x) for x in val[5:-1].split(",")]
        return r / 255, g / 255, b / 255, a
    if isinstance(val, str) and val.startswith("#"):
        h = val[1:]
        r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
        a = int(h[6:8], 16) / 255 if len(h) == 8 else 1
        return r, g, b, a
    return None


def blend(fg, bg):
    a = fg[3]
    return tuple(fg[i] * a + bg[i] * (1 - a) for i in range(3)) + (1,)


def luminance(c):
    def ch(x):
        return x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4
    return 0.2126 * ch(c[0]) + 0.7152 * ch(c[1]) + 0.0722 * ch(c[2])


def contrast(fg, bg):
    l1, l2 = sorted((luminance(fg), luminance(bg)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


# ---------------------------------------------------------------- query
def cmd_query(args):
    prefix = args[0] if args else ""
    level = None
    if "--level" in args:
        level = int(args[args.index("--level") + 1])
    show = "--values" in args
    rows = [v for v in DATA if v["name"].startswith(prefix) and (level is None or v["level"] == level)]
    for v in sorted(rows, key=lambda x: (x["level"], x["name"])):
        line = f"L{v['level']} {v['name']}"
        if v["level"] > 1:
            first = next(iter(v["modes"].values()))
            if isinstance(first, str) and first in BY_REF:
                line += f"  → {BY_REF[first]['name']}"
                if v["level"] == 2 and "dark" in v["modes"] and v["modes"]["dark"] != v["modes"]["light"]:
                    line += f" | dark → {BY_REF[v['modes']['dark']]['name']}"
        if show:
            line += "  = " + " / ".join(str(resolve(v, m)) for m in MODES)
        print(line)
    print(f"— {len(rows)} шт.")


# ---------------------------------------------------------------- validate
class Preset:
    def __init__(self, path):
        self.path = Path(path).resolve()
        self.data = json.loads(self.path.read_text(encoding="utf-8"))
        self.errors, self.warnings, self.notes = [], [], []
        self.new_l2 = {t["name"]: t for t in self.data.get("l2", [])}
        self.new_l3 = {t["name"]: t for t in self.data.get("l3", [])}

    def err(self, msg):
        self.errors.append(msg)

    def warn(self, msg):
        self.warnings.append(msg)

    # значение L2 из пресета или из системы
    def l2_value(self, name, mode):
        if name in self.new_l2:
            t = self.new_l2[name]
            val = t["values"][mode]
            if isinstance(val, str):
                p = find(val, 1)
                return resolve(p, mode) if p else None
            return val
        v = find(name, 2)
        return resolve(v, mode) if v else None

    def l3_value(self, name, mode):
        if name in self.new_l3:
            return self.l2_value(self.new_l3[name]["alias"], mode)
        v = find(name, 3)
        return resolve(v, mode) if v else None

    def check_existing(self):
        """Пресет, снятый с текущей системы (база или готовый компонент): сверка с индексом один к одному."""
        d = self.data
        for t in d.get("l1", []):
            v = find(t["name"], 1)
            if not v:
                self.err(f"L1 `{t['name']}` нет в системе")
        for t in d.get("l2", []):
            v = find(t["name"], 2)
            ch = t.get("change") or {}
            if not v:
                # новый L2 внутри существующей системы — только с решением автора (change.was = null)
                if "was" in ch and ch["was"] is None and ch.get("approved"):
                    self.notes.append(f"L2 `{t['name']}`: новый, одобрен ({ch['approved']})")
                else:
                    self.err(f"L2 `{t['name']}` нет в системе")
                continue
            for m in MODES:
                raw = v["modes"][m]
                cur = BY_REF[raw]["name"] if isinstance(raw, str) and raw in BY_REF else raw
                if cur != t["values"][m]:
                    if ch.get("approved") and (ch.get("was") or {}).get(m) == cur:
                        self.notes.append(f"L2 `{t['name']}` [{m}]: изменение одобрено: {cur} → {t['values'][m]}")
                    else:
                        self.err(f"L2 `{t['name']}` [{m}]: {t['values'][m]} ≠ {cur}")
        for t in d.get("l3", []):
            v = find(t["name"], 3)
            cur = BY_REF[next(iter(v["modes"].values()))]["name"] if v else None
            if cur != t["alias"]:
                # одобренное автором изменение существующего токена: был `was`, есть причина `approved`
                ch = t.get("change") or {}
                if ch.get("was") == cur and ch.get("approved"):
                    self.notes.append(f"L3 `{t['name']}`: изменение одобрено ({ch['approved']}): {cur} → {t['alias']}")
                else:
                    self.err(f"L3 `{t['name']}`: {t['alias']} ≠ {cur}")
        for s in d.get("textStyles", []):
            for prop, vname in s["vars"].items():
                if not find(vname, 2):
                    self.err(f"стиль `{s['name']}`: нет переменной {prop} `{vname}`")
        self.contrast_rows = []
        self.notes.append("Пресет снят с текущей системы; проверена сверка с индексом один к одному.")
        return not self.errors

    def check(self):
        d = self.data
        if d.get("origin") == "existing":
            return self.check_existing()
        comp = d.get("component", "")
        if not comp or not all(SEGMENT.match(s) for s in comp.split("/")):
            self.err(f"`component` должен быть kebab-case: `{comp}`")
        roots = set(d.get("roots") or [comp.split("/")[0]])
        seen = set()
        for kind, items in (("l2", d.get("l2", [])), ("l3", d.get("l3", []))):
            for t in items:
                n = t.get("name", "")
                if (kind, n) in seen:
                    self.err(f"дубль в пресете: `{n}`")
                seen.add((kind, n))
                if not all(SEGMENT.match(s) for s in n.split("/")):
                    self.err(f"имя не по регулярке сегмента: `{n}`")
                if t.get("type") not in TYPES:
                    self.err(f"`{n}`: type должен быть COLOR или FLOAT")
                sc = t.get("scopes") or []
                if len(sc) == 0 or any(s not in KNOWN_SCOPES for s in sc):
                    self.err(f"`{n}`: неверные scopes {sc}")
                if not t.get("description"):
                    self.warn(f"`{n}`: нет описания")

        # L2
        for n, t in self.new_l2.items():
            existing = find(n, 2)
            if existing:
                self.notes.append(f"L2 `{n}` уже есть в системе — будет сверено, а не создано")
            root = n.split("/")[0]
            if root == "color":
                self.warn(f"L2 `{n}`: новый семантический цвет. Допустимо только если в L2 нет подходящего — обоснуйте в decisions")
            if root not in ("space", "gap", "size", "radius", "border", "typography", "effects", "color"):
                self.err(f"L2 `{n}`: неизвестный корень `{root}`")
            elif root != "color" and root != "typography" and len(n.split("/")) > 1 and n.split("/")[1] not in roots:
                self.warn(f"L2 `{n}`: второй сегмент должен быть именем компонента ({', '.join(sorted(roots))})")
            if root == "typography":
                prop = n.split("/")[-1]
                if prop not in TYPO_SCOPES:
                    self.err(f"L2 `{n}`: последний сегмент типографики — size|line-height|letter-spacing|weight")
                elif t.get("scopes") != TYPO_SCOPES[prop]:
                    self.err(f"L2 `{n}`: scopes должны быть {TYPO_SCOPES[prop]}")
            elif root in L2_SCOPES and t.get("scopes") != L2_SCOPES[root]:
                self.err(f"L2 `{n}`: scopes должны быть {L2_SCOPES[root]}")
            vals = t.get("values") or {}
            for m in MODES:
                if m not in vals:
                    self.err(f"L2 `{n}`: нет значения для режима {m}")
                    continue
                val = vals[m]
                if isinstance(val, str):
                    p = find(val, 1)
                    if not p:
                        self.err(f"L2 `{n}` [{m}]: примитив `{val}` не найден в `1. Primitives`")
                    elif (p["type"] == "color") != (t["type"] == "COLOR"):
                        self.err(f"L2 `{n}` [{m}]: тип примитива `{val}` не совпадает")
                else:
                    if not any(e.get("token") == n for e in d.get("exceptions", [])):
                        self.err(f"L2 `{n}` [{m}]: сырое значение {val} без записи в exceptions")

        # L3
        for n, t in self.new_l3.items():
            if n.split("/")[0] not in roots:
                self.err(f"L3 `{n}`: корень не из roots {sorted(roots)}")
            a = t.get("alias", "")
            target = self.new_l2.get(a) or find(a, 2) or SYSTEM_NEW_L2.get(a)
            exc = any(e.get("token") == n for e in d.get("exceptions", []))
            if not target:
                if find(a, 1) and exc:
                    self.notes.append(f"L3 `{n}` → L1 `{a}` (исключение)")
                else:
                    self.err(f"L3 `{n}`: алиас `{a}` не найден в `2. General` (и не добавлен в l2)")
                continue
            ttype = target.get("type")
            ttype = "COLOR" if ttype in ("color", "COLOR") else "FLOAT"
            if ttype != t.get("type"):
                self.err(f"L3 `{n}`: тип {t.get('type')} не совпадает с `{a}` ({ttype})")
            ex = find(n, 3)
            if ex:
                cur = BY_REF[next(iter(ex["modes"].values()))]["name"]
                if cur == a:
                    self.notes.append(f"L3 `{n}` уже есть и совпадает")
                else:
                    self.warn(f"L3 `{n}` уже есть, но ссылается на `{cur}`, а пресет — на `{a}`")

        # текстовые стили
        for s in d.get("textStyles", []):
            for prop in ("fontSize", "lineHeight", "letterSpacing", "fontWeight"):
                vname = (s.get("vars") or {}).get(prop)
                if not vname or not (vname in self.new_l2 or find(vname, 2)):
                    self.err(f"стиль `{s.get('name')}`: переменная {prop} `{vname}` не найдена в L2")

        # контраст
        self.contrast_rows = []
        for c in d.get("contrast", []):
            need = 4.5 if c.get("kind") == "text" else 3.0
            for m in MODES:
                fg = parse_color(self.l3_value(c["fg"], m) or self.l2_value(c["fg"], m))
                bg = parse_color(self.l3_value(c["bg"], m) or self.l2_value(c["bg"], m))
                base = parse_color(self.l2_value(c.get("over", "color/bg/page/main"), m)) or (1, 1, 1, 1)
                if not fg or not bg:
                    self.err(f"контраст: не удалось разрешить `{c['fg']}` / `{c['bg']}` [{m}]")
                    continue
                bg_s = blend(bg, base)
                ratio = contrast(blend(fg, bg_s), bg_s)
                ok = ratio >= need
                self.contrast_rows.append((c["fg"], c["bg"], m, ratio, need, ok))
                if not ok and not c.get("accepted"):
                    self.warn(f"контраст `{c['fg']}` на `{c['bg']}` [{m}] = {ratio:.2f} < {need}")
        return not self.errors

    def report(self):
        d = self.data
        comp = d["component"].replace("/", "-")
        lines = [f"# Токены: {d.get('title', comp)}", "",
                 f"Пресет: `{self.path.relative_to(ROOT).as_posix()}`. Источник: `{d.get('source', '—')}`. Аналог: `{d.get('analog', '—')}`.", "",
                 f"Статус проверки: **{'OK' if not self.errors else 'ОШИБКИ'}** · L2 новых: {len(self.new_l2)} · L3: {len(self.new_l3)} · текстовых стилей: {len(d.get('textStyles', []))}", ""]
        for title, items in (("Ошибки", self.errors), ("Предупреждения", self.warnings), ("Заметки", self.notes)):
            if items:
                lines += [f"## {title}", ""] + [f"- {x}" for x in items] + [""]
        if d.get("l2"):
            lines += ["## Новые токены L2 (`2. General`)", "", "| Токен | light | dark | scopes |", "|---|---|---|---|"]
            for t in d["l2"]:
                lines.append(f"| `{t['name']}` | `{t['values']['light']}` | `{t['values']['dark']}` | {', '.join(t['scopes'])} |")
            lines.append("")
        lines += ["## Токены L3 (`3. Components`)", "", "| Токен | → L2 | light | dark | scope |", "|---|---|---|---|---|"]
        for t in d.get("l3", []):
            lv = self.l2_value(t["alias"], "light")
            dv = self.l2_value(t["alias"], "dark")
            lines.append(f"| `{t['name']}` | `{t['alias']}` | {lv} | {dv} | {', '.join(t['scopes'])} |")
        lines.append("")
        if d.get("textStyles"):
            lines += ["## Текстовые стили", "", "| Стиль | Шрифт | Переменные |", "|---|---|---|"]
            for s in d["textStyles"]:
                lines.append(f"| `{s['name']}` | {s.get('fontFamily', 'Roboto')} {s.get('fontStyle', '')} | {', '.join('`' + v + '`' for v in s['vars'].values())} |")
            lines.append("")
        if self.contrast_rows:
            lines += ["## Контраст", "", "| Передний план | Фон | Режим | Контраст | Норма | |", "|---|---|---|---|---|---|"]
            for fg, bg, m, r, need, ok in self.contrast_rows:
                lines.append(f"| `{fg}` | `{bg}` | {m} | {r:.2f} | {need} | {'✅' if ok else '⚠️'} |")
            lines.append("")
        if d.get("exceptions"):
            lines += ["## Исключения", ""] + [f"- `{e['token']}` — {e['reason']}" for e in d["exceptions"]] + [""]
        if d.get("decisions"):
            lines += ["## Решения и допущения", ""] + [f"- {x}" for x in d["decisions"]] + [""]
        out = ROOT / "reports" / f"{comp}-tokens.md"
        out.write_text("\n".join(lines), encoding="utf-8")
        return out


def cmd_validate(paths):
    ok_all = True
    presets = []
    for p in paths:
        pr = Preset(p)
        ok = pr.check()
        out = pr.report()
        presets.append(pr)
        ok_all &= ok
        print(f"{'OK ' if ok else 'ERR'} {p}: ошибок {len(pr.errors)}, предупреждений {len(pr.warnings)} → {out.relative_to(ROOT).as_posix()}")
        for e in pr.errors[:30]:
            print("   ✗", e)
    # пересечения между пресетами
    owner = {}
    for pr in presets:
        for kind in ("l2", "l3"):
            for t in pr.data.get(kind, []):
                key = (kind, t["name"])
                if key in owner and owner[key][1] != json.dumps(t, sort_keys=True):
                    ok_all = False
                    print(f"ERR конфликт `{t['name']}` в {owner[key][0]} и {pr.path.name}")
                owner.setdefault(key, (pr.path.name, json.dumps(t, sort_keys=True)))
    return ok_all


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == "query":
        cmd_query(args)
    elif cmd == "validate":
        sys.exit(0 if cmd_validate(args) else 1)
    elif cmd == "validate-all":
        sys.exit(0 if cmd_validate(sorted(glob.glob(str(ROOT / "presets" / "*.tokens.json")))) else 1)
    else:
        print(__doc__)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
