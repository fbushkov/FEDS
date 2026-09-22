"""FEDS: высота панели списка в состояниях Empty и Loading (как в макетах: панель той же ширины, что список,
содержимое по центру, высота около ¾ списка из восьми пунктов).

L2 size/field/select/dropdown/empty/{s} → L1 size/192 · size/240 · size/256 (S · M · L);
L3 field/size/select/{s}/dropdown-box/empty-height → L2.

Запуск: python tools/dropdown_empty_tokens.py
"""
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
P = ROOT / "presets/field-dropdown.tokens.json"
L1 = {"s": "size/192", "m": "size/240", "l": "size/256"}


def main():
    d = json.load(open(P, encoding="utf-8"))
    have2 = {t["name"] for t in d["l2"]}
    have3 = {t["name"] for t in d["l3"]}
    n2 = n3 = 0
    for s, v in L1.items():
        S = s.upper()
        l2 = f"size/field/select/dropdown/empty/{s}"
        if l2 not in have2:
            d["l2"].append({"name": l2, "type": "FLOAT", "scopes": ["WIDTH_HEIGHT"], "values": {"light": v, "dark": v},
                            "description": f"Dropdown {S} — высота панели «Ничего не найдено» и загрузки"})
            n2 += 1
        l3 = f"field/size/select/{s}/dropdown-box/empty-height"
        if l3 not in have3:
            d["l3"].append({"name": l3, "type": "FLOAT", "alias": l2, "scopes": ["WIDTH_HEIGHT"],
                            "description": f"Dropdown {S} — высота панели «Ничего не найдено» и загрузки"})
            n3 += 1
    io.open(P, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    print(f"field-dropdown: +L2 {n2}, +L3 {n3}")


if __name__ == "__main__":
    main()
