#!/usr/bin/env python3
"""
Lights, Camera, Action! — single-spine, emergent-surge model (2026-06-13).

Story-native structure (replaces the sandbox concurrent-tracks model):
  * ONE spine per Story. Two tracks:
      - Story Arc Track  : heroes' progress, 1 box per Milestone (the finale is
        reached when the last Milestone is marked).
      - Antagonist Track : SHORT, climax box reserved on top. Length = number of
        surge-beats (Episode 2, Movie 4). Boxes 1..N-1 fill from emergent surges;
        box N is the CLIMAX (reached by story at the finale, not by attrition).
  * SURGE = the heroes "fall back and regroup" (a weighty, infrequent Recovery
    Scene — the quiet/B-plot beat between dangers). It HEALS a lot and advances
    the Antagonist Track one box. Emergent & player-chosen: you fall back when
    you're hurt enough to need to, discovered at the table — never scheduled.
  * Players keep the climax box free: they won't VOLUNTARILY surge into box N.
  * LOSS VECTOR: a hero knocked Out of Action forces a regroup that surges even
    into the climax box -> antagonist wins BEFORE the finale (pre-climax loss).
  * Goal: tune heal size so the party falls back ~N-1 times across the Story, so
    the Antagonist Track reliably sits at N-1 (photo-finish) when the finale
    arrives, with the occasional OoA-driven pre-climax loss.

Attrition model identical to the prior sims (party 3, Easy challenges, p+2=0.85,
Oracle on) so numbers are comparable.
"""
import random
from statistics import mean

PARTY_SIZE        = 3
CHALLENGES_PER_MS = 2
REGULAR_PER_MS    = 3
READINESS_MAX     = 9
WEAK_COST         = 1
MISS_COST         = 2
P_PLUS2           = 0.85
ORACLE            = True
HEAL_MODE         = 'full'   # the surge-triggering regroup: 'full' = top-up to 9; 'rolled' = +3/+2/-1
USE_MEND          = False    # Option C: a small risky tactical Mend (no surge), used between regroups
MEND_THRESH       = 4        # a hero Mends when hurt to <= this (and the party isn't fully regrouping)
MEND_GATED        = False    # Mend is ungated (any scene); limited by the -1 risk + the declining ceiling
CAP_DROP          = 1        # declining recovery ceiling: each Recovery Scene lowers the cap by this (0 = heal to full)
CAP_FLOOR         = 4        # the recovery ceiling never drops below this
CAP_ON_FORCED     = True     # does an Out-of-Action (forced) regroup also lower the ceiling?
N_STORIES         = 80_000

def tier(m):
    d1,d2=random.randint(1,6),random.randint(1,6)
    t="strong" if d1+d2+m>=10 else "weak" if d1+d2+m>=7 else "miss"
    if ORACLE and d1==d2: t={"miss":"weak","weak":"strong","strong":"strong"}[t]
    return t
def mod(): return 2 if random.random()<P_PLUS2 else 1

class Hero:
    __slots__=("r","ooa","mended")
    def __init__(self): self.r=READINESS_MAX; self.ooa=False; self.mended=False
    def lose(self,n):
        self.r-=n
        if self.r<=0: self.r=0; self.ooa=True

