#!/usr/bin/env python3
"""
Amazing Forge — Rolled-recovery balance simulation + tuning battery.

Recovery rework (DECIDED 2026-06-09): recovery is the core move, ROLLED, via two
moves, and the heal is ALWAYS guaranteed (a bad roll never costs Readiness):

  CATCH YOUR BREATH (short rest, individual): Strong +CYB_STRONG / Weak,Miss +CYB_BASE,
      and on a Miss an imminent new Challenge appears.
  DOWNTIME (long rest, ONE group roll, on finishing a Quest): Strong +DT_STRONG /
      Weak,Miss +DT_BASE, and on a Miss you owe a Quest in your hosts' service.

PROBLEM FOUND (first pass): with reliable healing at max 9 and -1/-2 Pay the Price,
in-quest attrition collapsed (Out of Action ~0%, parties finish near full). The
Readiness track stopped giving the narrative consequences teeth. The Miss->threat
brake didn't help, because the same Catch Your Breath that draws the threat also
heals the damage it deals.

THIS VERSION runs a battery of tuning scenarios over three levers Ian proposed:
  (1) smaller heals          (CYB/DT numbers down)
  (2) lower max Readiness
  (3) harsher Pay the Price  (-2 Weak / -3 Miss)
...and combinations, to find what restores teeth. We measure not just Out of Action
but how LOW and HOW OFTEN Readiness gets pushed (the real "does it bite?" signal).

Quest-loss (a flee/Antagonist question, §4b) is NOT modeled here — recovery never
advances the Antagonist Track. These columns isolate *attrition*.
"""

import random
from statistics import mean

# Fixed structural assumptions (§3 defaults)
PARTY_SIZE            = 3
MILESTONES            = 3
CHALLENGES_PER_MS     = 2
REGULAR_ROLLS_PER_MS  = 3
EASY_CHALLENGE_BOXES  = PARTY_SIZE
NEW_THREAT_BOXES      = PARTY_SIZE     # size of the Challenge a CYB Miss injects
INJECT_CAP            = 8
REST_THRESHOLD_FRAC   = 0.56           # rest when r <= ~56% of max (=5 at max 9)
LULL_GUARD            = 12
P_PLUS2               = 0.80
ORACLE_BLESSING       = True
N_QUESTS              = 80_000

# A scenario is a dict of the tunable knobs.
def cfg(**kw):
    base = dict(
        rmax=9, start=9,
        weak_cost=1, miss_cost=2,
        cyb_strong=4, cyb_base=3,
        cyb_miss_heal=None,        # None => same as cyb_base (current "always heal");
                                   # set 0 for the Starforged "a miss recovers nothing" model
        dt_strong=7, dt_base=6,
        old=False,                 # old flat-+3 no-roll model
        old_heal=3, old_rests=1, old_victory=6,
        cyb_cap=0,                  # 0 = unlimited; else max CYB per hero per Milestone
    )
    base.update(kw)
    return base

# ----------------------------------------------------------------------------
def roll_tier(mod):
    d1, d2 = random.randint(1, 6), random.randint(1, 6)
    total = d1 + d2 + mod
    tier = "strong" if total >= 10 else "weak" if total >= 7 else "miss"
    if ORACLE_BLESSING and d1 == d2:
        tier = {"miss": "weak", "weak": "strong", "strong": "strong"}[tier]
    return tier

def mod_for_roll():
    return 2 if random.random() < P_PLUS2 else 1

class Hero:
    __slots__ = ("r", "ooa", "rmax", "minr", "rests_used")
    def __init__(self, c):
        self.r = c["start"]; self.rmax = c["rmax"]
        self.ooa = False; self.minr = self.r; self.rests_used = 0
    def lose(self, n):
        self.r -= n
        if self.r <= 0:
            self.r = 0; self.ooa = True
        if self.r < self.minr:
            self.minr = self.r
    def heal(self, n):
        self.r = min(self.rmax, self.r + n)
        if self.r > 0:
            self.ooa = False

