#!/usr/bin/env python3
"""
Reusable narrowband drift search over Breakthrough Listen (BL) open data, driven by a queue file.

  .venv/bin/python scan.py                 # process the next pending job (default --max-jobs 1)
  .venv/bin/python scan.py --list          # show the queue
  .venv/bin/python scan.py --max-jobs 2    # process two pending jobs
  .venv/bin/python scan.py add-cadence --coarse 34 --label "..." URL_ON1 URL_OFF1 URL_ON2 URL_OFF2 URL_ON3 URL_OFF3
  .venv/bin/python scan.py add-file --label "..." URL          # single .fil/.h5 file, no ON-OFF filter
  .venv/bin/python scan.py seed-index https://bldata.berkeley.edu/ATLAS/GB_ATLAS/ --coarse 18,34
  .venv/bin/python scan.py report          # regenerate scan_log.md / summary.json from the queue

Job kinds
  bl_h5_cadence : six (or any even number of) BL rawspec .0000.h5 files, ON/OFF alternating.  Only ONE coarse
                  channel (1,048,576 fine channels, ~2.9 MHz) is pulled from each remote file with HTTP range
                  requests (the compressed HDF5 chunks are copied byte-for-byte), so a 10 GB file costs ~160 MB.
  file          : a whole small public .fil/.h5 file downloaded with curl (e.g. the Voyager-1 test file).

For every job: turboSETI FindDoppler (de-Doppler search, |drift| <= --max-drift Hz/s) at each --snr threshold,
then (cadence jobs) turboSETI find_event_pipeline ON-OFF filtering at filter levels 1/2/3, a waterfall plot of the
top hit/event, and the results are written back into the queue file.  scan_log.md and summary.json are
regenerated from the queue after every run.  Hits are almost always RFI or noise; nothing here is a detection.

Weekly use: e.g.  crontab:  0 9 * * 1  cd /workspace/drake/seti && .venv/bin/python scan.py --max-jobs 1
"""
import argparse, datetime as dt, glob, hashlib, json, logging, os, re, shutil, subprocess, sys, time, warnings
warnings.filterwarnings("ignore")
HERE = os.path.dirname(os.path.abspath(__file__))
QUEUE = os.path.join(HERE, "queue.json")
NFPC_DEFAULT = 1048576

def now(): return dt.datetime.now().astimezone().isoformat(timespec="seconds")

# ----------------------------------------------------------------------------------------------- queue
def load_q(path):
    if os.path.exists(path): return json.load(open(path))
    return {"description": "Breakthrough Listen open-data scan queue (see scan.py docstring)", "jobs": []}

def _jsonable(o):
    try:
        import numpy as np
        if isinstance(o, np.generic): return o.item()
        if isinstance(o, np.ndarray): return o.tolist()
    except Exception: pass
    if isinstance(o, bytes): return o.decode(errors="replace")
    return str(o)

def save_q(q, path):
    tmp = path + ".tmp"; json.dump(q, open(tmp, "w"), indent=1, default=_jsonable); os.replace(tmp, path)

def job_id(files, coarse):
    h = hashlib.sha1(("|".join(files) + f"#{coarse}").encode()).hexdigest()[:8]
    stem = re.sub(r"[^A-Za-z0-9]+", "_", os.path.basename(files[0]).split(".")[0])[:40]
    return f"{stem}_cc{coarse}_{h}" if coarse is not None else f"{stem}_{h}"

def add_job(q, kind, files, coarse=None, label="", on_off_first="ON"):
    jid = job_id(files, coarse)
    if any(j["id"] == jid for j in q["jobs"]): print("already queued:", jid); return None
    q["jobs"].append({"id": jid, "kind": kind, "label": label, "files": files, "coarse_chan": coarse,
                      "on_off_first": on_off_first, "status": "pending", "added": now()})
    print("queued:", jid); return jid

