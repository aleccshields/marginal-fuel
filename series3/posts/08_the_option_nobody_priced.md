# The Option Nobody Priced

*In June 2022, PJM Interconnection suspended its generator interconnection queue. Roughly 2,500 gigawatts of generation projects had piled up in PJM alone — more than thirteen times PJM's average peak load. PJM halted new entries for eighteen months while it rebuilt its study process from scratch. Across all U.S. grid operators, the national queue has since grown past 4,000 gigawatts. Most of it will never be built.*

*The standard explanation is regulatory overload: too many applications, too few engineers, an environmental review process that takes years. That is part of the story. The larger part is financial. Developer behavior is entirely rational given the price structure of queue access. And that price structure is badly wrong.*

---

## The numbers

The Lawrence Berkeley National Laboratory tracks generator interconnection queues in its annual Queued Up report. The dataset, covering projects through end of 2024, shows active queue capacity rising from roughly 1,300 gigawatts in 2010 to 4,400 gigawatts by 2024, against approximately 1,260 gigawatts of installed U.S. generating capacity. The queue-to-installed-capacity ratio has grown from 1.2x to 3.5x over fourteen years.

Of projects that entered U.S. queues between 2000 and 2018 and have since resolved, roughly 15 percent reached commercial operation. The other 85 percent withdrew — before completing studies, after receiving unworkable cost estimates, or after sitting in queue long enough that project economics deteriorated. Withdrawal is the modal outcome by a wide margin.

*[Figure 1: Gigawatts in U.S. interconnection queues by year, 2010–2024, vs. total installed U.S. generating capacity — LBNL Queued Up]*

The queue is not a waitlist. It is something closer to an options market, and its price structure produces exactly the behavior these numbers describe.

---

## What a queue position is

Connecting a new generator to the grid requires an interconnection study. The RTO evaluates the project's impact on transmission flows, identifies required network upgrades, and assigns costs. The developer agrees to pay those upgrade costs or withdraws.

Entering the queue requires paying a study deposit. For a 100-megawatt solar project in PJM, total deposits across the feasibility, system impact, and facilities study phases run roughly $100,000 to $300,000. Deposits paid up to the point of withdrawal are forfeited; the developer loses them and exits the queue.

This is the structure of a call option. The deposit is the premium. The underlying asset is the right to interconnect and sell electricity under a long-term contract.

What is that right worth? A 100-megawatt solar project in PJM at current market conditions:

- Annual generation at 25 percent capacity factor: 219,000 MWh
- Current PPA prices for utility-scale solar in PJM: approximately $45–$55/MWh (LBNL Utility-Scale Solar report, 2024 edition)
- Lazard 2024 LCOE range for utility solar: $29–$41/MWh
- Developer margin at midpoints ($50 PPA, $35 LCOE): $15/MWh × 219,000 MWh = $3.3 million per year
- Present value over 20-year project life at 7 percent discount rate: approximately $35 million

The option premium: $200,000 in study deposits.
The development option value: $35 million.
The ratio: 0.57 percent.

*[Figure 3: Deposit cost vs. estimated development option value, representative 100 MW solar project in PJM — stated-assumption calculation]*

This calculation uses representative numbers with transparent assumptions. The directional point does not depend on precision: for any project with a PPA price that makes development attractive, study deposits priced at cost-of-study represent a small fraction of the option value conferred. Across project sizes and regions, the ratio stays below 2 percent under current market conditions.

In any other options market, an option priced at half a percent of the underlying's value would attract speculative buyers immediately. The interconnection queue is no different.

---

## What rational developers do

When an option is underpriced relative to its underlying, rational actors buy it in volume. A developer managing a portfolio of potential sites, some fully permitted and financed, some partially developed, some speculative, has every reason to enter all of them into the queue simultaneously. If one site clears interconnection with manageable upgrade costs, the developer proceeds. If others come back unfavorable or sit in queue too long, the developer withdraws and loses the deposit.

A $200,000 deposit loss on a project that doesn't proceed is an acceptable cost against a $35 million option exercised on a project that does. The speculative portfolio strategy is rational portfolio optimization under a mispriced option structure.

Each speculative entry consumes interconnection study capacity. Under sequential study procedures, projects are evaluated one after another in queue order. A speculative entry that takes eighteen months to study and then withdraws delays every project behind it by eighteen months. The speculative developer absorbs the deposit cost; the delay cost distributes across all subsequent projects in the queue.

