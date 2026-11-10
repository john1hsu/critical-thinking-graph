---
id: ct:power-analysis
type: Method
title: Power analysis
aliases: [statistical power analysis, a priori power analysis, sample size calculation, sample size justification]
domain: scientific-reasoning
summary: >-
  The practice of working out, before data are collected, how large a sample a
  study needs to have a good chance of detecting an effect of a given size at
  a chosen significance level, using the fixed relationship among sample size,
  alpha, effect size and statistical power.
level: intermediate
evidenceStatus: normative
broader: [ct:scientific-method, ct:statistical-reasoning]
related: [ct:law-of-small-numbers, ct:insensitivity-to-sample-size, ct:random-sampling, ct:replication-crisis, ct:researcher-degrees-of-freedom, ct:preregistration, ct:publication-bias, ct:hypothesis-testing]
requires: [ct:null-hypothesis-significance-testing]
relations:
  - {predicate: counteracts, object: ct:law-of-small-numbers, source: s2, confidence: high}
  - {predicate: counteracts, object: ct:replication-crisis, source: s5, confidence: medium}
  - {predicate: introducedBy, object: ct:jacob-cohen, source: s1, confidence: medium}
  - {predicate: appliedIn, object: ct:null-hypothesis-significance-testing, source: s1, confidence: high}
  - {predicate: supportedBy, object: ct:button-2013-power-failure-analysis, source: s5, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "A power primer"
    publisher: Psychological Bulletin 112(1), 155-159 (Cohen, 1992), hosted copy at the University of Victoria
    url: https://www.ece.uvic.ca/~bctill/papers/mocap/Cohen_1992.pdf
    type: primary
    accessed: 2026-11-10
  - id: s2
    title: "Belief in the law of small numbers"
    publisher: Psychological Bulletin 76(2), 105-110 (Tversky & Kahneman, 1971), hosted copy
    url: https://literature.wolkersdorfer.info/literature/Belief%20in%20the%20law%20of%20small%20numbers.pdf
    type: primary
    accessed: 2026-11-10
  - id: s3
    title: "Do studies of statistical power have an effect on the power of studies?"
    publisher: CAUSE (Consortium for the Advancement of Undergraduate Statistics Education) literature index; Sedlmeier & Gigerenzer, Psychological Bulletin 105(2), 1989
    url: https://www.causeweb.org/cause/node/7370
    type: institutional
    accessed: 2026-11-10
  - id: s4
    title: "Sample Size Justification (chapter 8 of Improving Your Statistical Inferences)"
    publisher: Daniel Lakens, open textbook (Eindhoven University of Technology)
    url: https://lakens.github.io/statistical_inferences/08-samplesizejustification.html
    type: textbook
    accessed: 2026-11-10
  - id: s5
    title: "Power failure: why small sample size undermines the reliability of neuroscience"
    publisher: Nature Reviews Neuroscience 14, 365-376 (Button et al., 2013), University of Bristol research portal
    url: https://research-information.bris.ac.uk/en/publications/power-failure-why-small-sample-size-undermines-the-reliability-of/
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s6
    title: "Serious power failure threatens the entire field of neuroscience"
    publisher: British Psychological Society Research Digest (2013)
    url: https://bps.org.uk/research-digest/serious-power-failure-threatens-entire-field-neuroscience
    type: institutional
    accessed: 2026-11-10
  - id: s7
    title: "A test is not a test"
    publisher: Nature Reviews Neuroscience 14, 877 (Hoppe, 2013, correspondence on Button et al.)
    url: https://www.nature.com/articles/nrn3475-c5.pdf
    type: peer-reviewed
    accessed: 2026-11-10
created: 2026-11-10
---

# Power analysis

Power analysis is the planning step in which a researcher decides how much data to collect by asking how likely the study is to detect an effect that is really there.[^s1] Statistical power is the long-run probability of rejecting a false null hypothesis, equal to one minus the Type II (missed-effect) error rate.[^s1] Four quantities are tied together: sample size, the significance criterion (alpha), the population effect size and power. Fix any three and the fourth follows, so in practice a planner usually fixes alpha, a target power and an effect size worth detecting, then solves for the sample size.[^s1]

## Origin

Power is part of the Neyman–Pearson approach to significance testing, but it was the psychologist and statistician Jacob Cohen who turned it into a routine planning tool for behavioral science.[^s1] Reviewing the 1960 volume of the *Journal of Abnormal and Social Psychology*, he found that the mean power to detect a medium-sized effect was only about .48, roughly a coin toss.[^s1] Tversky and Kahneman cited that finding in 1971 as a symptom of researchers' belief in the law of small numbers, and urged explicit power computation, relative to a reasonable hypothesis, before any study is run.[^s2] Cohen's 1992 *Psychological Bulletin* "power primer" then offered a short table-based guide, partly because he judged that the technical literature had kept researchers from using power at all.[^s1]

## How it works

Cohen proposed conventions to make the calculation tractable: for a standardized mean difference *d*, 0.2 is small, 0.5 medium and 0.8 large, and a target power of .80 paired with alpha = .05 accepts a fourfold larger risk of missing an effect than of a false alarm.[^s1] With those settings, a two-group *t* test needs 64 participants per group to detect a medium effect.[^s1]

A workplace example: an HR team wants to know whether a new onboarding programme cuts time-to-productivity. They have 15 new hires a quarter and plan to compare one cohort against the old programme. Before running the pilot, they decide the smallest improvement that would justify the cost is a moderate one, and a power calculation shows they would need around four quarters of hires in each arm to detect it reliably. That tells them the one-quarter pilot cannot settle the question: a favourable result would be fragile and a null result uninformative. They either pool data over a year, accept a coarser question, or report the pilot honestly as exploratory.[^s1][^s4]

## How to apply it

Lakens's open textbook lays out the inputs an a priori power analysis needs and the traps to avoid.[^s4]

1. **Choose alpha,** adjusting it if several tests will be run.[^s4]
2. **Choose the desired power** (equivalently the acceptable Type II error rate).[^s4]
3. **Justify the effect size.** Lakens calls basing it on the smallest effect size of interest, set from theory or practical stakes, the strongest justification available.[^s4]
4. **Compute the sample size** analytically or by simulation and report the settings so others can reproduce it.[^s4]
5. **If the aim is to show that an effect is absent,** plan for an equivalence test as well, since a non-significant result alone does not show that.[^s4]

Pitfalls: effect sizes taken from small pilot studies are too imprecise to plan with, and published effect sizes are inflated by publication bias, so power analyses built on them overestimate power.[^s4] Lakens also discourages defaulting to Cohen's "medium" benchmark when no real justification exists.[^s4] When resources rather than power fix the sample, he recommends saying so and reporting what effect sizes the study could and could not detect, rather than pretending the design is adequate.[^s4]

## Evidence

Advice to plan for power has been slow to change practice. Sedlmeier and Gigerenzer re-examined the journal Cohen had reviewed and found that by 1984 median power for medium effects had fallen from .46 to .37; only 2 of 64 experiments mentioned power and none estimated it.[^s3] In 2013, Button and colleagues analysed neuroscience meta-analyses and argued that average power in the field is very low, which both raises the miss rate and lowers the chance that a significant finding reflects a true effect, while inflating reported effect sizes.[^s5] Their analysis of 49 meta-analyses covering 730 studies put median power at about 21%.[^s6] In a published reply, Christian Hoppe argued that the link between power and the reliability of significant results depends on how many tested hypotheses are true, so the scale of that second problem is debated; the case for planning sample size to avoid missed effects is not.[^s7]

## Connections

- **Broader: scientific method and statistical reasoning.** Power analysis is a design decision taken before data collection within statistical inference.[^s1][^s4]
- **Counteracts the law of small numbers.** Tversky and Kahneman prescribed explicit power calculations as the cure for trusting small samples too much.[^s2]
- **Counteracts the replication crisis.** Button and colleagues trace part of the field's poor reproducibility to underpowered studies and call for adequately powered designs.[^s5]
- **Introduced by Jacob Cohen** as a practical tool for behavioral researchers, through his 1962 review and later handbook and primer.[^s1]
- **Applied in null hypothesis significance testing,** whose alpha and Type II error rate it takes as inputs.[^s1]
- **Supported by Button et al.'s 2013 analysis,** which documents the costs of skipping it.[^s5][^s6]
- **Related to insensitivity to sample size, random sampling, publication bias, preregistration, researcher degrees of freedom and hypothesis testing,** because sample size planning is one of the choices that, made openly in advance, limits how much noise can pass as signal.[^s3][^s4][^s5]

## Sources

[^s1]: J. Cohen, "A power primer", *Psychological Bulletin* 112(1), 1992, 155–159. https://www.ece.uvic.ca/~bctill/papers/mocap/Cohen_1992.pdf (accessed 2026-11-10)
[^s2]: A. Tversky & D. Kahneman, "Belief in the law of small numbers", *Psychological Bulletin* 76(2), 1971, 105–110. https://literature.wolkersdorfer.info/literature/Belief%20in%20the%20law%20of%20small%20numbers.pdf (accessed 2026-11-10)
[^s3]: P. Sedlmeier & G. Gigerenzer, "Do studies of statistical power have an effect on the power of studies?", *Psychological Bulletin* 105(2), 1989; CAUSE literature index entry. https://www.causeweb.org/cause/node/7370 (accessed 2026-11-10)
[^s4]: D. Lakens, "Sample Size Justification", chapter 8 of *Improving Your Statistical Inferences* (open textbook). https://lakens.github.io/statistical_inferences/08-samplesizejustification.html (accessed 2026-11-10)
[^s5]: K. S. Button, J. P. A. Ioannidis, C. Mokrysz, B. A. Nosek, J. Flint, E. S. J. Robinson & M. R. Munafò, "Power failure: why small sample size undermines the reliability of neuroscience", *Nature Reviews Neuroscience* 14, 2013, 365–376. https://research-information.bris.ac.uk/en/publications/power-failure-why-small-sample-size-undermines-the-reliability-of/ (accessed 2026-11-10)
[^s6]: British Psychological Society Research Digest, "Serious power failure threatens the entire field of neuroscience", 2013. https://bps.org.uk/research-digest/serious-power-failure-threatens-entire-field-neuroscience (accessed 2026-11-10)
[^s7]: C. Hoppe, "A test is not a test", correspondence, *Nature Reviews Neuroscience* 14, 2013, 877. https://www.nature.com/articles/nrn3475-c5.pdf (accessed 2026-11-10)
