---
id: ct:researcher-degrees-of-freedom
type: Concept
title: Researcher degrees of freedom
aliases: [analytic flexibility, garden of forking paths, undisclosed flexibility]
domain: scientific-reasoning
summary: >-
  The many often-arbitrary choices a researcher makes in framing hypotheses,
  designing a study, collecting and analysing data and reporting results;
  when those choices are made after seeing the data, or left undisclosed,
  they can make a false hypothesis look statistically significant.
level: intermediate
evidenceStatus: robust
broader: [ct:scientific-method, ct:statistical-reasoning]
related: [ct:replication-crisis, ct:preregistration, ct:null-hypothesis-significance-testing, ct:confirmation-bias, ct:multiverse-analysis]
requires: [ct:hypothesis-testing]
relations:
  - {predicate: introducedBy, object: ct:joseph-p-simmons, source: s1, confidence: high}
  - {predicate: introducedIn, object: ct:false-positive-psychology, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: ct:silberzahn-2018-many-analysts-study, source: s4, confidence: high}
  - {predicate: confusedWith, object: ct:p-hacking, source: s3, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "False-Positive Psychology: Undisclosed Flexibility in Data Collection and Analysis Allows Presenting Anything as Significant"
    publisher: Psychological Science 22(11), 1359-1366 (Simmons, Nelson & Simonsohn, 2011); author copy on SSRN
    url: https://papers.ssrn.com/abstract=1850704
    type: primary
    accessed: 2026-11-07
  - id: s2
    title: "Degrees of Freedom in Planning, Running, Analyzing, and Reporting Psychological Studies: A Checklist to Avoid p-Hacking"
    publisher: Frontiers in Psychology 7 (Wicherts, Veldkamp, Augusteijn, Bakker, van Aert & van Assen, 2016)
    url: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2016.01832/pdf
    type: peer-reviewed
    accessed: 2026-11-07
  - id: s3
    title: "The garden of forking paths: Why multiple comparisons can be a problem, even when there is no fishing expedition or p-hacking"
    publisher: Columbia University, Department of Statistics working paper (Gelman & Loken, 2013)
    url: https://sites.stat.columbia.edu/gelman/research/unpublished/forking.pdf
    type: academic
    accessed: 2026-11-07
  - id: s4
    title: "Many Analysts, One Data Set: Making Transparent How Variations in Analytic Choices Affect Results"
    publisher: Advances in Methods and Practices in Psychological Science 1(3), 337-356 (Silberzahn, Uhlmann, Martin, Anselmi et al., 2018)
    url: https://dare.uva.nl/id/0785a9cc-2470-4a3a-bea8-0f34828953c2
    type: peer-reviewed
    accessed: 2026-11-07
created: 2026-11-07
---

# Researcher degrees of freedom

Researcher degrees of freedom are the choices, many of them defensible but arbitrary, that a researcher makes while formulating a hypothesis and designing, running, analysing and reporting a study.[^s2] Each choice on its own looks harmless: which outcome measure to treat as primary, which participants to exclude, when to stop collecting data, which covariates to include. The problem is that when these choices are made opportunistically, or are shaped by the data already in hand, the actual chance of a false-positive result rises far above the nominal 5% that a significance test advertises, and reported effect sizes tend to be inflated.[^s1][^s2] The concept explains how honest researchers can publish findings that later fail to replicate.

## Origin

The term was popularised by Joseph Simmons, Leif Nelson and Uri Simonsohn in "False-Positive Psychology", published in *Psychological Science* in 2011.[^s1] Using computer simulations and two real experiments, they showed how easily flexibility in data collection, analysis and reporting lets a researcher accumulate and report significant evidence for a hypothesis that is false; in many situations a researcher was more likely to find support for a non-existent effect than to correctly conclude there was none.[^s1] Their remedy was disclosure-based: six requirements for authors and four guidelines for reviewers.[^s1]

In a 2013 working paper, statisticians Andrew Gelman and Eric Loken argued that the problem does not need deliberate fishing. Researchers usually run one analysis that seems reasonable for the data they have, without noticing that different data would have led them to a different, equally reasonable analysis. They called this the "garden of forking paths": because a p-value depends on what would have been done with other possible datasets, a significant result reached along a data-dependent path cannot be taken at face value.[^s3] They stressed that Simmons and colleagues had not accused researchers of cheating.[^s3]

## How it works

Wicherts and colleagues catalogued 34 degrees of freedom across five phases of a study.[^s2] Examples include stating a vague hypothesis without a predicted direction; measuring the same outcome several ways; running without a power analysis or a sampling plan; setting the stopping rule based on interim significance tests; handling missing data and outliers ad hoc; picking the dependent variable or inclusion criteria after the fact; choosing a one- or two-sided test once results are known; and not reporting failed studies.[^s2] Each fork offers another chance for noise to cross the significance threshold.

**Workplace example.** A marketing analyst runs an A/B test of a new email subject line. She tracks open rate, click rate and revenue per recipient, checks the dashboard daily, and plans to stop "when the result is clear." After a week, no metric differs overall. She then drops recipients flagged as likely bots, using a cutoff chosen after looking at the data, and finds that click rate is significantly higher for mobile users. Every step was plausible, yet with three outcomes, repeated peeking, a post-hoc exclusion rule and a subgroup split, the chance that pure noise produced a "win" is far greater than 5%.[^s1][^s2] The honest report is that the subgroup finding is exploratory and needs a fresh, pre-specified test.[^s3]

## How to apply it

1. When reading a study or a business analysis, ask which choices could have gone another way: outcomes, exclusions, stopping rule, subgroups, covariates.[^s2]
2. Check whether those choices were fixed in advance. Wicherts and colleagues call a specific, precise and exhaustive preregistration the preferred counter, and warn that vague preregistrations still leave room for p-hacking.[^s2]
3. Distinguish exploratory from confirmatory results, and treat findings from flexible analyses as hypotheses to be tested again, ideally in a preregistered replication.[^s3]
4. Report all measures, conditions and exclusions, and how the sample size was decided, as Simmons and colleagues require.[^s1]
5. Where many analyses are reasonable, show them all, for example with multilevel models that analyse all comparisons together rather than spotlighting the one that worked.[^s3]

## Evidence and limitations

The clearest demonstration that analytic choices alone change conclusions comes from Silberzahn and colleagues' 2018 crowdsourced study: 29 teams of 61 analysts were given the same dataset and asked whether soccer referees give more red cards to dark-skinned players. Estimated odds ratios ranged from 0.89 to 2.93 (median 1.31); 20 teams found a significant positive effect and 9 did not.[^s4] No team was fishing, yet reasonable choices produced a spread of answers.[^s4] Simmons and colleagues' simulations show the same inflation mathematically for false hypotheses.[^s1]

Limitations: flexibility is not wrongdoing, and many degrees of freedom cannot be removed, only disclosed or fixed in advance.[^s3] Preregistration is often impractical for observational research, and a preregistered plan protects only as far as it is specific.[^s2][^s3] Checklists flag where bias could enter but cannot show that it did in any particular study.[^s2]

## Connections

Researcher degrees of freedom was **introduced by Joseph Simmons** and colleagues **in "False-Positive Psychology"** (2011).[^s1] It is commonly **confused with p-hacking**: Gelman and Loken argue that p-hacking implies conscious, repeated testing, whereas the forking-paths problem arises even with a single, sincere analysis.[^s3] The effect of analytic flexibility is **demonstrated by Silberzahn and colleagues' many-analysts study**.[^s4] It sits within the **scientific method** and **statistical reasoning**, assumes familiarity with **hypothesis testing** and **null-hypothesis significance testing**, and is a key part of explanations of the **replication crisis**.[^s1][^s3] **Preregistration** and **multiverse analysis** are the main remedies, and data-dependent choices can be steered by **confirmation bias** toward the expected result.[^s2][^s3]

## Sources

[^s1]: Simmons, J. P., Nelson, L. D., & Simonsohn, U. (2011). "False-Positive Psychology: Undisclosed Flexibility in Data Collection and Analysis Allows Presenting Anything as Significant", Psychological Science 22(11), 1359-1366. https://papers.ssrn.com/abstract=1850704 (accessed 2026-11-07)
[^s2]: Wicherts, J. M., Veldkamp, C. L. S., Augusteijn, H. E. M., Bakker, M., van Aert, R. C. M., & van Assen, M. A. L. M. (2016). "Degrees of Freedom in Planning, Running, Analyzing, and Reporting Psychological Studies: A Checklist to Avoid p-Hacking", Frontiers in Psychology 7. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2016.01832/pdf (accessed 2026-11-07)
[^s3]: Gelman, A., & Loken, E. (2013). "The garden of forking paths: Why multiple comparisons can be a problem, even when there is no 'fishing expedition' or 'p-hacking' and the research hypothesis was posited ahead of time", Columbia University working paper. https://sites.stat.columbia.edu/gelman/research/unpublished/forking.pdf (accessed 2026-11-07)
[^s4]: Silberzahn, R., Uhlmann, E. L., Martin, D. P., Anselmi, P., et al. (2018). "Many Analysts, One Data Set: Making Transparent How Variations in Analytic Choices Affect Results", Advances in Methods and Practices in Psychological Science 1(3), 337-356. https://dare.uva.nl/id/0785a9cc-2470-4a3a-bea8-0f34828953c2 (accessed 2026-11-07)