# ----------------------------------------------------------------------------------------------- data access
def extract_coarse_channel(url, coarse, out_path, retries=3):
    """Copy one coarse channel of a remote BL rawspec HDF5 file into a small local HDF5 file (blimpy-compatible).
    Compressed chunks are fetched with HTTP range requests and written with write_direct_chunk (no recompression)."""
    import hdf5plugin, h5py, fsspec, requests, numpy as np
    from concurrent.futures import ThreadPoolExecutor
    if os.path.exists(out_path): return out_path
    fs = fsspec.filesystem("https", block_size=2**20)
    with h5py.File(fs.open(url, "rb"), "r") as f:
        d = f["data"]; attrs = dict(d.attrs); fattrs = dict(f.attrs)
        nt, nif, nch = d.shape
        nfpc = int(attrs.get("nfpc", NFPC_DEFAULT)) if int(attrs.get("nfpc", 0)) > 0 else NFPC_DEFAULT
        if d.chunks != (1, 1, nfpc): raise RuntimeError(f"unexpected chunking {d.chunks}")
        pl = d.id.get_create_plist(); filt = [pl.get_filter(i)[0] for i in range(pl.get_nfilters())]
        if filt not in ([32008], []): raise RuntimeError(f"unexpected filters {filt}")
        ranges = []
        for t in range(nt):
            ci = d.id.get_chunk_info_by_coord((t, 0, coarse * nfpc))
            ranges.append((t, ci.byte_offset, ci.size, ci.filter_mask))
    def get(r):
        t, off, size, fm = r
        for k in range(retries):
            try:
                resp = requests.get(url, headers={"Range": f"bytes={off}-{off+size-1}"}, timeout=120)
                if resp.status_code == 206 and len(resp.content) == size: return t, resp.content, fm
            except Exception: pass
            time.sleep(2 * (k + 1))
        raise RuntimeError(f"range fetch failed t={t}")
    with ThreadPoolExecutor(8) as ex: chunks = sorted(ex.map(get, ranges))
    tmp = out_path + ".part"
    with h5py.File(tmp, "w") as g:
        for k, v in fattrs.items(): g.attrs[k] = v
        kw = hdf5plugin.Bitshuffle(nelems=0, cname="lz4") if filt == [32008] else {}
        ds = g.create_dataset("data", shape=(nt, nif, nfpc), dtype="float32", chunks=(1, 1, nfpc), **kw)
        for t, raw, fm in chunks: ds.id.write_direct_chunk((t, 0, 0), raw, fm)
        for k, v in attrs.items():
            if k == "DIMENSION_LABELS": continue
            ds.attrs[k] = v
        ds.attrs["DIMENSION_LABELS"] = np.array([b"time", b"feed_id", b"frequency"], dtype=object)
        ds.attrs["fch1"] = float(attrs["fch1"]) + coarse * nfpc * float(attrs["foff"])
        ds.attrs["nchans"] = np.int32(nfpc); ds.attrs["nfpc"] = np.int32(nfpc)
        g.attrs["SOURCE_URL"] = url; g.attrs["COARSE_CHAN"] = coarse
    os.replace(tmp, out_path); return out_path

def download(url, out_path):
    if not os.path.exists(out_path):
        subprocess.run(["curl", "-s", "-L", "--fail", "-o", out_path + ".part", url], check=True)
        os.replace(out_path + ".part", out_path)
    return out_path

def header(path):
    from blimpy import Waterfall
    w = Waterfall(path, load_data=False); h = w.header
    g = lambda k: (h[k].decode() if isinstance(h.get(k), bytes) else h.get(k))
    out = {}
    for k in ("source_name", "tstart", "tsamp", "fch1", "foff", "nchans", "telescope_id"):
        v = g(k)
        try: v = v.item()
        except AttributeError: pass
        out[k] = v if isinstance(v, (str, int, float)) or v is None else str(v)
    out["n_ints"] = int(w.n_ints_in_file); return out

# ----------------------------------------------------------------------------------------------- search
def ensure_turboseti_compat():
    """turboSETI 2.3.2 + NumPy 2.x: a log line formats a 1-element array with %i and raises TypeError.
    Apply the one-line fix (idempotent) to the installed package."""
    import turbo_seti.find_doppler.find_doppler as m
    src = open(m.__file__).read()
    bad = '" is: %i" % max_val.total_n_hits)'
    if bad in src:
        open(m.__file__, "w").write(src.replace(bad, '" is: %i" % int(max_val.total_n_hits[0]))'))
        import importlib; importlib.reload(m)

def run_find_doppler(path, out_dir, snr, max_drift):
    ensure_turboseti_compat()
    from turbo_seti.find_doppler.find_doppler import FindDoppler
    os.makedirs(out_dir, exist_ok=True)
    dat = os.path.join(out_dir, os.path.basename(path).rsplit(".", 1)[0] + ".dat")
    if not os.path.exists(dat):
        fd = FindDoppler(path, max_drift=max_drift, snr=snr, out_dir=out_dir, n_coarse_chan=1,
                         log_level_int=logging.WARNING, blank_dc=True)
        fd.search(n_partitions=1, progress_bar="n")
    return dat

