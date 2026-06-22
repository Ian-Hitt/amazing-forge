# Lights, Camera, Action! — Math & Simulation Reference

> **Purpose.** A single source of truth for the **balance math** behind the game: the
> dice probabilities, the settled numeric rules, the *structural assumptions* used when
> modeling full play, and the results of any simulations. When a balance question comes up,
> set parameters **here** so we never have to re-guess them. Companion to
> `Core Mechanics - Master Reference.md` (the rules) — this doc is the *numbers behind* those
> rules.
>
> **Flags:** `✅ CONFIRMED` (settled), `📐 DERIVED` (computed from settled rules),
> `🔧 ESTIMATE` (assumption for modeling — not yet confirmed), `🚧 OPEN` (undecided).
> **Last updated:** 2026-06-13.

---

## 0. CANONICAL — split stats+assets, no ratchet (✅ 2026-06-22, `sim_spine.py`)

> **This is the current canonical balance model. It supersedes §0-prev (the 2026-06-13 spine model)
> and §0b (the difficulty ladder) below**, which are kept for the reasoning trail. Three locked
> changes (memory `dice-and-scaling-rework`; explored in scratchpad `sim_scaling*`/`sim_pair*`):

**1. Core roll is now +0 / +1 / +2 (split stats + assets).** Playtest showed players argue *any* of
4 specific Assets into fitting, so +2 was near-universal and the +1 floor collapsed. Fix — separate a
**honest** layer from a **flexible** one:
- Pick **2 of the 5 stats** (Strong/Quick/Clever/Sneaky/Charming). The action's **most-relevant**
  stat is chosen *objectively, not argued* (a chase is Quick, period). If it's one of your two → **+1**.
- **3 specific Assets**, still flexible/argued. If any apply → **+1**.
- Both → **+2**, one → **+1**, neither → **+0** (the new risk-of-failure floor).
- Tuned: `P_STAT = 0.55`, `P_ASSET = 0.85` → **avg mod ≈ 1.40** (was 1.85); +2 rate ≈ 47% (was 85%).
  This **retires the single broad "Attribute"** — you pick two stats instead.

**2. No ratchet.** A Recovery Scene heals the party **fully back to 9** every time; max Readiness no
longer declines. The old declining ceiling was keyed to *recovery count*, which grows with story
length — that's what broke Movie scaling (see "Why Movies didn't scale" below). Dropping it makes the
party durable enough to need only **~3 recoveries per Movie**, which is what makes the 4-box track right.

**3. Tracks & difficulty ladder.**

| Size | Milestones | Antagonist Track | Notes |
|---|---|---|---|
| **Episode** | 3 | **2** | unchanged |
| **Movie** | 6 | **4** (was 3) | **duo = 5** (one extra regroup) |

- Ladder: **Easy/Medium/Hard = players−1 / players / players+1.** The old **"+1 box for 4+" rule is
  dropped** — on the lower curve it double-penalized; plain `Medium = players` lands party 3 & 4 in band.

**Validation (`sim_spine.py`, all-Medium, fresh party / no Boons):**

| Party | Episode loss | Movie loss (track) | Movie recoveries |
|---|---|---|---|
| 2 | 12.5% | 9.6% (5-box) | ~4.1 |
| 3 | 6.3% | 15.7% (4-box) | ~3.2 |
| 4 | 6.1% | 12.3% (4-box) | ~3.1 |

**Boons settle a fresh party toward target** (per-roll tier-upgrade chance `BOON_P`): party-3 Movie
15.7% → **10.7%** at `BOON_P=0.05` → 6.9% at 0.10 — a campaign arc, not a break (the design guard barring
track-progress / OoA-prevention Boons keeps the curve intact). The slightly-hot fresh baseline is
intentional headroom for advancement; groups also dial down with Easy encounters. Duo Episodes (12.5%)
run a touch tense (adding a box over-corrects to ~1.4%); duos lean on the 5-box Movie track, not on
trivial 1-box "Easy" challenges.

**Why Movies didn't scale (the deep diagnosis — keep, it saves re-deriving).** This is an *attrition*
model, so loss inherently grows with story length: a Movie compounds attrition over ~2× the runway
while an Episode ends before danger accrues. **No single uniform rule puts both sizes at 10%** — short
stories want tightening, long ones cushioning; they pull opposite ways, so the two sizes are tuned
*individually* (fine — there are only two). The old killer interaction: the ratchet was keyed to
recovery *count*, which grows with length, so any fix that gave Movies the recovery headroom they
needed *fed* the ratchet that killed them. Dropping the ratchet broke that coupling. (`sim_scaling.py`
shows loss flat across length 2–8 only once the ratchet is keyed to progress / removed.)

---

## 0-prev. SUPERSEDED — the declining-ceiling spine model (2026-06-13, `sim_spine.py`)

> **Superseded 2026-06-22 by §0 above** (no ratchet; +0/+1/+2 roll; Movie 6/4). Kept for the
> reasoning trail. It dropped **sandbox** play (a bag of concurrent fixed-size arcs) for a **single
> nested spine**, because the old structure could not produce the design goal — a story whose villain
> ends *one step from winning* (the photo-finish).

