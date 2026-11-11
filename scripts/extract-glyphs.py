#!/usr/bin/env python3
"""Dev-only: bake glyph outlines from local fonts into scripts/garage/glyphs.json.

The generators then render text as SVG paths with the standard library only,
so the header and the circuit look identical on every device (GitHub serves
README images without webfonts). Needs fontTools; run once and commit the JSON.
"""
import json
import sys
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

CHARS = "".join(chr(c) for c in range(32, 127)) + "·×→°—–“”‘’…"
FONTS = {
    "display": "/usr/share/fonts/opentype/inter/InterDisplay-BlackItalic.otf",
    "bold": "/usr/share/fonts/opentype/inter/Inter-Bold.otf",
    "regular": "/usr/share/fonts/opentype/inter/Inter-Medium.otf",
}
OUT = Path(__file__).resolve().parent / "garage" / "glyphs.json"


def bake(path):
    font = TTFont(path)
    cmap, gs = font.getBestCmap(), font.getGlyphSet()
    upm = font["head"].unitsPerEm
    glyphs = {}
    for ch in CHARS:
        name = cmap.get(ord(ch))
        if not name:
            continue
        pen = SVGPathPen(gs)
        gs[name].draw(pen)
        glyphs[ch] = [round(gs[name].width), pen.getCommands()]
    return {"upm": upm, "ascender": font["hhea"].ascent, "glyphs": glyphs}


def main():
    data = {key: bake(path) for key, path in FONTS.items()}
    OUT.write_text(json.dumps(data, separators=(",", ":")), encoding="utf-8")
    print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    sys.exit(main())
