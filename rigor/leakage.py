"""Programmatic leakage checks: does any input derive from the quantity it predicts? Output: rigor/leakage.json"""
import json, os, re, sys, yaml
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
cfg = yaml.safe_load(open("params.yaml")); txt = open("params.yaml").read(); src = open("drake_model.py").read()
E = json.load(open("data/esi_hz.json"))
sc = cfg["scenarios"]; out = {}
out["earth_timeline"] = {s: dict(hard_step_tau=sc[s]["hard_step_tau"].get("dist"), bayes_update=sc[s].get("bayes_update", True) and cfg["run"]["bayes_update_on_earth_timing"])
                         for s in ("nathan_headline", "nathan_headline_ocean", "baseline", "baseline_ocean")}
out["selection_correction_in_code"] = "logL - np.log(np.where(Pc > 0, Pc, 1))" in src
solar = {"Earth", "Venus", "Mars", "Mercury", "Moon"}
out["esi_lists_contain_solar_system_bodies"] = any(n in solar for p in ("conservative", "optimistic") for n in E[p]["names"])
out["params_reference_model_outputs"] = bool(re.search(r"results/|results\.json|best_[a-z_]+\.json|samples_", txt))
out["seti_results_used_as_inputs"] = "scan_log" in txt or "queue.json" in txt
nto = cfg["scenarios"]["nathan_headline"]["extra_params"]["n_tool_origins"]["source"]
out["n_tool_origins_includes_hominins"] = "hominins" in nto
json.dump(out, open("rigor/leakage.json", "w"), indent=1); print(json.dumps(out, indent=1))
