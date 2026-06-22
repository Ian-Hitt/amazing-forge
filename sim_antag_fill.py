#!/usr/bin/env python3
"""
Lights, Camera, Action! — "how often does the Antagonist Track FILL?" audit.

Question: across the four Story Arc types, how often does the villain actually
fill its track (= the heroes LOSE the arc), and how full does it typically get?

Model (Master Reference §6/§7, Math & Sim §4b + the 2026-06-08 broadening):
  * The Antagonist Track is the losing side of the SAME arc; length = the Story
    Arc Track (Episode 3 / Movie 8 / Season 8 / Series 12).
  * Heroes fill THEIR track at 1 box per Milestone (the unified headway rule).
    The arc therefore runs N milestones; finishing N hero boxes = heroes win.
    It is a RACE: villain fills N first -> arc lost.
  * Villain advances two ways:
      (a) FLEE a Challenge  -> +1 villain box (the modeled floor, §4b).
          Rational play keeps a margin: heroes won't take the flee that fills
          the LAST box (matches sim_flee_retreat.py line 71).
      (b) Optional Pay-the-Price tick on a *telling* Miss -> +1 villain box.
          Table-discretionary, NEVER automatic. Modeled as: on a Miss, with
          probability P_PTP_TICK the table narrates a villain gain. This is the
          "main way Season/Series villains advance" per the Master Reference,
          and is the lever that is otherwise UNMODELED.
  * Recovery never advances the villain (double-count dropped, §4b finding).

We sweep P_PTP_TICK (how trigger-happy the table is) against all four arc types.
"""
import random
from statistics import mean

PARTY_SIZE           = 3
CHALLENGES_PER_MS    = 2
REGULAR_ROLLS_PER_MS = 3
READINESS_MAX        = 9
READINESS_START      = 9
WEAK_COST            = 1
MISS_COST            = 2
RECOVERY_HEAL        = 3
P_PLUS2              = 0.85          # current estimate w/ mandatory Attribute (§3b)
ORACLE_BLESSING      = True
FLEE_THRESHOLD       = 4            # flee when lowest active Readiness <= this
RESTS_PER_3_MS       = 1            # ~1 Recovery Scene per 3 milestones
N_ARCS               = 100_000

ARC_TYPES = [("Episode", 3), ("Movie", 8), ("Season", 8), ("Series", 12)]

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

def simulate(track_len, p_ptp_tick, use_flee=True):
    heroes=[Hero() for _ in range(PARTY_SIZE)]
    challenge_boxes = PARTY_SIZE          # "Easy" challenge
    antag=0; flees=0; ptp_ticks=0; ooa=0; lost=False

    # ~1 rest per 3 milestones, spread evenly
    rests = max(0, round(track_len / 3 * RESTS_PER_3_MS))
    rest_points=set()
    if rests>0:
        step=track_len/(rests+1)
        rest_points={int(round(step*(k+1))) for k in range(rests)}

    for ms in range(1, track_len+1):
        for _ in range(CHALLENGES_PER_MS):
            filled=0; guard=0
            while filled<challenge_boxes:
                active=[h for h in heroes if not h.ooa]
                if not active: break
                # rational flee: take it when hurting, but keep a 1-box margin
                if (use_flee and min(h.r for h in active)<=FLEE_THRESHOLD
                        and antag < track_len-1):
                    antag+=1; flees+=1
                    break
                for h in active:
                    t=roll_tier(mod())
                    if t=="strong": filled+=1
                    elif t=="weak": filled+=1; h.lose(WEAK_COST)
                    else:
                        before=h.ooa; h.lose(MISS_COST)
                        if h.ooa and not before: ooa+=1
                        if random.random() < p_ptp_tick:
                            antag+=1; ptp_ticks+=1
                            if antag>=track_len: lost=True; break
                    if filled>=challenge_boxes: break
                if lost: break
                guard+=1
                if guard>500: break
            if antag>=track_len: lost=True; break
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
                if random.random() < p_ptp_tick:
                    antag+=1; ptp_ticks+=1
                    if antag>=track_len: lost=True; break
        if lost: break
        if ms in rest_points:
            for h in heroes: h.heal(RECOVERY_HEAL)

    return {"lost":lost,"any_ooa":ooa>0,"flees":flees,"ptp":ptp_ticks,
            "antag":antag,"fill":antag/track_len}

def summarize(label, track_len, p_ptp_tick, **kw):
    res=[simulate(track_len,p_ptp_tick,**kw) for _ in range(N_ARCS)]
    n=len(res)
    print(f"{label:<22} loss={sum(r['lost'] for r in res)/n:6.2%}  "
          f"villain={mean(r['antag'] for r in res):5.2f}/{track_len:<2} "
          f"({mean(r['fill'] for r in res):5.1%} full)  "
          f"flees={mean(r['flees'] for r in res):.2f}  "
          f"ptpTicks={mean(r['ptp'] for r in res):.2f}  "
          f"anyOoA={sum(r['any_ooa'] for r in res)/n:6.2%}")

if __name__=="__main__":
    print(f"party={PARTY_SIZE} chal/ms={CHALLENGES_PER_MS}(Easy={PARTY_SIZE}) "
          f"reg/ms={REGULAR_ROLLS_PER_MS} p+2={P_PLUS2} oracle={ORACLE_BLESSING} "
          f"flee@R<={FLEE_THRESHOLD} rests=1/3ms\n")
    for ptp in (0.0, 0.10, 0.25, 0.50):
        print(f"=== Optional Pay-the-Price villain tick fires on {ptp:.0%} of Misses ===")
        for name, length in ARC_TYPES:
            summarize(f"  {name} ({length})", length, ptp)
        print()
