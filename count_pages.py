#!/usr/bin/env python3
"""
Amazing Forge — printed page-count estimator.

Estimates how long the book would be as a printed TTRPG, from the live
Markdown manuscript in docs/. Run it any time to re-check as chapters grow:

    python3 count_pages.py
    ./.venv/bin/python count_pages.py   # if you want the venv interpreter

TARGET FORMAT (decided 2026-06-09): a 6x9 trade paperback, the size of
Monster of the Week / Dungeon World (NOT a D&D-sized hardback). We assume
MINIMAL ART and GENEROUS MARGINS, which lowers words-per-page density.

Words-per-page bands below are calibrated for that format. RPG pages run a
lot lighter than a novel: headers, move/stat boxes, tables, callouts, and
whitespace all eat space without eating word count. The three bands let you
see a best/expected/worst spread rather than one false-precision number.

Tables are special: a table occupies far more vertical space than its word
count implies, so we count table rows separately and bill them a flat page
cost instead of letting them sink into the prose density.
"""

import re
import sys
from pathlib import Path

# --- tuning knobs (6x9, minimal art, generous margins) ---------------------

# Effective prose density, words per printed page.
#   LOW  = airier layout / more callouts and chapter breaks  -> longer book
#   MID  = expected
#   HIGH = denser running text                               -> shorter book
WORDS_PER_PAGE = {"low": 280, "mid": 320, "high": 360}

# A table row (incl. header/separator) is mostly vertical space, not words.
# Bill each row a flat slice of a page rather than counting its words as prose.
ROWS_PER_PAGE = 34          # how many table rows fill one 6x9 page
FRONT_BACK_MATTER_PAGES = 8 # title, credits, ToC, blank versos, back cover, etc.

PARTS = [
    ("Part One — Your First Game", "docs/part-one"),
    ("Part Two — Playing the Game", "docs/part-two"),
    ("Part Three — Building Your World", "docs/part-three"),
    ("Part Four — Reference & Tools", "docs/part-four"),
]

# ---------------------------------------------------------------------------

CODE_FENCE = re.compile(r"^```")
TABLE_ROW = re.compile(r"^\s*\|.*\|\s*$")
TABLE_SEP = re.compile(r"^\s*\|?[\s:|-]+\|?\s*$")  # |---|:--:| separator rows
HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
MD_NOISE = re.compile(r"[#>*_`~\[\]()!|]")


def analyze(text):
    """Return (prose_words, table_rows) for one Markdown document."""
    text = HTML_COMMENT.sub(" ", text)
    prose_words = 0
    table_rows = 0
    in_fence = False
    for line in text.splitlines():
        if CODE_FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            prose_words += len(line.split())
            continue
        if TABLE_ROW.match(line):
            table_rows += 1
            if not TABLE_SEP.match(line):
                # body/header rows still carry a little readable content
                prose_words += len(MD_NOISE.sub(" ", line).split()) // 2
            continue
        prose_words += len(MD_NOISE.sub(" ", line).split())
    return prose_words, table_rows


def part_pages(words, rows, wpp):
    return words / wpp + rows / ROWS_PER_PAGE


def collect(part_dir):
    root = Path(__file__).parent
    files = sorted((root / part_dir).rglob("*.md"))  # recurse into subfolders (e.g. genres/)
    words = rows = 0
    for f in files:
        w, r = analyze(f.read_text(encoding="utf-8"))
        words += w
        rows += r
    return words, rows, len(files)


def main():
    print("Amazing Forge — printed page estimate")
    print("Format: 6x9 trade paperback (MotW / Dungeon World), minimal art, generous margins")
    print("=" * 78)
    header = f"{'Part':36} {'files':>5} {'words':>7} {'rows':>5} {'low':>6} {'mid':>6} {'high':>6}"
    print(header)
    print("-" * 78)

    tot_w = tot_r = tot_f = 0
    tot = {k: 0.0 for k in WORDS_PER_PAGE}

    # include any loose top-level docs (index.md, etc.) under a catch-all
    seen_dirs = {d for _, d in PARTS}
    extra = []
    for f in sorted(Path(__file__).parent.glob("docs/*.md")):
        extra.append(f)

    rows_to_print = list(PARTS)

    for label, d in rows_to_print:
        w, r, nf = collect(d)
        tot_w += w
        tot_r += r
        tot_f += nf
        cells = {}
        for k, wpp in WORDS_PER_PAGE.items():
            p = part_pages(w, r, wpp)
            tot[k] += p
            cells[k] = p
        print(f"{label:36} {nf:>5} {w:>7} {r:>5} "
              f"{cells['low']:>6.0f} {cells['mid']:>6.0f} {cells['high']:>6.0f}")

    # loose docs (e.g. docs/index.md)
    if extra:
        w = r = 0
        for f in extra:
            ww, rr = analyze(f.read_text(encoding="utf-8"))
            w += ww
            r += rr
        tot_w += w
        tot_r += r
        tot_f += len(extra)
        cells = {}
        for k, wpp in WORDS_PER_PAGE.items():
            p = part_pages(w, r, wpp)
            tot[k] += p
            cells[k] = p
        print(f"{'(landing / loose docs)':36} {len(extra):>5} {w:>7} {r:>5} "
              f"{cells['low']:>6.0f} {cells['mid']:>6.0f} {cells['high']:>6.0f}")

    print("-" * 78)
    print(f"{'Manuscript subtotal':36} {tot_f:>5} {tot_w:>7} {tot_r:>5} "
          f"{tot['low']:>6.0f} {tot['mid']:>6.0f} {tot['high']:>6.0f}")
    for k in tot:
        tot[k] += FRONT_BACK_MATTER_PAGES
    print(f"{'+ front/back matter (~%d pp)' % FRONT_BACK_MATTER_PAGES:36} "
          f"{'':>5} {'':>7} {'':>5} "
          f"{tot['low']:>6.0f} {tot['mid']:>6.0f} {tot['high']:>6.0f}")
    print("=" * 78)
    print(f"ESTIMATED PRINTED LENGTH: ~{tot['mid']:.0f} pages "
          f"(range {tot['low']:.0f}–{tot['high']:.0f})")
    print(f"Total manuscript words: {tot_w:,}")


if __name__ == "__main__":
    sys.exit(main())