def simulate(milestones, antag_len, heal, rest_trigger):
    heroes=[Hero() for _ in range(PARTY_SIZE)]
    cb=PARTY_SIZE
    antag=0; falls=0; forced=0; ooa=0; lost=False
    cap=[READINESS_MAX]; first_avg=[None]

    def regroup(forced_revive):
        nonlocal antag,falls,forced,lost
        antag+=1
        if forced_revive: forced+=1
        else: falls+=1
        if CAP_DROP:                                  # declining ceiling: drop, then restore to it
            if CAP_ON_FORCED or not forced_revive:
                cap[0]=max(CAP_FLOOR, cap[0]-CAP_DROP)
            for h in heroes: h.r=cap[0]; h.ooa=False
        else:                                         # heal to full (or +heal capped)
            for h in heroes:
                h.r=min(READINESS_MAX,h.r+heal)
                if h.r>0: h.ooa=False
        if (not forced_revive) and first_avg[0] is None:
            first_avg[0]=mean(h.r for h in heroes)
        if antag>=antag_len: lost=True   # climax box filled early

    mends=[0]
    def lull():
        nonlocal lost
        if lost: return
        if any(h.ooa for h in heroes):
            regroup(True); return                         # forced (ignores reserve)
        if (mean(h.r for h in heroes)<=rest_trigger
              and antag < antag_len-1):
            regroup(False); return                        # voluntary (keeps climax free)
        if USE_MEND:                                      # Option C: small risky patch, no surge
            for h in heroes:
                if (not (MEND_GATED and h.mended)) and 0 < h.r <= MEND_THRESH:
                    h.mended=True; mends[0]+=1
                    t=tier(mod()); d = 3 if t=='strong' else 2 if t=='weak' else -1
                    h.r=max(0,min(cap[0],h.r+d))      # Mend can't exceed the current ceiling
                    if h.r<=0: h.ooa=True

    for ms in range(milestones):
        for h in heroes: h.mended=False
        for _ in range(CHALLENGES_PER_MS):
            filled=0; guard=0
            while filled<cb:
                active=[h for h in heroes if not h.ooa]
                if not active: break
                for h in active:
                    t=tier(mod())
                    if t=="strong": filled+=1
                    elif t=="weak": filled+=1; h.lose(WEAK_COST)
                    else:
                        b=h.ooa; h.lose(MISS_COST); ooa+= (h.ooa and not b)
                    if filled>=cb: break
                guard+=1
                if guard>500: break
            lull()
            if lost: break
        if lost: break
        active=[h for h in heroes if not h.ooa]
        for i in range(REGULAR_PER_MS):
            if not active: break
            h=active[i%len(active)]; t=tier(mod())
            if t=="weak": h.lose(WEAK_COST)
            elif t=="miss":
                b=h.ooa; h.lose(MISS_COST); ooa+=(h.ooa and not b)
        lull()
        if lost: break

    return {"lost":lost,"antag":antag,"falls":falls,"forced":forced,"mends":mends[0],
            "first_rest_avg":first_avg[0],"end_cap":cap[0],
            "photo": (not lost) and antag==antag_len-1,
            "low":   (not lost) and antag <antag_len-1,
            "any_ooa":ooa>0}

def run(label, milestones, antag_len, rest_trigger):
    res=[simulate(milestones,antag_len,9,rest_trigger) for _ in range(N_STORIES)]
    n=len(res); fa=[r['first_rest_avg'] for r in res if r['first_rest_avg'] is not None]
    print(f"  {label:<22} 1stRest={mean(fa) if fa else 0:.1f} "
          f"PHOTO-FINISH={sum(r['photo'] for r in res)/n:6.2%}  "
          f"loss={sum(r['lost'] for r in res)/n:6.2%}  "
          f"anyOoA={sum(r['any_ooa'] for r in res)/n:6.2%}")

if __name__=="__main__":
    # CANONICAL LOCKED CONFIG (2026-06-13).
    #   Recovery Scene = fall back & regroup: restores the party to its CURRENT Readiness ceiling
    #     (+1 villain Surge), and lowers that ceiling by 1 for the rest of the Story Arc (floor 4;
    #     resets to 9 at Downtime). So each regroup leaves the party a little worse than the last.
    #   Mend = small risky in-Challenge patch (+3/+2/Miss -1, no surge, capped at the current ceiling).
    #   Sizes: Episode 3/2, Movie 6/3.
    HEAL_MODE='full'; USE_MEND=True   # (module defaults already CAP_DROP=1, CAP_FLOOR=4)
    print(f"party={PARTY_SIZE} p+2={P_PLUS2} oracle={ORACLE}  CAP_DROP={CAP_DROP} floor={CAP_FLOOR}  "
          f"Mend +3/+2/-1\n")
    print("CANONICAL — declining recovery ceiling (-1 per Recovery Scene) + risky Mend")
    run("Episode 3/2 (trig<=6)", 3, 2, 6)
    run("Movie   6/3 (trig<=5)", 6, 3, 5)
