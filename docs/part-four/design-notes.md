# Design Notes

*Why the rules work the way they do.*

You don't need any of this to play. *Lights, Camera, Action!* is built so the rules in Parts One through Three stand on their own — read them, and you're ready.

This page is for two kinds of reader. The first is the design nerd who just wants to know *why* a rule is shaped the way it is — the thinking under the hood. The second is the tinkerer who wants to change something. If you're going to bend a rule, it helps to know what it was holding up: most of these choices are load-bearing, propping up something a few pages away, and the notes below say what. Tweak with that in mind and your house rules will hold together.

Each note names the chapter whose rule it explains.

---

## Why a Stat Layer *and* an Asset Layer

*(Chapter 7 — The Roll)*

The roll is **2d6 + 0 / +1 / +2**, and the modifier comes from two separate layers: your **two Stats** (one of the closed five — Strong, Quick, Clever, Sneaky, Charming) and your **three Assets** (specific signature talents, tools, friends). You get **+1** if the relevant Stat is one of yours, **+1** if an Asset applies, **+2** if both, **+0** if neither. The numbers aren't arbitrary; they're tuned around the 2d6 curve and the Readiness cap of 9.

That split is the whole point, and it came out of a problem with the *old* model. Originally a hero had four Assets and the first was a broad "Attribute," and the roll was just +2 (an Asset applies) or +1 (anything else). The trouble: players could argue almost any of four Assets into fitting almost any action, so **+2 was near-universal** — the +1 "floor" almost never came up, and being out of your element stopped meaning anything. The dice flattened.

The fix is to make one layer **objective** instead of argued. Which Stat an action calls for is decided by *what the action calls for*, not by a clever sentence — a chase is **Quick**, a feat of force is **Strong**, recalling a fact is **Clever**, and so on. The five Stats partition the action-space the way Starforged's stat list does, so "which is most relevant" is honest. Your three Assets stay flexible (you still argue those, with the one-sentence test). Now a roll only reaches +2 when *both* an honest Stat **and** a fitting Asset line up — and the floor returns for real.

Here's roughly what the dice do across that spread, weighted for how often each modifier actually comes up in play (Stats apply ~55% of the time, Assets ~85%), the **average modifier lands near +1.40:**

- **At +2 (Stat and Asset both fit — your wheelhouse):** roughly **42% Strong Hit, 42% Weak Hit, 17% Miss** — about an **83% hit rate.** Heroes mostly succeed, the story flows.
- **At +1 (one layer fits):** roughly **28% Strong, 44% Weak, 28% Miss** — about a **72% hit rate.** Likely, but with real risk and far more complications.
- **At +0 (out of your element — neither fits):** roughly **17% Strong, 42% Weak, 42% Miss** — about a **58% hit rate.** You can always *try*, but it's a real gamble. This is the new floor, and bringing it back is exactly what restores the tension the old always-+2 model had bled out.

