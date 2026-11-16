---
id: ct:p-hacking
type: Phenomenon
title: P-hacking
aliases: [p hacking, data dredging for significance, significance chasing, selective inference to significance]
domain: scientific-reasoning
summary: >-
  The practice of collecting, selecting or analysing data in several ways
  until a non-significant result crosses the p < .05 threshold, then reporting
  only the version that "worked", which inflates false positives and effect
  sizes in the published record.
level: intermediate
evidenceStatus: mixed
broader: [ct:questionable-research-practices]
related: [ct:researcher-degrees-of-freedom, ct:publication-bias, ct:preregistration, ct:replication-crisis, ct:null-hypothesis-significance-testing, ct:p-curve, ct:harking, ct:cherry-picking]
requires: [ct:null-hypothesis-significance-testing]
relations:
  - {predicate: instanceOf, object: ct:questionable-research-practices, source: s4, confidence: high}
  - {predicate: explainedBy, object: ct:publication-bias, source: s4, confidence: medium}
  - {predicate: amplifies, object: ct:replication-crisis, source: s4, confidence: medium}
  - {predicate: demonstratedBy, object: ct:head-2015-extent-of-p-hacking-study, source: s1, confidence: medium}
  - {predicate: supportedBy, object: ct:john-2012-questionable-research-practices-survey, source: s3, confidence: medium}
  - {predicate: challengedBy, object: ct:hartgerink-2017-reanalysis-of-head-2015, source: s5, confidence: high}
  - {predicate: challengedBy, object: ct:fiedler-schwarz-2016-qrp-prevalence-critique, source: s6, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "The Extent and Consequences of P-Hacking in Science"
    publisher: "PLoS Biology 13(3), e1002106 (Head, Holman, Lanfear, Kahn & Jennions, 2015)"
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4359000/
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s2
    title: "P-curve: A key to the file-drawer"
    publisher: "Journal of Experimental Psychology: General 143(2), 534-547 (Simonsohn, Nelson & Simmons, 2014); copy hosted at UC San Diego"
    url: https://pages.ucsd.edu/~cmckenzie/Simonsohnetal2014JEPGeneral.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s3
    title: "Measuring the Prevalence of Questionable Research Practices With Incentives for Truth Telling"
    publisher: "Psychological Science 23(5), 524-532 (John, Loewenstein & Prelec, 2012); author copy, Carnegie Mellon University"
    url: https://www.cmu.edu/dietrich/sds/docs/loewenstein/MeasPrevalQuestTruthTelling.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s4
    title: "Reproducibility of Scientific Results"
    publisher: "Stanford Encyclopedia of Philosophy (Fiona Fidler & John Wilcox, 2018)"
    url: https://plato.stanford.edu/entries/scientific-reproducibility/
    type: scholarly-encyclopedia
    accessed: 2026-11-16
  - id: s5
    title: "Reanalyzing Head et al. (2015): investigating the robustness of widespread p-hacking"
    publisher: "PeerJ 5, e3068 (C. H. J. Hartgerink, 2017)"
    url: https://peerj.com/articles/3068
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s6
    title: "Questionable Research Practices Revisited"
    publisher: "Social Psychological and Personality Science 7(1), 45-52 (Fiedler & Schwarz, 2016); course copy, University of Wisconsin-Madison"
    url: https://online225.psych.wisc.edu/wp-content/uploads/225-Master/225-UnitPages/Unit-10/Fiedler_SPPS_2015.pdf
    type: peer-reviewed
    accessed: 2026-11-16
created: 2026-11-16
---

# P-hacking

P-hacking is collecting, selecting or analysing data until a result that was not statistically significant becomes significant, and then presenting that version as if it were the only analysis run.[^s1] Typical moves include peeking at the data midway and deciding whether to keep collecting, measuring many outcomes and reporting the ones that cross the line, dropping or keeping outliers depending on what they do to the p-value, regrouping conditions, adding or removing covariates after seeing results, and rounding a p-value such as .053 down to "p < .05".[^s1][^s4] The Stanford Encyclopedia of Philosophy lists it among the questionable research practices, alongside cherry-picking and HARKing (presenting unexpected findings as if they had been predicted).[^s4]

## Origin

The label comes from the methodological reform debate in psychology in the early 2010s. Uri Simonsohn, Leif Nelson and Joseph Simmons used it for the exploitation of ambiguity in data collection and analysis, with the failed analyses quietly filed away, and pointed out that it defeats the old reassurance that a literature would need many unpublished null studies to produce a false finding: one dataset, analysed several ways, is enough.[^s2] Fidler and Wilcox place the practice within a wider family of questionable research practices that inflate false-positive rates, and link it to publication bias: when journals favour significant results, researchers cannot afford to leave null studies in the file drawer, so they massage them toward significance instead.[^s4]

## How it works

A significance test promises that, when there is no real effect, a result as extreme as the one observed turns up only about 5% of the time. That promise holds for a single planned analysis. Each extra outcome, stopping point, exclusion rule or model tried is another draw, and reporting only the draw that crossed .05 lets noise pass as discovery.[^s4] Because p-hackers tend to stop as soon as they reach significance, their results pile up just under the threshold.[^s2]

**Workplace example.** An operations team pilots new scheduling software in one warehouse and compares picking errors with a sister site. After three weeks the difference is not significant, so the analyst extends the pilot "to get more data", checks again weekly, then looks separately at night and day shifts, at error rate per order and per item, and finally excludes a week disrupted by a holiday. On the fourth combination the night-shift error rate per item shows p = .04, and that is the slide presented to management. No single choice was dishonest, but the reported p-value no longer means what it says. A fairer report would list every comparison tried and treat the night-shift finding as a hypothesis for a pre-specified follow-up test.[^s1][^s4]

## Evidence

**Self-reports.** John, Loewenstein and Prelec surveyed more than 2,000 US academic psychologists in 2012, using a truth-telling incentive. Among respondents in that condition, about two-thirds admitted having left some outcome measures out of a paper, 58% admitted deciding whether to collect more data after checking significance, and 43% admitted excluding data after seeing its effect on results; the authors judged these figures likely to be underestimates.[^s3] Fiedler and Schwarz challenged that reading in 2016. They argued that several items were ambiguous and could describe legitimate judgment calls, and that the share of researchers who had *ever* done something is not the prevalence of the practice. In their survey of 1,138 German psychologists, admission rates ran roughly five times higher than estimated prevalence across published findings, although clear violations were not zero.[^s6]

**The p-value record.** Simonsohn, Nelson and Simmons proposed p-curve, the distribution of significant p-values across a set of findings: true effects produce a right skew (more values near .01 than near .04), while intense p-hacking produces a left skew toward .05.[^s2] Head and colleagues text-mined p-values from open-access biomedical papers in 2015 and reported both evidential value in every discipline and a bump just below .05 consistent with widespread p-hacking. They concluded that the practice was common but weak relative to real effects, and unlikely to overturn meta-analytic conclusions.[^s1] Hartgerink's 2017 reanalysis showed the bump depended on how rounded two-decimal p-values were binned; after correcting for this, he found no evidence of a left skew and called the case for widespread p-hacking of that kind ambiguous at best, while stressing that other forms may leave no bump.[^s5]

**Limitations.** The status is therefore mixed: the mechanism by which flexible analysis inflates false positives is uncontested, but how often it happens, and how much it distorts a given literature, is still argued over.[^s4][^s5][^s6] P-curve itself cannot see non-significant results and can miss null effects mixed with true ones.[^s2]

## Connections

P-hacking is an **instance of questionable research practices**, and Fidler and Wilcox treat **publication bias** as part of the explanation for why researchers do it; together these practices inflate false positives and **amplify the replication crisis**.[^s4] Its prevalence is **demonstrated by Head and colleagues' 2015 text-mining study** and **supported by John and colleagues' 2012 survey**, but **challenged by Hartgerink's 2017 reanalysis** and by **Fiedler and Schwarz's critique** of survey-based prevalence figures.[^s1][^s3][^s5][^s6] It is the opportunistic use of **researcher degrees of freedom**, the ambiguity in data collection and analysis that Simonsohn and colleagues describe p-hackers exploiting.[^s2] **Preregistration** fixes analysis choices in advance and helps keep the false-positive rate at the stated alpha, and **p-curve** offers a way to check a body of findings for signs of it.[^s2][^s4] Understanding it requires **null-hypothesis significance testing**, whose single-analysis assumptions it violates.[^s4]

## Sources

[^s1]: Head, M. L., Holman, L., Lanfear, R., Kahn, A. T., & Jennions, M. D. (2015). "The Extent and Consequences of P-Hacking in Science", PLoS Biology 13(3), e1002106. https://pmc.ncbi.nlm.nih.gov/articles/PMC4359000/ (accessed 2026-11-16)
[^s2]: Simonsohn, U., Nelson, L. D., & Simmons, J. P. (2014). "P-curve: A key to the file-drawer", Journal of Experimental Psychology: General 143(2), 534-547. https://pages.ucsd.edu/~cmckenzie/Simonsohnetal2014JEPGeneral.pdf (accessed 2026-11-16)
[^s3]: John, L. K., Loewenstein, G., & Prelec, D. (2012). "Measuring the Prevalence of Questionable Research Practices With Incentives for Truth Telling", Psychological Science 23(5), 524-532. https://www.cmu.edu/dietrich/sds/docs/loewenstein/MeasPrevalQuestTruthTelling.pdf (accessed 2026-11-16)
[^s4]: Fidler, F., & Wilcox, J. (2018). "Reproducibility of Scientific Results", Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/entries/scientific-reproducibility/ (accessed 2026-11-16)
[^s5]: Hartgerink, C. H. J. (2017). "Reanalyzing Head et al. (2015): investigating the robustness of widespread p-hacking", PeerJ 5, e3068. https://peerj.com/articles/3068 (accessed 2026-11-16)
[^s6]: Fiedler, K., & Schwarz, N. (2016). "Questionable Research Practices Revisited", Social Psychological and Personality Science 7(1), 45-52. https://online225.psych.wisc.edu/wp-content/uploads/225-Master/225-UnitPages/Unit-10/Fiedler_SPPS_2015.pdf (accessed 2026-11-16)
