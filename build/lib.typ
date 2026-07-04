// Lights, Camera, Action! — shared definitions (colors, states, helpers).
// Imported by BOTH book.typ and the generated content.typ so that
// part-divider() resolves inside the included content.

// ---- palette ---------------------------------------------------------------
// Two outputs from one source. Color (digital):  ./build/build-pdf.sh
// Print interior (B&W-priced):                    ./build/build-pdf.sh print
// Print mode makes every chromatic color ink-black / neutral gray, so a POD
// printer classifies the interior as black-ink (the cheap tier), not color.
#let print-mode = sys.inputs.at("mode", default: "color") == "print"

// ---- font stacks -----------------------------------------------------------
// All OFL/commercially-embeddable (see build/fonts/ + its LICENSE-*.txt). The
// DejaVu Sans tail covers arrows (→ ← ↔), the Showdown star (★) and ✓/✗ marks
// so the build never silently falls back to a system (Apple) font for a glyph.
// Built hermetically via --ignore-system-fonts, so only build/fonts/ is used.
#let sans  = ("Montserrat", "DejaVu Sans")          // display: headings, heads, tables
#let serif = ("Source Serif 4", "DejaVu Sans")      // body text

#let accent     = if print-mode { rgb("#111111") } else { rgb("#cf4b1a") }  // deep orange
#let ink        = rgb("#1a1a1a")
#let soft       = rgb("#6b6b6b")                                            // gray (B&W-safe)
#let table-fill = if print-mode { rgb("#ededed") } else { rgb("#f4ece6") }
#let callout-bg = if print-mode { rgb("#f2f2f2") } else { rgb("#faf4ef") }
#let pos-color  = if print-mode { rgb("#1a1a1a") } else { rgb("#2e7d32") }  // green ✓
#let neg-color  = if print-mode { rgb("#1a1a1a") } else { rgb("#c0392b") }  // red ✗

// good/bad markers (substituted in for ✅/❌ at build time; print-aware)
#let good = text.with(fill: pos-color, weight: "bold")
#let bad  = text.with(fill: neg-color, weight: "bold")

// pandoc's typst writer emits `#horizontalrule` for `---` thematic breaks
#let horizontalrule = align(center)[#v(0.3em) #line(length: 28%, stroke: 0.6pt + soft) #v(0.3em)]

// move card — the print equivalent of the website's `.lca-move` (see
// docs/stylesheets/extra.css): a full-bordered box with a thick accent left
// edge, a name in accent, and an optional italic "when" descriptor. The SRD
// build rewrites each %%%LCAMOVE|name|when%%% marker into a call to this.
#let lca-move(name: [], when: [], body) = block(
  width: 100%,
  inset: (left: 11pt, rest: 9pt),
  above: 1.0em, below: 1.0em,
  fill: callout-bg,
  stroke: (left: 3.5pt + accent, rest: 0.5pt + soft.lighten(35%)),
  radius: 3pt,
  breakable: true,
)[
  #block(above: 0pt, below: 0.5em)[
    #text(font: sans, weight: 700, fill: accent, size: 11pt)[#name]
    #if when != [] {
      text(font: sans, style: "italic", fill: soft, size: 9pt)[ #sym.dash.em #when]
    }
  ]
  #set par(first-line-indent: 0pt)
  #body
]

// ---- art slots -------------------------------------------------------------
// Every illustration position in the book is a "slot." The build script checks
// build/art/ for a file named by the slot ID (e.g. G3.png): if present it emits
// an #art-image(...) call; if absent it emits #art-placeholder(...), a labeled
// dashed box so the position is still visibly PLACED in the PDF before real art
// exists. Drop an image named by ID into build/art/ and it swaps in on rebuild.
#let art-placeholder(id, caption, width: 100%, height: 2in) = block(
  width: width, height: height, above: 1.2em, below: 1.2em,
  fill: luma(246), stroke: (paint: soft, thickness: 0.8pt, dash: "dashed"),
  radius: 3pt, inset: 12pt, breakable: false,
)[
  #align(center + horizon)[
    #set text(font: sans, fill: soft)
    #set par(justify: false, leading: 0.5em)
    #text(weight: 700, size: 9.5pt, tracking: 0.15em)[ART · #upper(id)]
    #v(0.35em)
    #text(size: 8.5pt, style: "italic")[#caption]
  ]
]
#let art-image(path, width: 100%, height: auto) = block(
  above: 1.2em, below: 1.2em, breakable: false,
)[#image(path, width: width, height: height, fit: "contain")]

// running-head state: current Part and Chapter
#let cur-part = state("cur-part", none)
#let cur-chap = state("cur-chap", none)

// orphan-heading control. Headings are `sticky` (they won't be the last thing
// on a page), but sticky is happy as long as the heading + one line of the next
// block fits — so a heading can still land near the bottom with a stub of text
// under it. `heading-keep` reserves a fixed slab of space *below* the heading:
// the heading and a `reserve`-tall spacer live in one unbreakable block, so if
// less than that remains on the page Typst relocates the whole thing to the next
// page (leaving a gap below the previous section — room for art). A negative
// bottom margin pulls the following text back up into the reserved slab, so when
// the heading does NOT get bumped, spacing looks completely normal.
//
// This is deliberately query-free: an earlier here().position() + conditional
// pagebreak version oscillated (heading moves → remeasures → moves back) and
// never converged, corrupting page numbers. Reserving unbreakable height lets
// Typst's native page-breaker make the call in a single stable pass.
#let heading-keep(above, gap-below, reserve, inner) = block(
  breakable: false, sticky: true, above: above, below: gap-below - reserve,
)[
  #inner
  #v(reserve)
]

// full-page part divider. `slot`/`art`: the divider illustration (D1–D4). The
// build passes art: image(...) when the file exists, else leaves it none and we
// draw a full-width placeholder box beneath the title so the slot is visible.
#let part-divider(kicker, title, slot: none, art: none) = {
  cur-part.update(kicker)
  cur-chap.update(none)
  pagebreak(weak: true)        // digital build: no odd-page forcing (avoids blank versos)
  set page(header: none, footer: none)
  v(1.3in)
  align(center)[
    #text(font: sans, size: 12pt, weight: 600, fill: soft, tracking: 0.3em)[#upper(kicker)]
    #v(0.5em)
    #line(length: 1.4in, stroke: 1.5pt + accent)
    #v(0.6em)
    #text(font: sans, size: 30pt, weight: 800, fill: accent)[#title]
  ]
  v(0.7in)
  if art != none { align(center)[#art] }
  else if slot != none { art-placeholder(slot, kicker + " divider illustration", height: 3.4in) }
  pagebreak(weak: true)
}
