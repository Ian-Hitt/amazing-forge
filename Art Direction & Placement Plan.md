# Art Direction & Placement Plan — *Lights, Camera, Action!*

Working plan for illustrating the book. Covers the **art direction** (what it looks like),
the **placement map** (where each piece goes, keyed to the real TOC), the **priority tiers**
(what ships the book vs. what's gravy), and the **pipeline integration** (how art actually
gets into the Typst build). The SRD stays text-only by design — this plan is the *book* only.

---

## 0. DECIDED (2026-07-04): grayscale sketch interior + color cover

**Style: loose pen-and-ink sketch, like *Dungeon World* and *Monster of the Week*.** Interior
is **grayscale** (Option A below) — art authored in ink + gray, no reliance on the orange
accent, so the print interior stays on the cheap black-ink tier. The **cover** is the one color
exception. Sketch style suits this well: it reads as intentional and hand-made in pure
grayscale, and it scales from tiny spot drawings to full-page scenes without needing paint or
color. This supersedes the recommendation discussion below (kept for the cost rationale).

## 0a. Status (2026-07-04): placeholder set generated & placed

All 20 illustration slots generated via Gemini and placed in the book PDF. **House style:
clean pen-line** (loose linework, mood darkens by genre where it fits — e.g. Horror). Two
content themes, per Ian: **(1) the "making-of" layer** — the table as a movie writers'/
director's room, real people rolling dice and acting out the scenes they invent (frontispiece,
dividers, table spots); **(2) the genre layer** — the 7 genres (genre plates). Files live in
`build/art/` (gitignored). Icons (I1) done as SVG. Still to do: the F1–F7 diagrams (SVG), and
placing the S1 spots via inline markers. These are AI *placeholders* for the designer handoff.

## 0b. The cost rationale (why grayscale)

The print pipeline already produces two outputs from one source — a full-color digital PDF
and an **ink-black, B&W-priced** print interior (`print-mode` in `lib.typ` flattens every
chromatic color to black/gray). That flatten exists for a hard cost reason: on a ~300-page
6×9, a **color** POD interior runs ~$18–25/copy; a **black-ink** interior runs ~$3–4/copy.
Art is what forces that tier.

Three ways to go:

- **Option A — grayscale/line interior + color cover (RECOMMENDED).** Interior art is
  authored ink-friendly (line art, halftone, high-contrast, limited palette). Screen PDF
  still shows the orange accent; print stays on the cheap black-ink tier. This is the
  **Ironsworn model** (your stated reference — Ironsworn's interior is essentially
  monochrome) and it fits the pipeline we already built: *author every piece so it
  degrades cleanly to pure grayscale.*
- **Option B — full-color interior.** Premium/deluxe positioning only; ~5–6× the per-copy
  print cost.
- **Option C — a bound color plate signature** (8–16 glossy color pages mid-book) + B&W
  rest. Traditional, but POD support is uneven and it complicates the file.

**Everything below assumes Option A** unless you say otherwise. Concretely that means: design
in a limited palette of **ink black + accent orange (#cf4b1a) + grays**, and make sure the
piece reads with the orange removed. The build can carry `art-color.*` / `art-bw.*` variants
and swap on the `print` flag, exactly like the palette does.

---

## 1. Art direction

The book *is* "making movies at the table." Lean all the way in — cinema is the connective
tissue, not a garnish.

- **Production-craft motifs** as the through-line: clapperboard, spotlight cones, film-strip
  sprocket borders, director's chair, marquee/reel iconography. One small consistent motif
  (e.g. a film-strip rule or a spotlight) can tie every chapter opener together with *one*
  design instead of eighteen.
- **Genre = a movie genre.** Each of the 7 kits reads like a different **movie poster / lobby
  card**, tuned along the playful↔serious dial. This is the single highest-payoff art
  opportunity in the book.
- **Heroes = the cast; the antagonist = the antagonist.** Character art framed as publicity
  stills / cast photos. Remember the antagonist can be a *force* (a desert, a plague), so its
  imagery isn't always a face.
- **Tone:** cinematic and energetic, all-ages-approachable but **not** a kids' book (see
  [[game-positioning]]) — think adventure-movie one-sheet, not cartoon mascot.

---

## 2. Two kinds of "art" — and diagrams come first

For a rules-light book, the highest-ROI art is **explanatory, not decorative.** Budget and
schedule these ahead of illustration:

