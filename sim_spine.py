#!/usr/bin/env python3
"""
Lights, Camera, Action! — single-spine model (CANONICAL, 2026-06-22 rework).

Supersedes the 2026-06-13 declining-ceiling version. Three locked changes
(see memory dice-and-scaling-rework; explored in scratchpad sim_scaling*/sim_pair*):

  1. CORE ROLL is now +0 / +1 / +2 (split stats + assets).
       - Pick 2 of the 5 stats. The action's MOST-RELEVANT stat is chosen
         objectively (not argued); if it's one of your two -> +1.  P_STAT.
       - 3 specific Assets, flexible/argued; if any apply -> +1.  P_ASSET.
       - both -> +2, one -> +1, neither -> +0.
       Tuned to P_STAT=0.55 / P_ASSET=0.85 -> avg mod ~1.40 (was 1.85), so a +2
       must be earned (fixes the playtest "argue +2 onto everything" problem).

  2. NO RATCHET. A Recovery Scene heals the party FULLY back to 9 every time;
     max Readiness no longer declines. (The old declining ceiling was keyed to
     recovery COUNT, which grows with story length -> it broke Movie scaling.)

  3. TRACKS / LADDER.
       - Episode = 3 Milestones / 2-box Antagonist Track.
       - Movie   = 6 Milestones / 4-box Antagonist Track  (was 3).
       - Duo Movie = 5-box track (one extra regroup; keeps real 2-box challenges
         instead of trivial 1-box "Easy" filler).
       - Difficulty: Easy/Medium/Hard = players-1 / players / players+1.
         The old "+1 box for 4+ players" rule is DROPPED.

Surge-on-Recovery, the reserved climax box, Mend (no surge), and Out-of-Action
as the pre-climax loss vector are all unchanged from the spine model.

Targets (Ian, 2026-06-22): ~10% loss at all-Medium (win 9 of 10). A FRESH party
(no Boons) runs a touch hot on Movies (~16%); Boons pull it toward ~10% as the
party advances, and groups dial down with Easy encounters.
"""
import random
from statistics import mean

# core-roll curve
P_STAT  = 0.55      # P(action's most-relevant stat is one of the hero's 2 of 5)
P_ASSET = 0.85      # P(one of the 3 specific Assets can be argued to apply)
ORACLE  = True      # doubles upgrade a tier (Oracle's Blessing)
BOON_P  = 0.0       # per-roll chance a Boon upgrades the result one tier (0 = fresh party)

# attrition
READINESS_MAX     = 9
WEAK_COST         = 1
MISS_COST         = 2
CHALLENGES_PER_MS = 2
REGULAR_PER_MS    = 3
REST_TRIGGER      = 6      # party falls back (Recovery Scene) when avg Readiness <= this
USE_MEND          = True
MEND_THRESH       = 4

N_STORIES = 80_000

def mod():
    s = random.random() < P_STAT
    a = random.random() < P_ASSET
    return (1 if s else 0) + (1 if a else 0)

def tier(m):
    d1, d2 = random.randint(1, 6), random.randint(1, 6)
    t = "strong" if d1+d2+m >= 10 else "weak" if d1+d2+m >= 7 else "miss"
    if ORACLE and d1 == d2:
        t = {"miss": "weak", "weak": "strong", "strong": "strong"}[t]
    if BOON_P and random.random() < BOON_P:
        t = {"miss": "weak", "weak": "strong", "strong": "strong"}[t]
    return t

class Hero:
    __slots__ = ("r", "ooa", "mended")
    def __init__(self): self.r = READINESS_MAX; self.ooa = False; self.mended = False
    def lose(self, n):
        self.r -= n
        if self.r <= 0: self.r = 0; self.ooa = True

def simulate(milestones, antag_len, party, challenge_boxes):
    heroes = [Hero() for _ in range(party)]
    cb = challenge_boxes
    antag = 0; falls = 0; forced = 0; lost = False

    def regroup(forced_revive):
        nonlocal antag, falls, forced, lost
        antag += 1
        if forced_revive: forced += 1
        else: falls += 1
        for h in heroes:                       # NO ratchet: full heal to 9
            h.r = READINESS_MAX; h.ooa = False
        if antag >= antag_len: lost = True     # filled the reserved climax box -> lose

    def lull():
        nonlocal lost
        if lost: return
        if any(h.ooa for h in heroes):
            regroup(True); return                          # forced (ignores reserve)
        if mean(h.r for h in heroes) <= REST_TRIGGER and antag < antag_len - 1:
            regroup(False); return                         # voluntary (keeps climax free)
        if USE_MEND:
            for h in heroes:
                if 0 < h.r <= MEND_THRESH and not h.mended:
                    h.mended = True
                    t = tier(mod()); d = 3 if t == 'strong' else 2 if t == 'weak' else -1
                    h.r = max(0, min(READINESS_MAX, h.r + d))
                    if h.r <= 0: h.ooa = True

    for ms in range(milestones):
        for h in heroes: h.mended = False
        for _ in range(CHALLENGES_PER_MS):
            filled = 0; guard = 0
            while filled < cb:
                active = [h for h in heroes if not h.ooa]
                if not active: break
                for h in active:
                    t = tier(mod())
                    if t == "strong": filled += 1
                    elif t == "weak": filled += 1; h.lose(WEAK_COST)
                    else: h.lose(MISS_COST)
                    if filled >= cb: break
                guard += 1
                if guard > 500: break
            lull()
            if lost: break
        if lost: break
        active = [h for h in heroes if not h.ooa]
        for i in range(REGULAR_PER_MS):
            if not active: break
            h = active[i % len(active)]; t = tier(mod())
            if t == "weak": h.lose(WEAK_COST)
            elif t == "miss": h.lose(MISS_COST)
        lull()
        if lost: break

    return {"lost": lost, "antag": antag, "falls": falls, "forced": forced}

def loss(milestones, antag_len, party, challenge_boxes):
    res = [simulate(milestones, antag_len, party, challenge_boxes) for _ in range(N_STORIES)]
    n = len(res)
    return sum(r['lost'] for r in res) / n, mean(r['falls'] + r['forced'] for r in res)

def movie_track(party): return 5 if party == 2 else 4   # duo gets one extra regroup

def run(label, milestones, antag_len, party):
    cb = party                       # Medium difficulty = players (ladder centered on Medium)
    l, rec = loss(milestones, antag_len, party, cb)
    print(f"  {label:<26} party {party}  cb={cb}  loss={l:6.2%}  recoveries={rec:.2f}")

if __name__ == "__main__":
    print(f"P_stat={P_STAT} P_asset={P_ASSET}  avg mod ~"
          f"{mean(mod() for _ in range(200_000)):.2f}  (Boon_p={BOON_P})\n")
    print("CANONICAL (2026-06-22) — split stats+assets, no ratchet, all-Medium, fresh party")
    for p in (2, 3, 4):
        run("Episode 3 / 2-box", 3, 2, p)
        run(f"Movie   6 / {movie_track(p)}-box", 6, movie_track(p), p)
    print("\nBoons settle a fresh party toward ~10% as it advances (sweep BOON_P):")
    for bp in (0.0, 0.05, 0.10):
        BOON_P = bp
        l, _ = loss(6, 4, 3, 3)
        print(f"  BOON_P={bp:.2f}  party-3 Movie loss = {l:6.2%}")
