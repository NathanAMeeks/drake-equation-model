"""Scrambled Sobol QMC + control variate vs plain MC for E[log10 N_now] (unweighted), and a pick-freeze run with
memoised unchanged stages (solve_k, stage_chain, step DFTs). Output rigor/qmc.json"""
import json, math, os, sys, time, hashlib, numpy as np, yaml
from scipy.stats import qmc, norm
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(H); sys.path.insert(0, R)
import drake_model as dm
cfg = yaml.safe_load(open(os.path.join(R, "params.yaml"))); NREP, LOGN = 16, 12
def qmc_draw(m, n, rng, U):
    P = m.draw(n, rng); specs = m.param_specs(); cv = np.zeros(n); mu = 0.0; j = 0
    for k, s in specs.items():
        s = dm._num(s); d = s["dist"]
        if d not in ("uniform", "loguniform", "normal", "one_plus_loguniform") or k in m.scn.get("extra_params", {}): continue
        u = U[:, j]; j += 1
        if d == "uniform": P[k] = s["low"] + u * (s["high"] - s["low"])
        elif d in ("loguniform", "one_plus_loguniform"):
            a, b = math.log10(s["low"]), math.log10(s["high"]); x = a + u * (b - a)
            P[k] = 10 ** x + (1.0 if d == "one_plus_loguniform" else 0.0)
            if d == "loguniform": cv += x; mu += 0.5 * (a + b)     # control variate: sum of log10 loguniform inputs, exact mean
        else:
            lo, hi = s.get("min", -np.inf), s.get("max", np.inf); F = lambda x: norm.cdf((x - s["mean"]) / s["sd"])
            P[k] = s["mean"] + s["sd"] * norm.ppf(F(lo) + u * (F(hi) - F(lo)))
    if m.scn.get("links"): m._apply_links(P)
    m._apply_tool_origins(P); return P, cv - mu, j
def est(m, n, seed, use_qmc, dim):
    rng = np.random.default_rng(seed)
    U = qmc.Sobol(dim, scramble=True, seed=seed).random(n) if use_qmc else rng.random((n, dim))
    P, cv, _ = qmc_draw(m, n, rng, U); y = np.log10(np.maximum(m.evaluate(P)[0]["N_now"], 1e-300))
    c = np.cov(y, cv); b = c[0, 1] / c[1, 1]
    return y.mean(), (y - b * cv).mean()
out = {}
for s in ["nathan_headline_ocean", "baseline_ocean"]:
    m = dm.Model(cfg, s); dim = qmc_draw(m, 4, np.random.default_rng(0), np.full((4, 400), .5))[2]
    r = {}; t0 = time.time()
    for name, q in (("mc", False), ("qmc", True)):
        e = np.array([est(m, 2 ** LOGN, 100 + i, q, dim) for i in range(NREP)]); r[name] = e
    v = {f"{a}{'_cv' if c else ''}": float(r[a][:, c].var(ddof=1)) for a in ("mc", "qmc") for c in (0, 1)}
    out[s] = dict(n_per_rep=2 ** LOGN, reps=NREP, dim=dim, var_of_mean=v,
                  var_reduction_vs_mc={k: v["mc"] / x for k, x in v.items()}, mean_log10N_qmc_cv=float(r["qmc"][:, 1].mean()), secs=round(time.time() - t0, 1))
    print(s, out[s], flush=True)
# pick-freeze cache: memoise stages keyed by the bytes of their inputs; A and AB_i share them unless factor i feeds them
cache, hits = {}, [0, 0]
def memo(f):
    def g(*a):
        key = (f.__name__, hashlib.blake2b(b"".join(np.ascontiguousarray(x).tobytes() for x in a if isinstance(x, np.ndarray)), digest_size=16).digest())
        hits[1] += 1
        if key in cache: hits[0] += 1; return cache[key]
        cache[key] = r = f(*a); return r
    g.__name__ = f.__name__; return g
m = dm.Model(cfg, "nathan_headline_ocean"); n = 2000
A = m.draw(n, np.random.default_rng(5)); B = m.draw(n, np.random.default_rng(6))
fac = ["l_stone_yr", "f_plate_tectonics", "m_recurrence", "f_land_and_ocean", "sfr_now"]
def pf():
    m.evaluate(A)
    for k in fac: m.evaluate({**A, k: B[k]})
t = time.time(); pf(); t_plain = time.time() - t
orig = (dm.solve_k, dm.Model.stage_chain, dm.dft_trunc_exp)
dm.solve_k = memo(orig[0]); sc = memo(lambda self, P, a: orig[1](self, P, a)); sc.__name__ = "sc"
dm.Model.stage_chain = lambda self, P, a: memo_sc(self, P, a)
memo_sc = memo(lambda self, P, a, _f=orig[1]: _f(self, P, a)); memo_sc.__name__ = "stage_chain"
def memo_sc_wrap(self, P, a):
    keyarrs = [a] + [P[k] for k in sorted(cfg["multiphase"]["params"]) if k in P]
    key = ("stage_chain", hashlib.blake2b(b"".join(np.ascontiguousarray(x).tobytes() for x in keyarrs), digest_size=16).digest()); hits[1] += 1
    if key in cache: hits[0] += 1; return cache[key]
    cache[key] = r = orig[1](self, P, a); return r
dm.Model.stage_chain = memo_sc_wrap; dm.dft_trunc_exp = memo(orig[2])
t = time.time(); pf(); t_cache = time.time() - t
o1 = m.evaluate({**A, "l_stone_yr": B["l_stone_yr"]})[0]["N_now"]
dm.solve_k, dm.Model.stage_chain, dm.dft_trunc_exp = orig
o0 = m.evaluate({**A, "l_stone_yr": B["l_stone_yr"]})[0]["N_now"]
out["pick_freeze_cache"] = dict(n=n, factors=fac, secs_plain=round(t_plain, 2), secs_cached=round(t_cache, 2), speedup=round(t_plain / t_cache, 2),
                                cache_hit_rate=round(hits[0] / hits[1], 3), identical_output=bool(np.array_equal(o0, o1)))
print(out["pick_freeze_cache"])
json.dump(out, open(os.path.join(H, "qmc.json"), "w"), indent=1)
