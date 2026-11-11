"""The Contribution Circuit: a year of GitHub activity laid out as kerb blocks around a race track.

One block per day, in order, starting at the start/finish line. A car laps the track and every
block lights up as it passes, so busy stretches of the year flash brighter.
"""
from __future__ import annotations

import datetime as dt
import math

from .github import level, stats
from .text import text
from .track import Track

W, H = 1200, 470
LAP_SECONDS = 16
PALETTE = ["#262a31", "#5c4a12", "#b8901c", "#ff8a1f", "#ff2e3b"]   # quiet → flat out
BG, ASPHALT, PANEL = "#0d0f13", "#30343c", "#151820"
ACCENT = "#ff2e3b"


def _car(fill=ACCENT):
    """Top-down race car pointing along +x, centred on the origin."""
    return (
        f'<g>'
        f'<rect x="-14" y="-8.5" width="6" height="3.5" rx="1" fill="#0b0b0b"/>'
        f'<rect x="-14" y="5" width="6" height="3.5" rx="1" fill="#0b0b0b"/>'
        f'<rect x="7" y="-8" width="5.5" height="3" rx="1" fill="#0b0b0b"/>'
        f'<rect x="7" y="5" width="5.5" height="3" rx="1" fill="#0b0b0b"/>'
        f'<path d="M-15,-5 L-4,-6 L12,-3.2 L17,0 L12,3.2 L-4,6 L-15,5 Z" fill="{fill}"/>'
        f'<rect x="-17" y="-7" width="3" height="14" rx="1" fill="{fill}"/>'
        f'<rect x="15" y="-6" width="2.5" height="12" rx="1" fill="#f2f2f2"/>'
        f'<ellipse cx="-1" cy="0" rx="4" ry="2.6" fill="#101317"/>'
        f'<path d="M-15,-0.8 L15,-0.8 L15,0.8 L-15,0.8 Z" fill="#ffffff" opacity=".85"/>'
        f'</g>'
    )


def _chequered(x, y, ang, cols=2, rows=6, size=3.4):
    cells = []
    for r in range(rows):
        for c in range(cols):
            fill = "#f4f4f4" if (r + c) % 2 == 0 else "#111"
            cells.append(f'<rect x="{c * size - cols * size / 2:.1f}" y="{r * size - rows * size / 2:.1f}" '
                         f'width="{size}" height="{size}" fill="{fill}"/>')
    return f'<g transform="translate({x:.1f} {y:.1f}) rotate({ang:.1f})">{"".join(cells)}</g>'


def _stat(x, y, label, value, unit=""):
    return (
        text(label, x, y, 11.5, font="bold", fill="#8a909c", spacing=1.6)
        + text(value, x, y + 40, 36, font="display", fill="#ffffff")
        + (text(unit, x, y + 60, 12, font="regular", fill="#6b7280") if unit else "")
    )


