"""Branch-and-bound tightening of the guaranteed bounds + binding factors per tail. Output rigor/bounds_v2.json"""
import json, math, os, sys, time, yaml
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H); sys.path.insert(0, os.path.dirname(H))
import engine as E, drake_model as dm
cfg = yaml.safe_load(open(os.path.join(os.path.dirname(H), "params.yaml")))
def split(box, k, logsp):
    a, b = box[k]; mid = math.sqrt(a * b) if logsp and a > 0 else 0.5 * (a + b)
    return {**box, k: (a, mid)}, {**box, k: (mid, b)}
def bnb(m, box, tail, steps=60):
    """tail 'lo': guaranteed min = min over leaves of leaf lower bounds; 'hi': max over leaves of leaf upper bounds."""
    idx = 0 if tail == "lo" else 1; worse = min if tail == "lo" else max
    cand = [k for k, (a, b) in box.items() if b > a]
    leaves = [(E.bound(m, box, cfg)[idx], box)]
    for _ in range(steps):
        leaves.sort(key=lambda x: x[0], reverse=(tail == "hi")); v0, bx = leaves.pop(0)
        best = None
        for k in cand:
            a, b = bx[k]
            if b <= a * (1 + 1e-9): continue
            c1, c2 = split(bx, k, a > 0 and b / a > 10)
            v1, v2 = E.bound(m, c1, cfg)[idx], E.bound(m, c2, cfg)[idx]
            score = worse(v1, v2)
            if best is None or (score > best[0] if tail == "lo" else score < best[0]): best = (score, (v1, c1), (v2, c2))
        if best is None or best[0] == v0: leaves.append((v0, bx)); break
        leaves += [best[1], best[2]]
    return worse(v for v, _ in leaves), len(leaves)
def binding(m, box, tail):
    """Tightening of the tail bound when one factor is restricted to the half away from its worst end."""
    idx = 0 if tail == "lo" else 1; base = E.bound(m, box, cfg)[idx]; out = []
    for k, (a, b) in box.items():
        if b <= a: continue
        c1, c2 = split(box, k, a > 0 and b / a > 10)
        v1, v2 = E.bound(m, c1, cfg)[idx], E.bound(m, c2, cfg)[idx]
        if tail == "lo": worst, other, end = (v1, v2, "low end") if v1 <= v2 else (v2, v1, "high end"); gain = math.log10(other / base) if base > 0 else 0
        else: worst, other, end = (v1, v2, "low end") if v1 >= v2 else (v2, v1, "high end"); gain = math.log10(base / other)
        out.append((k, end, round(gain, 2)))
    return sorted(out, key=lambda x: -x[2])[:5]
if __name__ == "__main__":
    old = json.load(open(os.path.join(H, "bounds.json")))["scenarios"]; res = {}
    for s in ["nathan_headline_ocean", "baseline_ocean", "nathan_headline", "baseline"]:
        m = dm.Model(cfg, s); box = E.full_box(m); t = time.time()
        v2 = E.bound(m, box, cfg); blo, nlo = bnb(m, box, "lo"); bhi, nhi = bnb(m, box, "hi")
        res[s] = dict(old=[old[s]["N_now_lower"], old[s]["N_now_upper"]], engine_v2=list(v2), bnb=[blo, bhi], leaves=[nlo, nhi],
                      width_dex_old=math.log10(old[s]["N_now_upper"] / old[s]["N_now_lower"]), width_dex_new=math.log10(bhi / blo),
                      binding_low_tail=binding(m, box, "lo"), binding_high_tail=binding(m, box, "hi"), secs=round(time.time() - t, 1))
        print(s, res[s]["old"], v2, [blo, bhi], res[s]["binding_low_tail"][:3], res[s]["binding_high_tail"][:3], res[s]["secs"])
    json.dump(res, open(os.path.join(H, "bounds_v2.json"), "w"), indent=1)
