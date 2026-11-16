---
id: ct:grade-approach
type: Framework
title: GRADE approach
aliases: [GRADE, Grading of Recommendations Assessment Development and Evaluation, GRADE system, GRADE certainty of evidence]
domain: evidence-and-information-literacy
summary: >-
  A transparent framework for rating how confident one can be in a body of
  evidence, outcome by outcome, on four levels (high, moderate, low, very low),
  and for making strong or conditional recommendations that weigh that
  certainty against benefits, harms, values and costs.
level: intermediate
evidenceStatus: normative
broader: [ct:evidence-based-medicine]
related: [ct:hierarchy-of-evidence, ct:systematic-review, ct:publication-bias, ct:confounding, ct:risk-communication, ct:periodic-health-examination-report, ct:gordon-guyatt]
requires: [ct:randomized-controlled-trial, ct:systematic-review]
relations:
  - {predicate: counteracts, object: ct:publication-bias, source: s1, confidence: high}
  - {predicate: counteracts, object: ct:confounding, source: s2, confidence: medium}
  - {predicate: appliedIn, object: ct:systematic-review, source: s2, confidence: high}
  - {predicate: appliedIn, object: ct:evidence-based-medicine, source: s4, confidence: high}
  - {predicate: supportedBy, object: ct:mustafa-2013-grade-reliability-study, source: s3, confidence: medium}
sources:
  - id: s1
    title: "GRADE Handbook: Handbook for grading the quality of evidence and the strength of recommendations using the GRADE approach"
    publisher: GRADE Working Group (Schünemann, Brożek, Guyatt & Oxman, eds., updated 2013), GRADEpro GDT
    url: https://gdt.gradepro.org/app/handbook/handbook.html
    type: primary
    accessed: 2026-11-16
  - id: s2
    title: "Chapter 14: Completing 'Summary of findings' tables and grading the certainty of the evidence"
    publisher: "Cochrane Handbook for Systematic Reviews of Interventions v6.5 (Schünemann, Higgins, Vist, Glasziou, Akl, Skoetz & Guyatt, 2023)"
    url: https://www.cochrane.org/zh-hant/authors/handbooks-and-manuals/handbook/current/chapter-14
    type: textbook
    accessed: 2026-11-16
  - id: s3
    title: "The GRADE approach is reproducible in assessing the quality of evidence of quantitative evidence syntheses"
    publisher: "Journal of Clinical Epidemiology 66(7), 736-742 (Mustafa, Santesso, Brozek et al., 2013), RTI International record"
    url: https://www.rti.org/publication/the-grade-approach-is-reproducible-in-assessing-the-quality-of-evidence-of-quantitative-evidence-syntheses
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s4
    title: "What is GRADE?"
    publisher: BMJ Best Practice, Learn EBM toolkit (Siemieniuk & Guyatt)
    url: https://bestpractice.bmj.com/info/toolkit/learn-ebm/what-is-grade
    type: institutional
    accessed: 2026-11-16
created: 2026-11-16
---

# GRADE approach

GRADE (Grading of Recommendations Assessment, Development and Evaluation) is a structured way to answer two separate questions about evidence: how confident can we be that an estimated effect is close to the truth, and how strongly should anyone act on it?[^s1] Instead of stamping a single grade on a whole study, it rates the certainty of the evidence for each important outcome on four levels — high, moderate, low and very low — and then makes a recommendation that is either strong or conditional (weak).[^s1] By one count it is the most widely adopted evidence-grading tool, endorsed by more than 100 organisations.[^s4]

## Origin

The GRADE Working Group began meeting in 2000 as an informal international collaboration of methodologists, guideline writers, clinicians, health economists and public-health officials who were frustrated by the many incompatible grading systems then in use.[^s1] Its aim was one common, transparent method, and its handbook was edited by Holger Schünemann, Jan Brożek, Gordon Guyatt and Andrew Oxman.[^s1] Cochrane later adopted GRADE: its methods standards require every review to rate certainty for its main outcomes and to record each decision to move a rating up or down.[^s2]

## How it works