def build(days, total, login="d-murza"):
    days = days[-365:] if len(days) > 365 else days
    st = stats(days)
    nonzero = sorted(d["count"] for d in days if d["count"])
    ceiling = nonzero[int(len(nonzero) * 0.9)] if nonzero else 1

    track = Track(scale=1.0, dx=40, dy=48)
    n = max(len(days), 1)
    step = track.length / n
    half = 15            # half the asphalt width

    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
           f'role="img" aria-label="{total} GitHub contributions in the last year, drawn as a race track">']
    out.append(f'<style>'
               f'.f{{opacity:0;animation:pass {LAP_SECONDS}s linear infinite}}'
               f'@keyframes pass{{0%{{opacity:.95}}5%{{opacity:0}}100%{{opacity:0}}}}'
               f'.blink{{animation:blink 1.2s steps(2) infinite}}'
               f'@keyframes blink{{50%{{opacity:.25}}}}'
               f'</style>')
    out.append(f'<defs><filter id="glow" x="-50%" y="-50%" width="200%" height="200%">'
               f'<feGaussianBlur stdDeviation="3.5" result="b"/><feMerge><feMergeNode in="b"/>'
               f'<feMergeNode in="SourceGraphic"/></feMerge></filter>'
               f'<pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse">'
               f'<path d="M24 0H0V24" fill="none" stroke="#1a1d24" stroke-width="1"/></pattern></defs>')
    out.append(f'<rect width="{W}" height="{H}" rx="18" fill="{BG}"/>')
    out.append(f'<rect x="10" y="10" width="{W - 20}" height="{H - 20}" rx="12" fill="url(#grid)"/>')

    # title
    start = days[0]["date"] if days else ""
    end = days[-1]["date"] if days else ""
    out.append(text("CONTRIBUTION CIRCUIT", 40, 44, 22, font="display", fill="#ffffff"))
    out.append(text(f"{start}  →  {end}   ·   one kerb block = one day", 330, 43, 12.5,
                    font="regular", fill="#7c8391"))

    # track: run-off, asphalt, edge lines
    out.append(f'<path d="{track.path}" fill="none" stroke="#1b1e25" stroke-width="{2 * half + 34}" '
               f'stroke-linejoin="round"/>')
    out.append(f'<path d="{track.path}" fill="none" stroke="{ASPHALT}" stroke-width="{2 * half}" '
               f'stroke-linejoin="round"/>')
    out.append(f'<path d="{track.path}" fill="none" stroke="#454a54" stroke-width="1.2" '
               f'stroke-dasharray="10 12"/>')

    # kerb blocks (one per day) on both edges, with a flash overlay that fires when the car passes
    blocks, flashes = [], []
    for i, d in enumerate(days):
        s = (i + 0.5) * step
        x, y, ang = track.at(s)
        lv = level(d["count"], ceiling)
        nx, ny = -math.sin(math.radians(ang)), math.cos(math.radians(ang))
        bw = max(step * 0.78, 1.2)
        for side in (-1, 1):
            cx, cy = x + nx * side * (half + 4.5), y + ny * side * (half + 4.5)
            blocks.append(f'<rect x="{-bw / 2:.2f}" y="-3.5" width="{bw:.2f}" height="7" '
                          f'transform="translate({cx:.1f} {cy:.1f}) rotate({ang:.1f})" fill="{PALETTE[lv]}"/>')
            if lv:
                delay = -(LAP_SECONDS - (s / track.length) * LAP_SECONDS)
                flashes.append(f'<rect class="f" style="animation-delay:{delay:.2f}s" x="{-bw / 2:.2f}" y="-3.5" '
                               f'width="{bw:.2f}" height="7" transform="translate({cx:.1f} {cy:.1f}) '
                               f'rotate({ang:.1f})" fill="#fff8e1"/>')
    out.append(f'<g>{"".join(blocks)}</g>')
    out.append(f'<g filter="url(#glow)">{"".join(flashes)}</g>')

    # start / finish
    sx, sy, sang = track.at(0)
    out.append(_chequered(sx, sy, sang, cols=2, rows=9, size=3.4))
    out.append(text("S/F", sx - 12, sy + half + 30, 11, font="bold", fill="#9aa1ad", spacing=1))

    # the car
    out.append(f'<g filter="url(#glow)"><g>{_car()}'
               f'<animateMotion dur="{LAP_SECONDS}s" repeatCount="indefinite" rotate="auto" '
               f'path="{track.path}"/></g></g>')

    # telemetry panel
    px = 860
    out.append(f'<rect x="{px - 20}" y="70" width="320" height="{H - 100}" rx="14" fill="{PANEL}" '
               f'stroke="#232733"/>')
    out.append(f'<circle cx="{px + 4}" cy="98" r="5" fill="{ACCENT}" class="blink"/>')
    out.append(text("LIVE TELEMETRY", px + 18, 103, 13, font="bold", fill="#e5e7eb", spacing=2))
    out.append(text(f"@{login}", px + 270, 103, 12, font="regular", fill="#6b7280", anchor="end"))
    best_date = ""
    try:
        best_date = dt.date.fromisoformat(st["best_date"]).strftime("%d %b %Y")
    except ValueError:
        pass
    out.append(_stat(px, 140, "CONTRIBUTIONS", f"{total:,}", "last 12 months"))
    out.append(_stat(px + 155, 140, "TOP SPEED", f"{st['best']}", f"best day · {best_date}"))
    out.append(_stat(px, 240, "LONGEST STINT", f"{st['longest']}", "days in a row"))
    out.append(_stat(px + 155, 240, "CURRENT STINT", f"{st['current']}", "days and counting"))
    out.append(_stat(px, 340, "TIME ON TRACK", f"{st['active']}", f"active days of {len(days)}"))

    # legend
    lx, ly = 470, 440
    out.append(text("LESS", lx, ly + 4, 10.5, font="bold", fill="#6b7280", spacing=1))
    for k, col in enumerate(PALETTE):
        out.append(f'<rect x="{lx + 38 + k * 16}" y="{ly - 6}" width="12" height="12" rx="2" fill="{col}"/>')
    out.append(text("FLAT OUT", lx + 38 + 5 * 16 + 4, ly + 4, 10.5, font="bold", fill="#6b7280", spacing=1))
    out.append(text("Rebuilt daily by a GitHub Action", px, H - 40, 11, font="regular", fill="#4b5262"))

    out.append("</svg>")
    return "".join(out)
