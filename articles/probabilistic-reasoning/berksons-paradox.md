---
id: ct:berksons-paradox
type: Phenomenon
title: Berkson's paradox
aliases: [Berkson's bias, Berkson's fallacy, admission rate bias, Berkson's selection bias]
domain: probabilistic-reasoning
summary: >-
  A spurious association between two traits that are independent in the
  population, which appears when the sample is selected on the basis of
  either trait (for example, only people admitted to hospital), because
  selection on a common effect of both links them inside the sample.
level: intermediate
evidenceStatus: robust
broader: [ct:selection-bias, ct:statistical-paradox]
related: [ct:simpsons-paradox, ct:confounding, ct:survivorship-bias, ct:correlation-versus-causation, ct:random-sampling]
requires: [ct:conditional-probability]
relations:
  - {predicate: introducedBy, object: ct:joseph-berkson, source: s1, confidence: high}
  - {predicate: formalizedBy, object: ct:causal-diagrams, source: s2, confidence: high}
  - {predicate: appliedIn, object: ct:epidemiology, source: s4, confidence: high}
  - {predicate: appliedIn, object: ct:causal-inference, source: s5, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Limitations of the application of fourfold table analysis to hospital data"
    publisher: Biometrics 2(3), 47-53 (Berkson, 1946), PubMed record 21001024
    url: https://pubmed.ncbi.nlm.nih.gov/21001024/
    type: primary
    accessed: 2026-11-18
  - id: s2
    title: "Commentary: A structural approach to Berkson's fallacy and a guide to a history of opinions about it"
    publisher: International Journal of Epidemiology 43(2), 515-521 (Snoep, Morabia, Hernández-Díaz, Hernán & Vandenbroucke, 2014), PubMed Central
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3997377
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s3
    title: "A structural approach to selection bias"
    publisher: Epidemiology 15(5), 615-625 (Hernán, Hernández-Díaz & Robins, 2004), PubMed record 15308962
    url: https://pubmed.ncbi.nlm.nih.gov/15308962/
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s4
    title: "Admission rate bias"
    publisher: Catalogue of Bias, Centre for Evidence-Based Medicine, University of Oxford (Spencer, Aronson, Nunan & Heneghan)
    url: https://catalogofbias.org/biases/admission-rate-bias/
    type: academic
    accessed: 2026-11-18
  - id: s5
    title: "Collider bias undermines our understanding of COVID-19 disease risk and severity"
    publisher: Nature Communications 11, 2020 (Griffith, Morris, Tudball, ... Davies & Hemani), doi:10.1038/s41467-020-19478-2, RePEc/IDEAS record
    url: https://ideas.repec.org/a/nat/natcom/v11y2020i1d10.1038_s41467-020-19478-2.html
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s6
    title: "Directed Acyclic Graphs (chapter 3 of Causal Inference: The Mixtape)"
    publisher: Cunningham, Causal Inference - The Mixtape, online edition
    url: https://mixtape.scunning.com/03-directed_acyclical_graphs
    type: textbook
    accessed: 2026-11-18
created: 2026-11-18
---

# Berkson's paradox

Berkson's paradox is the appearance of an association between two traits that are unrelated in the wider population, produced purely by the way a sample was chosen. If being in the sample depends on having one trait or the other, then within the sample the two traits become linked, usually negatively, even though neither affects the other.[^s2][^s6] Epidemiologists also call it Berkson's bias, Berkson's fallacy or admission rate bias, after its best-known setting: studies that draw their subjects from hospital patients.[^s4]

## Origin

The statistician Joseph Berkson set out the problem in a 1946 *Biometrics* paper on the limits of analysing two-by-two tables built from hospital records.[^s1] His illustration was a hospital-based comparison of diabetes and cholecystitis: two diseases independent in the general population can look associated among inpatients, because a person with two conditions has more reasons to be admitted than a person with one.[^s2] A 2014 review in the *International Journal of Epidemiology* traces the idea back to Pearl's 1929 autopsy study of cancer and tuberculosis and recounts decades of disagreement: some later authors denied it applied to exposure-disease studies, while Roberts and colleagues (1978) offered empirical evidence and David Sackett (1979) catalogued it as admission rate bias.[^s2][^s4]

## How it works

The modern explanation uses causal diagrams. Hospital admission is a common effect, or collider, of both diseases: each arrow points into it. Left alone, a collider blocks any statistical path between its causes, so the diseases stay independent. Restricting the analysis to admitted patients conditions on the collider and opens that path, creating an association that exists only inside the selected group.[^s2][^s6] Hernán, Hernández-Díaz and Robins generalised the point in 2004, arguing that the many biases epidemiologists label "selection bias" share this one structure, conditioning on a common effect of exposure and outcome, whereas confounding arises from a common cause.[^s3]

A simulation in Cunningham's causal inference textbook makes the mechanism visible. It draws 2,500 people whose talent and looks are independent, then labels as "stars" only those in the top 15% of a combined score. Across everyone the correlation is essentially zero; among stars, and among non-stars, the better-looking tend to be less talented, simply because a star who scores low on one trait had to score high on the other to be selected.[^s6]

A workplace version: a hiring manager notices that, among the engineers the company hired, those with the strongest coding tests had the weakest interviews, and concludes that strong coders interview poorly. If candidates were hired whenever their test score plus interview score cleared a bar, the hired group will show exactly that trade-off even if the two skills are unrelated among applicants. The pattern says something about the hiring rule, not about engineers, the same selection-on-a-sum logic as the textbook's movie-star simulation.[^s6]

## How to spot and handle it

- Ask how cases got into the data. Hospital patients, tested patients, survey volunteers, hired staff and published studies are all filtered samples; if the filter depends on the variables being compared, expect a distortion.[^s4][^s5]
- Draw the causal diagram and check whether the selection variable has arrows from both traits; if so, an association inside the sample is suspect.[^s2][^s6]
- Compare against a population-based sample. Catalogue of Bias guidance recommends population controls, incident rather than prevalent cases, and excluding patients admitted for another disease, or adjusting for factors that drive selection.[^s4]
- Prefer good sampling over repair. Griffith and colleagues found that UK Biobank participants tested for COVID-19 differed strongly from the rest of the cohort on genetic, behavioural, cardiovascular, demographic and body-size traits, and concluded that sensitivity checks help but representative sampling at the design stage is the real fix.[^s5]

## Evidence

The paradox is a demonstrable consequence of probability, and documented cases show it is not merely theoretical. Sackett's 1979 data gave an odds ratio of about 4 between respiratory and locomotor disease among hospital patients against about 1 in the general population, and case-control studies of malaria and non-typhoidal salmonella reached opposite conclusions (odds ratios of 0.4 and 1.9) depending on which controls were used.[^s4] During the COVID-19 pandemic, many risk-factor studies drew on hospital patients, people tested for infection or volunteers, and Griffith and colleagues showed that collider bias in such samples can create or distort associations between the very traits that influence who gets sampled.[^s5] How much damage it has done to the published record is debated: Snoep and colleagues judged that the classic form probably had little impact on mainstream epidemiology, since most hospital studies use new cases and rarely treat one disease as a cause of another, while warning that population controls alone do not remove it.[^s2]

## Connections

- **Introduced by** Joseph Berkson, whose 1946 *Biometrics* paper on hospital data is the standard origin.[^s1][^s2]
- **Formalized by** causal diagrams, in which hospitalisation is a collider whose conditioning opens a spurious path.[^s2][^s6]
- **Broader:** selection bias, which Hernán and colleagues define as exactly this common-effect structure, and statistical paradoxes generally.[^s3]
- **Applied in** epidemiology, where it is a named threat to hospital-based case-control studies,[^s4] and in causal inference more widely, including the analysis of non-representative pandemic samples.[^s5]
- **Related to** confounding, its structural opposite (a common cause rather than a common effect);[^s3] Simpson's paradox, another way that subgrouping misleads; survivorship bias, a selection filter of the same kind; correlation versus causation; and random sampling, the design remedy.[^s3][^s5]
- **Requires** conditional probability, since the paradox concerns how associations change once one conditions on selection.[^s2]

## Sources

[^s1]: Berkson, "Limitations of the application of fourfold table analysis to hospital data", Biometrics 2(3), 1946. https://pubmed.ncbi.nlm.nih.gov/21001024/ (accessed 2026-11-18)
[^s2]: Snoep, Morabia, Hernández-Díaz, Hernán & Vandenbroucke, "Commentary: A structural approach to Berkson's fallacy and a guide to a history of opinions about it", International Journal of Epidemiology 43(2), 2014. https://pmc.ncbi.nlm.nih.gov/articles/PMC3997377 (accessed 2026-11-18)
[^s3]: Hernán, Hernández-Díaz & Robins, "A structural approach to selection bias", Epidemiology 15(5), 2004. https://pubmed.ncbi.nlm.nih.gov/15308962/ (accessed 2026-11-18)
[^s4]: Spencer, Aronson, Nunan & Heneghan, "Admission rate bias", Catalogue of Bias, CEBM, University of Oxford. https://catalogofbias.org/biases/admission-rate-bias/ (accessed 2026-11-18)
[^s5]: Griffith et al., "Collider bias undermines our understanding of COVID-19 disease risk and severity", Nature Communications 11, 2020. https://ideas.repec.org/a/nat/natcom/v11y2020i1d10.1038_s41467-020-19478-2.html (accessed 2026-11-18)
[^s6]: Cunningham, "Directed Acyclic Graphs", Causal Inference: The Mixtape. https://mixtape.scunning.com/03-directed_acyclical_graphs (accessed 2026-11-18)
