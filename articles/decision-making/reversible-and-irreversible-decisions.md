---
id: ct:reversible-and-irreversible-decisions
type: Concept
title: Reversible and irreversible decisions
aliases: [one-way and two-way door decisions, decision reversibility, Type 1 and Type 2 decisions]
domain: decision-making
summary: >-
  The distinction between choices that can be cheaply undone once more is
  learned and choices that lock in their consequences; it sets how much
  deliberation, evidence and delay a decision deserves, and it also changes
  how people feel about a choice after making it.
level: introductory
evidenceStatus: mixed
broader: [ct:judgment-and-decision-making]
related: [ct:expected-utility-theory, ct:premortem, ct:affective-forecasting, ct:sunk-cost-fallacy]
requires: []
relations:
  - {predicate: formalizedBy, object: ct:quasi-option-value, source: s2, confidence: high}
  - {predicate: contrastsWith, object: ct:net-present-value-rule, source: s2, confidence: high}
  - {predicate: appliedIn, object: ct:investment-decisions, source: s3, confidence: high}
  - {predicate: demonstratedBy, object: ct:gilbert-ebert-2002-changeable-outcomes-study, source: s1, confidence: high}
  - {predicate: supportedBy, object: ct:bullens-van-harreveld-2016-reversibility-review, source: s4, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Decisions and revisions: The affective forecasting of changeable outcomes"
    publisher: Journal of Personality and Social Psychology 82(4), 503-514 (Gilbert & Ebert, 2002), author's copy at Harvard University
    url: https://dtg.sites.fas.harvard.edu/Gilber%20t&%20Ebert%20(DECISIONS%20&%20REVISIONS).pdf
    type: peer-reviewed
    accessed: 2026-11-07
  - id: s2
    title: "What's the Option?"
    publisher: UC Berkeley, CUDARE Working Paper 1132 (Traeger, 2013), eScholarship
    url: https://escholarship.org/content/qt41v56658/qt41v56658.pdf?t=mqg6g5
    type: academic
    accessed: 2026-11-07
  - id: s3
    title: "Investment under Uncertainty"
    publisher: Princeton University Press (Dixit & Pindyck, 1994), publisher's book page
    url: https://press.princeton.edu/node/57666
    type: primary
    accessed: 2026-11-07
  - id: s4
    title: "Second thoughts about decision reversibility: An empirical overview"
    publisher: Social and Personality Psychology Compass 10(10), 550-560 (Bullens & van Harreveld, 2016), University of Amsterdam repository
    url: https://www.dare.uva.nl/id/a787944c-581e-48e0-a8c4-3f403fac3755
    type: peer-reviewed
    accessed: 2026-11-07
  - id: s5
    title: "2015 Letter to Shareholders (Exhibit 99.1 to Form 8-K)"
    publisher: Amazon.com, Inc., filed with the U.S. Securities and Exchange Commission (Bezos, April 2016)
    url: https://sec.gov/Archives/edgar/data/1018724/000119312516530910/d168744dex991.htm
    type: primary
    accessed: 2026-11-07
created: 2026-11-07
---

# Reversible and irreversible decisions

A decision is **reversible** when a poor choice can be undone at modest cost once its results come in, and **irreversible** when it commits resources, closes off options or changes the world in ways that cannot be walked back. Treating the two alike is a common source of both reckless commitments and needless paralysis. Decision theorists treat reversibility as a reason to value flexibility: when uncertainty will be resolved later, the chance to learn before committing has measurable worth.[^s2] Psychologists add a second, less obvious point: keeping a choice open tends to make people *less* satisfied with it, even though they expect the opposite.[^s1][^s4]

## Origin

The formal idea comes from economics. Kenneth Arrow and Anthony Fisher, and separately Claude Henry, showed in 1974 that the standard net-present-value rule can go wrong when a decision cannot be undone and uncertainty will clear up later; the extra value of waiting to learn became known as *quasi-option value* and the result as the "irreversibility effect".[^s2] Avinash Dixit and Robert Pindyck generalized the idea in 1994 to business investment, arguing that most investments are at least partly irreversible and that a firm can gain value by waiting for better, though never complete, information, by analogy with financial options.[^s3]

The popular workplace framing is Jeff Bezos's 2015 letter to Amazon shareholders. It split decisions into "Type 1" one-way doors, consequential and nearly irreversible, which deserve slow, consultative deliberation, and "Type 2" two-way doors, which can be made quickly by a small group because a mistake can be reversed.[^s5]

## How it works

Reversibility changes the expected cost of being wrong. For a reversible choice, the worst case is the cost of trying, noticing the problem and switching back; acting early also buys information that analysis alone cannot. For an irreversible choice, an error is permanent, so information gathered *before* committing is worth more. Traeger's decision rule makes this explicit: act now only if the project's net present value exceeds the combined value of postponing and of learning while postponing; even a project with zero NPV can be worth delaying purely for what one would learn.[^s2]

*Workplace example.* A product team debates two changes: renaming a settings menu, and migrating every customer onto a new billing system with the old one switched off. The menu rename can be A/B tested and rolled back in an afternoon, so a week of committee review costs more than a wrong guess. The billing migration, once the old system is retired and contracts re-signed, is a one-way door; there the team should run a [premortem](premortem.md), pilot with a subset of customers and keep the old system alive until the evidence is in. Bezos's letter warns that large organizations drift into using the heavyweight process for everything, which brings slowness, risk aversion and too little experimentation, while the opposite error, treating one-way doors lightly, tends to sink companies early.[^s5]

## How to apply it

1. **Classify before deliberating.** Ask what it would cost, in money, time, trust and lost options, to undo the choice in three months. Many decisions are partly reversible; the irreversible component is what deserves scrutiny.[^s3][^s5]
2. **Buy reversibility where it is cheap.** Pilots, staged rollouts, options to expand or abandon and keeping the old system running convert a one-way door into a series of smaller two-way doors, which is the logic of real options.[^s2][^s3]
3. **Match process to door type.** Fast, delegated decisions for two-way doors; slower, consultative review, pre-registered criteria and a deliberate search for disconfirming evidence for one-way doors.[^s5]
4. **Do not keep options open for comfort.** For personal choices where switching is unlikely, an open option mainly lowers satisfaction, so committing can be the better choice.[^s1][^s4]

## Evidence

The economic claim, that flexibility has non-negative value when learning is possible, is a theorem under the models' assumptions rather than an empirical finding.[^s2] The psychological claims rest on experiments. In Gilbert and Ebert's 2002 studies, students who could not exchange a photograph or poster they had chosen came to like it more than students who could, yet forecasters predicted no difference; in a third study about two-thirds of participants still preferred the changeable condition.[^s1] The authors attribute the gap to psychological processes that make settled outcomes feel better and that work less well while a choice remains open.[^s1] A 2016 review by Bullens and van Harreveld reports that, across studies, reversible decisions produced lower post-choice satisfaction and more regret, and organizes the cognitive and motivational mechanisms behind this.[^s4]

*Limitations.* The key experiments used small student samples (55 analyzed participants in Gilbert and Ebert's first study) and low-stakes objects,[^s1] and no large multi-lab replication was found for this run, so the satisfaction effect is rated *mixed* rather than robust. The two-door heuristic is practitioner advice from one executive, not a tested intervention,[^s5] and real decisions sit on a spectrum: an option value calculation needs estimates of what will be learned and when, which are often unknown.[^s2]

## Connections

- **Broader: judgment and decision making.** Reversibility is one of the structural features of a decision that JDM research uses to explain both normative advice and observed behaviour.[^s2][^s1]
- **Formalized by quasi-option value.** The value of keeping an irreversible choice open while information arrives is the formal content of the concept.[^s2]
- **Contrasts with the net-present-value rule.** NPV compares acting now with never acting; under irreversibility and learning it can recommend committing too early.[^s2]
- **Applied in investment decisions.** Dixit and Pindyck built a theory of firm investment around irreversibility and the option to wait.[^s3]
- **Demonstrated by Gilbert and Ebert (2002)** and **supported by Bullens and van Harreveld's 2016 review**, which show that people overvalue reversibility for their own satisfaction, an error of affective forecasting.[^s1][^s4]
- **Related: premortem, expected utility theory, sunk cost fallacy.** A premortem is a natural safeguard before a one-way door; expected utility is the baseline the option-value argument refines; and money already spent on an irreversible commitment should not by itself justify further commitment.[^s2][^s5]

## Sources

[^s1]: Gilbert, D. T., & Ebert, J. E. (2002). "Decisions and revisions: The affective forecasting of changeable outcomes." *Journal of Personality and Social Psychology*, 82(4), 503-514. https://dtg.sites.fas.harvard.edu/Gilber%20t&%20Ebert%20(DECISIONS%20&%20REVISIONS).pdf (accessed 2026-11-07)
[^s2]: Traeger, C. P. (2013). "What's the Option?" UC Berkeley CUDARE Working Paper 1132. https://escholarship.org/content/qt41v56658/qt41v56658.pdf?t=mqg6g5 (accessed 2026-11-07)
[^s3]: Dixit, A. K., & Pindyck, R. S. (1994). *Investment under Uncertainty*. Princeton University Press. https://press.princeton.edu/node/57666 (accessed 2026-11-07)
[^s4]: Bullens, L., & van Harreveld, F. (2016). "Second thoughts about decision reversibility: An empirical overview." *Social and Personality Psychology Compass*, 10(10), 550-560. https://www.dare.uva.nl/id/a787944c-581e-48e0-a8c4-3f403fac3755 (accessed 2026-11-07)
[^s5]: Bezos, J. P. (2016). "2015 Letter to Shareholders," Exhibit 99.1 to Amazon.com, Inc. Form 8-K, U.S. Securities and Exchange Commission. https://sec.gov/Archives/edgar/data/1018724/000119312516530910/d168744dex991.htm (accessed 2026-11-07)
