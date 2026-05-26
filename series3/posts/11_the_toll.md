# The Toll

*This is the first post in The Seam, a series on the financial mechanics of U.S. electricity transmission. The Queue (Series 2) showed that new generation cannot enter the grid cleanly. This series shows why the transmission infrastructure that would fix it is not getting built, and who profits from the gap.*

---

## What a locational price does

Electricity cannot be stored at grid scale. Every megawatt-hour consumed in Baltimore at 3:00 PM had to be generated somewhere and delivered through physical wires at that exact moment. If those wires cannot carry enough power to meet demand at the price producers are willing to sell, the price rises until the most expensive local generators pick up the slack.

A locational marginal price measures the cost of delivering power to a specific location, given the physical limits of the transmission network between the generation source and the load. Two zones connected by unconstrained wires have nearly identical LMPs. Congested interfaces produce price gaps.

---

## The Mid-Atlantic triad

PJM covers thirteen states from Illinois to New Jersey, operating the largest competitive electricity market in the world by load. It publishes hourly day-ahead prices for twenty-one load zones. Over the four full calendar years 2021–2024, three zones consistently sit at the top of the price stack: BGE (Baltimore), Dominion Energy (Northern Virginia and Richmond), and PEPCO (Washington, D.C.).

*[Figure 1: Average day-ahead LMP by PJM zone, 2021–2024]*

BGE averaged $51.56/MWh across the period. PEPCO averaged $49.50/MWh. Dominion averaged $50.32/MWh. At the other end: PECO (Philadelphia) at $36.63/MWh, ComEd (Chicago) at $37.25/MWh, AEC (Atlantic City) at $37.31/MWh.

The cheapest and most expensive zones averaged $14.93/MWh apart across four years. The spread has never closed.

---

## Where the congestion lives

PJM decomposes each LMP into three components: energy, congestion, and loss. The energy component reflects the marginal cost of generation system-wide. The loss component adjusts for transmission line losses. The congestion component captures the premium or discount from binding transmission constraints at that location.

A zone with a positive congestion component is import-constrained: it needs more power than the transmission network can deliver at the system energy price, so local generators with higher costs set the margin. A zone with a negative congestion component is export-constrained: it has more cheap generation than it can send to load centers, so that generation sits idle or depresses local prices below system levels.

BGE carried an average congestion component of +$6.84/MWh across 2021–2024. Dominion: +$6.19/MWh. PEPCO: +$5.03/MWh.

On the other side: PECO at −$6.40/MWh. Atlantic City Electric at −$6.22/MWh. Jersey Central at −$5.46/MWh.

*[Figure 3: Average daily congestion component by zone, 2021–2024]*

New Jersey and Philadelphia area utilities sit on surplus nuclear generation that cannot reach Mid-Atlantic load centers because the transmission interfaces are regularly at capacity. Baltimore, Northern Virginia, and D.C. pay a premium because that surplus cannot flow south.

The binding constraint runs along the interfaces connecting Pennsylvania and New Jersey's nuclear zones to the Mid-Atlantic load pocket. The physical bottleneck sits on the paths from PECO, PSEG, and JCPL territory southward into BGE and DOM.

---

## The spread holds

In 2021, the BGE–ComEd annual average spread was $8.60/MWh. In 2022, when natural gas prices spiked globally, it widened to $21.45/MWh, with gas-fired peakers in BGE territory setting the price as the constraint tightened. In 2023 it compressed to $11.74/MWh as gas prices fell. In 2024 it expanded to $15.17/MWh.

*[Figure 2: Annual LMP spread, key corridors vs. ComEd, 2021–2024]*

The 2022 spike is instructive. High gas prices are a supply shock that hits every zone. But in BGE, the gas price spike lands with extra force because constrained transmission means expensive local gas generation sets the price when the constraint binds. In an unconstrained system, cheap power from Pennsylvania and New Jersey flows south and limits BGE's exposure to local gas costs. The constraint prevents that arbitrage. BGE ratepayers pay the gas premium twice: once for the underlying fuel cost, once for the inability to import power from the north.

