"""Render text as SVG paths from pre-baked Inter glyphs (see scripts/extract-glyphs.py).

Inter is licensed under the SIL Open Font License 1.1 (https://rsms.me/inter/).
"""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

_GLYPHS = Path(__file__).with_name("glyphs.json")


@lru_cache(maxsize=None)
def _fonts():
    return json.loads(_GLYPHS.read_text(encoding="utf-8"))


def measure(s: str, size: float, font: str = "bold", spacing: float = 0.0) -> float:
    f = _fonts()[font]
    scale = size / f["upm"]
    w = sum(f["glyphs"].get(ch, f["glyphs"][" "])[0] for ch in s) * scale
    return w + spacing * max(len(s) - 1, 0)


def text(s: str, x: float, y: float, size: float, *, font: str = "bold", fill: str = "#fff",
         anchor: str = "start", spacing: float = 0.0, attrs: str = "") -> str:
    """Return a <g> of glyph paths with the baseline at (x, y)."""
    f = _fonts()[font]
    scale = size / f["upm"]
    width = measure(s, size, font, spacing)
    if anchor == "middle":
        x -= width / 2
    elif anchor == "end":
        x -= width
    parts, cx = [], x
    for ch in s:
        adv, d = f["glyphs"].get(ch, f["glyphs"][" "])
        if d:
            parts.append(
                f'<path transform="translate({cx:.1f} {y:.1f}) scale({scale:.5f} {-scale:.5f})" d="{d}"/>'
            )
        cx += adv * scale + spacing
    return f'<g fill="{fill}" {attrs}>{"".join(parts)}</g>'
