# Design Notes

*Why the rules work the way they do.*

You don't need any of this to play. *Amazing Forge* is built so the rules in Parts One through Three stand on their own — read them, and you're ready.

This page is for two kinds of reader. The first is the design nerd who just wants to know *why* a rule is shaped the way it is — the thinking under the hood. The second is the tinkerer who wants to change something. If you're going to bend a rule, it helps to know what it was holding up: most of these choices are load-bearing, propping up something a few pages away, and the notes below say what. Tweak with that in mind and your house rules will hold together.

Each note names the chapter whose rule it explains.

---

## Why +2 / +1 Instead of Stats

*(Chapter 7 — The Roll)*

Most games separate raw ability (a stat like Strength) from special tricks (a feat or spell). Amazing Forge collapses both into your four Assets — they *are* your stats and your special moves at once. That's why there are only two modifiers, and why the gap between them is exactly one point. The numbers aren't arbitrary; they're tuned around the 2d6 curve and the Readiness cap of 9.

Here's what the dice actually do:

- **At +2 (acting in your wheelhouse — the common case):** roughly **42% Strong Hit, 42% Weak Hit, 17% Miss.** That's about an **83% hit rate** — heroes mostly succeed, which keeps the story flowing and feels great for kids.
- **At +1 (out of your wheelhouse):** roughly **28% Strong, 44% Weak, 28% Miss** — about a **72% hit rate.** Still likely to succeed, but with real risk and far more complications.

Two design choices fall out of this. First, the floor is **+1, not +0:** a +0 option would make off-Asset actions feel hopeless and punish players for stepping outside their niche, which is the opposite of the cinematic, everyone-can-try feel we want. The +1 floor keeps a hero capable at anything. Second, the jump from +1 to +2 nearly **doubles your Strong-Hit rate** (28% → 42%) while barely moving your overall hit rate — so your Assets are clearly, tangibly worth having (you fail *cleanly* far more often in your wheelhouse) without ever making off-Asset actions feel like a wall. Because your four Assets cover your hero's whole zone of competence, most rolls in actual play land at +2.