def read_dat(dat):
    from turbo_seti.find_event.find_event import read_dat as rd
    df = rd(dat)
    return df

def top_hits(df, n=10):
    if df is None or len(df) == 0: return []
    df = df.sort_values("SNR", ascending=False).head(n)
    return [{"freq_mhz": round(float(r.Freq), 6), "drift_hz_s": round(float(r.DriftRate), 4), "snr": round(float(r.SNR), 2)} for r in df.itertuples()]

def waterfall_plot(paths, labels, f_mid, drift, title, out_png, half_bw_hz=None):
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    from blimpy import Waterfall
    import numpy as np
    hdrs = [header(p) for p in paths]
    T = max(h["n_ints"] * h["tsamp"] for h in hdrs)
    t0 = min(h["tstart"] for h in hdrs)
    half = half_bw_hz or max(800.0, abs(drift) * T * (len(paths) * 1.3) + 400.0)
    f0, f1 = f_mid - half / 1e6, f_mid + half / 1e6
    fig, axs = plt.subplots(len(paths), 1, figsize=(7, 1.6 * len(paths) + 1), sharex=True, squeeze=False)
    for ax, p, lab, h in zip(axs[:, 0], paths, labels, hdrs):
        w = Waterfall(p, f_start=f0, f_stop=f1)
        fr, data = w.grab_data(f_start=f0, f_stop=f1)
        data = np.squeeze(data)
        if data.ndim == 1: data = data[None, :]
        if fr[0] > fr[-1]: fr = fr[::-1]; data = data[:, ::-1]
        dt_ = (h["tstart"] - t0) * 86400.0
        ax.imshow(10 * np.log10(np.maximum(data, 1e-12)), aspect="auto", origin="upper", cmap="viridis",
                  extent=[(fr[0] - f_mid) * 1e6, (fr[-1] - f_mid) * 1e6, dt_ + h["n_ints"] * h["tsamp"], dt_])
        tt = np.array([dt_, dt_ + h["n_ints"] * h["tsamp"]])
        ax.plot(drift * (tt - (hdrs[0]["tstart"] - t0) * 86400.0), tt, "r--", lw=0.8, alpha=0.7)
        ax.set_xlim(-half, half); ax.set_ylabel(lab, fontsize=7)
    axs[-1, 0].set_xlabel(f"frequency offset from {f_mid:.6f} MHz (Hz)")
    fig.suptitle(title, fontsize=8); fig.tight_layout(); fig.savefig(out_png, dpi=110); plt.close(fig)
    return out_png

