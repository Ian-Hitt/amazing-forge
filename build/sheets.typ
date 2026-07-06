// Lights, Camera, Action! — blank play sheets, rebuilt natively for the print
// PDF. The website versions (docs/part-four/*-sheet.md) are hand-built HTML/CSS
// for browser printing and can't flow through the Markdown→Typst pipeline, so
// these are faithful Typst re-creations. Included by book.typ as back matter,
// after the main content. One sheet per page (photocopy-friendly): no running
// head, no page number. Colors come from lib.typ, so they go ink-black in the
// print (B&W-priced) build automatically.

#import "lib.typ": *

#let linecol = if print-mode { rgb("#9a9a9a") } else { rgb("#b9b3aa") }

// --- primitives -------------------------------------------------------------
// a single track/checkbox square, optionally highlighted (accent)
#let sqbox(body, size: 15pt, hi: false) = box(
  width: size, height: size, radius: 3pt,
  stroke: (thickness: if hi { 2.4pt } else { 1.6pt }, paint: if hi { accent } else { ink }),
)[#align(center + horizon)[#text(font: sans, size: 7.5pt, weight: 700, fill: if hi { accent } else { ink })[#body]]]

// a horizontal row of squares; `hi` = set of indices to highlight
#let track(labels, size: 15pt, gap: 3.5pt, hi: ()) = stack(dir: ltr, spacing: gap,
  ..labels.enumerate().map(p => sqbox(p.at(1), size: size, hi: hi.contains(p.at(0)))))

// small write-on checkbox
#let chk = box(width: 11pt, height: 11pt, radius: 2pt, stroke: 1.5pt + ink)

// a blank write-in line that fills the available width
#let fline(h: 1.35em) = box(width: 100%, height: h, stroke: (bottom: 0.9pt + linecol))

// section header:  LABEL ─────────────────────
#let ssec(title) = block(above: 0.85em, below: 0.4em)[
  #grid(columns: (auto, 1fr), gutter: 0.55em, align: horizon,
    text(font: sans, size: 9.5pt, weight: 800, tracking: 0.08em)[#upper(title)],
    line(length: 100%, stroke: 1.3pt + ink))
]

#let shint(body) = block(above: 0.1em, below: 0.4em)[#text(font: serif, size: 8.5pt, fill: soft)[#body]]

#let sref(body) = block(above: 0.85em, below: 0pt)[
  #line(length: 100%, stroke: 1.6pt + ink)
  #v(0.35em)
  #text(font: serif, size: 8pt, fill: soft)[#body]
]

#let notesbox(h: 3em) = box(width: 100%, height: h, radius: 6pt, stroke: 1.4pt + ink)

// full-page sheet frame: masthead + rule, then the body. The set-rules reset
// book.typ's airy body metrics (leading 0.72em / paragraph spacing 0.9em) to
// tight sheet defaults — otherwise the inherited spacing inflates a sheet onto
// a second page.
#let sheet(sub, body) = page(header: none, footer: none, margin: (x: 0.7in, top: 0.65in, bottom: 0.6in))[
  #set text(font: serif, size: 10pt, fill: ink)
  #set par(justify: false, leading: 0.5em, spacing: 0.5em, first-line-indent: 0pt)
  #block(above: 0pt, below: 0.7em)[
    #text(font: sans, size: 15pt, weight: 800, tracking: 0.04em)[#upper[Lights, Camera, Action!]]
    #v(0.14em)
    #text(font: sans, size: 8.5pt, weight: 700, fill: accent, tracking: 0.16em)[#upper(sub)]
    #v(0.25em)
    #line(length: 100%, stroke: 1.8pt + ink)
  ]
  #body
]

// ===========================================================================
// back-matter divider
// ===========================================================================
#page(header: none, footer: none)[
  #set par(justify: false, leading: 0.65em, spacing: 0.5em, first-line-indent: 0pt)
  #v(1.2in)
  #align(center)[
    #text(font: sans, size: 12pt, weight: 600, fill: soft, tracking: 0.3em)[#upper[Reference]]
    #v(0.5em)
    #line(length: 1.4in, stroke: 1.5pt + accent)
    #v(0.6em)
    #text(font: sans, size: 30pt, weight: 800, fill: accent)[Blank Sheets]
    #v(0.7em)
    #block(width: 3.9in)[
      #set par(justify: false, leading: 0.65em)
      #text(font: serif, size: 10.5pt, fill: soft)[
        Photocopy or reprint these freely for your table — one Hero Sheet per
        player, a Story Arc Tracker per Story, and the rest as you need them.
        Clean, always-current copies are also on the website.
      ]
    ]
  ]
]

