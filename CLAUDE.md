# Lights, Camera, Action! — Project Guide

We're writing a **TTRPG rulebook**. *Lights, Camera, Action!* (working title) is a fast, cinematic,
zero-prep tabletop RPG **for people who want to tell fast-paced cinematic stories** — NOT a kids'
game. Its rules sit, in *complexity*, between **Amazing Tales** (simple, very young) and
**Ironsworn: Starforged** (crunchy, adult) — light enough that a group of 10+ kids could self-run
it, but that's an accessibility claim, **not** a target audience. Approachable and story-first, with
just enough decisive mechanics to keep play flowing. Plays **Guided** (with a Guide) or **Co-op**
(no Guide, solo or group). See memory [[game-positioning]].

## Sources of truth — read these first

Two documents together define the book. **Always consult both before writing any content.**

**`Core Mechanics - Master Reference.md`** is the canonical spec for all core mechanics.
It is a *reference for writing the book*, not a chapter of the book itself.

- Its **Standard Vocabulary** table is the authoritative word list — match those exact terms
  and capitalization in everything, and flag deviations.
- Its **flags** show status: `✅ DECIDED` (canonical), `🚧 OPEN` (undecided — don't fill in),
  `⚠️ NOTE` (context).
- The **Appendix** lists every decision and what's still open.

**`Book Outline.md`** is the canonical spec for the book's structure and flow. It defines
every chapter, what belongs in it, and why. Use it to determine:

- Where a given mechanic or topic lives in the book.
- Whether content belongs in Part One (first-game, minimal) or Part Two (full reference).
- What `💡 Idea` sections are brainstormed but not yet approved — don't write these until Ian confirms them.
- What is `🚧 OPEN` and must not be written yet (e.g., character advancement).

When writing a chapter, the Outline defines the *scope and purpose*; the Master Reference
defines the *rules and vocabulary*. Neither overrides the other — they cover different things.

**`Math & Simulation Reference.md`** is the source of truth for the **balance math** — dice
probabilities, the settled numeric rules, the structural assumptions used for modeling, and
simulation results. Consult/update it for any balance or tuning question so parameters never
have to be re-guessed. The canonical model is **§0 (the spine model)**, validated by
`sim_spine.py`; older `sim_*.py` scripts back the superseded sections.

Source drafts (Gemini, in `/uploads` when present): **V5 is the most recent and
authoritative**; V3/V4 are older and superseded where they differ.

## Settled conventions (quick reference — details in the master doc)

> ⚠️ **2026-06-22 REWORK (see [[dice-and-scaling-rework]]) — decision locked, not yet propagated to
> chapters/printables.** Core roll is now **+0/+1/+2** (pick **2 of 5 stats** = honest +1, **3 Assets** =
> argued +1); the single broad **Attribute is retired**; the **recovery ratchet is dropped** (Recovery
> Scene heals fully to 9); **Movie = 6/4-box** (duo Movie = 5); the **"+1 box for 4+" ladder rule is
> dropped**. The bullets below still describe the OLD rules where noted — trust the rework + Math&Sim §0.

- **Terms:** Guide (never "GM"), Co-op play (never "GMless"), Readiness (never HP/health),
  Assets, **Stats** (pick **2 of the closed five**: Strong/Quick/Clever/Sneaky/Charming — the
  most-relevant one is chosen objectively, not argued), Story / Story Arc (never "Quest"; never bare "Arc"), Story Arc Track (never "Hero
  Track"/"Quest Track"), **Episode/Movie** (the two *individual* story sizes), **Season/Series**
  (prose *collection* patterns, not sizes — see [[spine-model]]), Antagonist Track, **Showdown**
  (the climax/reserved top box), Milestone, Scene, Challenge, Pay the Price, **Recovery Scene**
  (the fall-back-and-regroup move; "Surge" = the villain advance it triggers), **Fall back**
  (retreat from a Challenge — was "Flee"), Quit the Story Arc, **Thread/B-plot** (lose-clock-free
  subplot), Downtime (between-Stories reset), Ask the Oracle, Growth/Growth Track/Boon/Trade In
  (advancement — use "Growth," never "XP"). Avoid "damage."
- **Core roll (DECIDED 2026-06-22):** 2d6 + a **+0/+1/+2** modifier. You get **+1** if the action's
  **most-relevant stat** is one of your **2 of 5** (Strong/Quick/Clever/Sneaky/Charming — chosen
  *objectively*, not argued: a chase is Quick, period); **+1** if any of your **3 specific Assets**
  applies (these *are* argued — story flexibility); **+2** if both, **+0** if neither (the risk-of-
  failure floor). 10+ Strong, 7–9 Weak, 6− Miss; doubles upgrade a tier (Oracle's Blessing). A Hit =
  **narrate the change**. Tuned to stat≈0.55 / asset≈0.85 apply rates → avg mod ≈ 1.40 (was 1.85);
  this **retires the single broad Attribute** (the closed-five *list* survives; you pick two of it).
- **Readiness:** starts **9**. Weak −1, Miss −2 (always — no dodging). **No ratchet (DECIDED
  2026-06-22):** a **Recovery Scene heals the party fully back to 9** every time; max Readiness no
  longer declines (the old declining ceiling was too harsh and broke Movie scaling). **Mend** (small
  risky any-scene patch, no cap — Strong +3 / Weak +2 / **Miss −1**, self or ally, capped at 9, **no
  Surge**, can't revive Out of Action; a tactical patch-vs-push choice). **Recovery Scene** (fall
  back & regroup → party **back to 9**, reliable, **+1 villain Surge** — the only villain-advance
  trigger). Out of Action at 0 **forces a Recovery Scene** whose surge can lose the Story Arc.
  **Heroes can't die** — Readiness is *ammunition against the villain clock,* not a survival meter.
  (Fresh-party loss ~6% Episode / ~16% Movie at all-Medium; Boons settle Movies toward ~10% — Math &
  Sim §0.)
- **Story structure — single nested SPINE (DECIDED 2026-06-13; see [[spine-model]] & Math & Sim
  §0).** Dropped sandbox play. One Story = one spine with a **Story Arc Track** (progress, 1
  box/Milestone → the **Showdown**) and a short **Antagonist Track** whose **top box is the reserved
  climax.** **Two individual sizes (the only ones with machinery): Episode = 3 Milestones / 2-box
  track; Movie = 6 Milestones / 4-box track (duo Movie = 5-box).** **Season/Series are prose collection patterns, not
  sizes** (Episode/Movie are individual stories; a Season strings them on a throughline, a Series is
  a run of Seasons). **B-plots are threads** — light progress track, **no Antagonist Track/lose-clock**,
  resolve into the spine's climax. **Nesting is back** (a Season is *made of* Stories).
- **Antagonist Track — surges on the Recovery Scene.** Short, with the **top box reserved as the
  climax.** Lower boxes fill **only when the heroes fall back to regroup** (a Recovery Scene) —
  emergent, player-chosen, never scheduled, never per-roll automatic. The regroup is the quiet/B-plot
  beat, so **character scenes are where the villain gains ground.** **Out of Action forces a Surge
  that can fill the climax box → lose before the Showdown** (the loss vector). The antagonist may be
  a **force** (a desert, a plague) — characterize it so a Surge is concrete. **Quit the Story Arc** =
  terminal give-up; a lost Story seeds a new one. (Balance/validation: `Math & Simulation Reference.md`
  §0, `sim_spine.py`.)

## Advancement (DECIDED 2026-06-08; Growth rule revised 2026-06-12)

- **Character advancement** is settled. **Horizontal growth:** heroes gain tools/signature
  moves, **never bigger numbers**, so the +2/+1 curve and max-9 Readiness are untouched and
  **enemy tracks never rescale**. Per-hero **Growth Track**: **every 3rd Milestone the party
  marks (on any Story Arc), each hero earns 1 Growth** — cumulative, never resets per arc, all
  heroes tick together. Ties Growth to **headway actually played, not arcs finished** (~1 per
  session): a standalone Movie/Season can't be starved, and a stretched arc can't be gamed.
  (Replaced the old "1 per Quest completed.") Spend **2 Growth** on a **Boon** or **5 Growth** on
  a **New Asset** (ceiling **6**; **Trade In** one to exceed). Growth rate is a pure feel knob —
  Boons are horizontal, so it never rescales the curve. Use **Growth**, never "XP." See
  master-doc §4 Step 4 + Ch.13.
- **Boons are built, not picked (build-a-Boon, Ch.13):** a Boon = **Trigger** (when you may use it —
  open/flavorful, genres supply d10 tables) + **Effect** (what it does — a *closed* fixed list, the
  only dice-touching part; genres never add Effects). **Cadence is derived:** Strong effect (Upgrade
  / +1-to-roll / Take the Price) = once/Session, Mild (Reroll / +1-to-your-next-roll / Lend-a-reroll / Free
  Oracle / Steady-Hands-Mend) = once/Scene; **lock the Trigger to a situation → one step more often**.
  Never a *permanent* modifier (banked +1 = a temporary one-roll bonus, §4c-safe); excluded effects =
  extra track progress, preventing Out of Action. Max 2 Boons/Asset. Named **recipes** (Signature
  Move, In My Element, Dig Deep, Reliable, Lend a Hand, Mender, Scout, Take the Hit) are pre-built
  combos. Genre d10 trigger tables: **all 7 kits done.**

## Working notes

- **Book chapters live in `docs/`** (`docs/part-one/`, `docs/part-two/`, `docs/part-three/`) —
  these are the published deliverables. Edit chapters there, using clean-slug filenames
  (e.g. `01-build-your-world.md`). New chapters must also be added to `nav:` in `mkdocs.yml`.
- **Book structure (4 Parts):** **Part One — Your First Game** (tutorial, intentionally short);
  **Part Two — Playing the Game, In Depth** (everything about *playing* — the dice/track rules
  *plus* the Ask the Oracle move, Co-op/Guide play, Running the Game, and Growing Your Heroes);
  **Part Three — Building Your World** (a *self-contained* Part for worldbuilding only: the World
  Forge with its 10 questions, Starter Backdrops, running it, and the d6 idea tables);
  **Part Four — Reference & Tools** (lookups, blank sheets, play-side generators — not yet built).
  Key principle: **building the world is a separate experience from playing the game** — so the
  Oracle/Running/Co-op material is Part Two (it's *play*), and only worldbuilding is Part Three.
  Chapter numbers are now final: 7–10 rules, 11 Ask the Oracle, 12 Running the Game, 13 Growing
  Your Heroes, 14 Worldbuilding — all Part One through Part Three chapters now written.
- **Reference/design files stay in the repo root** (this file, the Master Reference, Book
  Outline, Math & Simulation, `sim_*.py`). As of 2026-06-22 they are **tracked and pushed to
  the public repo** (backed up there) — *not* gitignored anymore. The plan is to make the repo
  **private before the book goes on sale** (and publish a free SRD/PDF instead); only `.claude/`
  stays local.
- **Publishing:** the book is a MkDocs Material site on GitHub Pages —
  https://ian-hitt.github.io/amazing-forge/ (repo `Ian-Hitt/amazing-forge`, public).
  **Sync = push:** committing to `main` auto-builds (`mkdocs build --strict`) and deploys in
  ~1 min. `--strict` fails the build on broken links or a chapter missing from `nav:`.
  See memory [[hosting-and-publishing]].
- Persisted decisions and gotchas live in memory (`MEMORY.md` index); they carry across
  sessions — trust but verify against the master doc.
- Style: Ian prefers concise, direct responses.