def process(job, args):
    import pandas as pd
    jdir = os.path.join(HERE, "data", job["id"]); odir = os.path.join(HERE, "out", job["id"]); os.makedirs(jdir, exist_ok=True); os.makedirs(odir, exist_ok=True)
    t_start = time.time(); res = {"started": now(), "max_drift_hz_s": args.max_drift, "snr_thresholds": args.snr, "files": []}
    local = []
    for u in job["files"]:
        if job["kind"] == "bl_h5_cadence":
            p = os.path.join(jdir, os.path.basename(u).replace(".h5", f".cc{job['coarse_chan']}.h5"))
            extract_coarse_channel(u, job["coarse_chan"], p)
        else:
            p = download(u, os.path.join(jdir, os.path.basename(u)))
        local.append(p)
        h = header(p); res["files"].append({"url": u, "local_mb": round(os.path.getsize(p) / 2**20, 1), **h})
        print(f"  ready {os.path.basename(p)}  {res['files'][-1]['local_mb']} MB", flush=True)
    res["bytes_downloaded_mb"] = round(sum(f["local_mb"] for f in res["files"]), 1)
    is_cad = job["kind"] == "bl_h5_cadence" and len(local) >= 2
    first_on = job.get("on_off_first", "ON") == "ON"
    roles = [("ON" if (i % 2 == 0) == first_on else "OFF") for i in range(len(local))] if is_cad else ["single"] * len(local)
    res["roles"] = roles; res["by_snr"] = {}
    for snr in args.snr:
        sdir = os.path.join(odir, f"snr{snr:g}"); os.makedirs(sdir, exist_ok=True)
        dats = []; per_file = []
        for p, role in zip(local, roles):
            print(f"  turboSETI snr={snr} {os.path.basename(p)}", flush=True)
            dat = run_find_doppler(p, sdir, snr, args.max_drift); dats.append(dat)
            df = read_dat(dat)
            nz = int((df["DriftRate"].abs() > 0).sum()) if len(df) else 0
            per_file.append({"file": os.path.basename(p), "role": role, "hits": int(len(df)), "hits_nonzero_drift": nz, "top": top_hits(df, 5)})
        entry = {"per_file": per_file, "hits_total": sum(x["hits"] for x in per_file)}
        if is_cad:
            from turbo_seti.find_event.find_event_pipeline import find_event_pipeline
            dl = os.path.join(sdir, "dat_files.lst"); hl = os.path.join(sdir, "h5_files.lst")
            open(dl, "w").write("\n".join(dats) + "\n")
            h5s = []
            for p, d in zip(local, dats):     # find_event_pipeline expects the h5 next to / named like the dat
                link = d[:-4] + ".h5"
                if not os.path.exists(link): os.symlink(p, link)
                h5s.append(link)
            open(hl, "w").write("\n".join(h5s) + "\n")
            entry["events"] = {}
            for lvl in (1, 2, 3):
                csv = os.path.join(sdir, f"events_f{lvl}.csv")
                try:
                    ev = find_event_pipeline(dl, h5_file_list_str=hl, check_zero_drift=False, filter_threshold=lvl,
                                             on_off_first=job.get("on_off_first", "ON"), number_in_cadence=len(local),
                                             SNR_cut=snr, saving=True, csv_name=csv, user_validation=False, sortby_tstart=True)
                except Exception as e:
                    ev = None; entry.setdefault("errors", []).append(f"f{lvl}: {e!r}")
                n = 0 if ev is None else len(ev)
                n_ev = 0 if ev is None or not n else (int(ev["Hit_ID"].nunique()) if (lvl == 3 and "Hit_ID" in ev) else n)   # f1/f2 rows are single hits
                top, groups = [], []
                if ev is not None and n:
                    e2 = ev.sort_values("SNR", ascending=False)
                    top = [{"freq_mhz": round(float(r.Freq), 6), "drift_hz_s": round(float(r.DriftRate), 4), "snr": round(float(r.SNR), 2), "status": str(getattr(r, "status", ""))} for r in e2.head(5).itertuples()]
                    if lvl == 3 and "Hit_ID" in ev:
                        for hid, g in sorted(ev.groupby("Hit_ID"), key=lambda kv: -kv[1]["SNR"].max())[:5]:
                            groups.append({"hit_id": str(hid), "n_on_hits": int(len(g)), "max_snr": round(float(g["SNR"].max()), 2),
                                           "freqs_mhz": [round(float(x), 6) for x in g["Freq"]], "drifts_hz_s": [round(float(x), 4) for x in g["DriftRate"]],
                                           "snrs": [round(float(x), 2) for x in g["SNR"]]})
                entry["events"][f"f{lvl}"] = {"n_rows": n, "n_events": n_ev, "top": top, "groups": groups}
                print(f"  snr={snr} filter f{lvl}: {n} hit rows in {n_ev} events", flush=True)
        res["by_snr"][f"{snr:g}"] = entry
    # plot: the strongest surviving event at the lowest SNR threshold, else the strongest ON/single hit
    lo = f"{min(args.snr):g}"; E = res["by_snr"][lo]; pick = None; why = ""
    for lvl in ("f3", "f2"):
        if is_cad and E["events"][lvl]["top"]: pick = E["events"][lvl]["top"][0]; why = f"top {lvl} event (SNR>{lo})"; break
    if pick is None:
        cands = [(t, x["file"]) for x in E["per_file"] if x["role"] in ("ON", "single") for t in x["top"]]
        if cands: pick = max(cands, key=lambda c: c[0]["snr"])[0]; why = f"strongest hit in an ON/single file (SNR>{lo}); no ON-only event survived" if is_cad else f"strongest hit (SNR>{lo})"
    if pick:
        png = os.path.join(odir, "top_hit.png")
        try:
            labs = [f"{r} {(re.findall(r'_(\d{4})\.rawspec', os.path.basename(p)) or [''])[0]}" for r, p in zip(roles, local)]
            waterfall_plot(local, labs, pick["freq_mhz"], pick["drift_hz_s"], f"{job['id']}\n{why}: {pick['freq_mhz']:.6f} MHz, drift {pick['drift_hz_s']} Hz/s, S/N {pick['snr']}", png)
            res["plot"] = os.path.relpath(png, HERE); res["plot_what"] = why; res["plot_hit"] = pick
        except Exception as e: res["plot_error"] = repr(e)
    res["finished"] = now(); res["runtime_min"] = round((time.time() - t_start) / 60, 1)
    return res

