#!/usr/bin/env python3
"""
Lights, Camera, Action! — threads & Growth model (2026-06-14).

Question: B-plots/threads add Milestones. Growth = 1 per 3 Milestones the party marks.
Do threads inflate Growth in a way that breaks progression — or is the extra Growth paid
for by extra danger? Ian's hypothesis: more thread-Milestones = more scenes = more
Readiness drain = more regroups = more Surges on the FIXED (lose-clock-free threads don't
lengthen it) Antagonist Track -> more loss. If so, threads self-balance.

Model: a Story has `main_ms` spine Milestones + `thread_ms` thread Milestones, interleaved.
The Antagonist Track length stays fixed by Story SIZE (Episode 2 / Movie 3) — threads never
lengthen it. Each Milestone is a load of (Challenges, Regular-Roll scenes) that drains
Readiness; thread load is either 'full' (same as a main Milestone) or 'light' (quiet
character beats: no Challenge, a couple of rolls).

Attrition/recovery logic is copied verbatim from sim_spine.py (canonical) so numbers compare.
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
N_STORIES    = 60_000

MAIN_LOAD  = (2, 3)   # (Challenges, Regular scenes) per main Milestone — matches sim_spine
FULL_THREAD= (2, 3)   # a thread treated like a full spine Milestone
LIGHT_THREAD=(0, 2)   # a quiet B-plot Milestone: no Challenge, a couple of character rolls

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

def simulate(main_ms, thread_ms, antag_len, rest_trigger, thread_load):
    heroes=[Hero() for _ in range(PARTY_SIZE)]
    cb=PARTY_SIZE
    antag=0; lost=False; ooa=0; marked=0
    cap=[READINESS_MAX]

    # Build interleaved Milestone schedule: each entry is (challenges, regulars).
    sched=[]
    mains=[MAIN_LOAD]*main_ms
    thr=[thread_load]*thread_ms
    # round-robin interleave so threads are spread across the Story, not all bunched late
    i=j=0
    total=main_ms+thread_ms
    ratio=(thread_ms/main_ms) if main_ms else 0
    acc=0.0
    for _ in range(main_ms):
        sched.append(mains[i]); i+=1
        acc+=ratio
        while acc>=1 and j<thread_ms:
            sched.append(thr[j]); j+=1; acc-=1
    while j<thread_ms: sched.append(thr[j]); j+=1

    def regroup(forced):
        nonlocal antag,lost
        antag+=1
        if CAP_ON_FORCED or not forced:
            cap[0]=max(CAP_FLOOR, cap[0]-CAP_DROP)
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
                    t=tier(mod()); d=3 if t=='strong' else 2 if t=='weak' else -1
                    h.r=max(0,min(cap[0],h.r+d))
                    if h.r<=0: h.ooa=True

    for (nch,nreg) in sched:
        for h in heroes: h.mended=False
        for _ in range(nch):
            filled=0; guard=0
            while filled<cb:
                active=[h for h in heroes if not h.ooa]
                if not active: break
                for h in active:
                    t=tier(mod())
                    if t=="strong": filled+=1
                    elif t=="weak": filled+=1; h.lose(WEAK_COST)
                    else:
                        b=h.ooa; h.lose(MISS_COST); ooa+=(h.ooa and not b)
                    if filled>=cb: break
                guard+=1
                if guard>500: break
            lull()
            if lost: break
        if lost: break
        active=[h for h in heroes if not h.ooa]
        for k in range(nreg):
            if not active: break
            h=active[k%len(active)]; t=tier(mod())
            if t=="weak": h.lose(WEAK_COST)
            elif t=="miss":
                b=h.ooa; h.lose(MISS_COST); ooa+=(h.ooa and not b)
        lull()
        if lost: break
        marked+=1   # this Milestone completed

    return {"lost":lost,"marked":marked,"antag":antag,
            "photo":(not lost) and antag==antag_len-1}

def run(label, main_ms, thread_ms, antag_len, rest_trigger, thread_load):
    res=[simulate(main_ms,thread_ms,antag_len,rest_trigger,thread_load) for _ in range(N_STORIES)]
    n=len(res)
    loss=sum(r['lost'] for r in res)/n
    photo=sum(r['photo'] for r in res)/n
    mk=mean(r['marked'] for r in res)
    growth=mk/3                       # party-wide Growth per hero (1 per 3 marked)
    print(f"  {label:<34} loss={loss:6.2%}  photo={photo:6.2%}  "
          f"avg_milestones={mk:4.1f}  Growth/hero={growth:4.2f}")

if __name__=="__main__":
    print(f"party={PARTY_SIZE} p+2={P_PLUS2} oracle={ORACLE} cap_drop={CAP_DROP} floor={CAP_FLOOR}\n")

    print("MOVIE (6 main / 3-box track, trig<=5) — add FULL-load thread Milestones:")
    for t in range(0,10,1):
        run(f"  +{t} full threads ({6+t} MS)", 6, t, 3, 5, FULL_THREAD)
    print("\nMOVIE — add LIGHT-load thread Milestones (quiet B-plot beats):")
    for t in range(0,10,1):
        run(f"  +{t} light threads ({6+t} MS)", 6, t, 3, 5, LIGHT_THREAD)

    print("\nEPISODE (3 main / 2-box track, trig<=6) — add thread Milestones:")
    for t in range(0,5):
        run(f"  +{t} full threads ({3+t} MS)", 3, t, 2, 6, FULL_THREAD)
    for t in range(0,5):
        run(f"  +{t} light threads ({3+t} MS)", 3, t, 2, 6, LIGHT_THREAD)

    print("\nCREDITING-RULE comparison (3 protagonists, Movie spine 6 MS):")
    print("  Structure A: each hero owns a 2-MS character B-plot (+6 thread MS total)")
    print("    party-wide credit  -> each hero Growth = (6 + 6)//3 = 4")
    print("    char-specific      -> each hero Growth = (6 + 2)//3 = 2  (own thread only)")
    print("  Structure B: 2 shared non-character B-plots, ~3 MS total (+3 thread MS)")
    print("    party-wide credit  -> each hero Growth = (6 + 3)//3 = 3")
    print("  Baseline thread-free Movie -> each hero Growth = 6//3 = 2")
