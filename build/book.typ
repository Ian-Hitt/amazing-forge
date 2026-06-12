// Lights, Camera, Action! — print book template (6×9 trade paperback)
// Generated content is written to content.typ by build-pdf.sh and #included below.
// Edit THIS file for typography / layout; edit lib.typ for colors & dividers.

#import "lib.typ": *

#set document(title: "Lights, Camera, Action!", author: "Ian Hitt")

// ---- page geometry: 6×9, gutter margins, page numbers on the outside ------
#set page(
  width: 6in, height: 9in,
  margin: (inside: 0.95in, outside: 0.7in, top: 0.85in, bottom: 0.8in),
  binding: left,
  header: context {
    let here = here().page()
    let openers = query(heading.where(level: 1)).map(h => h.location().page())
    if openers.contains(here) { return }
    set text(font: "Avenir Next", size: 8pt, fill: soft, tracking: 0.08em)
    let part = cur-part.get()
    let chap = cur-chap.get()
    if calc.even(here) [#align(left)[#upper(if part != none { part })]]
    else [#align(right)[#upper(if chap != none { chap })]]
  },
  footer: context {
    let n = counter(page).get().first()
    set text(font: "Avenir Next", size: 9pt, fill: soft)
    if calc.odd(n) { align(right)[#n] } else { align(left)[#n] }
  },
)

// ---- base text + paragraphs -----------------------------------------------
// Block paragraphs: no first-line indent, a clear gap between paragraphs so the
// breaks read clearly (vs. the old indent-only run-together look).
#set text(font: ("Iowan Old Style", "Apple Color Emoji"), size: 10.5pt, fill: ink, lang: "en")
#set par(justify: true, leading: 0.72em, first-line-indent: 0pt, spacing: 0.9em)
#show link: it => text(fill: accent)[#it]

// ---- lists: indented, with breathing room between items and around the list -
#set list(indent: 0.7em, body-indent: 0.5em, spacing: 0.72em)
#set enum(indent: 0.7em, body-indent: 0.5em, spacing: 0.72em)
#show list: set block(spacing: 1.0em)
#show enum: set block(spacing: 1.0em)

// ---- headings --------------------------------------------------------------
#show heading.where(level: 1): it => {
  pagebreak(weak: true)
  cur-chap.update(it.body)
  v(1.4in)                       // chapter sink — standard book opener drop
  block(above: 0pt, below: 1.4em)[
    #set text(font: "Avenir Next", size: 26pt, weight: 800, fill: accent)
    #set par(first-line-indent: 0pt, justify: false, leading: 0.4em)
    #it.body
    #v(0.35em)
    #line(length: 2.2em, stroke: 2pt + accent)
  ]
}
#show heading.where(level: 2): it => block(above: 1.6em, below: 0.55em, sticky: true)[
  #set text(font: "Avenir Next", size: 14pt, weight: 700, fill: ink)
  #set par(first-line-indent: 0pt, justify: false)
  #it.body
]
#show heading.where(level: 3): it => block(above: 1.15em, below: 0.35em, sticky: true)[
  #set text(font: "Avenir Next", size: 11pt, weight: 700, fill: accent)
  #set par(first-line-indent: 0pt, justify: false)
  #it.body
]

// ---- tables: full-width, full grid, left-aligned, airy, page-breakable -----
// (Column widths are remapped to "first col auto, rest 1fr" in build-pdf.sh so
//  every table fills the text measure and long cells wrap instead of overflowing.)
#show figure: set block(breakable: true)
#show figure.where(kind: table): set block(above: 1.2em, below: 1.2em)
#set table(
  stroke: 0.5pt + rgb("#b8b8b8"),          // full grid — every cell bordered
  inset: (x: 7pt, y: 6pt),                 // more cell padding
  fill: (x, y) => if y == 0 { table-fill },
  align: left + top,                       // text left-aligned, never centered
)
#show table.cell.where(y: 0): set text(font: "Avenir Next", weight: 700, size: 9pt)
#show table: set text(size: 9.5pt)
#show table: set par(first-line-indent: 0pt, justify: false, leading: 0.6em, spacing: 0.5em)

// ---- blockquotes → callout boxes ------------------------------------------
#show quote.where(block: true): it => block(
  width: 100%, inset: (left: 12pt, rest: 10pt), above: 0.9em, below: 0.9em,
  fill: callout-bg, stroke: (left: 2.5pt + accent), radius: 2pt,
)[
  #set text(style: "italic")
  #set par(first-line-indent: 0pt)
  #it.body
]

// ---- front matter: title page ---------------------------------------------
#page(header: none, footer: none)[
  #v(2.2in)
  #align(center)[
    #text(font: "Avenir Next", size: 46pt, weight: 800, fill: accent)[Lights, Camera, Action!]
    #v(0.4em)
    #line(length: 2in, stroke: 2pt + accent)
    #v(0.6em)
    #text(font: "Avenir Next", size: 13pt, weight: 500, fill: soft)[
      A cinematic, zero-prep tabletop RPG for ages 10+
    ]
  ]
  #place(bottom + center, dy: -0.2in)[
    #text(font: "Avenir Next", size: 9pt, fill: soft)[Working draft]
  ]
]

// ---- front matter: table of contents --------------------------------------
#page(header: none, footer: none)[
  #text(font: "Avenir Next", size: 22pt, weight: 800, fill: accent)[Contents]
  #v(0.6em)
  #set text(size: 10pt)
  #show outline.entry.where(level: 1): it => {
    v(0.5em); text(font: "Avenir Next", weight: 700)[#it]
  }
  #outline(title: none, depth: 1, indent: auto)
]

#counter(page).update(1)

#include "content.typ"