// ===========================================================================
// 1 · HERO SHEET
// ===========================================================================
#sheet("Hero Sheet")[
  #grid(columns: (auto, 1fr, auto, 1fr), gutter: 0.5em, align: bottom,
    text(font: sans, size: 8pt, weight: 700)[#upper[Hero Name]], fline(),
    text(font: sans, size: 8pt, weight: 700)[#upper[Player]], fline())

  #ssec("Concept")
  #fline()
  #shint[Your one-line movie-poster pitch.]

  #ssec("Stats")
  #shint[Circle *two.* You get *+1* when the moment calls for one of them.]
  #stack(dir: ltr, spacing: 7pt,
    ..("Strong", "Quick", "Clever", "Sneaky", "Charming").map(s =>
      box(inset: (x: 10pt, y: 3.5pt), radius: 20pt, stroke: 2pt + ink)[
        #text(font: sans, size: 9pt, weight: 700)[#s]]))

  #ssec("Assets")
  #shint[Three things your hero is great at. Jot any *Boons* on the lines under each; check *Broken* if one gets knocked out.]
  #let asset-card(cap) = block(width: 100%, radius: 6pt, stroke: 1.3pt + ink, inset: 7pt,
    above: 0.45em, below: 0.45em, breakable: false)[
    #text(font: sans, size: 7pt, weight: 700, fill: soft, tracking: 0.05em)[#upper(cap)]
    #v(0.3em)
    #fline(h: 1.3em)
    #v(0.35em)
    #grid(columns: (auto, 1fr), gutter: 0.4em, align: horizon, rows: 1.15em,
      sqbox([], size: 12pt), fline(h: 1.05em))
    #v(0.25em)
    #grid(columns: (auto, auto), gutter: 0.45em, align: horizon,
      sqbox([], size: 11pt), text(font: sans, size: 7pt, weight: 700, fill: soft)[#upper[Broken]])
  ]
  #asset-card("1 · Skill or expertise")
  #asset-card("2 · Item, companion, or connection")
  #asset-card("3 · Their other side")

  #ssec("Readiness")
  #shint[Start at 9 (your max). Cross off as it drops; refill when you regroup.]
  #track(range(0, 10).map(i => [#i]), size: 15pt, hi: (9,))

  #ssec("Growth Track")
  #shint[Fill one box per Growth earned. Spend *2* on a Boon or *5* on a new Asset.]
  #track(range(18).map(_ => []), size: 13pt, gap: 3pt)

  #ssec("Story Arc Notes")
  #notesbox(h: 3.2em)
]

// ===========================================================================
// 2 · STORY ARC TRACKER
// ===========================================================================
#sheet("Story Arc Tracker")[
  #ssec("The Goal")
  #fline()
  #shint[The single, clear victory condition, in one sentence ("Recover the stolen Sun Crystal").]

  #ssec("Size")
  #stack(dir: ttb, spacing: 0.45em,
    box[#chk #h(4pt) #text(font: serif, size: 9pt)[*Episode* — 3 Milestones / 5-box antagonist (one sitting)]],
    box[#chk #h(4pt) #text(font: serif, size: 9pt)[*Movie* — 6 Milestones / 9-box antagonist (2–3 sessions)]])

  #ssec("The Tracks")
  #grid(columns: (auto, 1fr), gutter: 0.5em, rows: (auto, auto), align: horizon + left,
    text(font: sans, size: 7.8pt, weight: 800)[#upper[Hero]],
    track(range(1, 7).map(i => [#i]), size: 15pt),
    text(font: sans, size: 7.8pt, weight: 800)[#upper[Antag.]],
    track(("▲", "2", "▲", "4", "▲", "6", "▲", "8", "▲").map(s => [#s]), size: 15pt))
  #shint[Cross out the boxes you don't use — Episode is 3 hero / 5 antagonist boxes, Movie is 6 / 9. The antagonist's *▲ boxes are Closing In beats;* its last box is the antagonist's win.]

  #ssec("The Antagonist")
  #grid(columns: (auto, 1fr), gutter: 0.5em, align: bottom, row-gutter: 0.5em,
    text(font: sans, size: 8pt, weight: 700)[#upper[Who / what]], fline(),
    text(font: sans, size: 8pt, weight: 700)[#upper[What it wants]], fline())
  #shint[Give it a face — a person, a faction, or even a force (a desert, a plague, a deadline).]

  #ssec("Milestones")
  #shint[A concrete, pointable step toward the Goal. Number them to match the Hero Track boxes (Episode 1–3; Movie 1–6).]
  #let ms(n) = grid(columns: (auto, auto, 1fr), gutter: 0.45em, align: bottom,
    chk, text(font: sans, size: 9pt, weight: 800)[#n.], fline(h: 1.25em))
  #grid(columns: (1fr, 1fr), gutter: 1.2em, row-gutter: 0.55em,
    ms(1), ms(4), ms(2), ms(5), ms(3), ms(6))

  #ssec("Notes")
  #notesbox(h: 3em)
]

// ===========================================================================
// 3 · CHALLENGE TRACKER
// ===========================================================================
#sheet("Challenge Tracker")[
  #block(width: 100%, fill: table-fill, radius: 6pt, stroke: 1.6pt + ink, inset: 9pt, breakable: false, below: 0.6em)[
    #set text(font: serif, size: 8pt)
    #set par(leading: 0.5em, spacing: 0.55em, first-line-indent: 0pt, justify: false)
    #let lbl(b) = text(font: sans, size: 7.5pt, weight: 800)[#upper(b)]
    #lbl[Start a Challenge:] name the goal, pick a difficulty & draw the track, then *each player* rolls a *d6* → *5–6* +1 · *3–4* 0 · *1–2* −1 — a one-time nudge to _their_ first roll.

    #lbl[Each roll:] *Strong* fill 1 box · *Weak* fill 1 box, −1 Readiness · *Miss* no box, −2 Readiness _or_ take the *Devil's Bargain* (upgrade to a Strong Hit, refuse the loss → antagonist +1 box; not if it would knock you Out of Action). A *Strong Hit on doubles* is an Outstanding Success — fill *2 boxes* and take +1 to your next roll; a *Miss on doubles* advances the antagonist. _(4–5 heroes: Weak −2, Miss −3.)_

    #lbl[Size] (the same at any number of heroes): Normal = *3* · Hard = *6* · Epic = *9* (peak moments only) boxes — cross out the ones you don't use; anything shorter, don't draw a track. Track fills → Challenge won. A Challenge is _not_ a Milestone. Fall back = a Recovery Scene (lose its progress; the party heals up).

    #lbl[Types:] Combat · Journey · Stealth · Investigation · Social — same boxes-and-rolls, only the fiction changes.
  ]

  #let chal(n) = block(width: 100%, radius: 6pt, stroke: 1.4pt + ink, inset: 7pt, above: 0.5em, below: 0.5em, breakable: false)[
    #grid(columns: (auto, auto, 1fr, auto), gutter: 0.5em, align: horizon,
      text(font: sans, size: 10pt, weight: 800, fill: accent)[#n.],
      text(font: sans, size: 8pt, weight: 700)[#upper[Challenge]],
      fline(h: 1.25em),
      box[#text(font: sans, size: 7pt, weight: 700)[#upper[Size]] #h(4pt) #chk #h(2pt) #text(font: sans, size: 7.5pt, weight: 700)[Normal] #h(5pt) #chk #h(2pt) #text(font: sans, size: 7.5pt, weight: 700)[Hard] #h(5pt) #chk #h(2pt) #text(font: sans, size: 7.5pt, weight: 700)[Epic]])
    #v(0.45em)
    #grid(columns: (auto, auto, 1fr), gutter: 0.6em, align: horizon,
      stack(dir: ltr, spacing: 3.5pt,
        ..range(1, 9).map(i => sqbox([#i], size: 14pt)),
        sqbox([★], size: 14pt, hi: true)),
      text(font: sans, size: 7.5pt, weight: 700)[#upper[A box =]],
      fline(h: 1.2em))
  ]
  #for n in range(1, 7) { chal(n) }
]

// ===========================================================================
// 4 · WORLDBUILDING WORKSHEET
// ===========================================================================
#sheet("Worldbuilding Worksheet")[
  #let q(n, name, ask, hint, lines: 1) = block(above: 0.38em, below: 0.38em, breakable: false)[
    #grid(columns: (1.4em, 1fr), gutter: 0.4em, align: (right + top, left + top),
      text(font: sans, size: 9pt, weight: 800, fill: accent)[#n.],
      [
        #text(font: sans, size: 9pt, weight: 800)[#upper(name)] #h(0.3em) #text(font: serif, size: 9pt, fill: soft)[— #ask]
        #v(0.12em)
        #text(font: serif, size: 7.8pt, fill: soft)[#hint]
      ])
    #v(0.22em)
    #for _ in range(lines) [ #fline(h: 1.25em) #v(0.18em) ]
  ]
  #q(1, "The Genre", "What's the mood of our story?", [A feeling, not a setting. "Spooky — but the fun kind." What movie or show should this feel like?])
  #q(2, "The Setting", "Where and when does it happen?", [One strong image with a twist. Not "a medieval kingdom" but one built inside a sunless canyon.])
  #q(3, "The Denizens", "Who lives here?", [Two or three kinds, with a hint of how they relate. This is also what your heroes can be.])
  #q(4, "Magic", "How does it work, if at all?", [How common, and what it costs. "None at all" is a great answer. Sets what an Asset can be.])
  #q(5, "Technology", "What level are we at?", [Pick a level and add texture. "Laser blasters, but the ships run on duct tape and prayer."])
  #q(6, "The Leadership", "Who's in charge?", [Name who, and hint how secure. A cracked power structure plays better than a stable one.])
  #q(7, "The Enforcement", "How do they stay in charge?", [The muscle behind the power — often the heroes' most frequent opposition. It becomes Challenges, not stat blocks.])
  #q(8, "The Threats", "The two or three biggest dangers right now?", [Different scales and kinds — a creeping one, a sharp one, a hidden one. Make at least one concrete enough to tick a track.], lines: 2)
  #q(9, "The Forbidden", "One place, object, or action that's off-limits?", [Specific and tempting. "Nobody is allowed below the cloud line." A Story Arc waiting to happen.])
  #q(10, "The Reputation", "When people see a group like yours, what do they think?", [An outside opinion with an edge. "Reckless kids who don't know their place."])
  #sref[*When you're done:* read the ten answers back in order — a Story Arc usually forms in the overlap between the Threats, the Forbidden, and your Reputation. Stuck? Take the first decent answer, or just say "we'll find out."]
]

// ===========================================================================
// 5 · CAST SHEET
// ===========================================================================
#let logsheet(sub, hint, cols, heads, ref: none, rows: 18) = sheet(sub)[
  #shint[#hint]
  #table(
    columns: cols,
    stroke: 0.5pt + linecol,
    inset: (x: 6pt, y: 7pt),
    align: left + top,
    fill: (x, y) => if y == 0 { table-fill },
    rows: (auto,) + (1.55em,) * rows,
    ..heads.map(h => table.cell[#text(font: sans, size: 7.5pt, weight: 800, tracking: 0.05em)[#upper(h)]]),
    ..range(rows * cols.len()).map(_ => []))
  #if ref != none { sref[#ref] }
]

#logsheet(
  "Cast — People We've Met",
  [Name them, say what they do for the story, give them one unforgettable detail, and note how you left things. A ★ marks the ones who matter.],
  (1.4fr, 1fr, 1.7fr, 1.2fr),
  ("Name & ★", "Role", "The one detail", "Last seen"),
  ref: [*Roles:* Helper · Obstacle · Source · Petitioner · Innocent · Rival · Wildcard · Authority · Connector · Hidden Hand.],
  rows: 17,
)

// ===========================================================================
// 6 · PLACES SHEET
// ===========================================================================
#logsheet(
  "Places — Where We've Been",
  [Name it, say what it's _for_, give it one striking detail, and note the hook that's still open. Check *Back?* for places worth a return trip.],
  (1.3fr, 1.2fr, 1.9fr, 0.7fr),
  ("Name", "Function", "Detail & hook", "Back?"),
  rows: 18,
)
