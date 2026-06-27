"""Rolls-to-complete AND expected Readiness lost per challenge track size (3..10).
Raw attrition: fight the track to completion, no bargain, no recovery.
Weak = -1 Readiness, Miss = -2, Strong = 0. Doubles upgrade Weak->Strong."""

from itertools import product

P_STAT = 0.55
Q_ASSET = 0.469
WORK = 3
pa = 1 - (1 - Q_ASSET) ** WORK          # 0.85

# mod distribution
mod_p = {0: (1-P_STAT)*(1-pa), 1: P_STAT*(1-pa) + (1-P_STAT)*pa, 2: P_STAT*pa}

# 2d6 distribution
d2 = {}
for a, b in product(range(1,7), repeat=2):
    d2.setdefault((a+b, a==b), 0)
    d2[(a+b, a==b)] += 1/36

# per-roll outcome probs
pS = pW = pM = 0.0
p_dblmiss = 0.0                            # doubles that stay a Miss -> antagonist +1
for mod, pm in mod_p.items():
    for (tot, dbl), pt in d2.items():
        t = tot + mod
        if t >= 10: tier = 'S'
        elif t >= 7: tier = 'W'
        else: tier = 'M'
        if dbl and tier == 'W': tier = 'S'   # Oracle's Blessing
        if tier == 'S': pS += pm*pt
        elif tier == 'W': pW += pm*pt
        else: pM += pm*pt
        if dbl and tier == 'M': p_dblmiss += pm*pt

p_hit = pS + pW
loss_per_roll = pW*1 + pM*2
print(f"P(doubles-miss / roll)={p_dblmiss:.4f}  (~ (1,1),(2,2), rare (3,3)@+0)\n")

print(f"P(Strong)={pS:.3f}  P(Weak)={pW:.3f}  P(Miss)={pM:.3f}")
print(f"hit rate={p_hit:.3f}  rolls/box={1/p_hit:.3f}  Readiness lost/roll={loss_per_roll:.3f}\n")

print(f"{'boxes':>5} | {'rolls':>6} | {'antag+':>6} | {'total':>6} | {'/2p':>6} | {'/3p':>6} | {'/4p':>6} | {'/5p':>6}")
for n in range(3, 11):
    rolls = n / p_hit
    rd = rolls * loss_per_roll
    antag = rolls * p_dblmiss
    print(f"{n:>5} | {rolls:6.1f} | {antag:6.2f} | {rd:6.1f} | {rd/2:6.1f} | {rd/3:6.1f} | {rd/4:6.1f} | {rd/5:6.1f}")
