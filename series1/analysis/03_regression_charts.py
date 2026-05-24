"""
Marginal Fuel -- Regression Analysis & Charts

Core analysis: how does Henry Hub gas price transmit into PJM Dominion Zone
electricity prices? Has the relationship strengthened in the AI data center
era (post-2022)?

We run four specifications:
  M1: Baseline price transmission (Henry Hub -> Dominion LMP)
  M2: Same model on the LMP congestion component
  M3: Interaction -- has transmission intensified post-AI?
  M4: Log-log elasticity (levels, not differences)

Charts saved to posts/figures/
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import statsmodels.api as sm
import statsmodels.formula.api as smf
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent.parent / "data"
FIG_DIR  = Path(__file__).parent.parent / "posts" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

C = {
    "gas":   "#c0392b",
    "power": "#2471a3",
    "cong":  "#8e44ad",
    "pre":   "#aab7b8",
    "post":  "#e74c3c",
}
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 120,
})


def load():
    return pd.read_csv(DATA_DIR / "panel_weekly.csv", parse_dates=["week"])


# ====================================================================
# REGRESSIONS
# ====================================================================

def run_models(panel: pd.DataFrame):
    clean = panel.dropna(subset=["d_dom_lmp", "d_henry_hub", "d_dom_congestion"]).copy()

    # M1: Total LMP on Henry Hub price, seasonal controls
    m1 = smf.ols(
        "d_dom_lmp ~ d_henry_hub + winter + summer",
        data=clean
    ).fit(cov_type="HAC", cov_kwds={"maxlags": 4})

    # M2: Congestion component on Henry Hub
    m2 = smf.ols(
        "d_dom_congestion ~ d_henry_hub + winter + summer",
        data=clean
    ).fit(cov_type="HAC", cov_kwds={"maxlags": 4})

    # M3: Structural break -- has transmission strengthened post-AI?
    m3 = smf.ols(
        "d_dom_lmp ~ d_henry_hub + d_henry_hub:post_ai + winter + summer",
        data=clean
    ).fit(cov_type="HAC", cov_kwds={"maxlags": 4})

    # M4: Log-log elasticity (levels, not differences)
    m4 = smf.ols(
        "log_lmp ~ log_hh + winter + summer + year_trend",
        data=panel.dropna(subset=["log_lmp", "log_hh"])
    ).fit(cov_type="HAC", cov_kwds={"maxlags": 4})

    return {"M1": m1, "M2": m2, "M3": m3, "M4": m4}, clean


def print_table(models: dict):
    print("\n" + "=" * 68)
    print("GAS-TO-POWER PRICE TRANSMISSION: PJM DOMINION ZONE")
    print("HAC standard errors (Newey-West, 4 lags)")
    print("=" * 68)
    print(f"{'Variable':<32} {'M1':>9} {'M2':>9} {'M3':>9} {'M4':>9}")
    print(f"{'':32} {'d(LMP)':>9} {'d(Cong)':>9} {'d(LMP)':>9} {'log(LMP)':>9}")
    print("-" * 68)

    vars_show = [
        ("d_henry_hub",         "delta HH ($/MMBtu)"),
        ("d_henry_hub:post_ai", "delta HH x Post-AI"),
        ("log_hh",              "log Henry Hub"),
        ("winter",              "Winter dummy"),
        ("summer",              "Summer dummy"),
        ("year_trend",          "Year trend"),
    ]

    def fmt(res, v):
        if v not in res.params:
            return f"{'':>9}"
        coef = res.params[v]
        pv   = res.pvalues[v]
        star = "***" if pv < .01 else "**" if pv < .05 else "*" if pv < .10 else ""
        return f"{coef:>6.3f}{star:<3}"

    for v, label in vars_show:
        row = f"{label:<32}"
        for name in ["M1", "M2", "M3", "M4"]:
            row += fmt(models[name], v)
        print(row)

    print("-" * 68)
    for name, res in models.items():
        print(f"  {name}  N={int(res.nobs):>3}  R2={res.rsquared:.3f}  Adj.R2={res.rsquared_adj:.3f}")

    print("\n* p<.10  ** p<.05  *** p<.01")

    m3 = models["M3"]
    beta_base = m3.params.get("d_henry_hub", np.nan)
    beta_ai   = m3.params.get("d_henry_hub:post_ai", np.nan)
    print(f"\nKEY FINDING:")
    print(f"  Baseline beta (pre-AI):    {beta_base:.3f} $/MWh per $/MMBtu")
    print(f"  Post-AI increment (M3):    {beta_ai:+.3f} $/MWh per $/MMBtu")
    print(f"  Post-AI total beta:        {beta_base + beta_ai:.3f} $/MWh per $/MMBtu")
    print(f"  Change (%):                {100 * beta_ai / beta_base:+.1f}%")
    print(f"  M4 elasticity (log-log):   {models['M4'].params.get('log_hh', np.nan):.3f}")
    print(f"  M4 year trend:             {models['M4'].params.get('year_trend', np.nan):.3f} log pts/yr")


# ====================================================================
# CHARTS
# ====================================================================

def chart_timeseries(panel: pd.DataFrame):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 7), sharex=True)

    ax1b = ax1.twinx()
    ax1.plot(panel["week"],  panel["dom_lmp"],   color=C["power"], lw=1.4, label="Dominion LMP ($/MWh)")
    ax1b.plot(panel["week"], panel["henry_hub"], color=C["gas"],   lw=1.4, ls="--", label="Henry Hub ($/MMBtu)")
    ax1.set_ylabel("Electricity Price ($/MWh)", color=C["power"])
    ax1b.set_ylabel("Gas Price ($/MMBtu)",      color=C["gas"])
    ax1.tick_params(axis="y", colors=C["power"])
    ax1b.tick_params(axis="y", colors=C["gas"])
    lines = ax1.get_lines() + ax1b.get_lines()
    ax1.legend(lines, [l.get_label() for l in lines], loc="upper left", fontsize=9)
    ax1.set_title("A. Dominion Zone LMP vs. Henry Hub Gas Price (Weekly)", fontsize=11)

    ax2.bar(panel["week"], panel["dom_congestion"], width=5,
            color=C["cong"], alpha=0.7, label="Congestion component ($/MWh)")
    ax2.axhline(0, color="black", lw=0.6)
    ax2.set_ylabel("Congestion LMP ($/MWh)", color=C["cong"])
    ax2.tick_params(axis="y", colors=C["cong"])
    ax2.set_title("B. Dominion Zone Congestion Component of LMP", fontsize=11)

    ai_start = pd.Timestamp("2023-01-01")
    for ax in [ax1, ax2]:
        ax.axvspan(ai_start, panel["week"].max(), alpha=0.07, color=C["post"])
        ax.axvline(ai_start, color=C["post"], lw=0.9, ls=":")

    ax1.text(ai_start + pd.Timedelta(weeks=2), ax1.get_ylim()[1] * 0.93,
             "AI era", fontsize=8.5, color=C["post"])

    ax2.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax2.xaxis.set_major_locator(mdates.YearLocator())
    fig.tight_layout(h_pad=2)
    path = FIG_DIR / "fig01_time_series.png"
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {path.name}")


def chart_scatter(panel: pd.DataFrame):
    pre  = panel[panel["post_ai"] == 0].dropna(subset=["henry_hub", "dom_lmp"])
    post = panel[panel["post_ai"] == 1].dropna(subset=["henry_hub", "dom_lmp"])

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(pre["henry_hub"],  pre["dom_lmp"],  alpha=0.4, s=22, color=C["pre"],  label=f"Pre-2023 (n={len(pre)})")
    ax.scatter(post["henry_hub"], post["dom_lmp"], alpha=0.6, s=26, color=C["post"], label=f"2023-present (n={len(post)})")

    for subset, color in [(pre, C["pre"]), (post, C["post"])]:
        z = np.polyfit(subset["henry_hub"], subset["dom_lmp"], 1)
        x = np.linspace(subset["henry_hub"].min(), subset["henry_hub"].max(), 100)
        ax.plot(x, np.polyval(z, x), color=color, lw=2)
        slope = z[0]
        ax.annotate(f"slope={slope:.1f}", xy=(x[-1], np.polyval(z, x[-1])),
                    fontsize=8.5, color=color, ha="left")

    ax.set_xlabel("Henry Hub Spot Price ($/MMBtu)", fontsize=10)
    ax.set_ylabel("Dominion Zone Weekly Avg LMP ($/MWh)", fontsize=10)
    ax.set_title("Gas Price vs. Electricity Price\nHas the slope steepened in the AI era?", fontsize=11)
    ax.legend(fontsize=9)
    fig.tight_layout()
    path = FIG_DIR / "fig02_scatter.png"
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {path.name}")


def chart_rolling_beta(panel: pd.DataFrame, clean: pd.DataFrame):
    window = 52
    betas, lo, hi, dates = [], [], [], []

    for i in range(window, len(clean)):
        chunk = clean.iloc[i - window: i]
        X = sm.add_constant(chunk[["d_henry_hub"]])
        y = chunk["d_dom_lmp"]
        try:
            res = sm.OLS(y, X).fit(cov_type="HAC", cov_kwds={"maxlags": 4})
            betas.append(res.params["d_henry_hub"])
            lo.append(res.conf_int().loc["d_henry_hub", 0])
            hi.append(res.conf_int().loc["d_henry_hub", 1])
            dates.append(clean.iloc[i]["week"])
        except Exception:
            pass

    dates_pd = pd.to_datetime(dates)
    fig, ax = plt.subplots(figsize=(11, 4))
    ax.fill_between(dates_pd, lo, hi, alpha=0.18, color=C["power"])
    ax.plot(dates_pd, betas, color=C["power"], lw=2,
            label="52-week rolling beta (95% HAC CI shaded)")
    ax.axhline(0, color="black", lw=0.7, ls="--")

    ai_start = pd.Timestamp("2023-01-01")
    ax.axvline(ai_start, color=C["post"], lw=1.0, ls=":")
    y_top = max(betas) if betas else 10
    ax.text(ai_start + pd.Timedelta(weeks=3), y_top * 0.88,
            "AI era\nbegins", fontsize=8.5, color=C["post"])

    ax.set_ylabel("beta: d(HH) -> d(Dom LMP)\n($/MWh per $/MMBtu change)", fontsize=10)
    ax.set_title("Rolling Price Transmission Coefficient\n"
                 "Has AI-era data center load strengthened the gas-to-power link?", fontsize=11)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.legend(fontsize=9)
    fig.tight_layout()
    path = FIG_DIR / "fig03_rolling_beta.png"
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {path.name}")


def chart_congestion_heatmap(panel: pd.DataFrame):
    df = panel.copy()
    df["week_of_year"] = df["week"].dt.isocalendar().week.astype(int)

    pivot = df.pivot_table(
        index="year", columns="week_of_year", values="dom_congestion", aggfunc="mean"
    )

    fig, ax = plt.subplots(figsize=(13, 4))
    im = ax.imshow(pivot.values, aspect="auto", cmap="RdYlGn_r", vmin=-5, vmax=25)
    ax.set_yticks(range(len(pivot.index)))
    ax.set_yticklabels(pivot.index.astype(int))
    ax.set_xlabel("Week of Year", fontsize=10)
    ax.set_ylabel("Year", fontsize=10)
    ax.set_title("Dominion Zone Congestion Component ($/MWh) by Week\n"
                 "Red = high congestion; green = negative (relieved)", fontsize=11)
    fig.colorbar(im, ax=ax, label="$/MWh", shrink=0.8)
    fig.tight_layout()
    path = FIG_DIR / "fig04_congestion_heatmap.png"
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {path.name}")


def chart_implied_heat_rate(panel: pd.DataFrame):
    """Implied heat rate over time: LMP / Henry Hub, proxy for marginal generator efficiency.
    Rising trend signals less efficient (peaker) units setting the price more often."""
    df = panel.dropna(subset=["implied_heat_rate"]).copy()
    df = df[df["implied_heat_rate"] > 0]

    # 12-week rolling median to smooth noise
    df["hr_smooth"] = df["implied_heat_rate"].rolling(12, center=True).median()

    fig, ax = plt.subplots(figsize=(11, 4.5))
    ax.scatter(df["week"], df["implied_heat_rate"], alpha=0.25, s=14,
               color=C["power"], label="Weekly implied heat rate")
    ax.plot(df["week"], df["hr_smooth"], color=C["power"], lw=2,
            label="12-week rolling median")

    # Reference lines for generator types
    ax.axhline(7,  color="gray", lw=0.9, ls="--")
    ax.axhline(10, color="gray", lw=0.9, ls=":")
    ax.text(df["week"].iloc[2], 7.15,  "CCGT (~7 MMBtu/MWh)",   fontsize=8, color="gray")
    ax.text(df["week"].iloc[2], 10.15, "Peaker (~10 MMBtu/MWh)", fontsize=8, color="gray")

    ai_start = pd.Timestamp("2023-01-01")
    ax.axvspan(ai_start, df["week"].max(), alpha=0.07, color=C["post"])
    ax.axvline(ai_start, color=C["post"], lw=0.9, ls=":")
    ax.text(ai_start + pd.Timedelta(weeks=2),
            ax.get_ylim()[1] * 0.93, "AI era", fontsize=8.5, color=C["post"])

    ax.set_ylabel("Implied Heat Rate (MMBtu/MWh)", fontsize=10)
    ax.set_title("Implied Gas-to-Power Heat Rate: Dominion Zone\n"
                 "Rising trend signals less efficient generators setting the marginal price", fontsize=11)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.legend(fontsize=9)
    fig.tight_layout()
    path = FIG_DIR / "fig05_implied_heat_rate.png"
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {path.name}")


if __name__ == "__main__":
    panel = load()
    print(f"Panel: {len(panel)} weeks")

    models, clean = run_models(panel)
    print_table(models)

    print("\nGenerating charts...")
    chart_timeseries(panel)
    chart_scatter(panel)
    chart_rolling_beta(panel, clean)
    chart_congestion_heatmap(panel)
    chart_implied_heat_rate(panel)

    print(f"\nAll figures in posts/figures/")
    print("Next: write Post 2 using these results.")