def inject_test(job, args, f0_mhz=None, drift=0.37, amp_sigma=8.0):
    """Positive control: copy the cadence, add a synthetic drifting narrowband tone to the ON scans only, rerun the
    S/N-10 search + ON-OFF filter and check that the tone comes back as a filter-3 event at the injected drift."""
    import h5py, hdf5plugin, numpy as np
    from turbo_seti.find_event.find_event_pipeline import find_event_pipeline
    jdir = os.path.join(HERE, "data", job["id"]); idir = os.path.join(HERE, "out", job["id"], "inject"); os.makedirs(idir, exist_ok=True)
    src = sorted(glob.glob(os.path.join(jdir, "*.h5")), key=lambda p: header(p)["tstart"])
    roles = job["result"]["roles"]; hdr0 = header(src[0]); t00 = hdr0["tstart"]
    nf = int(hdr0["nchans"]); foff = hdr0["foff"]; fch1 = hdr0["fch1"]
    if f0_mhz is None: f0_mhz = fch1 + int(nf * 0.3) * foff          # 30% into the coarse channel, away from DC
    outs = []
    for p, role in zip(src, roles):
        o = os.path.join(idir, os.path.basename(p).replace(".h5", ".inj.h5"))
        if not os.path.exists(o):
            with h5py.File(p, "r") as f:
                x = f["data"][:]; attrs = dict(f["data"].attrs); fat = dict(f.attrs)
            if role == "ON":
                h = header(p); t = (h["tstart"] - t00) * 86400.0 + (np.arange(x.shape[0]) + 0.5) * h["tsamp"]
                sig = np.std(np.diff(x[:, 0, :], axis=1), axis=1) / np.sqrt(2)          # per-integration channel noise
                ch = (f0_mhz + drift * t / 1e6 - fch1) / foff
                for k in range(x.shape[0]):
                    c = int(round(ch[k]))
                    if 0 <= c < nf: x[k, 0, c] += amp_sigma * sig[k]
            with h5py.File(o, "w") as g:
                for k, v in fat.items(): g.attrs[k] = v
                ds = g.create_dataset("data", data=x, chunks=(1, 1, nf), **hdf5plugin.Bitshuffle(nelems=0, cname="lz4"))
                for k, v in attrs.items(): ds.attrs[k] = v
        outs.append(o)
    sdir = os.path.join(idir, "snr10"); dats = [run_find_doppler(o, sdir, 10.0, args.max_drift) for o in outs]
    dl = os.path.join(sdir, "dat_files.lst"); hl = os.path.join(sdir, "h5_files.lst")
    open(dl, "w").write("\n".join(dats) + "\n"); h5s = []
    for o, d in zip(outs, dats):
        link = d[:-4] + ".h5"
        if not os.path.exists(link): os.symlink(o, link)
        h5s.append(link)
    open(hl, "w").write("\n".join(h5s) + "\n")
    ev = find_event_pipeline(dl, h5_file_list_str=hl, check_zero_drift=False, filter_threshold=3, on_off_first="ON",
                             number_in_cadence=len(outs), SNR_cut=10.0, saving=True, csv_name=os.path.join(sdir, "events_f3.csv"), user_validation=False)
    rec = None
    if ev is not None and len(ev):
        tol_hz = abs(drift) * 1300 + 50
        for hid, g in ev.groupby("Hit_ID"):
            first = g.sort_values("MJD").iloc[0]
            if abs(first["Freq"] - f0_mhz) * 1e6 < tol_hz:
                rec = {"hit_id": str(hid), "drifts_hz_s": [round(float(v), 4) for v in g["DriftRate"]], "snrs": [round(float(v), 2) for v in g["SNR"]],
                       "freqs_mhz": [round(float(v), 6) for v in g["Freq"]]}
    n3 = 0 if ev is None else int(ev["Hit_ID"].nunique())
    txt = (f"A tone of {amp_sigma} x the per-channel noise per integration, drifting at {drift} Hz/s from {f0_mhz:.6f} MHz, was added to the three ON scans only. "
           + (f"Recovered as filter-3 event `{rec['hit_id']}` with ON-hit drifts {rec['drifts_hz_s']} Hz/s and S/N {rec['snrs']}." if rec else "It was NOT recovered as a filter-3 event.")
           + f" The injected copy produced {n3} filter-3 event(s) in total at S/N > 10.")
    return {"f0_mhz": f0_mhz, "drift_hz_s": drift, "amp_sigma": amp_sigma, "recovered": bool(rec), "match": rec, "n_f3_events": n3, "summary": txt}

