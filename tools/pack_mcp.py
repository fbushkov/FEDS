"""FEDS: упаковка для отладочного прогона в тестовом файле через Figma MCP (zlib + base64, частями с контрольными суммами).

  python tools/pack_mcp.py bundle                     — сборщик plugin/dist-dev/feds-mcp.js (без commitUndo: в MCP недоступен)
  python tools/pack_mcp.py def <component>            — presets/<component>.build.json без notes
  python tools/pack_mcp.py presets <c1,c2,...>        — пресеты токенов (только поля, нужные для диффа и записи)

Вывод: первая строка — «всего_частей длина_распакованного хэш_распакованного», далее по строке на часть:
«номер хэш_части текст_части». Хэш — полиномиальный (×31, mod 1e9+7) по кодам символов, как в проверке на стороне Figma.
В файле части складываются в feds.dev/pack:<ключ>:<номер>, сверяются и распаковываются: FEDS_INFLATE(склеенные части).
"""
import base64
import json
import re
import sys
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHUNK = 4000
KEEP = ("component", "kind", "origin", "partOf", "includes", "l1", "l2", "l3", "textStyles", "exceptions")


def h(text: str) -> int:
    x = 0
    for ch in text:
        x = (x * 31 + ord(ch)) % 1000000007
    return x


def payload(kind: str, arg: str | None) -> str:
    if kind == "bundle":
        src = (ROOT / "plugin/dist-dev/feds-mcp.js").read_text(encoding="utf-8")
        return re.sub(r"figma\.commitUndo\(\)[,;]?", "", src)
    if kind == "def":
        d = json.loads((ROOT / f"presets/{arg}.build.json").read_text(encoding="utf-8"))
        d.pop("notes", None)
        return json.dumps(d, ensure_ascii=False, separators=(",", ":"))
    out = []
    for c in arg.split(","):
        d = json.loads((ROOT / f"presets/{c}.tokens.json").read_text(encoding="utf-8"))
        out.append({k: d[k] for k in KEEP if k in d})
    return json.dumps(out, ensure_ascii=False, separators=(",", ":"))


def main():
    text = payload(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
    b64 = base64.b64encode(zlib.compress(text.encode("utf-8"), 9)).decode("ascii")
    parts = [b64[i:i + CHUNK] for i in range(0, len(b64), CHUNK)]
    print(len(parts), len(text), h(text))
    for i, p in enumerate(parts):
        print(i, h(p), p)


if __name__ == "__main__":
    main()
