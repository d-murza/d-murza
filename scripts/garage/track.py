"""Geometry for a closed race track: Catmull-Rom spline, arc-length sampling."""
from __future__ import annotations

import math

# Hand-designed circuit (screen coordinates, y grows downwards). Clockwise, starts on the main straight.
CONTROL_POINTS = [
    (300, 330), (470, 330), (640, 328), (735, 300), (758, 238),   # main straight → turn 1
    (720, 182), (640, 170), (590, 128), (612, 74), (560, 40),     # esses
    (470, 52), (410, 100), (350, 92), (300, 50), (215, 42),       # back section
    (120, 64), (78, 130), (120, 186), (205, 200), (225, 252),     # hairpin + chicane
    (170, 298), (100, 318), (150, 336), (225, 333),
]


def _catmull_rom(points, steps=40):
    """Closed centripetal-ish Catmull-Rom → dense polyline."""
    n = len(points)
    out = []
    for i in range(n):
        p0, p1, p2, p3 = (points[(i + k - 1) % n] for k in range(4))
        for s in range(steps):
            t = s / steps
            t2, t3 = t * t, t * t * t
            x = 0.5 * ((2 * p1[0]) + (-p0[0] + p2[0]) * t + (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2
                       + (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3)
            y = 0.5 * ((2 * p1[1]) + (-p0[1] + p2[1]) * t + (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2
                       + (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3)
            out.append((x, y))
    return out


def bezier_path(points=CONTROL_POINTS, scale=1.0, dx=0.0, dy=0.0) -> str:
    """Closed SVG path through the control points (Catmull-Rom converted to cubic Béziers)."""
    pts = [(x * scale + dx, y * scale + dy) for x, y in points]
    n = len(pts)
    d = [f"M{pts[0][0]:.1f},{pts[0][1]:.1f}"]
    for i in range(n):
        p0, p1, p2, p3 = (pts[(i + k - 1) % n] for k in range(4))
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d.append(f"C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}")
    return " ".join(d) + "Z"


class Track:
    def __init__(self, points=CONTROL_POINTS, scale=1.0, dx=0.0, dy=0.0):
        self.path = bezier_path(points, scale, dx, dy)
        poly = [(x * scale + dx, y * scale + dy) for x, y in _catmull_rom(points)]
        poly.append(poly[0])
        self.poly = poly
        self.cum = [0.0]
        for a, b in zip(poly, poly[1:]):
            self.cum.append(self.cum[-1] + math.dist(a, b))
        self.length = self.cum[-1]

    def at(self, s: float):
        """Point and tangent angle (degrees) at arc length s."""
        s %= self.length
        lo, hi = 0, len(self.cum) - 1
        while lo < hi - 1:
            mid = (lo + hi) // 2
            if self.cum[mid] <= s:
                lo = mid
            else:
                hi = mid
        a, b = self.poly[lo], self.poly[lo + 1]
        seg = self.cum[lo + 1] - self.cum[lo] or 1.0
        t = (s - self.cum[lo]) / seg
        x, y = a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t
        ang = math.degrees(math.atan2(b[1] - a[1], b[0] - a[0]))
        return x, y, ang
