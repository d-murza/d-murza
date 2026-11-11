#!/usr/bin/env python3
"""Render the animated hero banner into assets/header.svg (static, commit the output)."""
from pathlib import Path

from garage.header import header_svg

OUT = Path(__file__).resolve().parent.parent / "assets" / "header.svg"

if __name__ == "__main__":
    OUT.parent.mkdir(exist_ok=True)
    svg = header_svg()
    OUT.write_text(svg, encoding="utf-8")
    print(f"Wrote {OUT} ({len(svg) // 1024} KB)")
