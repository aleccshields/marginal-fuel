"""
Marginal Fuel -- Series 3 -- Post 11 -- Figure 1
Average day-ahead LMP by PJM zone, 2021-2024 (full years only)

Shows the persistent west-to-east price gradient across PJM zones.
The spread between cheapest and most expensive zone is the transmission
constraint premium paid by consumers in congested areas.

Requires: data/pjm_zones_daily.csv (from 11_fetch_pjm_zones.py)
Output:   series3/posts/figures/fig11_01_zone_lmp.png
Run from repo root: python series3/analysis/11_congestion_fig1.py
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent.parent / "data"
FIG_DIR  = Path(__file__).parent.parent / "posts" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

# Geography: which side of the main PJM east-west seam
# Zones that are persistently import-constrained (positive congestion component)
CONSTRAINED = {"BGE", "DOM", "PEPCO", "APS", "DAY", "DEOK", "EKPC", "OVEC", "DUQ", "AEP"}
# Zones that are persistently export-constrained (negative congestion, stranded generation)
SURPLUS     = {"PECO", "AEC", "JCPL", "PSEG", "ComEd", "PPL", "DPL", "RECO", "MetEd", "PenE", "ATSI"}
OMIT        = {"PJM"}   # system-wide average, not a zone


def load() -> pd.DataFrame:
    path = DATA_DIR / "pjm_zones_daily.csv"
    if not path.exists():
        sys.exit(f"Data not found: {path}\nRun 11_fetch_pjm_zones.py first.")
    df = pd.read_csv(path, parse_dates=["date"])
    # Full calendar years only
    df = df[df["date"].dt.year.between(2021, 2024)]
    return df


def zone_averages(df: pd.DataFrame) -> pd.Series:
    zones = [c.replace("_mean", "") for c in df.columns
             if c.endswith("_mean") and not c.replace("_mean", "") in OMIT
             and not c.replace("_mean", "").endswith("_cong")]
    means = {z: df[f"{z}_mean"].mean() for z in zones if f"{z}_mean" in df.columns}
    return pd.Series(means).sort_values()


def chart(avgs: pd.Series) -> None:
    plt.rcParams.update({
        "font.family": "serif",
        "font.size": 11,
        "axes.spines.top":   False,
        "axes.spines.right": False,
        "figure.dpi": 120,
    })

    fig, ax = plt.subplots(figsize=(10, 7))
    fig.subplots_adjust(left=0.18, right=0.88, top=0.88, bottom=0.12)

    colors = []
    for zone in avgs.index:
        if zone in CONSTRAINED:
            colors.append("#c0392b")   # red — import-constrained (pays the toll)
        elif zone in SURPLUS:
            colors.append("#2471a3")   # blue — surplus/export-constrained
        else:
            colors.append("#7f8c8d")

    bars = ax.barh(avgs.index, avgs.values, color=colors, alpha=0.85, height=0.65)

    # Label each bar
    for bar, val in zip(bars, avgs.values):
        ax.text(val + 0.3, bar.get_y() + bar.get_height() / 2,
                f"${val:.1f}", va="center", ha="left", fontsize=8.5)

    # Annotate the spread
    lo, hi = avgs.iloc[0], avgs.iloc[-1]
    lo_name, hi_name = avgs.index[0], avgs.index[-1]
    spread = hi - lo
    ax.annotate(
        "",
        xy=(hi, len(avgs) - 0.5),
        xytext=(lo, len(avgs) - 0.5),
        arrowprops=dict(arrowstyle="<->", color="#555", lw=1.3),
    )
    ax.text((lo + hi) / 2, len(avgs) - 0.1,
            f"${spread:.1f}/MWh spread\n({lo_name} → {hi_name})",
            ha="center", va="bottom", fontsize=9, color="#333")

    ax.set_xlabel("Average day-ahead LMP ($/MWh, 2021–2024)", fontsize=11)
    ax.set_title(
        "PJM Zone Day-Ahead Prices: West–East Gradient\n"
        "Average locational marginal price, full years 2021–2024",
        fontsize=12,
    )
    ax.axvline(avgs.mean(), color="#999", lw=0.8, ls="--")
    ax.text(avgs.mean() + 0.2, -0.7, "PJM avg", color="#999", fontsize=8, va="top")

    surp_p = mpatches.Patch(color="#2471a3", alpha=0.85, label="Surplus zones (stranded generation, negative congestion component)")
    cons_p = mpatches.Patch(color="#c0392b", alpha=0.85, label="Constrained zones (import-limited, positive congestion component)")
    ax.legend(handles=[surp_p, cons_p], fontsize=9, loc="lower right")

    fig.text(
        0.5, 0.02,
        "Source: EIA, PJM day-ahead hourly zonal LMPs, 2021–2024. "
        "Constrained zones (red) carry a positive average congestion component — they pay above the system energy price because transmission cannot deliver enough power. "
        "Surplus zones (blue) carry a negative congestion component — they have generation that cannot reach constrained load centers.",
        ha="center", fontsize=7.5, color="gray",
    )

    out = FIG_DIR / "fig11_01_zone_lmp.png"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out}")


if __name__ == "__main__":
    df   = load()
    avgs = zone_averages(df)
    print("Zone averages (2021-2024):")
    for z, v in avgs.items():
        side = "C" if z in CONSTRAINED else "S" if z in SURPLUS else "?"
        print(f"  [{side}] {z:8s}  ${v:.2f}/MWh")
    print(f"\nSpread: ${avgs.iloc[-1] - avgs.iloc[0]:.2f}/MWh "
          f"({avgs.index[0]} to {avgs.index[-1]})")
    chart(avgs)
