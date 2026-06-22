#!/usr/bin/env python3
"""
Amazing Forge — "Start a Challenge" opening-roll simulation.

Move under test (Ian, 2026-06-09):
  A new PROGRESS move, the twin of Start a Quest, rolled once when the heroes
  DELIBERATELY initiate a Challenge. It is a "+1 forward"-style temporary modifier
  (PbtA "forward"), applied only to the FIRST hero roll of that Challenge:

      Start a Challenge: 2d6 + 1 (generative, Oracle's Blessing on doubles)
        Strong (10+) -> +1 to your first roll this Challenge   ("you got the drop")
        Weak  (7-9)  ->  0, equal footing
        Miss  (6-)   -> -1 to your first roll this Challenge    ("they beat you to it")

Question: does a one-roll +-1 at the top of each Challenge MATERIALLY move the
attrition math (Out-of-Action rate, danger%, end Readiness, challenge pacing)?
We want the answer to be "no — it's a small, mostly-flavor nudge."

Harness mirrors sim_flee_retreat.py (§4b): party 3, Episodic (3 MS), flee valve,
1 Recovery Scene. Misses always cost Readiness. The ONLY change vs that baseline
is the optional first-roll modifier.
"""
import random
from statistics import mean

PARTY_SIZE           = 3
MILESTONES           = 3
CHALLENGES_PER_MS    = 2
REGULAR_ROLLS_PER_MS = 3
EASY_CHALLENGE_BOXES = PARTY_SIZE
ANTAG_TRACK_LEN      = MILESTONES
READINESS_MAX        = 9
READINESS_START      = 9
WEAK_COST            = 1
MISS_COST            = 2
RECOVERY_HEAL        = 3
P_PLUS2              = 0.80
ORACLE_BLESSING      = True
DANGER_FLOOR         = 2          # "should we flee?" signal: a hero pushed to <= this
N_QUESTS             = 200_000

def roll_tier(mod):
    d1, d2 = random.randint(1,6), random.randint(1,6)
    total = d1 + d2 + mod
    tier = "strong" if total>=10 else "weak" if total>=7 else "miss"
    if ORACLE_BLESSING and d1==d2:
        tier = {"miss":"weak","weak":"strong","strong":"strong"}[tier]
    return tier

def mod():
    return 2 if random.random() < P_PLUS2 else 1

def start_challenge_forward():
    """Generative 2d6+1 opening; returns the +-1 forward applied to the first roll."""
    t = roll_tier(1)
    return {"strong":+1, "weak":0, "miss":-1}[t]

class Hero:
    __slots__=("r","ooa","lowest")
    def __init__(self):
        self.r=READINESS_START; self.ooa=False; self.lowest=READINESS_START
    def lose(self,n):
        self.r-=n
        if self.r<=0: self.r=0; self.ooa=True
        if self.r<self.lowest: self.lowest=self.r
    def heal(self,n):
        self.r=min(READINESS_MAX,self.r+n)
        if self.r>0: self.ooa=False

