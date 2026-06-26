# Lights, Camera, Action! — Core Mechanics Master Reference

> ✅ **Reworked 2026-06-22, then again 2026-06-25** to the current model (see memories
> `dice-and-scaling-rework` + `miss-doubles-clock-proposal`, Math & Sim §0, and
> `PROPOSAL - Miss-Doubles Antagonist Clock.md`). The text below has been brought into line:
> - **Core roll is now +0 / +1 / +2** (2026-06-22). You pick **2 of the 5 stats** (most-relevant chosen
>   objectively → +1) and have **3 specific Assets** (argued → +1); both → +2, neither → +0. The
>   single broad **"Attribute" mechanic is retired** (the closed-five list survives as Stats — you pick two).
> - **No recovery ratchet** (2026-06-22). A Recovery Scene heals the party **fully to 9**; max Readiness
>   no longer declines.
> - **Antagonist-clock rework — the Devil's Bargain spine (DECIDED 2026-06-25).** **Recovery is now
>   FREE** — a Recovery Scene heals to 9 and **never advances the villain.** The old "surge on the
>   Recovery Scene," the term **"Surge,"** and the **"reserved climax box"** are all **RETIRED.** The
>   Antagonist Track advances **one box in exactly three ways:** a **Devil's Bargain** (on a Miss, a
>   hero may refuse the Readiness loss *and* upgrade the Miss to a Strong Hit, for villain +1 — never
>   on a knockout roll), a **Miss showing doubles** (villain +1; doubles now upgrade *only* a Hit), and
>   going **Out of Action** (villain +1 + an Asset breaks). The narrated villain beat is an **Attack**
>   on the track's **odd boxes;** the **last box = the villain wins.**
> - **Track sizes (2026-06-25): Episode = 5 boxes, Movie = 9 boxes — the SAME at any party size**
>   (the duo/two-player special case is GONE).
> - **Challenge difficulty is fixed by difficulty, not party size (2026-06-25, "Option B"):**
>   **Easy 2 / Medium 3 / Hard 4 / Very Hard 5** — party-independent, no party-size rules anywhere.
>   (Supersedes the 2026-06-22 plain p−1/p/p+1 ladder.)
> - **Loss is no longer a tuning target** — it's a rare earned tail; the tuned metric is the
>   **photo-finish** (villain one box from winning at the climax). Validated by `sim_devils.py` /
>   `sim_devils2.py`.

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
| **Stat** | One of a character's two broad "naturally good at" areas, from a closed five — **Strong** (force & force of personality, incl. intimidation), **Quick** (overt dexterity — agility, speed, aim), **Clever** (knowledge, reasoning, observation), **Sneaky** (stealth, deception, thievery), **Charming** (winning people over). The relevant Stat is chosen **objectively** by what the action calls for (never argued); add **+1** when it's one of your two. | Attribute, stat (lowercase), ability score |
| **Asset** | One of a character's three specific "amazing at" things — a signature talent, tool, or friend; argued via the one-sentence test, **+1** when it fits. | skill, stat, trait |
| **Broken Asset** | An Asset knocked offline when a hero goes Out of Action — gives no +1 until **Downtime** restores it. Temporary; never a penalty. | negative Asset, debuff, condition, impact |
| **Readiness** | The single 0–9 resource track (health + morale + supplies). Max stays **9** all game. | HP, health, hit points, stamina |
| **Mend** | The small, risky **any-scene** patch (in a Challenge, it's your turn instead of a Challenge Roll): recover a little — self or ally, rolled **Strong +3 / Weak +2 / Miss −1 Readiness** (capped at 9). **No usage cap; never advances the villain; can't revive Out of Action.** The −1 risk keeps it from substituting for a regroup. | heal, Catch Your Breath |
| **Recovery Scene** | The fall-back-and-regroup move: the party heals **fully back to 9** — **free** (no roll, no cost to the villain's clock). Reliable; the quiet/B-plot beat. **Recovery never advances the Antagonist Track.** | rest, healing |
| **Downtime** | The between-Story-Arcs rest: heals everyone to full and **restores any Broken Asset**. Free; the villain's clock resets. | long rest, Sojourn, victory bump |
| **Out of Action** | State when Readiness hits 0. | dead, KO'd, defeated |
| **Story / Story Arc** | One spine — a single central dramatic question — tracked with a **Story Arc Track** (progress) and an **Antagonist Track** (the villain's clock). Sized **Episode** or **Movie** (the only two with box machinery). | Quest, mission, adventure |
| **Episode** | A complete short Story — **3 Milestones, 5-box Antagonist Track** (Attacks on 1·3·5) — told in ~one sitting. Same track size at any party count. | one-shot, session quest |
| **Movie** | A complete feature Story — **6 Milestones, 9-box Antagonist Track** (Attacks on 1·3·5·7·9) — told over ~2–3 sessions. Same track size at any party count. | feature film |
| **Season** | A **collection** pattern (prose, no machinery): a run of Stories sharing a throughline. Not a box size. | arc (as the term), story arc |
| **Series** | A **collection** pattern (prose): the whole game, a run of Seasons. Always a collection; no box size of its own. | campaign, saga |
| **Story Arc Track** | A Story's progress track — one box per Milestone; filling it reaches the Showdown. | Hero Track, Quest Track |
| **Antagonist Track** | The losing side of the same Story: the villain's clock — **Episode 5 boxes / Movie 9 boxes** (same at any party size). Advances **one box** in exactly three ways: a **Devil's Bargain,** a **Miss showing doubles,** or a hero going **Out of Action.** Its **odd boxes are Attacks** (narrated villain beats); even boxes are silent pressure; the **last box loses the Story.** | enemy clock, doom track |
| **Devil's Bargain** | On a **Miss,** a hero *may* refuse the Readiness loss **and** upgrade the Miss to a **Strong Hit** — in exchange for advancing the Antagonist Track **one box.** Always optional; **never allowed on a roll that would knock the hero Out of Action.** The main engine of the villain's climb. | — |
| **Attack** | The narrated villain beat played out when an **odd box** of the Antagonist Track fills (1·3·5, plus 7·9 on a Movie): cut away and show the bad guys gaining ground on-screen. Even boxes pass silently. The **last Attack box is the villain's victory.** | the Surge |
| **Showdown** | The climax — reached when the heroes fill the Story Arc Track, played as one last roll. The Story's outcome is decided here, usually with the villain's clock near its last box. | finale, boss fight |
| **Thread (B-plot)** | A subplot/character arc riding alongside the spine: a light progress track, **no Antagonist Track / no lose-clock**; resolves into or beside the spine's climax. | side quest, B-arc |
| **Fall back** | Retreating from a losing Challenge (losing its progress) to regroup — handled as a **Recovery Scene** (full heal, **free**, no villain advance). | Flee, retreat (as the mechanic) |
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
| **Oracle's Blessing** | The doubles-upgrade rule — doubles upgrade a **Hit** one tier. On a **Miss,** doubles do *not* upgrade; instead they advance the Antagonist Track one box. | crit, critical |
| **Outstanding Success** | Doubles on a Strong Hit. | crit success |
| **Ask the Oracle** | The stuck-point move for deciding what happens next. | — |
| **Story Spark** | The small d6 idea table inside Ask the Oracle. | oracle table |
| **Ask the Dice** | The 1d6 yes/no oracle. | — |
| **Move** | Any defined procedure you invoke at the table. Every move is an **Action**, **Progress**, or **Frame move**. | maneuver, action (as the mechanic) |
| **Action move** | A move that *resolves a hero's attempt* — rolled 2d6 + 0/+1/+2 and read Strong/Weak/Miss; the dice **adjudicate** (did you pull it off?). | — |
| **Progress move** | A move that *opens or closes a progress track* (a Story Arc or a Challenge). The openers (Start a Story Arc, Start a Challenge) roll generatively to set how things begin; the closers (Fall back, Quit the Story Arc) are deterministic. | — |
| **Frame move** | A move that *shifts the fiction in the moment* (no track); when it rolls, the dice **generate** a direction rather than judge a hero, so it can never be "failed." | framing move, GM move |
| **Growth** | The advancement currency; earn 1 every 3 Milestones, spend on Boons/Assets. | XP, experience, levels |
| **Growth Track** | The per-hero row of boxes tracking earned Growth. | — |
| **Boon** | A once-per-Scene/Session signature move bought (2 Growth) onto an Asset card. | perk, feat, ability |
| **Trade In** | Retiring an Asset to make room for a new one at the 6-Asset ceiling. | — |
| **Genre** | The mood/feeling of the story — Worldbuilding Question 1. One of seven official genres. | theme; a *setting* used as the genre |
| **the seven genres** | The official set: **Adventure, Mystery, Horror, Sci-Fi, Caper, Drama, Post-Apocalypse.** | inventing alternate names for these |
| **Caper** | The official genre for clever, stylish heist/con stories (the heist *tone*). | Heist (as the genre name) |
| **Drama** | The official genre for juicy interpersonal stories (gossip, rivalry, love, stress). | Cozy Drama, Slice-of-Life |
| **tonal dial** | The playful↔serious scale every genre runs on; set per table. | tone slider, intensity setting |
| **Genre Kit** | A per-genre toolkit (Ch. 15): the feel, Worldbuilding prompts, archetypes, d100 Assets. | Starter Backdrop |

> ✅ **DECIDED — "Guide," not "GM."** Ian confirmed (2026-06-05) the facilitator role is
> the **Guide** throughout, because it fits the kid-friendly, collaborative tone. All "GM"
> / "Game Master" wording from the V4/V5 drafts is superseded.

> ✅ **DECIDED — "Co-op play."** Ian confirmed (2026-06-05) that play without a Guide is
> called **"Co-op play"** (not "GMless" from the drafts, nor the interim "Guideless").

> ✅ **DECIDED — seven genres + tonal dial (2026-06-09; Post-Apocalypse added later).** *Lights, Camera, Action!* officially supports
> **seven genres — Adventure, Mystery, Horror, Sci-Fi, Caper, Drama, Post-Apocalypse —** each playable along a
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
picks two Stats and three Assets, and sets their starting Readiness (Section 4).

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

### Step 2: Two Stats and Three Assets

A hero is defined by two layers that stack on every roll: **two Stats** (the broad kinds of
action they're naturally good at) and **three Assets** (the specific tools, talents, and
relationships they rely on). Pick the Stats first, then the Assets.

**Pick 2 Stats.** Choose **two** from a closed list of five. Each is broad — a whole category
of action — and on a roll you add **+1** whenever the action calls for one of your two.

| Stat | Covers |
|---|---|
| **Strong** | force *and* force of personality — muscle, toughness, endurance, intimidation |
| **Quick** | agility, reflexes, speed, aim — dodging, climbing, piloting, deft hands in the open |
| **Clever** | knowledge, reasoning, observation — knowing, figuring out, noticing, reading people |
| **Sneaky** | stealth, deception, thievery — moving unseen, lying, disguise, sleight of hand, picking locks |
| **Charming** | winning people over — persuading, rallying, comforting, inspiring, performing |

Picking two means *not* picking the other three: your hero shines when a scene calls for one
of their Stats and sweats when it calls for the rest. That trade-off is where the drama lives.

**Resolving overlaps (objective tiebreakers).** When two Stats both seem to fit, two tests keep
the choice objective rather than argued:
- **Strong vs. Quick** — power, leverage, and endurance are **Strong**; finesse, speed, and
  precision are **Quick.** (Bash the door = Strong; pick its lock = Sneaky; vault the wall = Quick.)
- **Acting on a person** — *win them over* so they want to help = **Charming**; *make them afraid*
  so they yield = **Strong** (force of personality); *deceive* them into believing something false
  = **Sneaky**; merely *reading* them = **Clever.**

**Why there is no "willpower" Stat.** Holding your nerve, keeping composure, not breaking under
fear — real, and central to Horror/Drama — but **reactive**: something you *endure*, not something
you *do.* It therefore lives in **Readiness** (you spend Readiness when rattled; Out of Action is
the break), never a Stat. Stats are for the proactive thing a hero *attempts* — which is why
*intimidation* (acting on someone) is Strong, while *resisting* intimidation is just Readiness.

> ✅ **DECIDED — 2 Stats + 3 Assets (2026-06-12; revised 2026-06-22).** Borrowing Starforged's
> *stat list* (the closed five — Strong, Quick, Clever, Sneaky, Charming — **not** its
> separate-stat mechanic): a hero picks **two Stats** as their natural strong suits plus **three
> specific Assets.** The single broad **"Attribute" mechanic is retired** (history: 2026-06-12
> made a hero's first Asset one broad Attribute capped at one; the 2026-06-22 rework split that
> into an objective **Stat** layer and the flexible **Asset** layer). A Stat is broad but **not
> universal** — each does nothing for a whole category of action (Strong does nothing to notice
> a clue, charm a guard, or sneak past one), which is what keeps a wide **+0 floor** where the
> Miss-tension lives. Unlike an Asset, the relevant Stat is **chosen objectively** by what the
> action calls for (a chase is Quick, a feat of force is Strong) — never argued. Splitting an
> objective Stat layer from the argued Asset layer restores the floor that one broad always-on
> Attribute had eroded (players could bend any of four Assets into fitting, so +2 was
> near-universal). Balance validated in `Math & Simulation Reference.md` §0.

**Pick 3 Assets.** Your **Assets** are the specific signature talents, tools, and friends your
hero is known for — the things that earn an extra **+1** when they fit the moment. Choose three.
A blank page is the hard part, so answer three questions:

- **What are they known for?** A **role or signature skill** — the thing people call them for, a
  tight title that names *who they are*: Ace Pilot · Fire-Mage · Tracker · Field Medic ·
  Cat Burglar · Locksmith. *(Lead with this. A good Asset answers "who is this hero?", the
  way "Ace Pilot" does and "a sturdy backpack" doesn't.)*
- **What's the one thing they're never without?** A signature **item, companion, or connection**
  — but one that could only be *theirs*: Grandpa's Lockpicks · A Loyal Pet Wolf · A Debt Owed by
  a Crime Boss. The test: *would this be the same in anyone's hands?* If yes, it's interchangeable
  kit — pick something loaded with story instead.
- **One more — your call.** A **Wild** pick: another role, a quirky talent, a second signature
  thing — anything that makes the hero yours.

This is the recommended path, not a cage — slots may be rearranged freely. When defining an
Asset, consider *how* the character got good at it; that instantly builds backstory.

> ✅ **DECIDED — recommended creation template (2026-06-12, the "questions"; revised
> 2026-06-22).** To beat the blank-page problem, creation is presented as ordered questions:
> **pick your 2 Stats, then 3 Assets** (trained skill / signature item-or-companion / wild pick;
> for concepts with no gear or buddy, slot 2 may be a **Connection** — mentor, contact,
> reputation). The Asset slots are a guiding default the player may rearrange. Purely a
> creation-flow scaffold — no mechanical weight beyond the Stats and Assets themselves.

**What makes a good Asset.** The master test is the **trigger**: finish *"You add +1 when…"* —
a good Asset completes it cleanly with a situation that **comes up in ordinary play.** That
single test catches both failure modes: too vague to finish the sentence (it's a Stat), or so
specific the trigger almost never fires (e.g. "Arson Investigator"). Two supporting checks:
**it tells you who the hero is** ("Ace Pilot" paints a person; "a sturdy backpack" doesn't), and
it's **pointed** — clearly *doesn't* cover everything, with obvious moments where it's useless.
Genre Asset tables present each entry *as* its trigger (`Asset | You add +1 when…`). Assets are
**facet-identities** — one mastery/role each (Swordmaster, Healer, Locksmith), the bricks that
build the broader **Archetypes** (Paladin = Templar + Healer + Ironclad). Your *Stats* are the
broad layer, so let Assets be pointed and identity-bearing.

- ✅ **Good:** Ace Pilot · Fire-Mage · Cat Burglar · Tracker · My Loyal Wolf · Grandpa's
  Lockpicks · Field Medic. *(Each names a person, and each has obvious situations where it's
  useless — that's the sign it's well-sized.)*
- ❌ **Just a Stat, reworded — avoid:** "Moving Quietly" (that's Sneaky), "An Iron Grip"
  (Strong), "Quick Reflexes" (Quick), "Effortless Charm" (Charming). *(These restate the Stat
  layer, so they never switch off — they fail the sizing test and define nothing.)*
- ❌ **Just a prop — avoid:** "A Sturdy Backpack," "A Flashlight." *(Interchangeable kit;
  it'd be the same in anyone's hands and tells you nothing about the hero. Load it with story —
  whose backpack, and why does it matter? — or pick a role instead.)*
- ❌ **The genre's premise — avoid:** if *every* hero in the genre already is one, it's too
  broad to mean anything (it would apply to most rolls — the old always-on-+1 problem). In a
  mystery everyone's a "Detective"; in a wasteland everyone's a "Scavenger" — those are
  **Concepts**, not Assets. Pick the *specialty* within (Forensic Analyst, Interrogator;
  Mechanic, Demolitionist). Genre Asset tables must list specializations, never the premise.
- ❌ **Too broad — avoid:** "Lucky," "Skilled," "Good at everything." *(These would help on
  literally **any** roll, so they stop meaning anything — that's what your Stats are for.)*
- ❌ **Too narrow — avoid:** "Picking brass locks," "Arson Investigation." *(If the trigger
  only fires in a rare, specific scenario, the Asset sits dead most of the game.)*
- ❌ **"I win" powers — avoid:** "Invincible," "Mind Control," "Always Succeeds."

**Rolling — two questions, each worth +1:**

- **+1 — a relevant Stat:** ask what the action *calls for* (objectively — a chase is Quick, a
  feat of force is Strong); if that Stat is one of your two, add +1. You don't argue this.
- **+1 — a fitting Asset:** you get +1 when you can say, in *one sentence*, how this exact Asset
  solves this exact problem, using fiction that's already true. This one you do argue.
- **+2 — both.** **+0 — neither:** you can still always try, but you're rolling the bare dice.

> ⚠️ **NOTE — the math.** Rolls land at **+0 / +1 / +2** depending on how many of the two
> questions hit. With **+2** (a relevant Stat *and* a fitting Asset): ≈42% Strong / 42% Weak /
> 17% Miss — an ~83% hit rate. With **+1** (one of the two): ≈28% Strong / 44% Weak / 28% Miss.
> With **+0** (neither — out of your element): the bare 2d6 curve, a real gamble. The **+0 floor**
> (replacing the old +1 floor) is the new edge of danger: reaching outside everything you're good
> at is a genuine risk. Splitting the objective Stat layer from the argued Asset layer keeps the
> average modifier honest (≈1.40, tuned to stat≈55% / asset≈85% apply) where one always-on broad
> Attribute had pushed +2 toward near-universal. See `Math & Simulation Reference.md` §0.

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
> heroes gain new tools and signature moves, never bigger numbers** — so the +0/+1/+2 curve and
> the max-9 Readiness cap are never touched, and **enemy/Challenge/Antagonist tracks never
> need rescaling.** The game is exactly as hard for a starting hero as for a campaign veteran;
> the veteran simply has more options and more spotlight moments.

- **Growth (the currency).** Each hero tracks their own **Growth** on a **Growth Track** (a
  simple row of boxes on the sheet). **Every 3rd Milestone the party marks — on any Story Arc —
  each hero earns 1 Growth** (all heroes tick together, exactly as everyone used to score on a
  shared win). Count every Milestone the party marks on the **main spine** and on **shared B-plot
  threads** (party-wide). **A character-specific B-plot is the exception: its Milestones credit
  Growth to that one hero only**, not the party. (See the DECIDED note below.) The tally is
  **cumulative across the whole game and never resets per arc**, so no Milestone is ever wasted — a 4-box "stretched Episode" carries its 4th Milestone
  toward the next Growth. This ties Growth to **headway actually played, not arcs finished**, which
  closes two holes the old "1 per Story Arc" rule had: a standalone Movie/Season can no longer be
  *starved* (it pays out as you play it, not only on completion), and a slow arc can no longer be
  *gamed* (stretching one arc over many sessions earns no more than playing it briskly). Rough
  feel: an Episode (3 boxes) ≈ 1 Growth ≈ one session of play; a Boon lands every ~2 sessions, a
  New Asset every ~5. Growth rate is a pure feel knob — Boons are horizontal (§ below), so faster
  Growth never rescales the +0/+1/+2 curve or enemy tracks.
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
    levers, not menu effects): marking extra track progress; preventing Out of Action; erasing an
    Antagonist Track box.
  - **Cadence is derived, not chosen.** Strong effect → **once/Session**; Mild → **once/Scene**;
    **lock the Trigger to a named situation → one step more often** (a Strong effect drops to
    once/Scene). This *is* the "narrow the trigger, widen the effect" trade, made mechanical, and
    it answers the old once-Scene-vs-Session question by construction.
  - **+1-type effects are temporary one-roll bonuses,** the same safe lever as the Start a Challenge roll
    (sim-cleared, `Math & Simulation Reference.md` §4c) — **never** a permanent modifier, so the
    +0/+1/+2 curve and enemy tracks still never rescale.
  - **Recipes (pre-built combos, presented by name in the book):** Signature Move (any time +
    Upgrade, Session), In My Element (situation + Upgrade, Scene), Dig Deep (any time + +1 to roll,
    Session), Reliable (any time + Reroll, Scene), Lend a Hand (help an ally + Lend a reroll, Scene),
    Mender (when you Mend + Steady Hands), Scout (any time + Free Oracle, Scene), Take the Hit (any
    time + Take the Price, Session). Each genre kit carries a **d10 Boon-trigger table** (all 7 done).
- **Asset ceiling: 6.** A hero starts with three Assets and can buy up to three more. Beyond six
  there are no new slots — buying a seventh means **Trading In** one of the existing six (a
  "your hero outgrew that" story beat); it still costs the full 5 Growth.
- **"Widen the Domain" was considered and cut.** A boon that broadened an Asset's coverage
  (more +2 frequency) was the lone non-horizontal option — it re-introduced power-creep and
  the "Lucky" problem the Asset rules warn against, and its benefit (broader coverage) is
  already served by buying a **New Asset**. All growth stays horizontal. *(This does not
  conflict with **Stats** at creation: Widen-the-Domain was an unbounded, repeatable,
  buy-with-Growth broadening of an arbitrary Asset that could stack toward "good at
  everything." Stats are a fixed pair of **creation-time** picks from a closed list, each with
  guaranteed deadzones, and they're uniform across all heroes — so the sim prices them
  in once and they never creep.)*

> ✅ **DECIDED — thread/B-plot Growth crediting (Ian, 2026-06-14; `sim_threads.py`).** Threads earn
> Growth, with one split: **shared B-plots credit the whole party; a character-specific B-plot
> credits only its own hero.** Modeling showed why this split is load-bearing, not flavor:
> *action-heavy* threads self-limit (full-Challenge side-arcs balloon loss — Movie 7%→22% at +3
> thread Milestones — so nobody farms them), but *quiet character B-plots* add Growth with little
> added danger (loss ~7%→9.5% at +3). If those quiet personal arcs credited party-wide, a party of
> 3 each running one would roughly **double** everyone's Growth (each hero (6 main + 6 thread)//3 =
> 4 vs. baseline 2). Per-hero crediting holds each hero near the spine baseline ((6 + own 2)//3 = 2)
> while still rewarding the thread — fair *and* the brake. Shared B-plots stay party-wide (a couple
> of them is a bounded ~+1 Growth and doesn't break the loss curve).

> Naming note: **"Growth," not "XP."** The vocab table bans "XP" for track Progress; the
> advancement currency uses the thematic term **Growth** to keep that distinction clean.

---

## 5. The Core Mechanic

Whenever a player attempts something risky or challenging, roll **2d6** and add the
modifier, built from two questions each worth **+1**: **+1** if the action calls for one of
your two **Stats** (chosen objectively by what the moment needs), **+1** if one of your three
**Assets** fits (argued via the one-sentence test). Both → **+2**; neither → **+0** (you can
still try — you just roll the bare dice).

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

A Weak Hit and a Miss cost Readiness exactly as shown — unless the hero takes a **Devil's Bargain**
(below), which trades the Miss's loss for a villain advance. The **Antagonist Track** never advances
*silently* on a roll; it moves only via the three named triggers — a **Devil's Bargain,** a **Miss
showing doubles,** or a hero going **Out of Action** (Sections 6/9). **Resting never advances it.**

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

If a player rolls **matching numbers (doubles)** on a **Hit**, their result is upgraded by one tier:

- A **Weak Hit** with doubles (like 4 & 4) becomes a **Strong Hit.**
- A **Strong Hit** with doubles (like 5 & 5) is an **Outstanding Success** — you succeed
  spectacularly and add an extra narrative bonus of your choice.

**Doubles on a Miss do *not* upgrade it.** Instead, the dice swing against the heroes and the
**Antagonist Track advances one box** (Section 6) — the random leg of the villain's clock. (If the
hero *also* takes a Devil's Bargain on that Miss, the two stack: the villain advances two boxes.)

### The Moves (Master List)

*Lights, Camera, Action!* runs on a small, fixed set of **moves** — every time you pick up the dice to
settle something, you're making one. They fall into three families by **what they do:**

- **Action moves** *resolve a hero's attempt* at something risky — **2d6 + 0/+1/+2**, read
  Strong/Weak/Miss. The dice **adjudicate** (did you pull it off?).
- **Progress moves** *open or close a progress track* — a Story Arc or a Challenge. The openers
  (Start a Story Arc, Start a Challenge) roll generatively to set how things begin; the closers
  (Fall back, Quit the Story Arc) are deterministic procedures.
- **Frame moves** *shift the fiction in the moment* — no track. When a Frame move rolls, the dice
  **generate** a direction rather than judge a hero — so a Frame move can never be "failed."

Each move is defined in full in the chapter noted; this list is the authoritative roster.

**Action moves — resolve a hero's attempt (2d6 + 0/+1/+2):**

| Move | What it does | Chapter |
|---|---|---|
| **The Roll** | The core move; handles any risky action, run as a **Regular Roll** (no track) or a **Challenge Roll** (marks a track). Every other move is shaped from it. | Ch.7 |
| **Aid Your Ally** | The core move pointed at a teammate — on a Hit, hand them +2/+1; same Pay the Price as any roll (Strong: ally +2; Weak: ally +1, aider −1; Miss: nothing, aider −2). | Ch.7/8 |
| **Mend** | A quick patch in any scene (in a Challenge, it's your turn instead of a Challenge Roll): self or ally, **Strong +3 / Weak +2 / Miss −1 Readiness**, capped at 9, **never advances the villain**, can't revive an Out-of-Action hero. | Ch.9 |
| **Recovery Scene** | Fall back and regroup: the party heals **fully back to 9** — **free** (no roll, no villain advance). Reliable; the quiet/B-plot beat. | Ch.9 |
| **Downtime** | The between-Story-Arcs rest: heals to full, restores any Broken Asset; free, the villain's clock resets. | Ch.9 |
| **Showdown** *(the climax)* | The last-box roll when the heroes reach the climax (Story Arc Track full); decides the Story's outcome. A Miss escalates rather than ending it outright. | Ch.8/10 |

**Progress moves — open or close a progress track:**

| Move | What it does | Dice |
|---|---|---|
| **Start a Story Arc** | Sets how a new Story Arc opens — *Clear purpose* / *More questions than answers* / *Trouble finds you first* (Ch.10). | 2d6 + 1, generative |
| **Start a Challenge** | Sets the opening of a Challenge the heroes *deliberately initiate*: a one-time **±1 to the first roll** (Strong +1 *you got the drop* / Weak 0 *even footing* / Miss −1 *they beat you to it*). Skipped when trouble is thrust on the heroes (Ch.8). | 2d6 + 1, generative |
| **Fall back** | Retreat from a losing Challenge (lose its progress) to regroup — resolved as a **Recovery Scene** (full heal, free, no villain advance) (Ch.8/9). | none |
| **Quit the Story Arc** | The terminal fall back — give up a Story; no penalty or bonus; the loss seeds a new Story (Ch.10). | none |

**Frame moves — shift the fiction in the moment:**

| Move | What it does | Dice |
|---|---|---|
| **Ask the Oracle** | The stuck-point move: name the next Milestone → do the obvious → **Story Spark** (d6) or **Ask the Dice** (1d6 yes/no) (Ch.11). | d6, generative |
| **Pay the Price** | Turns a Weak Hit/Miss into a fiction complication and its Readiness loss; never advances the Antagonist Track by itself (Ch.9). | none (optional prompt) |
| **Devil's Bargain** | On a Miss, refuse the Readiness loss and upgrade the Miss to a Strong Hit, in exchange for the Antagonist Track **+1** (Ch.9/10). Optional; never on a knockout roll. | none (player choice) |

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
| **Episode** | **3 Milestones** | **5 boxes** (Attacks on 1·3·5) | one TV episode, told in one sitting |
| **Movie** | **6 Milestones** | **9 boxes** (Attacks on 1·3·5·7·9) | a feature film, over ~2–3 sessions |

The Story Arc Track box count is a default, not a lock — a meaty Episode can stretch a Milestone or
two. The **Antagonist Track is the same size at any party count** (no duo/large-group special case):
because Challenges are sized by difficulty alone (Section 7), total rolls per Story stay about the
same whatever the table size, so the clock fills at about the same rate for everyone. Its **odd boxes
are Attacks** (narrated villain beats); the **last box is the villain's victory.** Sized this way, the
villain's clock tends to end up *near* full as the heroes reach their finale — the **photo-finish** —
without anyone being railroaded there (below).

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

> ✅ **DECIDED — single nested spine, two sizes (2026-06-13; track sizes & triggers revised
> 2026-06-25).** Replaces the sandbox model (concurrent independent arcs in four fixed sizes —
> Episode 3 / Movie 8 / Season 8 / Series 12 — each with an equal-length Antagonist Track, advanced
> by fleeing + an optional tick). That structure was a Starforged inheritance and **could not produce
> the game's goal** — a story whose villain ends *one step from winning*. The model: **one Story =
> one spine**, two individual sizes with machinery (**Episode 3 Milestones / 5-box Antagonist Track,
> Movie 6 / 9** — the same at any party size; the old duo special case is gone), Season/Series as
> prose collection patterns, B-plots as lose-clock-free threads. The Antagonist Track advances via
> the **Devil's Bargain spine** (next note); recovery is **free.** Validated in `Math & Simulation
> Reference.md` §0: the **photo-finish** is the tuned deliverable (~20% Episode / ~21% Movie at
> realistic play); loss is a rare earned tail (~6.5% / ~11%). Kills the old "four types / equal-length
> Antagonist Track / multiple concurrent arcs / no-feed-up" rules; **nesting returns** (a Season is
> *made of* Stories).
>
> *(History: the 2026-06-13 spine first sized the track Episode 3/2 · Movie 6/3, advanced it by a
> Surge on each Recovery Scene with a reserved climax box, and used Mend + a full-reset Recovery as
> two moves; 2026-06-22 revised Movie to 6/4 / duo 6/5. The 2026-06-25 Devil's Bargain rework
> retired the recovery-surge, the Surge term, and the reserved climax box, and resized to 5/9.)*

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
Story's other end. It is **Episode 5 boxes / Movie 9 boxes** (same at any party size). Its boxes fill
as the antagonist gains ground during play; its **odd boxes are Attacks** (narrated villain beats),
its even boxes are silent pressure, and its **last box is the villain's victory** — fill it before the
heroes finish their Story Arc Track and the bad guys win. The Story is a race: arrive at your Showdown
with the villain **one step from winning** — the **photo-finish** — or fall before you reach it.

> ✅ **DECIDED — how the Antagonist Track advances: the Devil's Bargain spine (2026-06-25).**
> The villain advances **one box** in exactly **three ways** — *not* when the heroes rest:
> 1. **A Devil's Bargain.** On a **Miss,** a hero may refuse the Readiness loss **and** upgrade the
>    Miss to a **Strong Hit,** in exchange for advancing the villain one box (Section 9). Always
>    optional; **never allowed on a roll that would knock the hero Out of Action.** This is the main
>    engine — the heroes feed the villain by buying their own successes.
> 2. **A Miss showing doubles.** When a Miss comes up doubles, the dice swing against the heroes and
>    the villain advances one box (Section 5). Doubles now upgrade *only* a Hit (Oracle's Blessing);
>    on a Miss they feed the villain instead. The random leg nobody controls. (A doubles-Miss the
>    hero *also* bargains advances the villain **two** boxes — they stack.)
> 3. **A hero going Out of Action.** Drop to 0 Readiness and the villain seizes the moment — one box,
>    on top of the broken Asset (Section 9). The structural/catastrophe trigger.
>
> This **retires the 2026-06-13 recovery-surge model** (a Surge per Recovery Scene), the term
> **"Surge,"** and the **reserved climax box.** Recovery is now **free** — falling back to regroup
> never advances the villain. Validated in `Math & Simulation Reference.md` §0 (`sim_devils.py` /
> `sim_devils2.py`): the photo-finish is the tuned deliverable; loss is a rare earned tail.

- **The Attack (what an odd box means).** You narrate a villain beat only on the **odd "Attack"
  boxes** (1·3·5, plus 7·9 on a Movie); the even boxes are silent pressure (the music tightening, the
  walls inching in — no scene needed). When an Attack box fills, **stop and play it out:** envision
  what the villain did off-screen, then **bring it on-screen as a complication** — a new obstacle, an
  escalation, an ally captured, the deadline jumps closer. The world visibly tightens. This keeps the
  villain's *story* beats paced even when boxes fill in a rush (two bargains in one fight just slide
  the clock; you play the Attack when the next odd box lands).
- **The pressure is player-authored.** Most of the villain's climb comes from Devil's Bargains —
  choices the heroes make under fire. The clock is a mirror of how hard they've pushed their luck.
- **It can't be gamed to zero.** Even a cautious party that never bargains still faces doubles-Misses
  and the odd knockdown, so the villain always creeps. (Recovery is free — fall back as often as the
  fiction allows; the small **Mend** also never advances the villain.)
- **Characterize the antagonist.** The antagonist may be a person, a faction, or a **force** (a
  harsh desert, a plague, a deadline). Name what it *wants* and what "winning" looks like, so every
  Attack is a concrete beat: the desert's clock fills → a sandstorm hits.
- **Losing before the climax (the loss vector).** A hero taken **Out of Action** advances the villain
  a box on the spot (Section 9) — and near the end of a Story Arc, that box can be the villain's last,
  losing the Story *before* the heroes reach their Showdown. This is the real risk that keeps
  Readiness meaningful — it is no longer a survival meter (heroes can't die) but **ammunition spent
  against the villain's clock.** (It is also why you can't take a Devil's Bargain on a knockout roll —
  you can't buy your way out of going down.)

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
>
> ✅ **DECIDED — Challenges and Milestones are fully decoupled (Ian, 2026-06-14).** Winning a
> Challenge does **not**, by itself, mark a Milestone. A **Challenge is just a Scene with more
> camera time**; a **Milestone is significant progress toward the goal.** You mark a Milestone
> when the *story* takes that step forward — which may or may not coincide with clearing a
> Challenge, and plenty of Challenges resolve without marking one. (Reflected in Ch.8.)

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

The number of boxes is **fixed by difficulty, not by party size** (Starforged-style, "Option B"):

- **Easy Challenge** — **2 boxes.**
- **Medium Challenge** — **3 boxes.**
- **Hard Challenge** — **4 boxes.**
- **Very Hard Challenge** *(optional — reach for it only at a climax, and only if you want to)* —
  **5 boxes.**

These are the same at any table — **no party-size scaling, no party-size rules anywhere.**

> **Fixed difficulty — Option B (DECIDED 2026-06-25).** Challenge size depends **only on difficulty**,
> never on headcount. Filling a fixed-size track takes about the same number of rolls regardless of who
> is rolling, so **total rolls per Story stay roughly party-independent** — which is what lets the
> Antagonist Track (Episode 5 / Movie 9) need *no* party-size scaling either. One difficulty table, one
> clock table, zero party-size rules. (Cost: a big group resolves a small fixed Challenge in ~1 round,
> so big groups lean on Hard/Very Hard for meaty set-pieces — the mirror of the old duo "thin" issue,
> which this also settles by giving the duo a meatier 3-box Medium for free.) **Supersedes the
> 2026-06-21 party-scaled ladder** (Easy = players−1 / Medium = players / Hard = players+1) and its
> 2026-06-22 revision. Validated in `Math & Simulation Reference.md` §0 (`sim_devils.py` /
> `sim_devils2.py`): photo-finish and loss are flat across party sizes 2–6.
>
> **Very Hard** remains an optional top rung reserved for the **Showdown** — the finale itself, not a
> pre-finale obstacle — so its extra length raises the climax's stakes without bleeding attrition into a
> later scene.

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

(The Antagonist Track is never advanced *silently* by a roll result — it moves only via a **Devil's
Bargain,** a **Miss showing doubles,** or a hero going **Out of Action** (Sections 5/6/9). Resting
never advances it.)

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
assist, then roll 2d6 + modifier (the usual **+0/+1/+2** — +1 if a relevant Stat fits the
help, +1 if a fitting Asset does):

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

> ✅ **DECIDED — Aid fully stacks (Ian, 2026-06-14).** The bonus adds on top of the ally's own
> modifier (**including their Asset's +2**), and **multiple allies may stack Aid on the same
> roll** (two Strong-Hit helpers = **+4** on the ally's next roll), with no cap on how many pile
> on. This is **self-limiting**, not a balance hole: every helper who whiffs eats the Pay the
> Price themselves (−1/−2), so two heroes stacking Aid risk ~6 team Readiness for one swing —
> a real cost the table chooses to spend on a roll they need. **Modeling confirms it doesn't dent
> the loss curve** (`sim_aid.py`, 2026-06-14): a 2-helper stack takes one roll to ~99% success,
> but the *opportunity cost* — two spent turns = one box-attempt that round instead of three —
> makes leaning on it in a Challenge strictly *worse* (Movie loss 7%→27% at the climax, →69% if
> spammed). It can't be farmed; where it's strong (a lone Showdown/clutch roll) it costs turns +
> Readiness and only buys drama-insurance, since a missed Showdown isn't the loss vector.

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

(A missed Showdown is a Miss like any other: doubles on it still advance the villain, and the
**Devil's Bargain is still on the table** — the ultimate gamble. Otherwise a Showdown is about
*finishing*, not regrouping.)

**Story Arc Showdown — the plot twist (optional).** You can make the *final box of the Story Arc
Track* a Showdown too — one last roll as the heroes go to complete the closing Milestone.
On a Strong or Weak Hit the Story Arc is won (Weak = Pay the Price on the way out). On a **Miss**,
*you thought it was over, but it wasn't:* **add one extra Milestone box to the Story Arc Track** and
introduce a climactic twist — the villain's true plan surfaces, an ally betrays you, the prize
isn't what it seemed. The heroes must complete that new Milestone before they can attempt the
Story Arc Showdown again. Importantly, **the twist itself adds no box to the Antagonist Track** — it
gives the heroes *more to do*, not the villains a free win (though with the villain's clock often
near full, finishing before they do is the whole tension of the moment). Like all
Showdowns it's optional, and it's a wonderful way to make the end of a Story Arc land with a
cinematic surprise.

Reserve Showdowns for moments that deserve the tension; everyday Challenges (and Story Arcs) should
still end the instant their last box fills.

### 7. Falling Back from a Challenge (The Escape Valve)

Heroes are never trapped in a Challenge they're losing. At any point — usually when Readiness
is running dangerously low and grinding out the remaining boxes isn't worth the cost — the
group may **fall back** and regroup. Falling back is resolved as a **Recovery Scene** (Section 9):

- **You lose the Challenge's progress.** Wipe the track; those boxes don't count.
- **The party heals fully back to 9** — the point of pulling back.
- **The villain gains nothing.** Recovery is **free** — falling back never advances the Antagonist
  Track. You simply live to fight another day.

Falling back is a **group decision** (in Co-op, made together). It's always safe and always available
at a genuine lull — so when you're battered, regrouping is the smart play, *not* a gamble. (The
pressure that climbs the villain's clock comes from the choices you make *under fire* — Devil's
Bargains and the dice — never from catching your breath.)

If the heroes decide a Story simply isn't winnable or worth the cost, they may **Quit the Story
Arc** — the terminal version of falling back — see Section 6. Falling back is the everyday,
scene-level valve; quitting is the whole-Story version.

### Recovery (Mend & the Recovery Scene)

> ✅ **DECIDED — recovery is free (2026-06-13; ratchet removed 2026-06-22; surge retired 2026-06-25).**
> Recovery is **two moves**, the **Readiness max stays 9 all game**, and **recovery is FREE.** The
> **Recovery Scene** (fall back and regroup) heals the party **fully back to 9** — no roll, **no cost
> to the villain's clock.** **Mend** is a small, risky **any-scene** patch that likewise never advances
> the villain — in a Challenge it's a *tactical choice* (patch vs. push), and **must cost on a Miss
> (−1)**, which keeps it from substituting for a regroup (no usage cap needed). The old "Surge on the
> Recovery Scene" is **retired** — the villain advances only via the Devil's Bargain, doubles-Misses,
> and Out of Action (Section 6). Recovery becomes a pure pacing signal (*when am I battered enough to
> fall back?*), not a loss vector. Balance validated in `Math & Simulation Reference.md` §0
> (`sim_devils.py` / `sim_devils2.py`): photo-finish is the tuned deliverable; loss is a rare tail.

**Mend (the any-scene patch).** Any time the fiction gives a beat — in a Challenge (*instead of* a
Challenge Roll) or in an ordinary scene — a hero may **Mend** (self or a teammate) to recover a
little. Roll **2d6 + modifier** (the usual +0/+1/+2 — +1 for a relevant Stat, +1 for a fitting
Asset; doubles upgrade):

- **Strong (10+):** +3 Readiness. · **Weak (7–9):** +2. · **Miss (6−):** **−1 Readiness** (the
  patch goes wrong) — and a Miss *can* drop a hero to Out of Action.

Mend **never advances the villain** and has **no usage cap**, but it's **capped at 9.** Its limit is
the **−1 risk** — so it smooths the ride between regroups but can't substitute for one. It's the
quick gamble to stay on your feet; when you're truly low, the safer play is to fall back for a full
Recovery Scene instead.

**The Recovery Scene (fall back and regroup).** When the bleed isn't worth it — or the party simply
needs to breathe at a safe lull (most often **between Challenges**) — they **fall back** and
regroup. It **heals the whole party fully back to 9** (reliable, no roll) and is **free — it never
advances the Antagonist Track** (Section 6). It is **gated by the fiction** (no safe beat, no
regroup) and **player-chosen**, *discovered in play, never on a schedule.* What it costs is the
camera, not the clock: a regroup means stepping out of the action — the campfire, the heart-to-heart,
the **character scene.** Falling back is always safe and always available, so you never ration or
dread it; the villain's clock climbs from the gambles you take under fire, not from resting.

**Downtime (between Story Arcs).** Finishing a Story Arc heals everyone to full and **restores any
Broken Asset** — free; the villain's clock resets (the Story Arc is resolved). It's the *slow down
and roleplay* breather between adventures (optionally a d6 prompt: gearing up, good company, loved
ones, a beat for the heart). Heroes always start the next Story fresh.

**Out of Action (the loss vector).** A hero at 0 Readiness can't act. **Going Out of Action advances
the Antagonist Track one box** on the spot (Section 6) — you fell, and the bad guys seized the moment
— and near the climax that box can be the villain's last, losing the Story *before* the heroes reach
their Showdown. **Mend cannot revive a downed hero** — only a full **Recovery Scene** (or Downtime,
both free) brings someone back from 0. So going down is no longer survival-neutral — near the climax
it is *how you lose*. (This, plus the fact that you **can't take a Devil's Bargain on a knockout
roll,** is why a battered party's smart play is to fall back for a free Recovery Scene rather than
gamble.) Heroes still can't die; the cost is the villain's box, a Broken Asset, and the regroup. This
is what keeps Readiness meaningful — **ammunition spent against the villain's clock**, not a survival
meter.

> ✅ **DECIDED — Out-of-Action timing & edge cases (Ian, 2026-06-14; surge → villain box, 2026-06-25).**
> - **A knockdown never pauses the Scene.** When a hero drops to 0 mid-Challenge, the action
>   continues — the rest of the party may **push on to finish the Challenge or fall back**, their
>   call. The Recovery Scene that revives the downed hero happens **once the Challenge ends, win or
>   lose** — never in the middle of it. So a single roll that **both fills the last box and drops its
>   roller to 0 wins the Challenge first**; the regroup follows in the aftermath. (The villain still
>   gains their box from the knockdown.)
> - **Multiple heroes down at once.** Each hero who goes down advances the villain **one box** and
>   breaks one of their Assets — going down is always individually costly. A single Recovery Scene
>   then gets the whole party back on their feet at once.
> - **Solo play:** with one hero, going Out of Action means there's no one to fight on — that
>   **Challenge is lost**; pull back, then take the Recovery Scene to get back up. (Solo is
>   technically supported, not a design target — default play is Co-op, optionally with a Guide.)

**Broken Assets (DECIDED 2026-06-09).** Going Out of Action also breaks **one Asset** — the one
that failed the hero in the moment they went down (Guide calls it; Co-op table agrees, defaulting
to whatever they were leaning on). A **broken Asset gives no +1:** any roll it would have covered
drops that Asset's +1, exactly like acting off-Asset. It is *never* a penalty — it only removes the
bonus, so the **+0 floor is preserved** with zero new math (this is why we break an existing Asset
rather than add a negative-modifier one). Only **Downtime (finishing a Story) restores a Broken
Asset** — a mid-Story Recovery Scene heals Readiness but can't un-break an Asset. Going down again
before the Story ends breaks a second Asset. This is the *durable* teeth layer (Starforged
"impacts") that a full-restoring Readiness track lacks; scoped to Out of Action only for now.
Distinct from advancement's **Trade In** (a break is temporary, free, and involuntary; a Trade In
is permanent, costs Growth, and is chosen — §4 / Ch.13). Optional flavor: a Guide may write a
one-off **condition** (*Broken Spirit, Rattled*) that behaves identically (cancels an Asset's +1,
clears at Downtime, never a flat penalty) when the hurt doesn't map to a single Asset.

**The teeth aren't the Readiness pool — they're the villain's clock.** A Recovery Scene restores you
fully and for free, so the party rarely *stays* worn down; the pressure is the Antagonist Track, fed
by the gambles you take (Devil's Bargains), the dice that betray you (doubles-Misses), and the
knockdowns that cost you a box and a **Broken Asset** until the Story ends. Readiness is ammunition
against that clock, not a dwindling survival pool — the pressure is the villain, not attrition.

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

> ✅ **Paying the Price never advances the Antagonist Track (2026-06-13).** A plain Weak Hit or Miss
> is a Readiness loss plus an in-scene complication — nothing more. The Antagonist Track advances only
> via a **Devil's Bargain,** a **Miss showing doubles,** or going **Out of Action** (Sections 5/6/9).
> (A Devil's Bargain is taken *instead of* paying the price — refuse the Readiness loss, upgrade the
> Miss to a Strong Hit, and advance the villain a box — so it's the one way a failed roll touches the
> clock, and it's the hero's choice.)

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

> 🔁 **SUPERSEDED by the spine-model rework (2026-06-13) and the Devil's Bargain clock rework
> (2026-06-25).** The single biggest structural change: **sandbox play is dropped.** Several decisions
> logged below are now obsolete and are retained only for the reasoning trail — the canonical rules are
> §6/§7/§9 above. Specifically superseded: *"Four Story Arc types + unified headway rule"* (now **two
> individual sizes** — **Episode 3 Milestones / 5-box Antagonist Track, Movie 6 / 9**, same at any party
> size — with Season/Series as **prose collection patterns**); *"Antagonist Track flee-primary +
> optional telling-failure tick"* **and** the interim *"advances only on a Recovery Scene, with a
> reserved climax box"* (now advances via the **Devil's Bargain spine** — a Devil's Bargain, a Miss
> showing doubles, or going Out of Action — with **odd-box Attacks** and **no reserved climax box;
> recovery is free**); *"rolled SF-C recovery"* (now **two free moves**: a small risky **Mend** —
> Strong +3 / Weak +2 / **Miss −1**, an any-scene tactical patch — plus the full-reset **Recovery
> Scene**, neither of which advances the villain; Downtime is the between-Stories reset); and
> *"multiple concurrent arcs / no feed-up"* (now **one nested spine**, with B-plots as lose-clock-free
> threads). New model validated in `Math & Simulation Reference.md` §0 (`sim_devils.py` /
> `sim_devils2.py`).

> ✅ **DECIDED — pre-playtest audit clarifications (2026-06-14).** A polish pass before playtesting
> settled several edge cases (details inline in §6/§7): **(1) Challenges ≠ Milestones** — a
> Challenge is just a Scene with more camera time; a Milestone is story progress, marked
> independently. **(2) Out-of-Action timing** — a knockdown never pauses a Challenge; the
> Recovery Scene that revives the downed hero fires after it ends (win or lose), and a roll that both
> wins and drops you wins first. **(3) Multiple heroes down at once** — each knockdown advances the
> villain one box and breaks one Asset; a single Recovery Scene then revives the whole party (timing
> per 2026-06-14; the per-knockdown villain box is the 2026-06-25 model). **(4) Solo OoA** →
> the lone hero loses that Challenge, then regroups (solo is supported, not a target). **(5) Aid
> fully stacks** — with the Asset and across multiple helpers, self-limited by each helper's Pay
> the Price. **(6) Genre count corrected to seven** (Post-Apocalypse). **(7) Threads earn Growth**
> — shared B-plots party-wide, character-specific B-plots to their own hero only (`sim_threads.py`;
> §4 DECIDED note). **(8) Fully-stacking Aid is balance-safe** — the opportunity cost makes it
> self-defeating to farm (`sim_aid.py`; §7 Aid note). Both modeled and closed 2026-06-14.
> **(9) Micro-clarifications** (derivable defaults, folded into the chapters): Mend on a hero
> already at 9 does nothing (and still risks the −1 — don't); a Recovery Scene always heals to a
> full 9 and is **free** (no declining ceiling — ratchet removed 2026-06-22; recovery-surge retired
> 2026-06-25); a loss past 0 stops at 0 (no overflow; OoA is the worst case); a generative roll
> (Start a Story Arc / Start a Challenge) that rolls doubles on an already-10+ result takes the top
> result **plus** a small extra edge.

> ✅ **DECIDED — the Devil's Bargain antagonist-clock rework (2026-06-25).** The defining rework of the
> Antagonist Track, propagated through the whole book. **(1) Recovery is FREE** — a Recovery Scene heals
> the party to 9 with no roll and **never** advances the villain; the **"Surge"** term and the
> **"reserved climax box"** are retired. **(2) The Antagonist Track advances one box in exactly three
> ways:** a **Devil's Bargain** (on a Miss, a hero may refuse the Readiness loss *and* upgrade the Miss
> to a Strong Hit, for villain +1 — optional, never on a knockout roll); a **Miss showing doubles**
> (villain +1 — doubles now upgrade *only* a Hit; on a Miss they feed the villain instead of upgrading
> Miss→Weak); and going **Out of Action** (villain +1 + an Asset breaks). A doubles-Miss that is *also*
> bargained advances the villain two boxes (they stack). **(3) The narrated villain beat is an Attack**
> on the track's **odd boxes** (Episode 1·3·5; Movie 1·3·5·7·9); even boxes are silent pressure; the
> **last box is the villain's victory.** **(4) Track sizes: Episode = 5 boxes, Movie = 9 boxes — the
> SAME at any party size** (the duo/two-player special case is removed). **(5) Challenge difficulty is
> fixed by difficulty, not party size — Option B:** Easy 2 / Medium 3 / Hard 4 / Very Hard 5,
> party-independent (no party-size rules anywhere; supersedes the 2026-06-21 party-scaled ladder and its
> 2026-06-22 revision). **(6) Design philosophy:** loss is no longer a tuning target — it's a rare
> earned tail; the tuned metric is the **photo-finish** (villain one box from winning at the climax).
> Validated by `sim_devils.py` / `sim_devils2.py` (Episode realistic ~20% photo-finish / ~6.5% loss;
> Movie ~21% / ~11%; party-independent; see `Math & Simulation Reference.md` §0). **Supersedes** the
> 2026-06-13 recovery-surge/reserved-climax model and the party-scaled difficulty ladder; also deletes
> the planned "Playing as a Pair" duo subsystem.

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
- ✅ The **Antagonist Track** is **CORE** (mandatory on every Story Arc). *(Trigger history —
  superseded: the flee-primary + optional-telling-failure tick of 2026-06-06/-06-08, then the
  recovery-Surge of 2026-06-13, are both retired; the current triggers are the **Devil's Bargain
  spine** of 2026-06-25 — see the DECIDED note above.)* Added **Quit the Story Arc**; losing a Story
  Arc seeds a new one.
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

- ✅ **Roll modifier — +0 / +1 / +2 (revised 2026-06-22, was +2 / +1).** +1 for a relevant
  **Stat** (one of your two, chosen objectively), +1 for a fitting **Asset** (one of your three,
  argued); both → +2, neither → +0. The **+0 floor** (replacing the old always-on +1 floor) is the
  edge of danger — acting outside your Stats and Assets is a real gamble. This is the scheme the
  current balance/simulation work and the max-9 target assume.

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