def apply_action(hero, tier, fills_box, st, c):
    box = 0
    if tier == "strong":
        box = 1 if fills_box else 0
    elif tier == "weak":
        box = 1 if fills_box else 0
        hero.lose(c["weak_cost"])
    else:
        before = hero.ooa
        hero.lose(c["miss_cost"])
        if hero.ooa and not before:
            st["ooa_events"] += 1
    return box

def run_challenge(heroes, boxes_needed, st, c):
    filled = 0; guard = 0
    while filled < boxes_needed:
        progressed = False
        for h in heroes:
            if h.ooa:
                continue
            progressed = True
            filled += apply_action(h, roll_tier(mod_for_roll()), True, st, c)
            if filled >= boxes_needed:
                break
        guard += 1
        if not progressed or guard > 200:
            break

def run_regular_rolls(heroes, n, st, c):
    active = [h for h in heroes if not h.ooa]
    for i in range(n):
        if not active:
            break
        apply_action(active[i % len(active)], roll_tier(mod_for_roll()), False, st, c)

def safe_lull(heroes, st, c):
    thresh = round(c["rmax"] * REST_THRESHOLD_FRAC)
    rounds = 0
    cap = c["cyb_cap"]
    while rounds < LULL_GUARD:
        rounds += 1
        # Out of Action heroes always recover (resting from the floor); the cap
        # only limits voluntary breathers.
        resters = [h for h in heroes
                   if h.ooa or (h.r <= thresh and (cap == 0 or h.rests_used < cap))]
        if not resters:
            break
        for h in resters:
            h.rests_used += 1
        misses = 0
        miss_heal = c["cyb_miss_heal"] if c["cyb_miss_heal"] is not None else c["cyb_base"]
        for h in resters:
            tier = roll_tier(mod_for_roll())
            st["cyb_uses"] += 1
            heal = c["cyb_strong"] if tier == "strong" else c["cyb_base"] if tier == "weak" else miss_heal
            h.heal(heal)
            if tier == "miss":
                st["cyb_misses"] += 1
                if st["injected"] < INJECT_CAP:
                    misses += 1
        if misses == 0:
            break
        for _ in range(misses):
            if st["injected"] >= INJECT_CAP:
                break
            st["injected"] += 1
            run_challenge(heroes, NEW_THREAT_BOXES, st, c)

def simulate_quest(c):
    heroes = [Hero(c) for _ in range(PARTY_SIZE)]
    st = {"ooa_events": 0, "cyb_uses": 0, "cyb_misses": 0, "injected": 0}
    if c["old"]:
        rest_pts = set()
        if c["old_rests"] > 0:
            step = MILESTONES / (c["old_rests"] + 1)
            rest_pts = {int(round(step * (k + 1))) for k in range(c["old_rests"])}
        for ms in range(1, MILESTONES + 1):
            for _ in range(CHALLENGES_PER_MS):
                run_challenge(heroes, EASY_CHALLENGE_BOXES, st, c)
            run_regular_rolls(heroes, REGULAR_ROLLS_PER_MS, st, c)
            if ms in rest_pts:
                for h in heroes:
                    h.heal(c["old_heal"])
        end_pre = mean(h.r for h in heroes)
        for h in heroes:
            h.heal(c["old_victory"])
    else:
        for ms in range(1, MILESTONES + 1):
            for h in heroes:
                h.rests_used = 0          # CYB cap (if any) refreshes each Milestone
            for _ in range(CHALLENGES_PER_MS):
                run_challenge(heroes, EASY_CHALLENGE_BOXES, st, c)
                safe_lull(heroes, st, c)
            run_regular_rolls(heroes, REGULAR_ROLLS_PER_MS, st, c)
            safe_lull(heroes, st, c)
        end_pre = mean(h.r for h in heroes)
        dt = roll_tier(mod_for_roll())
        for h in heroes:
            h.heal(c["dt_strong"] if dt == "strong" else c["dt_base"])
    return {
        "any_ooa": st["ooa_events"] > 0,
        "any_danger": any(h.minr <= 2 for h in heroes),     # someone hit <=2
        "mean_min": mean(h.minr for h in heroes),           # avg lowest reached
        "end_pre": end_pre,
        "cyb": st["cyb_uses"],
        "inj": st["injected"],
    }

