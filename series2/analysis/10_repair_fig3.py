"""
Marginal Fuel -- Series 3 -- Post 10 -- Figure 3
Reform scorecard: which interventions address which failures

No external data required. Stated-assumption evaluation based on public
regulatory record (FERC Orders 2023, 2023-A, 1920) and academic literature.

Two problems from Posts 8 and 9:
  Problem 1 (Premium): Study deposits << development option value → speculative entry
  Problem 2 (Strike):  Upgrade costs unknowable at entry, cascade-unstable → withdrawal cascade

Each reform rated on: fixes Problem 1, fixes Problem 2, implementation status.
Rating scale: 0 = no effect, 1 = partial, 2 = addresses it.

Output: series3/posts/figures/fig10_03_reform_scorecard.png
Run from repo root: python series3/analysis/10_repair_fig3.py
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

FIG_DIR = Path(__file__).parent.parent / "posts" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

# Reforms and their ratings
REFORMS = [
    "FERC Order 2023:\nHigher deposits",
    "FERC Order 2023:\nReadiness milestones",
    "FERC Order 2023:\nCluster studies",
    "Value-indexed\ndeposits (proposed)",
    "Secondary market\nfor queue positions",
    "Early cost disclosure\npre-commitment",
    "Socialized upgrade costs\n(Order 1920 direction)",
]

# Scores: [Problem 1 (premium), Problem 2 (strike)]
# 0 = none, 1 = partial, 2 = addresses
SCORES = np.array([
    [1, 0],   # Higher deposits: partial on premium, nothing on strike
    [1, 0],   # Readiness milestones: partial on premium (harder to game), nothing on strike
    [0, 1],   # Cluster studies: nothing on premium, partial on strike (reduces sequential delay)
    [2, 0],   # Value-indexed deposits: addresses premium, nothing on strike
    [1, 0],   # Secondary market: partial on premium (reveals value), nothing on strike
    [0, 2],   # Early cost disclosure: nothing on premium, addresses strike
    [0, 2],   # Socialized costs: nothing on premium, addresses strike
])

STATUS = [
    "Enacted (July 2024)",
    "Enacted (July 2024)",
    "Enacted (July 2024)",
    "Proposed",
    "Proposed",
    "Proposed",
    "Partial (planned\ntransmission only)",
]

COLOR_MAP = {0: "#f0f0f0", 1: "#f39c12", 2: "#27ae60"}
STATUS_COLOR = {
    "Enacted (July 2024)": "#2471a3",
    "Proposed":            "#7f8c8d",
    "Partial (planned\ntransmission only)": "#e67e22",
}

LABELS = ["Reduces\nspeculative entry\n(Problem 1)", "Stabilizes\ncost assignment\n(Problem 2)"]


def chart() -> None:
    plt.rcParams.update({
        "font.family": "serif",
        "font.size":   10,
        "axes.spines.top":    False,
        "axes.spines.right":  False,
        "axes.spines.left":   False,
        "axes.spines.bottom": False,
        "figure.dpi": 120,
    })

    n_reforms = len(REFORMS)
    n_cols    = len(LABELS)

    fig, ax = plt.subplots(figsize=(10, 6.5))
    fig.subplots_adjust(left=0.38, right=0.78, top=0.88, bottom=0.10)
    ax.set_aspect("equal")
    ax.axis("off")

    cell_w, cell_h = 1.6, 0.9

    # Column headers
    for j, label in enumerate(LABELS):
        ax.text((j + 0.5) * cell_w, n_reforms * cell_h + 0.2,
                label, ha="center", va="bottom", fontsize=9, fontweight="bold")

    # Cells
    SCORE_LABEL = {0: "–", 1: "Partial", 2: "Yes"}
    for i, reform in enumerate(REFORMS):
        row = n_reforms - 1 - i
        # Reform label (left)
        ax.text(-0.15, (row + 0.5) * cell_h, reform,
                ha="right", va="center", fontsize=8.5)
        # Score cells
        for j in range(n_cols):
            score = SCORES[i, j]
            rect  = plt.Rectangle(
                (j * cell_w + 0.05, row * cell_h + 0.05),
                cell_w - 0.1, cell_h - 0.1,
                facecolor=COLOR_MAP[score], edgecolor="#cccccc", linewidth=0.8,
            )
            ax.add_patch(rect)
            ax.text((j + 0.5) * cell_w, (row + 0.5) * cell_h,
                    SCORE_LABEL[score],
                    ha="center", va="center", fontsize=9,
                    color="#1a1a1a" if score < 2 else "white", fontweight="bold")
        # Status (right)
        s_color = STATUS_COLOR.get(STATUS[i], "#7f8c8d")
        ax.text(n_cols * cell_w + 0.15, (row + 0.5) * cell_h,
                STATUS[i], ha="left", va="center", fontsize=7.5, color=s_color)

    ax.set_xlim(-3.8, n_cols * cell_w + 2.5)
    ax.set_ylim(-0.4, (n_reforms + 1) * cell_h)

    ax.set_title(
        "Interconnection Queue Reform Scorecard\n"
        "Which interventions address which failures",
        fontsize=11, pad=12,
    )

    # Legend
    none_p   = mpatches.Patch(color="#f0f0f0", label="No effect", ec="#ccc")
    partial_p = mpatches.Patch(color="#f39c12", label="Partial")
    yes_p    = mpatches.Patch(color="#27ae60", label="Addresses it")
    ax.legend(handles=[none_p, partial_p, yes_p],
              loc="lower center", bbox_to_anchor=(0.3, -0.06),
              fontsize=8, framealpha=0.9, ncol=3)

    fig.text(
        0.5, 0.01,
        "Assessment based on FERC Orders 2023 and 1920 regulatory record and public academic literature.  "
        "Problem 1 = deposit underpricing (Post 8). Problem 2 = floating-strike cost instability (Post 9).",
        ha="center", fontsize=7, color="gray",
    )

    out = FIG_DIR / "fig10_03_reform_scorecard.png"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out}")


if __name__ == "__main__":
    chart()
    print("\nReform scorecard generated (no external data required).")
