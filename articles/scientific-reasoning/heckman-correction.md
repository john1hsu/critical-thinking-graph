---
id: ct:heckman-correction
type: Method
title: Heckman correction
aliases: [Heckman two-step estimator, Heckit, Heckman selection model]
domain: scientific-reasoning
summary: >-
  A two-step statistical method for estimating a relationship from a
  non-randomly selected sample: first model the probability that a case is
  observed at all, then add a correction term (the inverse Mills ratio) to the
  outcome regression so the estimate accounts for who was filtered out.
level: advanced
evidenceStatus: mixed
broader: [ct:causal-inference, ct:statistical-reasoning]
related: [ct:selection-bias, ct:survivorship-bias, ct:random-sampling, ct:confounding, ct:causal-diagrams]
requires: [ct:selection-bias]
relations:
  - {predicate: counteracts, object: ct:selection-bias, source: s1, confidence: high}
  - {predicate: counteracts, object: ct:survivorship-bias, source: s2, confidence: medium}
  - {predicate: introducedBy, object: ct:james-heckman, source: s1, confidence: high}
  - {predicate: challengedBy, object: ct:puhani-2000-heckman-correction-critique, source: s3, confidence: high}
  - {predicate: appliedIn, object: ct:criminology, source: s4, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Sample selection bias as a specification error"
    publisher: Econometrica 47(1), 153-162 (Heckman, 1979), Econometric Society publication page
    url: https://www.econometricsociety.org/publications/econometrica/1979/01/01/sample-selection-bias-specification-error
    type: primary
    accessed: 2026-11-18
  - id: s2
    title: "Econometrics I, Part 19: Sample Selection"
    publisher: NYU Stern School of Business, lecture notes (William Greene)
    url: https://pages.stern.nyu.edu/~wgreene/Econometrics/Econometrics-I-19.pdf
    type: academic
    accessed: 2026-11-18
  - id: s3
    title: "The Heckman correction for sample selection and its critique"
    publisher: Journal of Economic Surveys 14(1), 53-68 (Puhani, 2000), doi:10.1111/1467-6419.00104, IDEAS/RePEc record
    url: https://ideas.repec.org/a/bla/jecsur/v14y2000i1p53-68.html
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s4
    title: "Is the magic still there? The use of the Heckman two-step correction for selection bias in criminology"
    publisher: Journal of Quantitative Criminology (Bushway, Johnson & Slocum, 2007), doi:10.1007/s10940-007-9024-4, University of Maryland author copy
    url: https://ccjs.umd.edu/sites/ccjs.umd.edu/files/pubs/HeckmanCorrection.pdf
    type: peer-reviewed
    accessed: 2026-11-18
created: 2026-11-18
---

# Heckman correction

The Heckman correction is a statistical method for learning about a whole population when the outcome you care about is only visible for a filtered subset of it.[^s1] James Heckman framed the problem as an ordinary specification error: if the cases that make it into the sample differ systematically from those that do not, a regression on the visible cases is missing a variable, namely the information about why they were selected.[^s1] The correction estimates that missing piece and puts it back into the model.[^s2] For a critical thinker, the method matters less as a formula than as a disciplined way of refusing to treat survivors as a fair sample.[^s4]

## Origin

James Heckman set out the approach in a 1979 *Econometrica* paper, which proposed a simple two-stage estimator that could be computed with standard least-squares software and derived its large-sample behaviour.[^s1] The standard motivating case is wages: wage equations are estimated from people who work, and who chooses to work is itself a selective decision, which is why Greene's teaching notes file labour supply under self-selection.[^s2][^s3] Because it needed nothing beyond ordinary regression tools, the two-step version spread well beyond economics; by the mid-2000s it was a routine fixture of quantitative criminology.[^s4]

## How it works

The method runs two linked models.[^s2] The first is a selection equation, usually a probit, that predicts whether each case is observed using data available for everyone, including the cases whose outcome is missing.[^s4] From that model, each observed case gets a correction term called the inverse Mills ratio, which summarises how unusual it was for that case to be selected.[^s2] The second step is the outcome regression, run on the observed cases with the inverse Mills ratio added as an extra predictor; if the selection and outcome errors are correlated, the term soaks up the bias, and if they are not, its coefficient is near zero.[^s2]

A workplace example: an HR analyst wants to know whether a leadership course raises managers' performance ratings two years later. Ratings exist only for managers who stayed with the company, and weak performers were more likely to leave. Comparing ratings of course-takers and non-takers among stayers would mix the course's effect with who survived. The analyst first models staying versus leaving for every manager, using factors such as commute distance or a pension vesting date that plausibly affect leaving but not performance, then adds the resulting correction term to the ratings model.[^s4] Greene's lecture notes list exactly this kind of filter, survivorship among firms and mutual funds and attrition from trials and surveys, as cases of the non-random sampling the selection model is designed for.[^s2]

## How to apply it

Use it when outcomes are missing for a subset of cases, the reason they are missing could be linked to the outcome itself, and you still have covariates for the missing cases.[^s4] Steps: (1) write down the selection process and which variables drive it; (2) find at least one exclusion restriction, a variable that affects selection but not the outcome; (3) fit the selection probit on all cases; (4) add the inverse Mills ratio to the outcome model and correct the standard errors for the estimated term; (5) compare results with uncorrected and alternative estimates.[^s4][^s2] Censored and truncated data have their own models (Tobit and truncated regression), so check which situation you are in first.[^s4]

Common pitfalls are well documented. A 2007 review of 25 criminology articles found frequent misuse: logit swapped in for probit, predicted probabilities used instead of the inverse Mills ratio, standard errors left uncorrected, and 21 of 25 studies with no exclusion restriction at all.[^s4] Without one, the model is identified only by the curvature of the probit, and the correction term becomes highly collinear with the other predictors.[^s4] The authors concluded that selection bias is at root a substantive problem rather than a technical one, and that the estimator is no cure-all.[^s4]

## Evidence

Puhani's 2000 survey of Monte Carlo studies found that the two-step estimator performs reasonably when collinearity is low, that full maximum likelihood is preferable in that case, and that when collinearity is high, simpler alternatives such as subsample least squares or a two-part model are more robust.[^s3] The method also leans on a distributional assumption, joint normality of the two error terms, so results can shift when that assumption is wrong.[^s4] Evidence status is therefore recorded as mixed: the logic of the correction is sound, but its practical reliability depends on design choices that are often skipped.[^s3][^s4]

## Connections

The Heckman correction counteracts [[selection-bias]], which Heckman's paper reframed as an omitted-variable problem that can be estimated and removed.[^s1] It also counteracts [[survivorship-bias]] in the many settings, such as fund performance and firm survival, that fit the non-random sampling structure the selection model addresses.[^s2] It was introduced by James Heckman.[^s1] Puhani's survey challenges uncritical use by showing when the two-step estimator breaks down.[^s3] It is widely applied in criminology, where sentence length, for instance, is observed only for people who are incarcerated.[^s4] It complements [[random-sampling]], which avoids the problem by design, since the bias Heckman analysed arises only when samples are selected non-randomly.[^s1]

## Sources

[^s1]: Heckman, "Sample selection bias as a specification error", Econometrica 47(1), 1979. https://www.econometricsociety.org/publications/econometrica/1979/01/01/sample-selection-bias-specification-error (accessed 2026-11-18)
[^s2]: Greene, "Econometrics I, Part 19: Sample Selection", NYU Stern lecture notes. https://pages.stern.nyu.edu/~wgreene/Econometrics/Econometrics-I-19.pdf (accessed 2026-11-18)
[^s3]: Puhani, "The Heckman correction for sample selection and its critique", Journal of Economic Surveys 14(1), 2000. https://ideas.repec.org/a/bla/jecsur/v14y2000i1p53-68.html (accessed 2026-11-18)
[^s4]: Bushway, Johnson & Slocum, "Is the magic still there? The use of the Heckman two-step correction for selection bias in criminology", Journal of Quantitative Criminology, 2007. https://ccjs.umd.edu/sites/ccjs.umd.edu/files/pubs/HeckmanCorrection.pdf (accessed 2026-11-18)
