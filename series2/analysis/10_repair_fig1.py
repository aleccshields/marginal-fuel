"""
Marginal Fuel -- Series 3 -- Post 10 -- Figure 1
Withdrawal rate by entry cohort, 2010-2020

Shows the worsening trend: recent cohorts withdraw at 90%+ vs. 70-75% for 2010-2015.

Source:
  LBNL Queued Up, data through 2024
    Data file: data/lbnl_ix_queue_data_file_thru2024_v2.xlsx
    Sheet: "03. Complete Queue Data" (header row 1)

Methodology: withdrawal rate = withdrawn_MW / (withdrawn_MW + operational_MW)
Active and suspended excluded from denominator (not yet resolved).
Cohorts 2021+ excluded: too few resolved projects for reliable rate.
Cohorts 2015+ shown with lighter bars to flag lower resolved-GW coverage.

Output: series3/posts/figures/fig10_01_withdrawal_trend.png
Run from repo root: python series3/analysis/10_repair_fig1.py
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

ROOT    = Path(__file__).parent.parent.parent
DATA    = ROOT / "data"
FIG_DIR = Path(__file__).parent.parent / "posts" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

LBNL_FILE       = DATA / "lbnl_ix_queue_data_file_thru2024_v2.xlsx"
SHEET           = "03. Complete Queue Data"
ENTRY_YEARS     = list(range(2010, 2021))
MIN_RESOLVED_GW = 0.5


def load_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        sys.exit(f"\nData file not found: {path}\n"
                 "Download from: emp.lbl.gov/publications/queued-characteristics-power-plants\n")
    df = pd.read_excel(path, sheet_name=SHEET, header=1)
    df["mw"]     = pd.to_numeric(df["mw1"],    errors="coerce")
    df["q_year"] = pd.to_numeric(df["q_year"], errors="coerce")
    return df.dropna(subset=["mw", "q_year"])


def calc_rates(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for yr in ENTRY_YEARS:
        cohort  = df[df["q_year"] == yr]
        wd_mw   = cohort.loc[cohort["q_status"] == "withdrawn",    "mw"].sum()
        op_mw   = cohort.loc[cohort["q_status"] == "operational",  "mw"].sum()
        res_mw  = wd_mw + op_mw
        if res_mw / 1_000 < MIN_RESOLVED_GW:
            continue
        rows.append({
            "year":            yr,
            "withdrawal_rate": wd_mw / res_mw * 100,
            "resolved_gw":     res_mw / 1_000,
        })
    return pd.DataFrame(rows)


def chart(rates: pd.DataFrame) -> None:
    plt.rcParams.update({
        "font.family": "serif",
        "font.size":   11,
        "axes.spines.top":   False,
        "axes.spines.right": False,
        "figure.dpi":  120,
    })

    fig, ax = plt.subplots(figsize=(11, 6))
    fig.subplots_adjust(bottom=0.20)

    # Color: darker for well-resolved cohorts, lighter for recent (fewer resolved)
    colors = []
    for _, row in rates.iterrows():
        colors.append("#c0392b" if row["resolved_gw"] >= 5.0 else "#e8a49a")

    bars = ax.bar(rates["year"], rates["withdrawal_rate"],
                  color=colors, alpha=0.88, width=0.65)

    ax.axhline(85, color="#555", lw=0.8, ls="--", alpha=0.6)
    ax.text(rates["year"].max() + 0.15, 86.5, "85%", fontsize=8.5, color="#555")

    for bar, (_, row) in zip(bars, rates.iterrows()):
        ax.text(bar.get_x() + bar.get_width() / 2,
                row["withdrawal_rate"] + 1.2,
                f"{row['withdrawal_rate']:.0f}%",
                ha="center", va="bottom", fontsize=8.5)

    # Legend
    solid  = mpatches.Patch(color="#c0392b", alpha=0.88, label="≥5 GW resolved (higher confidence)")
    faded  = mpatches.Patch(color="#e8a49a", alpha=0.88, label="<5 GW resolved (fewer resolved projects)")
    ax.legend(handles=[solid, faded], fontsize=8.5, framealpha=0.9, loc="upper left")

    ax.set_xlabel("Queue entry year", fontsize=11)
    ax.set_ylabel("Withdrawal rate (% of resolved GW)", fontsize=11)
    ax.set_title(
        "Interconnection Queue: Withdrawal Rate by Entry Cohort, 2010–2020\n"
        "(share of withdrawn + operational GW that withdrew, as of end 2024)",
        fontsize=11,
    )
    ax.set_ylim(0, 115)
    ax.set_xticks(rates["year"])
    ax.set_xticklabels(rates["year"].astype(int), fontsize=10)

    fig.text(
        0.5, 0.04,
        "Source: LBNL Queued Up, data through 2024.  "
        "Cohorts 2021+ excluded (insufficient resolved projects).  "
        "Resolved = withdrawn + operational; active/suspended excluded.",
        ha="center", fontsize=7.5, color="gray",
    )

    out = FIG_DIR / "fig10_01_withdrawal_trend.png"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out}")


if __name__ == "__main__":
    df    = load_data(LBNL_FILE)
    rates = calc_rates(df)
    print("Withdrawal rates by entry year:")
    print(rates.to_string(index=False))
    chart(rates)