Doubles (Oracle's Blessing) nudge every result a little brighter on top of this, which is part of why the baseline numbers sit where they do.

---

## No Enemy Stats, No Death

*(Chapter 8 — Challenges)*

Amazing Forge gives enemies and obstacles **no Readiness, no stats, and no hit points.** Only the heroes track a number. You overcome a foe or a hazard by **filling its Challenge Track** — mechanically, *the track is the enemy.* And **heroes cannot die.** The worst that can happen is going **Out of Action** (recoverable — Chapter 9) or **losing the Quest** (the Antagonist Track fills — Chapter 10). Setbacks cost Readiness and story ground; never a character's life.

This is a deliberate choice in service of the "write a movie together" philosophy, and it does a lot of quiet work:

- **It keeps the spotlight on the heroes.** The interesting number on the table is *your* Readiness — your hero's wear and tear — not an enemy's stat block. The drama is about how much the heroes are willing to spend, not bookkeeping for the monster.
- **It makes any opposition trivial to "run."** A dragon, a snowstorm, a hostile crowd, and a ticking countdown are mechanically identical: a row of boxes. The Guide (or group) never needs to stat anything. That's what makes zero-prep possible.
- **It protects the story.** Because heroes can't die, players can throw themselves at dramatic risks without fear of a sudden, story-ending death. The stakes are still real — losing Readiness hurts, going Out of Action sidelines you, losing a Quest stings — but they're the kind of stakes a movie is built on: setbacks, costs, and comebacks, not a dead-end.

If you're coming from a game where defeating things means grinding down their HP, this will feel light. That lightness is the point.

---

## The Antagonist Track: A Deliberate Story Clock

*(Chapters 8 & 10 — Fleeing and the Antagonist Track)*

The Antagonist Track is a "story clock" in the tradition of games like *Monster of the Week* and *Blades in the Dark* — a visible counter that turns the antagonist's progress into something the whole table can see and feel. Three choices make it work the way it does:

- **It advances mainly when you flee.** Tying the villain's advance to fleeing — rather than to a per-roll trade — keeps it from being a cheap "don't go down" button: a retreat always costs you the scene's progress *and* a box, so players only do it when staying is genuinely worse. Balance was modeled in the simulation reference; it keeps Out-of-Action rare while making the Antagonist Track a meaningful, self-limiting clock.
- **It's deliberate, not automatic.** The track never lurches forward on a single unlucky roll. It moves when the *table* decides the antagonist gained ground — reliably when the heroes flee, and otherwise only when a telling failure clearly hands the bad guys an opening. Tying it to group judgment rather than to bad dice keeps it from feeling like random punishment and gives the heroes ownership of their fate. You lose because the story turned against you, beat by beat — not because the dice piled up.
- **It's core, not optional.** Earlier drafts made it an opt-in module. But the whole stay-alive design — heroes can't die, so they flee instead — depends on there being a track to advance when they do. Without it, fleeing would have no cost and losing would have no meaning. So every Quest draws one.

---

## Why Recovery Is Rolled, Gated, and Can Whiff

*(Chapter 9 — Readiness)*

The hard design problem with healing is simple: **if heroes can patch up to full whenever they like, nothing else has teeth.** Pay the Price stops mattering, low Readiness stops being scary, and Out of Action becomes a revolving door. An early version of this game made recovery a flat, automatic +3 you could take at any safe lull — and that's exactly what happened: the danger never accumulated.

The fix borrows from the games this one sits between. Recovery isn't a button; it's **infrequent and unreliable** — Mend is limited to once per hero per Milestone and can come up empty on a Miss. That means a hard stretch genuinely wears the party down, fleeing and Out of Action stay real possibilities, and a battered party has to *decide* who gets patched up and when. The teeth are back. (Letting Mend target a teammate, rather than only yourself, is a deliberate counterweight: it gives a healer hero a real job without lifting the per-hero cap.)

But notice the one line we never cross: **a bad recovery roll never takes Readiness away.** Punishing a failed heal with *more* damage — spiraling the hero who most needs help — is backwards and unfun. A Miss means the rest *didn't take* (you're no better off) and the world presses in — never that healing wounded you. So recovery carries real weight and real disappointment without ever being a trap. And because the heals are small and capped at **9**, even a good rest patches you up without wiping the slate clean: your choices accumulate across the adventure rather than resetting each time you stop.

---

## Why Growth Is Horizontal

*(Chapter 13 — Growing Your Heroes)*

Most games grow heroes *upward* — bigger numbers, higher bonuses, more health. *Amazing Forge* deliberately doesn't, and the payoff is worth understanding.

When heroes only get **bigger numbers**, the game has to keep handing the *enemies* bigger numbers too, just to stay tense — an endless arms race that's a lot of bookkeeping and easy to get wrong. This game sidesteps the whole problem. Because Growth only ever adds **tools and signature moves** — never a better roll — the math never moves:

- The roll is always **2d6 +2** (an Asset applies) or **+1** (anything else).
- **Readiness** is always capped at **9**.
- So a **Challenge Track**, an **Antagonist Track**, or a **Quest** that was the right difficulty in Episode One is *still* the right difficulty in the season finale. **You never rescale anything.**

A campaign veteran isn't a hero who *rolls better than a beginner.* They're a hero with more Assets to be +2 in more situations, and a fistful of signature moves to pull out when it matters. They feel powerful because they have more *answers* — more ways to make a scene go their way — not because the dice love them more.

> **One option we cut.** Early on we considered a Boon called *"Widen the Domain"* that would broaden an Asset so it earned its +2 in more situations. We dropped it: it was the one upgrade that quietly nudged the numbers (more +2 rolls), reintroducing the very "Lucky / good at everything" problem the Asset rules guard against. And its appeal — broader coverage — is already covered by simply buying a **New Asset.** Keeping *every* form of growth horizontal is what makes the no-rescaling promise hold.