The cascade compounds. As the queue grows and wait times lengthen, the value of an early queue position, which secures study priority and avoids the growing backlog, increases. Higher option value with the same deposit price makes entry more attractive to more developers. More entries lengthen wait times further. The queue is self-reinforcing.

LBNL tracks withdrawal rates by the year projects entered the queue. The trend is consistent: as queue volumes have grown over the past decade, withdrawal rates have risen and median time to commercial operation has extended. Projects that entered in 2012 faced a shorter median wait than projects entering in 2020. The system worsens its own congestion.

*[Figure 2: Withdrawal rate by queue entry year, 2008–2019, share of resolved GW — LBNL Queued Up, data through 2024]*

The consequence is visible in clean energy deployment data. The Rhodium Group and Princeton's ZERO Lab have both quantified how much IRA-eligible generation capacity sits in queues rather than producing electricity. The interconnection queue is not a minor administrative friction. At current volumes, it is a structural limit on how fast the grid can change.

---

## The cross-RTO pattern

The problem is not uniform across grid operators. MISO, PJM, and CAISO carry the largest absolute queue volumes; withdrawal rates are correspondingly high. SPP and NYISO have smaller queues and somewhat different dynamics driven by regional market conditions and deposit structures.

RTOs set different deposit amounts per megawatt. The correlation between deposit-per-MW and withdrawal rates across grid operators is directionally consistent with the options argument: regions with lower implicit option premiums show higher withdrawal rates. The sample is too small to support a causal regression. What the cross-RTO comparison shows is that the pricing failure is not uniform in severity, and the regions with the largest clean energy buildout targets, where development option values are highest, are also the regions where the mispricing is most acute.

MISO implemented cluster study reforms earlier than PJM, grouping applications into simultaneous study batches rather than processing them sequentially. Early evidence from MISO suggests that cluster studies reduce sequential delay for projects within a cluster, even if they do not directly address the speculative entry incentive. The MISO experience informs the design of FERC Order 2023.

---

## FERC Order 2023

FERC finalized Order 2023 in December 2023; it took effect in July 2024. The rule addresses speculative entry directly, with two main mechanisms.

**Cluster study methodology.** Applications are grouped and studied simultaneously rather than sequentially. A speculative entry in one cluster does not block the study of applications in subsequent clusters. Projects within the same cluster face cost estimates that reflect the simultaneous presence of all cluster members, which reduces the incentive to enter speculatively to secure favorable study assumptions ahead of competing applications. This is a meaningful structural reform. Sequential studies created a first-mover advantage for speculative holders; simultaneous clusters eliminate it within the cluster cycle.

**Readiness requirements and higher deposits.** Order 2023 requires applicants to demonstrate project readiness, including site control and evidence of commercial progress, at milestone checkpoints. Developers who cannot meet the milestones lose deposits and queue position. The rule also raised deposit amounts beyond the previous study-cost-recovery standard.

These are serious changes. Cluster studies address the sequential delay problem that most directly harms legitimate developers waiting behind speculative entries. Readiness milestones impose a commitment cost that scales differently than deposit size: a developer who does not hold a site cannot fabricate site control documentation cheaply. The milestone requirement distinguishes committed projects from speculative ones in a way that deposit increases alone cannot.

---

## What Order 2023 did not fix

The deposit increases raise the option premium. They do not close the valuation gap.

Before Order 2023, a 100-megawatt solar project in PJM paid study deposits of roughly $100,000 to $300,000 against a development option worth approximately $35 million. The option was priced at under 1 percent of the underlying.

Order 2023's deposit increases are significant in absolute terms. If deposits doubled for a project of this size, which is a generous estimate of the Order 2023 increase at 100 MW, the option is now priced at roughly 1.1 percent of the underlying. At any PPA price that makes development financially attractive, a developer who assigns reasonable probability to successful interconnection will pay 1.1 percent of the project's development value for the option. The speculative entry calculation has not changed sign. It has changed magnitude by a factor of two.

At current solar and wind PPA prices, study deposits sized to recover study costs will remain a small fraction of development option values. Order 2023 will reduce speculative entry at the margin. As long as PPA prices remain at levels that make $30 million to $50 million development options routine, deposits priced in the hundreds of thousands of dollars will attract speculative portfolio holders.

The readiness requirements are more effective as a long-run constraint precisely because they impose a cost that does not scale linearly with the number of speculative entries. A developer can afford larger deposits on ten speculative sites. A developer cannot fabricate site control on ten sites that don't exist. Whether this constraint proves durable depends on how strictly RTOs enforce documentation standards and whether developers find compliant routes around the intent of the requirements.

