---
id: ct:systematic-review
type: Method
title: Systematic review
aliases: [systematic literature review, systematic research synthesis]
domain: evidence-and-information-literacy
summary: >-
  A review of research that answers a clearly formulated question by finding,
  selecting, appraising and synthesising all eligible studies with explicit
  methods fixed in advance, so that the choice of evidence cannot be bent
  toward a preferred answer.
level: intermediate
evidenceStatus: normative
broader: [ct:scientific-method]
related: [ct:meta-analysis, ct:preregistration, ct:randomized-controlled-trial, ct:researcher-degrees-of-freedom, ct:confirmation-bias]
requires: [ct:source-credibility]
relations:
  - {predicate: counteracts, object: ct:suppressed-evidence, source: s1, confidence: high}
  - {predicate: detects, object: ct:publication-bias, source: s2, confidence: medium}
  - {predicate: influencedBy, object: ct:archie-cochrane, source: s1, confidence: high}
  - {predicate: appliedIn, object: ct:evidence-based-medicine, source: s2, confidence: medium}
  - {predicate: challengedBy, object: ct:ioannidis-2016-mass-production-of-systematic-reviews, source: s4, confidence: high}
sources:
  - id: s1
    title: "Chapter I: Introduction (Cumpston, Flemyng, Thomas, Higgins, Deeks & Clarke), Cochrane Handbook for Systematic Reviews of Interventions, version 6.5"
    publisher: Cochrane (2024)
    url: https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-i
    type: institutional
    accessed: 2026-11-09
  - id: s2
    title: "A brief history of research synthesis"
    publisher: "Evaluation & the Health Professions 25(1), 12-37 (Chalmers, Hedges & Cooper, 2002), Duke University repository"
    url: https://dukespace.lib.duke.edu/server/api/core/bitstreams/5541cd3e-4a21-461a-9862-fe5a69294275/content
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s3
    title: "The PRISMA 2020 statement: an updated guideline for reporting systematic reviews"
    publisher: "BMJ 372, n71 (Page, McKenzie, Bossuyt et al., 2021), White Rose eprints"
    url: https://eprints.whiterose.ac.uk/id/eprint/173303/1/bmj.n71.full.pdf
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s4
    title: "The Mass Production of Redundant, Misleading, and Conflicted Systematic Reviews and Meta-analyses"
    publisher: "The Milbank Quarterly 94(3), 485-514 (Ioannidis, 2016)"
    url: https://www.milbank.org/quarterly/articles/mass-production-redundant-misleading-conflicted-systematic-reviews-meta-analyses/
    type: peer-reviewed
    accessed: 2026-11-09
created: 2026-11-09
---

# Systematic review

A systematic review collates all the evidence that meets eligibility criteria set in advance in order to answer one specific research question, using explicit methods written down in a protocol before the results are known.[^s1] The PRISMA 2020 reporting guideline describes it the same way: explicit, systematic methods used to collate and synthesise the findings of studies that address a clearly formulated question.[^s3] Its point, for a critical thinker, is procedural: because the rules for finding and including studies are fixed first, the reviewer cannot quietly keep the studies that agree and drop the ones that do not.[^s1]

## Origin

Pooling evidence is old. Chalmers, Hedges and Cooper trace it to James Lind's eighteenth-century treatise on scurvy, which reviewed earlier publications in order to set aside prejudice, and to Karl Pearson's 1904 pooling of correlations from 11 typhoid inoculation studies.[^s2] Gene Glass coined "meta-analysis" in 1976 for the statistical combination of results from many studies.[^s2] The push for *systematic* methods came from a critique of the traditional narrative review: Pillemer called such reviews subjective and idiosyncratic, and social scientists showed that how studies were selected could itself bias a review, notably through publication bias toward significant results.[^s2] In medicine, Mulrow (1987) found that review articles in four major journals did not use scientific methods to identify, assess and synthesise evidence.[^s2]

Archie Cochrane had criticised the medical profession for not organising critical summaries of randomised trials; that criticism inspired Iain Chalmers and colleagues, the UK Cochrane Centre opened in 1992, and the international Cochrane Collaboration was founded in 1993.[^s1][^s2] The Campbell Collaboration followed at the start of the 2000s for social and educational policy.[^s2]

## How it works

Suppose a product team must decide whether to require two-person code review. One engineer circulates three blog posts and a conference talk showing fewer defects after pair review; another circulates two posts showing slower delivery. Each has, knowingly or not, chosen the evidence that suits them. A systematic approach instead fixes the question (does mandatory second review reduce escaped defects in teams like ours?), the sources to search, and the criteria a study must meet, and only then collects and appraises everything that qualifies, reporting what was excluded and why.[^s1][^s3] The answer may be less tidy, but it is no longer an artefact of who did the choosing.