**The model.** One Story Arc = one spine with two tracks. The **Story Arc Track** is progress (1 box /
Milestone; filling it reaches the **Showdown**). The **Antagonist Track** is short, its **top box
reserved as the climax**. Recovery is **two moves + a declining ceiling**:
- A **Readiness max** that starts at **9** and **drops 1 per Recovery Scene** (floor 4; resets to 9
  at Downtime). The ratchet that makes a Story Arc tighten as it runs.
- **Recovery Scene** (fall back and regroup) → restores the party **up to the current max**,
  reliable; **+1 villain Surge**; **lowers the max by 1.** The only thing that advances the
  Antagonist Track. Emergent/player-chosen; won't voluntarily surge the climax box.
- **Mend** — a small risky **any-scene** patch (Strong +3 / Weak +2 / **Miss −1**, capped at the
  current max), **no Surge**, can't revive Out of Action, **no usage cap.** The −1 risk + the
  declining ceiling (it only heals to the sinking max) keep it from substituting for a regroup.

**Out of Action forces a Recovery Scene that surges even into the climax box** — the loss vector
(and the reason Mend can't revive).

**Two individual sizes (the only ones with machinery):**

| Size | Milestones | Antagonist Track | 1st-rest avg | Photo-finish | Pre-climax loss |
|---|---|---|---|---|---|
| **Episode** | **3** | **2** (1 surge + climax) | **8.0** | ~98% | ~1.6% |
| **Movie** | **6** | **3** (2 surges + climax) | **8.0** | ~92% | **~7%** |

*(Party 3, p+2 = 0.85, Oracle on; CAP_DROP=1, floor 4; Mend +3/+2/−1, ungated; regroup when avg ≤ ~5–6.)*
**Season/Series carry no box machinery** — prose *collection* patterns (a run of Story Arcs);
B-plots are lose-clock-free *threads*. The ceiling **resets at Downtime (every Story Arc)**, so it
only ratchets *within* an arc — never across a Season/Series.

**Key tuning facts** (from the sweeps, `sim_spine.py`):
- The **surge-triggering regroup must restore the party** (to the current ceiling). A small/rolled
  heal that surges death-spirals: Movie loss hits **94%**. So **Mend (small + risky) cannot be the
  surge move**; it's a *separate, non-surging* tactical patch.
- **The declining ceiling (CAP_DROP=1) lands Ian's target:** 1st-rest avg exactly **8**, each
  regroup −1 ("a little worse each time"). CAP_DROP=2 spirals (Movie ~54%); `CAP_FLOOR` and
  gating forced revives barely move it — the ratchet *is* the pressure.
- **Mend works ungated** (any scene, no per-Milestone cap). The declining ceiling caps how high Mend
  can take you, so it can't substitute for a regroup — Recovery-Scene frequency is unchanged vs.
  gated (~2/Movie), the villain still surges, and it *lowers* loss: Movie **~7%** (gated was ~16%),
  photo-finish ~92%. So ungated is both simpler and closer to the ~10% goal.
- **Movie loss lands ~7%** (Episode ~1.6%) — in the 9-of-10 zone, a touch *under* the 10% goal.
  Nudging it exactly to 10% is structural (TODO #13), and "ceiling carries across a Season"
  is a hard-mode dial (TODO #14).
- **Without Mend / without the ceiling**, the Movie wants 7/4 and lands ~89–93% photo / ~4–6% loss;
  governing rule for sizing: **Antagonist boxes ≈ Milestones ÷ ~2.5 + the reserved climax box.**
- A **Mend Miss can knock you to Out of Action**, which discourages gambling a patch at very low
  Readiness — the math teaches "fall back fully when you're really hurt." **Conservative regrouping**
  beats panic-resting. The surge ticks **once per Recovery Scene**, never per hero healed.

---

## 0b. CANONICAL — Challenge difficulty ladder & party-size scaling (✅ 2026-06-21, `sim_mix.py`)

> ⚠️ **PARTIALLY SUPERSEDED 2026-06-22:** the "+1 box for groups of 4+" party-size scaling rule below is **dropped** per §0 — the ladder is now a plain Easy/Medium/Hard for all sizes. The rest of this section's reasoning still stands.

> **Re-centers the difficulty ladder.** Difficulty is a **screen-time dial, not a balance knob**
> (players pick Hard for set-pieces, Easy for quick beats), so a real story *mixes* Easy/Medium/Hard.
> The balance must therefore hold for a **mix**, not for all-Easy play.

**The ladder (DECIDED 2026-06-21):**
- **Easy = players − 1** (min 1), **Medium = players**, **Hard = players + 1.**
- **Very Hard = players + 2** — *optional, climaxes only* (see below).
- **Groups of 4+ add one box to every tier** (→ Easy = players, Medium = +1, Hard = +2, Very Hard = +3).

**The bug it fixes.** The old ladder (Easy = players) tuned the game to the *floor* of its own
difficulty range. Modeling a story-shaped mix (per-Challenge **40% Easy / 40% Medium / 20% Hard**)
on the canonical spine showed any realistic mix overshoots the loss target — the 3-player Movie hits
**~18% loss** (vs. the ~7–10% goal). Difficulty looked like a "sledgehammer" only because the ladder
was centered wrong: loss is convex (tail-driven) and the declining-ceiling ratchet amplifies it, so
all the error pushed one way. **Centering Medium on the balance point** makes Easy scenes bank slack
and Hard scenes spend it, so a mix nets to target. The **+1 box for 4+** keeps big parties (more
Readiness + Aid) regrouping enough to advance the villain — restoring climax tension that pure
recentering let sag.

**Validation** (`sim_mix.py`, canonical config, 40/40/20 mix, 80k stories/cell):

| Party | Easy = | Episode loss | Movie loss | Movie photo-finish |
|---|---|---|---|---|
| 2 | p−1 | 3.1% | 10.1% | 88.1% |
| 3 | p−1 | 1.4% | 5.7% | 90.5% |
| 4 | **p** | 4.4% | 13.5% | 85.0% |
| 5 | **p** | 3.7% | 10.6% | 85.4% |
| 6 | **p** | 3.3% | 8.8% | 84.2% |

All party sizes 2–6 land in a **~5–13% Movie-loss / 84–90% photo-finish** band — vs. the old ladder
on the same mix (3-player 18%, 2-player 29%) or pure recenter without the 4+ box (5–6 players sag to
3% loss / 74–78% photo, too safe). Party 4 is the boundary (slightly hot at 13.5%); the 4+ cutoff
keeps its error on the *tension* side rather than the *too-safe* side (Ian's call — 4+ over 5+).

**Very Hard climax (optional top rung), `sim_climax.py`.** Easy→Hard spans only ~2 boxes at a
3-player table, so **Very Hard = players + 2** was added as a deliberate lever for the **Showdown** —
the *finale itself*, not a pre-finale obstacle, so its extra length can't bleed attrition into a
later scene (the only risk is an OoA *during* the finale, softened by the "fill the last box wins
first" ruling). Modeled by making a Movie's last Challenge Very Hard vs. drawn-from-mix:

| Party | Very Hard finale boxes | Movie loss (mix climax → Very Hard) | Photo-finish |
|---|---|---|---|
| 2 | 4 | 10.8% → 14.3% | 87→85% |
| 3 | 5 | 5.3% → 7.9% | 91→90% |
| 4 | 7 | 12.1% → 15.2% | 86→84% |
| 5 | 8 | 9.6% → 11.5% | 86→86% |
| 6 | 9 | 7.7% → 9.2% | 85→86% |

Only **~+2–3 points of loss**, photo-finish flat — a gentle, safe escalation (and for the canonical
3-player Movie it nudges loss *toward* the 7–10% target). Excluded from the routine 40/40/20 mix, so
it doesn't shift the balance baseline; it's a discretionary climax tool.

**Note — this supersedes the all-Easy modeling assumption** in §3 below: the canonical play pattern
is a **mix centered on Medium**, not all-Easy. The §0 Episode/Movie figures (7% / 1.6%) are the
all-Easy *floor*; expected play sits at the §0b numbers above.

---

## 1. Settled numeric rules (✅ CONFIRMED — from the Master Reference)

| Quantity | Value |
|---|---|
| Core roll | 2d6 + modifier |
| Modifier — Asset applies | **+2** |
| Modifier — anything else | **+1** (floor; never +0) |
| Strong Hit | total **10+** |
| Weak Hit | total **7–9** |
| Miss | total **6 or less** |
| Oracle's Blessing | doubles upgrade result one tier (optional but usually on) |
| Readiness — start / max | **9**; max **declines −1 per Recovery Scene** (floor 4), resets to 9 at Downtime *(§0)* |
| Pay the Price — Weak Hit | **−1** Readiness |
| Pay the Price — Miss | **−2** Readiness |
| Mend (any-scene patch, ungated) | **+3** Strong / **+2** Weak / **−1** Miss Readiness (up to current max); **no Surge**; can't revive Out of Action *(§0)* |
| Recovery Scene (fall back & regroup) | restores party **up to current max**, reliable; **+1 Antagonist Surge** *and* **−1 to the max** *(the only villain-advance trigger — §0)* |
| Downtime (between Story Arcs) | resets max to 9, heals to full, restores a Broken Asset; **no Surge** |
| Out of Action | Readiness = **0** (recoverable; not death); **forces a Recovery Scene → can surge the climax box (loss vector)** |
| Challenge length — Easy / Medium / Hard | **players −1 (min 1) / players / players +1**; **4+ players add 1 box to each** *(§0b)* |
| Story Arc Track length — Episode / Movie | **3 / 6** Milestones *(§0; Season/Series are prose collections, no box machinery)* |
| Antagonist Track length — Episode / Movie | **2 / 3** (top box = reserved climax) *(§0)* |

> 🔁 **SUPERSEDED by §0 (2026-06-13).** The four-type / equal-length-Antagonist-Track structure
> below is replaced by the spine model (Episode 3/2, Movie 6/3; Season/Series are prose
> collections). Kept for the trail. *(Historical:* the old labels were Episode 3 / Movie 8 / Season
> 8 / Series 12 over a unified per-Milestone rule.) The Growth-rate point still holds: **1 Growth
> per 3 Milestones is balance-neutral** — Boons are horizontal, so Growth speed never rescales the
> +2/+1 curve or enemy tracks.

---

## 2. Dice probabilities (📐 DERIVED — exact, from the 2d6 curve)

**Without Oracle's Blessing** (matches the win rates quoted in the Master Reference):

| Modifier | Strong (10+) | Weak (7–9) | Miss (6−) | Hit rate |
|---|---|---|---|---|
| **+2** | 41.7% | 41.7% | 16.7% | **83.3%** |
| **+1** | 27.8% | 44.4% | 27.8% | **72.2%** |

**With Oracle's Blessing** (doubles upgrade one tier — the usual table state):

| Modifier | Strong | Weak | Miss | Hit rate |
|---|---|---|---|---|
| **+2** | 44.4% | 44.4% | 11.1% | **88.9%** |
| **+1** | 33.3% | 44.4% | 22.2% | **77.8%** |

*Note:* the +1→+2 jump roughly **doubles the Strong-Hit rate** (clean successes) while only
modestly raising the overall hit rate — this is the intended "Assets are clearly worth it,
but off-Asset is never hopeless" feel. Expected Readiness loss per roll: at +2 ≈ **0.75/roll**
(no Oracle) or **0.67/roll** (Oracle on); at +1 ≈ **1.00 / 0.89** per roll.

---

## 3. Structural assumptions for full-play modeling

These describe a *typical Episode* and are needed to simulate Readiness over a whole
adventure. **They are estimates pending confirmation / recovery of the original sim values.**

| Parameter | Value | Flag | Source |
|---|---|---|---|
| Party size | 3 | 🔧 ESTIMATE | modeling default |
| Milestones per Episode | 3 | ✅ CONFIRMED | = Story Arc Track length |
| Challenges per Milestone | ~2 | 🔧 ESTIMATE | Ian, 2026-06-06 |
| Per-Challenge difficulty mix | 40% Easy / 40% Medium / 20% Hard | ✅ CONFIRMED | canonical play pattern, §0b (was "all-Easy") |
| Regular Rolls per Milestone | ~3 | 🔧 ESTIMATE | Ian, 2026-06-06 |
| Mend: max effective heals | 1 per hero per Milestone (gated) | ✅ SF-C | `sim_recovery.py` |
| Share of rolls at +2 | 85% | 🔧 ESTIMATE | "most rolls are +2" + mandatory Attribute (was 80%; see §3b) |
| Oracle's Blessing on? | yes | 🔧 ESTIMATE | usual table state |

> 🚧 **OPEN — recover the original simulation parameters.** The Master Reference's win-rate
> targets and the max-9 Readiness cap came from earlier balance/sim work whose assumptions
> aren't recorded. If those can be found, reconcile them with the table above and re-flag as
> CONFIRMED.

> ✅ **MODELED — rolled recovery (2026-06-09), see §3a below.** Recovery was reworked from a
> certain flat +3 (0–1×/Story Arc) to two **rolled** moves that *always heal* (a bad roll never costs
> Readiness). The brake moved from *scarcity* (limited +3s) to *story injection*: a Mend
> Miss spawns a **new Challenge** and a Downtime Miss spawns a **new Story Arc** — a
> *downstream* drain (more rolls to face) rather than an upfront one. Expected per-use heal:
> Mend ≈ +3.3 (Oracle on); Downtime ≈ +6.4. Simulated in **`sim_recovery.py`**
> (the §4 `sim_antagonist_trade.py` models only the superseded trade question and still uses the
> old flat +3). The §4b flee-only Antagonist results are unaffected (recovery never advances the
> Antagonist Track), but the absolute Readiness/OoA figures shift sharply — see §3a.

---

## 3b. Mandatory Attribute Asset — +2-share sweep (2026-06-12)

> ⚠️ **SUPERSEDED 2026-06-22:** the single broad **Attribute** is replaced by a hero picking **2 of the 5 Stats** (Strong/Quick/Clever/Sneaky/Charming), and the **+0/+1/+2** roll model (§0) supersedes the `P_PLUS2 = 0.85` assumption used below. Kept for the reasoning trail.

Every hero's **first Asset is now an Attribute** (Strong / Quick / Clever / Sneaky / Charming) —
one sanctioned broad Asset, capped at one. This raises the share of rolls made at +2. Modeled
as a bump to `P_PLUS2` and swept against the **BASELINE** antagonist-trade harness
(`sim_antagonist_trade.py`, Miss always costs Readiness; 100k Episodes, party 3, Oracle on).
Note: in the BASELINE model the Antagonist Track never advances (no flee/Pay-the-Price modeled),
so `lost%` = 0 throughout — the informative teeth metrics are **Out-of-Action rate** and
**ending Readiness**.

| p(+2) | note | ≥1 hero OoA | OoA events/Q | end Readiness |
|---|---|---|---|---|
| 0.80 | old baseline (4 narrow Assets) | 9.72% | 0.120 | 4.80 / 9 |
| **0.85** | **expected with the Attribute** | **8.46%** | **0.103** | **4.92 / 9** |
| 0.90 | heavy-leaning (player routes to it) | 7.07% | 0.084 | 5.05 / 9 |
| 0.95 | pathological | 6.10% | 0.072 | 5.17 / 9 |

**Read.** The lift is small and, crucially, **uniform across every hero** — it's a one-time
global shift the model prices in by moving `P_PLUS2` 0.80 → 0.85, not a stackable per-hero
exploit. At the expected 0.85, Out-of-Action drops ~1.3 pts and parties end an Episode ~0.12
Readiness healthier; even the heavy-leaning 0.90 only trims OoA ~2.6 pts. **The Antagonist
economy is untouched** (it runs on fleeing + Pay-the-Price, not the +2 share). Conclusion:
the single capped Attribute is balance-safe — it does not soften the teeth enough to warrant
any compensating change to track lengths or trigger frequency. The max-one cap is what keeps it
there; a *second* broad Asset (the cut "Widen the Domain" path) is what would push `P_PLUS2`
into the teeth-dulling 0.90+ range, which is why it stays banned.

---

## 3a. Rolled-recovery simulation (`sim_recovery.py`, 2026-06-09) — 🔁 SUPERSEDED by §0

> The rolled Mend/Downtime economy modeled here is replaced by the single full-top-up Recovery
> Scene whose cost is the villain Surge (§0). Kept for the reasoning trail.

100k simulated Episodes; party 3, defaults from §3 (p(+2)=0.80, Oracle on). A Mend
Miss injects one Easy Challenge (3 boxes); heroes rest at a safe lull when Out of Action
or at Readiness ≤ 5. **Story Arc-loss is not modeled** (it's a flee/Antagonist question, §4b) — these
columns isolate *attrition*.

| Model | ≥1 hero OoA | OoA events/Q | End Readiness (pre-victory) | After victory heal |
|---|---|---|---|---|
| **OLD** — flat +3, no roll, 1 rest/Story Arc | **9.75%** | 0.12 | **4.80** / 9 | 8.71 / 9 |
| **NEW** — rolled, rest @ ≤5 | **0.04%** | 0.00 | **7.23** / 9 | 9.00 / 9 |

New-model texture: Mend used **5.1×/Story Arc**, **0.68** Misses/Story Arc → **0.68** injected
Challenges/Story Arc (injection cap never hit). Downtime Miss (**owe a Story Arc in your hosts' service**)
fires on **13.3%** of Story Arcs — roughly one owed obligation Story Arc per ~7–8 Story Arcs, a healthy seed
rate for follow-on adventures.

**Sensitivity to how aggressively the party rests** (rest when Readiness ≤ threshold):

| rest if r ≤ | ≥1 OoA | CYB uses/Q | injected/Q | end Readiness (pre) |
|---|---|---|---|---|
| 3 | 2.16% | 3.21 | 0.43 | 5.25 |
| 4 | 0.18% | 4.18 | 0.56 | 6.23 |
| 5 | 0.04% | 5.16 | 0.69 | 7.24 |
| 6 | 0.01% | 6.55 | 0.87 | 8.01 |
| 7 | 0.00% | 10.23 | 1.37 | 8.55 |

### Read (first pass)

- **Reliable healing collapses in-quest attrition.** Out of Action drops from ~1-in-10 Story Arcs
  (old) to **near zero**, and parties finish much healthier (4.8 → 7.2 pre-victory). This is the
  direct consequence of "healing always works" — but it means **the Readiness track stops giving
  the narrative consequences teeth:** Pay the Price doesn't bite, and Out of Action goes near-dead.
- **The Miss→threat brake fires but does *not* restore tension.** It adds ~0.7 Challenges/Story Arc,
  yet OoA stays ~0 — because *the same Mend that draws the threat also repairs the
  damage that threat deals.* It reshapes the **story** (more encounters/owed Story Arcs) without
  moving the **attrition math.** **Verdict: the track needs a real fix (Ian, 2026-06-09).**

### Tuning battery (which lever restores teeth)

Same harness, three proposed levers + combinations. Reference target = **OLD** (the proven
"Readiness had teeth" feel). `danger%` = share of Story Arcs where ≥1 hero was pushed to Readiness ≤2
(the real "Pay the Price bit / should we flee?" signal); `min r` = mean lowest Readiness reached.

| Scenario | ≥1 OoA | danger% | min r | end r (pre) | CYB/Q |
|---|---|---|---|---|---|
| OLD — flat +3, max 9, −1/−2 (reference) | 9.7% | 49.5% | 3.95 | 4.80 / 9 | — |
| NEW current — CYB 4/3, DT 7/6, max 9, −1/−2 | **0.0%** | **3.9%** | 4.65 | 7.23 / 9 | 5.1 |
| **smaller heals alone** (max 9, CYB 3/2, DT 6/5) | 0.1% | 5.9% | 4.54 | 6.75 / 9 | 6.9 |
| harsher price alone (max 9, −1/−3) | 3.8% | 22.6% | 4.09 | 7.23 / 9 | 6.5 |
| **A′** — max **6**, −1/−2, partial heals CYB 3/2, DT 5/4 | 6.1% | **82.0%** | 2.41 | 4.75 / 6 | 8.3 |
| **B** — max **7**, −1/**−3**, heals 4/3, 7/6 | **9.8%** | 72.4% | 2.87 | 6.02 / 7 | 8.0 |
| **G2** — max **9** kept, −1/**−3**, **CYB capped 1×/Milestone** | 10.6% | 36.9% | 3.85 | 6.12 / 9 | 5.4 |
| G1 — max 9, −1/−2, CYB capped 1×/MS (gate alone) | 0.9% | 10.1% | 4.54 | 6.73 / 9 | 4.7 |

### Findings (lever battery)

- **The root cause is on-demand, reliable healing — not the numbers.** Smaller heals alone do
  **nothing** (players just rest more). Whatever the fix, the *max-9 + always-available + always-
  succeeds* combination is what has to give.
- **Lowering the pool is the dominant numeric lever.** Identical harsher misses give 22.6% danger
  at max 9 but **72.9%** at max 7 — teeth come from a *tight pool*, not heal size.

### Starforged analysis (the model we're emulating)

Starforged keeps recovery from being a free button with **four brakes at once**, all currently
*off* in Lights, Camera, Action!:

1. **Tiny pools** — Health/Spirit/Supply are each **0–5**, not 0–9.
2. **Fiction-gated** — you heal only via *Make Camp* (resting in the field) or *Sojourn* (while in
   a community); never "any safe lull, any time."
3. **Unreliable** — a missed Make Camp/Sojourn means **you recover nothing and Pay the Price.**
   (Note: it is *not* downward damage — Sojourn never lowers your health. This fits Ian's red line:
   a Miss means *the rest didn't take*, not *you lose Readiness*.)
4. **Opportunity cost** — on a hit you *choose* which track to restore, only +1/+2.

Lights, Camera, Action!'s broken state has all four off: pool 0–9, any-lull gating, guaranteed heal, no
choice. The key insight: **make the heal able to *whiff* (Miss recovers 0, never downward), and
limit how often it can be attempted.** That recreates "infrequent + unreliable," which is where
Starforged's tension lives.

**Starforged-informed battery** (Miss recovers 0; gate = max Mend per hero per
Milestone):

| Scenario | ≥1 OoA | danger% | min r | end r (pre) | CYB/Q |
|---|---|---|---|---|---|
| OLD (proven teeth, reference) | 9.7% | 49.9% | 3.95 | 4.80 / 9 | — |
| **SF-C — max 9 kept, gate 1×/MS, Miss → +0** | **8.6%** | 38.0% | **3.92** | 5.25 / 9 | 5.4 |
| SF-A — max 6, no gate, Miss → +0 | 12.7% | 87.3% | 2.19 | 4.73 / 6 | 9.5 |
| SF-E — max 6, gate 2×/MS, Miss → +0 | 17.6% | 87.6% | 2.11 | 4.35 / 6 | 8.8 |
| SF-B — max 5, no gate, Miss → +0 (full SF pool) | 33.7% | 96.8% | 1.62 | 3.93 / 5 | 18.3 |
| (G1) max 9, gate 1×/MS, *always heals* | 0.9% | 10.1% | 4.54 | 6.73 / 9 | 4.7 |

### Decision — SF-C ADOPTED (Ian, 2026-06-09)

- **✅ SF-C — ADOPTED and written into the book.** Keep max 9 and gentle −1/−2; **Mend** (the
  short-rest move) is gated to **once per hero per Milestone**, **lull-gated**, and a **Miss
  recovers *nothing*** ("no comfort") + the usual complication. Reproduces the old teeth almost
  exactly (OoA 8.6%, min r 3.92, end 5.25) with the *least* change to settled rules: **no pool
  change, no harsher misses.** Closest emulation of Starforged (infrequent + unreliable). It
  reverses the day-old "a Miss still heals +3" (now Miss = +0, but never downward — fits the red
  line). **Added 2026-06-09:** Mend may target **self or a teammate** (the cap is per *recipient*,
  so total healing is unchanged from the sim — it just gives a healer hero a job); Out of Action
  recovery is exempt from the gate but can whiff (gives OoA teeth too).
- **A′ (alternative, not taken): tight pool.** Drop max to 6, keep reliable heals (Mend +2/+3,
  partial), gentle −1/−2. OoA 6%, danger 82%. Teeth from a small pool instead of from unreliable
  healing; keeps the "always heals" promise intact but requires the broad max-9→6 change.
- **A′ (alternative): tight pool.** Drop max to 6, keep reliable heals (Mend +2/+3,
  partial), gentle −1/−2. OoA 6%, danger 82%. Teeth from a small pool instead of from unreliable
  healing; keeps the "always heals" promise intact but requires the broad max-9→6 change.
- **Avoid the extremes:** max 5 / double-stacking tight-pool + gate + whiff (SF-B, SF-D) overshoot
  into 30%+ OoA and constant resting — too punishing for ages 10+.
- **Downtime (Sojourn analog):** parallel choice — its Miss could likewise become "find no comfort"
  (reduced recovery) instead of full +6, but it's between-Story Arcs and not balance-critical; can stay
  generous.

*No change applied to the book yet — awaiting Ian's pick of SF-C vs A′ (and the Downtime call).*

> **SUPERSEDED (2026-06-06).** This per-Miss "trade" model was explored and rejected (it was a
> near-free safety button). The adopted design is in **§4b** (villain advances only on *fleeing
> a Challenge*), now canonical in the Master Reference §6/§7. This section is kept for the
> reasoning trail.

**Current rule (Master Reference §6):** advancing an Antagonist Track box is *layered on top*
of Pay the Price — **not** a substitute for the Readiness loss.

**Proposed change (Ian, 2026-06-06):** let players **trade** a Miss — skip the 2-Readiness
loss by advancing one Antagonist box instead. The track is short (Easy = 3), and filling it
loses the Story Arc, so the trade is meant to be self-limiting (~2 safe trades per Episode).
See memory `project_antagonist_track_open` and Master Reference §6 (🚧 note).

### Simulation (first pass — `sim_antagonist_trade.py`)

200k / 100k simulated Episodes, defaults from §3. **BASELINE** = Miss always costs
Readiness. **TRADE** = a hero may trade a threatened Miss (Readiness ≤ 4) for an Antagonist
box, per a stated policy. "OoA" = at least one hero hit 0 Readiness during the Story Arc.

| Scenario | Story Arc-loss | ≥1 hero OoA | Mean trades | Mean villain boxes | Mean end Readiness |
|---|---|---|---|---|---|
| **Baseline** (1 rest) | 0% | **9.7%** | — | — | 4.80 |
| **Trade — conservative** (keep 1-box margin) | 0% | **1.0%** | 0.45 | 0.45 / 3 | 5.09 |
| **Trade — no safety margin** | 3.5% | 0.2% | 0.49 | 0.49 / 3 | 5.10 |
| **Trade — aggressive** (trade at Readiness ≤ 6) | **19.4%** | 0.3% | 1.31 | 1.31 / 3 | 5.61 |
| Baseline — **no rest** | 0% | **31.6%** | — | — | 2.08 |
| Trade — **no rest**, conservative | 0% | 7.5% | 0.97 | 0.97 / 3 | 2.61 |

### What this says (preliminary)

- **The trade does not "run away."** Because the Antagonist Track is short and filling it
  loses the Story Arc, the option is self-limiting — players physically can't spam it. Good.
- **But played sensibly it is nearly a free "don't go down" button.** With a 1-box safety
  margin, the trade cuts Out-of-Action from ~9.7% to ~1% while advancing the villain only
  ~0.45 boxes — almost no story cost. It largely *removes* the Readiness/OoA tension rather
  than trading against it.
- **A real cost only appears with aggressive trading** (quest-loss climbs to ~19%). So under
  this design the "consequence" depends on player discipline, not on the math forcing it.
- **Rests dominate the baseline.** Out-of-Action swings 9.7% → 31.6% with zero rests, so the
  rest-frequency estimate (§3) is the single most important number to pin down.

### Levers if we want the trade to be a real dilemma (not yet decided)

- **Shorten the Antagonist Track** (e.g. Easy = 2 boxes → only ~1 safe trade) so each trade
  bites harder.
- **Cap trades per Story Arc** explicitly, or make the *first* trade cheap and later ones costlier.
- Or **keep the current "layered on top"** rule, which preserves OoA stakes outright.

> **Caveat.** First-pass model with the §3 estimates and a heuristic trade policy; rolls are
> treated as independent and the trade decision is simplified. Re-run after confirming party
> size, rest frequency, and a **target Out-of-Action rate** (what OoA% per Story Arc is "right"?
> — currently undefined and needed to call pass/fail).

---

## 4b. Revised proposal: villain advances on FLEE (recommended direction) — 🔁 SUPERSEDED by §0

> The flee-as-sole-trigger model with an equal-length Antagonist Track is replaced by the spine
> model (§0): the villain surges on a Recovery Scene, the track is short with a reserved climax
> box, and the antagonist track length no longer equals the Story Arc Track. Kept for the trail.

**Model (Ian, 2026-06-06).** Misses **always** cost Readiness (clean baseline — no per-Miss
trade). The Antagonist Track advances **only when the heroes flee a Challenge**: fleeing ends
the Challenge, its progress is lost, and the villain gains one box. Short track (Episode = 3)
makes it self-limiting; filling it loses the Story Arc (= "quit the Story Arc"). Script:
`sim_flee_retreat.py`.

> **Note (2026-06-08): this remains the modeled floor.** The Master Reference now also allows an
> *optional* Antagonist tick on a telling failure (via Pay the Price), and the new Season/Series
> scales. Neither is modeled here: the optional tick is table-discretionary (not automatic), so the
> flee-only numbers below are the **lower bound** on villain advance at Episode scale; tables that
> opt in will see villain boxes accrue somewhat faster. Season/Series tracks are longer (8/12) and
> advance mainly via the optional telling-failure tick (not per-Challenge flees), so they are far
> less sensitive to per-Challenge flee rate. Re-sim only if
> the optional tick is ever made automatic.

| Scenario (party 3, Easy) | Story Arc-loss | ≥1 hero OoA | Flees | Villain boxes | End Readiness |
|---|---|---|---|---|---|
| **Baseline, 1 rest** (no flee) | 0% | 9.6% | — | — | 4.80 |
| Flee @ Readiness ≤ 2, 1 rest | 0% | **6.3%** | 0.34 | 0.34 / 3 | 4.96 |
| **Flee @ Readiness ≤ 4, 1 rest** | 0% | **1.5%** | 1.10 | 1.10 / 3 | 5.41 |
| Flee ≤ 4 **+ rest also advances villain**, 1 rest | **30.9%** ⚠️ | 1.1% | 0.97 | 1.97 / 3 | 5.22 |
| Baseline, 0 rests (no flee) | 0% | 31.7% | — | — | 2.08 |
| Flee @ Readiness ≤ 4, 0 rests | 0% | 12.6% | 1.87 | 1.87 / 3 | 3.33 |

**Findings.**

- **It holds.** The flee valve is self-limiting and never loses a Story Arc under rational play
  (players keep a 1-box margin). Villain advances a visible but modest ~1 box per Story Arc — a
  *real* cost, unlike the near-free per-Miss trade in §4.
- **Tunable to "pretty low" OoA.** Fleeing at Readiness ≤ 4 with one rest lands **any-hero
  Out-of-Action at ~1.5% per Story Arc** — rare but not impossible (heroes can still go OoA on a
  regular roll, which has no flee option). That matches the "pretty low" target.
- **⚠️ Don't double-count the villain trigger.** If Recovery Scenes *also* advance the villain
  (the current Master Reference §7 rule) on this short track, Story Arc-loss spikes to **~31%** —
  the two triggers fight over a 3-box budget. **Recommendation: make fleeing the *sole*
  Antagonist-advance trigger** and drop "a Recovery Scene marks a villain box." Recovery's cost
  becomes purely tempo / world-pressure.
- **Rests still dominate** the baseline OoA rate; confirm rest frequency (§3).

**Recommended ruling (pending Ian's confirmation):** adopt the flee model; villain advances
only on flee; keep the Antagonist Track length = Story Arc Track (works fine here); add an official
**Quit the Story Arc** as the terminal flee. Misses go back to always costing Readiness.

---

## 4c. Start a Challenge opening roll (`sim_start_challenge.py`, 2026-06-09)

**Move under test.** A new **Progress move**, the twin of *Start a Story Arc*, rolled once when
heroes **deliberately initiate** a Challenge. A PbtA-style one-roll temporary modifier (a
**+1 to your next roll**), applied only to the **first hero roll** of that Challenge:

`2d6 + 1` (generative, Oracle's Blessing on doubles) — **Strong → +1 to that roll** ("you got the
drop") · **Weak → 0** (equal footing) · **Miss → −1 to that roll** ("they beat you to it").

With Oracle on, the opening tiers are Strong 33.3% / Weak 44.4% / Miss 22.2%, so the modifier is
**+1 33.3% / 0 44.4% / −1 22.2%** → net expectation **+0.11** to a single roll.

200k Episodes, §3 defaults, harness mirrors `sim_flee_retreat.py` (flee @ R≤4, 1 rest).
`danger%` = ≥1 hero pushed to Readiness ≤2.

| Config | anyOoA | danger% | min R | end R | villain | rolls/chal |
|---|---|---|---|---|---|---|
| Baseline (no Start a Challenge) | 1.45% | 27.4% | 3.11 | 5.42 | 1.10 | 2.97 |
| **+ Start a Challenge** | 1.47% | 27.1% | 3.13 | 5.44 | 1.08 | 2.98 |
| Baseline — stress (no flee/rest) | 31.8% | 89.8% | 0.81 | 2.08 | — | 3.44 |
| **+ Start a Challenge** — stress | 31.1% | 89.1% | 0.86 | 2.14 | — | 3.45 |

**Finding (✅ CLEARED for adoption, 2026-06-09).** Every metric moves <0.5pp — the move does
**not** materially change attrition, danger, pacing, or villain advance. It is a small,
mostly-flavor nudge, **slightly hero-favorable** (the generative `2d6+1` skews toward Strong, so
+1 outweighs −1). A one-roll temporary modifier never rescales the +2/+1 curve or the win-rate
targets — the same reason a PbtA "forward" doesn't break PbtA. Confirms a temporary ±1 to a single
roll is a safe,
reusable lever for small situational swings (distinct from the "never bigger numbers" rule, which
governs *permanent* advancement). Script: `sim_start_challenge.py`.

---

## 5. Reproducing / re-running

Scripts (in this folder): **`sim_spine.py` (§0 — the canonical model)**; `sim_antag_heal.py` and
`sim_antag_fill.py` (the exploration that led to §0); and the superseded `sim_antagonist_trade.py`
(§4), `sim_flee_retreat.py` (§4b), `sim_recovery.py` (§3a), `sim_start_challenge.py` (§4c). All assumptions are constants at the
top; edit and re-run (`python3 sim_<name>.py`). Update the relevant section's table when
parameters change, and bump the "Last updated" date.
