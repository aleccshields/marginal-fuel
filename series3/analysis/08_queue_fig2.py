"""
Marginal Fuel -- Series 3 -- Figure 2
Withdrawal rate by queue entry year

Source:
  LBNL Queued Up, data through 2024
    emp.lbl.gov/publications/queued-characteristics-power-plants
    Data file: data/lbnl_ix_queue_data_file_thru2024_v2.xlsx
    Sheet: "03. Complete Queue Data" (header row 1)

Withdrawal rate = withdrawn_GW / (withdrawn_GW + operational_GW) per entry-year cohort.
Active and suspended projects are excluded from the denominator (not yet resolved).
Recent cohorts (2019+) are dropped: too few projects have resolved to give reliable rates.

Output: series3/posts/figures/fig02_withdrawal_rates.png

Run from repo root: python series3/analysis/08_queue_fig2.py
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

ROOT    = Path(__file__).parent.parent.parent
DATA    = ROOT / "data"
FIG_DIR = Path(__file__).parent.parent / "posts" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

LBNL_FILE       = DATA / "lbnl_ix_queue_data_file_thru2024_v2.xlsx"
SHEET           = "03. Complete Queue Data"
ENTRY_YEARS     = list(range(2008, 2020))
MIN_RESOLVED_GW = 1.0


def load_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        sys.exit(f"\nData file not found: {path}\n"
                 "Download from: emp.lbl.gov/publications/queued-characteristics-power-plants\n")

    df = pd.read_excel(path, sheet_name=SHEET, header=1)
    df["mw"]     = pd.to_numeric(df["mw1"],    errors="coerce")
    df["q_year"] = pd.to_numeric(df["q_year"], errors="coerce")
    return df.dropna(subset=["mw", "q_year"])


def withdrawal_rates(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for yr in ENTRY_YEARS:
        cohort      = df[df["q_year"] == yr]
        wd_mw       = cohort.loc[cohort["q_status"] == "withdrawn",    "mw"].sum()
        comp_mw     = cohort.loc[cohort["q_status"] == "operational",  "mw"].sum()
        resolved_mw = wd_mw + comp_mw

        if resolved_mw / 1_000 < MIN_RESOLVED_GW:
            continue

        rows.append({
            "year":            yr,
            "withdrawn_gw":    wd_mw   / 1_000,
            "completed_gw":    comp_mw / 1_000,
            "resolved_gw":     resolved_mw / 1_000,
            "withdrawal_rate": wd_mw / resolved_mw * 100,
        })

    return pd.DataFrame(rows)


def chart(rates: pd.DataFrame) -> None:
    plt.rcParams.update({
        "font.family": "serif",
        "font.size": 11,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "figure.dpi": 120,
    })

    fig, ax = plt.subplots(figsize=(11, 6))
    fig.subplots_adjust(bottom=0.18)

    ax.bar(rates["year"], rates["withdrawal_rate"],
           color="#c0392b", alpha=0.80, width=0.65)

    ax.axhline(50, color="#555", lw=0.8, ls="--", alpha=0.6)
    ax.text(rates["year"].max() + 0.15, 51.5, "50%", fontsize=8.5, color="#555")

    for _, row in rates.iterrows():
        ax.text(row["year"], row["withdrawal_rate"] + 1.5,
                f"{row['withdrawal_rate']:.0f}%",
                ha="center", va="bottom", fontsize=8.5)

    ax.set_xlabel("Queue entry year", fontsize=11)
    ax.set_ylabel("Withdrawal rate (% of resolved GW)", fontsize=11)
    ax.set_title(
        "Interconnection Queue: Share of Resolved GW That Withdrew, by Entry Year\n"
        "(as of end of 2024)",
        fontsize=11,
    )
    ax.set_ylim(0, 110)
    ax.set_xticks(rates["year"])
    ax.set_xticklabels(rates["year"].astype(int), fontsize=10)

    note = (f"Resolved = withdrawn + operational. "
            f"Cohorts with under {MIN_RESOLVED_GW:.0f} GW resolved excluded (recent years).")
    fig.text(0.5, 0.04,
             f"Source: LBNL Queued Up, data through 2024. {note}",
             ha="center", fontsize=7.5, color="gray")

    out = FIG_DIR / "fig02_withdrawal_rates.png"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out}")


if __name__ == "__main__":
    df    = load_data(LBNL_FILE)
    rates = withdrawal_rates(df)
    print("\nWithdrawal rates by entry year:")
    print(rates[["year", "withdrawn_gw", "completed_gw", "withdrawal_rate"]].to_string(index=False))
    chart(rates)
