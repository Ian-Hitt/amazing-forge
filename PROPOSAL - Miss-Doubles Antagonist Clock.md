# PROPOSAL — Antagonist Clock Redesign (the Devil's Bargain spine)

**Status: RECOMMENDED MODEL converged 2026-06-25 — pending Ian's final go to propagate.**
The clock is no longer "miss+doubles only" — that became the *random* leg of a three-trigger
model built around a player **Devil's Bargain.** Validated by `sim_devils.py` / `sim_devils2.py`.
The original Miss+Doubles writeup (the lineage that led here) is retained below the line.

---

## THE DEVIL'S BARGAIN SPINE — recommended model (2026-06-25)

The Antagonist Track advances from **three triggers** — two player-facing, one structural — and
**Recovery is free** (no surge). Readiness is decoupled from loss; the only loss vector is the
antagonist filling the track before the heroes finish their last Milestone.

### The three triggers

1. **Devil's Bargain (player choice).** On a **Miss**, a hero *may* forgo the Readiness damage
   **and** upgrade the result to a **Strong Hit**, in exchange for advancing the Antagonist Track
   **+1.** A bargain pushes *both* clocks: it fills the hero's challenge box *and* feeds the antagonist
   — a live "am I closer to my finish than the antagonist is to theirs?" gamble. It is always optional
   ("you never have to use it"). It is the engine, and it is the in-fiction source of the antagonist's
   story beats, so the mechanic *is* in service of the story.
   - **Can't bargain the knockout roll.** You may **not** bargain a Miss whose damage would knock
     you **Out of Action.** The bargain keeps you fighting; it can't save you from defeat. This makes
     OoA a genuine stake and pushes players to bargain *preemptively* around the danger zone (~4
     Readiness) to avoid being cornered — so cautious play feeds the clock too.