The spread stayed open every year. BGE's congestion component was positive in 2021, 2022, 2023, and 2024. The Rappahannock and North of Neck constraints in DOM territory appear in every PJM planning document. None have been relieved.

---

## What the congestion component represents

When BGE carries a +$6.84/MWh average congestion component, that number means BGE ratepayers paid $6.84 more per megawatt-hour than they would have paid if the transmission interface were unconstrained. Across BGE's service territory of approximately 1.3 million customers consuming roughly 25,000 GWh per year, the implied annual congestion cost is approximately $171 million. Per year. Persistent across the full observation period.

Dominion's service territory is larger, roughly 85,000 GWh per year. At +$6.19/MWh, the implied annual congestion cost is approximately $526 million.

These estimates use average load rather than peak constrained load, so they understate the cost during binding constraint hours. They also do not account for the secondary effects: the constraint suppresses wind and nuclear development in the surplus zones by holding down prices there, and it raises the operating cost of the gas-fired peakers that set the marginal price in the constrained zones.

The congestion component flows to generators in the constrained zone, who earn prices above their production costs, and to holders of financial transmission rights on the congested interfaces. FTR holders bought the right to collect the spread between source and sink prices in a given delivery period.

PJM auctions financial transmission rights for its major path-pairs, and the clearing prices reflect what market participants believe the congestion rent will be worth. PJM publishes those clearing prices. It does not publish who holds the resulting positions or what they collect in settlement.

---

## The rent and the line

A new transmission line from Pennsylvania into BGE territory would relieve the constraint. Power from PECO's nuclear plants, currently earning below-system prices because the interface is congested, would flow south. BGE ratepayers would pay less. PECO generators would earn more.

The congestion rent that accrues to in-zone generators and FTR holders would shrink proportionally. Generators behind the congested interface, collecting the $6.84/MWh premium over system energy prices, would lose that premium. FTR holders on the constrained path would lose the settlement spread.

The locational price arithmetic creates this situation directly. A persistent constraint pays the generator behind it, and that payment capitalizes into the asset's value. Building the relieving line destroys that value. The people who benefit from the constraint have a financial interest in its continuation. No conspiracy required.

---

## The planning process

The Mid-Atlantic transmission constraint is not new. The LMP spread between BGE and the Pennsylvania zones has existed in some form for decades. The Rappahannock and North of Neck constraints in DOM territory, and the interfaces separating PSEG from BGE, appear in every PJM State of the Market report.

PJM's transmission planning process evaluates whether new lines should be built. FERC's regional planning rules, updated by Order 1920 in 2024, govern how those costs would be allocated if lines were approved.

The question the data raises: how often does relief actually get built on persistently congested interfaces, and who evaluates the proposals when the people best positioned to influence the outcome are the same people collecting the rent?

Data and code are on [GitHub](https://github.com/aleccshields/marginal-fuel).

---

## Sources

**EIA wholesale markets**
- PJM day-ahead hourly zonal LMPs, 2021–2024: eia.gov/electricity/wholesalemarkets

**PJM market data**
- PJM State of the Market reports (Monitoring Analytics): monitoringanalytics.com
- PJM transmission constraint summaries: pjm.com/markets-and-operations/transmission

**FERC**
- Order 1920, Building for the Future Through Electric Regional Transmission Planning and Cost Allocation, Docket RM21-17, May 2024: ferc.gov

**Academic and policy background**
- Joskow, Paul L. and Tirole, Jean, "Transmission Rights and Market Power on Electric Power Networks," RAND Journal of Economics, 2000
- Hogan, William W., "Financial Transmission Rights: Analysis, Experience and Prospects," Harvard Kennedy School, 2002 (updated versions through 2023)
- Potomac Economics, Independent Market Monitor for MISO, annual reports: potomaceconomics.com

---

*Marginal Fuel examines energy markets, regulation, and the economics of the grid.*
