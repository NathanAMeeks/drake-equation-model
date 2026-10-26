"""Add [MEASURED]/[MODELED]/[GUESS] tags to every sourced variable in params.yaml (mapped from the provenance class)."""
import os, re, sys, yaml
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(ROOT, "tools"))
import provenance as prov
# literature-sourced items that are direct observations / censuses / dated records -> MEASURED; other literature -> MODELED
MEASURED = {"sfr_now", "m_disk_now", "f_gk", "f_m", "fp", "ne_gk", "ne_m", "n_giant_hz_gk", "r_bigfive_per_gyr", "r_sn_per_gyr",
            "multipliers.f_co_ratio", "multipliers.f_binary_ok", "species.species_concurrent_per_tool_world",
            "species.species_cumulative_per_tool_world", "species.context_total_named_species"}
MEAS_PREFIX = ("hard_steps.",)
MEAS_SUFFIX = (".f_star", ".ne", ".n_giant_hz")
GUESS_LIT = ("classic_static.", "multiphase.stage_h_radio_per_yr")   # SDO 2018 Table-1 ranges = compiled literature opinions
def tag(name, cls):
    if cls in ("ASSUMED", "user-supplied"): return "GUESS"
    if name.startswith(GUESS_LIT) and cls == "literature-sourced": return "GUESS"
    if cls == "literature + ASSUMED element": return "MODELED"
    if name in MEASURED or name.startswith(MEAS_PREFIX) or (name.startswith("star_classes.") and name.endswith(MEAS_SUFFIX) and not name.endswith("F.n_giant_hz")):
        return "MEASURED"
    return "MODELED"
if __name__ == "__main__":
    p = os.path.join(ROOT, "params.yaml"); txt = open(p).read(); cfg = yaml.safe_load(txt)
    lines = txt.split("\n"); done = 0; tags = {}
    for name, cls, spec in prov.rows(cfg, skip_scenario_dupes=False):
        if name.startswith("geometry."): continue
        t = tag(name, cls); tags[name] = (t, cls)
        src = str(spec["source"])[:40]
        cands = [i for i, l in enumerate(lines) if "source:" in l and src in l and "tag:" not in l]
        if not cands: continue
        i = cands[0]; l = lines[i]
        before = "\n".join(lines[:i]) + "\n" + l[:l.index("source:")]
        inflow = before.count("{") > before.count("}")
        if inflow: lines[i] = l.replace("source:", f'tag: "[{t}]", source:', 1)
        else:
            ind = l[:len(l) - len(l.lstrip())]; lines.insert(i, f'{ind}tag: "[{t}]"')
        done += 1
    open(p, "w").write("\n".join(lines))
    cfg2 = yaml.safe_load(open(p)); miss = [n for n, c, s in prov.rows(cfg2, skip_scenario_dupes=False) if "tag" not in s and not n.startswith("geometry.")]
    from collections import Counter
    print("tagged", done, "missing", miss, Counter(v[0] for v in tags.values()))
