> **⚙️ Designer reference — work in progress, published temporarily for review.** The *playable game* is Parts One–Three; this is the behind-the-scenes spec. It includes decision history and some sections marked **SUPERSEDED** (kept only as a reasoning trail — not current rules).

---

# Lights, Camera, Action! — Core Mechanics Master Reference

> **Purpose of this document.** This is the canonical source of truth for the core
> mechanics of *Lights, Camera, Action!*. It is a **reference for writing the rest of the book**,
> not a chapter of the book itself. It merges everything from the source drafts so no
> rule is lost.
>
> **Authority order.** **V5 is the most recent and authoritative draft.** Where V5
> conflicts with V3 or V4, V5 wins. V3/V4 are retained only where they contain content
> V5 dropped, or where Ian has made a separate decision (see flags).
>
> **How to read the flags.**
> - `✅ DECIDED` — a question Ian has resolved; treat as canonical.
> - `🚧 OPEN` — an unresolved design question; do **not** fill it in from old drafts.
> - `⚠️ NOTE` — a difference between drafts worth knowing, minor or already resolved by V5.
>
> **This doc is also the vocabulary authority.** The Standard Vocabulary table below is the
> canonical word list for the whole book. When writing or reviewing any chapter, match
> these exact terms and capitalization; flag deviations.
>
> **Source drafts:** `Amazing Forged Rules V5.pdf` (authoritative),
> `Amazing Forged Core Rules V4.pdf`, `Amazing Forged Core Rules V3.pdf`
> **Last reconciled:** 2026-06-05

---

## 0. What Lights, Camera, Action! Is

*Lights, Camera, Action!* is a cinematic, zero-prep TTRPG engine for adventures with kids
(ages 8–12). It is a hack that merges the absolute freedom of character creation from
**Amazing Tales** (by Martin Lloyd) with the high-tension, mechanically decisive pacing
of **Ironsworn: Starforged** (by Shawn Tomkin). It is designed to be played *in media
res* with zero preparation.

The engine is **genre- and setting-agnostic.** Because the mechanics focus on narrative
tension and dramatic pacing rather than simulation-heavy combat stats or specific spell
lists, the same rules tell any kind of story: high-octane sci-fi action, a spooky
mystery, a survival thriller, or a cozy modern-day small-town drama. Whatever the central
tension is, you track its progress with **Story Arcs, Milestones, and Challenges.**

---

## Standard Vocabulary (Canonical Terms)

This is the authoritative word list. Use these terms and this capitalization everywhere in
the book. When reviewing a chapter, treat any deviation as an error to flag.

