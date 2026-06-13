# Design Notes

*Why the rules work the way they do.*

You don't need any of this to play. *Lights, Camera, Action!* is built so the rules in Parts One through Three stand on their own — read them, and you're ready.

This page is for two kinds of reader. The first is the design nerd who just wants to know *why* a rule is shaped the way it is — the thinking under the hood. The second is the tinkerer who wants to change something. If you're going to bend a rule, it helps to know what it was holding up: most of these choices are load-bearing, propping up something a few pages away, and the notes below say what. Tweak with that in mind and your house rules will hold together.

Each note names the chapter whose rule it explains.

---

## Why +2 / +1 Instead of Stats

*(Chapter 7 — The Roll)*

Most games separate raw ability (a stat like Strength) from special tricks (a feat or spell). *Lights, Camera, Action!* collapses both into your four Assets — they *are* your stats and your special moves at once. That's why there are only two modifiers, and why the gap between them is exactly one point. The numbers aren't arbitrary; they're tuned around the 2d6 curve and the Readiness cap of 9.

Here's what the dice actually do:

- **At +2 (acting in your wheelhouse — the common case):** roughly **42% Strong Hit, 42% Weak Hit, 17% Miss.** That's about an **83% hit rate** — heroes mostly succeed, which keeps the story flowing and the momentum up.
- **At +1 (out of your wheelhouse):** roughly **28% Strong, 44% Weak, 28% Miss** — about a **72% hit rate.** Still likely to succeed, but with real risk and far more complications.

Two design choices fall out of this. First, the floor is **+1, not +0:** a +0 option would make off-Asset actions feel hopeless and punish players for stepping outside their niche, which is the opposite of the cinematic, everyone-can-try feel I want. The +1 floor keeps a hero capable at anything. Second, the jump from +1 to +2 nearly **doubles your Strong-Hit rate** (28% → 42%) while barely moving your overall hit rate — so your Assets are clearly, tangibly worth having (you fail *cleanly* far more often in your wheelhouse) without ever making off-Asset actions feel like a wall. Because your four Assets cover your hero's whole zone of competence, most rolls in actual play land at +2.

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
- **It surges when the heroes fall back to regroup.** The Antagonist Track advances one box per **Recovery Scene** — recovery you can rely on, ground you give up. Tying the villain's advance to *healing* (rather than a per-roll trade or a flat doom timer) is the whole engine: every breather hands the villain a box, so the quiet/character scenes are where the stakes climb. A small **Mend** lets you patch up *without* surging — that's a tactical choice, not a clock-dodge, which is why it's risky (a Miss costs Readiness) and can't revive a downed hero. Validated in the simulation reference: photo-finish ~93%+, real losses rare (~1–6%).
- **It's core, not optional, and Out of Action is the loss vector.** Heroes can't die — so the danger isn't death, it's the clock. A knocked-out hero *forces* a regroup, whose Surge can fill the reserved climax box and lose the Story Arc before the finale. That's what keeps Readiness meaningful: it's ammunition against the villain's clock, not a survival meter.

---

## Why Recovery Costs the Villain Ground

*(Chapter 9 — Readiness)*

The hard design problem with healing is simple: **if heroes can patch up to full whenever they like, nothing else has teeth.** Pay the Price stops mattering, low Readiness stops being scary, and Out of Action becomes a revolving door. An early version made recovery a flat, automatic +3 at any safe lull — and the danger never accumulated.

The fix isn't to make healing *unreliable* — it's to make it *cost the right thing.* The big recovery (the **Recovery Scene**) is fully reliable: fall back and the whole party comes back up. What it costs is **a Surge on the Antagonist Track** — the villain gains ground while you regroup. So recovery is never a free button; it's a trade against the one clock that can end the Story Arc. That's where the teeth moved: from *will the heal work?* to *can we afford to take it?*

**And a Recovery Scene heals you a little less each time.** Your Readiness max starts at 9 and drops by 1 with every regroup (floor 4), resetting only at Downtime. This is the **ratchet** that gives a Story Arc its rising pressure: the first time you fall back you come back to 8, then 7, then 6 — recovery never bails you out the way it did last time, so the longer a Story Arc runs the more it tightens, pushing the heroes to reach the climax before they're worn too thin. It's also why **length lives in *chaining* Story Arcs, not bloating one:** each Story Arc is a self-contained tension curve that resets at Downtime, so a Season or Series gets a fresh ceiling every Episode/Movie — the ratchet only bites *within* a single arc, never across the campaign. (A table that *wants* a grinding campaign can let the ceiling carry between arcs — a natural hard-mode dial.)

The small **Mend** is the counterweight that keeps Challenges interesting: a quick, risky patch you can take *instead of* pushing the scene. It doesn't surge the villain (so it's not a clock-dodge), but it has a real cost — a **Miss takes 1 Readiness**, and at low Readiness that can knock you Out of Action — so you can't just spam it to limp along. And it can't revive a downed hero: only a full regroup does that, which preserves Out of Action as the loss vector. Two recovery moves, two different decisions — exactly the kind of choice a deliberately light game wants on the table.

---

## Why Growth Is Horizontal

*(Chapter 13 — Growing Your Heroes)*

Most games grow heroes *upward* — bigger numbers, higher bonuses, more health. *Lights, Camera, Action!* deliberately doesn't, and the payoff is worth understanding.

When heroes only get **bigger numbers**, the game has to keep handing the *enemies* bigger numbers too, just to stay tense — an endless arms race that's a lot of bookkeeping and easy to get wrong. This game sidesteps the whole problem. Because Growth only ever adds **tools and signature moves** — never a better roll — the math never moves:

- The roll is always **2d6 +2** (an Asset applies) or **+1** (anything else).
- **Readiness** is always capped at **9**.
- So a **Challenge Track**, an **Antagonist Track**, or a **Story Arc** that was the right difficulty in Episode One is *still* the right difficulty in the season finale. **You never rescale anything.**

A veteran hero isn't a hero who *rolls better than a beginner.* They're a hero with more Assets to be +2 in more situations, and a fistful of signature moves to pull out when it matters. They feel powerful because they have more *answers* — more ways to make a scene go their way — not because the dice love them more.

> **One option I cut.** Early on I considered a Boon called *"Widen the Domain"* that would broaden an Asset so it earned its +2 in more situations. I dropped it: it was the one upgrade that quietly nudged the numbers (more +2 rolls), reintroducing the very "Lucky / good at everything" problem the Asset rules guard against. And its appeal — broader coverage — is already covered by simply buying a **New Asset.** Keeping *every* form of growth horizontal is what makes the no-rescaling promise hold. *(This is also why your **Attribute** is capped at one: a single broad Asset, fixed at creation and with whole categories it can't touch, barely moves the math — but letting heroes stack more broad coverage would be exactly the creep I cut. One is a feature; two is power-creep.)*
