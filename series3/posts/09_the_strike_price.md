# The Strike Price

*Post 8 showed that interconnection queue positions are call options priced at under one percent of their underlying development value. This post covers the other side of the option: the strike price.*

---

## The wrong order

Most options markets tell you the strike price before you buy. You read the contract, check the premium, decide whether the payoff structure makes sense, and either buy or walk. The interconnection queue runs this sequence in reverse.

A developer entering PJM's queue commits capital — study deposits, site control, permitting, early engineering — before learning what it will cost to actually connect. That number arrives in a System Impact Study, roughly eighteen months to two years later. The developer did not buy a standard call option. The developer bought a barrier option with a floating strike: the barrier is withdrawal, triggered by cost revelation, and the strike itself shifts endogenously based on what other holders in the same queue cluster decide to do.

The difference is not semantic. A standard call option has a fixed strike known at purchase. This instrument has a strike that is unknowable at entry, imprecise at first revelation, and subject to revision for years afterward. That is not a normal option. It is a broken one.

---

## The cost you learn in year two

Under the cost causation principle governing interconnection cost allocation, the developer whose project imposes costs on the transmission network pays those costs. The System Impact Study models the project's effect on transmission flows, identifies constraints the project would cause or worsen, and assigns upgrade costs accordingly.

For some projects, the number is negligible. A wind project connecting at an underutilized substation in a lightly loaded region might owe $3 million in network upgrades. A solar project in PJM's congested western zone, connecting to a line already running near capacity, might owe $180 million. Both paid the same study deposit. Both learned the actual cost of connection two years later.

*[Figure 2: Net option payoff vs. network upgrade cost assignment, by project size]*

The development option value for a 100 MW solar project in PJM, at current PPA prices, runs approximately $35 million. A developer assigned $10 million in upgrade costs clears that threshold with $25 million to spare. A developer assigned $60 million is $25 million underwater. The project does not get built.

---

## Where projects exit

The LBNL Queued Up dataset tracks 36,000 interconnection requests across U.S. grid operators through end of 2024. For the six major ISOs and RTOs — CAISO, ERCOT, ISO-NE, MISO, NYISO, and PJM — 80 percent of withdrawn projects have documented withdrawal phases. Among those projects, the distribution is not even.

In 44.8 percent of cases, projects exit at the System Impact Study. That is the single largest withdrawal category, nearly double the share withdrawing at the pre-cost Feasibility Study stage (23.6 percent). A conservative recoding of PJM's pre-reform "Initial Study" phase — an ISO-specific label that doesn't map cleanly to the standard taxonomy, covering roughly 1,500 additional projects — narrows the gap: SIS drops to 37.6 percent, pre-cost to 35.8 percent. Under either classification, System Impact Study is the modal exit point.

*[Figure 1: Study phase at withdrawal, major ISOs/RTOs (LBNL Queued Up, data through 2024)]*

Projects that survive the early screens and receive their first cost estimate withdraw more often than projects that quit before any estimate arrives. That is not proof that cost revelation causes the concentration — the SIS cohort and the Feasibility cohort may differ on other dimensions — but the pattern is consistent with developers exercising rational option logic: commit minimally, wait for the strike price, withdraw when the math doesn't work.

---

## The cascade

The cost causation principle has a second-order problem. Upgrade cost assignments are not fixed. They shift when other developers' plans change.

PJM assigns costs based on the projects present in the queue at the time of the study. A developer entering behind ten other projects connecting at the same substation receives a cost estimate that reflects the transmission upgrades those predecessors require. When three of those predecessors withdraw after receiving their own cost estimates, the remaining projects' assignments change. Upgrades the predecessors were supposed to fund get redistributed. The redistribution is asymmetric: some remaining projects benefit (lower upgrade requirements without the upstream projects), others deteriorate (they now anchor a longer electrical path). A project that looked viable at $20 million may come back at $55 million after restudy.

The feedback loop is not just instability — it is a positive reinforcement: withdrawals trigger restudies, restudies revise cost estimates, revised estimates trigger more withdrawals. In standard options markets, your exercise cost does not change because someone else decided not to exercise. In the interconnection queue, it does. LBNL's data on rising withdrawal rates over the past decade reflects the compounding: as queue volumes grew and cascade cycles multiplied, the probability of any given project reaching commercial operation fell.

A developer building a financing model cannot price this. The strike price is not a fixed number you learn at SIS. It is a number that can shift multiple times over years in queue, depending on decisions other developers make about projects you may never learn exist.

---

## The toll booth argument

The strongest defense of cost causation is that it screens efficiently. If developers bear the full upgrade cost their project imposes on the network, only projects that are economically viable at the true cost of interconnection proceed. A 70-percent-plus withdrawal rate, on this reading, means the queue is filtering correctly — most applications were not worth building at real cost. The System Impact Study is not a trap; it is a toll booth that collects what the project actually owes.

The problem with this argument is the cascade. A toll booth that charges different amounts to the same project depending on the queue position of unrelated predecessors is not measuring what the project owes. It is measuring the project's network impact plus the reshuffling of costs abandoned by whoever withdrew upstream. The signal and the noise are inseparable. A developer who receives a $55 million upgrade estimate after restudy does not know how much of that reflects their project's actual network impact and how much reflects costs redistributed from a predecessor who exited for unrelated financial reasons. The screening mechanism works in theory. In a queue with tens of thousands of speculative entries and rolling cascade restudies, it does not work in practice.

