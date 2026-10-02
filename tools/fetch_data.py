#!/usr/bin/env python3
"""Download the raw inputs that are too large / third-party to commit.
  data/pscomppars.csv   NASA Exoplanet Archive Planetary Systems Composite Parameters (all columns), via TAP
  data/smh2020_kois.csv Archive KOI cumulative table rows for the KOIs legible in Schulze-Makuch+2020 Fig. 2
Then run:  python hz_archive.py && python esi.py && python superhab.py
"""
import os, urllib.parse, urllib.request
TAP = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KOIS = ["K07894.01", "K08242.01", "K07621.01", "K07711.01", "K05554.01", "K08047.01", "K05135.01", "K07235.01", "K05237.01",
        "K05978.01", "K05389.01", "K05130.01", "K05819.01", "K07223.01", "K08000.01", "K05715.01", "K05176.01", "K00172.02",
        "K02162.01", "K05248.01", "K05276.01", "K05878.01", "K00456.04"]
def tap(query, out):
    url = TAP + "?" + urllib.parse.urlencode({"query": query, "format": "csv"})
    os.makedirs(os.path.dirname(out), exist_ok=True)
    print("fetching", out); urllib.request.urlretrieve(url, out)
if __name__ == "__main__":
    tap("select * from pscomppars", os.path.join(HERE, "data", "pscomppars.csv"))
    tap("select kepoi_name,kepler_name,koi_disposition,koi_pdisposition,koi_prad,koi_insol,koi_teq,koi_steff,koi_srad,koi_smass,koi_period "
        "from cumulative where kepoi_name in (" + ",".join(f"'{k}'" for k in KOIS) + ")", os.path.join(HERE, "data", "smh2020_kois.csv"))
