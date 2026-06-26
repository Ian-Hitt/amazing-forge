"""
Devil's-bargain antagonist clock — Monte Carlo.

Trigger model:
  - Core roll 2d6 + mod (+0/+1/+2): P_STAT=0.55, P_ASSET=0.85 (3 working assets).
    10+ Strong, 7-9 Weak, <=6 Miss. avg mod ~1.40.
  - Doubles on a HIT  -> Oracle's Blessing (upgrade a tier: Weak->Strong).
  - Doubles on a MISS -> villain +1 (RANDOM tick), stays a miss.
  - Devil's bargain (player choice, on any Miss): forgo damage, upgrade to STRONG
    (fill a box if it's a challenge roll), in exchange for villain +1.
    On a doubles-miss, the random +1 already fired, so bargaining it = +2 total.
  - Recovery is FREE (no surge). OoA breaks one asset (mod drops) until story end.

Loss = villain track reaches L before heroes complete all milestones.

Strategies (when does the player take the bargain?):
  never     - never
  need      - only to avoid going Out of Action this roll
  buffer3/2/1 - bargain while the villain is more than b boxes from winning
  greedy    - bargain whenever it won't lose THIS roll
"""
import random

P_STAT = 0.55
Q_ASSET = 0.469          # per-asset apply prob; 3 working -> 1-(1-q)^3 = 0.85
START_ASSETS = 3
READ_MAX = 9
REST_TRIGGER = 3         # voluntary free recovery at a boundary if min readiness <= this
DIFF = [(2, 0.4), (3, 0.4), (4, 0.2)]   # Option B fixed-difficulty challenge sizes
REG_PER_MS = 2           # connective regular rolls per milestone (exposure, no progress)
OOA_TICK = False         # if True, a hero hitting Out of Action also advances the villain +1

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
    # Oracle's Blessing: doubles on a hit upgrades a tier
    if doubles and tier == 'W': tier = 'S'
    elif doubles and tier == 'S': tier = 'S'   # already top
    return tier

def will_bargain(strategy, v, L, readiness, dmg):
    # never push to a guaranteed loss this roll
    if v + 1 >= L:
        return False
    if strategy == 'never': return False
    if strategy == 'need':  return (readiness - dmg) <= 0
    if strategy == 'greedy': return True
    if strategy.startswith('buffer'):
        b = int(strategy[6:])
        return v < (L - b)
    return False

def simulate(M, L, P, strategy):
    # heroes: readiness + working assets
    read = [READ_MAX] * P
    work = [START_ASSETS] * P
    out = [False] * P
    state = {'v': 0, 'turn': 0, 'lost': False}   # villain track / popcorn / loss flag

    def free_recovery():
        for i in range(P):
            read[i] = READ_MAX
            out[i] = False

    def next_hero():
        for _ in range(P):
            i = state['turn'] % P
            state['turn'] += 1
            if not out[i]:
                return i
        return None

    def tick(n=1):
        state['v'] += n
        if state['v'] >= L:
            state['lost'] = True

    def damage(i, dmg):
        # apply dmg to hero i; on Out of Action, break an asset (+ optional villain tick)
        read[i] -= dmg
        if read[i] <= 0:
            read[i] = 0; out[i] = True
            work[i] = max(0, work[i] - 1)
            if OOA_TICK:
                tick(1)

    for ms in range(M):
        # ---- the milestone's challenge ----
        boxes_needed = pick_diff()
        filled = 0
        retries = 0
        while filled < boxes_needed and not state['lost']:
            i = next_hero()
            if i is None:
                free_recovery(); filled = 0; retries += 1
                if retries > 6:
                    break
                continue
            a, b, dbl = roll()
            tier = outcome(a, b, hero_mod(work[i]), dbl)
            if tier in ('S', 'W'):
                filled += 1
                if tier == 'W':
                    damage(i, 1)
            else:  # MISS
                if dbl:
                    tick(1)                              # random tick (fate)
                if state['lost']: break
                if will_bargain(strategy, state['v'], L, read[i], 2):
                    tick(1)                              # bargain tick
                    if state['lost']: break
                    filled += 1                          # upgraded to Strong: fills a box
                else:
                    damage(i, 2)
        if state['lost']:
            return ('loss', state['v'])
        if min(read) <= REST_TRIGGER:
            free_recovery()

        # ---- connective regular rolls (exposure, no hero progress) ----
        for _ in range(REG_PER_MS):
            if state['lost']: break
            i = next_hero()
            if i is None:
                free_recovery(); i = next_hero()
            a, b, dbl = roll()
            tier = outcome(a, b, hero_mod(work[i]), dbl)
            if tier == 'M':
                if dbl:
                    tick(1)
                if state['lost']: break
                if will_bargain(strategy, state['v'], L, read[i], 2):
                    tick(1)                              # damage avoided, no box
                else:
                    damage(i, 2)
        if state['lost']:
            return ('loss', state['v'])
        if min(read) <= REST_TRIGGER:
            free_recovery()

    return ('win', state['v'])

def run(M, L, P, strategy, trials=60000):
    losses = 0; end_sum = 0; nearmiss = 0; bargmiss_total = 0
    for _ in range(trials):
        res, v = simulate(M, L, P, strategy)
        end_sum += v
        if res == 'loss':
            losses += 1
        elif v == L - 1:
            nearmiss += 1
    return losses / trials, end_sum / trials, nearmiss / trials

def block(title, M, Ls, P):
    print(f"\n===== {title}  (party {P}, {M} milestones) =====")
    str3 = ['never', 'need', 'buffer3', 'buffer2', 'greedy']
    for L in Ls:
        print(f"\n  Track L={L} (narrated beats ~ L/2 = {L/2:.0f} on shaded boxes):")
        print(f"    {'strategy':9} | {'loss%':>6} | {'endbox':>6} | {'nearmiss%':>9}")
        for s in str3:
            loss, endb, nm = run(M, L, P, s)
            print(f"    {s:9} | {loss*100:6.2f} | {endb:6.2f} | {nm*100:9.2f}")

def compare(title, M, L, P):
    global OOA_TICK
    print(f"\n===== {title}  (party {P}, {M} milestones, track L={L}) =====")
    print(f"    {'strategy':9} | {'loss OFF':>8} {'near OFF':>8} | {'loss ON':>8} {'near ON':>8}")
    for s in ['never', 'need', 'buffer3', 'buffer2', 'greedy']:
        OOA_TICK = False
        loff, _, noff = run(M, L, P, s)
        OOA_TICK = True
        lon, _, non = run(M, L, P, s)
        print(f"    {s:9} | {loff*100:7.2f}% {noff*100:7.2f}% | {lon*100:7.2f}% {non*100:7.2f}%")
    OOA_TICK = False

if __name__ == '__main__':
    random.seed(12345)
    print("Comparison: villain ticks from bargain+matches ONLY (OFF) vs +Out-of-Action (ON)")
    compare("EPISODE", 3, 6, P=2)
    compare("EPISODE", 3, 6, P=4)
    compare("MOVIE",   6, 10, P=2)
    compare("MOVIE",   6, 10, P=4)
    # does adding the OoA floor let us shorten the track?
    compare("EPISODE short", 3, 5, P=2)
    compare("MOVIE short",   6, 8, P=2)
