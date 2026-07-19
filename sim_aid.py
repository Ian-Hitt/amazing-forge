#!/usr/bin/env python3
"""
Lights, Camera, Action! — fully-stacking Aid model (2026-06-14).

Does letting MULTIPLE allies stack Aid on one roll (+4/+6 spikes) dent the loss curve?
The brake is the cost: a helper whose Aid is a Weak Hit loses 1 Readiness, a Miss loses 2,
AND every helper spends their turn buffing instead of acting. This sim makes both costs
explicit.

ALSO COVERS `Prepare` (the core move added 2026-07-18): Prepare is Aid pointed at your
OWN later roll instead of an ally's. Identical turn cost and Readiness risk (Strong banks
+2, Weak +1 and -1, Miss nothing and -2), so it lives inside this model's envelope — and
below its ceiling, since a lone Prepare tops out at +2 (no multi-helper +4/+6 spike) and the
banked bonus can expire unspent. A Prepare Miss is just a Miss (no new Antagonist-Track
trigger). No separate sim required; the `spam`/`climax` policies here bound the worst case.

Part 1 — a single decisive roll: success odds + helper Readiness spent for 0/1/2 helpers.
Part 2 — full Story (Movie/Episode) under three Aid policies, to see if stacking moves loss:
   none   = baseline (everyone acts independently; == sim_spine canonical)
   spam   = every Challenge round, 2 allies stack Aid on one lead
   climax = stacking only during the final Milestone's Challenges (the clutch use)

Attrition/recovery identical to sim_spine.py.
"""
import random
from statistics import mean

PARTY_SIZE   = 3
READINESS_MAX= 9
WEAK_COST    = 1
MISS_COST    = 2
P_PLUS2      = 0.85
ORACLE       = True
CAP_DROP     = 1
CAP_FLOOR    = 4
CAP_ON_FORCED= True
USE_MEND     = True
MEND_THRESH  = 4
N            = 200_000
N_STORIES    = 60_000

def roll_tier(m):
    d1,d2=random.randint(1,6),random.randint(1,6)
    t="strong" if d1+d2+m>=10 else "weak" if d1+d2+m>=7 else "miss"
    if ORACLE and d1==d2: t={"miss":"weak","weak":"strong","strong":"strong"}[t]
    return t
def mod(): return 2 if random.random()<P_PLUS2 else 1

# ---- Part 1: a single decisive roll ----------------------------------------
def aid_once():
    """one helper aids: returns (bonus_to_lead, readiness_cost_to_helper)."""
    t=roll_tier(mod())
    if t=="strong": return 2,0
    if t=="weak":   return 1,WEAK_COST
    return 0,MISS_COST

def decisive_roll(n_helpers):
    bonus=0; cost=0
    for _ in range(n_helpers):
        b,c=aid_once(); bonus+=b; cost+=c
    t=roll_tier(mod()+bonus)
    return t, cost

def part1():
    print("PART 1 — one decisive roll (lead's own mod is +2 @85% / +1, Oracle on):")
    print(f"  {'helpers':<9}{'P(Strong)':>11}{'P(success)':>12}{'avg team Readiness spent aiding':>34}")
    for h in (0,1,2):
        res=[decisive_roll(h) for _ in range(N)]
        strong=sum(t=='strong' for t,_ in res)/N
        succ  =sum(t!='miss'   for t,_ in res)/N
        spent =mean(c for _,c in res)
        print(f"  {h:<9}{strong:>10.1%}{succ:>12.1%}{spent:>30.2f}")
    print("  (success = Strong or Weak; a Weak still wins the box / Showdown, with a price)\n")

# ---- Part 2: full Story with an Aid policy ---------------------------------
class Hero:
    __slots__=("r","ooa")
    def __init__(self): self.r=READINESS_MAX; self.ooa=False
    def lose(self,n):
        self.r-=n
        if self.r<=0: self.r=0; self.ooa=True

def simulate(milestones, antag_len, rest_trigger, policy):
    heroes=[Hero() for _ in range(PARTY_SIZE)]
    cb=PARTY_SIZE
    antag=0; lost=False; ooa=0
    cap=[READINESS_MAX]

    def regroup(forced):
        nonlocal antag,lost
        antag+=1
        if CAP_ON_FORCED or not forced: cap[0]=max(CAP_FLOOR,cap[0]-CAP_DROP)
        for h in heroes: h.r=cap[0]; h.ooa=False
        if antag>=antag_len: lost=True

    def lull():
        if lost: return
        if any(h.ooa for h in heroes): regroup(True); return
        if mean(h.r for h in heroes)<=rest_trigger and antag<antag_len-1:
            regroup(False); return
        if USE_MEND:
            for h in heroes:
                if 0<h.r<=MEND_THRESH:
                    t=roll_tier(mod()); d=3 if t=='strong' else 2 if t=='weak' else -1
                    h.r=max(0,min(cap[0],h.r+d))
                    if h.r<=0: h.ooa=True

    def challenge(use_aid):
        nonlocal ooa
        filled=0; guard=0
        while filled<cb:
            active=[h for h in heroes if not h.ooa]
            if not active: break
            if use_aid and len(active)>=3:
                # 2 allies stack Aid on one lead -> ONE buffed attempt this round
                lead=active[0]; helpers=active[1:3]
                bonus=0
                for hh in helpers:
                    t=roll_tier(mod())
                    if t=="strong": bonus+=2
                    elif t=="weak": bonus+=1; hh.lose(WEAK_COST)
                    else: b=hh.ooa; hh.lose(MISS_COST); ooa+=(hh.ooa and not b)
                t=roll_tier(mod()+bonus)
                if t=="strong": filled+=1
                elif t=="weak": filled+=1; lead.lose(WEAK_COST)
                else: b=lead.ooa; lead.lose(MISS_COST); ooa+=(lead.ooa and not b)
            else:
                for h in active:
                    t=roll_tier(mod())
                    if t=="strong": filled+=1
                    elif t=="weak": filled+=1; h.lose(WEAK_COST)
                    else: b=h.ooa; h.lose(MISS_COST); ooa+=(h.ooa and not b)
                    if filled>=cb: break
            guard+=1
            if guard>500: break

    for ms in range(milestones):
        use_aid = (policy=='spam') or (policy=='climax' and ms==milestones-1)
        for _ in range(2):                       # CHALLENGES_PER_MS
            challenge(use_aid); lull()
            if lost: break
        if lost: break
        active=[h for h in heroes if not h.ooa]
        for k in range(3):                       # REGULAR_PER_MS
            if not active: break
            h=active[k%len(active)]; t=roll_tier(mod())
            if t=="weak": h.lose(WEAK_COST)
            elif t=="miss": b=h.ooa; h.lose(MISS_COST); ooa+=(h.ooa and not b)
        lull()
        if lost: break
    return {"lost":lost,"photo":(not lost) and antag==antag_len-1}

def run(label, ms, antag_len, trig, policy):
    res=[simulate(ms,antag_len,trig,policy) for _ in range(N_STORIES)]
    n=len(res)
    print(f"  {label:<26} loss={sum(r['lost'] for r in res)/n:6.2%}  "
          f"photo={sum(r['photo'] for r in res)/n:6.2%}")

if __name__=="__main__":
    part1()
    print("PART 2 — full Story loss/photo by Aid policy:")
    print(" MOVIE (6/3, trig<=5):")
    for p in ('none','climax','spam'):
        run(f"   policy={p}", 6,3,5,p)
    print(" EPISODE (3/2, trig<=6):")
    for p in ('none','climax','spam'):
        run(f"   policy={p}", 3,2,6,p)
