"""
Marginal Fuel -- Series 3 -- Post 9 -- Figure 1
Withdrawal phase distribution: share of withdrawn projects by study phase at withdrawal

Source:
  LBNL Queued Up, data through 2024
    Data file: data/lbnl_ix_queue_data_file_thru2024_v2.xlsx
    Sheet: "03. Complete Queue Data" (header row 1)

Regions included: CAISO, ERCOT, ISO-NE, MISO, NYISO, PJM (phase coverage >= 69%).
SPP (0% coverage) and Southeast/West (22-33%) excluded with note.

Phases ordered by study sequence. System Impact Study is where cost estimates first arrive.

Output: series3/posts/figures/fig09_01_withdrawal_phase.png

Run from repo root: python series3/analysis/09_strike_fig1.py
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

LBNL_FILE = DATA / "lbnl_ix_queue_data_file_thru2024_v2.xlsx"
SHEET     = "03. Complete Queue Data"

# Regions with reliable phase-at-withdrawal coverage (>= 69%)
REGIONS_INCLUDED = {"CAISO", "ERCOT", "ISO-NE", "MISO", "NYISO", "PJM"}

# Phases in study sequence order; SIS is where cost estimates first appear
PHASE_ORDER = [
    "Feasibility Study",
    "Cluster Study",
    "System Impact Study",
    "Facility Study",
    "IA Executed",
]

PHASE_COLORS = {
    "Feasibility Study":    "#aab7b8",
    "Cluster Study":        "#85c1e9",
    "System Impact Study":  "#c0392b",
    "Facility Study":       "#e67e22",
    "IA Executed":          "#27ae60",
}

UNKNOWN_PHASES = {
    "Withdrawn", "In Progress (unknown study)", "Suspended",
    "Not Started", "IA Pending",
}


def load_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        sys.exit(f"\nData file not found: {path}\n"
                 "Download from: emp.lbl.gov/publications/queued-characteristics-power-plants\n")
    df = pd.read_excel(path, sheet_name=SHEET, header=1)
    df["mw"] = pd.to_numeric(df["mw1"], errors="coerce")
    return df.dropna(subset=["mw"])


def phase_counts(df: pd.DataFrame) -> pd.Series:
    withdrawn = df[
        (df["q_status"] == "withdrawn") &
        (df["region"].isin(REGIONS_INCLUDED)) &
        (~df["IA_status_clean"].isin(UNKNOWN_PHASES))
    ]
    counts = withdrawn["IA_status_clean"].value_counts()
    # Keep only the study phases we care about
    counts = counts.reindex(PHASE_ORDER).fillna(0).astype(int)
    return counts


def chart(counts: pd.Series, total_region: int, total_known: int) -> None:
    plt.rcParams.update({
        "font.family": "serif",
        "font.size": 11,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "figure.dpi": 120,
    })

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.subplots_adjust(bottom=0.22)

    total = counts.sum()
    pct   = counts / total * 100
    colors = [PHASE_COLORS[p] for p in PHASE_ORDER]

    bars = ax.bar(PHASE_ORDER, pct, color=colors, alpha=0.88, width=0.55)

    for bar, val in zip(bars, pct):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            val + 0.8,
            f"{val:.1f}%",
            ha="center", va="bottom", fontsize=9,
        )

    # Annotate the SIS bar
    sis_idx = PHASE_ORDER.index("System Impact Study")
    ax.annotate(
        "Cost estimates\nfirst assigned here",
        xy=(sis_idx, pct["System Impact Study"]),
        xytext=(sis_idx + 0.55, pct["System Impact Study"] + 6),
        fontsize=8.5, color="#c0392b",
        arrowprops=dict(arrowstyle="->", color="#c0392b", lw=1.2),
    )

    ax.set_ylabel("Share of withdrawn projects (%)", fontsize=11)
    ax.set_xlabel("Study phase at withdrawal", fontsize=11)
    ax.set_title(
        "Where Projects Exit: Study Phase at Withdrawal\n"
        "(CAISO, ERCOT, ISO-NE, MISO, NYISO, PJM; projects with known phase)",
        fontsize=11,
    )
    ax.set_ylim(0, 50)
    ax.tick_params(axis="x", labelsize=9)

    coverage_pct = total_known / total_region * 100
    fig.text(
        0.5, 0.04,
        f"Source: LBNL Queued Up, data through 2024.  "
        f"N = {total_known:,} projects with known phase out of {total_region:,} withdrawn "
        f"in included regions ({coverage_pct:.0f}% coverage).  "
        f"SPP, Southeast, and West excluded (phase data <35%).",
        ha="center", fontsize=7.5, color="gray",
        wrap=True,
    )

    out = FIG_DIR / "fig09_01_withdrawal_phase.png"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out}")


if __name__ == "__main__":
    df = load_data(LBNL_FILE)

    region_withdrawn = df[
        (df["q_status"] == "withdrawn") & (df["region"].isin(REGIONS_INCLUDED))
    ]
    total_region = len(region_withdrawn)

    counts = phase_counts(df)
    total_known = int(counts.sum())

    print("Phase at withdrawal (included regions, known phase only):")
    total = counts.sum()
    for phase in PHASE_ORDER:
        n = counts[phase]
        print(f"  {phase:<30} {n:>5}  ({n/total*100:.1f}%)")
    print(f"\nKnown phase: {total_known:,} / {total_region:,} "
          f"({total_known/total_region*100:.0f}% coverage in included regions)")

    chart(counts, total_region, total_known)
