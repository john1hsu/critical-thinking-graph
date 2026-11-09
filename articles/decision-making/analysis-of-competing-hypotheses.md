---
id: ct:analysis-of-competing-hypotheses
type: Technique
title: Analysis of competing hypotheses
aliases: [ACH, ACH matrix, competing hypotheses matrix]
domain: decision-making
summary: >-
  A structured analytic technique, devised by the CIA analyst Richards Heuer,
  in which an analyst lays out every plausible explanation side by side in a
  matrix, scores each item of evidence against all of them, and favours the
  hypothesis with the least evidence against it rather than the most for it.
level: intermediate
evidenceStatus: contested
broader: [ct:structured-analytic-techniques, ct:debiasing]
related: [ct:key-assumptions-check, ct:devils-advocacy, ct:consider-the-opposite, ct:falsifiability, ct:inference-to-the-best-explanation, ct:bayesian-reasoning, ct:base-rate-neglect]
requires: [ct:confirmation-bias]
relations:
  - {predicate: introducedBy, object: ct:richards-heuer, source: s1, confidence: high}
  - {predicate: introducedIn, object: ct:psychology-of-intelligence-analysis, source: s1, confidence: high}
  - {predicate: appliedIn, object: ct:intelligence-analysis, source: s2, confidence: high}
  - {predicate: counteracts, object: ct:confirmation-bias, source: s2, confidence: medium}
  - {predicate: contrastsWith, object: ct:satisficing, source: s1, confidence: high}
  - {predicate: challengedBy, object: ct:mandel-karvetski-dhami-2018-ach-trial, source: s4, confidence: high}
  - {predicate: challengedBy, object: ct:dhami-belton-mandel-2019-ach-protocol-study, source: s3, confidence: high}
  - {predicate: challengedBy, object: ct:cheikes-2004-confirmation-bias-complex-analyses-study, source: s5, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Psychology of Intelligence Analysis, Chapter 8: Analysis of Competing Hypotheses"
    publisher: Richards J. Heuer Jr., Center for the Study of Intelligence, Central Intelligence Agency (1999)
    url: https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf
    type: primary
    accessed: 2026-11-09
  - id: s2
    title: "A Tradecraft Primer: Structured Analytic Techniques for Improving Intelligence Analysis"
    publisher: US Government, Central Intelligence Agency, Center for the Study of Intelligence (March 2009)
    url: https://www.cia.gov/resources/csi/static/955180a45afe3f5013772c313b16face/Tradecraft-Primer-apr09.pdf
    type: government
    accessed: 2026-11-09
  - id: s3
    title: "The \"analysis of competing hypotheses\" in intelligence analysis"
    publisher: "Applied Cognitive Psychology (Dhami, Belton & Mandel, 2019), doi:10.1002/acp.3550, author manuscript"
    url: https://mdx-repository.prod-uk.cayuse.com/download/68a5c6461fa622c2ea8d16f5f32e28fc06861520af1a4341f7740e8173d2cc48/229327/Dhami_et_al-2019-Applied_Cognitive_Psychology.pdf
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s4
    title: "Boosting intelligence analysts' judgment accuracy: What works, what fails?"
    publisher: "Judgment and Decision Making 13(6), 607-621 (Mandel, Karvetski & Dhami, 2018)"
    url: https://dlab.sauder.ubc.ca/sjdm/journal/18/18803/jdm18803.html
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s5
    title: "Confirmation Bias in Complex Analyses"
    publisher: "MITRE Technical Report MTR 04B0000017 (Cheikes, Brown, Lehner & Adelman, 2004)"
    url: https://www.mitre.org/sites/default/files/pdf/04_0985.pdf
    type: institutional
    accessed: 2026-11-09
created: 2026-11-09
---

# Analysis of competing hypotheses

Analysis of competing hypotheses (ACH) is a step-by-step procedure for choosing among rival explanations. Instead of building a case for the explanation that looks best, the analyst lists every reasonable hypothesis, sets them as columns of a matrix, rates each piece of evidence against all of them at once, and then tries to knock hypotheses out. The survivor is the one with the least evidence against it, not the one with the most evidence for it.[^s1]

## Origin

The technique was developed by Richards Heuer, a veteran CIA analyst, and set out in Chapter 8 of his 1999 book *Psychology of Intelligence Analysis*, which he described as perhaps the most important chapter in it.[^s1] Heuer's starting point was that analysts usually *satisfice*: they settle on the first explanation that seems good enough and then look for support, when the harder job is to hold several hypotheses in view simultaneously, something he thought people rarely manage without a structured aid.[^s1] The US Government's 2009 *Tradecraft Primer* later codified ACH as one of its diagnostic techniques and gave it the job of preventing premature closure on a single explanation.[^s2]

## How it works

Heuer's key idea is *diagnosticity*. Evidence that fits every hypothesis tells you nothing about which one is true, however much of it there is; his medical analogy is that a fever shows a patient is ill but not which illness they have.[^s1] The matrix forces each item to be scored against all hypotheses, exposing evidence that only *seems* to confirm the favourite.[^s1] The *Primer* names the failures ACH targets: being swayed by a first impression, failing to generate a full set of explanations, and relying on evidence that supports a preferred view but is also consistent with others.[^s2]

*Workplace example.* An e-commerce company sees late deliveries double in a month. The operations lead is sure the new route-planning software is to blame. An ACH session lists four hypotheses: the software, a shortage of warehouse staff, a carrier cutting capacity, and late inbound stock from suppliers. The team then scores evidence across all four columns. "Complaints rose sharply" fits every hypothesis, so it carries no weight. "Orders picked on time still arrive late" is inconsistent with the staffing and supplier hypotheses. "Late parcels are concentrated in regions served by one carrier, including routes the new software does not plan" is inconsistent with the software hypothesis. The carrier explanation survives with the fewest inconsistencies, and the team agrees in advance which signs (for example, late parcels spreading to other carriers) would reopen the question, as Heuer's final step advises.[^s1]

## How to apply it

Heuer's procedure has eight steps:[^s1]

1. **Identify all plausible hypotheses**, ideally by brainstorming with people who see the problem differently.[^s1]
2. **List the significant evidence and arguments** for and against each hypothesis.[^s1]
3. **Build the matrix**, hypotheses across the top and evidence down the side, and judge each item's diagnosticity.[^s1]
4. **Refine it**: reword or add hypotheses and drop evidence that discriminates between none of them.[^s1]
5. **Draw tentative conclusions by trying to disprove** each hypothesis, rather than proving one.[^s1]
6. **Test sensitivity**: ask how the result changes if a few linchpin items are wrong, misleading or open to another reading.[^s1]
7. **Report the relative likelihood of every hypothesis**, not just the winner.[^s1]
8. **Name milestones** that would show events taking a different course.[^s1]

The *Primer* recommends ACH when there is a lot of data to absorb, when a small team can challenge each other's reading of the evidence, when an issue is controversial and a record of the alternatives considered is useful, and when deception is possible; it adds a check for evidence that should be present if a hypothesis were true but is missing.[^s2]

**Pitfalls.** The method does not say precisely how to rate or combine evidence, so users improvise; it has no slot for base rates; and counting inconsistencies can produce ties rather than a ranking.[^s3]

## Evidence

Controlled tests have not shown that ACH improves accuracy, so its status here is *contested*. A 2004 MITRE experiment with 24 participants found confirmation bias in how evidence was weighted; ACH reduced it only among participants without professional analysis experience and did not reduce anchoring on initial beliefs, leading the authors to judge it not yet a robust debiasing method.[^s5]

In a 2018 randomised experiment, 50 UK intelligence analysts estimated which of four groups a target belonged to from base rates and 12 cues; analysts trained in and required to use ACH were no more accurate than controls, and their probability judgments were, if anything, slightly less coherent. Recalibration and averaging across analysts helped far more.[^s4] A 2019 analysis of the analysts' written protocols on the same kind of task found that the ACH group did gather more relevant evidence, attend more to diagnosticity and run more sensitivity checks, but rarely followed the method fully, used base rates less, applied their scoring rules less consistently and often ended in ties; the authors suggested considering alternatives such as consider-the-opposite strategies and Bayesian decision aids.[^s3]

## Connections

- **Broader:** a structured analytic technique, classed by the *Primer* as diagnostic, and a form of debiasing.[^s2]
- **Introduced by** Richards Heuer **in** *Psychology of Intelligence Analysis* (1999).[^s1]
- **Applied in** intelligence analysis, especially on high-volume, contested or deception-prone questions.[^s2]
- **Counteracts** confirmation bias, by design, through its focus on disconfirming and diagnostic evidence.[^s2]
- **Contrasts with** satisficing, the habit of accepting the first adequate explanation, which Heuer wrote ACH to replace with simultaneous evaluation.[^s1]
- **Challenged by** the 2004 MITRE experiment, the 2018 accuracy trial and the 2019 protocol study.[^s5] [^s4] [^s3]
- **Related to** the key assumptions check and devil's advocacy, its neighbours in the *Primer*;[^s2] to falsifiability and inference to the best explanation, since it ranks explanations by how well they survive attempted refutation;[^s1] and to Bayesian reasoning and base-rate neglect, since critics note the matrix ignores prior probabilities.[^s3]

## Sources

[^s1]: Heuer, R. J., Jr. (1999). *Psychology of Intelligence Analysis*, ch. 8, "Analysis of Competing Hypotheses". CIA Center for the Study of Intelligence. https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf (accessed 2026-11-09)
[^s2]: US Government (2009). *A Tradecraft Primer: Structured Analytic Techniques for Improving Intelligence Analysis*. CIA Center for the Study of Intelligence. https://www.cia.gov/resources/csi/static/955180a45afe3f5013772c313b16face/Tradecraft-Primer-apr09.pdf (accessed 2026-11-09)
[^s3]: Dhami, M. K., Belton, I. K. & Mandel, D. R. (2019). "The 'analysis of competing hypotheses' in intelligence analysis." *Applied Cognitive Psychology*. doi:10.1002/acp.3550. https://mdx-repository.prod-uk.cayuse.com/download/68a5c6461fa622c2ea8d16f5f32e28fc06861520af1a4341f7740e8173d2cc48/229327/Dhami_et_al-2019-Applied_Cognitive_Psychology.pdf (accessed 2026-11-09)
[^s4]: Mandel, D. R., Karvetski, C. W. & Dhami, M. K. (2018). "Boosting intelligence analysts' judgment accuracy: What works, what fails?" *Judgment and Decision Making* 13(6), 607–621. https://dlab.sauder.ubc.ca/sjdm/journal/18/18803/jdm18803.html (accessed 2026-11-09)
[^s5]: Cheikes, B. A., Brown, M. J., Lehner, P. E. & Adelman, L. (2004). *Confirmation Bias in Complex Analyses*. MITRE Technical Report MTR 04B0000017. https://www.mitre.org/sites/default/files/pdf/04_0985.pdf (accessed 2026-11-09)
