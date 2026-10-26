"""Paired comparison of v3 variants (A multiplicity cut, B multi-moon civs) vs parents (first 1e5 draws). -> rigor/v3.json"""
import json, numpy as np
def wq(x, w, qs):
    o = np.argsort(x); c = np.cumsum(w[o]); c /= c[-1]; return [float(x[o][np.searchsorted(c, q)]) for q in qs]
out = {}
for p in ["nathan_headline_ocean", "baseline_ocean"]:
    Z0 = np.load(f"results/samples_{p}.npz"); n = 100000
    rad0 = Z0["r_N_now_stage_radio"][:n] + Z0["r_N_now_stage_spacefaring"][:n]
    for v in ["", "_mult", "_moons", "_ab"]:
        Z = np.load(f"results/samples_{p}{v}.npz") if v else None
        N = Z["r_N_now"] if v else Z0["r_N_now"][:n]; lw = (Z if v else Z0)["r_logw"][:n]
        if v: assert np.array_equal(Z["p_sfr_now"], Z0["p_sfr_now"][:n]) and np.array_equal(Z["p_tau_" + "stone_tool_intelligence"] if "p_tau_stone_tool_intelligence" in Z.files else Z["p_sfr_now"], Z0["p_tau_stone_tool_intelligence"][:n] if "p_tau_stone_tool_intelligence" in Z.files else Z0["p_sfr_now"][:n])
        w = np.exp(lw - lw.max()) if p.startswith("baseline") else np.ones(n)
        rad = Z["r_N_radio_capable"] if v else rad0
        r = dict(p10_p50_p90=wq(N, w, [.1, .5, .9]), radio_median=wq(rad, w, [.5])[0])
        if v: r["paired_median_log10_ratio"] = wq(np.log10(np.maximum(N, 1e-300) / np.maximum(Z0["r_N_now"][:n], 1e-300)), w, [.5])[0]
        if v and "r_multi_civ_share" in Z.files:
            r["multi_civ_share_of_N"] = float((w * Z["r_N_now_multi_civ"]).sum() / (w * N).sum())
            r["multi_civ_share_median"] = wq(Z["r_multi_civ_share"], w, [.5])[0]
            r["N_civ_median"] = wq(Z["r_N_civ_now"], w, [.5])[0]
        out[p + (v or "_parent_1e5")] = r; print(p + v, {k: (f"{x:.3g}" if isinstance(x, float) else [f"{y:.3g}" for y in x]) for k, x in r.items()})
json.dump(out, open("rigor/v3.json", "w"), indent=1)
