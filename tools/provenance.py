"""Source-provenance table for README: classifies every sourced variable in params.yaml as
literature-sourced, user-supplied or ASSUMED, from its `source` text (or an explicit `provenance:` key)."""
import re

def cell(x): return str(x).replace("|", "/").replace("\n", " ")

def walk(node, path=()):
    """Yield (path, spec) for every dict that carries a `source` (a sampled variable or a sourced constant)."""
    if isinstance(node, dict):
        if "source" in node and ("dist" in node or "earth_gya" in node or "value" in node):
            yield path, node
            return
        for k, v in node.items():
            yield from walk(v, path + (str(k),))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            nm = v.get("name", str(i)) if isinstance(v, dict) else str(i)
            yield from walk(v, path + (nm,))

def classify(spec):
    if spec.get("provenance"): return spec["provenance"]
    s = str(spec.get("source", ""))
    s = re.sub(r"was ASSUMED[^;)]*|ASSUMED\s*->", "", s)   # history notes ("was ASSUMED ...") do not count
    head = s.lstrip()[:60].upper()
    if head.startswith("USER") or "USER-SUPPLIED" in s.upper() or "USER INPUT" in s.upper():
        return "user-supplied"
    if head.startswith("ASSUMED"):
        return "ASSUMED"
    if "ASSUMED" in s:
        return "literature + ASSUMED element"
    return "literature-sourced"

def name(path):
    p = [x for x in path if x not in ("params", "classes", "penalty_params", "extra_params", "overrides", "hazard_params", "advance_params")]
    return ".".join(p)

def rows(cfg, skip_scenario_dupes=True):
    out, seen = [], set()
    for path, spec in walk(cfg):
        if path and path[0] == "scenarios" and skip_scenario_dupes:
            key = (path[-1], str(spec.get("source")))
            if key in seen: continue
        seen.add((path[-1], str(spec.get("source"))))
        out.append((name(path), classify(spec), spec))
    g = cfg.get("geometry", {})
    if "disk_volume_ly3" in g:   # plain constant (comment-sourced in params.yaml)
        out.append(("geometry.disk_volume_ly3", "user-supplied", {"source": f"USER-SUPPLIED ~{float(g['disk_volume_ly3']):.2g} ly^3 (cylinder r = {g.get('disk_radius_ly')} ly, thickness {g.get('disk_thickness_ly')} ly); used only for spacing", "url": ""}))
    return out

def section(cfg, level="##"):
    R = rows(cfg)
    counts = {}
    for _, c, _ in R: counts[c] = counts.get(c, 0) + 1
    order = ["literature-sourced", "literature + ASSUMED element", "user-supplied", "ASSUMED"]
    L = [f"{level} Source provenance\n",
         "Every sourced variable in [`params.yaml`](params.yaml), classified from its `source` field: "
         "**literature-sourced** (value or range taken or derived from cited published data), "
         "**literature + ASSUMED element** (cited data, but the mapping onto the model variable or part of the range is a judgement), "
         "**user-supplied** (Nathan's own inputs) and **ASSUMED** (no usable quantitative literature value; the reason is in the source text). "
         "Counts: " + ", ".join(f"{c} {counts.get(c, 0)}" for c in order) + ".\n",
         "<details><summary>Full provenance table (click to expand)</summary>\n",
         "| variable | provenance | first source / note | URL |", "|---|---|---|---|"]
    for c in order:
        for nm, cl, spec in R:
            if cl != c: continue
            src = cell(spec.get("source", ""))
            short = src if len(src) <= 160 else src[:157].rsplit(" ", 1)[0] + " …"
            url = cell(str(spec.get("url", "")).split(" ; ")[0])
            L.append(f"| `{nm}` | {cl} | {short} | {url} |")
    L.append("\n</details>\n")
    return "\n".join(L) + "\n"

if __name__ == "__main__":
    import yaml, sys
    cfg = yaml.safe_load(open(sys.argv[1] if len(sys.argv) > 1 else "params.yaml"))
    for nm, cl, spec in rows(cfg): print(f"{cl:30s} {nm:45s} {str(spec.get('source',''))[:70]}")
