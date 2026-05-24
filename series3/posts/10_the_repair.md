# The Repair

*This is the third post in The Queue, a series on the financial and regulatory mechanics of U.S. generator interconnection. Post 8 showed that interconnection queue positions are call options priced at under one percent of their underlying development value. Post 9 showed that network upgrade costs function as a floating-strike barrier option — unknowable at entry and cascade-unstable. This post evaluates what it would take to fix both.*

---

## The trajectory

For projects entering PJM's interconnection queue in 2015, roughly 74 percent of resolved capacity withdrew before reaching commercial operation. For the 2020 cohort, the figure is 96 percent. One in twenty-five projects makes it through.

*[Figure 1: Withdrawal rate by entry cohort, 2010–2020 (LBNL Queued Up, data through 2024)]*

This is not a steady state. The withdrawal rate has nearly doubled over a decade, with no reversal visible in the data. That trend matters for how to think about the repair. The queue is not broken and stable — it is broken and deteriorating.

---

## Two failures and how they interact

Post 8 identified the first failure: study deposits are priced at under one percent of the development option value they unlock. A developer can hold a $35 million call option for $200,000. Rational portfolio holders enter in volume. The queue floods.

Post 9 identified the second failure: the network upgrade cost — the effective strike price — is unknowable at queue entry, first revealed eighteen months later at the System Impact Study, and subject to revision whenever predecessor projects withdraw. Developers commit before they know the exercise cost.

The two problems are not independent. High cost uncertainty amplifies the incentive to speculate: developers rationally hold queue positions while waiting for cost information to mature, then exit when the number exceeds the option value. Reducing cost uncertainty would reduce the rational holding period, which would reduce speculative portfolio size, which would reduce queue volume. A repair that only addresses deposit pricing leaves cost instability in place and gets partial results. A repair that only addresses cost instability without fixing deposit pricing still tolerates speculative entry at near-zero cost.

---

## What Order 2023 accomplished

FERC finalized Order 2023 in December 2023 and it took effect July 2024. The rule made three meaningful changes.

Higher deposits raised the option premium. Before the rule, a 100 MW solar project in PJM paid study deposits of roughly $100,000 to $300,000 against a development option worth approximately $35 million — under one percent of the underlying. After Order 2023, deposits increased significantly; for many project sizes they roughly doubled. The option is now priced at roughly one to two percent of the underlying. The speculative entry calculation has not changed sign. It has changed magnitude by a factor of two.

Readiness milestones impose a commitment cost that does not scale linearly with the number of speculative entries. A developer can afford larger deposits on ten speculative sites. A developer cannot fabricate site control documentation on ten sites that do not exist. Whether this constraint proves durable depends on how strictly RTOs enforce documentation standards. The requirement is structurally sounder than deposit increases alone.

Cluster studies reduce sequential delay. Under the old process, a speculative entry that consumed eighteen months of engineering time before withdrawing delayed every project behind it by eighteen months. Under cluster studies, applications in the same cohort are evaluated simultaneously. A withdrawal within a cluster harms co-cluster members through cost redistribution, but does not block the next cluster from beginning its study. This is a genuine improvement on the cascade problem — partial, but real.

---

## The 2024 signal

Queue entries fell from 811 GW in 2023 to 505 GW in 2024, a 38 percent drop.

*[Figure 2: Queue entry volume by year, 2015–2024, with Order 2023 timeline (LBNL Queued Up, data through 2024)]*

Three explanations fit the data. Order 2023's readiness requirements may have deterred developers who lacked site control from entering. Higher interest rates through 2023 and 2024 may have pushed marginal projects below viability thresholds, reducing legitimate entries as much as speculative ones. And 2023's record 811 GW was itself an anomaly — developers may have accelerated entries ahead of the Order 2023 effective date, creating a pull-forward that the 2024 drop is partly reversing.

The data cannot distinguish these explanations yet. Causal attribution requires additional cohort years. The 2024 drop is notable, and assigning it entirely to Order 2023 would be premature.

---

## What each reform addresses

The queue has two distinct failure modes, and available reforms address them unevenly.

*[Figure 3: Reform scorecard — which interventions address which failures]*

Three enacted reforms move the needle partially on one problem each. Higher deposits partially raise the option premium. Readiness milestones impose commitment costs that partially deter speculative entry through a different mechanism. Cluster studies partially stabilize costs by eliminating sequential delay within a cohort, though not the cascade that occurs when projects within a cluster withdraw.

Four proposed or partially implemented reforms could go further. Value-indexed deposits — set as a fixed percentage of the estimated development option value rather than study cost recovery — directly address the premium mispricing. At three percent of a $35 million option, the deposit is $1.05 million. A developer with genuine site control and financing pays this readily. A speculative portfolio holder pays it twelve times over on twelve positions, for $12.6 million in total exposure against options that may never be exercised. The math changes.

A FERC-regulated secondary market for queue positions would surface the true option premium through price discovery. If a PJM queue position in a congested zone trades at $2 million on a secondary market, that number reveals what committed developers actually believe the position is worth — information the study deposit structure currently suppresses. Buyers of queue positions on secondary markets typically have financing and permits in hand. The secondary market routes positions toward capital-committed developers without requiring FERC to calculate option values administratively.

