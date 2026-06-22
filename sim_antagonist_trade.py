#!/usr/bin/env python3
"""
Amazing Forge — Antagonist-Track "trade a Miss" balance simulation.

Question being modeled (see Math & Simulation Reference.md, OPEN question):
  Should advancing an Antagonist Track box REPLACE a Miss's Readiness loss
  (a player-elected trade), instead of being layered on top of it?

We compare two models over many simulated Easy Quests:
  BASELINE : a Miss always costs 2 Readiness (current canonical rule).
  TRADE    : on a Miss, the party MAY skip the 2 Readiness loss by advancing
             one Antagonist Track box instead. The track is the same length as
             the Quest Track (Easy = 3 boxes). If it fills, the Quest is LOST.

All structural assumptions are parameters at the top so they can be re-tuned
as the real numbers firm up. Defaults reflect Ian's 2026-06-06 estimates.
"""

import random
from statistics import mean

# ----------------------------------------------------------------------------
# PARAMETERS (edit these — they are assumptions, not settled rules)
# ----------------------------------------------------------------------------
PARTY_SIZE              = 3      # heroes at the table
MILESTONES              = 3      # Easy Quest = 3 (also = Quest Track length)
CHALLENGES_PER_MS       = 2      # "2 easy challenges ..."
REGULAR_ROLLS_PER_MS    = 3      # "... plus another ~3 regular rolls"
EASY_CHALLENGE_BOXES    = PARTY_SIZE          # Easy Challenge = # players
RESTS_PER_QUEST         = 1      # Recovery Scenes per quest (Ian: 0–1)
RECOVERY_HEAL           = 3
QUEST_VICTORY_HEAL      = 6      # not used mid-quest; here for completeness
READINESS_MAX           = 9
READINESS_START         = 9
WEAK_COST               = 1
MISS_COST               = 2
P_PLUS2                 = 0.85   # share of rolls made inside an Asset (+2);
                                 # 0.85 reflects the mandatory broad Attribute (2026-06-12).
                                 # Pre-Attribute baseline was 0.80. See Math & Sim Ref §3b.
ORACLE_BLESSING         = True   # doubles upgrade one tier
ANTAG_TRACK_LEN         = MILESTONES          # "same # of boxes as Quest Track"

# Trade policy (TRADE model): a hero trades away a Miss's Readiness loss when
# their Readiness is at or below this threshold (i.e. the hit would hurt /
# threaten Out of Action), as long as trades remain before the Quest is lost.
# We keep >=1 box of safety margin by default so the trade itself never loses
# the quest outright (players wouldn't elect to lose).
TRADE_THRESHOLD         = 4
KEEP_SAFETY_MARGIN      = 1      # leave this many antag boxes unfilled

N_QUESTS                = 200_000

# ----------------------------------------------------------------------------
def roll_tier(mod):
    """Return 'strong' | 'weak' | 'miss', applying Oracle's Blessing on doubles."""
    d1, d2 = random.randint(1, 6), random.randint(1, 6)
    total = d1 + d2 + mod
    if total >= 10:
        tier = "strong"
    elif total >= 7:
        tier = "weak"
    else:
        tier = "miss"
    if ORACLE_BLESSING and d1 == d2:
        tier = {"miss": "weak", "weak": "strong", "strong": "strong"}[tier]
    return tier

def mod_for_roll():
    return 2 if random.random() < P_PLUS2 else 1

class Hero:
    __slots__ = ("r", "ooa")
    def __init__(self):
        self.r = READINESS_START
        self.ooa = False
    def lose(self, n):
        self.r -= n
        if self.r <= 0:
            self.r = 0
            self.ooa = True
    def heal(self, n):
        if self.r <= 0 and self.ooa:
            self.ooa = False
        self.r = min(READINESS_MAX, self.r + n)
        if self.r > 0:
            self.ooa = False

def apply_outcome(hero, tier, fills_box, state, use_trade):
    """Returns boxes_filled (0/1). Mutates hero + state (antag, ooa_events)."""
    box = 0
    if tier == "strong":
        box = 1 if fills_box else 0
    elif tier == "weak":
        box = 1 if fills_box else 0
        hero.lose(WEAK_COST)
    else:  # miss
        if use_trade and want_trade(hero, state):
            state["antag"] += 1                 # trade: advance villain instead
            state["trades"] += 1
        else:
            before = hero.ooa
            hero.lose(MISS_COST)
            if hero.ooa and not before:
                state["ooa_events"] += 1
    return box

