---
id: ct:preregistration
type: Technique
title: Preregistration
aliases: [pre-registration, study preregistration, pre-analysis plan, prospective trial registration]
domain: scientific-reasoning
summary: >-
  The practice of recording a study's hypotheses, design, outcomes and
  analysis plan in a time-stamped, independent registry before the data are
  collected or examined, so that confirmatory tests can be told apart from
  exploratory findings and selective reporting becomes visible.
level: intermediate
evidenceStatus: mixed
broader: [ct:scientific-method]
related: [ct:researcher-degrees-of-freedom, ct:replication-crisis, ct:null-hypothesis-significance-testing, ct:power-analysis, ct:systematic-review, ct:p-hacking, ct:registered-reports, ct:open-science]
requires: [ct:hypothesis-testing]
relations:
  - {predicate: counteracts, object: ct:publication-bias, source: s4, confidence: high}
  - {predicate: counteracts, object: ct:hindsight-bias, source: s1, confidence: medium}
  - {predicate: detects, object: ct:reporting-bias, source: s1, confidence: medium}
  - {predicate: appliedIn, object: ct:randomized-controlled-trial, source: s4, confidence: high}
  - {predicate: supportedBy, object: ct:kaplan-irvin-2015-nhlbi-null-results-study, source: s2, confidence: medium}
  - {predicate: supportedBy, object: ct:scheel-2021-registered-reports-positive-results-study, source: s3, confidence: medium}
  - {predicate: challengedBy, object: ct:szollosi-2020-is-preregistration-worthwhile, source: s5, confidence: medium}
  - {predicate: challengedBy, object: ct:claesen-2021-preregistration-adherence-study, source: s6, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "The preregistration revolution"
    publisher: Proceedings of the National Academy of Sciences (Nosek, Ebersole, DeHaven & Mellor, 2018), doi:10.1073/pnas.1708274114; copy hosted by errorstatistics.com
    url: https://errorstatistics.com/wp-content/uploads/2017/07/nosek-et-al-preregistration-revolution.pdf
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s2
    title: "Likelihood of Null Effects of Large NHLBI Clinical Trials Has Increased over Time"
    publisher: PLOS ONE 10(8), e0132382 (Kaplan & Irvin, 2015); DOAJ record
    url: https://doaj.org/article/3ca4f2975c8245e09e5311375dc03103
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s3
    title: "An Excess of Positive Results: Comparing the Standard Psychology Literature With Registered Reports"
    publisher: Advances in Methods and Practices in Psychological Science 4(2) (Scheel, Schijen & Lakens, 2021), Association for Psychological Science
    url: https://www.psychologicalscience.org/journals/ampps/25152459211007467/
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s4
    title: "ClinicalTrials.gov: A Report to the Board of Scientific Counselors (LHNCBC-TR-2005-003)"
    publisher: U.S. National Library of Medicine, Lister Hill National Center for Biomedical Communications (Zarin, Bergeris, Ide & Tse, 2005)
    url: https://www.lhncbc.nlm.nih.gov/LHC-publications/PDF/tr2005003.pdf
    type: government
    accessed: 2026-11-12
  - id: s5
    title: "Is Preregistration Worthwhile?"
    publisher: Trends in Cognitive Sciences (Szollosi, Kellen, Navarro, Shiffrin, van Rooij & Van Zandt, 2020), doi:10.1016/j.tics.2019.11.009; FORRT curated summary
    url: https://forrt.org/curated_resources/is-preregistration-worthwhile/
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s6
    title: "Comparing dream to reality: an assessment of adherence of the first generation of preregistered studies"
    publisher: Royal Society Open Science 8(10) (Claesen, Gomes, Tuerlinckx & Vanpaemel, 2021); DOAJ record
    url: https://doaj.org/article/4c3b51be665d4138b3f0af7c0d8ca92c
    type: peer-reviewed
    accessed: 2026-11-12
created: 2026-11-12
---

# Preregistration

Preregistration means committing to a study's hypotheses and analysis steps before knowing the outcome, usually by posting the plan to an independent, time-stamped registry such as ClinicalTrials.gov or the Open Science Framework.[^s1] Its purpose is to keep two kinds of research apart: prediction, which tests an idea against data not yet seen, and postdiction, which builds an idea from data already in hand. Nosek and colleagues argue that both are valuable but that mixing them up makes findings look more certain than they are.[^s1]

## Origin

Preregistration started in medicine as trial registration. Section 113 of the US Food and Drug Administration Modernization Act of 1997 required certain drug-effectiveness trials for serious diseases to be registered, and the NIH launched ClinicalTrials.gov to hold them in February 2000.[^s4] The main concern behind it was that some trial results never get published, or get published only in part, which can mislead patients and policymakers who rely on the published record.[^s4] In September 2004 the International Committee of Medical Journal Editors said its journals would consider a trial for publication only if it had been registered before the first patient was enrolled. That made registration a condition of publishing in those journals.[^s4] During the 2010s, psychology and the social sciences adopted the idea for all kinds of hypothesis-testing research. Nosek and colleagues' 2018 paper "The preregistration revolution" became a widely cited statement of the case.[^s1]

## How it works

Once data have been seen, hindsight makes almost any result look predictable, and researchers can misremember what they meant to test. Questions such as which outcome, which participants to exclude and which covariates to include branch into what Gelman and Loken call a garden of forking paths, and a p-value chosen after walking those paths no longer means what it claims.[^s1] A plan written beforehand fixes those choices, so the confirmatory test keeps its meaning and any departure from the plan can be seen.[^s1]

Workplace example: a product team wants to test whether a redesigned checkout page raises completed purchases. Before the experiment runs, the analyst records in a shared, dated document the primary metric (completed orders per session), the two-week test window, the rule for excluding bot traffic and the planned test. When the results come in, conversion is flat, but basket size is up among mobile users. Because the plan exists, the team reports the primary result as null and labels the mobile finding as exploratory, to be confirmed in a follow-up test, instead of presenting it as what the redesign was meant to do.[^s1]

## How to apply it

1. **Write the plan before you see the outcome data:** the hypotheses, primary and secondary outcomes, sample size and stopping rule, exclusion criteria, and the exact analysis.[^s1]
2. **Register it somewhere independent and time-stamped,** so the date and content can't be changed quietly later.[^s1][^s4]
3. **Report every deviation openly.** Changes during data collection are acceptable if they are documented. For problems you can't predict, such as violated statistical assumptions, use decision trees, standard operating procedures or staged plans.[^s1]
4. **Keep confirmatory and exploratory results apart in the write-up.** Preregistration doesn't rank prediction above postdiction; it keeps them labelled.[^s1]
5. **For existing datasets,** state what you had already seen. A holdout sample can recover a clean test.[^s1]

Pitfalls: a vague plan leaves room for the flexibility it was meant to remove, and authors and readers can still take narrative license by emphasising whichever results look interesting.[^s1] In **registered reports**, a related format, journals review the plan and accept it in principle before data collection, which takes the outcome out of the publication decision.[^s1]

## Evidence

The evidence is suggestive but observational. In 55 large cardiovascular trials funded by the US National Heart, Lung, and Blood Institute between 1970 and 2012, 57% of trials published before 2000 reported a significant benefit on the primary outcome, against 8% of those published after. Prior registration on ClinicalTrials.gov was strongly associated with the shift toward null results.[^s2] A 2021 comparison in psychology found positive results for the first hypothesis in 96% of a random sample of standard articles but in only 44% of 71 registered reports. The authors propose reduced publication bias and less Type I error inflation as likely, though unproven, reasons.[^s3]

Adherence is a weak point. Of 27 early preregistered articles in *Psychological Science*, only two followed their plans with no deviations, and nine disclosed none of their deviations.[^s6] Critics also question the rationale itself. Szollosi and colleagues argue that how informative a test is depends on how well the statistics map onto a theory, and that preregistration neither fixes that mapping nor reliably leads researchers to better theories.[^s5] The status is therefore mixed: there is good evidence that registration changes what gets reported, but how much it improves inference is still debated.[^s2][^s3][^s5][^s6]

## Connections

- **Broader: the scientific method; requires hypothesis testing.** Preregistration only means something for research that tests a stated hypothesis.[^s1]
- **Counteracts publication bias.** Trial registration was created because unpublished and partly published trials distort the evidence base.[^s4]
- **Counteracts hindsight bias and detects reporting bias.** A dated plan stops after-the-fact stories from passing as predictions and shows when outcomes were switched or left out.[^s1]
- **Applied in randomized controlled trials,** where registration is a legal and editorial requirement.[^s4]
- **Supported by** the Kaplan–Irvin trial analysis and the Scheel–Schijen–Lakens comparison of registered reports.[^s2][^s3]
- **Challenged by** Szollosi and colleagues' theory-first critique and by Claesen and colleagues' adherence audit.[^s5][^s6]
- **Related to researcher degrees of freedom, p-hacking, the replication crisis, power analysis and systematic reviews.** These are the flexibility it constrains, the crisis it responds to, and neighbouring practices that are also fixed in advance.[^s1][^s3]

## Sources

[^s1]: B. A. Nosek, C. R. Ebersole, A. C. DeHaven & D. T. Mellor, "The preregistration revolution", *Proceedings of the National Academy of Sciences*, 2018. https://errorstatistics.com/wp-content/uploads/2017/07/nosek-et-al-preregistration-revolution.pdf (accessed 2026-11-12)
[^s2]: R. M. Kaplan & V. L. Irvin, "Likelihood of Null Effects of Large NHLBI Clinical Trials Has Increased over Time", *PLOS ONE* 10(8), e0132382, 2015. https://doaj.org/article/3ca4f2975c8245e09e5311375dc03103 (accessed 2026-11-12)
[^s3]: A. M. Scheel, M. R. M. J. Schijen & D. Lakens, "An Excess of Positive Results: Comparing the Standard Psychology Literature With Registered Reports", *Advances in Methods and Practices in Psychological Science* 4(2), 2021. https://www.psychologicalscience.org/journals/ampps/25152459211007467/ (accessed 2026-11-12)
[^s4]: D. A. Zarin, A. Bergeris, N. C. Ide & T. Tse, "ClinicalTrials.gov: A Report to the Board of Scientific Counselors", U.S. National Library of Medicine technical report LHNCBC-TR-2005-003, 2005. https://www.lhncbc.nlm.nih.gov/LHC-publications/PDF/tr2005003.pdf (accessed 2026-11-12)
[^s5]: A. Szollosi, D. Kellen, D. J. Navarro, R. Shiffrin, I. van Rooij & T. Van Zandt, "Is Preregistration Worthwhile?", *Trends in Cognitive Sciences*, 2020; FORRT summary. https://forrt.org/curated_resources/is-preregistration-worthwhile/ (accessed 2026-11-12)
[^s6]: A. Claesen, S. Gomes, F. Tuerlinckx & W. Vanpaemel, "Comparing dream to reality: an assessment of adherence of the first generation of preregistered studies", *Royal Society Open Science* 8(10), 2021. https://doaj.org/article/4c3b51be665d4138b3f0af7c0d8ca92c (accessed 2026-11-12)
