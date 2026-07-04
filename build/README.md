# PDF build — Lights, Camera, Action!

Turns the Markdown in `docs/` into a polished 6×9 PDF (`build/Lights-Camera-Action.pdf`).
The Markdown stays the single source of truth; re-run the build any time it changes.

## Pipeline

```
docs/*.md  ──pandoc (gfm → Typst)──▶  content.typ  ──book.typ template──▶  Lights-Camera-Action.pdf
```

- **`build-pdf.sh`** — orchestrator. Lists the chapters per Part (in reading order),
  runs Pandoc on each, assembles `content.typ` with part dividers, compiles with Typst.
- **`book.typ`** — the book template: 6×9 geometry, gutter margins, fonts, heading
  styles, running heads, table/blockquote styling, title page, table of contents.
- **`lib.typ`** — shared colors, the `part-divider()` helper, and the `horizontalrule`
  glue Pandoc needs. Imported by both `book.typ` and `content.typ`.
- **`content.typ`** — generated each run; do not edit by hand.

## Build it

```bash
./build/build-pdf.sh          # → build/Lights-Camera-Action.pdf        (full color, for digital)
./build/build-pdf.sh print    # → build/Lights-Camera-Action-print.pdf  (ink-black, B&W-priced POD)
```

Requires `pandoc` and `typst` (`brew install pandoc typst`).

### Standalone SRD booklet

The System Reference Document (`docs/part-four/rules-reference.md`) also builds on its
own as a compact 6×9 booklet — the whole game in ~15 pages:

```bash
./build/build-srd-pdf.sh          # → build/Lights-Camera-Action-SRD.pdf
./build/build-srd-pdf.sh print    # → build/Lights-Camera-Action-SRD-print.pdf  (B&W-priced)
```

Pipeline: `rules-reference.md ──srd-preprocess.py──▶ pandoc ──marker rewrite──▶ srd.typ ──▶ PDF`.

- **`srd-preprocess.py`** rewrites the web SRD's raw-HTML `.lca-move` move cards (which
  Pandoc would otherwise drop) into `%%%LCAMOVE|name|when%%%` sentinels.
- **`build-srd-pdf.sh`** runs Pandoc, rewrites those sentinels into `#lca-move(…)` card
  calls, unwraps intra-doc anchor links (MkDocs slugs that don't resolve in print), and
  compiles with **`srd.typ`** — an SRD title/CC-BY page, a depth-2 reference TOC, and
  lighter section openers. Shares fonts, colors, and the `lca-move` card style with the
  book build via `lib.typ`.
- **`content-srd.typ`** is generated each run; do not edit by hand.

**Color vs. print.** The default build uses the deep-orange accent + warm table/callout
tints — free on screen, on-brand for the website. The `print` build swaps every chromatic
color for ink-black / neutral gray so a print-on-demand service (KDP, DriveThruRPG)
classifies the interior as **black-ink** — the cheap tier (~$3–4/copy vs. ~$18–25 for color
on a 250-page 6×9). The switch is one flag (`--input mode=print`); the palette lives at the
top of `lib.typ`.

### Preview specific pages as images

```bash
typst compile --root . --pages 1,2,120 --format png build/book.typ "build/preview/p{p}.png"
```

## Typography

- Body: **Iowan Old Style** · Headings/UI: **Avenir Next** · Accent: deep orange `#cf4b1a`
  (matches the website). Change these at the top of `lib.typ` / `book.typ`.

## What's included / excluded

Included: front matter, Parts One–Three, and the prose chapters of Part Four.

**Excluded by design:** the 6 Part Four HTML form-sheets — hero sheet, quest tracker,
cast sheet, places sheet, moves cheatsheet, world-forge worksheet. These are bespoke
HTML/CSS *printables* that already render perfectly on the website; print those pages
straight from the browser. Re-creating them in Typst is a separate, optional task.

When chapters are added/renamed, update both `nav:` in `mkdocs.yml` **and** the file
arrays in `build-pdf.sh`.

## Known manuscript issues this surfaced (content fixes, not pipeline bugs)

1. **Draft status tags in headings** — several chapter H1s end with `(Complete)`
   (e.g. `# Chapter 7 — The Roll (Complete)`). These print verbatim in the book and ToC.
2. **Inconsistent chapter heading levels** — 9 chapter files open with `## Chapter …`
   (level 2) instead of `# Chapter …` (level 1), so they don't get chapter-opener
   styling (new page + large title) in the PDF. Normalizing to `#` fixes the PDF and
   tidies the website's in-page outline too.

## Roadmap to print-on-demand (when ready)

The digital build above is the free/distributable PDF. To graduate to a print-ready
file for KDP / DriveThruRPG, the increments are small because the layout already exists:

- Re-enable odd-page part/chapter starts (`pagebreak(to: "odd")` in `lib.typ`/`book.typ`).
- Add bleed + crop marks via `#set page(..., bleed: ...)` and export PDF/X.
- Size the gutter for the final page count; order a physical proof.
- Design a wraparound cover (back + spine + front) in a layout app — the one task that
  lives outside this pipeline.
