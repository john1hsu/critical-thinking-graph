---
id: ct:randomized-controlled-trial
type: Method
title: Randomized controlled trial
aliases: [RCT, randomised controlled trial, randomized trial, randomized experiment, A/B test]
domain: scientific-reasoning
summary: >-
  A comparative experiment in which participants are assigned to a treatment
  or a control group by a chance process, so that differences in outcomes can
  be attributed to the treatment rather than to how the groups were chosen.
level: introductory
evidenceStatus: normative
broader: [ct:scientific-method]
related: [ct:hypothesis-testing, ct:correlation-versus-causation, ct:simpsons-paradox, ct:null-hypothesis-significance-testing, ct:causal-diagrams, ct:regression-to-the-mean]
requires: [ct:confounding]
relations:
  - {predicate: counteracts, object: ct:confounding, source: s3, confidence: high}
  - {predicate: counteracts, object: ct:selection-bias, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: ct:mrc-1948-streptomycin-trial, source: s4, confidence: high}
  - {predicate: appliedIn, object: ct:medicine, source: s4, confidence: high}
  - {predicate: challengedBy, object: ct:deaton-cartwright-2018-rct-critique, source: s2, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Why the 1948 MRC trial of streptomycin used treatment allocation based on random numbers"
    publisher: Journal of the Royal Society of Medicine 104(9), 383-386 (Chalmers, 2011)
    url: https://www.jameslindlibrary.org/wp-data/uploads/2016/08/J-R-Soc-Med-2011-09-Chalmers-383-6.pdf
    type: peer-reviewed
    accessed: 2026-11-05
  - id: s2
    title: "Understanding and misunderstanding randomized controlled trials"
    publisher: Social Science & Medicine 210, 2-21 (Deaton & Cartwright, 2018)
    url: https://pubmed.ncbi.nlm.nih.gov/29331519/
    type: peer-reviewed
    accessed: 2026-11-05
  - id: s3
    title: "Techniques for randomization and allocation for clinical trials"
    publisher: Jornal Vascular Brasileiro 23, e20240046 (Miola, Espósito & Miot, 2024)
    url: https://new.scielo.br/j/jvb/a/ybgBFTM5wJCk3MVT77n9xLn/?lang=en
    type: peer-reviewed
    accessed: 2026-11-05
  - id: s4
    title: "The MRC randomized trial of streptomycin and its legacy: a view from the clinical front line"
    publisher: James Lind Library, Royal College of Physicians of Edinburgh (Crofton, 2004)
    url: https://www.jameslindlibrary.org/articles/the-mrc-randomized-trial-of-streptomycin-and-its-legacy-a-view-from-the-clinical-front-line/
    type: institutional
    accessed: 2026-11-05
  - id: s5
    title: "Medical Research Council (1948): Streptomycin treatment of pulmonary tuberculosis"
    publisher: James Lind Library record of the BMJ 2:769-782 report
    url: https://www.jameslindlibrary.org/records/medical-research-council-1948b/
    type: institutional
    accessed: 2026-11-05
created: 2026-11-05
---

# Randomized controlled trial

A randomized controlled trial (RCT) compares an intervention with a control condition after a chance process, rather than anyone's judgement, decides who gets which. Random allocation tends to even out the factors that could also affect the outcome, including ones nobody measured or thought of, so the groups start out comparable and a later difference in outcomes can more reliably be credited to the intervention.[^s3] That is why the RCT is the standard tool for the critical-thinking question "did this cause that, or were the groups different to begin with?"

## Origin

Fair comparisons are much older than randomization. For centuries investigators such as James Lind built comparison groups by alternation, taking patients in turn, and alternation remained the main method until after the Second World War, according to Iain Chalmers' 2011 history.[^s1] The trial most often treated as the symbol of the randomized design is the UK Medical Research Council's 1948 study of streptomycin for pulmonary tuberculosis, run by a team including the statistician Austin Bradford Hill, the coordinator Marc Daniels and Philip D'Arcy Hart.[^s4] Each centre had numbered envelopes ordered by random numbers, each holding a card for streptomycin or bed rest, opened only when the next eligible patient was accepted.[^s4] After six months, 4 of 55 streptomycin patients had died against 15 of 52 on bed rest; radiologists who read the X-rays did not know which group a patient was in.[^s4] The published report became a methodological landmark mainly for describing how investigators were kept from knowing the next assignment in advance.[^s5]

Chalmers argues that it is a myth that clinical RCTs grew mainly out of R. A. Fisher's statistical theory: the link has not been demonstrated, and Hill's main concern was to stop clinicians from foreseeing and steering allocations.[^s1]

## How it works

Suppose a software company wants to know whether a new onboarding email raises 90-day retention. Comparing customers who opened the email with those who did not is misleading, because people who open onboarding emails are probably more engaged anyway; engagement is a confounder. In an RCT, a random number decides which new sign-ups receive the email, so the two groups differ, on average, only in the email.[^s3] Three ingredients make this work:

- **Random sequence.** Simple randomization is like a lottery and works well with large groups; block randomization keeps group sizes equal, and stratified blocks balance key known factors.[^s3]
- **Allocation concealment.** Whoever enrols a participant must not know the next assignment, or they can steer people toward one arm and recreate selection bias.[^s3] This was the main rationale in 1948, and it remains a primary reason for random allocation today.[^s1]
- **Blinding.** After allocation, masking who got what protects against performance bias in how care is given and detection bias in how outcomes are scored.[^s3]

## How to apply it

When reading or designing a trial, ask: was the sequence truly random, and was it concealed from the people enrolling participants?[^s3] Were outcome assessors blinded where possible?[^s3] With small samples, simple randomization can leave groups unequal in size or covariates, so check the baseline table rather than assuming balance.[^s3] Then ask who was in the trial: Deaton and Cartwright stress that results apply to the trial sample, often a convenience sample, and that carrying them to another population or individual needs separate justification.[^s2]

## Evidence and limitations

Randomization is a standard of good causal inquiry rather than an empirical effect, but its strength is often overstated. In a 2018 critique, Angus Deaton and Nancy Cartwright argued that randomization does not make the groups equal in everything except the treatment, does not guarantee a precise estimate, and does not remove the need to think about covariates; at best it gives an unbiased estimate, which in a single trial is of limited use.[^s2] They also argued that RCTs are most informative inside a cumulative research programme that combines them with theory and other methods, so that we learn why something works, not only whether it worked once.[^s2] Practical limits follow from the design: the 1948 trial itself was shaped by a scarce drug and by ethical choices about the control group, who were promised streptomycin later if it proved useful.[^s4]

## Connections

An RCT **counteracts confounding** by balancing measured and unmeasured factors across arms, which is why reasoning about **correlation versus causation** and **Simpson's paradox** points toward it.[^s3] It **counteracts selection bias** when allocation is both random and concealed, the safeguard Chalmers identifies as the real point of the 1948 design.[^s1] The method is **demonstrated by the MRC 1948 streptomycin trial**, its most cited exemplar, and is **applied in medicine** as the basis of fair tests of treatments.[^s4] It is **challenged by Deaton and Cartwright's 2018 critique**, which disputes the "gold standard" status claimed for RCTs, especially in the social sciences.[^s2] It is a specific form of **hypothesis testing** and is often analysed with **null-hypothesis significance testing**.

## Sources

[^s1]: Chalmers, "Why the 1948 MRC trial of streptomycin used treatment allocation based on random numbers", JRSM 104(9), 2011. https://www.jameslindlibrary.org/wp-data/uploads/2016/08/J-R-Soc-Med-2011-09-Chalmers-383-6.pdf (accessed 2026-11-05)
[^s2]: Deaton & Cartwright, "Understanding and misunderstanding randomized controlled trials", Social Science & Medicine 210, 2018. https://pubmed.ncbi.nlm.nih.gov/29331519/ (accessed 2026-11-05)
[^s3]: Miola, Espósito & Miot, "Techniques for randomization and allocation for clinical trials", J Vasc Bras 23, 2024. https://new.scielo.br/j/jvb/a/ybgBFTM5wJCk3MVT77n9xLn/?lang=en (accessed 2026-11-05)
[^s4]: Crofton, "The MRC randomized trial of streptomycin and its legacy: a view from the clinical front line", James Lind Library, 2004. https://www.jameslindlibrary.org/articles/the-mrc-randomized-trial-of-streptomycin-and-its-legacy-a-view-from-the-clinical-front-line/ (accessed 2026-11-05)
[^s5]: Medical Research Council, "Streptomycin treatment of pulmonary tuberculosis", BMJ 1948, James Lind Library record. https://www.jameslindlibrary.org/records/medical-research-council-1948b/ (accessed 2026-11-05)
