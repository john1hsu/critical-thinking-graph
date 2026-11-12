---
id: ct:hierarchy-of-evidence
type: Framework
title: Hierarchy of evidence
aliases: [levels of evidence, evidence pyramid, evidence hierarchy]
domain: evidence-and-information-literacy
summary: >-
  A ranking of study designs by how well they usually protect against bias,
  typically placing randomised trials and their systematic reviews above
  cohort, case-control and case-series studies, used as a quick guide to which
  evidence should carry more weight for a given kind of question.
level: introductory
evidenceStatus: normative
broader: [ct:evidence-based-medicine, ct:source-evaluation]
related: [ct:systematic-review, ct:randomized-controlled-trial, ct:primary-and-secondary-sources, ct:source-credibility, ct:publication-bias, ct:iain-chalmers]
requires: [ct:randomized-controlled-trial]
relations:
  - {predicate: appliedIn, object: ct:evidence-based-medicine, source: s2, confidence: high}
  - {predicate: counteracts, object: ct:confounding, source: s4, confidence: medium}
  - {predicate: challengedBy, object: ct:grade-approach, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:grade-approach, source: s3, confidence: medium}
sources:
  - id: s1
    title: "New evidence pyramid"
    publisher: "Evidence-Based Medicine 21(4), 125-127 (Murad, Asi, Alsawas & Alahdab, 2016), PubMed Central"
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4975798
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s2
    title: "Explanation of the 2011 OCEBM Levels of Evidence"
    publisher: Oxford Centre for Evidence-Based Medicine, University of Oxford (Howick, Chalmers, Glasziou et al., 2011)
    url: https://www.cebm.ox.ac.uk/resources/levels-of-evidence/explanation-of-the-2011-ocebm-levels-of-evidence
    type: academic
    accessed: 2026-11-12
  - id: s3
    title: "GRADE: an emerging consensus on rating quality of evidence and strength of recommendations"
    publisher: "BMJ 336(7650), 924-926 (Guyatt, Oxman, Vist, Kunz, Falck-Ytter, Alonso-Coello & Schünemann, 2008), EPA HERO record"
    url: https://hero.epa.gov/reference/783306
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s4
    title: "What is GRADE?"
    publisher: BMJ Best Practice (Siemieniuk & Guyatt)
    url: https://bestpractice.bmj.com/info/evidence/learn-ebm/what-is-grade/
    type: institutional
    accessed: 2026-11-12
created: 2026-11-12
---

# Hierarchy of evidence

A hierarchy of evidence ranks kinds of studies by how well their design usually shields a result from bias. The familiar picture is a pyramid: laboratory work, expert opinion and case series at the base, then case-control and cohort studies, then randomised controlled trials, with systematic reviews and meta-analyses at the apex.[^s1] Its job is practical: when a question has been studied many ways, it tells a reader which kind of study to look for first and which deserves more weight when findings disagree.[^s2]

## Origin

Formal hierarchies grew out of clinical epidemiology. Early versions such as the Canadian Task Force on the Periodic Health Examination (1979) and David Sackett's 1989 scheme mainly rated evidence about treatments and put randomised trials above observational studies.[^s2] The Oxford Centre for Evidence-Based Medicine published broader levels around 1998–2000, adding separate rankings for diagnosis, prognosis and economic analysis, and an international group led by Jeremy Howick, including Iain Chalmers and Paul Glasziou, simplified them in the 2011 OCEBM Levels.[^s2] According to Murad and colleagues, the pyramid idea became widely known in the early 1990s as clinicians learned critical-appraisal skills.[^s1]

## How it works

The ranking rests on one idea: designs differ in how many alternative explanations they rule out. Random allocation balances known and unknown confounders between groups, so a trial's difference in outcomes is harder to explain away than a difference between people who chose their own exposure; GRADE, for example, starts observational evidence at low certainty because of residual confounding.[^s4] The 2011 OCEBM version also stresses that the best design depends on the question: for local prevalence a current local survey is ideal, while for treatment benefits a systematic review of randomised trials ranks first.[^s2]

A workplace example: an HR team is told that a new wellness app "reduces sick days by 30%". The claim comes from a vendor case study of one firm that adopted the app. Using the hierarchy, the team notes that this is the weakest kind of evidence — a single uncontrolled case — and asks whether any controlled comparison or randomised pilot exists. Finding none, they run a small randomised pilot across departments before committing to a company-wide contract — the same move the OCEBM Levels describe of seeking the likely-best evidence for the question first.[^s2]

## How to apply it

1. Identify the type of question (does it work, how common is it, how accurate is a test, what are the harms) and pick the matching ladder.[^s2]
2. Search first for the highest-ranked evidence that answers it, usually a systematic review of the right study design.[^s2]
3. Treat the rank as a starting point, not a verdict. A badly run trial can be downgraded, and an observational study with a very large effect or a clear dose-response gradient can be upgraded.[^s4]
4. Judge the remaining weaknesses explicitly: risk of bias, inconsistency between studies, indirectness, imprecision and publication bias.[^s4]

## Evidence and limitations

Critics have long called design-only rankings simplistic.[^s2] Murad and colleagues argue that study design is a poor stand-in for risk of bias, so the lines between levels should be drawn as wavy rather than straight, and that systematic reviews belong not at the apex but as a lens through which the other studies are read; a meta-analysis of surgical case series is not comparable to one of well-run trials.[^s1] The OCEBM authors themselves warn that a lower-ranked study can sometimes give stronger evidence and that rigid hierarchies can discourage independent judgment.[^s2] The GRADE working group responded to inconsistent grading systems across guideline bodies with a single transparent scheme that rates certainty per outcome and separates quality of evidence from strength of recommendation.[^s3] GRADE ratings still involve judgment, so two reviewers can disagree.[^s4]

## Connections

The hierarchy is a working tool of evidence-based medicine, where the OCEBM Levels were built to help clinicians find likely-best evidence quickly.[^s2] It helps counteract confounding by favouring randomised designs, since observational evidence is presumed to carry residual confounding.[^s4] It is challenged and refined by the GRADE approach, which showed that design alone is an insufficient surrogate for evidence quality,[^s1] and it contrasts with GRADE, which rates certainty outcome by outcome rather than by study type.[^s3] It sits beside the systematic review, which Murad and colleagues recast as a lens on the pyramid,[^s1] and builds on the randomised controlled trial and on judging source credibility.

## Sources

[^s1]: Murad, Asi, Alsawas & Alahdab, "New evidence pyramid", Evidence-Based Medicine 21(4), 2016. https://pmc.ncbi.nlm.nih.gov/articles/PMC4975798 (accessed 2026-11-12)
[^s2]: Howick et al., "Explanation of the 2011 OCEBM Levels of Evidence", Oxford Centre for Evidence-Based Medicine. https://www.cebm.ox.ac.uk/resources/levels-of-evidence/explanation-of-the-2011-ocebm-levels-of-evidence (accessed 2026-11-12)
[^s3]: Guyatt et al., "GRADE: an emerging consensus on rating quality of evidence and strength of recommendations", BMJ 336, 2008. https://hero.epa.gov/reference/783306 (accessed 2026-11-12)
[^s4]: Siemieniuk & Guyatt, "What is GRADE?", BMJ Best Practice. https://bestpractice.bmj.com/info/evidence/learn-ebm/what-is-grade/ (accessed 2026-11-12)