GRADE starts from study design and then adjusts. A body of randomised trials starts at high certainty; a body of observational studies starts at low, mainly because of residual confounding and selection bias.[^s2] Five considerations can lower the rating, usually by one level for a serious problem or two for a very serious one: risk of bias in the studies, inconsistency between their results, indirectness (the studies answer a somewhat different question), imprecision (wide confidence intervals or few events) and suspected publication bias.[^s1][^s2] Three considerations can raise observational evidence: a large effect, a dose-response gradient, and plausible confounding that would have worked against the observed effect.[^s1] The result is reported in a "Summary of findings" table that shows, for each outcome, relative and absolute effects, the number of studies and participants, and the certainty rating with footnotes explaining every judgement.[^s2]

Certainty is not the same as recommendation strength. A panel weighs the balance of benefits and harms, people's values and preferences, resource use, equity, acceptability and feasibility, so high-certainty evidence can still yield a conditional recommendation and low-certainty evidence can occasionally justify a strong one.[^s1] A strong recommendation means nearly every informed person would choose the same option; a weak one means informed people would differ, so shared decision-making matters.[^s4]

A workplace example: an occupational-health team is asked whether to buy sit-stand desks to reduce back pain. A review finds a few small randomised trials. They start at high certainty, but the team rates down once for risk of bias (no blinding, many dropouts) and once for imprecision (the confidence interval runs from a meaningful benefit to none), leaving low certainty.[^s2] Given the cost and the fact that staff would value the desks differently, the team issues a conditional recommendation: offer them on request rather than rolling them out to everyone.[^s4]

## How to apply it

1. Frame the question and list the outcomes that matter to the people affected, rating each separately.[^s1]
2. Gather the body of evidence, ideally through a systematic review, and set the starting level by design.[^s2]
3. Check the five reasons to rate down and, for observational evidence, the three reasons to rate up; write down why for each.[^s2]
4. Present absolute effects alongside certainty, then move to a recommendation through the evidence-to-decision factors.[^s1][^s4]

## Evidence and limitations

GRADE ratings remain judgements, and its proponents acknowledge the subjectivity while arguing the process is transparent and reproducible.[^s4] In a 2013 study, trained raters using GRADE agreed far more than when they gave intuitive ratings (inter-rater reliability about 0.66–0.72 for two raters versus roughly 0.3 intuitively), and agreement rose further with three or four raters.[^s3] That evidence comes from trained raters working on prepared materials, so agreement in everyday guideline panels may be lower.[^s3] The default of starting observational evidence low also means some questions that cannot be studied by trials rarely reach high certainty, which Cochrane now partly addresses by letting non-randomised studies assessed with ROBINS-I start higher before rating down.[^s2]

## Connections

GRADE grew within evidence-based medicine, where it supplies the grading step for clinical recommendations.[^s4] It is the standard way to rate certainty in Cochrane systematic reviews.[^s2] By treating publication bias as an explicit reason to rate down, it counteracts the distorting effect of unpublished null results,[^s1] and by starting non-randomised evidence low it guards against mistaking confounded associations for effects.[^s2] Its reliability claim is supported by the Mustafa and colleagues reproducibility study.[^s3] It refines the older hierarchy of evidence, which ranks designs alone, by letting a design's starting level move up or down,[^s1] and its insistence on reporting absolute as well as relative effects ties it to risk communication.[^s2]

## Sources

[^s1]: Schünemann, Brożek, Guyatt & Oxman (eds.), GRADE Handbook, GRADE Working Group, updated 2013. https://gdt.gradepro.org/app/handbook/handbook.html (accessed 2026-11-16)
[^s2]: Schünemann et al., "Chapter 14: Completing 'Summary of findings' tables and grading the certainty of the evidence", Cochrane Handbook for Systematic Reviews of Interventions v6.5, 2023. https://www.cochrane.org/zh-hant/authors/handbooks-and-manuals/handbook/current/chapter-14 (accessed 2026-11-16)
[^s3]: Mustafa, Santesso, Brozek et al., "The GRADE approach is reproducible in assessing the quality of evidence of quantitative evidence syntheses", Journal of Clinical Epidemiology 66(7), 2013. https://www.rti.org/publication/the-grade-approach-is-reproducible-in-assessing-the-quality-of-evidence-of-quantitative-evidence-syntheses (accessed 2026-11-16)
[^s4]: Siemieniuk & Guyatt, "What is GRADE?", BMJ Best Practice. https://bestpractice.bmj.com/info/toolkit/learn-ebm/what-is-grade (accessed 2026-11-16)
