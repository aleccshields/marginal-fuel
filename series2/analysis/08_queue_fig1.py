"""
Marginal Fuel -- Series 3 -- Figure 1
Gigawatts in U.S. interconnection queues by year vs. total installed U.S. capacity

Source:
  LBNL Queued Up, data through 2024
    emp.lbl.gov/publications/queued-characteristics-power-plants
    Data file: data/lbnl_ix_queue_data_file_thru2024_v2.xlsx
    Sheet: "03. Complete Queue Data" (header row 1)

  EIA Electric Power Annual, Table 3.1 (installed capacity, hardcoded below)
    eia.gov/electricity/annual/

GW in queue at year-end Y = projects that entered queue in year Y or earlier
and had not yet withdrawn or reached commercial operation by end of Y.
Suspended projects are counted as active.

Output: series3/posts/figures/fig01_queue_vs_installed.png

Run from repo root: python series3/analysis/08_queue_fig1.py
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
from pathlib import Path

ROOT    = Path(__file__).parent.parent.parent
DATA    = ROOT / "data"
FIG_DIR = Path(__file__).parent.parent / "posts" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

LBNL_FILE = DATA / "lbnl_ix_queue_data_file_thru2024_v2.xlsx"
SHEET     = "03. Complete Queue Data"

# EIA Electric Power Annual, Table 3.1 -- net summer capacity, all sectors (GW)
# 2020-2024: EIA Electric Power Monthly, Table 6.1 (2024 is preliminary)
EIA_INSTALLED_GW = {
    2010: 1039, 2011: 1054, 2012: 1063, 2013: 1072, 2014: 1081,
    2015: 1090, 2016: 1087, 2017: 1096, 2018: 1106, 2019: 1114,
    2020: 1125, 2021: 1144, 2022: 1181, 2023: 1220, 2024: 1260,
}

PLOT_YEARS = list(range(2010, 2025))


def excel_serial_to_year(series: pd.Series) -> pd.Series:
    dates = pd.to_datetime("1899-12-30") + pd.to_timedelta(
        pd.to_numeric(series, errors="coerce"), unit="D"
    )
    return dates.dt.year


def load_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        sys.exit(f"\nData file not found: {path}\n"
                 "Download from: emp.lbl.gov/publications/queued-characteristics-power-plants\n")

    df = pd.read_excel(path, sheet_name=SHEET, header=1)
    df["mw"]      = pd.to_numeric(df["mw1"],    errors="coerce")
    df["q_year"]  = pd.to_numeric(df["q_year"], errors="coerce")
    df["wd_year"] = excel_serial_to_year(df["wd_date"])
    df["on_year"] = excel_serial_to_year(df["on_date"])
    df = df.dropna(subset=["mw", "q_year"])
    print(f"Loaded {len(df):,} projects  |  {df['mw'].sum()/1000:,.0f} GW total")
    print(f"Status breakdown: {df['q_status'].value_counts().to_dict()}")
    return df


def queue_gw_by_year(df: pd.DataFrame) -> dict:
    result = {}
    for yr in PLOT_YEARS:
        mask = (
            (df["q_year"] <= yr) &
            (df["wd_year"].isna() | (df["wd_year"] > yr)) &
            (df["on_year"].isna() | (df["on_year"] > yr))
        )
        result[yr] = df.loc[mask, "mw"].sum() / 1_000
    return result


def chart(queue_gw: dict) -> None:
    years      = PLOT_YEARS
    queue_vals = [queue_gw[y] for y in years]
    inst_vals  = [EIA_INSTALLED_GW.get(y, float("nan")) for y in years]

    plt.rcParams.update({
        "font.family": "serif",
        "font.size": 11,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "figure.dpi": 120,
    })

    fig, ax = plt.subplots(figsize=(13, 6))
    fig.subplots_adjust(bottom=0.18)

    x = np.arange(len(years))
    w = 0.38

    ax.bar(x - w/2, queue_vals, w, color="#2471a3", alpha=0.85,
           label="GW in interconnection queues")
    ax.bar(x + w/2, inst_vals,  w, color="#aab7b8", alpha=0.75,
           label="Installed U.S. generating capacity")

    ax.set_xticks(x)
    ax.set_xticklabels(years, rotation=45, ha="right", fontsize=9)
    ax.set_ylabel("Gigawatts (GW)", fontsize=11)
    ax.set_title(
        "U.S. Interconnection Queue vs. Installed Generating Capacity, 2010–2024",
        fontsize=12,
    )
    ax.legend(fontsize=9, framealpha=0.9)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"{v:,.0f}"))

    fig.text(
        0.5, 0.04,
        "Sources: LBNL Queued Up, data through 2024 (queue); "
        "EIA Electric Power Annual / Monthly, Table 3.1 / 6.1 (installed capacity; 2024 preliminary).",
        ha="center", fontsize=7.5, color="gray",
    )

    out = FIG_DIR / "fig01_queue_vs_installed.png"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    print(f"\nSaved: {out}")


if __name__ == "__main__":
    df = load_data(LBNL_FILE)
    gw = queue_gw_by_year(df)
    print("\nQueue GW at year-end:")
    for yr, val in gw.items():
        inst = EIA_INSTALLED_GW.get(yr, 0)
        print(f"  {yr}: {val:>6,.0f} GW in queue  |  {inst} GW installed  |  ratio {val/inst:.1f}x")
    chart(gw)
