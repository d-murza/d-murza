#!/usr/bin/env python3
"""Build dist/contribution-circuit.svg from the last year of GitHub contributions.

    python scripts/generate-circuit.py            # real data (needs GITHUB_TOKEN)
    python scripts/generate-circuit.py --demo     # offline preview with fake data
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from garage.circuit import build
from garage.github import demo_calendar, fetch_calendar

USERNAME = "d-murza"


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--demo", action="store_true", help="use generated sample data")
    parser.add_argument("--output", type=Path, default=Path("dist/contribution-circuit.svg"))
    args = parser.parse_args()

    days, total = demo_calendar() if args.demo else fetch_calendar(USERNAME)
    svg = build(days, total, USERNAME)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(svg, encoding="utf-8")
    print(f"Wrote {args.output} ({len(days)} days, {total} contributions, {len(svg) // 1024} KB)")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # surface a clean error in the Action log
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
