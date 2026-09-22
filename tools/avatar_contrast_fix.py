"""FEDS: контраст WCAG AA у Avatar (текст 4.5:1, иконки 3:1, светлая и тёмная тема) — точечные перепривязки L3.

Найдено проверкой plugin/tests/a11y.test.ts при повторе Avatar (22.09.2026):
- Filled: светлые инициалы и иконки на `solid/{hue}/medium` (500/450) — 2.2–4.1 → `solid/{hue}/hard` (700/250):
  единственная ступень, где светлый текст проходит в light, а тёмный — в dark (8.1 / 6.4 / 8.2 / 10.7 / 5.0);
- бейдж-счётчик `context/notification` (brand 500) с белой цифрой — 3.8 → `indicator/brand/hard` (8.4 / 9.0);
- Soft жёлтый: текст `palette/yellow` на `accent/yellow/light` — 4.48 → подложка `accent/yellow/soft` (4.61).
Отмечены `change` (было → стало, одобрено по правилу «Контраст WCAG AA обязателен»).

Запуск: python tools/avatar_contrast_fix.py
"""
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
P = ROOT / "presets/avatar.tokens.json"
WHY = "2026-09-22, контраст WCAG AA (повтор Avatar): правило автора «Контраст WCAG AA обязателен»"
HUES = ["blue", "green", "red", "purple", "yellow"]

FIX = {f"avatar/{box}/hard/{h}": f"color/static/bg/solid/{h}/hard" for box in ("box", "box-group") for h in HUES}
FIX["avatar/status/counter"] = "color/static/indicator/brand/hard"
FIX["avatar/box/soft/yellow"] = "color/static/bg/transparent/accent/yellow/soft"
FIX["avatar/box-group/soft/yellow"] = "color/static/bg/transparent/accent/yellow/soft"


def main():
    d = json.load(open(P, encoding="utf-8"))
    n = 0
    for t in d["l3"]:
        want = FIX.get(t["name"])
        if want and t["alias"] != want:
            t["change"] = {"was": t["alias"], "approved": WHY}
            t["alias"] = want
            n += 1
    io.open(P, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    print(f"avatar: перепривязано {n}")


if __name__ == "__main__":
    main()
