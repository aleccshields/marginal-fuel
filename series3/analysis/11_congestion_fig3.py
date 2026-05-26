"""
Marginal Fuel -- Series 3 -- Post 11 -- Figure 3
Congestion component: which zones bear the highest constraint costs

The LMP congestion component isolates transmission-constraint costs from
energy price differences. A positive congestion component means the zone
pays above the energy price because power cannot flow freely into it.
The annual average congestion component per zone reveals the structural
nature of each constraint: zones with persistently positive congestion
components are import-constrained by physical transmission limits.

Requires: data/pjm_zones_daily.csv (from 11_fetch_pjm_zones.py)
Output:   series3/posts/figures/fig11_03_congestion_component.png
Run from repo root: python series3/analysis/11_congestion_fig3.py
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent.parent / "data"
FIG_DIR  = Path(__file__).parent.parent / "posts" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

WEST_ZONES = {"ComEd", "AEP", "ATSI", "DEOK", "DAY", "EKPC", "OVEC", "DUQ", "APS"}
EAST_ZONES = {"BGE", "DOM", "PEPCO", "PSEG", "JCPL", "PECO", "AEC", "DPL", "PPL",
              "MetEd", "PenE", "RECO"}
OMIT       = {"PJM"}


def load() -> pd.DataFrame:
    path = DATA_DIR / "pjm_zones_daily.csv"
    if not path.exists():
        sys.exit(f"Data not found: {path}\nRun 11_fetch_pjm_zones.py first.")
    df = pd.read_csv(path, parse_dates=["date"])
    df = df[df["date"].dt.year.between(2021, 2024)]
    return df


def congestion_by_zone_year(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["year"] = df["date"].dt.year

    cong_cols = [c for c in df.columns
                 if c.endswith("_cong_mean")
                 and c.replace("_cong_mean", "") not in OMIT]

    zones = [c.replace("_cong_mean", "") for c in cong_cols]

    records = []
    for zone, col in zip(zones, cong_cols):
        annual = df.groupby("year")[col].mean().reset_index()
        annual.columns = ["year", "congestion"]
        annual["zone"] = zone
        records.append(annual)

    return pd.concat(records, ignore_index=True)


def chart(cong: pd.DataFrame) -> None:
    plt.rcParams.update({
        "font.family": "serif",
        "font.size": 11,
        "axes.spines.top":   False,
        "axes.spines.right": False,
        "figure.dpi": 120,
    })

    years = sorted(cong["year"].unique())
    # Average across years for sorting
    zone_avg = (
        cong.groupby("zone")["congestion"]
        .mean()
        .sort_values()
    )
    zones = zone_avg.index.tolist()

    fig, axes = plt.subplots(1, len(years), figsize=(12, 7), sharey=True)
    fig.subplots_adjust(left=0.14, right=0.93, top=0.88, bottom=0.18,
                        wspace=0.08)

    col_map = {
        "pos_strong": "#c0392b",
        "pos_light":  "#e8a090",
        "neg_light":  "#a0c4e8",
        "neg_strong": "#2471a3",
    }

    def bar_color(val):
        if val > 2:
            return col_map["pos_strong"]
        elif val > 0:
            return col_map["pos_light"]
        elif val > -2:
            return col_map["neg_light"]
        else:
            return col_map["neg_strong"]

    for ax, yr in zip(axes, years):
        sub = cong[cong["year"] == yr].set_index("zone")["congestion"]
        vals = [sub.get(z, 0) for z in zones]
        colors = [bar_color(v) for v in vals]
        ax.barh(zones, vals, color=colors, alpha=0.9, height=0.7)
        ax.axvline(0, color="#999", lw=0.7)
        ax.set_title(str(yr), fontsize=10, pad=6)
        ax.set_xlabel("$/MWh", fontsize=8.5)
        ax.tick_params(axis="y", labelsize=8.5)
        if ax != axes[0]:
            ax.tick_params(axis="y", left=False)

    axes[0].set_ylabel("PJM Zone", fontsize=10)

    # Shared title
    fig.suptitle(
        "PJM Congestion Component by Zone, 2021–2024\n"
        "Average daily LMP congestion component ($/MWh) — positive = import-constrained",
        fontsize=11, y=0.97,
    )

    pos_p  = mpatches.Patch(color=col_map["pos_strong"], alpha=0.9,
                             label="Positive (import-constrained, >$2/MWh)")
    pos_lp = mpatches.Patch(color=col_map["pos_light"],  alpha=0.9,
                             label="Positive ($0–$2/MWh)")
    neg_lp = mpatches.Patch(color=col_map["neg_light"],  alpha=0.9,
                             label="Negative ($0 to −$2/MWh)")
    neg_p  = mpatches.Patch(color=col_map["neg_strong"], alpha=0.9,
                             label="Negative (export-constrained, <−$2/MWh)")
    fig.legend(handles=[pos_p, pos_lp, neg_lp, neg_p],
               loc="lower center", ncol=2, fontsize=8, bbox_to_anchor=(0.5, 0.0),
               framealpha=0.9)

    fig.text(
        0.5, 0.10,
        "Source: EIA, PJM day-ahead hourly zonal LMPs, 2021–2024. "
        "Congestion component = LMP minus energy and loss components. "
        "Positive values indicate the zone pays a premium due to binding transmission constraints. "
        "Negative values indicate the zone has excess generation that cannot be exported.",
        ha="center", fontsize=7.5, color="gray",
    )

    out = FIG_DIR / "fig11_03_congestion_component.png"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out}")


if __name__ == "__main__":
    df   = load()
    cong = congestion_by_zone_year(df)
    print("Average congestion component by zone (2021-2024, $/MWh):")
    summary = cong.groupby("zone")["congestion"].mean().sort_values()
    for z, v in summary.items():
        tag = "E" if z in EAST_ZONES else "W" if z in WEST_ZONES else "?"
        print(f"  [{tag}] {z:8s}  {v:+.2f}")
    chart(cong)
