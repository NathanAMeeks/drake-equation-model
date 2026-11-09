#!/usr/bin/env python3
"""
Extended, time-aware Drake model for worlds hosting "stone-age-or-greater" tool users.

All inputs live in params.yaml (single config).  Usage:
    python drake_model.py [--config params.yaml] [--n 1000000] [--out results]

Model outline (per Monte-Carlo sample = one possible "state of the world"):
  1. Galactic disk star-formation history SFR(t): thick-disk phase (constant) then an
     exponential thin-disk phase normalised to today's SFR and today's disk mass.
  2. Planet production per time bin for G/K and M hosts:
        SFR(t) * stars/Msun * f_class * ne_class * f_GHZ * f_metal(t) * prod(multipliers) [* f_M_hab]
  3. Biology: a chain of hard steps (Carter/Hanson/Watson/Snyder-Beattie), each an exponential
     waiting time with expected time tau_k.  Delay-to-tool-users distribution g(d) = convolution.
     Optionally the sample is weighted by the likelihood of Earth's observed transition dates,
     conditioned on Earth having completed all steps by now (observer selection), i.e. the
     Snyder-Beattie et al. 2021 Bayesian update.
  4. A tool-using phase lasts Exp(mean L_eff), L_eff = 1/(1/L + r_kill); after it ends the
     planet can re-evolve tool users at rate 1/(m_rec*tau_last) (alternating renewal).
  5. Planet must be younger than its habitable window; whole-biosphere sterilisation hazard
     r_ster(t) = r_ster0 * SFR(t)/SFR_now removes planets.
  6. N(t) = number of worlds with tool users alive at time t; N_now = N(13.8 Gyr).
"""
import argparse, json, math, os, copy, time
import numpy as np
import yaml

# ------------------------------------------------------------------ sampling helpers
def _num(spec):
    out = {}
    for k, v in spec.items():
        if isinstance(v, str):
            try: v = float(v)
            except ValueError: pass
        out[k] = v
    return out

def sample(spec, n, rng):
    spec = _num(spec)
    d = spec["dist"]
    if d == "fixed":
        rng.random(n)  # consume the stream so scenarios with fixed overrides stay paired
        return np.full(n, float(spec["value"]))
    if d == "uniform":
        return rng.uniform(spec["low"], spec["high"], n)
    if d == "loguniform":
        return 10 ** rng.uniform(math.log10(spec["low"]), math.log10(spec["high"]), n)
    if d == "normal":
        x = rng.normal(spec["mean"], spec["sd"], n)
        lo, hi = spec.get("min", -np.inf), spec.get("max", np.inf)
        bad = (x < lo) | (x > hi)
        while bad.any():
            x[bad] = rng.normal(spec["mean"], spec["sd"], bad.sum())
            bad = (x < lo) | (x > hi)
        return x
    if d == "lognormal10":
        return 10 ** rng.normal(spec["mu"], spec["sigma"], n)
    if d == "one_plus_loguniform":
        return 1.0 + 10 ** rng.uniform(math.log10(spec["low"]), math.log10(spec["high"]), n)
    if d == "inv_exp":   # tau = scale / E, E ~ Exp(1): Earth's interval is a uniform-quantile draw of Exp(mean tau)
        return spec["scale"] / rng.exponential(1.0, n)
    raise ValueError(f"unknown dist {d}")

def best(spec):
    spec = _num(spec)
    if "best" in spec:
        return float(spec["best"])
    d = spec["dist"]
    if d == "fixed": return float(spec["value"])
    if d == "uniform": return 0.5 * (spec["low"] + spec["high"])
    if d == "loguniform": return math.sqrt(spec["low"] * spec["high"])
    if d == "normal": return float(spec["mean"])
    if d == "lognormal10": return 10 ** spec["mu"]
    if d == "one_plus_loguniform": return 1.0 + math.sqrt(spec["low"] * spec["high"])
    if d == "inv_exp": return spec["scale"] / math.log(2.0)   # median
    raise ValueError(d)