def want_trade(hero, state):
    if state["antag"] >= ANTAG_TRACK_LEN - KEEP_SAFETY_MARGIN:
        return False
    return hero.r <= TRADE_THRESHOLD

def run_challenge(heroes, boxes_needed, state, use_trade):
    filled = 0
    guard = 0
    while filled < boxes_needed:
        progressed = False
        for h in heroes:
            if h.ooa:
                continue
            progressed = True
            tier = roll_tier(mod_for_roll())
            filled += apply_outcome(h, tier, True, state, use_trade)
            if filled >= boxes_needed:
                break
        guard += 1
        if not progressed or guard > 200:
            break

def run_regular_rolls(heroes, n, state, use_trade):
    active = [h for h in heroes if not h.ooa]
    for i in range(n):
        if not active:
            break
        h = active[i % len(active)]
        tier = roll_tier(mod_for_roll())
        apply_outcome(h, tier, False, state, use_trade)

def simulate_quest(use_trade):
    heroes = [Hero() for _ in range(PARTY_SIZE)]
    state = {"antag": 0, "trades": 0, "ooa_events": 0}
    quest_lost = False
    rest_points = set()
    if RESTS_PER_QUEST > 0:
        # spread rests across milestones (e.g. 1 rest -> after milestone 2 of 3)
        step = MILESTONES / (RESTS_PER_QUEST + 1)
        rest_points = {int(round(step * (k + 1))) for k in range(RESTS_PER_QUEST)}

    for ms in range(1, MILESTONES + 1):
        for _ in range(CHALLENGES_PER_MS):
            run_challenge(heroes, EASY_CHALLENGE_BOXES, state, use_trade)
        run_regular_rolls(heroes, REGULAR_ROLLS_PER_MS, state, use_trade)
        if state["antag"] >= ANTAG_TRACK_LEN:
            quest_lost = True
            break
        if ms in rest_points:
            for h in heroes:
                h.heal(RECOVERY_HEAL)

    any_ooa = state["ooa_events"] > 0
    end_r = mean(h.r for h in heroes)
    return {
        "lost": quest_lost,
        "any_ooa": any_ooa,
        "ooa_events": state["ooa_events"],
        "trades": state["trades"],
        "end_r": end_r,
        "antag": state["antag"],
    }

def summarize(use_trade, label):
    res = [simulate_quest(use_trade) for _ in range(N_QUESTS)]
    n = len(res)
    print(f"\n=== {label} ===")
    print(f"  Quests simulated............ {n:,}")
    print(f"  Quest LOST (antag filled)... {sum(r['lost'] for r in res)/n:6.2%}")
    print(f"  >=1 hero went Out of Action. {sum(r['any_ooa'] for r in res)/n:6.2%}")
    print(f"  Mean Out-of-Action events... {mean(r['ooa_events'] for r in res):6.3f} per quest")
    print(f"  Mean trades used............ {mean(r['trades'] for r in res):6.3f} per quest")
    print(f"  Mean antag boxes at end..... {mean(r['antag'] for r in res):6.3f} / {ANTAG_TRACK_LEN}")
    print(f"  Mean ending Readiness....... {mean(r['end_r'] for r in res):6.2f} / {READINESS_MAX}")

if __name__ == "__main__":
    print("Amazing Forge — Antagonist-trade balance sim")
    print(f"party={PARTY_SIZE}  milestones={MILESTONES}  "
          f"challenges/ms={CHALLENGES_PER_MS} (Easy={EASY_CHALLENGE_BOXES} boxes)  "
          f"regular/ms={REGULAR_ROLLS_PER_MS}  rests={RESTS_PER_QUEST}")
    print(f"p(+2)={P_PLUS2}  oracle={ORACLE_BLESSING}  "
          f"trade_threshold<= {TRADE_THRESHOLD}  safety_margin={KEEP_SAFETY_MARGIN}")
    summarize(False, "BASELINE  (Miss always costs Readiness)")
    summarize(True,  "TRADE     (Miss may advance Antagonist Track instead)")
