# The Cost of Free Fuel

*Three Mile Island Unit 1 shut down on September 20, 2019. Constellation Energy cited mounting losses with no viable path to profitability. Five years later, on the same calendar date, Microsoft signed a 20-year power purchase agreement to bring it back. Constellation is spending roughly $1.6 billion to restart the 835-megawatt reactor; the Department of Energy added a $1 billion loan in late 2025. The plant that the market couldn't support in 2019 now requires $2.6 billion of capital to restart because one buyer needed what it produces, and no alternative resource could serve the same purpose.*

*This is the first post in Zero Margin, a series on the economics of firm, carbon-free power in a gas-priced electricity market.*

---

## The mechanism

Nuclear fuel costs roughly $7 to $9 per megawatt-hour of electricity produced. A natural gas combined-cycle plant running at a 7 MMBtu/MWh heat rate and $3/MMBtu gas pays roughly $21 per megawatt-hour in fuel alone. Nuclear's fuel cost is a third of that.

The fuel cost doesn't determine what the plant gets paid.

In PJM and other competitive wholesale markets, the hourly clearing price for electricity is set by the last unit dispatched to meet demand: the marginal generator. Nuclear plants have near-zero marginal cost. They always clear the market, dispatching at whatever price natural gas sets. In most hours, gas is at the margin. The locational marginal price therefore approximates gas price multiplied by a heat rate factor, and nuclear plants collect the full LMP regardless of their actual fuel cost.

When Henry Hub trades at $8/MMBtu and power clears at $50/MWh, a nuclear plant earns $50 against $7 to $9 in fuel cost. When Henry Hub falls below $3, the same plant earns $20 against unchanged fixed costs.

*[Figure 1: Henry Hub annual average price 2000–2025 and U.S. nuclear net retirements by year]*

---

## The retirement wave

Nuclear plants carry fixed costs that don't move with the market. NRC-mandated staffing levels, physical security infrastructure, periodic refueling outages, and deferred maintenance backlogs from decades of operation run $25 to $45 per megawatt-hour depending on the plant's age and configuration. Rate cases in a regulated utility environment covered those costs regardless of wholesale prices. Deregulation in the 1990s put nuclear plants into competitive markets. The cost structure stayed.

The shale revolution drove Henry Hub from above $8/MMBtu in 2008 to below $3 for most of the following decade. LMPs fell with gas prices. Plants that had been earning comfortable margins on a $50/MWh LMP found themselves earning $20 to $30/MWh against operating costs of $30 to $45/MWh.

Between 2013 and 2022, roughly 10 gigawatts of nuclear capacity retired in the United States. Several closures had plant-specific causes: San Onofre suffered steam generator failures; Crystal River sustained containment damage during a maintenance project. But most shared the same financial profile: a plant earning the gas LMP against a fixed cost structure the market couldn't cover.

The plants that survived held one of two characteristics: low enough operating costs to stay above water when LMPs compressed, or location in states that intervened before the closure decision became irreversible. Illinois, New Jersey, and New York each passed zero-emission credit programs to save specific plants from retirement. Those programs, and whether they produced measurable effects on regional electricity prices, are the subject of Post 2.

---

## What the LMP doesn't price

Fuel cost arithmetic understates what the market misses. Three things nuclear provides do not appear in the LMP.

**Reliability.** Nuclear plants run at roughly 92% capacity factor across the year, independent of weather, fuel delivery constraints, or gas price spikes. Wind runs at 35 to 40%; gas plant output depends on pipeline access. The prior series in this publication documented how Transco pipeline constraints spike the basis spread and push electricity prices higher on cold winter mornings. A nuclear plant 50 miles from load keeps generating through the same event.

**Carbon-free generation.** The LMP is indifferent to emissions. A gas plant and a nuclear plant clearing at the same price contribute differently to a state's carbon balance, and the wholesale market sends no price signal for that difference. State renewable portfolio standards don't cover nuclear. Only the ZEC programs and the IRA nuclear production tax credit addressed it directly, and both are workarounds rather than market design.

**Grid inertia.** Synchronous generators contribute rotational mass that stabilizes grid frequency under sudden load or generation changes. Inverter-based renewables do not. As wind and solar penetration rises, the per-unit value of synchronous inertia increases. No wholesale market mechanism prices it.

