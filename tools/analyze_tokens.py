"""FEDS: анализ экспорта переменных Figma (input/tokens/variables.json).

Строит плоский индекс переменных, проверяет алиасы и уровни ссылок,
выводит грамматику имён по компонентам.

Запуск:  python tools/analyze_tokens.py
Выход:   analysis/token-index.json, analysis/token-report.md
"""
import collections
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "input" / "tokens" / "variables.json"
OUT = ROOT / "analysis"
LEVEL = {"@1._primitives": 1, "@2._general": 2, "@3._components": 3}
SEGMENT = re.compile(r"^-?[a-z0-9]+(-[a-z0-9]+)*$")


def load():
    data = json.loads(SRC.read_text(encoding="utf-8"))
    flat = []

    def walk(node, col, path):
        if not isinstance(node, dict):
            return
        if "$variable_metadata" in node:
            meta = node["$variable_metadata"]
            flat.append({
                "level": LEVEL.get(col), "collection": col, "name": meta["name"],
                "type": node["$type"], "description": node.get("$description", ""),
                "id": meta["figmaId"], "ref": "{" + col + "." + ".".join(path) + "}",
                "modes": meta["modes"],
            })
            return
        for k, v in node.items():
            if k != "$collection_metadata":
                walk(v, col, path + [k])

    for col, body in data.items():
        walk(body, col, [])
    collections_meta = {c: b["$collection_metadata"] for c, b in data.items()}
    return flat, collections_meta


def grammar(names):
    """Для группы имён: по длине пути — множество значений каждого сегмента."""
    by_len = collections.defaultdict(list)
    for n in names:
        by_len[len(n.split("/"))].append(n.split("/"))
    out = []
    for length, rows in sorted(by_len.items()):
        segs = [sorted({r[i] for r in rows}) for i in range(length)]
        out.append((length, len(rows), segs))
    return out


def main():
    flat, cols = load()
    by_ref = {v["ref"]: v for v in flat}
    issues = collections.defaultdict(list)
    for v in flat:
        if not all(SEGMENT.match(s) for s in v["name"].split("/")):
            issues["non-kebab"].append(v["name"])
        for mode, val in v["modes"].items():
            if isinstance(val, str) and val.startswith("{"):
                target = by_ref.get(val)
                if not target:
                    issues["broken-alias"].append(f"{v['name']} [{mode}] → {val}")
                    continue
                v.setdefault("targets", {})[mode] = target["name"]
                if target["level"] != v["level"] - 1:
                    issues["level-skip-or-upward"].append(f"{v['name']} (L{v['level']}) → {target['name']} (L{target['level']})")
            elif v["level"] > 1:
                issues["raw-value-above-L1"].append(f"{v['name']} [{mode}] = {val}")

    OUT.mkdir(exist_ok=True)
    (OUT / "token-index.json").write_text(json.dumps(flat, ensure_ascii=False, indent=1), encoding="utf-8")

    lines = ["# Отчёт по токенам (генерируется tools/analyze_tokens.py)", ""]
    for c, m in cols.items():
        n = sum(1 for v in flat if v["collection"] == c)
        lines.append(f"- **{m['name']}** — {n} переменных, режимы: {', '.join(x['name'] for x in m['modes'])}")
    lines += ["", "## Проблемы", ""]
    for k in ("broken-alias", "level-skip-or-upward", "raw-value-above-L1", "non-kebab"):
        lines.append(f"### {k}: {len(issues[k])}")
        lines += [f"- `{x}`" for x in issues[k][:50]] + [""]
    lines += ["## Грамматика L3 по компонентам", ""]
    comps = sorted({v["name"].split("/")[0] for v in flat if v["level"] == 3})
    for comp in comps:
        names = [v["name"] for v in flat if v["level"] == 3 and v["name"].split("/")[0] == comp]
        lines.append(f"### {comp} ({len(names)})")
        for length, cnt, segs in grammar(names):
            lines.append(f"- [{length} сегм., {cnt}] " + " / ".join(s[0] if len(s) == 1 else "{" + ",".join(s) + "}" for s in segs))
        lines.append("")
    lines += ["## Грамматика L2 (корни)", ""]
    roots = sorted({"/".join(v["name"].split("/")[:2]) for v in flat if v["level"] == 2})
    for r in roots:
        names = [v["name"] for v in flat if v["level"] == 2 and v["name"].startswith(r + "/")]
        for length, cnt, segs in grammar(names):
            lines.append(f"- [{cnt}] " + " / ".join(s[0] if len(s) == 1 else "{" + ",".join(s) + "}" for s in segs))
    (OUT / "token-report.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"{len(flat)} переменных; проблем: " + ", ".join(f"{k}={len(v)}" for k, v in issues.items()))


if __name__ == "__main__":
    main()
