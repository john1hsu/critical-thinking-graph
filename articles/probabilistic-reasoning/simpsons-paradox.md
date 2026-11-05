---
id: ct:simpsons-paradox
type: Phenomenon
title: Simpson's paradox
aliases: [Simpson's reversal, Yule-Simpson effect, amalgamation paradox, reversal paradox]
domain: probabilistic-reasoning
summary: >-
  A statistical pattern in which an association between two variables that
  holds in a whole population weakens, vanishes or reverses direction once
  the population is split into subgroups, so that pooled and stratified data
  point to opposite conclusions.
level: intermediate
evidenceStatus: robust
broader: [ct:statistical-paradox]
related: [ct:base-rate-neglect, ct:randomized-controlled-trial, ct:correlation-versus-causation, ct:berksons-paradox, ct:sure-thing-principle]
requires: [ct:conditional-probability]
relations:
  - {predicate: explainedBy, object: ct:confounding, source: s4, confidence: high}
  - {predicate: demonstratedBy, object: ct:bickel-1975-berkeley-admissions-study, source: s2, confidence: high}
  - {predicate: formalizedBy, object: ct:causal-diagrams, source: s3, confidence: high}
  - {predicate: appliedIn, object: ct:clinical-research, source: s4, confidence: high}
  - {predicate: studiedIn, object: ct:philosophy-of-science, source: s1, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Simpson's Paradox"
    publisher: Stanford Encyclopedia of Philosophy (Weinberger)
    url: https://plato.stanford.edu/entries/paradox-simpson/
    type: scholarly-encyclopedia
    accessed: 2026-11-05
  - id: s2
    title: "Sex Bias in Graduate Admissions: Data from Berkeley"
    publisher: Science 187(4175), 398-404 (Bickel, Hammel & O'Connell, 1975), University of Iowa course copy
    url: https://homepage.stat.uiowa.edu/~mbognar/1030/Bickel-Berkeley.pdf
    type: primary
    accessed: 2026-11-05
  - id: s3
    title: "Understanding Simpson's Paradox"
    publisher: The American Statistician 68(1), 8-13 (Pearl, 2014), UCLA Cognitive Systems Laboratory technical report R-414
    url: https://ftp.cs.ucla.edu/pub/stat_ser/r414.pdf
    type: peer-reviewed
    accessed: 2026-11-05
  - id: s4
    title: "Simpson's Paradox in Clinical Research: A Cautionary Tale"
    publisher: Journal of Clinical Medicine 12(4), 1633 (Bonovas & Piovani, 2023), MDPI
    url: https://www.mdpi.com/2077-0383/12/4/1633
    type: peer-reviewed
    accessed: 2026-11-05
created: 2026-11-05
---

# Simpson's paradox

Simpson's paradox occurs when two variables are associated one way in a whole population but the association shrinks, disappears or flips sign inside every subgroup once the population is divided up.[^s1] A treatment can raise success rates for men and for women separately and still look worse for everyone combined. Nothing in the arithmetic is contradictory; the surprise comes from how people read the numbers.[^s1][^s3]

## Origin

Karl Pearson (1899) and George Udny Yule (1903) first noticed associations that change when tables are combined, and E. H. Simpson's 1951 paper on interaction in contingency tables gave the effect its name.[^s1] Colin Blyth used it in 1972 to argue against the sure-thing principle of decision theory, the idea that an option better in every case must be better overall.[^s1][^s3] Its best-known real case is the 1975 *Science* paper by Peter Bickel, Eugene Hammel and J. W. O'Connell on Berkeley graduate admissions, which named the pooling problem after Simpson.[^s2]

## How it works

The overall rate is a weighted average of the subgroup rates, and the weights are the share of each group that falls in each subgroup. If one group is concentrated in the hard subgroup, its overall average is dragged down even when it does better within every subgroup.[^s1][^s4]

A workplace example: two support teams report ticket resolution rates. Team A resolves 90 of 100 easy tickets (90%) and 60 of 200 hard tickets (30%), or 150 of 300 overall (50%). Team B resolves 170 of 200 easy tickets (85%) and 25 of 100 hard ones (25%), or 195 of 300 overall (65%). Team A is better at both kinds of ticket, yet looks much worse on the dashboard because it was routed twice as many hard tickets. Ranking the teams on the pooled figure would punish the stronger team, the same weighting trap the encyclopedia entry illustrates with a hypothetical treatment.[^s1]

The Berkeley data followed the same pattern. In fall 1973 about 44% of 8,442 male applicants were admitted against about 35% of 4,321 female applicants, yet department by department there was no sign of bias against women and, pooled correctly, a small bias in their favour. Women had applied more often to departments that turned most applicants away.[^s2] A 1986 study of kidney stone treatment shows the clinical version: open surgery succeeded more often than percutaneous nephrolithotomy for both small stones (93% vs 87%) and large stones (73% vs 69%), but less often overall (78% vs 83%), because surgeons used open surgery mostly on the harder, larger stones.[^s4]

## How to spot and handle it

- Ask whether some third variable affects both which group a case lands in and the outcome; stone size and department choice are classic examples.[^s4]
- Break the headline figure down by the plausible third variables and see whether the comparison holds inside each subgroup.[^s4]
- Do not assume the stratified answer always wins. Pearl showed, building on Lindley and Novick, that the same table can call for the pooled answer when the third variable is caused by the treatment (a mediator) and the split answer when it is a prior common cause (a confounder). The numbers alone cannot decide; a causal model of how the data arose can.[^s3][^s1]
- Prefer designs that break the link between grouping and treatment. When the grouping variable is uncorrelated with treatment, as in a randomised, balanced design, a reversal of success rates cannot occur, although odds ratios can still behave oddly.[^s1]

## Evidence

As a mathematical fact the reversal is not in doubt; the empirical question is how often it misleads real analyses. Documented cases span admissions, surgery, hospital infection control and pandemic data: Bonovas and Piovani in 2023 describe Covid-19 case fatality that looked higher in Italy than in China overall but was higher in China within every age band, because Italy's cases were much older.[^s4] They also report a Dutch hospital study in which antibiotic prophylaxis looked protective overall but was linked to more urinary infections within both low- and high-incidence hospitals.[^s4] Philosophers still debate what makes the reversal feel paradoxical; Pearl attributes it to reading observational proportions as if they were effects of intervening, while other analyses stress the weighting arithmetic.[^s1][^s3]

## Connections

- **Explained by** confounding: a variable unevenly spread across the compared groups and linked to the outcome produces the reversal.[^s4]
- **Demonstrated by** the 1975 Berkeley admissions study, the textbook real-world case.[^s2]
- **Formalized by** causal diagrams, whose back-door criterion tells an analyst whether to use the pooled or the split data.[^s3]
- **Applied in** clinical research, where non-randomised comparisons are especially exposed to it.[^s4]
- **Studied in** the philosophy of science, which uses it to probe probabilistic causation and decision principles such as the sure-thing principle.[^s1]
- **Related to** base-rate neglect, since both arise from ignoring how cases are distributed, to correlation versus causation, to randomised controlled trials as the design remedy, and to Berkson's paradox, the collider case that Pearl contrasts with confounding.[^s1][^s3]
- **Requires** conditional probability, because the paradox is a statement about conditional rates and their weighted averages.[^s1]

## Sources

[^s1]: Weinberger, "Simpson's Paradox", Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/entries/paradox-simpson/ (accessed 2026-11-05)
[^s2]: Bickel, Hammel & O'Connell, "Sex Bias in Graduate Admissions: Data from Berkeley", Science 187, 1975. https://homepage.stat.uiowa.edu/~mbognar/1030/Bickel-Berkeley.pdf (accessed 2026-11-05)
[^s3]: Pearl, "Understanding Simpson's Paradox", The American Statistician 68(1), 2014 (UCLA technical report R-414). https://ftp.cs.ucla.edu/pub/stat_ser/r414.pdf (accessed 2026-11-05)
[^s4]: Bonovas & Piovani, "Simpson's Paradox in Clinical Research: A Cautionary Tale", Journal of Clinical Medicine 12(4), 1633, 2023. https://www.mdpi.com/2077-0383/12/4/1633 (accessed 2026-11-05)
