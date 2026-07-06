#!/usr/bin/env python3
"""Deal scene vignettes to chapter openers and composite one banner per chapter.

The chapter-opener film strip is a FIXED frame (compose-strip.py) with three
scene windows. This deals three vignettes from the pool (build/art/V*.png) to
each opener-bearing chapter — deterministically (fixed seed, so rebuilds are
stable) and with no scene repeated from the immediately preceding chapter — then
composites build/art/openers/<slug>.png for each.

build-pdf.sh passes the chapters in reading order via --slugs; it then injects a
#chapter-opener("…/openers/<slug>.png") after each chapter's H1.

Use:
    ./build/deal-openers.py --slugs foreword,01-build-your-world,02-create-your-hero,…
"""
from __future__ import annotations
import argparse, random, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ART = ROOT / "build" / "art"
OUT = ART / "openers"
COMPOSE = ROOT / "build" / "compose-strip.py"
SEED = 7  # fixed → same deal every rebuild (banners don't churn)


def pool() -> list[str]:
    ids = [p.stem for p in ART.glob("V*.png") if p.stem[1:].isdigit()]
    return sorted(ids, key=lambda s: int(s[1:]))


def deal(slugs: list[str], scenes: list[str]) -> dict[str, list[str]]:
    rnd = random.Random(SEED)
    out: dict[str, list[str]] = {}
    prev: set[str] = set()
    for slug in slugs:
        avail = [v for v in scenes if v not in prev]
        if len(avail) < 3:            # tiny pool safety net
            avail = scenes[:]
        pick = rnd.sample(avail, 3)
        out[slug] = pick
        prev = set(pick)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slugs", required=True, help="comma-separated chapter slugs in reading order")
    args = ap.parse_args()

    scenes = pool()
    if len(scenes) < 3:
        print(f"need at least 3 vignettes in build/art/ (found {len(scenes)})", file=sys.stderr)
        return 1
    slugs = [s.strip() for s in args.slugs.split(",") if s.strip()]
    OUT.mkdir(parents=True, exist_ok=True)

    assignment = deal(slugs, scenes)
    for slug, triple in assignment.items():
        dst = OUT / f"{slug}.png"
        subprocess.run(
            [sys.executable, str(COMPOSE), "--scenes", ",".join(triple), "--out", str(dst)],
            check=True, stdout=subprocess.DEVNULL,
        )
    print(f"dealt + composited {len(assignment)} chapter opener(s) from {len(scenes)} scenes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
