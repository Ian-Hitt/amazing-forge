"""
Devil's-bargain clock v2 — adds the "can't bargain the knockout roll" rule.

Same core as sim_devils.py, plus:
  - LETHAL_BARGAIN_OK = False  -> you may NOT use the bargain on a Miss whose
    damage would take you to 0 (you can't buy your way out of Out of Action).
    Consequence: defensive players bargain PREEMPTIVELY at low Readiness to stay
    out of the danger zone, and OoA actually lands sometimes.
  - OOA_TICK = True            -> going Out of Action advances the villain +1.
  - tracks mean bargains used and mean OoA events, to see who feeds the clock.

Strategies:
  never   - never bargain
  need    - bargain only to avoid OoA (only legal when LETHAL_BARGAIN_OK)
  healthy - bargain when a hit would leave you at <= DANGER (preemptive defense)
  hbuf2   - healthy AND a villain-buffer of 2 (defensive + opportunistic)
  buffer2 - bargain while villain > 2 from winning
  greedy  - bargain whenever it won't lose this roll
"""
import random

P_STAT = 0.55
Q_ASSET = 0.469
START_ASSETS = 3
READ_MAX = 9
REST_TRIGGER = 4   # expected play: Recovery Scene after ~5-6 lost (Readiness 3-4)
DIFF = [(2, 0.4), (3, 0.4), (4, 0.2)]
REG_PER_MS = 2

OOA_TICK = True
LETHAL_BARGAIN_OK = True
DANGER = 2          # "healthy" players bargain when a hit would leave them <= this

def pick_diff():
    r = random.random(); c = 0.0
    for boxes, p in DIFF:
        c += p
        if r <= c: return boxes
    return DIFF[-1][0]

def hero_mod(working):
    stat = 1 if random.random() < P_STAT else 0
    pa = 1 - (1 - Q_ASSET) ** max(working, 0)
    asset = 1 if random.random() < pa else 0
    return stat + asset

def roll():
    a = random.randint(1, 6); b = random.randint(1, 6)
    return a, b, (a == b)

def outcome(a, b, mod, doubles):
    total = a + b + mod
    if total >= 10: tier = 'S'
    elif total >= 7: tier = 'W'
    else: tier = 'M'
    if doubles and tier == 'W': tier = 'S'
    return tier

def will_bargain(strategy, v, L, readiness, dmg, lethal):
    if v + 1 >= L: return False                       # never hand the villain the win
    if (not LETHAL_BARGAIN_OK) and lethal: return False  # can't buy out of a knockout
    if strategy == 'never':  return False
    if strategy == 'need':   return (readiness - dmg) <= 0
    if strategy == 'healthy':return (readiness - dmg) <= DANGER
    if strategy == 'greedy': return True
    if strategy.startswith('hbuf'):
        b = int(strategy[4:])
        return (v < (L - b)) or ((readiness - dmg) <= DANGER)
    if strategy.startswith('buffer'):
        b = int(strategy[6:])
        return v < (L - b)
    return False

def simulate(M, L, P, strategy):
    read = [READ_MAX] * P
    work = [START_ASSETS] * P
    out = [False] * P
    st = {'v': 0, 'turn': 0, 'lost': False, 'nb': 0, 'noo': 0}

    def free_recovery():
        for i in range(P):
            read[i] = READ_MAX; out[i] = False

    def next_hero():
        for _ in range(P):
            i = st['turn'] % P; st['turn'] += 1
            if not out[i]: return i
        return None

    def tick(n=1):
        st['v'] += n
        if st['v'] >= L: st['lost'] = True

    def damage(i, dmg):
        read[i] -= dmg
        if read[i] <= 0:
            read[i] = 0; out[i] = True
            work[i] = max(0, work[i] - 1)
            st['noo'] += 1
            if OOA_TICK: tick(1)

    def handle_miss(i, dbl, is_challenge):
        # returns True if a box was filled (challenge bargain upgrade)
        if dbl:
            tick(1)
        if st['lost']: return False
        lethal = (read[i] - 2) <= 0
        if will_bargain(strategy, st['v'], L, read[i], 2, lethal):
            st['nb'] += 1
            tick(1)
            if st['lost']: return False
            return is_challenge   # upgraded to Strong -> fills a box in a challenge
        else:
            damage(i, 2)
            return False

    for ms in range(M):
        boxes_needed = pick_diff()
        filled = 0; retries = 0
        while filled < boxes_needed and not st['lost']:
            i = next_hero()
            if i is None:
                free_recovery(); filled = 0; retries += 1
                if retries > 6: break
                continue
            a, b, dbl = roll()
            tier = outcome(a, b, hero_mod(work[i]), dbl)
            if tier in ('S', 'W'):
                filled += 1
                if tier == 'W': damage(i, 1)
            else:
                if handle_miss(i, dbl, True): filled += 1
        if st['lost']: return ('loss', st['v'], st['nb'], st['noo'])
        if min(read) <= REST_TRIGGER: free_recovery()

        for _ in range(REG_PER_MS):
            if st['lost']: break
            i = next_hero()
            if i is None:
                free_recovery(); i = next_hero()
            a, b, dbl = roll()
            tier = outcome(a, b, hero_mod(work[i]), dbl)
            if tier == 'M':
                handle_miss(i, dbl, False)
        if st['lost']: return ('loss', st['v'], st['nb'], st['noo'])
        if min(read) <= REST_TRIGGER: free_recovery()

    return ('win', st['v'], st['nb'], st['noo'])