def run(label, c):
    res = [simulate_quest(c) for _ in range(N_QUESTS)]
    n = len(res)
    return dict(
        label=label,
        ooa=sum(r["any_ooa"] for r in res) / n,
        danger=sum(r["any_danger"] for r in res) / n,
        mean_min=mean(r["mean_min"] for r in res),
        end_pre=mean(r["end_pre"] for r in res),
        cyb=mean(r["cyb"] for r in res),
        inj=mean(r["inj"] for r in res),
        rmax=c["rmax"],
    )

SCENARIOS = [
    ("OLD  flat+3 noroll, max9, -1/-2",          cfg(old=True)),
    ("NEW  current: CYB4/3 DT7/6 max9 -1/-2",    cfg()),
    # --- Starforged-informed: the heal can WHIFF (Miss recovers 0, never downward) ---
    # --- combined with a tight pool and/or gating the move's frequency.            ---
    ("SF-A  max6, miss=0, no gate (3/2 heal)",   cfg(rmax=6, start=6, cyb_strong=3, cyb_base=2, cyb_miss_heal=0)),
    ("SF-B  max5, miss=0, no gate (2/1 heal)",   cfg(rmax=5, start=5, cyb_strong=2, cyb_base=1, cyb_miss_heal=0, dt_strong=4, dt_base=3)),
    ("SF-C  max9, miss=0, GATE 1/MS (3/2)",      cfg(cyb_cap=1, cyb_strong=3, cyb_base=2, cyb_miss_heal=0)),
    ("SF-D  max6, miss=0, GATE 1/MS (3/2)",      cfg(rmax=6, start=6, cyb_cap=1, cyb_strong=3, cyb_base=2, cyb_miss_heal=0)),
    ("SF-E  max6, miss=0, GATE 2/MS (3/2)",      cfg(rmax=6, start=6, cyb_cap=2, cyb_strong=3, cyb_base=2, cyb_miss_heal=0)),
    # references from the prior battery
    ("A' max6 -1/-2, always-heal 3/2 (no whiff)", cfg(rmax=6, start=6, cyb_strong=3, cyb_base=2, dt_strong=5, dt_base=4)),
]

if __name__ == "__main__":
    print("Amazing Forge — rolled-recovery tuning battery")
    print(f"party={PARTY_SIZE}  milestones={MILESTONES}  challenges/ms={CHALLENGES_PER_MS} "
          f"(Easy={EASY_CHALLENGE_BOXES})  regular/ms={REGULAR_ROLLS_PER_MS}  "
          f"p(+2)={P_PLUS2}  oracle={ORACLE_BLESSING}  N={N_QUESTS:,}")
    print(f"rest policy: Catch Your Breath when Out of Action or r <= ~{REST_THRESHOLD_FRAC:.0%} of max")
    print(f"metrics: >=1 hero OoA | 'danger' = >=1 hero hit Readiness <=2 | mean lowest r reached |")
    print(f"         end Readiness before victory/Downtime | CYB uses & injected Challenges per Quest\n")
    rows = [run(lbl, c) for lbl, c in SCENARIOS]
    hdr = f"{'scenario':<40}{'OoA%':>7}{'danger%':>9}{'min r':>7}{'end r':>7}{'CYB/Q':>7}{'inj/Q':>7}"
    print(hdr); print("-" * len(hdr))
    for r in rows:
        print(f"{r['label']:<40}{r['ooa']:>6.1%}{r['danger']:>8.1%}"
              f"{r['mean_min']:>7.2f}{r['end_pre']:>6.2f}/{r['rmax']}{r['cyb']:>7.2f}{r['inj']:>7.2f}")
    print("\n('end r' is per-hero mean at Quest completion, BEFORE the victory Downtime/heal.)")
