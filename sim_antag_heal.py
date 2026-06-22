#!/usr/bin/env python3
"""
Lights, Camera, Action! — "villain advances when heroes REST" audit.

New tension model (Ian, 2026-06-13): heroes can't die, so the dramatic question
is NOT survival — it's the Antagonist Track. Lean into it. Readiness becomes
*ammunition spent against the villain clock*:

  * The villain advances +1 each time the party takes a RECOVERY SCENE (a rest).
    One tick per rest EVENT, not per hero healed. (Original "heal advances the
    villain" design, restored as the PRIMARY trigger.)
  * Players self-regulate: they rest when hurt, but STOP resting once the track
    is one box from full (keep the margin) -> this parks the track near N-1.
  * LOSS VECTOR: a hero knocked Out of Action MUST be revived. That forced
    Recovery Scene advances the villain EVEN past the margin -> it can fill the
    last box and lose the arc. So the real question becomes "can we avoid going
    Out of Action while the villain is one step from winning?" -- survival
    tension rerouted entirely through the lose-state.
  * No per-challenge flee valve in this model (heroes grind challenges); the
    heal-clock is the sole spine. Quitting = losing the arc anyway.

Recovery Scene = Mend (SF-C): +3 strong / +2 weak / +0 miss (whiff), Oracle on,
once per hero per Milestone, capped at READINESS_MAX. Heals self + allies in the
one scene; the scene advances the villain once.

Metrics across the four arc types:
  loss%        -- villain filled the track (arc lost)
  end fill     -- mean villain boxes / track at arc end
  near-miss%   -- arcs that END at exactly N-1 (the photo finish we want)
  low%         -- arcs that end <= half full (villain felt irrelevant)
  anyOoA%      -- at least one hero hit 0 during the arc
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
P_PLUS2              = 0.85
ORACLE_BLESSING      = True
REST_THRESHOLD       = 5     # OPTIMIZING trigger: rest when AVG party Readiness <= this
HEAL_UP_TO           = 6     # when resting, every hero at/below this tops up (batch)
KO_TICK              = 1      # villain boxes a forced (Out-of-Action) revive marks
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
    __slots__=("r","ooa","mended")
    def __init__(self): self.r=READINESS_START; self.ooa=False; self.mended=False
    def lose(self,n):
        self.r-=n
        if self.r<=0: self.r=0; self.ooa=True
    def mend(self):
        if self.mended: return
        self.mended=True
        t=roll_tier(mod())
        heal = 3 if t=="strong" else 2 if t=="weak" else 0
        if heal:
            self.r=min(READINESS_MAX,self.r+heal)
            if self.r>0: self.ooa=False

def simulate(track_len, rest_threshold, max_rests_per_ms=1, mend_gate=True):
    heroes=[Hero() for _ in range(PARTY_SIZE)]
    challenge_boxes = PARTY_SIZE
    antag=0; ooa=0; rests=0; forced=0; lost=False
    rests_this_ms=[0]

    def rest_check():
        # returns True if the arc was just lost
        nonlocal antag, rests, forced, lost
        down = [h for h in heroes if h.ooa]
        hurt = min((h.r for h in heroes), default=READINESS_MAX)
        if down:
            # forced revive: advances villain regardless of margin/cap (loss vector).
            # OoA recovery is EXEMPT from the per-MS gate (you must bring them back).
            antag+=KO_TICK; rests+=1; forced+=1
            for h in heroes:
                if h.ooa or not mend_gate: h.mended=False
                h.mend()
            if antag>=track_len: lost=True; return True
        else:
            avg = mean(h.r for h in heroes)
            # OPTIMIZING: rest only when the party is collectively low (worth a tick),
            # or when someone is about to drop (emergency). Then BATCH-heal everyone
            # who'd benefit (<= HEAL_UP_TO), to get max Readiness back per villain tick.
            if ((avg<=rest_threshold or hurt<=2) and antag < track_len-1
                    and rests_this_ms[0] < max_rests_per_ms):
                antag+=1; rests+=1; rests_this_ms[0]+=1
                for h in heroes:
                    if h.r<=HEAL_UP_TO:
                        if not mend_gate: h.mended=False
                        h.mend()
        return False

    for ms in range(1, track_len+1):
        for h in heroes: h.mended=False
        rests_this_ms[0]=0
        # ---- challenges (no flee; grind to the end), rest-check after each ----
        for _ in range(CHALLENGES_PER_MS):
            filled=0; guard=0
            while filled<challenge_boxes:
                active=[h for h in heroes if not h.ooa]
                if not active: break          # whole party down -> ends below
                for h in active:
                    t=roll_tier(mod())
                    if t=="strong": filled+=1
                    elif t=="weak": filled+=1; h.lose(WEAK_COST)
                    else:
                        before=h.ooa; h.lose(MISS_COST)
                        if h.ooa and not before: ooa+=1
                    if filled>=challenge_boxes: break
                guard+=1
                if guard>500: break
            if rest_check(): break
            if lost: break
        if lost: break
        # ---- regular rolls ----
        active=[h for h in heroes if not h.ooa]
        for i in range(REGULAR_ROLLS_PER_MS):
            if not active: break
            h=active[i%len(active)]
            t=roll_tier(mod())
            if t=="weak": h.lose(WEAK_COST)
            elif t=="miss":
                before=h.ooa; h.lose(MISS_COST)
                if h.ooa and not before: ooa+=1
        # ---- end-of-milestone lull ----
        if rest_check(): break

    fill = antag/track_len
    return {"lost":lost,"antag":antag,"fill":fill,
            "near_miss": (not lost) and antag==track_len-1,
            "low": (not lost) and antag <= track_len/2,
            "any_ooa":ooa>0,"rests":rests,"forced":forced}

def summarize(label, track_len, rest_threshold):
    res=[simulate(track_len,rest_threshold) for _ in range(N_ARCS)]
    n=len(res)
    print(f"{label:<14} loss={sum(r['lost'] for r in res)/n:6.2%}  "
          f"endFill={mean(r['fill'] for r in res):5.1%} ({mean(r['antag'] for r in res):4.1f}/{track_len:<2}) "
          f"nearMiss={sum(r['near_miss'] for r in res)/n:6.2%}  "
          f"low(<=half)={sum(r['low'] for r in res)/n:6.2%}  "
          f"anyOoA={sum(r['any_ooa'] for r in res)/n:6.2%}  "
          f"rests={mean(r['rests'] for r in res):.1f}")

if __name__=="__main__":
    print(f"party={PARTY_SIZE} chal/ms={CHALLENGES_PER_MS}(Easy={PARTY_SIZE}) reg/ms={REGULAR_ROLLS_PER_MS} "
          f"p+2={P_PLUS2} oracle={ORACLE_BLESSING}\n")
    for thr in (4, 5, 6):
        print(f"=== party rests when lowest Readiness <= {thr} ===")
        for name, length in ARC_TYPES:
            summarize(f"  {name} ({length})", length, thr)
        print()