def run(M, L, P, strategy, trials=60000):
    loss = end = near = barg = ooa = 0
    for _ in range(trials):
        res, v, nb, noo = simulate(M, L, P, strategy)
        end += v; barg += nb; ooa += noo
        if res == 'loss': loss += 1
        elif v == L - 1: near += 1
    n = trials
    return dict(loss=loss/n, end=end/n, near=near/n, barg=barg/n, ooa=ooa/n)

def block(title, M, L, P, strategies):
    print(f"\n  {title}  (party {P}, L={L})")
    print(f"    {'strategy':9} | {'loss%':>6} {'near%':>6} | {'endbox':>6} {'#barg':>6} {'#OoA':>6}")
    for s in strategies:
        r = run(M, L, P, s)
        print(f"    {s:9} | {r['loss']*100:6.2f} {r['near']*100:6.2f} | "
              f"{r['end']:6.2f} {r['barg']:6.2f} {r['ooa']:6.2f}")

def sweep(title, M, Ls, P):
    # PHOTO-FINISH headline: near-miss% is the deliverable, loss% the guardrail.
    print(f"\n===== {title}  (party {P}, {M} ms) — rule: can't bargain knockout, OoA ticks =====")
    print(f"    cautious(buf3)        realistic(hbuf2)      reckless(greedy)")
    print(f"    {'L':>2} | {'near%':>6} {'loss%':>6}  | {'near%':>6} {'loss%':>6}  | {'near%':>6} {'loss%':>6}")
    for L in Ls:
        rc = run(M, L, P, 'buffer3')
        rr = run(M, L, P, 'hbuf2')
        rg = run(M, L, P, 'greedy')
        print(f"    {L:>2} | {rc['near']*100:6.1f} {rc['loss']*100:6.1f}  | "
              f"{rr['near']*100:6.1f} {rr['loss']*100:6.1f}  | "
              f"{rg['near']*100:6.1f} {rg['loss']*100:6.1f}")

def confirm(title, M, L, P):
    print(f"\n  {title}  L={L}, party {P}")
    print(f"    {'temperament':12} | {'photo-finish%':>13} | {'loss%':>6}")
    for label, s in [('cautious', 'buffer3'), ('realistic', 'hbuf2'),
                     ('reckless', 'greedy')]:
        r = run(M, L, P, s)
        print(f"    {label:12} | {r['near']*100:13.1f} | {r['loss']*100:6.1f}")

if __name__ == '__main__':
    random.seed(12345)
    LETHAL_BARGAIN_OK = False
    OOA_TICK = True
    print("Confirm chosen structure: EPISODE 5 (attacks 1/3/5), MOVIE 9 (attacks 1/3/5/7/9)")
    print("Recovery at Readiness ~4 (REST_TRIGGER=4).")
    print("\n========== EPISODE = 5 ==========")
    confirm("EPISODE", 3, 5, 2)
    confirm("EPISODE", 3, 5, 4)
    print("\n========== MOVIE = 9  (vs 10, 11 for context) ==========")
    confirm("MOVIE", 6, 9, 2)
    confirm("MOVIE", 6, 9, 4)
    confirm("MOVIE", 6, 10, 2)
    confirm("MOVIE", 6, 11, 2)
