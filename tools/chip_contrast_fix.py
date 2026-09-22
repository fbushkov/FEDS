"""FEDS: контраст WCAG AA у Chip (текст 4.5:1, светлая и тёмная тема) — точечные перепривязки L3.

Найдено проверкой plugin/tests/a11y.test.ts при повторе Chip (22.09.2026), худший случай по Default / Hover / Pressed:
- Soft, текст синий, красный, зелёный, фиолетовый: `status/{hue}/soft/on*` на своей подложке — 4.1–4.5 (тёмная тема)
  → `color/static/text/palette/{hue}` (6.1–8.6);
- Soft, серый вторичный текст: `status/base/soft/on-secondary` — 4.31 → `color/static/text/base/medium` (5.13);
- Filled, White, вторичный текст: `status/base/soft/on-secondary` — 3.59 → `color/static/text/base/firm` (5.8);
- Soft, жёлтый: на Hover и Pressed подложка темнее и текст падает до 4.31 — подложки на светлые сплошные ступени
  (как в исправлении светлой темы): default `solid/yellow/weak` 4.81, hover `solid/yellow/mild` 4.67, active `status/yellow/soft/default` 4.61;
- Filled, жёлтый, Pressed: тёмный текст на `status/yellow/medium/active` (светлая тема 0.51) — 3.22
  → `status/yellow/bold/default` (6.33), как уже устроено в тёмной теме.
Отмечены `change` (было → стало, одобрено по правилу «Контраст WCAG AA обязателен»).

Запуск: python tools/chip_contrast_fix.py
"""
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
P = ROOT / "presets/chip.tokens.json"
WHY = "2026-09-22, контраст WCAG AA (повтор Chip): правило автора «Контраст WCAG AA обязателен»"

FIX = {}
for h in ("blue", "red", "green", "purple"):
    for tone in ("main", "secondary"):
        FIX[f"chip/text/soft/{tone}/{h}"] = f"color/static/text/palette/{h}"
FIX["chip/text/soft/secondary/base"] = "color/static/text/base/medium"
FIX["chip/text/hard/secondary/base-inverse"] = "color/static/text/base/firm"
FIX["chip/bg/soft/yellow/default"] = "color/static/bg/solid/yellow/weak"
FIX["chip/bg/soft/yellow/hover"] = "color/static/bg/solid/yellow/mild"
FIX["chip/bg/soft/yellow/active"] = "color/status/yellow/soft/default"
FIX["chip/bg/hard/yellow/active"] = "color/status/yellow/bold/default"


def main():
    d = json.load(open(P, encoding="utf-8"))
    n = 0
    names = {t["name"] for t in d["l3"]}
    missing = set(FIX) - names
    assert not missing, missing
    for t in d["l3"]:
        want = FIX.get(t["name"])
        if want and t["alias"] != want:
            t["change"] = {"was": t["alias"], "approved": WHY}
            t["alias"] = want
            n += 1
    io.open(P, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    print(f"chip: перепривязано {n}")


if __name__ == "__main__":
    main()