def wquantile(x, w, q):
    o = np.argsort(x); x, w = x[o], w[o]
    c = np.cumsum(w); c = c / c[-1]
    return np.interp(q, c, x)

# ------------------------------------------------------------------ DFT helpers
def dft_trunc_exp(x, J, omega_log):
    """DFT of binned exponential p_j=(1-q)q^j, j<J, q=exp(-x).  x shape (n,1); omega_log = -2*pi*i*k/M."""
    one_minus_q = -np.expm1(-x)                         # (n,1)
    z = -x + omega_log                                  # log(q*omega)
    return one_minus_q * (-np.expm1(J * z)) / (-np.expm1(z))

def dft_trunc_const(J, omega_log):
    out = np.empty(omega_log.shape[-1], dtype=complex)
    out[0] = J
    out[1:] = (-np.expm1(J * omega_log[0, 1:])) / (-np.expm1(omega_log[0, 1:]))
    return out[None, :]

def solve_k(target, D, iters=80):
    """Solve (exp(kD)-1)/k = target for k (vectorised bisection); k=1/tau of thin-disk exponential."""
    lo = np.full_like(target, -20.0); hi = np.full_like(target, 20.0)
    f = lambda k: np.where(np.abs(k) < 1e-9, D, np.expm1(k * D) / np.where(np.abs(k) < 1e-9, 1, k))
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        big = f(mid) > target
        hi = np.where(big, mid, hi); lo = np.where(big, lo, mid)
    return 0.5 * (lo + hi)

