---
id: ct:selection-bias
type: Phenomenon
title: Selection bias
aliases: [sample selection bias, selection effect]
domain: scientific-reasoning
summary: >-
  A systematic error that arises when the people or cases that end up in a
  study, sample or comparison differ from the population of interest because
  of how they were chosen, recruited or retained, so the observed association
  or estimate is distorted.
level: intermediate
evidenceStatus: robust
broader: [ct:causal-inference, ct:statistical-reasoning]
related: [ct:confounding, ct:random-sampling, ct:randomized-controlled-trial, ct:hasty-generalization, ct:berksons-paradox, ct:survivorship-bias, ct:correlation-versus-causation]
requires: [ct:random-sampling]
relations:
  - {predicate: contrastsWith, object: ct:confounding, source: s2, confidence: high}
  - {predicate: formalizedBy, object: ct:causal-diagrams, source: s2, confidence: high}
  - {predicate: studiedIn, object: ct:epidemiology, source: s1, confidence: high}
  - {predicate: studiedIn, object: ct:econometrics, source: s3, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Selection bias"
    publisher: "Catalogue of Bias, Centre for Evidence-Based Medicine, University of Oxford (Nunan, Bankhead & Aronson, 2017)"
    url: https://catalogofbias.org/biases/selection-bias/
    type: academic
    accessed: 2026-11-11
  - id: s2
    title: "A structural approach to selection bias"
    publisher: "Epidemiology 15(5):615-625 (Hernán, Hernández-Díaz & Robins, 2004), doi:10.1097/01.ede.0000135174.63482.43"
    url: https://pubmed.ncbi.nlm.nih.gov/15308962/
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s3
    title: "Sample selection bias as a specification error"
    publisher: "Econometrica 47(1):153-162 (Heckman, 1979)"
    url: https://www.econometricsociety.org/publications/econometrica/1979/01/01/sample-selection-bias-specification-error
    type: primary
    accessed: 2026-11-11
  - id: s4
    title: "The Legend of Abraham Wald"
    publisher: "American Mathematical Society Feature Column (Casselman, June 2016)"
    url: https://www.ams.org/samplings/feature-column/fc-2016-06
    type: institutional
    accessed: 2026-11-11
  - id: s5
    title: "Limitations of the application of fourfold table analysis to hospital data"
    publisher: "Biometrics 2(3):47-53 (Berkson, 1946), PubMed record 21001024"
    url: https://pubmed.ncbi.nlm.nih.gov/21001024/
    type: primary
    accessed: 2026-11-11
created: 2026-11-11
---

# Selection bias

Selection bias is a systematic error that appears when the individuals in a study, or the groups being compared, differ in a consistent way from the population the conclusion is meant to describe.[^s1] The cause is the route by which cases got into the data: who was recruited, who volunteered, who stayed until the end, or whose records happened to be kept.[^s1] Heckman described it as the bias that comes from estimating relationships with samples that were not randomly selected.[^s3]

## Origin

Worries about unrepresentative data are old, but the term covers several problems that different fields named separately. In medicine, Joseph Berkson's 1946 paper in *Biometrics* examined the limits of drawing associations from two-by-two tables built out of hospital records, an early warning that patients who reach a hospital are a filtered group.[^s5] In economics, James Heckman's 1979 *Econometrica* paper treated estimation from non-randomly selected samples as a form of omitted-variable specification error and proposed a two-step estimator, computable with ordinary least squares, to correct for it.[^s3] During the Second World War, Abraham Wald at Columbia's Statistical Research Group estimated aircraft vulnerability using damage data available only from planes that returned, explicitly modelling the hits that the missing planes would have shown; the popular "armor the engines" anecdote is, according to Bill Casselman's 2016 review of the record, largely a later reconstruction.[^s4]

In 2004 Miguel Hernán, Sonia Hernández-Díaz and James Robins argued that this umbrella term hides one shared causal structure. On their account, selection bias arises when an analysis is restricted to, or adjusts for, a variable that is affected both by the exposure (or its causes) and by the outcome (or its causes). They proposed calling bias from such shared downstream effects selection bias and reserving confounding for bias from shared upstream causes, and they argued the framework points to a common correction strategy.[^s2]

## How it works

Consider a software company that wants to know whether its onboarding programme makes customers successful. An analyst surveys accounts that are still active after six months and finds that most of them rate onboarding highly and use the product heavily, so the team concludes onboarding drives success. But staying active is influenced both by whether onboarding worked and by how successful the customer was; accounts that churned are absent from the survey. Restricting the analysis to survivors can make onboarding look more effective than it is. The data were not falsified; the filter did the work. This is the shared structure Hernán and colleagues describe: selecting on a variable downstream of both the thing studied and the outcome.[^s2]

The same pattern appears in familiar settings. Clinical trials may enrol healthy younger adults while the people who actually receive a vaccine are older and sicker, so trial results may not carry over.[^s1] People who volunteer for long-term diet and lifestyle cohorts tend to be more health-conscious, so those cohorts often show lower mortality than the general population.[^s1] Participants who drop out of a study for reasons related to the treatment or the outcome leave the remaining group unrepresentative.[^s1]

To spot selection bias, ask how each case entered the data and what would have kept a case out. If inclusion depended on the outcome, on the exposure, or on anything they both influence, the comparison is suspect.[^s1][^s2]

## Evidence

Selection bias is well documented, though its size and even its direction are often hard to pin down in a given study.[^s1] The Catalogue of Bias at Oxford's Centre for Evidence-Based Medicine reports that a 1978 door-to-door survey of Parkinson's disease in Copiah County, Mississippi found 13 of 31 cases had never received medical care, so a study relying on medical records would have missed over 40% of cases.[^s1] The same entry describes how observational studies suggested hormone replacement therapy protected women against coronary heart disease, while later randomized trials suggested it might raise risk; the women who chose the therapy were more active, more health-conscious and better off.[^s1] It also cites a 2018 analysis of oral-health trials in which trials with inadequate or unclear random sequence generation reported larger effects (difference in effect size 0.13), and a 2001 study in which selection bias overestimated preterm infant survival by as much as 100%.[^s1]

Remedies exist but are partial. In trials, adequate randomization, concealed allocation and intention-to-treat analysis protect against it; in observational research, methods such as imputation, sensitivity analyses and inverse probability weighting can help under stated assumptions but rarely remove the bias entirely.[^s1] Heckman's two-step correction depends on modelling the selection process correctly.[^s3]

## Connections

- **Contrasts with confounding.** In the structural account, confounding comes from common causes of exposure and outcome, while selection bias comes from conditioning on their common effects, so the two need different fixes.[^s2] Self-selection can also introduce confounding, as in the hormone therapy studies.[^s1]
- **Formalized by causal diagrams,** which Hernán, Hernández-Díaz and Robins use to show that case-control, cohort and censoring biases share one mechanism.[^s2]
- **Studied in epidemiology,** where clinical and observational research catalogue its forms and preventive steps.[^s1]
- **Studied in econometrics,** where Heckman framed it as a specification error with a correction estimator.[^s3]
- **Counteracted by randomized controlled trials and random sampling,** since randomization and allocation concealment are the central safeguards against it in trials.[^s1]
- **Related to survivorship bias and Berkson's paradox,** two named forms that arise when only survivors or only hospital patients are observed,[^s4][^s5] and to hasty generalization, the everyday-argument version of concluding about a population from a group that differs systematically from it.[^s1]

## Sources

[^s1]: Nunan, Bankhead & Aronson, "Selection bias", Catalogue of Bias, CEBM, University of Oxford (2017). https://catalogofbias.org/biases/selection-bias/ (accessed 2026-11-11)
[^s2]: Hernán, Hernández-Díaz & Robins, "A structural approach to selection bias", Epidemiology 15(5):615-625 (2004). https://pubmed.ncbi.nlm.nih.gov/15308962/ (accessed 2026-11-11)
[^s3]: Heckman, "Sample selection bias as a specification error", Econometrica 47(1):153-162 (1979). https://www.econometricsociety.org/publications/econometrica/1979/01/01/sample-selection-bias-specification-error (accessed 2026-11-11)
[^s4]: Casselman, "The Legend of Abraham Wald", AMS Feature Column (2016). https://www.ams.org/samplings/feature-column/fc-2016-06 (accessed 2026-11-11)
[^s5]: Berkson, "Limitations of the application of fourfold table analysis to hospital data", Biometrics 2(3):47-53 (1946). https://pubmed.ncbi.nlm.nih.gov/21001024/ (accessed 2026-11-11)
