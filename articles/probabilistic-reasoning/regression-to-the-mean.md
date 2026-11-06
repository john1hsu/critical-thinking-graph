---
id: ct:regression-to-the-mean
type: Phenomenon
title: Regression to the mean
aliases: [regression toward the mean, regression towards mediocrity, reversion to the mean]
domain: probabilistic-reasoning
summary: >-
  The statistical tendency for cases picked out because they scored unusually
  high or low on one measurement to score closer to the average when measured
  again, simply because the two measurements are imperfectly correlated. It
  can make chance fluctuation look like the effect of a treatment, policy or
  reward.
level: introductory
evidenceStatus: robust
broader: [ct:statistical-reasoning]
related: [ct:representativeness-heuristic, ct:outside-view, ct:randomized-controlled-trial, ct:overconfidence-effect, ct:base-rate-neglect, ct:correlation-versus-causation]
requires: []
relations:
  - {predicate: introducedBy, object: ct:francis-galton, source: s3, confidence: high}
  - {predicate: confusedWith, object: ct:placebo-effect, source: s2, confidence: medium}
  - {predicate: appliedIn, object: ct:clinical-research, source: s2, confidence: high}
  - {predicate: studiedIn, object: ct:epidemiology, source: s1, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Regression to the mean: what it is and how to deal with it"
    publisher: International Journal of Epidemiology 34(1), 215-220 (Barnett, van der Pols & Dobson, 2005), PubMed record
    url: https://pubmed.ncbi.nlm.nih.gov/15333621/
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s2
    title: "Effect of regression to the mean on decision making in health care"
    publisher: BMJ 326(7398), 1083-1084 (Morton & Torgerson, 2003), White Rose Research Online author copy
    url: https://eprints.whiterose.ac.uk/42/1/1083.pdf
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s3
    title: "Regression towards Mediocrity in Hereditary Stature"
    publisher: Journal of the Anthropological Institute 15, 246-263 (Galton, 1886), offprint record, Wellcome Collection
    url: https://wellcomecollection.org/works/sf54qjj5
    type: primary
    accessed: 2026-11-06
  - id: s4
    title: "On the Psychology of Prediction"
    publisher: Oregon Research Institute Research Bulletin 12(4) (Kahneman & Tversky, 1972), University of Oregon Scholars' Bank
    url: https://scholarsbank.uoregon.edu//bitstreams/2fbae090-7a99-4301-8402-26e6e3a4c00c/download
    type: primary
    accessed: 2026-11-06
created: 2026-11-06
---

# Regression to the mean

Regression to the mean is what happens when a group is chosen because its members scored at an extreme on one measurement and is then measured again: on the second occasion the group's average lies closer to the population average, even if nothing has been done to it.[^s2] The effect follows from ordinary variation in repeated measurements, and it can make that natural variation look like real change.[^s1] It is not a force pulling individuals back; it is a property of selecting on extreme values when two measurements are not perfectly correlated.[^s2]

## Origin

Francis Galton named the pattern in an 1886 paper in the *Journal of the Anthropological Institute*, "Regression towards Mediocrity in Hereditary Stature," where "mediocrity" meant the average.[^s3] Comparing 930 adult children with their parents, he found that the children of unusually tall parents tended to be shorter than their parents, and the children of unusually short parents tended to be taller.[^s2] The paper appeared in the journal's 1886 volume, although Galton's own offprint is catalogued as 1885.[^s3]

In psychology, Daniel Kahneman and Amos Tversky's 1972 report *On the Psychology of Prediction* showed that people rarely anticipate regression and, when they see it, tend to invent causal stories to explain it.[^s4]

## How it works

Any measured score mixes a stable component with a chance component such as luck, measurement error or a good or bad day. Selecting the most extreme scorers disproportionately picks people whose chance component happened to be large in that direction, and that component does not reliably repeat.[^s2] The effect therefore grows as measurement error grows and as the correlation between the two measurements falls, and it is largest when follow-up is restricted to a subgroup chosen for an extreme baseline value.[^s1][^s2]

A workplace example: a sales director sends the ten lowest-performing representatives from the first quarter to a coaching course. In the second quarter their average results improve and the course is declared a success. But some of those ten were simply unlucky in the first quarter (a lost client, a slow territory), and their figures would have recovered anyway. Without a comparable group that did not receive coaching, the improvement cannot be attributed to the course.[^s1][^s2]

Kahneman and Tversky's best-known illustration comes from flight training. Instructors observed that trainees who were praised after an excellent manoeuvre usually did worse on the next attempt, and concluded that praise was counterproductive.[^s4] Regression alone predicts this pattern, because an exceptional performance is likely to be followed by a more typical one whatever the instructor says. Since we tend to reward good performances and punish bad ones, regression can make punishment appear to work and reward appear to backfire.[^s4]

## How to spot and handle it

Suspect regression whenever people, sites or units were selected *because* they were unusually good or bad: the worst-ranked hospitals, the accident black spot, the patients with the most severe symptoms at enrolment.[^s2] Morton and Torgerson give health-care examples: over 80% of women who lost bone density in their first year of osteoporosis treatment gained it in the second year without any change in therapy, and the reported 75-90% fall in meningitis C cases after vaccination overstated the vaccine's contribution because part of the drop would have occurred anyway.[^s2]

The main defences are in study design and analysis. Randomise extreme units to an intervention or a control group, so that both regress equally and only the difference is credited to the intervention; take several baseline measurements and average them rather than acting on a single high reading; and use statistical methods that adjust for the baseline value.[^s1][^s2] In forecasting, Kahneman and Tversky's normative point is that predictions should be pulled toward the average more strongly the less reliable the evidence is, whereas intuitive predictions stay close to the extreme input.[^s4]

## Evidence

Regression to the mean is a mathematical consequence of imperfect correlation, so its existence is not in dispute; the practical question is how much of a given change it explains.[^s1] Barnett and colleagues conclude that it is ubiquitous in repeated measurements and should be considered as a possible explanation whenever change is observed.[^s1] The cognitive claim, that people neglect it, rests on Kahneman and Tversky's problems: no graduate student who answered the flight-training question mentioned regression, and on an IQ problem 73 of 108 respondents gave confidence intervals centred on the extreme observed score of 140.[^s4] Those findings come from small question-based samples, so the size of the neglect in expert settings is less certain than the statistical effect itself.[^s4]

## Connections

- **Introduced by** Francis Galton, whose 1886 study of heredity in stature named the effect.[^s3]
- **Confused with** the placebo effect: patients enrolled at their worst often improve on placebo, and part of that apparent placebo response may be regression.[^s2]
- **Applied in** clinical research, where trial design and audit must separate regression from treatment effects.[^s2]
- **Studied in** epidemiology, where design and analysis methods for handling it have been developed.[^s1]
- **Related to** the representativeness heuristic and base-rate neglect, which lead people to make non-regressive predictions from extreme evidence; to the outside view and randomized controlled trials, which correct for it; and to correlation versus causation, since regression produces change with no causal intervention behind it.[^s4][^s1]

## Sources

[^s1]: Barnett, van der Pols & Dobson, "Regression to the mean: what it is and how to deal with it", International Journal of Epidemiology 34(1), 2005. https://pubmed.ncbi.nlm.nih.gov/15333621/ (accessed 2026-11-06)
[^s2]: Morton & Torgerson, "Effect of regression to the mean on decision making in health care", BMJ 326, 2003. https://eprints.whiterose.ac.uk/42/1/1083.pdf (accessed 2026-11-06)
[^s3]: Galton, "Regression towards Mediocrity in Hereditary Stature", Journal of the Anthropological Institute 15, 1886 (offprint record, Wellcome Collection). https://wellcomecollection.org/works/sf54qjj5 (accessed 2026-11-06)
[^s4]: Kahneman & Tversky, "On the Psychology of Prediction", Oregon Research Institute Research Bulletin 12(4), 1972. https://scholarsbank.uoregon.edu//bitstreams/2fbae090-7a99-4301-8402-26e6e3a4c00c/download (accessed 2026-11-06)