# ------------------------------------------------------------------ core model
class Model:
    def __init__(self, cfg, scenario):
        self.cfg = cfg
        run = cfg["run"]
        self.dt = run["dt_gyr"]; self.T = run["t_now_gyr"]
        self.I = int(round(self.T / self.dt))
        self.t = (np.arange(self.I) + 0.5) * self.dt          # bin centres, Gyr after BB
        self.M = 1 << int(math.ceil(math.log2(self.I * 6)))   # DFT length (no wrap for <=5 steps)
        k = np.arange(self.M // 2 + 1)
        self.omega_log = (-2j * np.pi * k / self.M)[None, :]
        self.Mc = 1 << int(math.ceil(math.log2(self.I * 2)))  # for galactic convolution
        self.steps = cfg["hard_steps"]
        self.scn = cfg["scenarios"][scenario]
        self.scenario = scenario
        ts = run["earth_habitable_start_gya"]
        dates = [ts] + [s["earth_gya"] for s in self.steps]
        self.earth_dt = np.array([dates[i] - dates[i + 1] for i in range(len(self.steps))])
        self.earth_T = ts - 0.0                                # completed by now
        self.iE = int(round(self.earth_T / self.dt))
        # v2 options (per scenario): multi-spectral host classes (M/K/G/F) and multiphase civilisation stages
        self.ms = bool(self.scn.get("multispectral", False)) and "star_classes" in cfg
        self.classes = list(cfg["star_classes"]["classes"].keys()) if self.ms else []
        self.mp = bool(self.scn.get("multiphase", False)) and "multiphase" in cfg
        self.stages = cfg["multiphase"]["stages"] if self.mp else []

    def _targets(self, s):
        """Host classes a multiplier applies to. Legacy tags: gk -> K,G,F ; m -> M."""
        tags = s.get("applies_to", ["gk", "m"])
        if not self.ms: return [t for t in tags if t in ("gk", "m")]
        out = []
        for t in tags:
            out += {"gk": ["K", "G", "F"], "m": ["M"]}.get(t, [t])
        return [c for c in out if c in self.classes]

    def active_multipliers(self):
        return {k: v for k, v in self.cfg.get("multipliers", {}).items()
                if (("scenarios" not in v) or (self.scenario in v["scenarios"]))
                and (self.ms or not v.get("multispectral_only", False))}

    def param_specs(self):
        specs = dict(self.cfg["params"])
        if self.ms:   # replace the 2-class (G/K, M) parameters by per-class ones
            sc = self.cfg["star_classes"]
            for k in sc["replaces_params"]: specs.pop(k, None)
            for c, d in sc["classes"].items():
                for fld, nm in (("f_star", f"f_star_{c}"), ("ne", f"ne_{c}"), ("th_gyr", f"th_{c}_gyr"), ("n_giant_hz", f"n_giant_hz_{c}")):
                    specs[nm] = d[fld]
        for name, s in self.active_multipliers().items():
            specs[name] = s
        hst = self.scn["hard_step_tau"]
        for i, s in enumerate(self.steps):
            if hst.get("dist") == "earth_interval":        # tau fixed at Earth's observed interval
                spec = {"dist": "fixed", "value": float(self.earth_dt[i])}
            elif hst.get("dist") == "earth_random_draw":   # Earth's interval = one random draw (uniform quantile)
                spec = {"dist": "inv_exp", "scale": float(self.earth_dt[i])}
            else:
                spec = hst
            specs["tau_" + s["name"]] = s.get("tau_gyr", spec)
        if self.mp:
            for name, s in self.cfg["multiphase"]["params"].items():
                specs[name] = s
        for name, s in self.scn.get("overrides", {}).items():
            specs[name] = {**specs.get(name, {}), **s}
        for name, s in self.scn.get("extra_params", {}).items():   # scenario-only parameters (drawn last => pairing kept)
            specs[name] = s
        return specs

    def draw(self, n, rng):
        extra = self.scn.get("extra_params", {})
        P = {k: sample(v, n, rng) for k, v in self.param_specs().items() if k not in extra}
        sim = self.scn.get("similarity")
        if sim:   # per-sample bootstrap mean of ESI^k over the Archive HZ-rocky population (aux_* = other variants)
            E = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), sim["esi_file"])))
            for pop in ("conservative", "optimistic"):
                e = np.array(E[pop]["esi4"]); idx = rng.integers(0, len(e), size=(n, len(e)))
                for k in sim["exponents"]:
                    P[f"aux_w_{pop}_k{k}"] = (e[idx] ** float(k)).mean(1)
            P["w_similarity"] = P[f"aux_w_{sim['population']}_k{sim['headline_exponent']}"].copy()
            if self.ms:   # per host type: bootstrap that type's own ESI list if it has >= min_n planets, else the pooled weight
                kx = float(sim["headline_exponent"]); bt = E[sim["population"]]["by_type"]
                for c in self.classes:
                    e = np.array(bt.get(c, {}).get("esi4", []))
                    if len(e) >= int(sim.get("min_n_by_type", 3)):
                        idx = rng.integers(0, len(e), size=(n, len(e))); P[f"w_similarity_{c}"] = (e[idx] ** kx).mean(1)
                    else:
                        P[f"w_similarity_{c}"] = P["w_similarity"].copy()
        for k, v in extra.items():
            P[k] = sample(v, n, rng)
        self._apply_tool_origins(P)
        return P

    def _apply_tool_origins(self, P):
        """Cross-lineage tool use: last step's expected time = Earth's multicellularity->tools interval / n independent origins."""
        if "n_tool_origins" in P:
            P["tau_" + self.steps[-1]["name"]] = self.earth_dt[-1] / P["n_tool_origins"]

    def best_point(self):
        P = {k: np.array([best(v)]) for k, v in self.param_specs().items()}
        sim = self.scn.get("similarity")
        if sim:
            E = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), sim["esi_file"])))
            P["w_similarity"] = np.array([E[sim["population"]]["mean_pow"][str(sim["headline_exponent"])]])
            if self.ms:
                bt = E[sim["population"]]["by_type"]
                for c in self.classes:
                    d = bt.get(c, {})
                    P[f"w_similarity_{c}"] = (np.array([d["mean_pow"][str(sim["headline_exponent"])]]) if d.get("n", 0) >= int(sim.get("min_n_by_type", 3)) else P["w_similarity"].copy())
        ov = self.scn.get("overrides", {})
        for i, s in enumerate(self.steps):                    # Copernican point: tau = Earth's interval
            k = "tau_" + s["name"]
            P[k] = np.array([float(ov[k]["best"]) if (k in ov and "best" in ov[k]) else self.earth_dt[i]])
        self._apply_tool_origins(P)
        return P

    def evaluate(self, P):
        n = len(next(iter(P.values())))
        dt, I, T, t = self.dt, self.I, self.T, self.t
        col = lambda a: np.asarray(a, float)[:, None]
        # ---- 1. star formation history (Msun/yr)
        Mform = P["m_disk_now"] / (1 - P["return_fraction"])
        ts_, tq = P["disk_start_gyr"], P["thick_end_gyr"]
        S_thick = P["f_early_disk_mass"] * Mform / ((tq - ts_) * 1e9)
        D = T - tq
        target = (1 - P["f_early_disk_mass"]) * Mform / (P["sfr_now"] * 1e9)   # Gyr
        kk = solve_k(target, D)
        sfr = np.where(t[None, :] < col(ts_), 0.0,
              np.where(t[None, :] < col(tq), col(S_thick),
                       col(P["sfr_now"]) * np.exp(col(kk) * (T - t[None, :]))))
        # ---- 2. habitable-planet production per bin, per host class
        fZ = 1.0 / (1.0 + np.exp(-(t[None, :] - col(P["t_metal_gyr"])) / 0.5))
        cls = self.classes if self.ms else ["gk", "m"]
        mult = {c: np.ones(n) for c in cls}; multm = {c: np.ones(n) for c in cls}
        for name, s in self.active_multipliers().items():
            for c in self._targets(s):
                mult[c] = mult[c] * P[name]
                if s.get("applies_to_exomoons", True):
                    multm[c] = multm[c] * P[name]
        # similarity weight applies to every habitable body (planets and moons); per class if available
        if "w_similarity" in P:
            for c in cls:
                wc = P.get(f"w_similarity_{c}", P["w_similarity"])
                mult[c] = mult[c] * wc; multm[c] = multm[c] * wc
        if "f_superhab" in P:     # superhabitable fraction: step-success probability x boost (capped at 1); planets only, not moons
            f = P["f_superhab"]
            for c in (self.cfg["star_classes"].get("superhab_classes", ["K"]) if self.ms else ["gk"]):
                mult[c] = (1 - f) * mult[c] + f * np.minimum(mult[c] * P["superhab_boost"], 1.0)
        moon = P.get("f_exomoon_host", np.zeros(n)) * P.get("f_exomoon_habitable", np.ones(n))
        base = sfr * 1e9 * dt * col(P["stars_per_msun"] * P["fp"] * P["f_ghz"]) * fZ
        pl, th, moon_share = {}, {}, {}
        for c in cls:
            if self.ms:
                d = self.cfg["star_classes"]["classes"][c]
                fs, ne, ng, thc = P[f"f_star_{c}"], P[f"ne_{c}"], P[f"n_giant_hz_{c}"], P[f"th_{c}_gyr"]
                pen = np.ones(n)
                for pp in d.get("penalty_params", []): pen = pen * P[pp]
            else:
                fs, ne, ng, thc = P[f"f_{c}"], P[f"ne_{c}"], P.get(f"n_giant_hz_{c}", np.zeros(n)), P[f"th_{c}_gyr"]
                pen = P["f_m_habitable"] if c == "m" else np.ones(n)
            ne_eff = ne * mult[c] + ng * moon * multm[c]
            moon_share[c] = np.where(ne_eff > 0, ng * moon * multm[c] / np.where(ne_eff > 0, ne_eff, 1), 0.0)
            pl[c] = base * col(fs * ne_eff * pen); th[c] = thc
        # ---- 3. hard-step delay distribution g(d) via analytic DFTs
        G = np.ones((n, self.M // 2 + 1), dtype=complex)
        taus = np.stack([P["tau_" + s["name"]] for s in self.steps], axis=1)
        for j in range(taus.shape[1]):
            G *= dft_trunc_exp(col(dt / taus[:, j]), I, self.omega_log)
        g = np.fft.irfft(G, n=self.M)[:, :I]
        g = np.clip(g, 0, None)
        # Earth-timing likelihood weight (Snyder-Beattie+2021 style)
        if self.cfg["run"].get("bayes_update_on_earth_timing", True) and self.scn.get("bayes_update", True):
            Pc = g[:, :self.iE].sum(1)
            logL = (-np.log(taus) - self.earth_dt[None, :] / taus).sum(1)
            with np.errstate(divide="ignore"):
                logw = np.where(Pc > 0, logL - np.log(np.where(Pc > 0, Pc, 1)), -np.inf)
        else:
            logw = np.zeros(n)
        # ---- 4. occupancy kernel: alternating renewal (on: L_eff, off: tau_rec)
        Lgyr = P["l_stone_yr"] / 1e9
        r_kill = (P["r_bigfive_per_gyr"] * P["p_bigfive_kills_toolusers"]
                  + P["p_lethal_astro"] * (P["r_grb_per_gyr"] + P["r_sn_per_gyr"]) + P["r_self_per_gyr"])
        alpha = 1.0 / Lgyr + r_kill
        stage_out = {}
        if self.mp:   # multiphase: stage chain inside each tool-using episode; episode mean length replaces 1/alpha
            alpha, phi = self.stage_chain(P, alpha)
            for k, nm in enumerate(self.stages): stage_out[nm] = phi[:, k]
        beta = 1.0 / (P["m_recurrence"] * taus[:, -1])
        pi_on = beta / (alpha + beta); Lp = 1.0 / (alpha + beta)
        c_ = (Lp / dt) * (-np.expm1(-dt / Lp))
        Khat = col(pi_on) * dft_trunc_const(I, self.omega_log) + \
               col((1 - pi_on) * c_ / (-np.expm1(-dt / Lp))) * dft_trunc_exp(col(dt / Lp), I, self.omega_log)
        Q = np.clip(np.fft.irfft(G * Khat, n=self.M)[:, :I], 0, None)   # expected occupied worlds per planet vs age
        cdf_g = np.cumsum(g, 1)
        # ---- 5. windows, sterilisation, galactic convolution
        age = (np.arange(I) + 0.5) * dt
        rster = col(P["r_ster0_per_gyr"]) * sfr / col(P["sfr_now"])
        H = np.cumsum(rster * dt, 1)
        eH = np.exp(H)
        Mc = self.Mc
        F = lambda x: np.fft.rfft(x, n=Mc)
        surv = np.exp(-(H[:, -1:] - H))[:, ::-1]           # indexed by age
        Fsum = 0; Nnow_c, Never_c = {}, {}
        for c in cls:
            Fc = F(pl[c] * eH) * F(Q * (age[None, :] < col(th[c])))
            Fsum = Fsum + Fc
            Nnow_c[c] = np.clip(np.fft.irfft(Fc, n=Mc)[:, I - 1], 0, None) * np.exp(-H[:, -1])
            # worlds that EVER produced tool users by now (archaeological form, Frank & Sullivan 2016)
            cg = np.where(age[None, :] < col(th[c]), cdf_g,
                          np.take_along_axis(cdf_g, np.minimum((col(th[c]) / dt).astype(int), I - 1), 1))
            Never_c[c] = (pl[c][:, ::-1] * cg * surv).sum(1)
        Nt = np.clip(np.fft.irfft(Fsum, n=Mc)[:, :I], 0, None) * np.exp(-H)
        N_now = Nt[:, -1].copy()
        N_ever = sum(Never_c.values())
        th0 = th[cls[0]] if not self.ms else th["G"]
        out = dict(N_now=N_now, N_timeavg=Nt.mean(1), N_peak=Nt.max(1),
                   t_peak=t[np.argmax(Nt, 1)], N_ever=N_ever, logw=logw,
                   N_now_gk=None, n_hab_total=sum(p.sum(1) for p in pl.values()),
                   p_tool_gk_window=np.take_along_axis(cdf_g, np.minimum((col(th0) / dt).astype(int), I - 1), 1)[:, 0])
        tot = sum(Nnow_c.values())
        sun_like = [c for c in cls if c != "m" and c != "M"]
        out["frac_gk"] = np.where(tot > 0, sum(Nnow_c[c] for c in sun_like) / np.where(tot > 0, tot, 1), np.nan)
        out["exomoon_share_gk"] = moon_share["gk"] if not self.ms else moon_share["K"]
        if self.ms:
            for c in cls:
                out[f"N_now_{c}"] = Nnow_c[c]; out[f"N_ever_{c}"] = Never_c[c]; out[f"exomoon_share_{c}"] = moon_share[c]
                out[f"n_hab_{c}"] = pl[c].sum(1)
        if self.mp:
            out["L_episode_yr"] = 1e9 / alpha
            for nm, ph in stage_out.items():
                out[f"phi_{nm}"] = ph; out[f"N_now_stage_{nm}"] = N_now * ph
        # mean planet age-at-formation of habitable planets (sanity vs Lineweaver 2001)
        w_age = sum(pl.values())
        out["mean_planet_age"] = (w_age * (T - t)[None, :]).sum(1) / w_age.sum(1)
        return out, Nt

    def stage_chain(self, P, alpha):
        """Multiphase civilisation stages inside one tool-using episode (continuous-time Markov chain).
        States 1..S (lithic, agricultural, industrial, radio, spacefaring). From stage s:
          advance s->s+1 at rate 1/tau_s ; stage-specific collapse at rate h_s, of which a fraction q regresses to s-1
          (recurrence: it can re-advance later) and 1-q ends the episode (lineage lost); plus the baseline
          end-of-lineage rate alpha (L_stone, Big-Five, GRB/SN, r_self) in every stage.
        Every episode starts in stage 1. Expected time in each stage per episode T = e1^T (-Q_on)^-1, so
        phi_s = T_s / sum(T) is the long-run share of tool-using time spent in stage s (exact for the
        alternating renewal; stage relaxation assumed fast compared with Gyr galactic time), and the mean episode
        length sum(T) replaces 1/alpha in the on/off kernel."""
        mpc = self.cfg["multiphase"]; S = len(self.stages); n = len(alpha)
        a = [1e9 / P[k] for k in mpc["advance_params"]]                # per Gyr, s -> s+1 (S-1 entries)
        h = [np.zeros(n)] + [1e9 * P[k] for k in mpc["hazard_params"]]   # per Gyr, stage 1 has no extra hazard
        q = P[mpc["regress_fraction_param"]]
        Qm = np.zeros((n, S, S))
        for s_ in range(S):
            out_rate = alpha + h[s_]
            if s_ < S - 1:
                Qm[:, s_, s_ + 1] = a[s_]; out_rate = out_rate + a[s_]
            if s_ > 0:
                Qm[:, s_, s_ - 1] = q * h[s_]
            Qm[:, s_, s_] = -out_rate
        e1 = np.zeros((n, S)); e1[:, 0] = 1.0
        Tst = np.linalg.solve(np.transpose(-Qm, (0, 2, 1)), e1[..., None])[..., 0]   # row 1 of (-Q)^-1
        Tst = np.clip(Tst, 0, None)
        Ltot = Tst.sum(1)
        return 1.0 / Ltot, Tst / Ltot[:, None]

# ------------------------------------------------------------------ classic static (SDO-style)
def classic_static(cfg, rng):
    c = cfg["classic_static"]; n = int(c["n_samples"])
    s = {k: sample(v, n, rng) for k, v in c.items() if isinstance(v, dict)}
    lam = 10 ** np.clip(s["log10_lambdaVt"], -300, 300)
    fl = -np.expm1(-lam)
    N = s["R_star"] * s["fp"] * s["ne"] * fl * s["fi"] * s["f_stone"] * s["L_stone"]
    return N

# ------------------------------------------------------------------ driver
def run(cfg_path, n_override=None, outdir="results", scenarios=None, do_classic=True):
    cfg = yaml.safe_load(open(cfg_path))
    os.makedirs(outdir, exist_ok=True)
    runc = cfg["run"]; n = int(n_override or runc["n_samples"]); chunk = int(runc["chunk"])
    allres = {}
    for scen in (scenarios or runc["scenarios_to_run"]):
        m = Model(cfg, scen)
        rng = np.random.default_rng(runc["seed"])
        keys = list(m.param_specs().keys())
        if m.scn.get("similarity"):
            sim = m.scn["similarity"]
            keys += ["w_similarity"] + [f"aux_w_{p}_k{k}" for p in ("conservative", "optimistic") for k in sim["exponents"]]
            keys += [f"w_similarity_{c}" for c in m.classes]
        store = {k: [] for k in keys}; res = {}
        Nt_w = np.zeros(m.I); wsum = 0.0
        t0 = time.time()
        for i0 in range(0, n, chunk):
            nn = min(chunk, n - i0)
            P = m.draw(nn, rng)
            o, Nt = m.evaluate(P)
            for k in keys: store[k].append(P[k])
            for k, v in o.items():
                if v is not None: res.setdefault(k, []).append(np.array(v, copy=True))  # copy: never keep views of big arrays
            if (i0 // chunk) % 50 == 0:
                print(f"[{scen}] {i0+nn}/{n}  {time.time()-t0:.0f}s", flush=True)
        print(f"[{scen}] DONE {n}/{n}  {time.time()-t0:.0f}s", flush=True)
        P = {k: np.concatenate(v) for k, v in store.items()}
        R = {k: np.concatenate(v) for k, v in res.items()}
        bp, _ = m.evaluate(m.best_point())
        np.savez_compressed(os.path.join(outdir, f"samples_{scen}.npz"), **{"p_" + k: v for k, v in P.items()},
                            **{"r_" + k: v for k, v in R.items()})
        bestd = {k: (float(v[0]) if v is not None else None) for k, v in bp.items()}
        json.dump(bestd, open(os.path.join(outdir, f"best_{scen}.json"), "w"), indent=1)
        allres[scen] = dict(P=P, R=R, best=bestd)
    Ncl = None
    if do_classic:
        rng = np.random.default_rng(runc["seed"] + 1)
        Ncl = classic_static(cfg, rng)
        np.save(os.path.join(outdir, "classic_static_N.npy"), Ncl)
    return cfg, allres, Ncl

def load(cfg_path, outdir):
    cfg = yaml.safe_load(open(cfg_path)); allres = {}
    for scen in cfg["run"]["scenarios_to_run"]:
        z = np.load(os.path.join(outdir, f"samples_{scen}.npz"))
        P = {k[2:]: z[k] for k in z.files if k.startswith("p_")}
        R = {k[2:]: z[k] for k in z.files if k.startswith("r_")}
        allres[scen] = dict(P=P, R=R, best=json.load(open(os.path.join(outdir, f"best_{scen}.json"))))
    Ncl = np.load(os.path.join(outdir, "classic_static_N.npy"))
    return cfg, allres, Ncl

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "params.yaml"))
    ap.add_argument("--n", type=int, default=None)
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "results"))
    ap.add_argument("--scenario", default=None, help="run only this scenario (no report); for parallel runs")
    ap.add_argument("--analyze-only", action="store_true", help="load saved samples and write the report")
    a = ap.parse_args()
    import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    if a.scenario:
        run(a.config, a.n, a.out, scenarios=[a.scenario], do_classic=(a.scenario == "baseline"))
        raise SystemExit(0)
    if a.analyze_only:
        cfg, allres, Ncl = load(a.config, a.out)
    else:
        cfg, allres, Ncl = run(a.config, a.n, a.out)
    import analyze
    analyze.report(cfg, allres, Ncl, a.out)