def simulate(use_start_challenge, flee_threshold=4, rests=1):
    use_flee = flee_threshold > 0
    heroes=[Hero() for _ in range(PARTY_SIZE)]
    antag=0; flees=0; ooa=0; lost=False
    chal_rolls=[]                      # rolls to resolve each challenge (pacing)
    rest_points=set()
    if rests>0:
        step=MILESTONES/(rests+1)
        rest_points={int(round(step*(k+1))) for k in range(rests)}

    for ms in range(1,MILESTONES+1):
        for _ in range(CHALLENGES_PER_MS):
            needed=EASY_CHALLENGE_BOXES; filled=0; guard=0; rolls=0
            # the opening roll, applied to the very first hero roll of this Challenge
            forward = start_challenge_forward() if use_start_challenge else 0
            first_roll_pending = True
            while filled<needed:
                active=[h for h in heroes if not h.ooa]
                if not active: break
                if use_flee and min(h.r for h in active)<=flee_threshold and antag < ANTAG_TRACK_LEN-1:
                    antag+=1; flees+=1
                    break
                for h in active:
                    m = mod()
                    if first_roll_pending:
                        m += forward; first_roll_pending=False
                    t=roll_tier_premod(m)
                    rolls+=1
                    if t=="strong": filled+=1
                    elif t=="weak": filled+=1; h.lose(WEAK_COST)
                    else:
                        before=h.ooa; h.lose(MISS_COST)
                        if h.ooa and not before: ooa+=1
                    if filled>=needed: break
                guard+=1
                if guard>300: break
            chal_rolls.append(rolls)
            if antag>=ANTAG_TRACK_LEN: lost=True; break
        if lost: break
        active=[h for h in heroes if not h.ooa]
        for i in range(REGULAR_ROLLS_PER_MS):
            if not active: break
            h=active[i%len(active)]
            t=roll_tier_premod(mod())
            if t=="weak": h.lose(WEAK_COST)
            elif t=="miss":
                before=h.ooa; h.lose(MISS_COST)
                if h.ooa and not before: ooa+=1
        if ms in rest_points:
            for h in heroes: h.heal(RECOVERY_HEAL)
    return {"lost":lost,"any_ooa":ooa>0,"ooa":ooa,"flees":flees,"antag":antag,
            "end_r":mean(h.r for h in heroes),
            "danger":any(h.lowest<=DANGER_FLOOR for h in heroes),
            "min_r":min(h.lowest for h in heroes),
            "chal_rolls":mean(chal_rolls) if chal_rolls else 0}

def roll_tier_premod(m):
    # same as roll_tier but mod already includes any forward; kept separate for clarity
    d1, d2 = random.randint(1,6), random.randint(1,6)
    total = d1 + d2 + m
    tier = "strong" if total>=10 else "weak" if total>=7 else "miss"
    if ORACLE_BLESSING and d1==d2:
        tier = {"miss":"weak","weak":"strong","strong":"strong"}[tier]
    return tier

def summarize(label,**kw):
    res=[simulate(**kw) for _ in range(N_QUESTS)]
    n=len(res)
    print(f"{label:<40} loss={sum(r['lost'] for r in res)/n:6.2%}  "
          f"anyOoA={sum(r['any_ooa'] for r in res)/n:6.2%}  "
          f"OoA/Q={mean(r['ooa'] for r in res):.3f}  "
          f"danger={sum(r['danger'] for r in res)/n:6.2%}  "
          f"minR={mean(r['min_r'] for r in res):.2f}  "
          f"endR={mean(r['end_r'] for r in res):.2f}  "
          f"villain={mean(r['antag'] for r in res):.2f}  "
          f"rolls/chal={mean(r['chal_rolls'] for r in res):.2f}")

if __name__=="__main__":
    print(f"party={PARTY_SIZE} ms={MILESTONES} chal/ms={CHALLENGES_PER_MS}(Easy={EASY_CHALLENGE_BOXES}) "
          f"reg/ms={REGULAR_ROLLS_PER_MS} p+2={P_PLUS2} oracle={ORACLE_BLESSING} N={N_QUESTS:,}\n")
    print("Start a Challenge tier odds (2d6+1, Oracle on): Strong 33.3% / Weak 44.4% / Miss 22.2%")
    print("  -> first-roll forward applied:  +1 33.3% / 0 44.4% / -1 22.2%  (net E = +0.11)\n")
    print("-- rational play: flee @ R<=4, 1 Recovery Scene --")
    summarize("BASELINE  (no Start a Challenge)",  use_start_challenge=False)
    summarize("START a CHALLENGE (+1/0/-1 fwd)",   use_start_challenge=True)
    print("\n-- stress: no flee, no rest (pure attrition, isolates the modifier) --")
    summarize("BASELINE  (no Start a Challenge)",  use_start_challenge=False, flee_threshold=0, rests=0)
    summarize("START a CHALLENGE (+1/0/-1 fwd)",   use_start_challenge=True,  flee_threshold=0, rests=0)