PJM and FERC designed capacity markets to capture part of the reliability value. For most of the past decade, capacity prices fell short. PJM's base residual auction cleared at $28.92/MW-day for the 2024/25 delivery year. The 2025/26 auction, held in July 2024, cleared at $269.92/MW-day for most of PJM, roughly tenfold higher, driven by accelerating load growth, coal retirements, and an interconnection queue backlog that prevents new supply from entering the market fast enough. The Dominion Zone, where Northern Virginia's data centers concentrate, cleared at $444/MW-day. That spike, what caused it, and what it implies for nuclear economics, is the subject of Post 3.

---

## The current moment

Constellation Energy shares opened at roughly $53 at their February 2022 spinoff from Exelon and passed $300 during 2024, a better-than-fivefold increase. That performance reflects several converging factors: gas prices stayed elevated longer than the 2012–2020 period suggested they would, the IRA nuclear production tax credit established a floor under plant economics, and hyperscaler demand created a class of buyers willing to pay above-market rates for firm, 24/7 carbon-free power.

None of those three factors resolved the underlying market design problem. They worked around it.

Gas prices fell again in 2023 as new LNG export terminals filled and storage normalized. The IRA credit phases out as LMPs rise, which means it provides support when plants need it but shrinks when markets tighten. It doesn't close the gap for good. The Microsoft PPA solves the problem for Three Mile Island; it doesn't clear the market for the rest of the fleet.

The demand backdrop has shifted since the retirement wave. Dominion Energy contracted 7,000 megawatts of new data center load in Northern Virginia in a single year. The PJM reserve margin is tightening as coal retirements accelerate faster than new supply can enter through the interconnection queue. Load growth from AI data centers runs at a high, steady rate around the clock, independent of season or weather. That profile matches nuclear's dispatch characteristics better than any other resource on the grid today.

The plant Constellation retired in 2019 for financial reasons now requires $2.6 billion to restart, will take until 2028 to return to service, and is the subject of a 20-year contract because the buyer couldn't find another resource that would do the same job. The market couldn't support the plant at $30/MWh. It couldn't replace the plant either.

---

## What's next

Post 2 examines the state zero-emission credit programs that intervened before the IRA and the hyperscaler deals changed the calculus. Illinois, New Jersey, and New York each enacted ZEC legislation at different dates to save specific plants from announced retirements, creating a natural experiment. The empirical question: did retaining nuclear capacity measurably lower wholesale electricity prices in the zones those plants serve? A difference-in-differences design across the three programs estimates the market gap ZECs filled, and what closing it cost or saved ratepayers.

Data and code are on [GitHub](https://github.com/aleccshields/marginal-fuel).

---

## Sources

**Plant operations and retirements**
- U.S. nuclear generating unit retirements and capacity: [EIA Electric Power Monthly](https://www.eia.gov/electricity/monthly/), Table 6.1; [EIA Preliminary Monthly Electric Generator Inventory](https://www.eia.gov/electricity/data/eia860m/)
- Three Mile Island Unit 1 retirement (September 2019) and Crane Clean Energy Center PPA: [Constellation Energy press release](https://www.constellationenergy.com/news/2024/Constellation-to-Launch-Crane-Clean-Energy-Center-Restoring-Jobs-and-Carbon-Free-Power-to-The-Grid.html); DOE loan announcement, November 2025

**Price data**
- Henry Hub daily spot price: [FRED series DHHNGSP](https://fred.stlouisfed.org/series/DHHNGSP), Federal Reserve Bank of St. Louis
- PJM Dominion Zone day-ahead LMPs: [EIA Wholesale Electricity Markets](https://www.eia.gov/electricity/wholesalemarkets/)

**Capacity markets**
- PJM 2025/26 Base Residual Auction results ($269.92/MW-day RTO, $444.26/MW-day Dominion Zone): S&P Global, July 30, 2024; [PJM 2025/26 BRA Report](https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/2025-2026/2025-2026-base-residual-auction-report.pdf)

**Nuclear fuel costs and capacity factors**
- Nuclear fuel cost benchmarks: [EIA Electric Power Annual](https://www.eia.gov/electricity/annual/), Table 8.4
- U.S. nuclear fleet capacity factors: [EIA Electric Power Monthly](https://www.eia.gov/electricity/monthly/), Table 6.2

**IRA nuclear production tax credit**
- Section 45U zero-emission nuclear power production credit: [IRA Section 13105 tracker](https://iratracker.org/programs/ira-section-13105-zero-emission-nuclear-power-production-tax-credit/). Note: the One Big Beautiful Bill Act of 2025 added foreign-entity restrictions; the domestic credit remains in effect through 2032.

---

*Zero Margin examines the economics of firm, carbon-free power in a gas-priced electricity market.*
