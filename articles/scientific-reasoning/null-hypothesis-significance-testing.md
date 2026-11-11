---
id: ct:null-hypothesis-significance-testing
type: Method
title: Null-hypothesis significance testing
aliases: [NHST, significance testing, statistical significance testing, p-value testing, null ritual]
domain: scientific-reasoning
summary: >-
  The statistical procedure of assuming a "no effect" null hypothesis,
  computing a p-value (the probability, under that model, of data at least as
  extreme as those observed) and declaring a result "statistically
  significant" when the p-value falls below a preset threshold, usually 0.05.
level: intermediate
evidenceStatus: contested
broader: [ct:hypothesis-testing, ct:statistical-reasoning]
related: [ct:power-analysis, ct:researcher-degrees-of-freedom, ct:replication-crisis, ct:p-hacking, ct:publication-bias, ct:preregistration, ct:inverse-fallacy, ct:randomized-controlled-trial, ct:conditional-probability, ct:gerd-gigerenzer]
requires: [ct:hypothesis-testing, ct:conditional-probability]
relations:
  - {predicate: introducedBy, object: ct:ronald-fisher, source: s1, confidence: medium}
  - {predicate: influencedBy, object: ct:jerzy-neyman, source: s2, confidence: high}
  - {predicate: contrastsWith, object: ct:bayesian-reasoning, source: s3, confidence: medium}
  - {predicate: studiedIn, object: ct:statistics, source: s3, confidence: high}
  - {predicate: challengedBy, object: ct:amrhein-2019-retire-statistical-significance, source: s5, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Statistical Methods for Research Workers, Chapter III: Distributions"
    publisher: Oliver and Boyd (Fisher, 1925), Classics in the History of Psychology, York University
    url: https://www.yorku.ca/pclassic/Fisher/Methods/chap3.htm
    type: primary
    accessed: 2026-11-11
  - id: s2
    title: "Mindless statistics"
    publisher: The Journal of Socio-Economics 33, 587-606 (Gigerenzer, 2004), hosted copy at Oklahoma State University
    url: https://psychology.okstate.edu/faculty/jgrice/psyc4333/GG_Mindless_2004.pdf
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s3
    title: "The ASA's statement on p-values: context, process, and purpose"
    publisher: The American Statistician 70(2), 129-133 (Wasserstein & Lazar, 2016), hosted copy at UC Berkeley
    url: https://www.stat.berkeley.edu/%7Ealdous/Real_World/ASA_statement.pdf
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s4
    title: "Redefine statistical significance"
    publisher: Nature Human Behaviour 2, 6-10 (Benjamin et al., 2018), Utrecht University repository
    url: https://dspace.library.uu.nl/handle/1874/360978
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s5
    title: "Scientists rise up against statistical significance"
    publisher: Nature 567, 305-307 (Amrhein, Greenland & McShane, 2019), NASA ADS record
    url: https://ui.adsabs.harvard.edu/abs/2019Natur.567..305A
    type: primary
    accessed: 2026-11-11
created: 2026-11-11
---

# Null-hypothesis significance testing

Null-hypothesis significance testing (NHST) is the most widely used statistical decision procedure in the empirical sciences. The analyst assumes a null hypothesis, typically "no difference" or "zero correlation", computes a p-value, and calls the result statistically significant if that p-value is below a cutoff, conventionally 0.05.[^s2] The American Statistical Association (ASA) defines the p-value informally as the probability, under a specified statistical model, that a summary of the data would be equal to or more extreme than the value actually observed.[^s3] A small p-value therefore says the data fit the null model poorly; it does not by itself say how likely any hypothesis is, how big an effect is, or whether it matters.[^s3]

## Origin

Ronald Fisher popularised significance tests in *Statistical Methods for Research Workers* (1925). Discussing the normal distribution, he noted that a probability of 1 in 20 corresponds to a deviation of roughly two standard deviations and suggested treating that point as a practical limit for judging whether a deviation is significant, while acknowledging that some real effects would be missed.[^s1] Fisher later rejected any fixed conventional level and urged researchers to report exact p-values.[^s2] In the 1930s Jerzy Neyman and Egon Pearson proposed a different framework: two explicit hypotheses, error rates alpha (Type I) and beta (Type II) and the sample size fixed in advance from the costs of each error, with power equal to 1 minus beta and "accepting" a hypothesis meaning acting as if it were true.[^s2] Gerd Gigerenzer argues that textbook NHST is a hybrid of the two that neither camp endorsed: Fisher's lone null hypothesis joined to Neyman-Pearson's yes/no decision, with the threshold frozen at 5% by convention. He calls the routine form the "null ritual".[^s2]

## How it works

An online retailer runs an A/B test of a new checkout button. The null hypothesis is that the new button converts no better than the old one. After two weeks the new version shows a slightly higher conversion rate, and the test reports p = 0.03. Under NHST the team declares the difference significant and rejects the null.[^s2] What that p-value licenses is narrow: if the null model and all its assumptions held, a difference at least this large would turn up about 3% of the time.[^s3] It is not a 97% chance that the new button is better, it is not the probability that chance alone produced the result, and with a large enough sample a commercially trivial lift can still give a tiny p-value.[^s3] If the team had also tracked several other metrics and reported only the one that crossed 0.05, the p-value would be close to uninterpretable.[^s3]

These misreadings are common even among experts. In a 2002 survey by Haller and Krauss summarised by Gigerenzer, every psychology student and about 80% of statistics teachers at six German universities endorsed at least one false statement about what p = 0.01 means.[^s2] The most popular error, endorsed by about 70% of each group, was that the p-value gives the probability of wrongly rejecting the null.[^s2]

## How to apply it

1. **Plan before collecting data.** State the hypotheses, the analysis and the sample size in advance, ideally with a power analysis, so that a non-significant result is informative.[^s2]
2. **Report exact p-values and every analysis run.** Selective reporting of the tests that "worked" invalidates the numbers that remain, so disclose all hypotheses explored and all p-values computed.[^s3]
3. **Pair the p-value with estimates.** Give effect sizes and confidence or credibility intervals, and judge practical importance separately from statistical significance.[^s3]
4. **Do not treat the threshold as a bright line.** A p-value near 0.05 is weak evidence on its own, and a large p-value does not show the null is true; decisions should also weigh study design, measurement quality and outside evidence.[^s3]
5. **Consider complementary methods.** The ASA lists Bayesian methods, likelihood ratios, Bayes factors, decision-theoretic models and false discovery rates as alternatives or supplements.[^s3]

## Evidence and limitations

Criticism of NHST is long-standing, but it intensified with the replication crisis. In 2016 the ASA issued its first formal statement on a specific statistical practice, prompted partly by a psychology journal's ban on p-values; its six principles stress that p-values measure incompatibility with a model, not the truth of a hypothesis or the size of an effect.[^s3] Reformers disagree about the remedy. A 72-author group led by Daniel Benjamin proposed in 2018 lowering the default threshold for claims of new discoveries from 0.05 to 0.005.[^s4] In 2019 Valentin Amrhein, Sander Greenland and Blake McShane, backed by more than 800 signatories, argued instead for abandoning the dichotomy of "significant" versus "non-significant" altogether, because it fuels overclaiming and the dismissal of possibly important effects.[^s5] NHST remains standard in journals, trials and industry experiments, so the practical question for a critical thinker is less whether to use it than how to read it correctly.[^s3]

## Connections

NHST is a statistical specialisation of **hypothesis testing** and part of **statistical reasoning**, and it assumes a working grasp of **conditional probability**, since a p-value is a probability of data given the null rather than of the null given data.[^s3] Its significance-test core was **introduced by Ronald Fisher**, and the decision form taught today was **influenced by Jerzy Neyman** and Egon Pearson's error-rate framework.[^s1][^s2] It is **studied in statistics** and **contrasts with Bayesian reasoning**, which the ASA names among the main alternative ways of weighing evidence.[^s3] The method is **challenged by Amrhein and colleagues' 2019 call to retire statistical significance**, while the Benjamin proposal to tighten the threshold is a reform from within.[^s4][^s5] **Power analysis** supplies the sample-size planning NHST needs, and **researcher degrees of freedom**, **p-hacking**, **publication bias** and **preregistration** concern how selective analysis and reporting distort, or protect, the meaning of p-values.[^s2][^s3]

## Sources

[^s1]: Fisher, *Statistical Methods for Research Workers*, Ch. III (1925), Classics in the History of Psychology. https://www.yorku.ca/pclassic/Fisher/Methods/chap3.htm (accessed 2026-11-11)
[^s2]: Gigerenzer, "Mindless statistics", The Journal of Socio-Economics 33 (2004), 587-606. https://psychology.okstate.edu/faculty/jgrice/psyc4333/GG_Mindless_2004.pdf (accessed 2026-11-11)
[^s3]: Wasserstein & Lazar, "The ASA's statement on p-values: context, process, and purpose", The American Statistician 70(2) (2016), 129-133. https://www.stat.berkeley.edu/%7Ealdous/Real_World/ASA_statement.pdf (accessed 2026-11-11)
[^s4]: Benjamin et al., "Redefine statistical significance", Nature Human Behaviour 2 (2018), 6-10. https://dspace.library.uu.nl/handle/1874/360978 (accessed 2026-11-11)
[^s5]: Amrhein, Greenland & McShane, "Scientists rise up against statistical significance", Nature 567 (2019), 305-307. https://ui.adsabs.harvard.edu/abs/2019Natur.567..305A (accessed 2026-11-11)
