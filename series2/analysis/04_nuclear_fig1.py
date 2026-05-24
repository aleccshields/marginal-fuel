"""
Zero Margin -- Figure 1
Henry Hub annual average price + U.S. nuclear commercial retirement timeline

Inputs:
  FRED_API_KEY env var (same key used in 01_fetch_data.py)

Output:
  posts/figures/fig01_nuclear_henry_hub.png

Nuclear retirement data is hardcoded from EIA Electric Power Monthly, Table 6.1.
Run this script any time to regenerate the figure with updated Henry Hub data.
"""

import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from pathlib import Path

FIG_DIR = Path(__file__).parent.parent / "posts" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

C = {
    "gas":    "#c0392b",
    "retire": "#2471a3",
}

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 120,
})

# U.S. commercial nuclear retirements by year (net MW)
# Source: EIA Electric Power Monthly, Table 6.1
# Excludes research/test reactors; San Onofre net capacity per EIA plant records
RETIREMENTS_MW = {
    2000: 0, 2001: 0, 2002: 0, 2003: 0, 2004: 0,
    2005: 0, 2006: 0, 2007: 0, 2008: 0, 2009: 0,
    2010: 0, 2011: 0, 2012: 0,
    2013: 3566,  # Crystal River 3 (860), Kewaunee (556), San Onofre 2+3 (2150)
    2014:  620,  # Vermont Yankee
    2015:    0,
    2016:  478,  # Fort Calhoun
    2017:    0,
    2018:  619,  # Oyster Creek
    2019: 1514,  # Pilgrim (677) + Three Mile Island Unit 1 (837)
    2020: 1030,  # Indian Point Unit 2
    2021: 1041,  # Indian Point Unit 3
    2022:  805,  # Palisades
    2023:    0,
    2024:    0,
    2025:    0,
}


def fetch_henry_hub_annual() -> pd.DataFrame:
    api_key = os.environ.get("FRED_API_KEY", "")
    if not api_key:
        raise EnvironmentError(
            "FRED_API_KEY not set.\n"
            "Windows: set FRED_API_KEY=your_key\n"
            "Mac/Linux: export FRED_API_KEY=your_key\n"
            "Get a free key at https://fred.stlouisfed.org/docs/api/api_key.html"
        )
    url = (
        "https://api.stlouisfed.org/fred/series/observations"
        "?series_id=DHHNGSP"
        "&observation_start=2000-01-01"
        f"&api_key={api_key}"
        "&file_type=json"
    )
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    obs = resp.json()["observations"]

    df = pd.DataFrame(obs)[["date", "value"]].copy()
    df["date"] = pd.to_datetime(df["date"])
    df["value"] = pd.to_numeric(df["value"], errors="coerce").dropna()
    df = df.dropna(subset=["value"])

    df["year"] = df["date"].dt.year
    annual = (
        df.groupby("year")["value"]
        .mean()
        .reset_index()
        .rename(columns={"value": "henry_hub"})
    )
    return annual


def chart_figure1(hh: pd.DataFrame) -> None:
    ret = pd.DataFrame(
        list(RETIREMENTS_MW.items()), columns=["year", "retired_mw"]
    ).assign(retired_gw=lambda d: d["retired_mw"] / 1000)

    years = list(range(2000, 2026))

    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(11, 7), gridspec_kw={"hspace": 0.5}
    )

    # ── Panel A: Henry Hub annual average ─────────────────────────────────
    hh_plot = hh[hh["year"].between(2000, 2025)]
    ax1.fill_between(hh_plot["year"], hh_plot["henry_hub"],
                     alpha=0.15, color=C["gas"])
    ax1.plot(hh_plot["year"], hh_plot["henry_hub"],
             color=C["gas"], lw=2, marker="o", ms=3.5, label="Henry Hub annual avg")

    # $3 reference line
    ax1.axhline(3, color="gray", lw=0.8, ls="--")
    ax1.text(2000.3, 3.3, "$3/MMBtu", fontsize=8, color="gray")

    # Shade low-gas era (2012–2020)
    ax1.axvspan(2012, 2020.5, alpha=0.07, color=C["retire"])
    ax1.text(2016, 7.2, "Low-gas era", fontsize=8.5, color=C["retire"], ha="center")

    ax1.set_xlim(1999.5, 2025.5)
    ax1.set_ylabel("Henry Hub Annual Avg ($/MMBtu)", fontsize=10)
    ax1.set_title("A. Henry Hub Natural Gas Price — Annual Average", fontsize=11)
    ax1.xaxis.set_major_locator(mticker.MultipleLocator(5))

    # ── Panel B: Nuclear retirements ──────────────────────────────────────
    ret_plot = ret[ret["year"].between(2000, 2025)]
    bars = ax2.bar(
        ret_plot["year"], ret_plot["retired_gw"],
        color=C["retire"], alpha=0.75, width=0.6
    )

    # Label non-zero bars
    for bar, (_, row) in zip(bars, ret_plot.iterrows()):
        if row["retired_gw"] > 0:
            ax2.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.04,
                f"{row['retired_gw']:.1f} GW",
                ha="center", fontsize=7.5, color=C["retire"]
            )

    # Shade same low-gas era
    ax2.axvspan(2012, 2020.5, alpha=0.07, color=C["retire"])

    ax2.set_xlim(1999.5, 2025.5)
    ax2.set_ylabel("Nuclear Capacity Retired (GW)", fontsize=10)
    ax2.set_title("B. U.S. Nuclear Commercial Retirements by Year", fontsize=11)
    ax2.xaxis.set_major_locator(mticker.MultipleLocator(5))

    fig.text(
        0.5, 0.005,
        "Sources: Henry Hub — FRED series DHHNGSP (St. Louis Fed); "
        "Retirements — EIA Electric Power Monthly, Table 6.1",
        ha="center", fontsize=8, color="gray"
    )

    path = FIG_DIR / "fig01_nuclear_henry_hub.png"
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {path.name}")


if __name__ == "__main__":
    print("Fetching Henry Hub annual data from FRED (2000–present)...")
    hh = fetch_henry_hub_annual()
    print(f"  {len(hh)} years ({hh['year'].min()}–{hh['year'].max()})")

    print("Generating Figure 1...")
    chart_figure1(hh)
    print("Done. Run from: python analysis/04_nuclear_fig1.py")
