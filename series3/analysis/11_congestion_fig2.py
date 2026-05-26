"""
Marginal Fuel -- Series 3 -- Post 11 -- Figure 2
Annual BGE–ComEd and DOM–ComEd price spreads, 2021-2024

The BGE–ComEd spread is the most direct observable proxy for congestion
on the PJM east-west seam. A persistent, positive spread means the
transmission constraint is not being resolved. If it were, the spread
would converge to near zero (only loss differences would remain).

Requires: data/pjm_zones_daily.csv (from 11_fetch_pjm_zones.py)
Output:   series3/posts/figures/fig11_02_spread_persistence.png
Run from repo root: python series3/analysis/11_congestion_fig2.py
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent.parent / "data"
FIG_DIR  = Path(__file__).parent.parent / "posts" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

# Corridor pairs to track: (expensive zone, cheap zone, label)
CORRIDORS = [
    ("BGE",   "ComEd", "BGE – ComEd\n(Baltimore → Chicago)"),
    ("DOM",   "ComEd", "DOM – ComEd\n(Virginia → Chicago)"),
    ("PEPCO", "ComEd", "PEPCO – ComEd\n(DC → Chicago)"),
    ("PSEG",  "ComEd", "PSEG – ComEd\n(NJ → Chicago)"),
]

COLORS = ["#c0392b", "#e67e22", "#8e44ad", "#2471a3"]


def load() -> pd.DataFrame:
    path = DATA_DIR / "pjm_zones_daily.csv"
    if not path.exists():
        sys.exit(f"Data not found: {path}\nRun 11_fetch_pjm_zones.py first.")
    df = pd.read_csv(path, parse_dates=["date"])
    df = df[df["date"].dt.year.between(2021, 2024)]
    return df


def annual_spreads(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["year"] = df["date"].dt.year
    records = []
    for hi, lo, label in CORRIDORS:
        hi_col, lo_col = f"{hi}_mean", f"{lo}_mean"
        if hi_col not in df.columns or lo_col not in df.columns:
            continue
        df["spread"] = df[hi_col] - df[lo_col]
        annual = df.groupby("year")["spread"].mean().reset_index()
        annual["corridor"] = label
        annual["hi_zone"]  = hi
        annual["lo_zone"]  = lo
        records.append(annual)
    return pd.concat(records, ignore_index=True)


def chart(spreads: pd.DataFrame) -> None:
    plt.rcParams.update({
        "font.family": "serif",
        "font.size": 11,
        "axes.spines.top":   False,
        "axes.spines.right": False,
        "figure.dpi": 120,
    })

    years = sorted(spreads["year"].unique())
    x = range(len(years))

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.subplots_adjust(bottom=0.20, right=0.72)

    for i, (hi, lo, label) in enumerate(CORRIDORS):
        sub = spreads[spreads["hi_zone"] == hi].sort_values("year")
        if sub.empty:
            continue
        ax.plot(x, sub["spread"].values, marker="o", color=COLORS[i],
                linewidth=2, markersize=6, label=label, zorder=3)
        # Label final year value
        ax.text(len(years) - 0.1, sub["spread"].values[-1],
                f"${sub['spread'].values[-1]:.1f}",
                color=COLORS[i], fontsize=8.5, va="center", ha="left")

    ax.axhline(0, color="#bbb", lw=0.8, ls="--")
    ax.set_xticks(list(x))
    ax.set_xticklabels(years)
    ax.set_ylabel("Average annual LMP spread ($/MWh)", fontsize=11)
    ax.set_title(
        "PJM East–West Price Spread: Four Key Corridors\n"
        "Annual average day-ahead LMP differential vs. ComEd (Chicago)",
        fontsize=12,
    )
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"${v:.0f}"))
    ax.legend(
        loc="upper left", bbox_to_anchor=(1.01, 1.0),
        fontsize=8.5, framealpha=0.9, title="Corridor\n(expensive → cheap)",
        title_fontsize=8,
    )
    ax.set_ylim(bottom=0)

    fig.text(
        0.5, 0.04,
        "Source: EIA, PJM day-ahead hourly zonal LMPs, 2021–2024. "
        "Spread = expensive zone annual avg LMP minus ComEd annual avg LMP. "
        "A persistent positive spread indicates a binding transmission constraint between the two zones. "
        "Zero spread would indicate unconstrained transfer capacity.",
        ha="center", fontsize=7.5, color="gray", wrap=True,
    )

    out = FIG_DIR / "fig11_02_spread_persistence.png"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out}")


if __name__ == "__main__":
    df      = load()
    spreads = annual_spreads(df)
    print("Annual spreads ($/MWh):")
    pivot = spreads.pivot(index="year", columns="hi_zone", values="spread")
    print(pivot.to_string())
    chart(spreads)
