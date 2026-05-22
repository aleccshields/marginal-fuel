# The Number Behind the Gas Bill

*A weekly regression, 238 observations, and one finding that cuts against the obvious story.*

---

Post 1 described the mechanism: gas-fired plants set the clearing price in PJM, so a Henry Hub spike lands on electricity buyers. The claim was $5 to $6 per megawatt-hour for every dollar increase in gas. This post shows the regression that produces that number, what the data say about whether AI data center growth has changed it, and why the more important result is the one that doesn't involve the transmission coefficient at all.

---

## The data

The panel covers 238 weeks: September 2020 through June 2025. Two public sources, no cost:

- **Henry Hub spot price** — FRED series DHHNGSP, daily averages aggregated to weekly. Free API key from the St. Louis Fed.
- **PJM Dominion Zone day-ahead LMPs** — EIA annual CSV files, hourly observations aggregated to daily then weekly. No account required.

The LMP series includes the congestion component separately, which becomes relevant in M2 below. Gas prices are in $/MMBtu; electricity in $/MWh.

The panel splits 119 weeks pre-2023 and 119 post. ChatGPT launched November 2022; hyperscaler data center capex inflected sharply through 2023. The January 2023 breakpoint is a reasonable place to test for a structural change.

---

## The baseline result

The scatter below places each week as a point: Henry Hub on the horizontal axis, Dominion Zone LMP on the vertical. Pre-2023 observations in gray; 2023-present in red. Fit lines for each period are annotated with their slopes.

*[Figure 2: Gas Price vs. Dominion Zone LMP — pre-2023 vs. 2023-present]*

M1 regresses weekly changes in LMP on weekly changes in Henry Hub, with winter and summer dummies included. The coefficient is **5.61 $/MWh per $/MMBtu** (p<0.01, HAC standard errors, Newey-West 4 lags). R² of 0.28.

First-differencing removes the shared nominal trend in both series, so this R² measures how much of the week-to-week *change* in electricity prices is explained by the week-to-week change in gas prices. Roughly 28% is a meaningful share for a differenced specification. The $5-6 range from Post 1 holds.

---

## Does the AI era change the slope?

The rolling beta chart below plots the 52-week price transmission coefficient through the full sample. The shaded band is the 95% confidence interval.

*[Figure 3: Rolling Price Transmission Coefficient (52-week window)]*

M3 adds an interaction term: Henry Hub change multiplied by a post-2022 indicator. If data center load were tightening the gas-to-power link — pulling more gas generation online to serve new demand, and making the system more exposed to gas price shocks — the interaction coefficient should be positive and significant.

The baseline coefficient in M3 is 6.18 (p<0.01). The post-AI interaction is -4.04 and statistically indistinguishable from zero. The rolling beta confirms it: transmission is noisy across the full sample with no sustained upward break after January 2023.

This is the finding most people expect to see. It is not there.

---

## What the congestion component shows

The heatmap below maps the Dominion Zone congestion component by year and week. Red cells are high-congestion weeks; green is negative congestion.

*[Figure 4: Dominion Zone Congestion Component — year × week heatmap]*

M2 regresses weekly changes in the congestion component on weekly Henry Hub changes. The coefficient is 0.15 and insignificant. In this data, gas price movements do not predict the congestion component of Dominion Zone LMPs.

The likely reason: Henry Hub reflects supply basin prices in Louisiana and Appalachia. The more proximate signal for grid congestion is the Transco basis spread — the premium mid-Atlantic buyers pay above Henry Hub when pipeline capacity binds. When Transco is constrained, gas can't reach the generators that need it, which shows up in both the basis spread and the congestion component simultaneously. Daily Transco basis data isn't freely available, which is why this analysis uses Henry Hub as the gas price variable. The M2 null is a data limitation rather than evidence that pipeline constraints don't affect congestion.

---

## The finding that matters

M4 switches from first differences to log-levels, regressing log Dominion Zone LMP on log Henry Hub plus seasonal dummies and a linear year trend. The elasticity is **0.885** (p<0.01): a 10% increase in Henry Hub is associated with roughly a 9% increase in wholesale electricity prices. R² of 0.73 — though this is a higher bar to compare to M1's 0.28, since level models absorb shared trends that difference models strip out.

The year trend coefficient is **0.097** (p<0.01). Holding gas prices and seasonality constant, Dominion Zone LMPs have risen roughly 10% per year in nominal terms over the sample period.

That trend cannot be attributed to any single cause. Coal plant retirements raise the marginal cost of generation by pushing dispatch up the supply curve toward less efficient units. Transmission constraints bind more often as load grows. Data center demand in Northern Virginia added thousands of megawatts of contracted load in a short period. General cost inflation runs through both fuel and non-fuel O&M. The regression separates out gas prices and seasonality; everything else goes into the trend.

What the data does show is this: the AI-era demand shock is not appearing as stronger sensitivity to gas price changes. It's appearing as a higher price floor. The transmission coefficient measures how a gas price shock propagates through the system; it's the variable relevant for hedging and short-run procurement. The year trend measures the baseline electricity price level under sustained demand pressure; that's the variable that matters for long-run power purchase agreements and the internal rate of return on new capacity investment.

---

## Regression table

Full output is in the repository. Key coefficients:

| | M1 d(LMP) | M2 d(Cong) | M3 d(LMP) | M4 log(LMP) |
|---|---|---|---|---|
| delta HH ($/MMBtu) | 5.61*** | 0.15 | 6.18*** | — |
| delta HH × Post-AI | — | — | -4.04 | — |
| log Henry Hub | — | — | — | 0.885*** |
| Year trend | — | — | — | 0.097*** |
| Seasonal controls | Yes | Yes | Yes | Yes |
| N | 237 | 237 | 237 | 238 |
| R² | 0.28 | 0.01 | 0.28 | 0.73 |

HAC standard errors (Newey-West, 4 lags). \* p<.10 \*\* p<.05 \*\*\* p<.01

---

## What's next

Post 3 moves from price transmission to the regulatory constraint that prevents supply from closing the gap. FERC's certificate policy governs new interstate gas pipeline capacity. The 2022 policy revision made approvals more contested. The Northeast Supply Enhancement has been caught in that process for years while Northern Virginia's load keeps climbing.

Data and code are on GitHub.

---

*Marginal Fuel covers energy markets, regulation, and the economics of the grid.*