# ----------------------------------------------------------------------------------------------- report
CAVEATS = """**Caveats (read these first).** Every hit and every "event" below is almost certainly radio-frequency interference (RFI) or noise. No detection is claimed. turboSETI hits are simply narrowband features above an S/N threshold, and the ON-OFF test only removes signals that also appear in the OFF pointings; a filter-3 event would still need checks against known RFI, a look at the waterfall, and above all re-observation at a later date before it means anything. The S/N 5 runs are deliberately below the usual BL threshold (10) and are dominated by noise fluctuations. These are tiny slices (one ~2.9 MHz coarse channel per file) of public data that BL has already searched; BL reported no technosignature in them."""

def report(q, path_md, path_json):
    done = [j for j in q["jobs"] if j["status"] == "done"]
    pend = [j for j in q["jobs"] if j["status"] == "pending"]
    fail = [j for j in q["jobs"] if j["status"] == "failed"]
    L = ["# SETI scan log (Breakthrough Listen open data)\n",
         f"Generated by `seti/scan.py` on {now()} (America/Phoenix). Queue: {len(done)} done, {len(pend)} pending, {len(fail)} failed.\n",
         CAVEATS + "\n"]
    for j in done:
        r = j["result"]; L.append(f"## {j['label'] or j['id']}\n")
        L.append(f"* Job id `{j['id']}`, kind `{j['kind']}`" + (f", coarse channel {j['coarse_chan']}" if j.get("coarse_chan") is not None else "") +
                 f"; run {r['started']} → {r['finished']} ({r['runtime_min']} min); data pulled ≈ {r['bytes_downloaded_mb']} MB.")
        L.append(f"* turboSETI FindDoppler: max |drift| {r['max_drift_hz_s']} Hz/s, S/N thresholds {', '.join(str(s) for s in r['snr_thresholds'])}, DC bin blanked.")
        L.append("\n| file | role | source | MJD start | f_top (MHz) | channel width (Hz) | ints × tsamp (s) | URL |\n|---|---|---|---|---|---|---|---|")
        for f, role in zip(r["files"], r["roles"]):
            L.append(f"| `{os.path.basename(f['url'])}` | {role} | {f['source_name']} | {f['tstart']:.5f} | {f['fch1']:.6f} | {abs(f['foff'])*1e6:.3f} | {f['n_ints']} × {f['tsamp']:.3f} | {f['url']} |")
        for s, E in r["by_snr"].items():
            L.append(f"\n**S/N > {s}:** {E['hits_total']} hits in total (" + "; ".join(f"{x['role']} {x['hits']}" for x in E["per_file"]) + ").")
            if "events" in E:
                L.append("ON-OFF filtering (turboSETI find_event_pipeline, zero-drift hits excluded): " +
                         ", ".join((f"filter {k[1]}: {v['n_rows']} hits" if k != "f3" else f"filter 3: {v.get('n_events', v['n_rows'])} event(s) ({v['n_rows']} ON hits)") for k, v in E["events"].items()) +
                         " (filter 1 = S/N and drift cuts only; 2 = in at least one ON and no OFF; 3 = in all ONs and no OFF).")
            rows = []
            for x in E["per_file"]:
                for t in x["top"][:3]: rows.append((t, x["role"], x["file"]))
            rows = sorted(rows, key=lambda z: -z[0]["snr"])[:5]
            if rows:
                L.append("\n| top hits | frequency (MHz) | drift (Hz/s) | S/N | file |\n|---|---|---|---|---|")
                for i, (t, role, fn) in enumerate(rows, 1): L.append(f"| {i} ({role}) | {t['freq_mhz']:.6f} | {t['drift_hz_s']} | {t['snr']} | `{fn}` |")
            if "events" in E:
                gs = E["events"]["f3"].get("groups") or []
                if gs:
                    L.append("\nFilter-3 events (one row per event; the hits in the three ON scans):\n\n| event | ON-hit frequencies (MHz) | ON-hit drifts (Hz/s) | ON-hit S/N |\n|---|---|---|---|")
                    for g in gs: L.append(f"| `{g['hit_id']}` | {', '.join(f'{x:.6f}' for x in g['freqs_mhz'])} | {', '.join(str(x) for x in g['drifts_hz_s'])} | {', '.join(str(x) for x in g['snrs'])} |")
                if E["events"]["f2"]["top"]:
                    L.append(f"\nStrongest filter-2 hits (ON-only at this threshold): " + "; ".join(f"{t['freq_mhz']:.6f} MHz, {t['drift_hz_s']} Hz/s, S/N {t['snr']}" for t in E["events"]["f2"]["top"][:3]) + ".")
            if E.get("errors"): L.append("\nErrors: " + "; ".join(E["errors"]))
        if r.get("plot"): L.append(f"\n![top hit]({r['plot']})\n\nPlot: {r['plot_what']} — {r['plot_hit']['freq_mhz']:.6f} MHz, drift {r['plot_hit']['drift_hz_s']} Hz/s, S/N {r['plot_hit']['snr']}. Red dashed line = fitted drift.\n")
        if j.get("injection_test"):
            it = j["injection_test"]
            L.append(f"\n**Injection-recovery check (pipeline sanity test, synthetic signal).** {it['summary']}\n")
        if j.get("notes"): L.append(f"\n*Notes:* {j['notes']}\n")
    if fail:
        L.append("## Failed jobs\n"); L += [f"* `{j['id']}`: {j.get('error')}" for j in fail]
    L.append("\n## Pending queue\n")
    L += [f"* `{j['id']}` ({j['kind']}" + (f", coarse channel {j['coarse_chan']}" if j.get("coarse_chan") is not None else "") + f"): {j['label']}" for j in pend] or ["* (empty)"]
    L.append("\n## How the queue works\n")
    L.append("`seti/queue.json` lists jobs with `status` pending / done / failed. `python scan.py` takes the next pending job(s) (`--max-jobs`), "
             "pulls the data (one coarse channel per remote BL HDF5 file via HTTP range requests, or a whole small file), runs turboSETI at each S/N threshold, "
             "applies ON-OFF cadence filtering when the job is a cadence, plots the top hit, stores results in the job, marks it done and rebuilds this log. "
             "Add work with `scan.py add-cadence`, `scan.py add-file` or `scan.py seed-index <BL directory URL> --coarse a,b`. A weekly cron line such as "
             "`0 9 * * 1 cd /workspace/drake/seti && .venv/bin/python scan.py --max-jobs 1` keeps it moving.\n")
    open(path_md, "w").write("\n".join(L) + "\n")
    # compact README text
    parts = []
    for j in done:
        r = j["result"]; s_hi, s_lo = max(r["snr_thresholds"]), min(r["snr_thresholds"])
        Eh, El = r["by_snr"][f"{s_hi:g}"], r["by_snr"][f"{s_lo:g}"]
        ev = lambda E: (f"; ON-OFF filter-3 events: {E['events']['f3'].get('n_events', E['events']['f3']['n_rows'])}" if "events" in E else "")
        parts.append(f"* **{j['label']}** — hits at S/N>{s_hi:g}: {Eh['hits_total']}{ev(Eh)}; at S/N>{s_lo:g}: {El['hits_total']}{ev(El)}." +
                     (f" Top plotted: {r['plot_hit']['freq_mhz']:.6f} MHz, {r['plot_hit']['drift_hz_s']} Hz/s, S/N {r['plot_hit']['snr']} ([plot](seti/{r['plot']}))." if r.get("plot") else "") +
                     (f" Injection check: a synthetic drifting tone added to the ON scans was {'recovered' if j['injection_test']['recovered'] else 'NOT recovered'} as a filter-3 event." if j.get("injection_test") else ""))
    txt = ("Feasibility pass on Breakthrough Listen public data with turboSETI (`seti/scan.py`, queue in `seti/queue.json`). "
           "Full details in [`seti/scan_log.md`](seti/scan_log.md).\n\n" + "\n".join(parts) + "\n\n" +
           "Every hit is almost certainly RFI or noise; **no detection is claimed**, and anything interesting would need re-observation. " +
           f"{len(pend)} job(s) pending for the weekly run.")
    json.dump({"generated": now(), "readme_text": txt, "n_done": len(done), "n_pending": len(pend)}, open(path_json, "w"), indent=1)