| Canonical term | Use it for | Do **not** use |
|---|---|---|
| **Guide** | The person running the game (director + oracle). | GM, Game Master, DM, Referee |
| **Co-op play** | Solo or cooperative play with no Guide. | GMless, Guideless |
| **Guided play** | Play with a Guide. | GM'd play, refereed play |
| **player** | A person controlling a hero. | — |
| **character / hero** | A player's in-fiction persona. | PC |
| **Concept** | The "movie poster" pitch for a character. | backstory (as the mechanic) |
| **Asset** | One of a character's four "amazing at" things (+2). | skill, stat, trait |
| **Attribute** | The one broad, stat-like Asset every hero picks first, from a closed list of five — **Strong, Quick, Clever, Sneaky, Charming**. A normal Asset (+2 when it fits), capped at one per hero. | stat, ability score, the five-as-separate-stats |
| **Broken Asset** | An Asset knocked offline when a hero goes Out of Action — gives no +2 (rolls fall to +1) until **Downtime** restores it. Temporary; never a penalty. | negative Asset, debuff, condition, impact |
| **Readiness** | The single 0–9 resource track (health + morale + supplies). Its **max declines within a Story Arc** — see Readiness max. | HP, health, hit points, stamina |
| **Readiness max** | The current recovery ceiling. Starts at **9**; **drops 1 with each Recovery Scene** (floor 4); resets to 9 at **Downtime**. Recovery (Mend or Recovery Scene) can't exceed it. The "ratchet" that makes a Story Arc tighten as it runs. | — |
| **Mend** | The small, risky **any-scene** patch (in a Challenge, it's your turn instead of a Challenge Roll): recover a little — self or ally, rolled **Strong +3 / Weak +2 / Miss −1 Readiness** (up to the current max). **No cap; does not surge the villain; can't revive Out of Action.** The −1 risk + the declining ceiling (it only heals to the current max) keep it from substituting for a regroup. | heal, Catch Your Breath |
| **Recovery Scene** | The fall-back-and-regroup move: the party recovers **up to its current Readiness max** — and in return the **Antagonist Track surges one box** *and* the **Readiness max drops by 1.** Reliable; the weighty quiet/B-plot beat. | rest, healing |
| **Downtime** | The between-Story-Arcs rest: resets the **Readiness max to 9**, heals everyone to full, **restores any Broken Asset**. No Surge. | long rest, Sojourn, victory bump |
| **Out of Action** | State when Readiness hits 0. | dead, KO'd, defeated |
| **Story / Story Arc** | One spine — a single central dramatic question — tracked with a **Story Arc Track** (progress) and an **Antagonist Track** (the villain's clock). Sized **Episode** or **Movie** (the only two with box machinery). | Quest, mission, adventure |
| **Episode** | A complete short Story — **3 Milestones, 2-box Antagonist Track** — told in ~one sitting. | one-shot, session quest |
| **Movie** | A complete feature Story — **6 Milestones, 3-box Antagonist Track** — told over ~2–3 sessions. | feature film |
| **Season** | A **collection** pattern (prose, no machinery): a run of Stories sharing a throughline. Not a box size. | arc (as the term), story arc |
| **Series** | A **collection** pattern (prose): the whole game, a run of Seasons. Always a collection; no box size of its own. | campaign, saga |
| **Story Arc Track** | A Story's progress track — one box per Milestone; filling it reaches the Showdown. | Hero Track, Quest Track |
| **Antagonist Track** | The losing side of the same Story: a **short** track whose **top box is the reserved climax (the Showdown)**. Lower boxes **surge** when the heroes take a Recovery Scene; filling the top box loses the Story. | enemy clock, doom track |
| **The Surge** | The villain advance played out when a Recovery Scene fills an Antagonist box. | — |
| **Showdown** | The climax — reached when the heroes fill the Story Arc Track; the reserved top Antagonist box. The Story's outcome is decided here. | finale, boss fight |
| **Thread (B-plot)** | A subplot/character arc riding alongside the spine: a light progress track, **no Antagonist Track / no lose-clock**; resolves into or beside the spine's climax. | side quest, B-arc |
| **Fall back** | Retreating from a losing Challenge (losing its progress) to regroup — handled as a **Recovery Scene** (full heal + Surge). | Flee, retreat (as the mechanic) |
| **Quit the Story Arc** | Giving up a Story entirely — the terminal fall back; the bad guys win. | forfeit, surrender |
| **Start a Story Arc** | The opening roll made once when a Story Arc begins (2d6 + 1, **generative** — no failure): sets how it opens — *Clear purpose* / *More questions than answers* / *Trouble finds you first*. | Swear an Iron Vow |
| **Milestone** | A chapter of the story (a collection of Scenes); checks one Story Arc Track box. Every 3rd Milestone earns each hero 1 Growth. | objective, step |
| **Scene** | A single beat of play — one or a few Regular Rolls, or a full Challenge. Milestones are made of Scenes. | — |
| **Challenge** | An active multi-roll obstacle + its track. | encounter, scene (as a mechanic) |
| **Challenge Track** | The box row you fill during a Challenge. | — |
| **Regular Roll** | A one-off 2d6 roll with no track. | simple roll |
| **Challenge Roll** | A 2d6 roll that marks Challenge progress. | — |
| **Progress** | What you mark on a track. | points, XP |
| **Pay the Price** | The complication that follows a Weak Hit/Miss. | penalty, damage |
| **Strong Hit / Weak Hit / Miss** | The three roll outcomes. | success/partial/fail |
| **Oracle's Blessing** | The doubles-upgrade rule. | crit, critical |
| **Outstanding Success** | Doubles on a Strong Hit. | crit success |
| **Ask the Oracle** | The stuck-point move for deciding what happens next. | — |
| **Story Spark** | The small d6 idea table inside Ask the Oracle. | oracle table |
| **Ask the Dice** | The 1d6 yes/no oracle. | — |
| **Move** | Any defined procedure you invoke at the table. Every move is an **Action**, **Progress**, or **Frame move**. | maneuver, action (as the mechanic) |
| **Action move** | A move that *resolves a hero's attempt* — rolled 2d6 + 2/+1 and read Strong/Weak/Miss; the dice **adjudicate** (did you pull it off?). | — |
| **Progress move** | A move that *opens or closes a progress track* (a Story Arc or a Challenge). The openers (Start a Story Arc, Start a Challenge) roll generatively to set how things begin; the closers (Fall back, Quit the Story Arc) are deterministic. | — |
| **Frame move** | A move that *shifts the fiction in the moment* (no track); when it rolls, the dice **generate** a direction rather than judge a hero, so it can never be "failed." | framing move, GM move |
| **Growth** | The advancement currency; earn 1 every 3 Milestones, spend on Boons/Assets. | XP, experience, levels |
| **Growth Track** | The per-hero row of boxes tracking earned Growth. | — |
| **Boon** | A once-per-Scene/Session signature move bought (2 Growth) onto an Asset card. | perk, feat, ability |
| **Trade In** | Retiring an Asset to make room for a new one at the 6-Asset ceiling. | — |
| **Genre** | The mood/feeling of the story — Worldbuilding Question 1. One of six official genres. | theme; a *setting* used as the genre |
| **the six genres** | The official set: **Adventure, Mystery, Horror, Sci-Fi, Caper, Drama.** | inventing alternate names for these |
| **Caper** | The official genre for clever, stylish heist/con stories (the heist *tone*). | Heist (as the genre name) |
| **Drama** | The official genre for juicy interpersonal stories (gossip, rivalry, love, stress). | Cozy Drama, Slice-of-Life |
| **tonal dial** | The playful↔serious scale every genre runs on; set per table. | tone slider, intensity setting |
| **Genre Kit** | A per-genre toolkit (Ch. 15): the feel, Worldbuilding prompts, archetypes, d100 Assets. | Starter Backdrop |

> ✅ **DECIDED — "Guide," not "GM."** Ian confirmed (2026-06-05) the facilitator role is
> the **Guide** throughout, because it fits the kid-friendly, collaborative tone. All "GM"
> / "Game Master" wording from the V4/V5 drafts is superseded.

> ✅ **DECIDED — "Co-op play."** Ian confirmed (2026-06-05) that play without a Guide is
> called **"Co-op play"** (not "GMless" from the drafts, nor the interim "Guideless").

> ✅ **DECIDED — six genres + tonal dial (2026-06-09).** *Lights, Camera, Action!* officially supports
> **six genres — Adventure, Mystery, Horror, Sci-Fi, Caper, Drama —** each playable along a
> **playful↔serious tonal dial.** "Caper" is the heist *tone* (never "Heist" as the name);
> "Drama" is the juicy interpersonal kind (never "cozy drama"). Genre is Worldbuilding Q1; each
> genre has a **Genre Kit** in Ch. 15 (which replaced the old "Starter Backdrops" idea). A kit
> describes a *setting* (standing conditions), never a prescribed *Story Arc*.

---

## 1. Core Principles

1. **Think Like a Movie, Not a Game.** If there isn't an active threat or an obvious
   next step, don't roll. Cut straight to the next exciting scene.
2. **Zero Prep.** Do not write modules or plan encounters. Agree on a starting scenario
   as a group, draw your tracks, and begin.
3. **Mechanics First, Fiction Second.** The dice decide *whether* the characters lose
   footing or take a setback; the story explains *how* it happened.
4. **Narrative-First Gaming.** The rules exist to tell the coolest, most exciting story
   possible. They are "story rules," not strict technical or simulation-heavy combat
   mechanics.
5. **Guided or Co-op Sandbox.** Whether you play with a Guide directing the action or
   fully cooperatively without one, both styles are built for player-led sandbox play
   where the players have ultimate freedom over where the journey goes.

> ⚠️ **NOTE — resolved by V5.** Earlier drafts split on Principle 3's wording ("get hurt"
> in V4 vs "lose footing" in V3). V5 settles it as "lose footing or take a setback," which
> is used above.

---

## 2. Getting Started: Setting the Stage

Launch a session by going through these steps together. In under 15 minutes you'll have a
world, characters, and be in the middle of the action.

### Step 1: Worldbuilding (Build the World)

Define the setting. Either choose a classic starter backdrop from *Amazing Tales* (like
the Pirate Seas or the Deep Dark Forest), **or** build your own by answering the 10
collaborative questions in Section 3 (Worldbuilding).

### Step 2: Create Characters

Create heroes that fit the world you just forged. Each player describes their Concept,
chooses four Assets, and sets their starting Readiness (Section 4).

### Step 3: Decide on a Starting Story Arc & Antagonist

- **The Goal** — The ultimate victory condition (e.g., "Recover the Sun Crystal").
- **The Milestones** — The achievements needed to win. For a first game, pick exactly
  **3.** You can also skip writing them down and "wing it" as you play.
- **The Antagonist / Main Obstacle** — Every quest needs a main force stopping you. A
  dragon guarding a volcano, a rival gang in a heist, or even the ticking clock of an
  approaching storm.

### Step 4: Draw the Tracks

Draw a row of boxes for the **Heroes** — one box per Milestone (e.g., 3 milestones = 3
boxes). This is the **Story Arc Track.**

Then draw a second, identical row underneath for the **Antagonist Track** (Section 6) — same
number of boxes. Every Story Arc has both tracks; the Antagonist Track is the bad guys racing you,
and it's also what makes fleeing possible when things get dangerous.

### Step 5: Choose the Starting Scene (In Media Res)

Open the "movie" *in media res* — right at the start of the action. To slay a dragon,
don't start in a tavern buying supplies; start at the mouth of the cave, or fleeing town
if the journey there is the first milestone. Describe the scene, ask "What do you do?" and
play.

---

## 3. Worldbuilding (10 Questions)

If you're not using a starter backdrop, answer these as a group to define the "physics"
and "social rules" of your sandbox:

1. **The Genre** — The mood of the story? (Mystery, spooky, action/adventure, drama?)
2. **The Setting** — Time and place? (Medieval kingdom, deep space, underwater city, modern day with a twist?)
3. **The Denizens** — Who lives here? (Common races, species, or types of people we'll meet and can play as.)
4. **Magic** — How does it work? (Common or rare? Wands, ancient spirits, inner power? Or none at all?)
5. **Technology** — What level? (Swords and shields? Steampunk gears? Laser blasters and AI? Lost tech?)
6. **The Leadership** — Who's in charge? (A king, a corporation, a council, a lawless wasteland?)
7. **The Enforcement** — How do they stay in charge? (An army, spies, robot sentries, the people's respect?)
8. **The Threats** — The 2–3 biggest dangers right now? (Ancient evil, resource shortage, rival nation, monster infestation?)
9. **The Forbidden** — One place, object, or action that's off-limits? (Forbidden ruins, a type of magic, beyond the great wall?)
10. **The Reputation** — When people see a group like yours, what do they think? (Brave protectors, troublemakers, legends?)

---

## 4. Character Creation

Building a character takes less than two minutes.

### Step 1: The Concept

The Concept is the big "movie poster" pitch for who you're playing. It should fit the
sandbox built in Worldbuilding. Use this formula:

> **Concept = [Adjective, Species, or Twist] + [Class, Job, or Archetype]**

Genre examples to inspire kids:

- **Sci-Fi Adventure:** "A Renegade Robot Pilot" or "A Cyber-Scout with a Robot Dog."
- **Epic Fantasy:** "An Ice-Dragon Knight" or "A Grumpy Goblin Alchemist."
- **Spooky Mystery:** "A Fearless Ghost-Hunting Detective."
- **Cozy Town Drama:** "A Fast-Talking High-School Journalist."

**The Golden Question.** Once a player has a Concept, ask: *"If your character was on a
movie poster, what's their signature action pose, and what are they wearing?"* This
breathes life into the concept and gets kids describing their actions.

### Step 2: The Four Assets

Instead of stats, the player chooses **four things their character is amazing at.** These
are their **Assets** — the signature tools, talents, and relationships the character
relies on to solve problems.

- **Backstory & Origin.** When defining an Asset, consider *how* the character got good at
  it — this instantly builds backstory. (Where did you learn to shoot? Was speaking to
  animals a gift from a forest spirit?)
- **Beyond Expertise.** Assets don't have to be skills. They can be gear, magic, or allies:
  - **Skills & Magic:** Fire Magic, Hacking, Acrobatics, Tracking, Solving Mysteries.
  - **Magical Items & Gear:** A Hoverboard, a Shield Generator, an Enchanted Sword, a Grappling Hook.
  - **Companions & Allies:** A Loyal Pet Wolf, a Tiny Repair Drone, a Wise Sprite Companion.

**Why Assets carry so much weight.** In most games you roll a generic stat (like Strength)
*plus* a narrow special ability. *Lights, Camera, Action!* folds both into one currency —
**your four Assets ARE your stats.** They do double duty: areas of raw competence *and*
signature tricks. One of the four is deliberately the broad, stat-like one (the **Attribute**,
below); the other three should be specific, or the +2 stops meaning anything and the math
goes soft.

> ✅ **DECIDED — Attributes (2026-06-12).** Borrowing Starforged's *asset types* idea (the
> list, not its separate-stat mechanic): a hero's **first Asset is an Attribute** — their
> natural strong suit, chosen from a closed list of five. It is a normal Asset in every way
> (+2 when it fits, +1 floor when it doesn't); it is simply *allowed* to be broad. As in
> Starforged, the **player argues** which Attribute fits from how they describe the action —
> the system never dictates it. **Max one Attribute per hero** (a creation pick; you can't buy
> a second with Growth). Reverses the old blanket "no generic traits like Strength" rule,
> which over-claimed on balance grounds: one capped, deadzone-having broad Asset doesn't break
> the curve (see sim, `Math & Simulation Reference.md`).

| Attribute | Covers (Starforged analog) |
|---|---|
| **Strong** | force, might, endurance *(Iron)* |
| **Quick** | speed, agility, reflexes, precision *(Edge)* |
| **Clever** | knowledge, reasoning, noticing *(Wits)* |
| **Sneaky** | stealth, trickery, deception *(Shadow)* |
| **Charming** | social, courage, empathy, connection *(Heart)* |

The **max-one cap is load-bearing:** it guarantees every hero keeps a wide **+1 floor** —
Strong does nothing to notice a clue, charm a guard, or sneak past one — and that floor is
where the Miss-tension lives. The other three Assets stay specific and personal; that's where
the character's voice is.

> ✅ **DECIDED — recommended creation template (2026-06-12, the "four questions").** To beat
> the blank-page problem, creation is presented as four ordered questions, a typed loadout in
> the Starforged-asset-types spirit: **(1)** what are you best at? → **Attribute**; **(2)** what
> did you train in? → a **Skill/Expertise**; **(3)** what's your signature item or sidekick? →
> an **Item/Companion** (or a **Connection** — mentor, contact, reputation — for concepts with
> no gear/buddy); **(4)** one **Wild** pick of the player's choice (anything but a second
> Attribute). **Only Q1 (the one Attribute) is a hard rule; slots 2–4 are a guiding default the
> player may rearrange.** Purely a creation-flow scaffold — no mechanical weight, the four are
> still just Assets — so no balance impact beyond the Attribute itself (§3b sim unchanged).

**What makes a (non-Attribute) Asset good.** Aim for a **domain of competence** — broad
enough to come up often, specific enough that it clearly *doesn't* cover everything.

- ✅ **Good:** Fire Magic · Acrobatics · Fast-Talking · My Loyal Wolf · Grandpa's
  Lockpicks · Piloting · Tracking · Healing Herbs. *(Each has obvious situations where it's
  useless — that's the sign it's well-sized.)*
- ❌ **Still banned — no-deadzone traits:** "Lucky," "Skilled," "Good at everything."
  *(These would help on literally **any** roll — even alongside your Attribute — so you'd drift
  to +2 always. The five Attributes are fine precisely **because** each has a whole category it
  does nothing for.)*
- ❌ **Avoid — too narrow:** "Picking brass locks," "Juggling." *(Rarely comes up, so it
  almost never helps.)*
- ❌ **Avoid — "I win" powers:** "Invincible," "Mind Control," "Always Succeeds."

**Rolling with Assets:**

- **+2 — an Asset applies:** you get +2 when you can say, in *one sentence*, how this exact
  Asset solves this exact problem, using fiction that's already true. If you have to stretch
  the sentence, it doesn't apply.
- **+1 — anything else:** a reasonable action outside all of your Assets. You're a capable
  hero, so you're never helpless — but this isn't your wheelhouse, so it's riskier.

> ⚠️ **NOTE — the math.** With **+2** (acting in your wheelhouse, the common case): ≈42%
> Strong / 42% Weak / 17% Miss — an ~83% hit rate, a good feel for kids. With **+1** (out of
> your wheelhouse): ≈28% Strong / 44% Weak / 28% Miss — ~72% hit, riskier but not punishing.
> The +1 floor (rather than +0) keeps off-niche actions from feeling hopeless, while the
> doubled Strong-Hit rate (28%→42%) keeps Assets clearly worth having. Because the four
> Assets *are* the character's competence, most rolls are +2. The mandatory **Attribute**
> nudges the share of +2 rolls up modestly (the model's `P_PLUS2` moved 0.80 → 0.85), but the
> lift is small and **uniform across every hero** — sim shows it only trims the Out-of-Action
> rate ~1–2 pts and adds ~0.1 ending Readiness per Episode, not enough to soften the teeth
> (`Math & Simulation Reference.md` §1).

### Step 3: Readiness

Every character starts with **9 Readiness.** Unlike games that track health, magic, and
inventory separately, *Lights, Camera, Action!* bundles all of it into one track. Readiness is a
unified measure of three things:

- **Physical Health** — stamina, energy, physical armor.
- **Mental Health** — focus, morale, courage, composure under stress.
- **Supplies** — key equipment, ammo, food, useful adventure gear.

If a character is badly hurt, mentally stressed, **and** low on gear, they're no longer
ready for adventuring and drop toward 0.

When Readiness reaches **0**, the character is **Out of Action** (exhausted, overwhelmed,
too scared to continue, or out of vital supplies) and can't act until they recover. How
recovery and Out of Action work is covered under **Recovery** (Section 7).

### Step 4: Growing Your Heroes (Advancement)

> ✅ **DECIDED — character advancement (2026-06-08).** Heroes grow across adventures via a
> **Growth Track** and a small boon menu. The defining principle is **horizontal growth:
> heroes gain new tools and signature moves, never bigger numbers** — so the +2/+1 curve and
> the max-9 Readiness cap are never touched, and **enemy/Challenge/Antagonist tracks never
> need rescaling.** The game is exactly as hard for a starting hero as for a campaign veteran;
> the veteran simply has more options and more spotlight moments.

- **Growth (the currency).** Each hero tracks their own **Growth** on a **Growth Track** (a
  simple row of boxes on the sheet). **Every 3rd Milestone the party marks — on any Story Arc —
  each hero earns 1 Growth** (all heroes tick together, exactly as everyone used to score on a
  shared win). Count every Milestone marked, on any arc; a single beat that marks boxes on two
  arcs at once counts each box. The tally is **cumulative across the whole game and never resets
  per arc**, so no Milestone is ever wasted — a 4-box "stretched Episode" carries its 4th Milestone
  toward the next Growth. This ties Growth to **headway actually played, not arcs finished**, which
  closes two holes the old "1 per Story Arc" rule had: a standalone Movie/Season can no longer be
  *starved* (it pays out as you play it, not only on completion), and a slow arc can no longer be
  *gamed* (stretching one arc over many sessions earns no more than playing it briskly). Rough
  feel: an Episode (3 boxes) ≈ 1 Growth ≈ one session of play; a Boon lands every ~2 sessions, a
  New Asset every ~5. Growth rate is a pure feel knob — Boons are horizontal (§ below), so faster
  Growth never rescales the +2/+1 curve or enemy tracks.
- **Spending Growth:**

  | Buy | Cost | Limit |
  |---|---|---|
  | **Boon** — a once-per-Scene/Session signature move attached to an existing Asset card | **2 Growth** | max **2 Boons per Asset** |
  | **New Asset** | **5 Growth** | ceiling **6 Assets**; at 6, **Trade In** (retire) one to add one |

- **Boons are horizontal, and built from two pieces (Ch.13).** A Boon never raises a hero's
  *baseline* roll. As of the build-a-Boon revision, a Boon = a **Trigger** (when you may use it —
  open, flavorful, genre-supplied) + an **Effect** (what it does — a **closed, fixed list**, the
  only part that touches the dice). Genres add Triggers, never Effects.
  - **Effects (closed list).** *Strong:* **Upgrade** (one tier better — Miss→Weak or Weak→Strong),
    **+1 to the roll** (banked one-time +1), **Take the Price** (Asset/you absorbs a Price for you
    or a nearby ally). *Mild:* **Reroll** a Miss, **+1 to your next roll** (your or an ally's next roll),
    **Lend a reroll** (aided ally rerolls a Miss), **Free Oracle** (one yes/no), **Steady Hands**
    (your **Mend** gives +1 / lets you Mend an ally as if yourself). Explicitly **excluded** (balance
    levers, not menu effects): marking extra track progress; preventing Out of Action; skipping the
    Antagonist Surge.
  - **Cadence is derived, not chosen.** Strong effect → **once/Session**; Mild → **once/Scene**;
    **lock the Trigger to a named situation → one step more often** (a Strong effect drops to
    once/Scene). This *is* the "narrow the trigger, widen the effect" trade, made mechanical, and
    it answers the old once-Scene-vs-Session question by construction.
  - **+1-type effects are temporary one-roll bonuses,** the same safe lever as the Start a Challenge roll
    (sim-cleared, `Math & Simulation Reference.md` §4c) — **never** a permanent modifier, so the
    +2/+1 curve and enemy tracks still never rescale.
  - **Recipes (pre-built combos, presented by name in the book):** Signature Move (any time +
    Upgrade, Session), In My Element (situation + Upgrade, Scene), Dig Deep (any time + +1 to roll,
    Session), Reliable (any time + Reroll, Scene), Lend a Hand (help an ally + Lend a reroll, Scene),
    Mender (when you Mend + Steady Hands), Scout (any time + Free Oracle, Scene), Take the Hit (any
    time + Take the Price, Session). Each genre kit carries a **d10 Boon-trigger table** (all 7 done).
- **Asset ceiling: 6.** A hero starts with four Assets and can buy up to two more. Beyond six
  there are no new slots — buying a seventh means **Trading In** one of the existing six (a
  "your hero outgrew that" story beat); it still costs the full 5 Growth.
- **"Widen the Domain" was considered and cut.** A boon that broadened an Asset's coverage
  (more +2 frequency) was the lone non-horizontal option — it re-introduced power-creep and
  the "Lucky" problem the Asset rules warn against, and its benefit (broader coverage) is
  already served by buying a **New Asset**. All growth stays horizontal. *(This does not
  conflict with the **Attribute** at creation: Widen-the-Domain was an unbounded, repeatable,
  buy-with-Growth broadening of an arbitrary Asset that could stack toward "good at
  everything." The Attribute is a single, **capped-at-one**, creation-time pick from a closed
  list, with guaranteed deadzones, and it's uniform across all heroes — so the sim prices it
  in once and it never creeps.)*

> Naming note: **"Growth," not "XP."** The vocab table bans "XP" for track Progress; the
> advancement currency uses the thematic term **Growth** to keep that distinction clean.

---

## 5. The Core Mechanic

Whenever a player attempts something risky or challenging, roll **2d6** and add the
modifier (**+2** if one of your Assets applies, **+1** for anything else).

There are two ways to resolve a roll, depending on the situation:

- **Regular Rolls (simple risks)** — quick actions that don't need a track (jumping a
  fence, recalling a clue, picking a normal lock). On a success you simply accomplish the
  action and the story moves on.
- **Challenge Rolls (action scenes)** — active, multi-step obstacles using a Challenge
  Track (fighting a monster, fleeing an eruption, navigating a hazard). On a success you
  mark progress on the track.

| Roll | Result | Regular Roll outcome | Challenge Roll outcome |
|---|---|---|---|
| **10+** | **Strong Hit** | Full success — you do exactly what you wanted, cleanly. Move on! | Mark **1 Progress** on the Challenge Track. |
| **7–9** | **Weak Hit** | Success at a cost — you achieve it, but with a minor setback. **Pay the Price** (lose **1** Readiness). | Mark **1 Progress** AND **Pay the Price** (lose **1** Readiness). |
| **6 or less** | **Miss** | Failure — your action fails and things get worse. **Pay the Price** (lose **2** Readiness). | Mark **no Progress** AND **Pay the Price** (lose **2** Readiness). |

A Weak Hit and a Miss **always** cost Readiness, exactly as shown — there is no way to dodge
that loss on a roll. The **Antagonist Track** never advances *automatically* on a roll; it moves
only when the heroes take a **Recovery Scene** (Section 7/9) — falling back to regroup surges the
villain one box. The bad guys gaining ground is never a silent per-roll consequence.

### Narrate the Change

Every roll turns back into fiction. On a **Strong or Weak Hit**, the acting player
**narrates how the scene changes** — what they pull off, what they find or reveal, or how
the situation shifts — and, when the scene is finished, narrates its ending and what the
heroes turn to next. **That narrated change *is* the progress.** Even a Regular Roll that
fills no track pushes the story forward, because the world is now different than it was. (On
a **Miss**, the change is the Pay the Price complication.)

This is what lets one core move handle everything — including investigation. Searching for a
clue, a Hit means you narrate finding *something* and decide what it is; the table can work
out what it means now or save that for later. A big search (combing a crime scene) can be a
**Challenge** — each progress point is a fresh clue *or* a new avenue (you spot a hidden door
now; a later roll finds what's inside). Either way you've moved the story closer to its end,
which is the whole job of the core move.

### The Oracle's Blessing (Optional)

If a player rolls **matching numbers (doubles)**, their result is upgraded by one tier:

- A **Miss** with doubles (like 2 & 2) becomes a **Weak Hit.**
- A **Weak Hit** with doubles (like 4 & 4) becomes a **Strong Hit.**
- A **Strong Hit** with doubles (like 5 & 5) is an **Outstanding Success** — you succeed
  spectacularly and add an extra narrative bonus of your choice.

### The Moves (Master List)

*Lights, Camera, Action!* runs on a small, fixed set of **moves** — every time you pick up the dice to
settle something, you're making one. They fall into three families by **what they do:**

- **Action moves** *resolve a hero's attempt* at something risky — **2d6 + 2/+1**, read
  Strong/Weak/Miss. The dice **adjudicate** (did you pull it off?).
- **Progress moves** *open or close a progress track* — a Story Arc or a Challenge. The openers
  (Start a Story Arc, Start a Challenge) roll generatively to set how things begin; the closers
  (Fall back, Quit the Story Arc) are deterministic procedures.
- **Frame moves** *shift the fiction in the moment* — no track. When a Frame move rolls, the dice
  **generate** a direction rather than judge a hero — so a Frame move can never be "failed."

Each move is defined in full in the chapter noted; this list is the authoritative roster.

**Action moves — resolve a hero's attempt (2d6 + 2/+1):**

| Move | What it does | Chapter |
|---|---|---|
| **The Roll** | The core move; handles any risky action, run as a **Regular Roll** (no track) or a **Challenge Roll** (marks a track). Every other move is shaped from it. | Ch.7 |
| **Aid Your Ally** | The core move pointed at a teammate — on a Hit, hand them +2/+1; same Pay the Price as any roll (Strong: ally +2; Weak: ally +1, aider −1; Miss: nothing, aider −2). | Ch.7/8 |
| **Mend** | A quick patch in any scene (in a Challenge, it's your turn instead of a Challenge Roll): self or ally, **Strong +3 / Weak +2 / Miss −1 Readiness**, up to current max, **no Surge**, can't revive an Out-of-Action hero. | Ch.9 |
| **Recovery Scene** | Fall back and regroup: recover **up to the current Readiness max**; **surges the Antagonist Track one box** *and* **lowers the max by 1** (start 9, floor 4). Reliable; the quiet/B-plot beat. | Ch.9 |
| **Downtime** | The between-Story-Arcs rest: resets the Readiness max to 9, heals to full, restores any Broken Asset (no Surge). | Ch.9 |
| **Showdown** *(the climax)* | The last-box roll when the heroes reach the climax (Story Arc Track full); decides the Story's outcome. A Miss escalates rather than ending it outright. | Ch.8/10 |

**Progress moves — open or close a progress track:**

| Move | What it does | Dice |
|---|---|---|
| **Start a Story Arc** | Sets how a new Story Arc opens — *Clear purpose* / *More questions than answers* / *Trouble finds you first* (Ch.10). | 2d6 + 1, generative |
| **Start a Challenge** | Sets the opening of a Challenge the heroes *deliberately initiate*: a one-time **±1 to the first roll** (Strong +1 *you got the drop* / Weak 0 *even footing* / Miss −1 *they beat you to it*). Skipped when trouble is thrust on the heroes (Ch.8). | 2d6 + 1, generative |
| **Fall back** | Retreat from a losing Challenge (lose its progress) to regroup — resolved as a **Recovery Scene** (full heal + Surge) (Ch.8/9). | none |
| **Quit the Story Arc** | The terminal fall back — give up a Story; no penalty or bonus; the loss seeds a new Story (Ch.10). | none |

**Frame moves — shift the fiction in the moment:**

| Move | What it does | Dice |
|---|---|---|
| **Ask the Oracle** | The stuck-point move: name the next Milestone → do the obvious → **Story Spark** (d6) or **Ask the Dice** (1d6 yes/no) (Ch.11). | d6, generative |
| **Pay the Price** | Turns a Weak Hit/Miss into a fiction complication; *may* tick the Antagonist Track on a telling failure (Ch.9). | none (optional prompt) |

*Doubles on any 2d6 move trigger **Oracle's Blessing** (upgrade one tier — including the
generative tiers of Start a Story Arc).*

---

## 6. Story Arcs and the Antagonist Track

The story is a race between the Heroes and the Antagonist.

### The Story Arc Track

A **Story** is one spine — a single central dramatic question — tracked with two paired rows of
boxes. The **Story Arc Track** is the heroes' progress: **mark a box whenever the table agrees you
made significant headway — a Milestone.** Fill the track and the heroes reach the **climax** (the
**Showdown**), where the Story's outcome is decided.

**Two story sizes — Episode and Movie.** A Story is one of two sizes, and these are the *only* two
with their own box machinery:

| Size | Story Arc Track | Antagonist Track | Feels like |
|---|---|---|---|
| **Episode** | **3 Milestones** | **2** (1 surge + the climax) | one TV episode, told in one sitting |
| **Movie** | **6 Milestones** | **3** (2 surges + the climax) | a feature film, over ~2–3 sessions |

The box counts are defaults, not locks — a meaty Episode can stretch a Milestone or two. The
Antagonist Track is always **short**, sized so its surges land the villain *one step from winning*
right as the heroes reach the climax (below).

**Seasons and Series are collections, not sizes.** Episode and Movie are *individual* stories.
**Season** and **Series** describe how you string those stories together over a long game — they
are prose patterns, not new machinery:

- A **Season** is usually a **collection**: a run of Episodes/Movies sharing a throughline — a
  recurring antagonist, a season-long question carried by a B-plot **thread** (below). (Occasionally
  a Season is a single long serialized spine — but that's just a big Movie, an individual story with
  more Milestones.)
- A **Series** is **always a collection**: the whole game, a run of Seasons. You run it with these
  same rules — one Story at a time, threads tying them together. A Series has no box count of its
  own.

**B-plots and character arcs are threads, not peers.** A subplot rides alongside the spine with its
own light progress track but **no Antagonist Track — no lose-clock of its own.** It advances when
the fiction advances it and **resolves into or beside the spine's climax.** Threads are the
connective tissue of a Season: the slow-burn relationship, the rival, the season-long mystery.

> ✅ **DECIDED — single nested spine, two sizes (2026-06-13).** Replaces the sandbox model
> (concurrent independent arcs in four fixed sizes — Episode 3 / Movie 8 / Season 8 / Series 12 —
> each with an equal-length Antagonist Track, advanced by fleeing + an optional tick). That
> structure was a Starforged inheritance and **could not produce the game's goal** — a story whose
> villain ends *one step from winning*. The new model: **one Story = one spine**, two individual
> sizes with machinery (**Episode 3/2, Movie 6/3**), Season/Series as prose collection patterns,
> B-plots as lose-clock-free threads. Recovery is **two moves** — a small risky **Mend** (no surge,
> the in-Challenge tactical choice) and the full-reset **Recovery Scene** (which surges the villain).
> Validated in `Math & Simulation Reference.md` (the new
> spine-model section): the photo-finish becomes the default ending (~89–97%) with a rare, real
> loss (~2–6%). Kills the old "four types / equal-length Antagonist Track / multiple concurrent
> arcs / no-feed-up" rules; **nesting returns** (a Season is *made of* Stories).

### Start a Story Arc (The Opening Roll)

Once a Story Arc is set up (Goal, Milestones, antagonist, both tracks), make one **Start a Story Arc**
roll to set *how it opens:* **2d6 + 1** (no Asset applies — this isn't a test of a hero's skill;
the +1 is the off-Asset floor, and **Oracle's Blessing applies** on doubles). It is **generative,
not pass/fail** — all three tiers are playable openings, differing only in how much trouble is
already on the heroes when the first Scene starts:

- **10+ — Clear purpose.** Open on the front foot; the heroes are in control and move first.
- **7–9 — More questions than answers.** Open in motion with **one** complication already in
  play (Ask the Oracle, or just decide).
- **6− — Trouble finds you first.** Open in the thick of it; the first Scene is likely an
  unchosen Challenge (Ask the Oracle for the obstacle).

The result sets the *temperature* of the first Scene; the content always points at the **first
Milestone**. First games (Part One) skip the roll and simply open in media res (Ch.3).

> ✅ **DECIDED — Start a Story Arc opening roll (2026-06-09).** A **Progress move** (it opens a Story Arc
> track rather than resolving a hero's attempt; originally filed as a "Frame move" before the
> three-family revision): one **2d6 + 1** roll made when a Story Arc begins, to generate the tone of
> its opening. Modeled on Starforged's *Swear an
> Iron Vow*, **minus** the momentum reward. **Generative, not adjudicative** — no hero is tested,
> so there is no failure; the three tiers (*Clear purpose* / *More questions than answers* /
> *Trouble finds you first*) are three flavors of opening, a "Miss" being simply the most
> cinematic way in. It uses the **full core roll** (the +1 off-Asset floor; Oracle's Blessing
> applies) rather than a bare d6, so the familiar Strong/Weak/Miss ladder carries the
> good/middle/poor shape. **No balance impact** (no Readiness or track stakes; not modeled in the
> Math doc). Part One **skips** it (assume a clean launch, open in media res); Part Two (Ch.10)
> teaches it with interpretation guidance. Vocabulary row added; listed in *The Moves*.

### The Antagonist Track (The Bad-Guy Clock)

> ✅ **DECIDED — the Antagonist Track is a CORE rule (2026-06-06).** Every Story Arc has one. It
> was formerly optional; Ian made it mandatory because the flee/retreat rule (below) is built
> on it — it is the heroes' stay-alive valve, not just a hard-fail option.

The Antagonist Track is **the losing side of the same Story** — not a separate arc, but this
Story's other end. It is **short**, and its **top box is the climax (the Showdown), held in
reserve.** The lower boxes fill as the antagonist gains ground during play; the **top box is taken
only at the climax** — when the heroes reach their Showdown (its outcome decided there) or when
they are overwhelmed before getting there (below). The Story is a race: arrive at your Showdown
with the villain **one step from winning** — the photo-finish — or fall before you reach it.

> ✅ **DECIDED — how the Antagonist Track advances: surge on the Recovery Scene (2026-06-13).**
> The villain advances **one box each time the heroes fall back to regroup** — i.e. take a
> **Recovery Scene** (Section 9). Falling back to lick your wounds buys recovery at the cost of
> ground: while you catch your breath, the antagonist moves. This replaces the old flee /
> optional-Pay-the-Price triggers. It is **emergent and player-chosen** — you regroup when the
> dice and fiction leave you hurt enough to need it, *discovered in play, never scheduled to a
> beat.* Modeled in `Math & Simulation Reference.md` (spine-model section): with this trigger and
> a short reserved-climax track, the villain reliably lands at one-from-full at the finale.

- **The Surge (what a filled box means).** When a Recovery Scene fills a box, stop and play it out.
  While the heroes regrouped, the antagonist gained ground — **envision what that looks like for
  them off-screen**, then **complicate whatever happens next:** a new obstacle, an escalation, an
  ally captured, the deadline jumps closer. The world visibly tightens.
- **The regroup is the quiet beat between dangers.** A Recovery Scene is the campfire, the
  heart-to-heart, the lick-your-wounds lull — **often a B-plot or character beat.** So character
  scenes are *where the villain gains ground*: taking time for the cast is never free, which gives
  the slow scenes real stakes. Regrouping only when you genuinely need to is the disciplined play.
- **Keep the climax box free.** The heroes won't *voluntarily* surge into the top box — that would
  hand the villain the win. Voluntary regroups fill up to one-from-full and stop there.
- **Characterize the antagonist.** The antagonist may be a person, a faction, or a **force** (a
  harsh desert, a plague, a deadline). Name what it *wants* and what "winning" looks like, so every
  surge is a concrete beat: surge the desert's track → a sandstorm hits.
- **Losing before the climax (the loss vector).** A hero taken **Out of Action** *forces* a Recovery
  Scene — the team has to get them back on their feet — and that forced **Surge can fill even the
  reserved climax box.** If it does, the villain wins before the heroes reach their Showdown: the
  Story is lost early. This is the real risk that keeps Readiness meaningful — it is no longer a
  survival meter (heroes can't die) but **ammunition spent against the villain's clock.**

**Quitting a Story Arc (the official lose).** Heroes are never forced to grind a Story Arc to a
deadly end. At any point the group may simply **give up the Story Arc** — the terminal version of
fleeing. There is **no mechanical penalty or bonus** for quitting: no special heal, no carry-
over. The heroes lick their wounds, the villains win this one, and the table moves on to a new
Story Arc. Quitting (or losing) exists precisely so a low-Readiness party can stay alive instead of
being ground down.

**Losing is a Story Arc seed.** A lost Story Arc is not a dead end — it's fuel. When the antagonists
win, ask together: *how did the world change now that they got what they wanted?* Use the
answer to reshape the setting, then write a **new Story Arc** — directly or indirectly born from
this defeat. Losing should leave the table excited about what happens next, not deflated.

### Milestones Are Made of Scenes

Think of a Milestone as a **chapter of the story** — and a chapter is made of **Scenes,**
just like a movie. A Scene is a single beat of play: it might be one or two quick **Regular
Rolls** (search the room, talk your way past a guard), or it might be a big enough moment to
run as a full **Challenge** (Section 7). A Milestone usually strings several Scenes together;
it is **not** the same thing as a single Challenge. When the heroes have played through the
Scenes that make up a Milestone and accomplished it, check a box on the Story Arc Track.

(Occasionally a Milestone *is* small enough to resolve in a single Scene — even one Regular
Roll — but the typical Milestone is a short sequence of Scenes building to its payoff.)

**Example Story Arc: "Retrieve the Sun Crystal" (Episode, stretched to 4 Milestones)**
*Goal:* Steal back the Sun Crystal from the Goblin King's vault to save the winter village.

- **Milestone 1 — Find the secret mountain entrance.** A few Scenes: question a villager
  (Regular Roll), brave the snowstorm up the cliff (Regular Roll), spot the hidden door.
  Accomplishing it checks Box 1.
- **Milestone 2 — Cross the Bottomless Chasm.** A bigger Scene worth a full **Journey
  Challenge** (3 boxes) — swing on vines, build rope bridges — perhaps bookended by a short
  Regular-Roll Scene on either side. Milestone done → Box 2.
- **Milestone 3 — Pull off the Vault Heist.** Several Scenes: scout the guards (Regular
  Roll), then the **Stealth Challenge** to bypass traps, then a quick getaway beat. → Box 3.
- **Milestone 4 — Defeat the Goblin King and Escape!** The climactic Scenes — a **Combat
  Challenge** against the King, then the escape. King defeated and heroes clear → Box 4.
  Story Arc complete; the village is saved.

> ✅ **DECIDED — a Milestone is a collection of Scenes, not a single Challenge.** Ian
> clarified (2026-06-06): think in movie terms — a Milestone is a *chapter* made of *Scenes*,
> where a Scene is one/a few Regular Rolls **or** a full Challenge. A lone Challenge is
> normally a Scene *inside* a Milestone, not a Milestone by itself. **"Scene" is confirmed as
> a canonical Standard Vocabulary term** (Ian, 2026-06-06).

---

## 7. Challenges (The Action Scenes)

A Challenge plays out big, high-stakes, multi-step events worth more story time than a
single roll. Minor tasks (jumping a gap, a simple lock, searching a quiet library) need
**no track** — just one Regular Roll. If the situation is dangerous, dynamic, or dramatic
(fighting a monster, fleeing a collapsing temple, crossing a hostile swamp, combing a crime
scene for clues), draw a Challenge Track.

**No enemy stats — and no death.** Enemies and obstacles have **no Readiness, no stats, no
hit points.** Only the heroes track Readiness. You overcome a foe or a hazard by **filling
its Challenge Track** (or advancing a Milestone) — mechanically, *the track is the enemy.*
And **heroes can't die.** The worst that happens is going **Out of Action** (recoverable) or
**losing the Story Arc** (the Antagonist Track fills). Setbacks cost Readiness and story
ground — never a character's life.

**Deciding: Regular Roll or Challenge?** This is a *group* call (in Co-op play, made
together — not by one player), and it's purely a story question, never a tactical one. Ask:
**"How much screen time does this scene deserve? Is this a big, fun moment worth playing
out — or just a blip on the way to the next big thing?"** Another way to put it: *how much
of the movie should this be?* There is **no mechanical reward for rushing** — you don't win
the Story Arc faster or take less harm by skipping a Challenge Track. So the only thing that
should decide it is which choice tells the better story. If the dragon fight matters, draw
the track and savor it; if the group would rather get past it to the real climax, one
Regular Roll is perfectly legitimate.

### 1. Set the Difficulty (Draw the Track)

The number of boxes scales with the size of the player group:

- **Easy Challenge** — boxes = number of players. (2 players = 2 boxes)
- **Medium Challenge** — boxes = number of players **+1.** (2 players = 3 boxes)
- **Hard Challenge** — boxes = number of players **+2.** (2 players = 4 boxes)

### 2. The Turn Loop

A Challenge runs in a loose, popcorn-style round-robin. **No initiative rolls, no complex
action phases.**

- Anyone may act first — the group chooses based on the fiction (whoever the moment is
  about).
- **Everyone acts once before anyone acts twice.** Once each hero has taken a turn, the
  round resets and anyone may go again, in any order. This keeps one strong character from
  soaking every roll — spread the spotlight and share the fun evenly.
- On your turn, describe what your character does, then roll 2d6 + modifier. (Instead of
  rolling, you may spend your turn to **Aid an Ally** — see below.)
- Resolve using the Core Mechanic table.

### 3. Marking Progress & Taking Hits

- **Strong Hit (10+):** fill 1 box.
- **Weak Hit (7–9):** fill 1 box, but **Pay the Price** (lose 1 Readiness).
- **Miss (6 or less):** fill 0 boxes, and **Pay the Price** (lose 2 Readiness).

(The Antagonist Track is never advanced *automatically* by a roll result — only when the heroes
take a **Recovery Scene** (fall back and regroup, Section 7/9), which surges the villain one box.)

### 4. Ending the Challenge

The Challenge ends the moment the last empty box is filled.

- The obstacle is cleared and the heroes complete the current Milestone.
- Immediately check off 1 box on the Story Arc Track.
- Wipe the scrap paper clean of the Challenge Track.

(For a climactic Challenge, you can make filling that last box a **Showdown** — see below.)

### 5. Aid Your Ally

**A variant of the core move** (the book defines it in **Ch.7 — The Roll**, not in the
Challenge chapter; it's general teamwork, usable in or out of a Challenge). On your turn,
instead of acting against a problem yourself, you can help a teammate. Describe how you
assist, then roll 2d6 + modifier (use **+2** if one of your Assets fits the help, **+1**
otherwise):

- **Strong Hit:** your ally gets **+2** on their next roll.
- **Weak Hit:** your ally gets **+1** on their next roll, and **you Pay the Price (−1
  Readiness).**
- **Miss:** your help doesn't land — no bonus — and **you Pay the Price (−2 Readiness).**

Aid uses the **same math and the same Pay the Price as any roll** — the Readiness cost is
*not* a punishment for helping; Aid is simply the core move pointed at a teammate, so it
carries the same risk every action does. Doubles upgrade the tier as normal. Aid is the best
use of a turn when the obstacle isn't in your wheelhouse — and because the popcorn rule means
everyone acts every round anyway, it gives a real job to the hero whose Assets don't fit the
moment.

### 6. The Showdown (Optional Climax)

By default, filling the last box of a track completes it automatically — clean and fast,
which keeps the story flowing. But for a moment the group has decided is a *true climax*
(the same "how big is this moment?" question used to draw a Challenge), you can make it a
**Showdown**: filling the final box requires one last roll. A Showdown can cap either a
**Challenge Track** (the climax of a scene) or the **Story Arc Track** (the climax of the whole
Story Arc — see below).

Roll 2d6 + modifier for that last box:

- **Strong Hit:** triumphant victory — you win and add a narrative bonus of your choice.
- **Weak Hit:** you win, but it costs you — **Pay the Price** as normal.
- **Miss:** you don't finish *yet*. **Add one extra box to the track** (you must fill it
  before attempting the Showdown again), and the situation escalates — a new wrinkle, a
  fresh danger. A missed Showdown is **delay and drama, never outright defeat.**

(A Showdown roll never advances the Antagonist Track — only a Recovery Scene does that. A Showdown
is about *finishing*, not regrouping.)

**Story Arc Showdown — the plot twist (optional).** You can make the *final box of the Story Arc
Track* a Showdown too — one last roll as the heroes go to complete the closing Milestone.
On a Strong or Weak Hit the Story Arc is won (Weak = Pay the Price on the way out). On a **Miss**,
*you thought it was over, but it wasn't:* **add one extra Milestone box to the Story Arc Track** and
introduce a climactic twist — the villain's true plan surfaces, an ally betrays you, the prize
isn't what it seemed. The heroes must complete that new Milestone before they can attempt the
Story Arc Showdown again. Importantly, **this does not add a box to the Antagonist Track** (only
fleeing does) — the twist gives the heroes *more to do*, not the villains a free win. Like all
Showdowns it's optional, and it's a wonderful way to make the end of a Story Arc land with a
cinematic surprise.

Reserve Showdowns for moments that deserve the tension; everyday Challenges (and Story Arcs) should
still end the instant their last box fills.

### 7. Falling Back from a Challenge (The Escape Valve)

Heroes are never trapped in a Challenge they're losing. At any point — usually when Readiness
is running dangerously low and grinding out the remaining boxes isn't worth the cost — the
group may **fall back** and regroup. Falling back is resolved as a **Recovery Scene** (Section 9):

- **You lose the Challenge's progress.** Wipe the track; those boxes don't count.
- **The party regroups up to its current Readiness max** (which then drops by 1 — see §9) — the point of pulling back.
- **The Antagonist Track surges one box** — the bad guys gain ground because the heroes gave it.
  Play out the **Surge** (Section 6).

Falling back is a **group decision** (in Co-op, made together). Because every fall-back both heals
the party *and* surges the villain, and the Antagonist Track is short with a reserved climax box,
you can only regroup so many times before the villain is one step from winning. That makes each
retreat a real, weighty choice, not a free reset.

If the heroes fall back so much (or simply decide to give up) that the villain takes the climax
box, that is **Quitting the Story** — see Section 6. Falling back is the everyday, scene-level
valve; quitting is the whole-Story version.

### Recovery (Mend & the Recovery Scene)

> ✅ **DECIDED — two recovery moves + a declining recovery ceiling (2026-06-13).** Recovery is
> **two moves**, governed by a **Readiness max that starts at 9 and drops 1 per Recovery Scene**
> (floor 4; resets at Downtime). The **Recovery Scene** (fall back and regroup) restores the party
> **up to its current max**, **surges the villain one box**, *and* **lowers the max by 1** — so each
> regroup leaves the party a little worse than the last (the ratchet that makes a Story Arc tighten;
> Ian's "average ~8 after the first rest"). Reliable; player-chosen; the only thing that advances
> the Antagonist Track. **Mend** is a small, risky **any-scene** patch that **does not surge** — in a
> Challenge it's a *tactical choice* (patch vs. push). Mend can't be the surge-trigger (a small heal
> that surges death-spirals — `sim_spine.py`) and **must cost on a Miss (−1)**. **It needs no usage
> cap:** the −1 risk *and* the declining ceiling (Mend only heals to the current, sinking max) keep
> it from substituting for a regroup — validated ungated in `Math & Simulation Reference.md` §0
> (1st-rest avg 8, Episode loss ~2.5%, Movie ~7%; surge frequency unchanged vs. gated).

**Mend (the any-scene patch).** Any time the fiction gives a beat — in a Challenge (*instead of* a
Challenge Roll) or in an ordinary scene — a hero may **Mend** (self or a teammate) to recover a
little. Roll **2d6 + modifier** (+2 if an Asset fits the care, else +1; doubles upgrade):

- **Strong (10+):** +3 Readiness. · **Weak (7–9):** +2. · **Miss (6−):** **−1 Readiness** (the
  patch goes wrong) — and a Miss *can* drop a hero to Out of Action.

Mend **never surges the villain** and has **no usage cap.** Its limits are the **−1 risk** and that
it only heals **up to your current (declining) max** — so it smooths the ride between regroups but
can never substitute for one or climb you back to full. It's the quick gamble to stay on your feet — when
you're truly low, the safer play is to fall back for a full Recovery Scene instead.

**The Recovery Scene (fall back and regroup).** When the bleed isn't worth it — or the party simply
needs to breathe at a safe lull (most often **between Challenges**) — they **fall back** and
regroup. It **restores the whole party up to its current Readiness max** (reliable, no roll),
**surges the Antagonist Track one box** (Section 6), and **lowers the Readiness max by 1** for the
rest of the Story Arc (floor 4). The max starts at 9, so the first regroup brings everyone to 8,
the next to 7, and so on — **each regroup heals a little less than the last,** tightening the Story
Arc toward its climax. It is **gated by the fiction** (no safe beat, no regroup) and **player-chosen**,
*discovered in play, never on a schedule.* The heroes won't *voluntarily* surge into the reserved
climax box. Because the regroup is the quiet beat — **often a B-plot or character scene** (the
campfire, the heart-to-heart) — **taking time for the cast is never free**: character scenes are
where the villain gains ground, which gives the slow scenes real stakes.

**Downtime (between Story Arcs).** Finishing a Story Arc **resets the Readiness max to 9**, heals
everyone to full, and **restores any Broken Asset** — **no Surge** (the Story Arc is resolved). It's the *slow down and
roleplay* breather between adventures (optionally a d6 prompt: gearing up, good company, loved
ones, a beat for the heart). Heroes always start the next Story fresh.

**Out of Action (the loss vector).** A hero at 0 Readiness can't act. **Mend cannot revive them** —
only a full **Recovery Scene** (or Downtime) brings a hero back from 0, so getting them up **forces
a Recovery Scene**, and that forced **Surge advances the villain even into the reserved climax
box.** If it fills, the villain wins before the Showdown: the Story is lost early. So going down is
no longer survival-neutral — near the climax it is *how you lose*. (This is why Mend can't revive:
otherwise a quick patch would dodge the loss vector.) Heroes still can't die; the cost is the
Surge, a Broken Asset, and the regroup you were forced to spend. This is what keeps Readiness
meaningful — **ammunition spent against the villain's clock**, not a survival meter.

**Broken Assets (DECIDED 2026-06-09).** Going Out of Action also breaks **one Asset** — the one
that failed the hero in the moment they went down (Guide calls it; Co-op table agrees, defaulting
to whatever they were leaning on). A **broken Asset gives no +2:** any roll it would have covered
is made at **+1**, exactly like acting off-Asset. It is *never* a penalty — it only removes the
bonus, so the **+1 floor is preserved** with zero new math (this is why we break an existing Asset
rather than add a negative-modifier one). Only **Downtime (finishing a Story) restores a Broken
Asset** — a mid-Story Recovery Scene heals Readiness but can't un-break an Asset. Going down again
before the Story ends breaks a second Asset. This is the *durable* teeth layer (Starforged
"impacts") that a full-restoring Readiness track lacks; scoped to Out of Action only for now.
Distinct from advancement's **Trade In** (a break is temporary, free, and involuntary; a Trade In
is permanent, costs Growth, and is chosen — §4 / Ch.13). Optional flavor: a Guide may write a
one-off **condition** (*Broken Spirit, Rattled*) that behaves identically (cancels the +2 → roll
+1, clears at Downtime, never a flat penalty) when the hurt doesn't map to a single Asset.

**The teeth aren't the Readiness pool — they're the Surge.** A Recovery Scene restores you fully,
so the party rarely *stays* worn down; the cost is that every regroup hands the villain a box, and
a **Broken Asset rides with you until the Story ends.** Readiness is ammunition against the
Antagonist Track, not a dwindling pool — the pressure is the villain's clock, not attrition.

---

## 8. Pacing: Controlling the Story Clock

Pacing keeps the story exciting and ensures the adventure actually reaches a conclusion.
Two primary tools:

### 1. Progress Track Difficulty

Every track is a decision about how much "screen time" an event gets. A Hard Challenge
(more boxes) eats a larger chunk of the session. If real-world time is running short, lower
the difficulty of future Challenges to move the story along.

### 2. Milestone Timing (The 40-Minute Rule)

The Milestone is the most powerful pacing tool. Because nothing strictly defines a
Milestone, you can complete them as fast or slow as needed. Since the Story Arc Track shows
exactly how many remain, you can gauge your position:

- **The 2-Hour Adventure** — an Episode (3 boxes) finishes in ~2 hours at roughly one
  Milestone every **40 minutes.**
- **The 4-Hour Adventure** — the same 3-box Episode stretches to 4 hours at **80 minutes**
  per Milestone.

Watch the clock and the empty boxes to decide whether to add scene detail or resolve a
Challenge quickly.

---

## 9. Pay the Price (The Complication Loop)

On a **Weak Hit** (lose 1 Readiness) or a **Miss** (lose 2 Readiness), "Paying the Price"
is more than a number — it's **the most obvious negative outcome happening right now in the
scene.** Make the most logical, cinematic complication occur, then explain how it saps
Readiness. If stuck, roll a **d10** or pick from the table.

> ✅ **Paying the Price never advances the Antagonist Track (2026-06-13).** The Price is a
> Readiness loss plus an in-scene complication — nothing more. The Antagonist Track advances
> **only** when the heroes take a **Recovery Scene** (Section 7/9). This replaces the old
> optional "telling-failure tick," which is retired under the spine model.

| d10 | The Price | How It Looks (Example) |
|---|---|---|
| 1 | **The Environment Rebels** | The floor crumbles, a pipe bursts with hot steam, or a door slams shut, sealing your exit. |
| 2 | **You Lose Gear or Power** | Your flashlight dies, your rope snaps, or your shield's battery drains to critical. |
| 3 | **You Get Separated** | A falling boulder blocks the path between you and your friends, or you're cornered. |
| 4 | **An Enemy Gains Ground** | A foe reaches the high ground, blocks your escape, or gets in prime position to strike. |
| 5 | **A New Obstacle Appears** | An alarm blares, reinforcements arrive, or a sudden magical storm rolls in. |
| 6 | **Your Action Backfires** | Your spell lights the wrong curtains, you make a loud crash that alerts foes, or you trip a hidden trap. |
| 7 | **A Costly Decision** | To save a dropped item, you must take 1 extra Readiness loss. |
| 8 | **You Are Rattled & Shaken** | A ghost's screech chills your bones, or a wave of self-doubt saps your focus and energy. |
| 9 | **A Hidden Truth Is Revealed** | The map you've followed is outdated, or the lava monster is immune to normal weapons. |
| 10 | **Roll Twice or Amplify** | Two minor complications hit at once, or one threat escalates into a dramatic movie moment! |

> ✅ **DECIDED — no "damage."** V5's entry 7 reads "take extra damage." Per the vocabulary
> decision, this doc says "1 extra Readiness loss" (the word "damage" is avoided).

---

## 10. Narrative Direction: Guided vs. Co-op Play

The single goal of the game is to tell the coolest, most cinematic story possible. Every
mechanic — from 2d6 resolution to the Antagonist Track — is a "story rule" that
pushes the plot forward.

### When Nobody Knows What Happens Next (Ask the Oracle)

Between scenes, if the table goes quiet and no one's sure what comes next, turn here. This
is the Co-op engine for keeping the movie rolling without a Guide (a Guide can lean on it
too). Work down the list and stop the moment you have something to play.

**First, find your next Milestone.** The fastest way to get unstuck is to name what the
heroes are trying to do *right now*. Look at your Story Arc Track — what's the next box? If you
haven't decided the next Milestone yet, decide one now, pulling from everything already on
the table: your **Worldbuilding** answers (the Threats, the Forbidden, the Leadership, the
Reputation), the characters and their Assets, the **NPCs and places you've already met or
heard about**, and any **other Story Arcs** you have running. The next scene is almost always
"a step toward the next Milestone."

Then frame the actual scene — pick whichever fits:

1. **Do the obvious thing.** Talk it out as a group: what would clearly happen next in this
   movie? Usually someone already knows. Run with it.
2. **Spark it.** Want a surprise? Roll the **Story Spark** below and bend whatever you get
   toward the next Milestone.
3. **Ask the Dice (yes/no).** If it's really a yes/no question ("Is the gate guarded?"),
   roll **1d6: 1** = No, and worse · **2–3** = No · **4–5** = Yes · **6** = Yes, and more.
   (If the answer's likely, roll +1; unlikely, −1.)

**Story Spark (d6)** — bend the result toward your next Milestone:

| d6 | Spark |
|---|---|
| 1 | **A new face** arrives — an ally, an enemy, or someone you can't read yet. |
| 2 | **A discovery** — you find or notice something important. |
| 3 | **The threat closes in** — the antagonist or the world makes a move against the heroes. |
| 4 | **A door opens** — a clue, a shortcut, or a lead toward the Milestone. |
| 5 | **A cost surfaces** — something you need is missing, broken, or guarded (roll Pay the Price for flavor). |
| 6 | **A hard choice** — two good paths pull in opposite directions; pick one. |

### Playing with a Guide (Guided Play)

One person steps into the role of the **Guide** (the Director).

- **No Prep, Pure Improv.** Start with an empty sheet, ask the kids the 10 Worldbuilding
  questions, and begin *in media res.*
- **Always Ask the Oracle.** When you don't know an answer, don't make it up — turn to the
  kids: *"What scary thing is blocking the bridge?"* Their answers build the world.
- **You frame the cuts and play the world.** Between beats the Guide narrates the cut to the
  next scene, and voices the NPCs, creatures, and forces the heroes meet.

### Playing Without a Guide (Co-op Play)

Everyone is a player, sharing the directing duties equally.

- **The Golden Rule — "Do the Obvious or Coolest Next Thing."** Introduce the most logical
  or dramatic thing that would happen next.
- **Who Decides the Price?** The player who rolled has final narrative rights over the
  complication that hits their hero. If stuck, brainstorm with the table.
- **Share the director's chair (popcorn).** Framing scene transitions rotates just like
  turns in a Challenge: if you narrated the cut into the last scene, let someone else set up
  this one. Spread the spotlight so no one player runs the show.
- **Playing an NPC.** When you speak for an NPC, your own hero steps back from that
  conversation — you can't really argue with yourself, so let the others deal with the NPC
  (especially for back-and-forth dialogue). Or the table can **group-narrate** an NPC,
  deciding together what they say and do — fine for big moments, but it slows things down, so
  save it for when it matters.

> ✅ **DECIDED — Readiness recovery (2026-06-09, reverses the 2026-06-05 rule).** The drafts'
> "recover 1 between Challenges" loop was rejected, *and* so is the interim "Recovery Scene:
> flat +3, never roll." Recovery is now **rolled** via two moves — **Mend** (short rest) and
> **Downtime** (long rest). Full spec + rationale in **Section 7**; balance in
> `Math & Simulation Reference.md` §3/§3a (the **SF-C** model). Headlines: recovery **never costs
> Readiness** (a Miss fails to heal, never downward); **Mend** is once-per-hero-per-Milestone,
> lull-gated, targets **self or ally**, Strong +3 / Weak +2 / **Miss = no heal + complication**;
> **Downtime** is dependable, Strong +7 / Weak +6 / Miss +6 **+ owe a Story Arc**; finishing a Story Arc
> prompts Downtime (absorbs the old +6 victory bump); max Readiness stays 9.

---

## Appendix: Reconciliation Summary

> 🔁 **SUPERSEDED by the spine-model rework (2026-06-13).** The single biggest change since these
> entries: **sandbox play is dropped.** Several decisions logged below are now obsolete and are
> retained only for the reasoning trail — the canonical rules are §6/§7/§9 above. Specifically
> superseded: *"Four Story Arc types + unified headway rule"* (now **two individual sizes** —
> Episode 3/2, Movie 6/3 — with Season/Series as **prose collection patterns**); *"Antagonist
> Track flee-primary + optional telling-failure tick"* (now advances **only on a Recovery
> Scene**, with a **reserved climax box**); *"rolled SF-C recovery"* (now **two moves**: a small
> risky **Mend** — Strong +3 / Weak +2 / **Miss −1**, no surge, an any-scene tactical patch —
> plus the full-reset **Recovery Scene** that surges the villain; Downtime is the between-Stories
> reset); and *"multiple concurrent arcs / no feed-up"* (now **one nested spine**, with B-plots as
> lose-clock-free threads). New model validated in `Math & Simulation Reference.md` (spine-model
> section, `sim_spine.py`).

**V5 is authoritative.** It is the newest and most complete draft, and it supersedes V3/V4
wherever they differ. Mechanics V5 introduced (now canonical above): the **Antagonist
Track**, the **Regular vs. Challenge Roll** split, the **Pacing / 40-Minute Rule** section,
the **Challenge Turn Loop** and end-of-Challenge procedure, the **Concept formula + Golden
Question**, the detailed **Asset** guidance, the three-pillar **Readiness** breakdown, the
fifth Core Principle, and the *Amazing Tales* **starter-backdrop** option.

**Kept from V3/V4 (not in V5, still useful):**
- The **"Retrieve the Sun Crystal"** nested-Milestone example (Section 6).
- Fuller flavor wording in the **Pay the Price** table (Section 9).

**Design additions beyond the drafts (Ian's calls, 2026-06-05 / -06-06 / -06-08):**
- **Four Story Arc types + unified headway rule (2026-06-12); *Quest* → Story Arc, *Campaign* → Series.**
  Replaces the old Episodic/Season/Campaign "nested scales" + feed-up model (itself a replacement for
  the 3/4/5 Easy/Medium/Hard scale). **Episode (3) / Movie (8, or 12) / Season (8) / Series (12)** —
  pure *labels* over box-count + narrative life, **no per-type machinery.** One rule at every type:
  mark a box on significant headway (a Milestone); a single beat may mark several arcs at once.
  **Feed-up/nesting removed** — a smaller arc no longer fills a larger one. Long arcs have **no
  progress floor** (a filler run is Episodic play earning its own Growth). Canonical example
  *Avatar: The Last Airbender* (Episode / Season / Series) (Section 6).
- **Antagonist Track is CORE; flee-primary, table-discretion-broadened (2026-06-06 / -06-08).**
  Mandatory on every Story Arc. **Fleeing a Challenge** is the always-on trigger (lose its progress +
  advance the villain). Broadened 2026-06-08: on a **telling failure** the table *may* also mark a
  box via **Pay the Price** (narrate the antagonist's gain) — never automatic, the main way
  Season/Series villains advance. Not advanced by ordinary Weak/Miss or Recovery. Added
  **characterize-your-antagonist** (the foe can be a force, e.g. a desert). Added **Quit the
  Story Arc** (terminal flee, no penalty/bonus) and "losing seeds a new Story Arc." Flee-only floor
  modeled in `Math & Simulation Reference.md` §4b; optional tick is discretionary/unmodeled
  (Section 6/7/9).
- **Tighter Asset definition** — Assets do double duty (stat + special ability); added
  good/avoid lists, a one-sentence trigger, and the win-rate math (Section 4).
- **Regular-vs-Challenge** is an explicit group/story call with no reward for rushing;
  **popcorn turn rule** (everyone acts before anyone repeats) (Sections 5, 7).
- **Aid Your Ally** added — teamwork **variant of the core move** (defined in Ch.7), same
  +2/+1 math and same Pay the Price as any roll: Strong = ally +2; Weak = ally +1 and aider
  −1 Readiness; Miss = no bonus and aider −2 (Section 5). *(Corrected 2026-06-09: earlier
  draft wrongly said Aid never costs Readiness and lived in the Challenge chapter.)*
- **Rolled recovery — two moves (2026-06-09, reverses the flat-+3 Recovery Scene; tuned to
  SF-C).** Healing is the core move and **never costs Readiness** (a Miss fails to heal, never
  downward) — but to keep the Readiness track's teeth (sim: reliable on-demand healing flattens
  all tension), it's made Starforged-style infrequent + unreliable. **Mend** (short rest;
  **self or ally**; lull-gated; **once per hero per Milestone**): Strong +3 / Weak +2 / **Miss =
  no heal + complication**. **Downtime** (long rest, one group roll, dependable): Strong +7 /
  Weak +6 / Miss +6 + owe a Story Arc. Max Readiness stays 9; neither advances the Antagonist Track.
  Defines Out of Action recovery, which now can whiff (Section 7; balance in Math doc §3a).
- **Broken Assets — durable-teeth layer (DECIDED 2026-06-09).** Going Out of Action breaks
  **one Asset** (the one that failed you), which gives **no +2** (rolls fall to +1) until
  **Downtime restores it — one per rest.** Never a penalty (preserves the +1 floor, zero new
  math); we break an existing Asset rather than add a negative modifier. The durable consequence
  layer (Starforged "impacts") a recovering Readiness track lacks; scoped to Out of Action only.
  Distinct from advancement's Trade In (temporary/free/involuntary vs. permanent/costs-Growth/
  chosen). Optional Guide flavor: free-floating **conditions** (*Broken Spirit*) that work the
  same way (Section 7; new **Broken Asset** Vocabulary row; touches §4 Assets + Ch.13).
- **Victory bump folded into Downtime (2026-06-09).** Completing a Story Arc *prompts* Downtime
  (the +6-each heal now lives there, rolled), still enabling **multiple ongoing Story Arcs** (no
  clean start/stop) (Section 7).
- **Showdown** added — optional climactic last-box roll; a miss adds a box + escalates,
  never an outright loss; never advances the Antagonist Track. Applies to a Challenge Track
  **or** the Story Arc Track — the **Story Arc Showdown** (2026-06-06) turns the final Milestone into a
  roll whose Miss adds a Milestone box + a plot twist ("you thought it was over…") (Section 7).
- **Ask the Oracle** added — the Co-op "what happens next" move: name the next Milestone
  first, then do the obvious thing / roll the **Story Spark** d6 / roll the **Ask the Dice**
  yes/no (Section 10).
- **Start a Story Arc opening roll (2026-06-09).** A **Progress move**: one **2d6 + 1** roll when a
  Story Arc begins, **generative not pass/fail**, setting the tone of its opening (*Clear purpose* /
  *More questions than answers* / *Trouble finds you first*). Modeled on *Swear an Iron Vow* minus
  the momentum reward; uses the full core roll so the Strong/Weak/Miss ladder carries the
  good/middle/poor shape; Oracle's Blessing applies. No balance impact. Part One skips it; Part
  Two (Ch.10) teaches it. Also introduced the **Action vs. Frame** move families as the organizing
  lens for the new **The Moves (Master List)** in Section 5 (Sections 5, 6).
- **Co-op directing rules** added — scene transitions and NPC voicing rotate popcorn-style;
  playing an NPC sidelines your own hero; group-narration option (Section 10).
- **"Narrate the Change"** principle added — a Hit means the player narrates how the scene
  changes; that change *is* the progress (covers investigation; clue-searches can be
  Challenges) (Section 5).
- **Opposition model stated** — enemies/obstacles have no stats or Readiness (you beat them
  by filling tracks); heroes can't die — worst case is Out of Action / losing the Story Arc
  (Section 7).

**Decisions locked in:**
- ✅ Facilitator term: **"Guide,"** not "GM"/"Game Master" — applied throughout.
- ✅ Play-mode term: **"Co-op play,"** not "GMless"/"Guideless" — applied throughout.
- ✅ The **Antagonist Track** is **CORE** (mandatory on every Story Arc). It advances **primarily by
  fleeing a Challenge** (2026-06-06), and may **optionally** be ticked on a telling failure via
  Pay the Price (2026-06-08) — never automatically; recovery moves never advance it. Added
  **Flee** and **Quit the Story Arc**; losing a Story Arc seeds a new one.
- ✅ **Four Story Arc types** — Episode (3) / Movie (8–12) / Season (8) / Series (12); labels over
  box-count, one unified headway rule, no feed-up (2026-06-12). Supersedes the Episodic/Season/Campaign
  nested scales and the 3/4/5 Easy/Medium/Hard scale.
- ✅ **Pay the Price #7** says "Readiness loss," not "damage."
- ✅ Principle 3 wording resolved by V5 ("lose footing or take a setback").
- ✅ **Max Readiness is 9** (flat — no scaling by party size).
- ✅ **Readiness recovery (rolled, 2026-06-09; SF-C tuning)** — two moves; recovery never costs
  Readiness (a Miss fails to heal, never downward), but is kept infrequent + unreliable so the
  track keeps its teeth. **Mend** (short rest; self or ally; lull-gated; once per hero per
  Milestone): Strong +3 / Weak +2 / Miss = no heal + complication. **Downtime** (long rest, group
  roll, dependable): +6/+7, Miss = owe a Story Arc. Both capped at 9; finishing a Story Arc prompts
  Downtime (absorbs the old +6 victory bump). Max Readiness stays 9. Old "+1 between Challenges"
  loop, the interim flat-+3 Recovery Scene, and the (one-day) "always-heals" rolled version all
  rejected.
- ✅ **Multiple Story Arcs can run at once** — the old "one active adventure" rule is dropped.

- ✅ **Asset modifier — +2 / +1.** +2 when an Asset applies, +1 for anything else. The +1
  floor (not +0) keeps off-niche actions from feeling hopeless; this is the scheme all the
  balance/simulation work and the max-9 target assumed.

- ✅ **Character advancement (2026-06-08)** — **horizontal** growth via a per-hero **Growth
  Track**: earn 1 **Growth** every 3 Milestones (cumulative, never resets per arc); spend **2** on a **Boon** (a once-per-
  Scene/Session signature move on an Asset, max 2/Asset) or **5** on a **New Asset** (ceiling
  6; **Trade In** one to exceed). Never adds a *permanent* modifier (a banked once/Session +1
  to a single roll — **Dig Deep** — is allowed, the same safe lever as the Start-a-Challenge roll, §4c),
  so the curve and enemy tracks need no rescaling. ("Widen the Domain" considered and cut as
  the lone non-horizontal option.)
  Section 4, Step 4.

- ✅ **Start a Story Arc opening roll (2026-06-09)** — one **2d6 + 1**, generative (never a failure),
  made when a Story Arc begins to set its opening tone. A **Progress move** (originally filed as the
  first "Frame move," before the three-family revision); Part One skips it. See Sections 5–6 and
  **The Moves (Master List)**.

- ✅ **Three move families: Action / Progress / Frame (2026-06-09, revised same day)** — the
  move families are Standard Vocabulary terms, not just an organizing lens. Originally split two
  ways (Action / Frame); **revised to three** because the old "Frame" family was doing two jobs —
  opening/closing tracks *and* coloring the fiction. **Action move** = resolves a hero's attempt
  (2d6 + 2/+1, adjudicative); **Progress move** = opens or closes a progress track (Start a Story Arc,
  Start a Challenge, Flee, Quit the Story Arc); **Frame move** = shifts the fiction in the moment, no
  track (Ask the Oracle, Pay the Price). The printable **Moves Cheatsheet** (Part Four) lists every
  move under these three headings. See the vocab table and **The Moves (Master List)**.

- ✅ **Start a Challenge opening roll (2026-06-09)** — a new **Progress move**, the twin of Start
  a Story Arc, rolled once when the heroes *deliberately initiate* a Challenge (skipped when trouble is
  thrust on them). **2d6 + 1**, generative (Oracle's Blessing on doubles): Strong → **+1** to the
  first Challenge Roll, Weak → 0, Miss → **−1**. A one-time bonus to a single roll (the bonus/penalty
  applies to the single first roll, then it's gone), so it never rescales the +2/+1 curve. Sim-cleared as a
  negligible, mostly-flavor nudge — `Math & Simulation Reference.md` §4c. Confirms a temporary ±1
  to a single roll is a safe lever, distinct from the "never bigger numbers" rule on *permanent* advancement.
  See Ch.8 and **The Moves (Master List)**.

**Still open (need a call):**
- All core-mechanics *numbers* are settled; remaining work is playtesting and tuning.

---

## Notes for the Main Handbook (not core mechanics)

Items that matter but belong in the player-facing handbook, not this mechanics reference:

- **Safety & tone tools.** A light line (for ages 10+) empowering anyone at the table to
  skip or soften content that's too scary or not fun. Important, but it's a safety guide,
  not a mechanic.