The cluster methodology's effectiveness is real but time-limited. Cluster cycles create new coordination points at which developers game entry timing to land in favorable clusters alongside weaker competitors. The strategic behavior migrates rather than disappears.

---

## What a functional queue would look like

Three structural changes would reach closer to the root.

**A secondary market for queue positions.** Queue transfers already happen informally. Developers sell projects mid-development, and buyers acquire queue position along with the project. A FERC-regulated secondary market would make this price visible. If a queue position in PJM's congested zone is trading at $2 million on a secondary market, that price reveals what developers actually believe the underlying option is worth, information the study deposit structure currently suppresses. It also routes positions toward capital-committed developers: buyers of queue positions on secondary markets typically have financing and permits in hand, while original queue entrants range from fully committed to fully speculative.

**Deposits indexed to development option value rather than study cost.** Current deposits recover what the RTO spends on studies. A deposit set at a fixed percentage of the estimated development option value, using regional PPA benchmarks and project capacity as inputs, would price speculative entry out of the market for low-confidence projects without eliminating legitimate development activity. At 3 percent of a $35 million development option, the deposit is $1.05 million. A developer with genuine site control, a near-term PPA, and a defined financing structure pays $1.05 million readily. A developer holding a speculative placeholder pays the same amount for an asset they may never develop. The formula is not technically complex; the political difficulty is that the industry would resist deposits calibrated to option value rather than cost of service.

**Competitive auctions for access in oversubscribed areas.** Where interconnection capacity in a specific zone is genuinely scarce, an auction would allocate access to developers who value it most and reveal the price of that scarcity. Auction revenue could fund transmission expansion in the same congested zone, connecting the revealed value of access to the capital needed to expand it. This is the most structurally coherent reform and the least politically tractable. Incumbent developers and utilities with existing queue positions benefit from first-in-line priority; competitive auctions strip that advantage and reassign it to the highest bidder.

---

## Closing

The United States needs to add hundreds of gigawatts of generating capacity over the next decade. Interconnection queues contain roughly 4,400 gigawatts of projects attempting to connect to a 1,260-gigawatt grid. Of the projects from 2000 to 2018 that have since resolved, 85 percent withdrew before construction began.

NEPA reform will help at the margin. More RTO engineering staff will help at the margin. FERC Order 2023's cluster methodology is a genuine structural improvement. None of these address the underlying pricing failure: a developer can hold a $35 million development option for $200,000 in study deposits. The option remains priced at under 1 percent of the underlying even after Order 2023's deposit increases.

When options are systematically underpriced, demand for them exceeds supply of the underlying asset. The interconnection queue has too many applications because holding a queue position is too cheap relative to what a successful position is worth. Until deposit costs reflect option value rather than study cost, the queue will refill faster than any process reform can drain it.

Data and code are on [GitHub](https://github.com/aleccshields/marginal-fuel).

---

## Sources

**Interconnection queue statistics**
- Lawrence Berkeley National Laboratory, "Queued Up: Characteristics of Power Plants Seeking Transmission Interconnection," data through 2024: emp.lbl.gov/publications/queued-characteristics-power-plants
- LBNL Queued Up data file: available for download at emp.lbl.gov/publications/queued-characteristics-power-plants

**FERC Order 2023**
- FERC Order 2023, Improvements to Generator Interconnection Procedures and Agreements, Docket RM22-14, December 2023: ferc.gov
- FERC Order 2023-A (clarification), May 2024: ferc.gov

**PPA prices and project economics**
- LBNL, "Utility-Scale Solar, 2024 Edition": emp.lbl.gov/utility-scale-solar
- Lazard Levelized Cost of Energy Analysis, 2024: lazard.com/research

**Interconnection procedures (deposit schedules)**
- PJM Open Access Transmission Tariff, Attachment O (Interconnection Procedures): pjm.com
- MISO Generator Interconnection Procedures, Attachment X: misoenergy.org

**Clean energy deployment in interconnection queues**
- Rhodium Group, U.S. Clean Power Outlook reports: rhg.com
- REPEAT Project (Princeton ZERO Lab), grid modeling and interconnection analysis: repeatproject.org

**Queue reform context**
- Grid Strategies, "Disconnected: Clean Energy Stuck in Interconnection Queues," 2023: gridstrategiesllc.com
- FERC technical conference on interconnection reform, Docket AD21-14: ferc.gov

---

*Marginal Fuel examines energy markets, regulation, and the economics of the grid.*
