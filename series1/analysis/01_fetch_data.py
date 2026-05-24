"""
Marginal Fuel -- Data Acquisition
Fetches all data needed for the gas-to-power price transmission analysis.

Free sources used:
  - FRED API (Henry Hub daily): free key at fred.stlouisfed.org
  - EIA API v2 (Transco Zone 6 spot prices): free key at eia.gov/opendata
  - EIA wholesale markets (PJM Dominion Zone DA LMPs): no auth required

Run this first. Saves cleaned CSVs to ../data/

Set environment variables before running:
  export FRED_API_KEY=your_key_here
  export EIA_API_KEY=your_key_here   (optional, for Transco basis spread)
"""

import io
import os
import requests
import pandas as pd
import numpy as np
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)

FRED_API_KEY = os.environ.get("FRED_API_KEY", "")
EIA_API_KEY  = os.environ.get("EIA_API_KEY", "")


# =====================================================================
# 1. HENRY HUB -- FRED API
# =====================================================================

def fetch_henry_hub_fred():
    print("Fetching Henry Hub daily from FRED...")
    url = "https://api.stlouisfed.org/fred/series/observations"
    params = {
        "series_id": "DHHNGSP",
        "api_key": FRED_API_KEY,
        "file_type": "json",
        "observation_start": "2015-01-01",
        "observation_end": "2026-12-31",
    }
    r = requests.get(url, params=params, timeout=30)
    r.raise_for_status()
    obs = r.json()["observations"]
    df = pd.DataFrame(obs)[["date", "value"]]
    df["date"] = pd.to_datetime(df["date"])
    df["henry_hub"] = pd.to_numeric(df["value"], errors="coerce")
    df = df[["date", "henry_hub"]].dropna()

    out = DATA_DIR / "henry_hub_daily.csv"
    df.to_csv(out, index=False)
    print(f"  Saved {len(df)} rows to {out.name}")
    print(f"  Range: {df['date'].min().date()} to {df['date'].max().date()}")
    print(f"  Latest price: ${df['henry_hub'].iloc[-1]:.2f}/MMBtu")
    return df


# =====================================================================
# 2. TRANSCO ZONE 6 NY -- EIA API v2 (optional)
# =====================================================================
# Requires a free EIA API key: https://www.eia.gov/opendata/register.php
# Adds basis spread context. Henry Hub alone is sufficient for the core analysis.

def fetch_transco_eia_api(api_key: str = EIA_API_KEY):
    if not api_key:
        print("  EIA_API_KEY not set -- skipping Transco Zone 6.")
        print("  Register free at https://www.eia.gov/opendata/register.php")
        return None

    print("Fetching Transco Zone 6 NY spot prices from EIA API v2...")
    url = "https://api.eia.gov/v2/natural-gas/pri/sum/data/"
    params = {
        "api_key": api_key,
        "frequency": "daily",
        "data[0]": "value",
        "facets[series][]": "RNGWTZ6NYD",
        "start": "2015-01-01",
        "sort[0][column]": "period",
        "sort[0][direction]": "asc",
        "length": 5000,
        "offset": 0,
    }
    all_rows = []
    while True:
        r = requests.get(url, params=params, timeout=30)
        r.raise_for_status()
        data = r.json().get("response", {})
        rows = data.get("data", [])
        if not rows:
            break
        all_rows.extend(rows)
        total = data.get("total", 0)
        if len(all_rows) >= total:
            break
        params["offset"] += 5000

    if not all_rows:
        print("  No Transco data returned -- series ID may have changed.")
        return None

    df = pd.DataFrame(all_rows)
    df["date"] = pd.to_datetime(df["period"])
    df["transco_z6_ny"] = pd.to_numeric(df["value"], errors="coerce")
    df = df[["date", "transco_z6_ny"]].dropna().sort_values("date")

    out = DATA_DIR / "transco_z6_daily.csv"
    df.to_csv(out, index=False)
    print(f"  Saved {len(df)} rows to {out.name}")
    return df


