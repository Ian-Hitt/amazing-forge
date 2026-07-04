// Lights, Camera, Action! — System Reference Document (SRD) print template.
// A standalone 6×9 booklet built from docs/part-four/rules-reference.md only.
// Shares typography with book.typ and colors/helpers with lib.typ; content is
// written to content-srd.typ by build-srd-pdf.sh and #included below.

#import "lib.typ": *

#set document(title: "Lights, Camera, Action! — System Reference Document", author: "Ian Hitt")

// ---- page geometry: 6×9, matches the book -------------------------------
#set page(
  width: 6in, height: 9in,
  margin: (inside: 0.9in, outside: 0.7in, top: 0.8in, bottom: 0.8in),
  binding: left,
  header: context {
    let here = here().page()
    let openers = query(heading.where(level: 1)).map(h => h.location().page())
    if openers.contains(here) { return }
    set text(font: sans, size: 8pt, fill: soft, tracking: 0.08em)
    let sec = cur-chap.get()
    if calc.even(here) [#align(left)[#upper[Lights, Camera, Action! — SRD]]]
    else [#align(right)[#upper(if sec != none { sec })]]
  },
  footer: context {
    let n = counter(page).get().first()
    set text(font: sans, size: 9pt, fill: soft)
    if calc.odd(n) { align(right)[#n] } else { align(left)[#n] }
  },
)

// ---- base text + paragraphs (matches book.typ) -----------------------------
#set text(font: serif, size: 10.5pt, fill: ink, lang: "en")
#set par(justify: true, leading: 0.72em, first-line-indent: 0pt, spacing: 0.9em)
#show link: it => text(fill: accent)[#it]

#set list(indent: 0.7em, body-indent: 0.5em, spacing: 0.72em)
#set enum(indent: 0.7em, body-indent: 0.5em, spacing: 0.72em)
#show list: set block(spacing: 1.0em)
#show enum: set block(spacing: 1.0em)

// ---- headings --------------------------------------------------------------
// H1 = a top-level SRD section opener (there are three). Lighter sink than the
// book's chapter openers — this is a reference booklet, not a chaptered book.
#show heading.where(level: 1): it => {
  pagebreak(weak: true)
  cur-chap.update(it.body)
  v(0.7in)
  block(above: 0pt, below: 1.5em)[
    #set text(font: sans, size: 23pt, weight: 800, fill: accent)
    #set par(first-line-indent: 0pt, justify: false, leading: 0.4em)
    #it.body
    #v(0.3em)
    #line(length: 2.2em, stroke: 2pt + accent)
  ]
}
// reserve space below each heading so it never starts near the page bottom
// (see heading-keep in lib.typ) — leaves a gap on the prior page for art.
#show heading.where(level: 2): it => heading-keep(1.5em, 1.4em, 54pt)[
  #set text(font: sans, size: 14pt, weight: 700, fill: ink)
  #set par(first-line-indent: 0pt, justify: false)
  #it.body
]
#show heading.where(level: 3): it => heading-keep(1.05em, 1.3em, 40pt)[
  #set text(font: sans, size: 11pt, weight: 700, fill: accent)
  #set par(first-line-indent: 0pt, justify: false)
  #it.body
]
#show heading.where(level: 4): it => heading-keep(0.9em, 1.2em, 32pt)[
  #set text(font: sans, size: 10pt, weight: 700, fill: ink)
  #set par(first-line-indent: 0pt, justify: false)
  #it.body
]

// ---- tables (matches book.typ) ---------------------------------------------
#show figure: set block(breakable: true)
#show figure.where(kind: table): set block(above: 1.1em, below: 1.1em)
#set table(
  stroke: 0.5pt + rgb("#b8b8b8"),
  inset: (x: 7pt, y: 6pt),
  fill: (x, y) => if y == 0 { table-fill },
  align: left + top,
)
#show table.cell.where(y: 0): set text(font: sans, weight: 700, size: 9pt)
#show table: set text(size: 9.5pt)
#show table: set par(first-line-indent: 0pt, justify: false, leading: 0.6em, spacing: 0.5em)

// ---- blockquotes → callout boxes (matches book.typ) ------------------------
#show quote.where(block: true): it => block(
  width: 100%, inset: (left: 12pt, rest: 10pt), above: 0.9em, below: 0.9em,
  fill: callout-bg, stroke: (left: 2.5pt + accent), radius: 2pt,
)[
  #set text(style: "italic")
  #set par(first-line-indent: 0pt)
  #it.body
]

// ---- title page ------------------------------------------------------------
#page(header: none, footer: none)[
  #v(1.6in)
  #align(center)[
    #block[
      #set text(font: sans, size: 40pt, weight: 800, fill: accent, hyphenate: false)
      #set par(justify: false, leading: 0.2em)
      Lights,\
      Camera,\
      Action!
    ]
    #v(0.5em)
    #line(length: 2in, stroke: 2pt + accent)
    #v(0.6em)
    #text(font: sans, size: 15pt, weight: 700, fill: ink)[System Reference Document]
    #v(0.4em)
    #text(font: sans, size: 11pt, weight: 500, fill: soft)[
      The whole game, in one place
    ]
  ]
  #place(bottom + center, dy: -0.2in)[
    #text(font: sans, size: 9pt, fill: soft)[Working draft]
  ]
]

// ---- copyright / license ---------------------------------------------------
// The SRD is the open-system document: system offered under CC BY 4.0.
#page(header: none, footer: none)[
  #v(0.9in)
  #align(center)[
    #text(font: sans, size: 15pt, weight: 800, fill: accent)[Lights, Camera, Action!]
    #v(0.25em)
    #text(font: sans, size: 8pt, fill: soft, tracking: 0.25em)[SYSTEM REFERENCE DOCUMENT]
    #v(0.5em)
    #text(font: serif, size: 10.5pt, style: "italic")[A cinematic, zero-prep tabletop RPG]
  ]
  #place(bottom + left, dx: 0in, dy: 0in)[
    #set text(font: serif, size: 8.5pt, fill: soft)
    #set par(justify: false, leading: 0.6em, spacing: 0.7em, first-line-indent: 0pt)
    #block(width: 100%)[
      This System Reference Document describes the _Lights, Camera, Action!_ game
      system. The system is made available under the Creative Commons Attribution
      4.0 International License (CC BY 4.0, creativecommons.org/licenses/by/4.0).
      You are free to create and sell your own material using this system, with
      attribution.

      The CC BY 4.0 license covers the *game system* — the rules, mechanics, and
      procedures set out in this document. It does not extend to the text, art,
      layout, or presentation of the full rulebook, _Lights, Camera, Action!_,
      which are all rights reserved.

      Set in Montserrat and Source Serif 4 (SIL Open Font License 1.1), with
      DejaVu Sans. Made with MkDocs, Pandoc, and Typst. #linebreak()
      Read or play online: ian-hitt.github.io/amazing-forge
    ]
  ]
]

// ---- table of contents -----------------------------------------------------
#page(header: none, footer: none)[
  #text(font: sans, size: 20pt, weight: 800, fill: accent)[Contents]
  #v(0.5em)
  #set text(size: 9.5pt)
  #show outline.entry.where(level: 1): it => {
    v(0.45em); text(font: sans, weight: 700)[#it]
  }
  #outline(title: none, depth: 2, indent: auto)
]

#counter(page).update(1)

#include "content-srd.typ"
