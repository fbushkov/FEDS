"""FEDS: токены для Alert по композиции Atlassian Flag (Appearance Default / Bold) и кнопок на насыщенной заливке.

Новые L2 (`2. General`, light и dark), все ступени подбираются по WCAG AA (текст 4.5:1):
  color/status/{blue,green,red,yellow}/bold/{default,on,on-secondary} — насыщенная заливка роли и текст на ней
    (существующие status/*/medium в light дают 3.8–4.1 и остаются за Badge/Status до решения автора);
  color/action/{text,indicator}/base/on-bold/disabled — дополнение к on-bold (Filled Primary).
Новые L3: alert/default/*, alert/bold/*. Действия Alert — кнопки типа Inverse (tools/button_inverse_tokens.py).

Запуск: python tools/flag_tokens.py
"""
import importlib.util
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("dtf", ROOT / "tools/dark_theme_fix.py")
dtf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dtf)
contrast, first, IDX = dtf.contrast, dtf.first, dtf.IDX
WHY = "2026-09-21, Alert по композиции Flag (Appearance Bold/Default): новые токены"
LIGHT_SURFACE, DARK_SURFACE = "color/neutral/0", "color/neutral/900"
ROLE_HUE = {"info": "blue", "success": "green", "warning": "yellow", "error": "red"}


def l2(name, light, dark, scopes, desc):
    return {"name": name, "type": "COLOR", "scopes": scopes, "values": {"light": light, "dark": dark}, "hidden": True,
            "description": desc, "change": {"was": None, "approved": WHY}}


def l3(name, alias, scopes, desc):
    return {"name": name, "type": "COLOR", "alias": alias, "scopes": scopes, "description": desc}


NEW_L2 = []
BG, TXT, ICO, STROKE = ["FRAME_FILL", "SHAPE_FILL"], ["TEXT_FILL"], ["SHAPE_FILL", "STROKE_COLOR"], ["STROKE_COLOR"]

# насыщенные заливки ролей: белый текст (жёлтый — тёмный) ≥ 4.5:1 в обеих темах
for hue in ["blue", "green", "red"]:
    steps = [f"color/{hue}/{n}" for n in (500, 550, 600, 650, 700)]
    ok = lambda base: lambda s: contrast("color/neutral/0", s, base) >= 4.5  # noqa: E731
    lt, dk = first(steps, ok(LIGHT_SURFACE)), first(steps, ok(DARK_SURFACE))
    sec = lambda bg, base: first(["color/transparent-white/900", "color/transparent-white/950", "color/neutral/0"],  # noqa: E731
                                 lambda s: contrast(s, bg, base) >= 4.5)
    NEW_L2 += [
        l2(f"color/status/{hue}/bold/default", lt, dk, BG, f"Насыщенная заливка роли ({hue}) с белым текстом ≥ 4.5:1"),
        l2(f"color/status/{hue}/bold/on", "color/neutral/0", "color/neutral/0", TXT + ICO, "Текст и иконка на насыщенной заливке роли"),
        l2(f"color/status/{hue}/bold/on-secondary", sec(lt, LIGHT_SURFACE), sec(dk, DARK_SURFACE), TXT, "Второй уровень текста на насыщенной заливке"),
    ]
NEW_L2 += [
    l2("color/status/yellow/bold/default", "color/yellow/450", "color/yellow/450", BG, "Насыщенная жёлтая заливка: текст тёмный (белый на жёлтом не читается)"),
    l2("color/status/yellow/bold/on", "color/neutral/900", "color/neutral/900", TXT + ICO, "Тёмный текст и иконка на жёлтой заливке"),
    l2("color/status/yellow/bold/on-secondary", "color/transparent-black/800", "color/transparent-black/800", TXT, "Второй уровень текста на жёлтой заливке"),
]
# неактивный текст поверх насыщенной заливки (Filled Primary Disabled)
for part, sc in [("text", TXT), ("indicator", ICO)]:
    NEW_L2.append(l2(f"color/action/{part}/base/on-bold/disabled", "color/transparent-white/450", "color/transparent-white/450", sc, "Неактивный текст поверх насыщенной заливки"))

# L3 Alert: Appearance Default (карточка Flag) и Bold
ALERT_L3 = [
    l3("alert/default/bg", "color/bg/raised/main", BG, "Alert Default: поверхность карточки"),
    l3("alert/default/inverse-bg", "color/bg/raised/inverse-main", BG, "Alert Default на тёмной поверхности"),
    l3("alert/default/border", "color/static/border/base/low", STROKE, "Alert Default: рамка карточки"),
    l3("alert/default/inverse-border", "color/static/border/base/inverse-low", STROKE, "Alert Default на тёмной поверхности: рамка"),
]
for role, hue in ROLE_HUE.items():
    ALERT_L3 += [
        l3(f"alert/bold/bg/{role}", f"color/status/{hue}/bold/default", BG, f"Alert Bold {role}: заливка"),
        l3(f"alert/bold/text/{role}", f"color/status/{hue}/bold/on", TXT, f"Alert Bold {role}: заголовок"),
        l3(f"alert/bold/description/{role}", f"color/status/{hue}/bold/on-secondary", TXT, f"Alert Bold {role}: текст"),
        l3(f"alert/bold/icon/{role}", f"color/status/{hue}/bold/on", ICO, f"Alert Bold {role}: иконка в цвет заголовка"),
    ]


def merge(path, key, items):
    d = json.load(open(path, encoding="utf-8"))
    have = {t["name"] for t in d.get(key, [])}
    add = [t for t in items if t["name"] not in have]
    d.setdefault(key, []).extend(add)
    io.open(path, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    return len(add)


def main():
    for t in NEW_L2:
        print(f"L2 {t['name']:44} {t['values']['light']:30} {t['values']['dark']}")
    print("L2 +", merge(ROOT / "presets/_system.tokens.json", "l2", NEW_L2))
    print("L3 alert +", merge(ROOT / "presets/alert.tokens.json", "l3", ALERT_L3))


if __name__ == "__main__":
    main()