Early cost disclosure would restructure the information revelation sequence. Under the current process, developers commit capital before receiving cost estimates. An early cost screen — even a rough preliminary estimate provided before the deposit is paid or within the first sixty days — would let developers make the exercise decision before sinking years of development cost. This does not require changing who bears upgrade costs. It requires changing when they learn what those costs are.

Socialized upgrade costs, the direction Order 1920 points for planned transmission, removes the floating-strike problem entirely for the lines it covers. Developers connecting to planned transmission infrastructure face no project-level cost assignment uncertainty. Order 1920 currently applies to long-range regional planning, not to generator-triggered interconnection upgrades. Extending its logic to a broader share of upgrade costs would require FERC to decide that ratepayers, not developers, bear the cost of transmission expansion — a distributional shift FERC has avoided for three decades.

---

## The commons problem

The Contrarian's framing from the council is worth naming directly: the interconnection queue is partly a commons problem, not only a pricing problem. Each speculative entry imposes cascade costs on all subsequent queue holders — costs that the depositing developer does not bear. Higher deposits and milestones are Pigouvian taxes on this externality, but they are pooled across a cluster rather than charged to the individual cascade trigger.

There is no current mechanism that fully internalizes this externality. Competitive auctions for scarce interconnection capacity in oversubscribed zones would come closest — prices would reflect the true congestion value, and developers who bid low would not enter. The revenue could fund transmission expansion in the same zone, connecting the revealed value of access to the capital needed to expand it. This is the most structurally coherent reform and the least politically tractable. Incumbent developers and utilities with existing queue positions benefit from first-in-line priority. Competitive auctions strip that advantage.

---

## What FERC can and cannot do

FERC's authority under the Federal Power Act covers wholesale electricity markets and interstate transmission. The deposit structure, interconnection study procedures, and cost allocation rules all fall within FERC jurisdiction. Value-indexed deposits, secondary markets, and cluster study refinements are all available to FERC through rulemaking.

Early cost disclosure requires RTOs to restructure their study processes. FERC can direct that restructuring through interconnection procedure reform, though implementation falls to each RTO and would face resistance from RTO engineering staff and incumbent queue holders who benefit from current information asymmetries.

Extending socialized cost allocation from planned transmission to generator-triggered upgrades requires FERC to reallocate costs from developers to ratepayers. Utilities and transmission owners would support this; competitive generators who benefit from the current cost causation principle would oppose it. The distributional stakes are high enough that it would require either a FERC rulemaking with broad stakeholder support or Congressional authorization.

No queue reform works in isolation from transmission planning. If upgrade costs are unknowable partly because the underlying transmission system was not planned to host the generation mix the market is producing, patching the queue process addresses symptoms. Order 1920's forward-looking planning is the structural complement to queue reform, not an alternative to it.

---

## Closing

The 2020 cohort has a 96 percent withdrawal rate. That number is partly efficient — some projects were never viable at true interconnection cost and should not have been built. The screening function of cost causation is not wrong in theory. But a withdrawal rate that has risen from 74 percent to 96 percent over a decade, driven partly by cascade instability that assigns costs based on unrelated predecessors' decisions, reflects more than efficient screening. It reflects a system that is getting harder to use.

FERC Order 2023 raised the option premium and added milestone commitment costs. Those are real improvements, and the 2024 entry drop may be early evidence that they are biting. The floating-strike problem — the cascade-unstable, unknowable upgrade cost — remains substantially untouched.

The repair is not a single rule. It is a sequence: value-indexed deposits to fix the premium, early cost disclosure to stabilize the strike, and regional planning under Order 1920 to reduce the share of upgrade costs that flow through the generator-triggered process at all. Each of those is available within existing FERC authority. None of them is imminent.

Data and code are on [GitHub](https://github.com/aleccshields/marginal-fuel).

---

## Sources

**LBNL Queued Up**
- Lawrence Berkeley National Laboratory, "Queued Up: Characteristics of Power Plants Seeking Transmission Interconnection," data through 2024: emp.lbl.gov/publications/queued-characteristics-power-plants

**FERC Orders**
- FERC Order 2023, Improvements to Generator Interconnection Procedures and Agreements, Docket RM22-14, December 2023: ferc.gov
- FERC Order 2023-A (clarification), May 2024: ferc.gov
- FERC Order 1920, Building for the Future Through Electric Regional Transmission Planning and Cost Allocation, Docket RM21-17, May 2024: ferc.gov

**Clean energy deployment**
- Rhodium Group, U.S. Clean Power Outlook reports: rhg.com
- REPEAT Project (Princeton ZERO Lab): repeatproject.org

**Queue reform context**
- Grid Strategies, "Disconnected: Clean Energy Stuck in Interconnection Queues," 2023: gridstrategiesllc.com
- LBNL, "Utility-Scale Solar, 2024 Edition": emp.lbl.gov/utility-scale-solar
- Lazard Levelized Cost of Energy Analysis, 2024: lazard.com/research

---

*Marginal Fuel examines energy markets, regulation, and the economics of the grid.*