# ----------------------------------------------------------------------------------------------- CLI
def seed_index(q, url, coarse_list, product="0000", nodes=None, label_prefix=""):
    """Queue every complete 6-scan cadence (consecutive scan numbers, ON/OFF alternating) found in a BL directory index."""
    import requests
    html = requests.get(url, timeout=60).text
    names = sorted(set(re.findall(r'href="([^"]+\.rawspec\.%s\.h5)"' % product, html)))
    groups = {}
    for n in names:
        m = re.match(r"(blc\d+)_guppi_(\d+)_(\d+)_(.+?)_(\d{4})\.rawspec", n)
        if m and (not nodes or m.group(1) in nodes): groups.setdefault(m.group(1), []).append((int(m.group(5)), n))
    for node, lst in sorted(groups.items()):
        lst.sort(); runs, cur = [], [lst[0]]
        for a, b in zip(lst, lst[1:]):
            if b[0] == a[0] + 1: cur.append(b)
            else: runs.append(cur); cur = [b]
        runs.append(cur)
        for r in runs:
            if len(r) != 6: continue
            files = [url.rstrip("/") + "/" + n for _, n in r]
            for c in coarse_list:
                add_job(q, "bl_h5_cadence", files, c, f"{label_prefix}{node} scans {r[0][0]:04d}-{r[-1][0]:04d}, coarse channel {c}")

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", nargs="?", default="run", choices=["run", "add-cadence", "add-file", "seed-index", "report", "inject-test"])
    ap.add_argument("urls", nargs="*")
    ap.add_argument("--queue", default=QUEUE); ap.add_argument("--max-jobs", type=int, default=1)
    ap.add_argument("--snr", type=float, nargs="+", default=[10.0, 5.0]); ap.add_argument("--max-drift", type=float, default=4.0)
    ap.add_argument("--coarse", default=None); ap.add_argument("--label", default=""); ap.add_argument("--on-off-first", default="ON")
    ap.add_argument("--nodes", default=None, help="seed-index: comma list of compute nodes, e.g. blc23,blc24")
    ap.add_argument("--list", action="store_true"); ap.add_argument("--job", default=None, help="run this job id even if not first")
    a = ap.parse_args(); q = load_q(a.queue)
    md, js = os.path.join(HERE, "scan_log.md"), os.path.join(HERE, "summary.json")
    if a.list:
        for j in q["jobs"]: print(f"{j['status']:8s} {j['id']:60s} {j['label']}")
        return
    if a.cmd == "add-cadence":
        add_job(q, "bl_h5_cadence", a.urls, int(a.coarse), a.label, a.on_off_first); save_q(q, a.queue); return
    if a.cmd == "add-file":
        add_job(q, "file", a.urls, None, a.label); save_q(q, a.queue); return
    if a.cmd == "seed-index":
        seed_index(q, a.urls[0], [int(c) for c in (a.coarse or "32").split(",")], nodes=(a.nodes.split(",") if a.nodes else None), label_prefix=a.label); save_q(q, a.queue); return
    if a.cmd == "inject-test":
        j = next(j for j in q["jobs"] if j["id"] == a.job)
        j["injection_test"] = inject_test(j, a); print(j["injection_test"]["summary"]); save_q(q, a.queue); report(q, md, js); return
    if a.cmd == "report":
        report(q, md, js); print("wrote", md); return
    todo = [j for j in q["jobs"] if (j["id"] == a.job if a.job else j["status"] == "pending")][: a.max_jobs]
    if not todo: print("queue empty: nothing pending")
    for j in todo:
        print(f"[{now()}] job {j['id']}", flush=True)
        try:
            j["result"] = process(j, a); j["status"] = "done"; j["processed"] = now()
        except Exception as e:
            import traceback; traceback.print_exc()
            j["status"] = "failed"; j["error"] = repr(e)
        save_q(q, a.queue)
    report(q, md, js); print("wrote", md)

if __name__ == "__main__":
    main()
