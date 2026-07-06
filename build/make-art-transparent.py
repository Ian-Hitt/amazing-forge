#!/usr/bin/env python3
"""Key the near-white paper background out of the generated sketches (build/art/*.png).

The Gemini sketches are drawn on a *near*-white ground (~243-255), not pure white
and with no alpha — so on the pure-white book page they show as a faint off-white
rectangle. This flood-fills that paper region inward from the image borders and
makes it transparent, leaving the linework (and any light area *enclosed* by
linework) fully opaque. Because it fills only the border-connected region, it
removes the background box without touching interior tones — no halos, no washed
mid-grays.

Originals are copied once into build/art/raw/ before anything is overwritten, so
this is safe to re-run: it always re-derives from the pristine raw copy.

Use:
    ./build/make-art-transparent.py            # process every PNG
    ./build/make-art-transparent.py --only G3,D1
"""
from __future__ import annotations
import argparse, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
ART = ROOT / "build" / "art"
RAW = ART / "raw"

# Fill tolerance around each seed's colour. Paper sits ~243-255; ink/shading is
# darker, so ~24 captures the paper (and its gentle gradient) without eating the
# soft pencil work that starts lower down.
THRESH = 26
SENTINEL = (255, 0, 255)  # a colour that can't occur in a grayscale sketch


def seeds(w, h):
    m = 2  # inset a hair so we sample paper, not a stray edge pixel
    xs = (m, w // 2, w - 1 - m)
    ys = (m, h // 2, h - 1 - m)
    # every border point (corners + edge midpoints); skip the true centre
    return [(x, y) for x in xs for y in ys if not (x == w // 2 and y == h // 2)]


def process(src: Path, dst: Path) -> None:
    im = Image.open(src).convert("RGB")
    w, h = im.size
    mask = im.copy()
    for (x, y) in seeds(w, h):
        # only seed from a genuinely light pixel — don't flood from a dark border
        if sum(mask.getpixel((x, y))) / 3 < 200:
            continue
        ImageDraw.floodfill(mask, (x, y), SENTINEL, thresh=THRESH)
    # alpha: 0 where the fill reached (paper), 255 elsewhere (the drawing)
    alpha = Image.new("L", (w, h), 255)
    apx = alpha.load()
    mpx = mask.load()
    for j in range(h):
        for i in range(w):
            if mpx[i, j] == SENTINEL:
                apx[i, j] = 0
    # soften the cut a touch so the edge isn't aliased
    alpha = alpha.filter(ImageFilter.GaussianBlur(0.6))
    out = im.convert("RGBA")
    out.putalpha(alpha)
    out.save(dst)
    cleared = sum(1 for j in range(h) for i in range(w) if mpx[i, j] == SENTINEL)
    print(f"  {src.name}: cleared {cleared * 100 // (w * h)}% to transparent")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="comma-separated slot IDs (default: all PNGs)")
    args = ap.parse_args()

    RAW.mkdir(parents=True, exist_ok=True)
    pngs = sorted(p for p in ART.glob("*.png"))
    if args.only:
        want = {s.strip() for s in args.only.split(",")}
        pngs = [p for p in pngs if p.stem in want]
    if not pngs:
        print("no matching PNGs.", file=sys.stderr)
        return 1

    for p in pngs:
        raw = RAW / p.name
        if not raw.exists():          # back up the pristine original exactly once
            raw.write_bytes(p.read_bytes())
        process(raw, p)               # always derive from the raw copy
    print(f"done: {len(pngs)} image(s). Rebuild: ./build/build-pdf.sh")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
