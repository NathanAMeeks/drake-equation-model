# MANIFEST — archive of the local working copy (2026-11-09)

`MANIFEST.csv` lists every file in the local working copy `/workspace/drake`: path, size, SHA-256, where it lives on GitHub, and how it was verified.

- **git (348 files):** committed to `main` at commit `3644c01`. The link is `blob/<commit>/<path>`.
- **release (86 files):** stored as GitHub Release assets. None is split, and each is a single file under 2 GB.
  - [`data-2026-11-09`](https://github.com/NathanAMeeks/drake-equation-model/releases/tag/data-2026-11-09): 59 Monte Carlo sample arrays (`*.npz`, `*.npy`), 5.07 GB.
  - [`seti-data-2026-11-09`](https://github.com/NathanAMeeks/drake-equation-model/releases/tag/seti-data-2026-11-09): 27 raw SETI files, 4.50 GB. They are public Breakthrough Listen data: coarse-channel extracts of GBT observations of 3I/ATLAS from https://bldata.berkeley.edu/ATLAS/GB_ATLAS/, plus the BL tutorial Voyager-1 file from https://storage.googleapis.com/gbt_fil/.
  - **Asset names:** each name is the repo path with `/` replaced by `__`. To restore a file, download it and rename it back, for example `results__v1__samples_baseline.npz` becomes `results/v1/samples_baseline.npz`. Then check it with `sha256sum -c`.
- **Excluded:**
  - `xpost/arcylo_photo1.jpg`: a private X post image, kept out of the public repo.
  - `.venv/`: virtual environment, rebuildable from `requirements.txt`.
  - `__pycache__/`: bytecode cache.
  - `.test/data`: a symlink duplicating `data/`.
- **Verification (2026-11-09):**
  - Git files: SHA-256 from a fresh clone of the remote.
  - Release assets: GitHub's reported size and SHA-256 digest, plus a full re-download of every asset, all hashed with SHA-256.
  - Result: 434 of 434 published files match, covering 9,749,011,429 bytes, which is 100% of published bytes and 99.997% of all bytes in the working copy.

**Note:** `data/` holds the 2026-11-09 NASA Exoplanet Archive pull (6,464 rows). The model has not been rerun on it. The current headline in the README uses the 2026-11-02 data.

## Removed Nov 9, 2026: Smithsonian pages
`data/si_species.html` and the 21 pages in `data/si/` are Smithsonian Human Origins pages under Smithsonian copyright. They were removed from the current tree. MANIFEST.csv now lists each with its original source URL, and `data/SOURCES_smithsonian.md` holds the links. The extracted data, `data/si_when_lived.json`, stays. No release asset contained these pages.
