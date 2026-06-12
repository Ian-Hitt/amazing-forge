// Lights, Camera, Action! — shared definitions (colors, states, helpers).
// Imported by BOTH book.typ and the generated content.typ so that
// part-divider() resolves inside the included content.

// ---- palette ---------------------------------------------------------------
// Two outputs from one source. Color (digital):  ./build/build-pdf.sh
// Print interior (B&W-priced):                    ./build/build-pdf.sh print
// Print mode makes every chromatic color ink-black / neutral gray, so a POD
// printer classifies the interior as black-ink (the cheap tier), not color.
#let print-mode = sys.inputs.at("mode", default: "color") == "print"

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

// running-head state: current Part and Chapter
#let cur-part = state("cur-part", none)
#let cur-chap = state("cur-chap", none)

// full-page part divider
#let part-divider(kicker, title) = {
  cur-part.update(kicker)
  cur-chap.update(none)
  pagebreak(weak: true)        // digital build: no odd-page forcing (avoids blank versos)
  set page(header: none, footer: none)
  v(2.6in)
  align(center)[
    #text(font: "Avenir Next", size: 12pt, weight: 600, fill: soft, tracking: 0.3em)[#upper(kicker)]
    #v(0.5em)
    #line(length: 1.4in, stroke: 1.5pt + accent)
    #v(0.6em)
    #text(font: "Avenir Next", size: 30pt, weight: 800, fill: accent)[#title]
  ]
  pagebreak(weak: true)
}