The stakes of skipping this step have been measured. Antman and colleagues (1992) compared textbook and review recommendations for heart-attack treatment with cumulative syntheses of the trials and found that advice on some life-saving treatments lagged the evidence by more than a decade, while some harmful practices were still recommended long after trials had shown harm.[^s2]

## How to apply it

1. **Write the question and protocol first.** State the question, eligibility criteria and analysis plan in a protocol before looking at results.[^s1]
2. **Search broadly and record the search.** Report full search strategies so others could rerun them.[^s3]
3. **Select studies transparently.** Say how many people screened records and whether they worked independently, and show the path from records found to studies included in a flow diagram.[^s3]
4. **Appraise each study.** Assess risk of bias in the included studies rather than counting them as equal.[^s1][^s3]
5. **Look for what is missing.** PRISMA 2020 asks reviewers to assess the risk of bias due to missing results, the gap left when unfavourable findings go unreported.[^s3] Historians of the method stress that publication bias is one of the main ways a review can mislead.[^s2]
6. **Synthesise and report everything.** The 27-item PRISMA checklist lets readers judge whether the methods were appropriate and how far to trust the findings.[^s3]

For everyday questions a full review is impractical, but the habits scale down: decide what would count as relevant evidence before searching, look for the studies that would disconfirm your view, and ask of any summary you are handed how its sources were chosen.[^s1][^s2]

## Evidence and limitations

Systematic review is a methodological standard, not a guarantee. Ioannidis (2016) reported that annual publication of systematic reviews rose about 2,700 percent between 1991 and 2014, against 153 percent for all PubMed items, with some questions covered by more than 20 overlapping meta-analyses (185 on antidepressants for depression between 2007 and 2014).[^s4] He argued that many are redundant, seriously flawed or tied to sponsors whose interests their conclusions tend to favour, and that few are both non-misleading and useful.[^s4] A review is only as good as the studies it can find: if unfavourable results were never published, a thorough search still inherits the gap, which is why reporting guidelines ask reviewers to assess missing results explicitly.[^s3][^s2] Readers therefore need to appraise the review itself, starting with its protocol, search and conflicts of interest.[^s3][^s4]

## Connections

- **Counteracts suppressed evidence.** Fixing eligibility criteria and methods in advance limits the selective choices that produce cherry-picked summaries.[^s1]
- **Detects publication bias.** The research-synthesis tradition grew partly from recognising that selection toward significant results biases reviews, and modern reviews look for it.[^s2]
- **Influenced by Archie Cochrane.** His call for organised critical summaries of trials inspired the Cochrane Collaboration.[^s1]
- **Applied in evidence-based medicine.** Antman's comparison of textbook advice with trial syntheses showed why clinical guidance should rest on systematic reviews.[^s2]
- **Challenged by Ioannidis (2016).** His analysis documents mass production of redundant and conflicted reviews.[^s4]
- **Related to meta-analysis and preregistration.** Meta-analysis, as Glass defined it, is the statistical combination of study results that a review may include, and a review's advance protocol, like preregistration, limits choices made after the results are known.[^s1][^s2]

## Sources

[^s1]: Cumpston, Flemyng, Thomas, Higgins, Deeks & Clarke, "Chapter I: Introduction", *Cochrane Handbook for Systematic Reviews of Interventions*, version 6.5, Cochrane (2024). https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-i (accessed 2026-11-09)
[^s2]: Chalmers, Hedges & Cooper, "A brief history of research synthesis", *Evaluation & the Health Professions* 25(1) (2002), 12-37. https://dukespace.lib.duke.edu/server/api/core/bitstreams/5541cd3e-4a21-461a-9862-fe5a69294275/content (accessed 2026-11-09)
[^s3]: Page, McKenzie, Bossuyt et al., "The PRISMA 2020 statement: an updated guideline for reporting systematic reviews", *BMJ* 372 (2021), n71. https://eprints.whiterose.ac.uk/id/eprint/173303/1/bmj.n71.full.pdf (accessed 2026-11-09)
[^s4]: Ioannidis, "The Mass Production of Redundant, Misleading, and Conflicted Systematic Reviews and Meta-analyses", *The Milbank Quarterly* 94(3) (2016), 485-514. https://www.milbank.org/quarterly/articles/mass-production-redundant-misleading-conflicted-systematic-reviews-meta-analyses/ (accessed 2026-11-09)
