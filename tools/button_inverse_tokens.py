"""FEDS: инверсный вид Button для Filled, Outline и Text (решение автора 21.09.2026).

Inverse — тип кнопки для тёмных и насыщенных поверхностей. Им пользуются все компоненты с кнопками
(Alert, Banner, Popover…): своих кнопок под подложки компоненты не заводят.
  Filled  · Inverse — белая (светлая) заливка, тёмный текст: главное действие на тёмной карточке;
  Outline · Inverse — белая рамка и белый текст, фон прозрачный: альтернативное действие;
  Text    · Inverse — только белый текст: ссылки, «Назад», закрытие.
В тёмной теме `inverse-*` меняются местами вместе с инверсной поверхностью (как во всей системе).

Также убирает приватную часть Alert `_ Alert / Action` (токены alert/action/*, alert/size/{s}/action/*
и их L2) и L2 on-bright / bg on-bold, которыми пользовалась только она.

Запуск: python tools/button_inverse_tokens.py
"""
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
P = {n: ROOT / f"presets/{n}.tokens.json" for n in ("button", "alert", "_system")}
D = {n: json.load(open(p, encoding="utf-8")) for n, p in P.items()}
APPROVED = "2026-09-21, решение автора: инверсный вид кнопки для тёмных и насыщенных поверхностей"
STATES = ("default", "hover", "pressed", "disabled")
BG, TXT, ICO, STROKE = ["FRAME_FILL", "SHAPE_FILL"], ["TEXT_FILL"], ["SHAPE_FILL", "STROKE_COLOR"], ["STROKE_COLOR"]


def l3(name, alias, scopes, desc):  # desc — как у остальных L3 кнопки: «Component token for button …»
    return {"name": name, "type": "COLOR", "alias": alias, "scopes": scopes, "description": desc,
            "change": {"was": None, "approved": APPROVED}}


def st(tpl, s, disabled=None):
    return disabled if (s == "disabled" and disabled) else tpl.format(st=s)


NEW = []
for s in STATES:
    NEW += [
        # Filled · Inverse: светлая заливка inverse, текст и иконка — основной цвет темы (тёмный на белом)
        l3(f"button/fill/inverse/bg/{s}", f"color/action/bg/base/inverse/{s}", BG, f"Component token for button fill inverse bg-{s}"),
        l3(f"button/fill/inverse/border/{s}", "color/action/border/base/ghost/default", STROKE, f"Component token for button fill inverse border-{s}"),
        l3(f"button/fill/inverse/text/{s}", st("color/action/text/base/hard/{st}", s, "color/action/text/base/inverse-hard/disabled"), TXT, f"Component token for button fill inverse text-{s}"),
        l3(f"button/fill/inverse/icon/{s}", st("color/action/indicator/base/hard/{st}", s, "color/action/indicator/base/inverse-hard/disabled"), ICO, f"Component token for button fill inverse icon-{s}"),
        # Outline · Inverse: прозрачный фон, светлая рамка, светлый текст
        l3(f"button/outline/inverse/bg/{s}", f"color/action/bg/base/inverse-ghost/{s}", BG, f"Component token for button outline inverse bg-{s}"),
        l3(f"button/outline/inverse/border/{s}", st("color/action/border/base/inverse-controls/{st}", s, "color/action/border/base/inverse-soft/disabled"),
           STROKE, f"Component token for button outline inverse border-{s}"),
        l3(f"button/outline/inverse/text/{s}", f"color/action/text/base/inverse-hard/{s}", TXT, f"Component token for button outline inverse text-{s}"),
        l3(f"button/outline/inverse/icon/{s}", f"color/action/indicator/base/inverse-hard/{s}", ICO, f"Component token for button outline inverse icon-{s}"),
    ]

# Text · Inverse: существующие button/text-button/inverse/* (фон и рамка ghost, иконка inverse/icon/primary);
# текст — светлый inverse-hard, как иконка (исходный brand/firm на тёмной поверхности не читается)
TEXT_INVERSE = {f"button/text-button/inverse/text/{s}": f"color/action/text/base/inverse-hard/{s}" for s in STATES}


def main():
    btn = D["button"]
    have = {t["name"] for t in btn["l3"]}
    btn["l3"].extend(t for t in NEW if t["name"] not in have)
    fixed = 0
    for t in btn["l3"]:
        want = TEXT_INVERSE.get(t["name"])
        if want and t["alias"] != want:
            t["change"] = {"was": t["alias"], "approved": APPROVED}
            t["alias"] = want
            fixed += 1
    btn["decisions"] = [d for d in btn["decisions"] if not (isinstance(d, dict) and d.get("id") == "button-inverse")] + [{
        "id": "button-inverse", "date": "2026-09-21",
        "decision": "Тип Inverse у Filled, Icon - Filled, Outline, Icon - Outline и Text: кнопки для тёмных и насыщенных поверхностей. "
                    "Компоненты с кнопками (Alert и др.) используют Inverse, а не свои кнопки. Text Inverse: текст inverse-hard (как иконка)."}]

    # Alert: убрать приватную часть `_ Alert / Action` и её L2
    al = D["alert"]
    n3, n2 = len(al["l3"]), len(al.get("l2", []))
    al["l3"] = [t for t in al["l3"] if not t["name"].startswith(("alert/action/", "alert/size/m/action/", "alert/size/s/action/"))]
    al["l2"] = [t for t in al.get("l2", []) if not t["name"].startswith(("space/alert/action/", "border/alert/action-focus", "gap/alert/action-inner/", "radius/alert/action/", "radius/alert/action-focus/", "size/alert/action-icon/")) and not t["name"].startswith(("typography/alert/m/action/", "typography/alert/s/action/"))]

    # _system: L2, которыми пользовалась только `_ Alert / Action`
    sy = D["_system"]
    m2 = len(sy["l2"])
    drop = ("color/action/text/base/on-bright/", "color/action/indicator/base/on-bright/", "color/action/bg/base/on-bold/", "color/action/bg/base/on-bright/")
    sy["l2"] = [t for t in sy["l2"] if not t["name"].startswith(drop)]

    for n, p in P.items():
        io.open(p, "w", encoding="utf-8").write(json.dumps(D[n], ensure_ascii=False, indent=2) + "\n")
    print(f"Button: +L3 {len([t for t in NEW if t['name'] not in have])}, Text Inverse текст {fixed}")
    print(f"Alert: -L3 {n3 - len(al['l3'])}, -L2 {n2 - len(al['l2'])}; _system: -L2 {m2 - len(sy['l2'])}")


if __name__ == "__main__":
    main()