Doubles (Oracle's Blessing) nudge every result a little brighter on top of this, which is part of why the baseline numbers sit where they do.

---

## No Enemy Stats, No Death

*(Chapter 8 — Challenges)*

*Lights, Camera, Action!* gives enemies and obstacles **no Readiness, no stats, and no hit points.** Only the heroes track a number. You overcome a foe or a hazard by **filling its Challenge Track** — mechanically, *the track is the enemy.* And **heroes cannot die.** The worst that can happen is going **Out of Action** (recoverable — Chapter 9) or **losing the Story Arc** (the Antagonist Track fills — Chapter 10). Setbacks cost Readiness and story ground; never a character's life.

This is a deliberate choice in service of the "write a movie together" philosophy, and it does a lot of quiet work:

- **It keeps the spotlight on the heroes.** The interesting number on the table is *your* Readiness — your hero's wear and tear — not an enemy's stat block. The drama is about how much the heroes are willing to spend, not bookkeeping for the monster.
- **It makes any opposition trivial to "run."** A dragon, a snowstorm, a hostile crowd, and a ticking countdown are mechanically identical: a row of boxes. The Guide (or group) never needs to stat anything. That's what makes zero-prep possible.
- **It protects the story.** Because heroes can't die, players can throw themselves at dramatic risks without fear of a sudden, story-ending death. The stakes are still real — losing Readiness hurts, going Out of Action sidelines you, losing a Story Arc stings — but they're the kind of stakes a movie is built on: setbacks, costs, and comebacks, not a dead-end.

If you're coming from a game where defeating things means grinding down their HP, this will feel light. That lightness is the point.

---

## The Antagonist Track: A Reserved-Climax Story Arc Clock

*(Chapters 8, 9 & 10 — the Recovery Scene and the Antagonist Track)*

The Antagonist Track is a "story clock" in the tradition of *Monster of the Week* and *Blades in the Dark* — a visible counter for the villain's progress. But this one is built around a single goal: **the best ending is the villain *one step from winning* at the climax** (the photo-finish). Three choices get it there:

- **Its top box is the reserved climax.** Lower boxes fill during play; the final box is taken only at the **Showdown** (or by a hero going Out of Action). That's what *guarantees* the near-miss instead of leaving it to luck: the track is built to fill *up to* one-from-full and stop, so the heroes arrive at the finale with the villain at the door. Emergent clocks scatter — this one is engineered to land.
- **It surges when the heroes fall back to regroup.** The Antagonist Track advances one box per **Recovery Scene** — recovery you can rely on, ground you give up. Tying the villain's advance to *healing* (rather than a per-roll trade or a flat doom timer) is the whole engine: every breather hands the villain a box, so the quiet/character scenes are where the stakes climb. A small **Mend** lets you patch up *without* surging — that's a tactical choice, not a clock-dodge, which is why it's risky (a Miss costs Readiness) and can't revive a downed hero. Validated in the simulation reference: a fresh party loses an all-Medium **Episode** ~6% of the time and a **Movie** ~16%; as heroes pick up Boons the Movie settles toward ~10% — comfortably inside the win-nine-of-ten goal, with the photo-finish the common ending.
- **It's core, not optional, and Out of Action is the loss vector.** Heroes can't die — so the danger isn't death, it's the clock. A knocked-out hero *forces* a regroup, whose Surge can fill the reserved climax box and lose the Story Arc before the finale. That's what keeps Readiness meaningful: it's ammunition against the villain's clock, not a survival meter.

---

## Why Recovery Costs the Villain Ground

*(Chapter 9 — Readiness)*

The hard design problem with healing is simple: **if heroes can patch up to full whenever they like, nothing else has teeth.** Pay the Price stops mattering, low Readiness stops being scary, and Out of Action becomes a revolving door. An early version made recovery a flat, automatic +3 at any safe lull — and the danger never accumulated.

The fix isn't to make healing *unreliable* — it's to make it *cost the right thing.* The big recovery (the **Recovery Scene**) is fully reliable: fall back and the whole party comes all the way back up to 9. What it costs is **a Surge on the Antagonist Track** — the villain gains ground while you regroup. So recovery is never a free button; it's a trade against the one clock that can end the Story Arc. That's where the teeth moved: from *will the heal work?* to *can we afford to take it?* The rising pressure of a Story Arc lives entirely in that clock — every regroup hands the villain a box, so the closer the heroes get to the finale, the less slack they have left to spend.

> **One mechanic I cut: the "declining ceiling."** An earlier draft had each Recovery Scene heal you a little *less* — a Readiness max that started at 9 and dropped a point per regroup. The idea was to add a second source of rising pressure. In practice it always felt too harsh: it punished the very move it was named for, and it broke the two story sizes. Attrition naturally compounds with length, so a sinking ceiling that's tuned to feel fair across a short **Episode** crushes a longer **Movie**, and one tuned for the Movie barely registers in the Episode. Letting the Surge clock carry *all* the rising pressure — and tuning the two sizes' Antagonist Tracks individually instead — does the same job without the cruelty or the scaling break. Recovery is now simply: fall back, come back to full.

The small **Mend** is the counterweight that keeps Challenges interesting: a quick, risky patch you can take *instead of* pushing the scene. It doesn't surge the villain (so it's not a clock-dodge), but it has a real cost — a **Miss takes 1 Readiness**, and at low Readiness that can knock you Out of Action — so you can't just spam it to limp along. And it can't revive a downed hero: only a full regroup does that, which preserves Out of Action as the loss vector. Two recovery moves, two different decisions — exactly the kind of choice a deliberately light game wants on the table.

---

## Why Growth Is Horizontal

*(Chapter 13 — Growing Your Heroes)*

Most games grow heroes *upward* — bigger numbers, higher bonuses, more health. *Lights, Camera, Action!* deliberately doesn't, and the payoff is worth understanding.

When heroes only get **bigger numbers**, the game has to keep handing the *enemies* bigger numbers too, just to stay tense — an endless arms race that's a lot of bookkeeping and easy to get wrong. This game sidesteps the whole problem. Because Growth only ever adds **tools and signature moves** — never a better roll — the math never moves:

- The roll is always **2d6 + 0 / +1 / +2** (a Stat fits, an Asset fits, both, or neither). Growth never changes those modifiers.
- **Readiness** is always capped at **9**.
- So a **Challenge Track**, an **Antagonist Track**, or a **Story Arc** that was the right difficulty in Episode One is *still* the right difficulty in the season finale. **You never rescale anything.**

A veteran hero isn't a hero who *rolls better than a beginner.* They're a hero with more Assets to be +2 in more situations, and a fistful of signature moves to pull out when it matters. They feel powerful because they have more *answers* — more ways to make a scene go their way — not because the dice love them more.

> **One option I cut.** Early on I considered a Boon called *"Widen the Domain"* that would broaden an Asset so it earned its +2 in more situations. I dropped it: it was the one upgrade that quietly nudged the numbers (more +2 rolls), reintroducing the very "Lucky / good at everything" problem the Stat-and-Asset split guards against. And its appeal — broader coverage — is already covered by simply buying a **New Asset.** Keeping *every* form of growth horizontal is what makes the no-rescaling promise hold.