**A. Rules diagrams / infographics (explanatory — do these first).** These teach the
signature systems better than prose and are made in-house (SVG/Typst/Figma) so they stay in
sync with the rules:

1. **The Roll** ladder — 10+ Strong / 7–9 Weak / 6− Miss, plus **Doubles** (upgrade a Hit;
   Miss-on-doubles feeds the antagonist).
2. **Readiness** — the 0–9 health bar, Weak −1 / Miss −2, Recovery heals to 9.
3. **The Story spine** — Hero Track (progress → climax) running against the **Antagonist
   Track**; the **Devil's Bargain** loop.
4. **Antagonist Track** — Episode 5-box / Movie 9-box, odd boxes = "Bad Guys Close In,"
   last box = antagonist wins.
5. **Challenge ladder** — Normal 3 / Hard 6 / Epic 9, and how Pay the Price scales with hero
   count.
6. **Three-act / beat-sheet** structure (Part Four).
7. **Character-sheet anatomy** — Stats (pick 2 of 5), 3 Assets, Readiness, Growth.

**B. Illustration (decorative / evocative — genre plates, openers, spot art).** The mood and
sales layer. Covered in the placement map.

A small **icon system** straddles both and pays off book-wide *and* on the printable sheets:
5 stat icons (Strong/Quick/Clever/Sneaky/Charming), Readiness, Doubles, and move-type marks.
Design once, reuse everywhere.

---

## 3. Placement map (keyed to the actual TOC)

**Front matter**
- **Cover** — front now; wraparound (back + spine + front) at POD time. Lives outside this
  pipeline (layout app). *Highest sales priority, separate task.*
- **Frontispiece** — one full-page establishing illustration opposite the title page.
- Title page already has a strong text treatment; add at most a small clapperboard/spotlight
  mark.

