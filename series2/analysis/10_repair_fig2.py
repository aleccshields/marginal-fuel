"""
Marginal Fuel -- Series 3 -- Post 10 -- Figure 2
Queue entry volume by year with FERC Order 2023 timeline

Source:
  LBNL Queued Up, data through 2024
    Data file: data/lbnl_ix_queue_data_file_thru2024_v2.xlsx
    Sheet: "03. Complete Queue Data" (header row 1)

Shows the 38% drop in 2024 entries vs. 2023. FERC Order 2023 took effect
July 2024. Vertical markers note Order 2023 finalization (Dec 2023) and
effective date (July 2024). Three competing explanations noted in figure text.

Output: series3/posts/figures/fig10_02_entry_volume.png
Run from repo root: python series3/analysis/10_repair_fig2.py
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from pathlib import Path

ROOT    = Path(__file__).parent.parent.parent
DATA    = ROOT / "data"
FIG_DIR = Path(__file__).parent.parent / "posts" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

LBNL_FILE  = DATA / "lbnl_ix_queue_data_file_thru2024_v2.xlsx"
SHEET      = "03. Complete Queue Data"
PLOT_YEARS = list(range(2015, 2025))


def load_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        sys.exit(f"\nData file not found: {path}\n"
                 "Download from: emp.lbl.gov/publications/queued-characteristics-power-plants\n")
    df = pd.read_excel(path, sheet_name=SHEET, header=1)
    df["mw"]     = pd.to_numeric(df["mw1"],    errors="coerce")
    df["q_year"] = pd.to_numeric(df["q_year"], errors="coerce")
    return df.dropna(subset=["mw", "q_year"])


def entry_by_year(df: pd.DataFrame) -> pd.Series:
    return (
        df[df["q_year"].isin(PLOT_YEARS)]
        .groupby("q_year")["mw"]
        .sum()
        .div(1_000)
        .reindex(PLOT_YEARS, fill_value=0)
    )


def chart(gw: pd.Series) -> None:
    plt.rcParams.update({
        "font.family": "serif",
        "font.size":   11,
        "axes.spines.top":   False,
        "axes.spines.right": False,
        "figure.dpi":  120,
    })

    fig, ax = plt.subplots(figsize=(11, 6))
    fig.subplots_adjust(bottom=0.22)

    colors = ["#2471a3" if yr < 2024 else "#e67e22" for yr in PLOT_YEARS]
    ax.bar(PLOT_YEARS, gw, color=colors, alpha=0.85, width=0.65)

    # Order 2023 finalized Dec 2023; effective July 2024
    ax.axvline(2023.5, color="#c0392b", lw=1.2, ls="--", alpha=0.8)
    ax.text(2023.55, gw.max() * 0.95,
            "Order 2023\nfinalized\n(Dec 2023)",
            fontsize=7.5, color="#c0392b", va="top")

    # Label the 2024 bar
    ax.annotate(
        f"{gw[2024]:.0f} GW\n(−38% vs 2023)",
        xy=(2024, gw[2024]),
        xytext=(2023.1, gw[2024] + 60),
        fontsize=8.5, color="#e67e22",
        arrowprops=dict(arrowstyle="->", color="#e67e22", lw=1.1),
    )

    for yr, val in gw.items():
        ax.text(yr, val + 8, f"{val:.0f}", ha="center", va="bottom", fontsize=8)

    ax.set_xlabel("Year of queue entry", fontsize=11)
    ax.set_ylabel("New capacity entering queue (GW)", fontsize=11)
    ax.set_title(
        "U.S. Interconnection Queue: New Entries by Year, 2015–2024",
        fontsize=12,
    )
    ax.set_xticks(PLOT_YEARS)
    ax.set_xticklabels(PLOT_YEARS, rotation=45, ha="right", fontsize=9)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"{v:.0f}"))

    fig.text(
        0.5, 0.04,
        "Source: LBNL Queued Up, data through 2024.  "
        "2024 drop may reflect FERC Order 2023 readiness requirements (effective July 2024), "
        "higher interest rates reducing marginal project viability, or pipeline digestion after record 2023 entries.  "
        "Causal attribution requires additional years of data.",
        ha="center", fontsize=7.5, color="gray", wrap=True,
    )

    out = FIG_DIR / "fig10_02_entry_volume.png"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out}")


if __name__ == "__main__":
    df = load_data(LBNL_FILE)
    gw = entry_by_year(df)
    print("Queue entries by year (GW):")
    for yr, val in gw.items():
        print(f"  {yr}: {val:>6.0f} GW")
    chart(gw)
