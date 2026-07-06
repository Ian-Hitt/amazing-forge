# Lights, Camera, Action! — Project Guide

We're writing a **TTRPG rulebook**. *Lights, Camera, Action!* is a fast, cinematic,
zero-prep tabletop RPG **for people who want to tell fast-paced cinematic stories** — NOT a kids'
game. Its rules sit, in *complexity*, between **Amazing Tales** (simple, very young) and
**Ironsworn: Starforged** (crunchy, adult) — light enough that a group of 10+ kids could self-run
it, but that's an accessibility claim, **not** a target audience. Approachable and story-first, with
just enough decisive mechanics to keep play flowing. Plays **Guided** (with a Guide) or **Co-op**
(no Guide, group only — solo dropped). **2–6 players** (up to 6 = 5 characters + a Guide; 5–6 →
recommend one Guide). See memory [[game-positioning]] and [[player-count-model]].

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

> ⚠️ **2026-06-25 ANTAGONIST REWORK (the Devil's Bargain spine) — DECIDED and PROPAGATED through the
> whole book (Ch.7–12, all 7 kits, Part Four) + the Master Reference + Math&Sim §0.** Recovery is now
> **free** (no Surge); the Antagonist Track advances via the **Devil's Bargain** (on a Miss: forgo the
> damage + upgrade to Strong, antagonist +1; not on a knockout roll), a **Miss on doubles**, and **Out of
> Action.** Doubles now upgrade only a **Hit**; a doubles-Miss feeds the antagonist (the old Miss→Weak
> upgrade is gone). **Antagonist Track: Episode 5 / Movie 9, odd boxes are the antagonist "Closing In"** (the term
> "Surge" is retired), last box = antagonist wins; **same at any party size** (duo special case dropped).
> Validated by `sim_devils.py`/`sim_devils2.py`; see [[miss-doubles-clock-proposal]].
>
> ⚠️ **2026-06-27 CHALLENGE LADDER + PLAYER COUNT — DECIDED and PROPAGATED (Master Reference, SRD, Ch.8/9/12,
> Part One 00/05/07, all 7 kits, sheets, the Play Online app, Book Outline, Math&Sim §0).** **Drop Easy; three
> tiers — Normal 3 / Hard 6 / Epic 9 boxes, the SAME at any number of heroes** (nothing shorter than a Normal
> gets a track). Renames **Medium→Normal, Very Hard→Epic.** **Tier = length; hero count = damage:** Pay the
> Price scales — **2–3 heroes Weak −1/Miss −2; 4–5 heroes Weak −2/Miss −3** (the roller takes the hit; the
> only thing that changes with group size; Mend's −1 unscaled). **Players vs. characters: 2–6 players; up to 6
> = 5 characters + a Guide; solo dropped; 5–6 players → recommend one Guide.** Supersedes the Option B fixed
> ladder above. See [[challenge-ladder-final]] and [[player-count-model]]; feel validated by `readiness_per_box.py`.
>
> ⚠️ **2026-06-27 SRD-feedback batch — DECIDED and PROPAGATED book-wide (Master Ref, SRD, all chapters, all
> sheets, the app, Math&Sim, Book Outline).** **(1) "Oracle's Blessing" → "Doubles"** (it's just crit-hit /
> crit-miss: doubles upgrade a Hit, a Miss on doubles feeds the antagonist). **(2) "Closing In" → "Bad Guys
> Close In"** — that's the move name; the short **"Closing In"** is the printable-sheet abbreviation ONLY.
> **(3) Downtime** is no longer framed as a heal or a win-step — it's the between-Stories reset whose job is
> **restoring Broken Assets** (Recovery Scenes already heal free/any-time). **(4) Threads/B-plots REMOVED**
> entirely (TODO to redesign later). **(5) Milestone ≈ ~1 hour** of table time (the "40-Minute Rule" is now
> the **One-Hour Rule**). **(6) Moves render as cards** via a shared `.lca-move` class (`docs/stylesheets/
> extra.css`); the SRD is the reference implementation, and the cards are now **rolled out book-wide**
> (Ch.4/5/7/8/9/10/11 + SRD). See [[srd-feedback-batch]].
>
> ⚠️ **2026-06-22 dice rework (see [[dice-and-scaling-rework]]) — also propagated:** core roll **+0/+1/+2**
> (pick **2 of 5 stats** = +1, **3 Assets** = +1), single broad **Attribute retired**, recovery ratchet
> dropped (full heal to 9), "+1 box for 4+" dropped. Trust this banner + Math&Sim §0 over any stale phrasing below.

- **Terms:** Guide (never "GM"), Co-op play (never "GMless"), Readiness (the hero's single **Health Bar** — body/mind/supplies in one 0–9 track; the *term* is always "Readiness," but "Health Bar" is the OK plain-language framing — supersedes the old "never HP/health" rule, 2026-07-02),
  Assets, **Stats** (pick **2 of the closed five**: Strong/Quick/Clever/Sneaky/Charming — the
  most-relevant one is chosen objectively, not argued), Story / Story Arc (never "Quest"; never bare "Arc"), **Hero Track** (the hero's
  progress clock — renamed from "Story Arc Track" 2026-07-03, which supersedes the old "never Hero Track" rule; still never "Quest Track"), **Episode/Movie** (the two *individual* story sizes), **Season/Series**
  (prose *collection* patterns, not sizes — see [[spine-model]]), **antagonist** (the umbrella
  term for the adversary — default to it; **never "villain,"** which is only *one type* of
  antagonist — it can also be a force: a desert, a plague), Antagonist Track, **climax**
  (the final, usually Epic, Challenge — the last Milestone simply *is* the win; the separate
  **"Showdown" roll was retired 2026-06-26**, no extra finishing roll), Milestone, Scene, Challenge, Pay the Price, **Devil's Bargain**
  (buy a win on a Miss for a antagonist box), **Doubles** (the crit-hit/crit-miss rule — doubles upgrade a **Hit** one tier; a **Strong Hit** on doubles is an **Outstanding Success** = spectacular success **plus +1 to your next roll** (DECIDED 2026-07-02) — and **during a Challenge it fills two boxes instead of one** (DECIDED 2026-07-05; both effects apply); a **Miss on doubles** advances the antagonist; **"Oracle's Blessing" retired 2026-06-27**), **Bad Guys Close In** (the narrated antagonist beat on an odd Antagonist box — the bad guys close in; the short form **"Closing In"** is the printable-sheet abbreviation ONLY; **"Attack"/"Surge" retired**), **Recovery Scene** (the fall-back-and-regroup move — now **free**), **Fall back**
  (retreat from a Challenge — was "Flee"), Quit the Story Arc, **Downtime** (between-Stories reset whose job is restoring **Broken Assets** — NOT a heal; Recovery Scenes already heal free/any-time), Ask the Oracle, Growth/Growth Track/Boon/Trade In
  (advancement — use "Growth," never "XP"). **Threads/B-plots: REMOVED 2026-06-27** (the subplot subsystem is cut — see TODO). Avoid "damage."
- **Core roll (DECIDED 2026-06-22):** 2d6 + a **+0/+1/+2** modifier. You get **+1** if the action's
  **most-relevant stat** is one of your **2 of 5** (Strong/Quick/Clever/Sneaky/Charming — chosen
  *objectively*, not argued: a chase is Quick, period); **+1** if any of your **3 specific Assets**
  applies (these *are* argued — story flexibility); **+2** if both, **+0** if neither (the risk-of-
  failure floor). 10+ Strong, 7–9 Weak, 6− Miss; doubles upgrade a **Hit** (Doubles) but on a **Miss advance
  the antagonist** (Ch.7). A Hit = **narrate the change**. Tuned to stat≈0.55 / asset≈0.85 apply rates → avg mod ≈ 1.40 (was 1.85);
  this **retires the single broad Attribute** (the closed-five *list* survives; you pick two of it).
- **Readiness:** starts **9**. Weak −1, Miss −2 (always — no dodging). Max never declines; a
  **Recovery Scene heals the party fully to 9** and is **free** (no roll, no antagonist advance — fall
  back as often as the fiction allows). **Mend** (small risky any-scene patch — Strong +3 / Weak +2 /
  **Miss −1**, self or ally, cap 9, never advances the antagonist, can't revive Out of Action). **Out of
  Action** at 0 breaks an Asset **and advances the antagonist +1** (one of the three triggers; can't be
  Devil's-Bargained away). **Heroes can't die** — Readiness is a *pacing signal* (when to fall back)
  and a resource weighed against the Devil's Bargain, **not** the loss meter. (Loss is a rare earned
  tail, not a target — Math & Sim §0.)
- **Story structure — single nested SPINE (DECIDED 2026-06-13; see [[spine-model]] & Math & Sim
  §0).** Dropped sandbox play. One Story = one spine with a **Hero Track** (progress, 1
  box/Milestone → the **climax**) and an **Antagonist Track** (the antagonist's race; three triggers
  below). **Two individual sizes: Episode = 3 Milestones / 5-box Antagonist Track (Bad Guys Close In on 1·3·5);
  Movie = 6 Milestones / 9-box (Bad Guys Close In on 1·3·5·7·9) — same at any party size.** **Season/Series are prose collection patterns, not
  sizes** (Episode/Movie are individual stories; a Season strings them on a throughline, a Series is
  a run of Seasons). **Nesting is back** (a Season is *made of* Stories). (Threads/B-plots REMOVED 2026-06-27.)
- **Antagonist Track — the Devil's Bargain spine (DECIDED 2026-06-25).** Advances **+1** three ways:
  a **Devil's Bargain** (on a Miss, forgo the damage + upgrade to Strong → antagonist +1; optional; not
  on a knockout roll — the main, player-authored driver), a **Miss on doubles** (random), and **Out
  of Action** (catastrophe). **Recovery never advances it** (free). **Odd boxes are Bad Guys Close In** — the
  narrated antagonist beat (cut to the antagonist closing in / winning off-screen); even boxes are silent pressure; the
  **last box = antagonist wins** → lose the Story before the heroes finish (loss vector). The antagonist may
  be a **force** (a desert, a plague) — characterize it so each time the bad guys close in is concrete. **Quit the Story
  Arc** = terminal give-up; a lost Story seeds a new one. Loss is a rare earned tail; the metric is
  the **photo-finish.** (Validation: `Math & Simulation Reference.md` §0, `sim_devils.py`/`sim_devils2.py`.)

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
  / Take the Price) = once/Session, Mild (Reroll / +1-to-your-next-roll / Lend-a-reroll /
  Steady-Hands-Mend) = once/Scene; **lock the Trigger to a situation → one step more often**.
  Never a *permanent* modifier (banked +1 = a temporary one-roll bonus, §4c-safe); excluded effects =
  extra track progress, preventing Out of Action. Max 2 Boons/Asset. Named **recipes** (Signature
  Move, In My Element, Reliable, Lend a Hand, Mender, Scout, Take the Hit) are pre-built
  combos. Genre d10 trigger tables: **all 7 kits done.** (**+1-to-roll** and **Free Oracle** effects
  cut 2026-07-04; **Dig Deep** recipe cut with the on-demand +1.)

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
