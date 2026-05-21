"""
Marginal Fuel -- Panel Construction
Merges gas price and LMP data into a weekly panel ready for regression.

Inputs (from 01_fetch_data.py):
  data/henry_hub_daily.csv   -- Henry Hub spot price from FRED
  data/pjm_dom_lmp_daily.csv -- Dominion Zone LMP + congestion from EIA

Output:
  data/panel_weekly.csv
"""

import pandas as pd
import numpy as np
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"


def load_henry_hub():
    df = pd.read_csv(DATA_DIR / "henry_hub_daily.csv", parse_dates=["date"])
    df = df[["date", "henry_hub"]].dropna()
    print(f"Henry Hub: {len(df)} daily obs ({df['date'].min().date()} to {df['date'].max().date()})")
    return df


def load_lmp_daily():
    df = pd.read_csv(DATA_DIR / "pjm_dom_lmp_daily.csv", parse_dates=["date"])
    print(f"Dominion LMP: {len(df)} daily obs ({df['date'].min().date()} to {df['date'].max().date()})")
    print(f"  Avg LMP: ${df['dom_lmp_mean'].mean():.2f}/MWh  |  Avg congestion: ${df['dom_congestion_mean'].mean():.2f}/MWh")
    return df


def build_weekly_panel(hh: pd.DataFrame, lmp: pd.DataFrame) -> pd.DataFrame:
    # Align both series to ISO week (Monday-start)
    hh["week"]  = hh["date"]  - pd.to_timedelta(hh["date"].dt.weekday,  unit="D")
    lmp["week"] = lmp["date"] - pd.to_timedelta(lmp["date"].dt.weekday, unit="D")

    hh_weekly = (
        hh.groupby("week")
        .agg(henry_hub=("henry_hub", "mean"), hh_obs=("henry_hub", "count"))
        .reset_index()
    )

    lmp_weekly = (
        lmp.groupby("week")
        .agg(
            dom_lmp=("dom_lmp_mean", "mean"),
            dom_congestion=("dom_congestion_mean", "mean"),
            dom_lmp_max=("dom_lmp_max", "mean"),
            lmp_obs=("dom_lmp_mean", "count"),
        )
        .reset_index()
    )

    panel = pd.merge(hh_weekly, lmp_weekly, on="week", how="inner")

    # Drop weeks with incomplete data
    panel = panel[(panel["hh_obs"] >= 4) & (panel["lmp_obs"] >= 5)].copy()
    panel = panel.sort_values("week").reset_index(drop=True)

    # -- Time features --
    panel["year"]  = panel["week"].dt.year
    panel["month"] = panel["week"].dt.month

    # Seasonal dummies (heating/cooling demand)
    panel["winter"] = panel["month"].isin([12, 1, 2]).astype(int)
    panel["summer"] = panel["month"].isin([6, 7, 8]).astype(int)

    # Post-2022 indicator -- AI data center demand acceleration
    # ChatGPT launched Nov 2022; hyperscaler capex inflected 2023+
    panel["post_ai"]    = (panel["year"] >= 2023).astype(int)
    panel["year_trend"] = panel["year"] - panel["year"].min()

    # -- First differences (for stationarity) --
    panel["d_henry_hub"]      = panel["henry_hub"].diff()
    panel["d_dom_lmp"]        = panel["dom_lmp"].diff()
    panel["d_dom_congestion"] = panel["dom_congestion"].diff()

    # -- Log-log for elasticity --
    panel["log_hh"]  = np.log(panel["henry_hub"].clip(lower=0.1))
    panel["log_lmp"] = np.log(panel["dom_lmp"].clip(lower=0.1))

    # -- Implied gas-to-power heat rate --
    # LMP ($/MWh) / gas price ($/MMBtu) ~ heat rate (MMBtu/MWh)
    # Efficient CCGT = ~7; peakers ~10
    panel["implied_heat_rate"] = panel["dom_lmp"] / panel["henry_hub"].clip(lower=0.1)

    out = DATA_DIR / "panel_weekly.csv"
    panel.to_csv(out, index=False)

    print(f"\nPanel built: {len(panel)} weeks")
    print(f"  Range: {panel['week'].min().date()} to {panel['week'].max().date()}")
    print(f"  Pre-AI weeks (2020-2022): {(panel['post_ai'] == 0).sum()}")
    print(f"  Post-AI weeks (2023+):    {(panel['post_ai'] == 1).sum()}")
    print(f"  Avg Henry Hub: ${panel['henry_hub'].mean():.2f}/MMBtu")
    print(f"  Avg Dominion LMP: ${panel['dom_lmp'].mean():.2f}/MWh")
    print(f"  Avg implied heat rate: {panel['implied_heat_rate'].mean():.1f} MMBtu/MWh")
    print(f"Saved to {out.name}")
    return panel


if __name__ == "__main__":
    hh    = load_henry_hub()
    lmp   = load_lmp_daily()
    panel = build_weekly_panel(hh, lmp)
    print("\nNext: run 03_regression_charts.py")
