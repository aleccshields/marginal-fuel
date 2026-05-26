"""
Marginal Fuel -- Series 3 -- Post 11
Data acquisition: PJM all-zone day-ahead LMPs, 2020-2024

Source:
  EIA wholesale markets annual CSVs (no auth required)
  URL: eia.gov/electricity/wholesalemarkets/csv/pjm_lmp_da_hr_zones_{year}.csv

Downloads hourly zone LMPs for all 21 PJM load zones and aggregates to
daily averages. Saves:
  data/pjm_zones_hourly_{year}.parquet  -- raw hourly (large)
  data/pjm_zones_daily.csv             -- daily averages, all zones

Run from repo root: python series3/analysis/11_fetch_pjm_zones.py
"""

import io
import sys
import requests
import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)

YEARS = list(range(2020, 2026))

# Short labels for the 21 zones (strips " LMP" suffix, abbreviates)
ZONE_MAP = {
    "Allegheny Power System LMP":                   "APS",
    "American Electric Power Co., Inc LMP":         "AEP",
    "American Transmission Systems, Inc LMP":       "ATSI",
    "Atlantic Electric Company LMP":                "AEC",
    "Baltimore Gas and Electric Company LMP":       "BGE",
    "ComEd LMP":                                    "ComEd",
    "Dayton Power and Light Company LMP":           "DAY",
    "Delmarva Power and Light LMP":                 "DPL",
    "Dominion Energy LMP":                          "DOM",
    "Duke Energy Ohio/Kentucky LMP":                "DEOK",
    "Duquesne Light LMP":                           "DUQ",
    "East Kentucky Power Coop LMP":                 "EKPC",
    "Jersey Central Power and Light Company LMP":   "JCPL",
    "Metropolitan Edison Company LMP":              "MetEd",
    "Ohio Valley Electric LMP":                     "OVEC",
    "PECO Energy LMP":                              "PECO",
    "PJM Total LMP":                                "PJM",
    "PPL Electric Utilities LMP":                   "PPL",
    "Pennsylvania Electric LMP":                    "PenE",
    "Potomac Electric Power LMP":                   "PEPCO",
    "Public Service Electric and Gas Company LMP":  "PSEG",
    "Rockland Electric Company LMP":                "RECO",
}

CONG_MAP = {k.replace(" LMP", " (Congestion)"): v + "_cong"
            for k, v in ZONE_MAP.items()}


def fetch_year(year: int) -> pd.DataFrame | None:
    url = f"https://www.eia.gov/electricity/wholesalemarkets/csv/pjm_lmp_da_hr_zones_{year}.csv"
    try:
        r = requests.get(url, timeout=120)
        r.raise_for_status()
    except Exception as e:
        print(f"  {year}: download failed — {e}")
        return None

    lmp_cols  = list(ZONE_MAP.keys())
    cong_cols = list(CONG_MAP.keys())
    use_cols  = ["Local Date", "Hour Number"] + lmp_cols + cong_cols

    df = pd.read_csv(
        io.BytesIO(r.content),
        skiprows=3,
        usecols=lambda c: c in use_cols,
        low_memory=False,
    )
    df["Local Date"] = pd.to_datetime(df["Local Date"], errors="coerce")
    df = df.dropna(subset=["Local Date"])

    for col in lmp_cols + cong_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.rename(columns={**ZONE_MAP, **CONG_MAP, "Local Date": "date"})
    print(f"  {year}: {df['date'].min().date()} to {df['date'].max().date()} "
          f"({len(df):,} hourly rows)")
    return df


def daily_agg(hourly: pd.DataFrame) -> pd.DataFrame:
    lmp_zones  = list(ZONE_MAP.values())
    cong_zones = [v + "_cong" for v in ZONE_MAP.values()]
    all_zones  = [z for z in lmp_zones + cong_zones if z in hourly.columns]

    daily = (
        hourly.groupby("date")[all_zones]
        .agg(["mean", "count"])
        .reset_index()
    )
    # Flatten multiindex
    daily.columns = [
        "_".join(c).strip("_") if c[1] else c[0]
        for c in daily.columns
    ]
    # Keep only days with >= 20 hourly obs for the PJM total column
    count_col = "PJM_count" if "PJM_count" in daily.columns else None
    if count_col:
        daily = daily[daily[count_col] >= 20]
    return daily


def main():
    all_hourly = []
    for yr in YEARS:
        print(f"Fetching {yr}...")
        df = fetch_year(yr)
        if df is not None:
            all_hourly.append(df)

    if not all_hourly:
        sys.exit("No data downloaded.")

    hourly = pd.concat(all_hourly, ignore_index=True)
    print(f"\nTotal hourly rows: {len(hourly):,}")

    print("Aggregating to daily...")
    daily = daily_agg(hourly)

    out = DATA_DIR / "pjm_zones_daily.csv"
    daily.to_csv(out, index=False)
    print(f"Saved {len(daily):,} daily rows to {out.name}")
    print(f"Range: {daily['date'].min().date()} to {daily['date'].max().date()}")
    print(f"Columns: {len(daily.columns)}")

    # Quick summary: average LMP by zone across full period
    lmp_means = {z: daily[f"{z}_mean"].mean() for z in ZONE_MAP.values()
                 if f"{z}_mean" in daily.columns}
    print("\nAverage day-ahead LMP by zone (full period):")
    for zone, val in sorted(lmp_means.items(), key=lambda x: x[1]):
        print(f"  {zone:8s}  ${val:6.2f}/MWh")


if __name__ == "__main__":
    main()