2. **Matches (random).** A Miss showing **doubles** advances the antagonist **+1** regardless (doubles
   on a *Hit* stays Oracle's Blessing). ~5.7%/roll. This is the **disciplinarian**: it makes riding
   to the brink risky, so rational players keep a buffer. A doubles-Miss you *also* bargain = **+2**
   (the scary case — ruling: they stack).
3. **Out of Action (structural).** A hero hitting **0** advances the antagonist **+1** (on top of
   breaking an Asset). Ties the clock lightly back to the true catastrophe. Numerically minor under
   free recovery, but it's what makes OoA *matter to the antagonist*.

### Track sizes & narration (decoupled)

The **tick** (frequent, bursty) is decoupled from the **narrated antagonist beat** (paced) — so
back-to-back ticks never cram multiple antagonist scenes into one fight. Narrate the antagonist getting
ahead only on the **odd "attack" boxes**; even boxes are pure pressure (a visible countdown).

- **Episode = 5 boxes.** Attacks on **1 · 3 · 5** → **3 antagonist beats.** Box 5 = climax / antagonist win.
- **Movie = 9 boxes.** Attacks on **1 · 3 · 5 · 7 · 9** → **5 antagonist beats.** Box 9 = climax / win.
- The track **must be odd** so the top box is itself an attack (the antagonist's winning blow *is* their
  final attack). That's why Movie is 9, not 10. **9 is the max for a Movie.**

### Why this model

- **Serves the north star.** "What is a roleplaying game but making choices and seeing what happens?"
  The clock is a *choice* (the bargain), disciplined by *randomness* (matches), with a structural
  floor (OoA). Every advance is narratable: you cut a corner, fate swung, or you fell.
- **Not the rejected resource economy.** The recovery-surge tie was *defensive bookkeeping* (ration
  your heals) — grim and choiceless. This is a *Faustian gamble* — active, tempting, story-generating.
  It is technically a second resource to balance, which is the point of calling it a devil's bargain.
- **Recovery is free.** Readiness becomes a pacing signal ("battered → fall back") and a resource you
  weigh against the clock — no longer a loss vector by itself.
- **Loss is a tail, not a target.** The dramatic deliverable is the **photo-finish** (antagonist one box
  from winning); loss is the rare *earned* overrun. We tune for photo-finish frequency and let loss
  fall where it may. Earlier loss-rate targeting is abandoned — the goal is the tensest story, not a
  win/lose ratio.

### Sim results

`sim_devils.py` / `sim_devils2.py`: rule = can't-bargain-knockout + OoA ticks; recovery at Readiness
~4; **Option B fixed-difficulty sizing** (Easy 2 / Medium 3 / Hard 4 / Very Hard 5, party-independent).
Photo-finish % = antagonist ends one box from winning; loss % = antagonist overruns. Three table
temperaments (cautious / realistic / reckless bargaining):

| Story | cautious | realistic | reckless |
|---|---|---|---|
| **Episode = 5** | 8% pf / 3% loss | 20% / 6.5% | 44% / 16% |
| **Movie = 9** | 10% pf / 5% loss | 21% / 11% | 38% / 22% |

- **Party-independent** (party 2 ≈ party 4) — Option B holds, **zero party-size rules**, the whole
  "Playing as a Pair" subsystem stays deleted.
- **Movie is intentionally spicier than the Episode** — the bigger, higher-investment story carries
  more real peril at its climax. Losses are uncommon and always self-inflicted by pushing the bargain.
- **The photo-finish is player-authored:** a pushing player rides to one-box-away *by design*; track
  length sets the *stakes* of pushing, not its frequency. Rational players self-regulate (keep a
  buffer) because matches/OoA can tip a brink-sitting antagonist over.

### Open / to propagate

- Same big propagation surface as the original (Ch.8–10 + all 7 genre kits + Three-Act / Beat Sheet
  / Story Engine all reference the old recovery-surge model and Option-A party-scaled difficulty).
- Reframe the "reserved climax box" language — here the top *odd* box is the antagonist's final attack.
- Sequence against the un-propagated 2026-06-22 dice rework (+0/+1/+2, retired Attribute) so the
  chapter rewrites land together.
- Audit Boons/Mend/Downtime for anything that keyed off recovery-surge.

---

## Lineage — the original Miss+Doubles writeup (2026-06-23)

*Kept for the reasoning that led to the model above. Where it differs, the section above wins.*

---

## The problem this solves

The current spine ties the Antagonist Track to **Recovery Scenes** (a Surge per regroup). That:

- turned the game into a **resource-management / attrition economy** — which isn't the point;
  the game's identity is *all mechanics in service of story*;
- made loss **hyper-sensitive to challenge pacing**: the sim assumed a constant 2 challenges
  per milestone, but real play is a variable 0–2. At realistic pacing, loss **collapses to
  ~0%** — the game is effectively *unloseable*, gutting its one distinctive feature;
- created **duo fragility** that needed an elaborate special-rules subsystem.

## The core change

The Antagonist Track advances on a **Miss + doubles** (a roll that is *both* a Miss *and*
shows doubles). **Recovery becomes free** (heal, no Surge). Readiness stays as the
"battered → fall back" pacing signal. Out of Action still **breaks an Asset** (durable teeth)
and forces a free Recovery.

### Why Miss+doubles is the right trigger
- **Automated & player-indirect** — can't be gamed to zero (the property we wanted from the recovery tie).
- **Not resource management** — the property we wanted to *lose*.
- **Faithful to Monster of the Week** (the inspiration): a Miss is when the GM advances the countdown.
- **Story-serving**: a Miss becomes *"you stumbled and the antagonist pounced,"* not "−2 Readiness."
- **Calculable**: P(Miss ∧ doubles) = **5.74% per roll (~1 in 17)**.
- **Loseable in ALL play styles** — light play still ~5% (the recovery model collapsed to ~0%).
- **Doubles flip from pure-good to double-edged**: Oracle's Blessing on a hit, antagonist Surge on a
  Miss. *"The dice swing hard, for good or ill."*

## The dice rule
- Roll **2d6 + mod** (+0/+1/+2). **10+ Strong, 7–9 Weak, 6− Miss.**
- **Doubles on a HIT** → Oracle's Blessing (upgrade a tier), as now.
- **Doubles on a MISS** → stays a Miss **and the antagonist advances one box** (no upgrade).
  The Miss still costs Readiness.

## Readiness (same job, decoupled from the antagonist)
- Starts **9**. Weak −1, Miss −2.
- **Recovery Scene**: fall back, heal to 9, **free** (no Surge). Its job is to push you into
  regroup / character beats — narrative pacing, not a resource.
- **Out of Action** (0 Readiness): forces a free Recovery **and breaks an Asset** (lost until
  Downtime). This is the durable sting that keeps Readiness meaningful.
- **Emergent coupling (free flavor):** broken Asset → fewer +2s → more Misses → more
  Miss+doubles → antagonist creeps faster. Soft, fiction-first; mechanically minor (~0.2 pts).

## Clock sizes — grounded in the doubles math
Antagonist advances ≈ 5.74% × (rolls in the story):
- **Episode** (~16–25 rolls): ~**1** advance.
- **Movie** (~32–51 rolls): ~**2.4** advances.

Set the clock ~2× the typical advance so the antagonist usually ends *one short* (the near-miss /
photo-finish) and overrunning is the tail. Sim results (party 3, broken-Asset coupling live):

| Clock | balanced loss | near-miss | light | action |
|---|---|---|---|---|
| **Episode = 3** | 14% | 21% | 7% | 19% |
| Episode = 4 | 4.6% | 9.5% | 1.9% | 6.9% |
| **Movie = 5** | 12% | 13% | 4.7% | 18% |
| Movie = 6 | 5.2% | 7% | 1.6% | 8.6% |

**Recommended: Episode = 3, Movie = 5** (dramatic + loseable; Movie matches MotW's 5).
Safer alt: **4 / 6** (~5% loss).

## The party-size question — KEY open decision
Bigger groups roll more dice → more Miss+doubles → faster clock. Under the recommended clocks,
balanced-pacing loss climbs with party size (duo 5.9% → 5-player 30% on a Movie). Two fixes:

**Option A — party-scaled challenges + party-scaled clock.**
Keep Medium = party-size boxes; add **+1 clock box per player above 3**. Flattens loss to ~12%.
Cost: two things scale with party.

**Option B — fixed-difficulty challenges + fixed clock (Starforged-style). ← RECOMMENDED, CONFIRMED**
Challenge size depends **only on difficulty**, not party: **Easy 2 / Medium 3 / Hard 4 /
Very Hard 5** for everyone. Filling a fixed-size track takes ~the same number of rolls
regardless of who's rolling, so **total rolls per story become ~party-independent → the clock
needs no scaling.** One difficulty table, one clock table, **zero party-size rules.**
- Cost: big groups resolve a small fixed challenge in ~1 round (some players don't act in it) —
  the mirror of the duo "thin" issue; big groups lean on Hard/Very Hard for meaty set-pieces.
- Bonus: makes the duo's Medium meatier (3 boxes) *for free*, settling the original complaint.

**CONFIRMED 2026-06-23 (`sim_md_fixed.py`).** Fixed sizing (Easy2/Med3/Hard4, 40/40/20 mix),
clocks Ep3/Mv5. Balanced-pacing **Movie loss is flat across party size: 2p 10.7% · 3p 10.9% ·
4p 11.3% · 5p 12.5% · 6p 13.8%** (vs Option A's 5.9%→30% swing). Episodes flat too
(12.8%→15.3%); light play stays loseable (duo Movie 4.1%); near-miss ~12–14% Movie / ~21% Ep
across all sizes. The mild upward creep at 5–6 players is in the right direction (big groups, not
small) and small enough to ignore — a 6-box Movie clock for 6 players would flatten it if ever
wanted. **Verdict: adopt Option B — no party-size rules at all.**

Under **either** option the duo needs **no special rules** — Readiness stays 9, no 5-box duo
track, no 12-box hero sheet.

## What this DELETES
- The recovery ratchet / surge-on-recovery.
- The entire **"Playing as a Pair"** plan (+3 Readiness, 5-box duo Movie track, 12-box hero
  sheet, variable-headcount handling).
- The need for **precise loss-rate tuning.** Philosophy: loss *real-but-rare* + frequent
  *near-miss*; the structure delivers this robustly, so the math is a **sanity check, not a dial.**

## Reserved climax box — needs reframing
With no voluntary control over the fill, "antagonist one step away" emerges *statistically* rather
than being mechanically guaranteed (the old reserve worked because voluntary recovery stopped
one short). Top box = the Showdown; the antagonist overrunning into it before you reach your last
Milestone = loss. Decide whether to keep "reserved" language or simplify.

## Open questions for tomorrow
1. ~~Option A vs B (party scaling)~~ — **RESOLVED: Option B, confirmed flat across 2–6 players.**
2. Exact clock sizes — **3/5** (dramatic) vs **4/6** (safer).
3. Reserved-box framing under the new fill.
4. **Audit anything that keys off Readiness/recovery** and might break when recovery goes free
   (Boons granting rerolls/Mend, Mend itself, Broken-Asset restoration timing, Downtime).
5. **Propagation order** — this interacts with the un-propagated 2026-06-22 dice rework
   (+0/+1/+2, retired Attribute). Sequence the chapter rewrites so they land together.

## Sims (scratchpad, this session)
- `sim_md_full.py` — full model: Miss+doubles, free recovery, broken-Asset coupling, clock
  sweep, party-size robustness. **Move into repo + Math & Sim §0 if we adopt this.**
- `sim_missdoubles.py` — first cut of the trigger.
- `sim_cpm_sens.py` — proves the pacing-sensitivity problem (loss collapses at realistic pacing).
- `sim_diffknob.py` — difficulty/pacing as opt-in danger dials.

## Tonight's playtest config (2 players) — for the record
Published book as-is **+** free recovery **+** a **3-box** clock ticking on **double-Misses**
**+** challenges sized at the 3-player column. A test of whether the core loop is *fun*.
