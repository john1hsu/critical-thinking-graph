---
id: ct:deliberate-reflection
type: Technique
title: Deliberate reflection
aliases: [structured reflection, diagnostic reflection, guided reflection, reflective reasoning procedure]
domain: debiasing-and-metacognition
summary: >-
  A structured debiasing procedure, developed in research on medical diagnosis,
  in which a person who has formed a first impression lists the findings that
  support and contradict it, then assumes it is wrong and tests alternative
  explanations the same way before committing to a final judgment.
level: intermediate
evidenceStatus: mixed
broader: [ct:debiasing]
related: [ct:consider-the-opposite, ct:dual-process-theory, ct:metacognition, ct:premortem, ct:overconfidence-effect]
requires: [ct:availability-heuristic]
relations:
  - {predicate: counteracts, object: ct:availability-heuristic, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: ct:mamede-2010-availability-bias-reflection-study, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:silvia-mamede, source: s2, confidence: medium}
  - {predicate: introducedBy, object: ct:henk-schmidt, source: s2, confidence: medium}
  - {predicate: counteracts, object: ct:salient-distracting-features, source: s3, confidence: medium}
  - {predicate: supportedBy, object: ct:prakash-2019-reflective-strategies-meta-analysis, source: s5, confidence: medium}
  - {predicate: challengedBy, object: ct:lambe-2018-guided-reflection-null-study, source: s6, confidence: medium}
  - {predicate: appliedIn, object: ct:clinical-diagnostic-reasoning, source: s4, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Effect of availability bias and reflective reasoning on diagnostic accuracy among internal medicine residents"
    publisher: JAMA 304(11), 1198-1203 (Mamede, van Gog, van den Berge, Rikers, van Saase, van Guldener & Schmidt, 2010), PubMed record
    url: https://pubmed.ncbi.nlm.nih.gov/20841533/
    type: peer-reviewed
    accessed: 2026-11-04
  - id: s2
    title: "Effects of reflective practice on the accuracy of medical diagnoses"
    publisher: Medical Education 42(5), 468-475 (Mamede, Schmidt & Penaforte, 2008), Erasmus University repository
    url: https://repub.eur.nl/pub/17793
    type: primary
    accessed: 2026-11-04
  - id: s3
    title: "Exploring the role of salient distracting clinical features in the emergence of diagnostic errors and the mechanisms through which reflection counteracts mistakes"
    publisher: BMJ Quality & Safety 21(4), 295-300 (Mamede, Splinter, van Gog, Rikers & Schmidt, 2012)
    url: https://qualitysafety.bmj.com/content/21/4/295
    type: peer-reviewed
    accessed: 2026-11-04
  - id: s4
    title: "Effects of deliberate reflection on diagnostic accuracy, confidence and diagnostic calibration in dermatology"
    publisher: Perspectives on Medical Education (Costa Filho, Moura, Brandão, Schmidt & Mamede, 2019), Erasmus University repository full text
    url: https://repub.eur.nl/pub/118085/Repub_118085_O-A.pdf
    type: peer-reviewed
    accessed: 2026-11-04
  - id: s5
    title: "Interventions to improve diagnostic decision making: A systematic review and meta-analysis on reflective strategies"
    publisher: Medical Teacher 41(5), 517-524 (Prakash, Sladek & Schuwirth, 2019), Flinders University research record
    url: https://researchnow.flinders.edu.au/en/publications/interventions-to-improve-diagnostic-decision-making-a-systematic-/
    type: peer-reviewed
    accessed: 2026-11-04
  - id: s6
    title: "Guided reflection interventions show no effect on diagnostic accuracy in medical students"
    publisher: Frontiers in Psychology 9:2297 (Lambe, Hevey & Kelly, 2018)
    url: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2018.02297/pdf
    type: peer-reviewed
    accessed: 2026-11-04
created: 2026-11-04
---

# Deliberate reflection

Deliberate reflection is a short, scripted check on a first impression. After an initial judgment pops into mind, the reasoner writes down the evidence that fits it and the evidence that does not, then deliberately assumes the judgment is wrong, names alternative explanations, and weighs each one the same way before settling on a final answer.[^s4] It was built to counter errors that arise when fast, pattern-matching judgment latches onto whatever comes to mind most easily, above all the availability heuristic.[^s1]

## Origin

The procedure comes from a research programme on clinical reasoning led by Silvia Mamede and Henk Schmidt at Erasmus University Rotterdam. Their 2008 study with Jose Penaforte asked 42 internal medicine residents in Brazil to diagnose 16 cases either by first impression or by reflecting, and found that reflection made no difference on simple cases but improved accuracy on complex, unusual ones.[^s2] The group's best-known test came in a 2010 *JAMA* experiment that targeted availability bias directly,[^s1] and later studies standardised the procedure under the name deliberate reflection.[^s4]

## How it works

Fast, nonanalytical judgment matches a new situation to stored examples. If a similar-looking example was met recently, it comes to mind easily and can be mistaken for the right answer. In the 2010 study, 36 residents first evaluated six cases; they then diagnosed eight new cases on first impression, four of which resembled earlier cases but had different diagnoses. Second-year residents scored lower on the look-alike cases (1.55 of 4) than on the others (2.19) and repeated the earlier, wrong diagnosis about twice as often. When the residents re-diagnosed the look-alike cases using structured reanalysis, accuracy rose for both year groups.[^s1] A 2012 follow-up showed a related benefit against salient but irrelevant findings that pull attention toward the wrong diagnosis: reflection raised correct diagnoses and cut errors traced to those distractors, but only for residents, not for medical students, suggesting that the procedure works only when the reasoner knows which features tell the alternatives apart.[^s3]

*Workplace example.* A clinic doctor saw two patients with influenza last week. A new patient arrives with fever and aches, and "flu" comes to mind at once. Using deliberate reflection, she lists what fits flu (fever, aches) and what does not (a recent trip abroad, a rash, symptoms lasting ten days), then assumes flu is wrong and works through two alternatives, such as a travel-acquired infection, against the same findings. The contradicting findings now point to the alternative, so she orders the relevant test rather than sending the patient home. The same script transfers to any judgment made by recognition, such as an engineer diagnosing a server outage that resembles last month's incident.[^s4]

## How to apply it

1. **Record the first impression** and how confident you are in it.[^s4]
2. **List supporting evidence:** the findings that fit the first impression.[^s4]
3. **List contradicting evidence:** findings that argue against it, and findings you would expect to see if it were true but do not.[^s4]
4. **Assume it is wrong.** Name at least two alternative explanations and repeat steps 2 and 3 for each.[^s4]
5. **Decide:** rank the explanations by fit and commit to a final judgment and confidence rating.[^s4]

**When to use it:** for complex or unusual problems, and when a case closely resembles one handled recently; on routine cases first impressions did as well as reflection.[^s2] **Pitfalls:** the method needs enough domain knowledge to recognise discriminating features,[^s3] and in novices reflection can switch a correct first answer to a wrong one about as often as it fixes a wrong one.[^s6]

## Evidence

The evidence is rated *mixed*. A 2019 *Medical Teacher* systematic review of 44 studies with 4,380 medical professionals pooled the guided-reflection studies and found a moderate benefit for diagnostic decision making (effect size 0.38, 95% CI 0.23 to 0.52).[^s5] A 2019 study of 61 final-year students diagnosing dermatology images found a large accuracy gain from a 3.5-minute reflection task (about 50% versus 38% correct), but no improvement in confidence calibration: both groups remained overconfident.[^s4] Against this, a 2018 experiment with 186 medical students found that short and long guided-reflection tasks did not improve final diagnoses over first impressions, with corrections roughly balanced by changes for the worse.[^s6] Most studies use written vignettes, single sessions and trainees, so effects on experienced clinicians in real practice are less certain.[^s4]

## Connections

- **Counteracts** the availability heuristic: structured reanalysis reversed accuracy losses caused by recent exposure to look-alike cases.[^s1]
- **Demonstrated by** the 2010 *JAMA* experiment by Mamede and colleagues on availability bias in internal medicine residents.[^s1]
- **Introduced by** Silvia Mamede and Henk Schmidt, whose 2008 study first tested reflective practice against first-impression diagnosis.[^s2]
- **Counteracts** salient distracting features, eye-catching findings that misdirect diagnosis.[^s3]
- **Supported by** the 2019 meta-analysis by Prakash, Sladek and Schuwirth.[^s5]
- **Challenged by** Lambe, Hevey and Kelly's 2018 null result in medical students.[^s6]
- **Applied in** clinical diagnostic reasoning, where it has been tested in internal medicine and dermatology.[^s4]
- **Related to** consider-the-opposite and the premortem, which likewise make the case against a current view explicit, and to dual-process theory, since it deliberately switches from nonanalytical to analytical reasoning.[^s1]

## Sources

[^s1]: Mamede, S., van Gog, T., van den Berge, K., Rikers, R. M. J. P., van Saase, J. L. C. M., van Guldener, C. & Schmidt, H. G. (2010). "Effect of availability bias and reflective reasoning on diagnostic accuracy among internal medicine residents." *JAMA* 304(11), 1198-1203. https://pubmed.ncbi.nlm.nih.gov/20841533/ (accessed 2026-11-04)
[^s2]: Mamede, S., Schmidt, H. G. & Penaforte, J. C. (2008). "Effects of reflective practice on the accuracy of medical diagnoses." *Medical Education* 42(5), 468-475. https://repub.eur.nl/pub/17793 (accessed 2026-11-04)
[^s3]: Mamede, S., Splinter, T. A. W., van Gog, T., Rikers, R. M. J. P. & Schmidt, H. G. (2012). "Exploring the role of salient distracting clinical features in the emergence of diagnostic errors and the mechanisms through which reflection counteracts mistakes." *BMJ Quality & Safety* 21(4), 295-300. https://qualitysafety.bmj.com/content/21/4/295 (accessed 2026-11-04)
[^s4]: Costa Filho, G. B., Moura, A. S., Brandão, P. R., Schmidt, H. G. & Mamede, S. (2019). "Effects of deliberate reflection on diagnostic accuracy, confidence and diagnostic calibration in dermatology." *Perspectives on Medical Education*. https://repub.eur.nl/pub/118085/Repub_118085_O-A.pdf (accessed 2026-11-04)
[^s5]: Prakash, S., Sladek, R. & Schuwirth, L. (2019). "Interventions to improve diagnostic decision making: A systematic review and meta-analysis on reflective strategies." *Medical Teacher* 41(5), 517-524. https://researchnow.flinders.edu.au/en/publications/interventions-to-improve-diagnostic-decision-making-a-systematic-/ (accessed 2026-11-04)
[^s6]: Lambe, K. A., Hevey, D. & Kelly, B. D. (2018). "Guided reflection interventions show no effect on diagnostic accuracy in medical students." *Frontiers in Psychology* 9, 2297. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2018.02297/pdf (accessed 2026-11-04)