# =====================================================================
# 3. PJM DOMINION ZONE -- day-ahead hourly LMPs via EIA annual CSVs
# =====================================================================
# EIA publishes PJM zone LMPs as annual CSV files. No API key required.
# Available: 2020 (partial, Sep onward) through present.
# URL pattern: eia.gov/electricity/wholesalemarkets/csv/pjm_lmp_da_hr_zones_{year}.csv

def fetch_pjm_dom_lmp_eia(years: list = None):
    if years is None:
        years = list(range(2020, 2026))

    print(f"Fetching PJM Dominion Zone LMPs from EIA annual files ({years[0]}-{years[-1]})...")

    DOM_COL  = "Dominion Energy LMP"
    DOM_CONG = "Dominion Energy (Congestion)"
    DATE_COL = "Local Date"

    all_years = []
    for yr in years:
        url = f"https://www.eia.gov/electricity/wholesalemarkets/csv/pjm_lmp_da_hr_zones_{yr}.csv"
        try:
            r = requests.get(url, timeout=60)
            r.raise_for_status()
            df = pd.read_csv(
                io.BytesIO(r.content),
                skiprows=3,
                usecols=[DATE_COL, DOM_COL, DOM_CONG],
            )
            df[DATE_COL] = pd.to_datetime(df[DATE_COL], errors="coerce")
            df[DOM_COL]  = pd.to_numeric(df[DOM_COL],  errors="coerce")
            df[DOM_CONG] = pd.to_numeric(df[DOM_CONG], errors="coerce")
            df = df.dropna(subset=[DATE_COL, DOM_COL])
            all_years.append(df)
            print(f"  {yr}: {df[DATE_COL].min().date()} to {df[DATE_COL].max().date()} ({len(df):,} hrs)")
        except Exception as e:
            print(f"  {yr}: failed - {e}")

    if not all_years:
        print("  No EIA PJM data retrieved.")
        return None

    hourly = pd.concat(all_years, ignore_index=True)
    hourly = hourly.rename(columns={DATE_COL: "date", DOM_COL: "dom_lmp", DOM_CONG: "dom_congestion"})

    df_daily = (
        hourly.groupby("date")
        .agg(
            dom_lmp_mean=("dom_lmp", "mean"),
            dom_lmp_min=("dom_lmp", "min"),
            dom_lmp_max=("dom_lmp", "max"),
            dom_congestion_mean=("dom_congestion", "mean"),
            hours=("dom_lmp", "count"),
        )
        .reset_index()
    )
    df_daily = df_daily[df_daily["hours"] >= 20]  # drop partial days

    out = DATA_DIR / "pjm_dom_lmp_daily.csv"
    df_daily.to_csv(out, index=False)
    print(f"  Saved {len(df_daily)} daily obs to {out.name}")
    print(f"  Range: {df_daily['date'].min().date()} to {df_daily['date'].max().date()}")
    print(f"  Avg Dominion LMP: ${df_daily['dom_lmp_mean'].mean():.2f}/MWh")
    return df_daily


# =====================================================================
# QUICK DATA SUMMARY
# =====================================================================

def print_summary():
    print("\n" + "=" * 55)
    print("DATA SUMMARY")
    print("=" * 55)
    for fname in ["henry_hub_daily.csv", "transco_z6_daily.csv", "pjm_dom_lmp_daily.csv"]:
        path = DATA_DIR / fname
        if path.exists():
            df = pd.read_csv(path)
            date_col = "date" if "date" in df.columns else df.columns[0]
            df[date_col] = pd.to_datetime(df[date_col])
            print(f"  {fname}")
            print(f"    {len(df):,} rows | {df[date_col].min().date()} to {df[date_col].max().date()}")
        else:
            print(f"  {fname} : NOT FOUND")
    print("=" * 55)


if __name__ == "__main__":
    hh      = fetch_henry_hub_fred()
    transco = fetch_transco_eia_api()
    lmp     = fetch_pjm_dom_lmp_eia()

    print_summary()
    print("\nNext: run 02_build_panel.py")