**Part One — Your First Game** (tutorial, 8 sections) — keep it warm and human; this is the
welcome mat.
- Part divider plate.
- 1–2 spot illustrations of people *at the table* (the cast), so the tutorial feels human.
- Diagram: **the Roll** ladder (P0 — it's the first mechanic anyone meets).

**Part Two — Playing the Game** (rules, 8 chapters) — the mechanical heart → **diagrams carry
this Part.**
- Part divider.
- Diagrams P0: Roll & Doubles, Readiness, the Story spine, Antagonist Track, Challenge ladder.
- Move cards already have a card style; add per-move icons (P2).

**Part Three — Building Your World** (worldbuilding + 7 genre kits) — the showcase.
- Part divider.
- **7 genre plates** (Adventure, Mystery, Horror, Sci-Fi, Caper, Drama, Post-Apocalypse) —
  movie-poster feel, one per kit. The imagination-selling centerpiece.
- World Forge: a map/board motif; spot art in Cool Characters / Locations / NPCs.

**Part Four — Reference & Tools** (prose only in the PDF)
- Part divider.
- Beat-sheet / three-act **diagrams** (explanatory).
- Note: the 7 HTML form-sheets are excluded from the PDF and have their own web visual
  identity — art there is a separate track from this plan.

---

## 4. Priority tiers & rough counts

- **P0 — ships the book (~18 pieces + cover):** cover, frontispiece, 4 part dividers, ~6 core
  rules diagrams, 7 genre plates.
- **P1 — makes it feel finished:** chapter-opener treatment (ideally **one** repeatable motif,
  not 18 bespoke pieces), a handful of spot illustrations, the three-act/beat diagrams.
- **P2 — polish:** full icon system + marginalia, endpapers, per-move icons, decorative
  section breaks.

Sequence to build P0 first — and within P0, the **diagrams** unblock the rules Parts and can
be produced in-house immediately, independent of any illustration budget or vendor.

---

## 5. Pipeline integration (how art gets into the build)

Keep the Markdown clean — it's shared by the website *and* the SRD build, so art placement
should **not** be inline in the `.md`. Drive it from the build side:

- **Part dividers:** extend `part-divider()` in `lib.typ` to take an optional image (centered
  plate or full-bleed background). One helper change, covers all 4.
- **Chapter openers:** drive from a **manifest** (chapter-slug → image path) read by
  `build-pdf.sh`, so the H1 show rule can place a banner without touching Markdown. Cleaner
  and more portable than markers in the prose.
- **Diagrams as SVG** — crisp at any size, tiny, Typst renders them natively, and the *same
  SVG can serve the website*, so diagrams live in `docs/assets/` (shared). Illustrations
  (raster) that are print-only can live in `build/art/`.
- **Grayscale gate:** mirror the palette swap — carry `name-color.*` / `name-bw.*` variants
  and pick by the `print` flag, so no full-color raster can sneak into the black-ink interior
  and silently bump the print tier. Worth a build-time check.
- **Full-bleed** needs `bleed` on the page + images sized past the trim; that comes in with
  the POD step (bleed/crop marks are already on the roadmap in `build/README.md`).
- **The heading-break gaps are opportunistic, not targetable.** The orphan-control gaps we
  added leave *incidental* whitespace; they're a nice place for a spot piece when one happens
  to land there, but real placement should be intentional (dividers, openers, manifest), not
  "fill the gap." (Softens the earlier "that's where art goes" framing.)

---

## 6. Sourcing (your call — noted, not decided here)

- **Diagrams/icons:** in-house regardless (Typst/SVG/Figma) — they must track the rules.
- **Illustration:** commissioned (best/slow/$), AI-assisted (fast/cheap, but consistency +
  licensing caveats, and note the system doc is CC-BY), stock/asset packs, or a mix. If AI is
  in the mix anywhere, keep it clear of anything the CC-BY SRD touches.

---

## 7. Shot list

Sketch style throughout (Dungeon World / Monster of the Week). Sizes are for a 6×9 trim; text
block is ≈ 4.35 in wide × 7.35 in tall. "Full page" pieces get +0.125 in bleed added at POD.
Draw everything grayscale-safe (ink + gray, no color-dependence).

### Covers & front matter

| ID | Piece | Priority | Size | Notes |
|----|-------|----------|------|-------|
| C1 | Front cover | P0 | 6×9 full, +bleed | **Color** (the one exception). Wraparound (back+spine+front) at POD. Separate task, layout app. |
| C2 | Frontispiece | P1 | Full page | One establishing sketch scene facing the title page. Sets the tone. |
| C3 | Title-page mark | P2 | ~1.5 in | Small clapperboard/spotlight sketch; optional flourish. |

### Part dividers (4)

| ID | Piece | Priority | Size | Notes |
|----|-------|----------|------|-------|
| D1 | Part One divider | P0 | Full page | Warm "at the table" scene — this is the welcome mat. |
| D2 | Part Two divider | P0 | Full page | Rules/play energy (dice, the roll). |
| D3 | Part Three divider | P0 | Full page | Worldbuilding/genre montage. |
| D4 | Part Four divider | P0 | Full page | Reference/toolbox feel. |

### Rules diagrams (in-house SVG, sketch-flavored but legible — do these first)

| ID | Piece | Priority | Size | Notes |
|----|-------|----------|------|-------|
| F1 | The Roll ladder | P0 | 4.35 in wide × ~2.5 in | 10+ Strong / 7–9 Weak / 6− Miss + Doubles. First mechanic anyone meets. |
| F2 | Readiness track | P0 | 4.35 in × ~1.5 in | The 0–9 health bar; Weak −1 / Miss −2; heal to 9. |
| F3 | The Story spine | P0 | 4.35 in × ~3.5 in | Hero Track vs. Antagonist Track; the Devil's Bargain loop. |
| F4 | Antagonist Track | P0 | 4.35 in × ~2 in | Episode 5-box / Movie 9-box; odd = Bad Guys Close In; last = antagonist wins. |
| F5 | Challenge ladder | P0 | 4.35 in × ~2.5 in | Normal 3 / Hard 6 / Epic 9 + how Pay the Price scales with hero count. |
| F6 | Three-act / beat-sheet | P1 | 4.35 in × ~4 in | Part Four structure diagram. |
| F7 | Character-sheet anatomy | P1 | 4.35 in × ~5 in | Stats (2 of 5), 3 Assets, Readiness, Growth — labeled. |

### Genre plates (7 — the showcase)

| ID | Piece | Priority | Size | Notes |
|----|-------|----------|------|-------|
| G1 | Adventure | P0 | Half–full page (~4.35 × 5 in) | Sketch scene, tuned playful↔serious per the genre's dial. |
| G2 | Mystery | P0 | Half–full page | " |
| G3 | Horror | P0 | Half–full page | " |
| G4 | Sci-Fi | P0 | Half–full page | " |
| G5 | Caper | P0 | Half–full page | " |
| G6 | Drama | P0 | Half–full page | " (no cozy drama — keep it dramatic). |
| G7 | Post-Apocalypse | P0 | Half–full page | " |

### Chapter openers (~18 numbered chapters)

| ID | Piece | Priority | Size | Notes |
|----|-------|----------|------|-------|
| O1 | Opener spot ×~18 | P1 | ~3 in vignette or 4.35 × 1.75 in banner | One small sketch per chapter head. Cheapest path: one reusable film-strip/spotlight motif = 1 design; richest: bespoke vignette per chapter. |

### Spot illustrations (scattered, DW/MotW-style)

| ID | Piece | Priority | Size | Notes |
|----|-------|----------|------|-------|
| S1 | Key spots ×~10 | P1 | ~2.5–3.5 in | Tutorial "people playing," a hero cast still, an antagonist-as-force sketch, Recovery/Fall-back beats, etc. |
| S2 | Filler spots ×~10–15 | P2 | ~1.5–2.5 in | Small drawings to enliven text pages and land in the heading-break gaps opportunistically. |

### Icon set

| ID | Piece | Priority | Size | Notes |
|----|-------|----------|------|-------|
| I1 | Icon set (~10) | P2 | drawn ~1 in, used 0.3–0.5 in | 5 stat icons (Strong/Quick/Clever/Sneaky/Charming) + Readiness, Doubles, move-type marks. Reused book-wide **and** on the printable sheets. |

**Totals:** P0 = **18 pieces + cover** (4 dividers, 5 core diagrams, 7 genre plates, + cover).
P1 ≈ frontispiece + 2 diagrams + ~18 openers + ~10 key spots. P2 ≈ ~10–15 filler spots +
icon set + flourishes.

---

## 8. AI placeholder prompts

Placeholders to hand a designer alongside this plan: they show **intent + placement**, not
final art. Paste the **style prefix** before every subject line so the whole set reads as one
coherent look, and append the **negative prompt**. Match the aspect ratio to the slot's size.

**Style prefix (paste before every prompt):**
> *Loose black-and-white pen-and-ink sketch illustration, hand-drawn linework with light
> cross-hatching and gestural shading, high contrast, plain white background. Rough, energetic
> indie-RPG interior art in the spirit of Dungeon World and Monster of the Week. Grayscale
> only, no color. Cinematic framing, all-ages but not childish. No text, no lettering, no
> borders.*

**Negative prompt:**
> *color, photorealistic, 3D render, glossy, painterly, watermark, signature, text, letters,
> words, logos, frame, page border, cluttered background, anime, chibi, cutesy cartoon.*

**Aspect ratios by slot:** full page → **2:3** · genre plate → **2:3 or 4:5** · banner →
**5:2** (wide) · vignette/spot → **1:1 or 4:5** · icon → **1:1**.

### Diagrams (F1–F7) — note

Do **not** AI-generate these — an image model will get the mechanics wrong and the whole point
is accuracy. For the handoff, drop a **rough hand-sketched mockup** (even phone-photo of a
napkin sketch) into the slot so the designer sees the intended layout; final versions are
built in-house as SVG. The subject of each is already specified in §7's diagram table.

### Illustration prompts (subject lines)

| ID | Piece | Prompt (append style prefix + negative) |
|----|-------|------------------------------------------|
| C1 | Cover | *(Color, designer-led — separate task.)* An ensemble of adventurers striking a dynamic hero pose as a film spotlight and clapperboard frame the scene; energetic, poster-like. |
| C2 | Frontispiece | A film clapperboard snapping shut, and out of the opening burst a dragon, a spaceship, a detective, and a wanderer — imagination spilling out of the movies. Full-page, tone-setting. |
| C3 | Title mark | A single small clapperboard with a spotlight glow. Simple icon. |
| D1 | Part One divider | Friends around a tabletop mid-game, dice rolling, and imaginative shapes (a dragon, a rocket) rising like smoke from the table. Warm, welcoming. |
| D2 | Part Two divider | Two oversized six-sided dice tumbling through the air with motion lines, dramatic and kinetic. |
| D3 | Part Three divider | An open book or unrolled map from which genre scenes swirl outward — a castle, a ray-gun, a haunted house, a ruined city. A montage of possibility. |
| D4 | Part Four divider | A director's desk / open toolbox: scattered dice, character sheets, a pencil, a spotlight, index cards. Reference-and-tools feel. |
| G1 | Adventure | Heroes crossing a fraying rope bridge over a deep chasm toward a ruined jungle temple, a glint of treasure ahead. Sweeping, pulpy. |
| G2 | Mystery | A detective bent over a clue-strewn desk with a magnifying glass, rain streaking a window, long noir shadows. |
| G3 | Horror | A lone figure with a flashlight in a doorway; a huge shadow or half-seen creature looms beyond. Dread, negative space. |
| G4 | Sci-Fi | Space explorers in suits dwarfed before a towering alien monolith under a field of stars. Awe and scale. |
| G5 | Caper | A crew mid-heist rappelling toward a vault past a laser grid, sly confident grins, stylish and slick. |
| G6 | Drama | A charged face-to-face confrontation between two characters under a single theatrical spotlight, high emotion. (Not cozy.) |
| G7 | Post-Apocalypse | A lone wanderer in makeshift gear on a ridge, overlooking a ruined, overgrown city skyline at dusk. |
| O1 | Chapter-opener motif | A horizontal strip of film with a few tiny scene frames inside it, a spotlight glow at one end. Reusable banner. (5:2) |
| S1a | Spot — at the table | Two or three players laughing around dice and snacks, a hand mid-roll. |
| S1b | Spot — cast still | A single confident hero character portrait, half-length, publicity-still framing. |
| S1c | Spot — antagonist as force | A menacing dust storm or roiling plague cloud with a face barely suggested in it. |
| S1d | Spot — Recovery Scene | Weary heroes regrouping around a small campfire, catching their breath. |
| S1e | Spot — Fall back | Characters in a dynamic dramatic retreat, glancing back over a shoulder. |
| S1f | Spot — the Roll | A hand releasing two dice in mid-air, motion lines, tension. |
| S2 | Filler spots | Small standalone objects, one per image: a d6, a clapperboard, a spotlight, a film reel, a torch, a rolled map, an old key, a compass. (1:1 each) |
| I1 | Icon set | Simple single-subject icons, 1:1: a flexed arm (Strong), running legs or a lightning bolt (Quick), a lightbulb or gears (Clever), a mask or footprints (Sneaky), a speech swirl or star (Charming), a heart-shaped bar (Readiness), two matching dice (Doubles), a clapperboard (moves). |

---

## 9. How placement works in the build (drop-in art)

Every art position is a **slot** identified by the IDs in §7. The book build
(`build/build-pdf.sh`) places each slot automatically:

- **No image yet →** a labeled dashed **placeholder box** is drawn at the exact position
  and size (e.g. "ART · D1 — Part One divider illustration"). The book always compiles, so
  the placement is visible even before any art exists.
- **Image present →** the box is replaced by the image on the next rebuild. **No code
  change** — just drop the file in and re-run `./build/build-pdf.sh`.

**To drop in art:** save the file as `build/art/<ID>.<ext>` (`png`, `jpg`, `svg`, or `webp`),
using the slot ID as the filename — `D1.png`, `C2.png`, `G3.png`, `O1.png`, …. Rebuild.

**Fixed slots** (one obvious anchor each) are placed automatically: **C2** frontispiece,
**D1–D4** part dividers, **G1–G7** genre plates (after each genre's heading), **O1** the one
reusable chapter-opener motif (same image on every chapter head).

**Inline slots** — spots and diagrams that live mid-prose — are placed with a marker you drop
in the Markdown wherever the art goes:

```
<!--art:ID|caption|height-->
```

Put it on its own line. It's an HTML comment, so it's **invisible on the website and in the
SRD** — only the book PDF build turns it into a slot. `caption` and `height` are optional
(default: the ID, and 2.4in). Examples:

```
<!--art:F1|The Roll ladder — 10+ / 7–9 / 6−|2.6in-->      diagram slot in the Roll chapter
<!--art:S1d|Recovery Scene — heroes at a campfire|2.5in-->  spot slot beside the rule
<!--art:S2-1|a single six-sided die|1.4in-->                filler spot
```

Same drop-in rule: no file yet → labeled placeholder box; save `build/art/<ID>.<ext>` → image
on rebuild. Use any IDs you like for filler (`S2-1`, `S2-2`, …).

`build/art/` is gitignored — placeholder AI art stays local, off the public repo. Still
hand-placed only: the **icons I1** (tiny, inline, reused — better set by the designer than
boxed in text) and the color cover **C1** (layout-app / designer territory).

---

## Open decisions to confirm

1. **Color vs. B&W-priced interior** (§0) — gates the whole art medium. Recommendation: A.
2. **Chapter openers:** one repeatable motif, or bespoke per chapter?
3. **Where shared art lives:** `docs/assets/` (web+print) vs. `build/art/` (print-only).
4. **Sourcing path** for illustration.
