"""Fetch the contribution calendar from the GitHub GraphQL API (or fake one for previews)."""
from __future__ import annotations

import datetime as dt
import json
import os
import random
import urllib.request

QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount } }
      }
    }
  }
}
"""


def fetch_calendar(login: str):
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("GITHUB_TOKEN is not set (use --demo for an offline preview)")
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": login}}).encode(),
        headers={"Authorization": f"bearer {token}", "User-Agent": "contribution-circuit"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = json.load(resp)
    if payload.get("errors"):
        raise RuntimeError(payload["errors"])
    cal = payload["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    days = [{"date": d["date"], "count": d["contributionCount"]}
            for w in cal["weeks"] for d in w["contributionDays"]]
    return days, cal["totalContributions"]


def demo_calendar(seed: int = 7):
    rng = random.Random(seed)
    today = dt.date.today()
    days = []
    for i in range(364, -1, -1):
        d = today - dt.timedelta(days=i)
        busy = 0.35 + 0.45 * (d.weekday() < 5)
        count = 0 if rng.random() > busy else int(rng.expovariate(0.25)) + 1
        days.append({"date": d.isoformat(), "count": count})
    return days, sum(d["count"] for d in days)


def stats(days):
    counts = [d["count"] for d in days]
    best = max(days, key=lambda d: d["count"]) if days else {"count": 0, "date": "-"}
    longest = cur = 0
    for c in counts:
        cur = cur + 1 if c else 0
        longest = max(longest, cur)
    # current streak; a quiet "today" doesn't end it yet
    tail = counts[:-1] if counts and counts[-1] == 0 else counts
    current = 0
    for c in reversed(tail):
        if not c:
            break
        current += 1
    return {
        "best": best["count"], "best_date": best["date"],
        "longest": longest, "current": current,
        "active": sum(1 for c in counts if c),
    }


def level(count: int, ceiling: int) -> int:
    """0-4 intensity relative to a robust ceiling (like GitHub's quartiles)."""
    if count <= 0:
        return 0
    r = count / max(ceiling, 1)
    return 1 if r <= 0.25 else 2 if r <= 0.5 else 3 if r <= 0.8 else 4