---

## What the cascade costs the grid

Projects that withdraw mid-study consumed engineering capacity. They held queue position that delayed developers behind them. And they destabilized cost estimates for everyone who came after.

The timing constraint compounds. A project that clears SIS with workable costs in 2024 may have taken four years to get there. If a cascade re-triggers during that window, the developer faces a choice between absorbing the new cost, requesting a restudy (adding twelve to eighteen months), or withdrawing. Many withdraw.

The Rhodium Group's U.S. clean power outlook and Princeton's REPEAT project have both quantified how much IRA-eligible capacity sits stranded in queues rather than producing electricity. The mechanism is the cascade: projects that looked viable at entry are no longer viable three years later, after upstream withdrawals revised their cost assignments.

---

## Two models

Cost causation is not the only allocation method transmission planners have tried.

ERCOT's competitive renewable energy zone program built transmission to zones with high renewable potential and spread costs across all load. The CREZ lines completed in 2013 connected roughly 18 gigawatts of wind capacity in West Texas to Dallas and Houston at approximately $6.9 billion, spread across Texas ratepayers at roughly $4 per month per household. Wind developers in ERCOT face no strike price uncertainty of the PJM variety. They face fixed process timelines and no mid-process cost revisions.

CREZ is not a replicable model. It was a politically negotiated outcome specific to Texas's state-jurisdictional grid, a legislative mandate for renewable buildout, and a geography where long-distance transmission to load centers was identifiable in advance. Presenting it as a generalizable policy answer skips too much. What CREZ demonstrates is narrower but still useful: when you remove the floating-strike problem, large-scale development can happen without the speculative queue dynamics Post 8 described. West Texas wind scaled because developers could bet on volume rather than navigate a cost assignment lottery. That observation does not tell you how to build CREZ outside Texas. It tells you what the lottery is costing.

FERC Order 1920, finalized in May 2024, moves in this direction for long-term transmission planning. It requires regional transmission organizations to conduct 20-year forward-looking studies and build infrastructure to accommodate projected generation, with costs spread across beneficiaries rather than triggering generators. The rule applies to planned transmission, not to existing interconnection cost allocation. But the direction marks a departure from the project-by-project cost causation model that has governed interconnection for three decades.

---

## The option framework completed

Post 8 showed that queue deposits are priced at under one percent of the development option value they unlock. This post adds the strike price.

Even with reformed deposit pricing, a developer entering PJM's queue faces a strike price — the network upgrade cost assignment — that is unknown at entry, imprecise at first revelation, and subject to revision for years. You cannot calculate expected option payoff without a reasonable estimate of the strike. The current system withholds that estimate until after commitment, then revises it based on decisions you cannot observe or control.

Deposit reform addresses the premium problem. Strike price certainty addresses a different one. A functional interconnection queue would need both: deposit levels that price speculative entry out of the market for low-confidence projects, and cost allocation rules that give developers a stable, predictable strike price before they commit capital and wait three years for a study result.

The first reform is administratively tractable. The second requires deciding who bears network upgrade costs among generators, transmission owners, and ratepayers — a distributional question FERC has avoided for thirty years.

---

## Closing

The 85 percent withdrawal rate from post-2000 interconnection queues has a mechanism. Among projects with documented exit phases in major ISOs, System Impact Study is the modal withdrawal point — the moment developers first learn what network connection costs. Whether every withdrawal at SIS represents a failure is genuinely debatable. Some projects were never going to be built at any reasonable interconnection cost; the SIS just surfaces that efficiently.

What is not debatable is the cascade. The floating strike means that even projects which would have been viable at their initial cost estimate may not be viable three years later, after the queue reshuffles around them. A developer entering PJM's queue today is buying a barrier option with an uncertain premium and an unknowable, unstable strike. The math works out for some of them. For most, it does not.

Data and code are on [GitHub](https://github.com/aleccshields/marginal-fuel).

---

## Sources

**LBNL Queued Up**
- Lawrence Berkeley National Laboratory, "Queued Up: Characteristics of Power Plants Seeking Transmission Interconnection," data through 2024: emp.lbl.gov/publications/queued-characteristics-power-plants

**FERC interconnection cost allocation**
- FERC Order 2023, Improvements to Generator Interconnection Procedures and Agreements, Docket RM22-14, December 2023: ferc.gov
- FERC Order 1920, Building for the Future Through Electric Regional Transmission Planning and Cost Allocation, Docket RM21-17, May 2024: ferc.gov

**ERCOT CREZ program**
- Public Utility Commission of Texas, "Competitive Renewable Energy Zones Transmission Optimization Study," 2008
- ERCOT, "CREZ Progress Report," 2013: ercot.com

**Clean energy deployment in queues**
- Rhodium Group, U.S. Clean Power Outlook reports: rhg.com
- REPEAT Project (Princeton ZERO Lab), grid modeling and interconnection analysis: repeatproject.org

**PPA prices and project economics**
- LBNL, "Utility-Scale Solar, 2024 Edition": emp.lbl.gov/utility-scale-solar
- Lazard Levelized Cost of Energy Analysis, 2024: lazard.com/research

---

*Marginal Fuel examines energy markets, regulation, and the economics of the grid.*
