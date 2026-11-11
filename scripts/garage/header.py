"""Animated hero banner: a GT car on an alpine pass at golden hour."""
from __future__ import annotations

import random

from .text import text

W, H = 1200, 360
GROUND = 300                      # road surface y


def _ridge(rng, y_base, amp, step, width=2400):
    """Mountain silhouette repeated seamlessly every 1200 px."""
    pts, x = [], 0
    heights = []
    while x <= 1200:
        heights.append(y_base - rng.uniform(0.25, 1.0) * amp)
        x += step
    heights[-1] = heights[0]
    for rep in range(width // 1200):
        for i, h in enumerate(heights):
            pts.append((rep * 1200 + i * step, h))
    d = f"M0,{H} " + " ".join(f"L{x:.0f},{y:.0f}" for x, y in pts) + f" L{width},{H} Z"
    return d


def _car(x, y, body="#e10600"):
    """Side-view GT coupé, rear at x, wheels touching y."""
    wheel = lambda cx: (
        f'<g transform="translate({cx} -24)">'
        f'<circle r="24" fill="#0c0c0f"/><circle r="22" fill="none" stroke="#1d1d22" stroke-width="2"/>'
        f'<circle r="15" fill="#c9ccd3"/>'
        f'<g fill="#7d828c">' + "".join(
            f'<rect x="-2" y="-14" width="4" height="12" rx="2" transform="rotate({a})"/>' for a in range(0, 360, 72))
        + '</g><circle r="4" fill="#2b2e35"/>'
        f'<animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="0.35s" '
        f'repeatCount="indefinite" additive="sum"/></g>'
    )
    return (
        f'<g transform="translate({x} {y})">'
        f'<animateTransform attributeName="transform" type="translate" values="{x} {y};{x} {y - 1.5};{x} {y}" '
        f'dur="0.5s" repeatCount="indefinite"/>'
        # shadow
        f'<ellipse cx="150" cy="2" rx="160" ry="7" fill="#000" opacity=".45"/>'
        # body
        f'<path d="M4,-16 C0,-26 2,-36 12,-42 L34,-47 C60,-52 84,-56 104,-62 C124,-74 160,-80 186,-68 '
        f'C200,-62 212,-56 230,-52 C262,-48 290,-44 302,-34 C308,-28 306,-20 300,-16 L268,-16 '
        f'A30,30 0 0 0 208,-16 L92,-16 A30,30 0 0 0 32,-16 Z" fill="{body}"/>'
        # glasshouse
        f'<path d="M112,-58 C130,-70 160,-74 182,-64 L196,-56 L116,-54 Z" fill="#1a1f2b"/>'
        f'<path d="M150,-71 L148,-55" stroke="{body}" stroke-width="3"/>'
        # highlights and details
        f'<path d="M14,-41 C70,-50 120,-56 150,-56 C200,-56 250,-50 296,-38" fill="none" stroke="#ff6b5e" '
        f'stroke-width="1.6" opacity=".7"/>'
        f'<path d="M40,-30 L260,-30" stroke="#ffffff" stroke-width="5" opacity=".9"/>'
        f'<path d="M40,-24 L260,-24" stroke="#111" stroke-width="2" opacity=".5"/>'
        f'<path d="M6,-40 L2,-30" stroke="#ff2b2b" stroke-width="5" stroke-linecap="round"/>'
        f'<path d="M296,-38 L304,-33" stroke="#fff6c8" stroke-width="5" stroke-linecap="round"/>'
        f'<path d="M10,-46 L40,-50 L40,-47 L12,-43 Z" fill="#111"/>'
        + wheel(62) + wheel(238) +
        # headlight beam
        f'<path d="M305,-34 L420,-58 L420,-6 Z" fill="url(#beam)" opacity=".55"/>'
        f'</g>'
    )


def header_svg():
    rng = random.Random(11)
    far, mid, near = _ridge(rng, 230, 120, 60), _ridge(rng, 262, 85, 45), _ridge(rng, 290, 50, 30)
    posts = "".join(f'<rect x="{i * 60}" y="{GROUND - 26}" width="5" height="26" fill="#2a2230"/>'
                    for i in range(0, 42))
    streaks = "".join(
        f'<rect x="{rng.randint(40, 640)}" y="{rng.randint(150, 280)}" width="{rng.randint(40, 160)}" '
        f'height="2" rx="1" fill="#ffd9a8" opacity="{rng.uniform(.08, .25):.2f}">'
        f'<animate attributeName="x" from="900" to="-200" dur="{rng.uniform(.6, 1.4):.2f}s" '
        f'begin="{rng.uniform(0, 1.2):.2f}s" repeatCount="indefinite"/></rect>'
        for _ in range(14)
    )
    title = text("DMYTRO MURZA", 58, 118, 78, font="display", fill="#ffffff")
    shadow = text("DMYTRO MURZA", 64, 124, 78, font="display", fill="#e10600", attrs='opacity=".9"')
    sub = text("MACHINE LEARNING  ·  BACKEND  ·  M.Sc. COMPUTER SCIENCE @ UNI KONSTANZ",
               62, 160, 15, font="bold", fill="#ffe2c4", spacing=1.8)
    quote = text("“Simplify, then add lightness.”  —  Colin Chapman", 62, 190, 13,
                 font="regular", fill="#d9a98a")

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
        f'aria-label="Dmytro Murza: a red GT car driving an alpine pass at sunset">'
        f'<defs>'
        f'<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="#140d24"/><stop offset=".45" stop-color="#4a1f4e"/>'
        f'<stop offset=".78" stop-color="#d4553a"/><stop offset="1" stop-color="#ffb35c"/></linearGradient>'
        f'<radialGradient id="sun" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#fff1c1"/>'
        f'<stop offset=".55" stop-color="#ffb347"/><stop offset="1" stop-color="#ff8a3d" stop-opacity="0"/>'
        f'</radialGradient>'
        f'<linearGradient id="beam" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff6c8"/>'
        f'<stop offset="1" stop-color="#fff6c8" stop-opacity="0"/></linearGradient>'
        f'<clipPath id="frame"><rect width="{W}" height="{H}" rx="18"/></clipPath>'
        f'</defs>'
        f'<g clip-path="url(#frame)">'
        f'<rect width="{W}" height="{H}" fill="url(#sky)"/>'
        f'<circle cx="930" cy="150" r="130" fill="url(#sun)"/>'
        f'<circle cx="930" cy="150" r="48" fill="#ffe7a8" opacity=".92"/>'
        # parallax mountains (each layer is two seamless 1200px tiles)
        f'<g><path d="{far}" fill="#6a2f55" opacity=".85"/>'
        f'<animateTransform attributeName="transform" type="translate" from="0 0" to="-1200 0" dur="90s" '
        f'repeatCount="indefinite"/></g>'
        f'<g><path d="{mid}" fill="#40203f"/>'
        f'<animateTransform attributeName="transform" type="translate" from="0 0" to="-1200 0" dur="40s" '
        f'repeatCount="indefinite"/></g>'
        f'<g><path d="{near}" fill="#24152a"/>'
        f'<animateTransform attributeName="transform" type="translate" from="0 0" to="-1200 0" dur="16s" '
        f'repeatCount="indefinite"/></g>'
        f'{streaks}'
        # guardrail
        f'<g><rect x="0" y="{GROUND - 22}" width="2400" height="5" fill="#3a2f3f"/>{posts}'
        f'<animateTransform attributeName="transform" type="translate" from="0 0" to="-60 0" dur="0.18s" '
        f'repeatCount="indefinite"/></g>'
        # road
        f'<rect y="{GROUND}" width="{W}" height="{H - GROUND}" fill="#120e16"/>'
        f'<rect y="{GROUND}" width="{W}" height="3" fill="#2e2533"/>'
        f'<line x1="0" y1="{GROUND + 32}" x2="{W + 80}" y2="{GROUND + 32}" stroke="#ffcf6b" stroke-width="4" '
        f'stroke-dasharray="44 36"><animate attributeName="stroke-dashoffset" from="0" to="80" dur="0.22s" '
        f'repeatCount="indefinite"/></line>'
        + _car(640, GROUND + 6)
        + shadow + title + sub + quote +
        f'</g></svg>'
    )
