#!/usr/bin/env python3
"""
Amazing Forge — "flee a Challenge" escape-valve simulation.

Model under test (Ian, 2026-06-06):
  * Misses ALWAYS cost Readiness (clean baseline rule restored — no per-Miss trade).
  * The Antagonist Track advances ONLY when the heroes FLEE a Challenge.
  * Fleeing ends the Challenge immediately: its progress is lost, and the villain
    gets one box. It is the heroes' escape valve when the Readiness bleed of
    finishing the Challenge is no longer worth it.
  * The Antagonist Track is short (Easy = 3). Filling it loses the Quest, so
    fleeing is self-limiting. (Fleeing the whole Quest = "quit the Quest".)

Compared against BASELINE (no escape valve; Misses cost Readiness, heroes must
grind every Challenge to the end).
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
N_QUESTS             = 100_000

def roll_tier(mod):
    d1, d2 = random.randint(1,6), random.randint(1,6)
    total = d1 + d2 + mod
    tier = "strong" if total>=10 else "weak" if total>=7 else "miss"
    if ORACLE_BLESSING and d1==d2:
        tier = {"miss":"weak","weak":"strong","strong":"strong"}[tier]
    return tier

def mod():
    return 2 if random.random() < P_PLUS2 else 1

class Hero:
    __slots__=("r","ooa")
    def __init__(self): self.r=READINESS_START; self.ooa=False
    def lose(self,n):
        self.r-=n
        if self.r<=0: self.r=0; self.ooa=True
    def heal(self,n):
        self.r=min(READINESS_MAX,self.r+n)
        if self.r>0: self.ooa=False

def simulate(use_flee, flee_threshold, rests, rest_advances_antag):
    heroes=[Hero() for _ in range(PARTY_SIZE)]
    antag=0; flees=0; ooa=0; lost=False
    rest_points=set()
    if rests>0:
        step=MILESTONES/(rests+1)
        rest_points={int(round(step*(k+1))) for k in range(rests)}

    for ms in range(1,MILESTONES+1):
        for _ in range(CHALLENGES_PER_MS):
            needed=EASY_CHALLENGE_BOXES; filled=0; guard=0
            while filled<needed:
                active=[h for h in heroes if not h.ooa]
                if not active: break
                # flee decision at the top of each round-robin pass
                if use_flee and min(h.r for h in active)<=flee_threshold and antag < ANTAG_TRACK_LEN-1:
                    antag+=1; flees+=1
                    break  # abandon challenge; progress lost
                for h in active:
                    t=roll_tier(mod())
                    if t=="strong": filled+=1
                    elif t=="weak": filled+=1; h.lose(WEAK_COST)
                    else:
                        before=h.ooa; h.lose(MISS_COST)
                        if h.ooa and not before: ooa+=1
                    if filled>=needed: break
                guard+=1
                if guard>300: break
            if antag>=ANTAG_TRACK_LEN: lost=True; break
        if lost: break
        # regular rolls (single rolls; no flee option)
        active=[h for h in heroes if not h.ooa]
        for i in range(REGULAR_ROLLS_PER_MS):
            if not active: break
            h=active[i%len(active)]
            t=roll_tier(mod())
            if t=="weak": h.lose(WEAK_COST)
            elif t=="miss":
                before=h.ooa; h.lose(MISS_COST)
                if h.ooa and not before: ooa+=1
        if ms in rest_points:
            if rest_advances_antag and use_flee:
                antag+=1
                if antag>=ANTAG_TRACK_LEN: lost=True; break
            for h in heroes: h.heal(RECOVERY_HEAL)
    return {"lost":lost,"any_ooa":ooa>0,"ooa":ooa,"flees":flees,
            "antag":antag,"end_r":mean(h.r for h in heroes)}

def summarize(label,**kw):
    res=[simulate(**kw) for _ in range(N_QUESTS)]
    n=len(res)
    print(f"{label:<46} loss={sum(r['lost'] for r in res)/n:6.2%}  "
          f"anyOoA={sum(r['any_ooa'] for r in res)/n:6.2%}  "
          f"OoA/quest={mean(r['ooa'] for r in res):.3f}  "
          f"flees={mean(r['flees'] for r in res):.2f}  "
          f"villain={mean(r['antag'] for r in res):.2f}/{ANTAG_TRACK_LEN}  "
          f"endR={mean(r['end_r'] for r in res):.2f}")

if __name__=="__main__":
    print(f"party={PARTY_SIZE} ms={MILESTONES} chal/ms={CHALLENGES_PER_MS}(Easy={EASY_CHALLENGE_BOXES}) "
          f"reg/ms={REGULAR_ROLLS_PER_MS} p+2={P_PLUS2} oracle={ORACLE_BLESSING}\n")
    print("-- with 1 Recovery Scene --")
    summarize("BASELINE (no flee)", use_flee=False, flee_threshold=0, rests=1, rest_advances_antag=False)
    summarize("FLEE @ R<=2", use_flee=True, flee_threshold=2, rests=1, rest_advances_antag=False)
    summarize("FLEE @ R<=4", use_flee=True, flee_threshold=4, rests=1, rest_advances_antag=False)
    summarize("FLEE @ R<=4, rest also advances villain", use_flee=True, flee_threshold=4, rests=1, rest_advances_antag=True)
    print("\n-- with 0 Recovery Scenes --")
    summarize("BASELINE (no flee)", use_flee=False, flee_threshold=0, rests=0, rest_advances_antag=False)
    summarize("FLEE @ R<=2", use_flee=True, flee_threshold=2, rests=0, rest_advances_antag=False)
    summarize("FLEE @ R<=4", use_flee=True, flee_threshold=4, rests=0, rest_advances_antag=False)
