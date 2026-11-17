---
id: ct:survivorship-bias
type: CognitiveBias
title: Survivorship bias
aliases: [survivor bias, survivorship error]
domain: cognitive-biases
summary: >-
  The error of drawing conclusions from the cases that made it through a
  selection process (the surviving firms, funds, products or people) while
  overlooking the cases that were filtered out, whose absence makes the
  survivors look more typical, skilful or causally instructive than they are.
level: introductory
evidenceStatus: mixed
broader: [ct:cognitive-bias, ct:selection-bias]
related: [ct:abraham-wald, ct:base-rate-neglect, ct:availability-heuristic, ct:hasty-generalization, ct:regression-to-the-mean, ct:publication-bias, ct:consider-the-opposite]
requires: [ct:selection-bias]
relations:
  - {predicate: instanceOf, object: ct:selection-bias, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: ct:feiler-tong-larrick-2013-censorship-bias-study, source: s4, confidence: medium}
  - {predicate: supportedBy, object: ct:denrell-2003-undersampling-of-failure, source: s3, confidence: high}
  - {predicate: studiedIn, object: ct:finance, source: s5, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Survivorship bias"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/science/survivorship-bias
    type: encyclopedia
    accessed: 2026-11-17
  - id: s2
    title: "The Legend of Abraham Wald"
    publisher: American Mathematical Society, Feature Column (Casselman, University of British Columbia, 2016)
    url: https://www.ams.org/samplings/feature-column/fc-2016-06
    type: institutional
    accessed: 2026-11-17
  - id: s3
    title: "Vicarious learning, undersampling of failure, and the myths of management"
    publisher: Organization Science 14(3), 227-243 (Denrell, 2003), Stanford GSB publication record
    url: https://www.gsb.stanford.edu/faculty-research/publications/vicarious-learning-undersampling-failure-myths-management
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s4
    title: "Biased judgment in censored environments"
    publisher: Management Science 59(3), 573-591 (Feiler, Tong & Larrick, 2013), doi:10.1287/mnsc.1120.1612, Duke Scholars record
    url: https://scholars.duke.edu/publication/938357
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s5
    title: "Survivorship bias in performance studies"
    publisher: Review of Financial Studies 5(4), 553-580 (Brown et al., 1992), IDEAS/RePEc record
    url: https://ideas.repec.org/a/oup/rfinst/v5y1992i4p553-80.html
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s6
    title: "Everyday econometricians: Selection neglect and overoptimism when learning from others"
    publisher: WZB Working Paper 2023-24 (Barron, Huck & Jehiel, 2023)
    url: https://philippe-jehiel.enpc.fr/wp-content/uploads/sites/2/2024/05/wp_202324_.pdf
    type: preprint
    accessed: 2026-11-17
created: 2026-11-17
---

# Survivorship bias

Survivorship bias is the error of reasoning only from the entities that passed through some selective filter, while the ones that failed the filter drop out of view; the conclusions drawn from what remains are then distorted.[^s1] In statistical terms it is a form of sampling bias: the cases still observable at the end of a period are not a fair sample of the group that started it.[^s1] As a thinking error it is quieter than most biases, because nothing in the evidence on the table looks wrong. The problem is what is missing from the table.[^s3]

## Origin

The best-known illustration comes from the Second World War. Abraham Wald, a Columbia statistician working with the Statistical Research Group, wrote memoranda on how to estimate aircraft vulnerability using damage data from bombers that returned, making explicit assumptions about the planes that did not.[^s2] The popular retelling, in which Wald told the military to armour the parts of returning planes that showed the fewest holes, is largely reconstruction: his memoranda contain no such recommendation, though a later note by his colleague W. Allen Wallis does credit him with the underlying insight that hits to the most vulnerable areas were the ones least likely to show up on planes that made it home.[^s2] The term is long established in finance, where Brown and colleagues showed in 1992 that studying only the funds that survive can create an illusion that past performance predicts future performance.[^s5]

## How it works

A selection process removes cases for reasons related to the outcome you care about, and you then compare or generalise from the remainder.[^s1] Consider a team lead who reads the post-mortems of the company's three most successful product launches and notices that each one skipped user research to ship fast. The lesson "speed beats research" seems obvious. But launches that skipped research and flopped were quietly cancelled and never written up, so the sample cannot show whether skipping research helps, hurts or does nothing.[^s3] Denrell's analysis of organisational learning makes this general: because failed firms vanish and the business press concentrates on winners, risky practices that make outcomes more extreme can look like recipes for success among survivors, even when they have no benefit across all firms that tried them.[^s3] The same structure appears in investment: funds with poor returns are closed or merged, so averages over surviving funds overstate typical performance and can even fabricate apparent persistence of skill.[^s5]

## Evidence

The statistical effect is well established; the psychological claim that people fail to correct for it has narrower but growing support.[^s5] In four studies, Feiler, Tong and Larrick found that people judging from censored samples (where outcomes beyond a cut-off are hidden) leaned too heavily on what they saw, and the error grew with stronger censorship and greater variability, producing costly and overly cautious decisions.[^s4] A 2023 working paper by Barron, Huck and Jehiel, with a lab experiment of 192 participants and an online study of about 1,000, found that most people learning from others' selected outcomes behaved close to a fully naive benchmark; prompts and extra information did not reduce the neglect when the data-generating process was complex.[^s6] That paper was not yet peer-reviewed when consulted, and the effect appears to depend on how complex and how censored the environment is, so evidence status is recorded here as mixed rather than robust.[^s4][^s6]

## How to spot it

Ask where the sample came from and what process decided which cases you can now see.[^s1] Warning signs include advice drawn from "how the winners did it" (successful founders, top performers, long-lived buildings), datasets that contain only currently existing firms, products or accounts, and follow-up surveys where people with worse outcomes were more likely to drop out.[^s1] If the filter that removed cases is plausibly linked to the outcome itself, the remaining sample cannot settle the question.[^s3]

## How to counter it

Reconstruct the denominator: list everyone who tried the practice, not only those who succeeded, and compare success rates with and without it.[^s3] Use datasets that retain dead or delisted cases, which is how finance researchers estimate the size of the distortion.[^s5] When the missing cases cannot be recovered, state the assumptions about them explicitly, as Wald's memoranda did, instead of treating the visible sample as representative.[^s2] Because simple warnings appear to help little, structural fixes that bring the failures into view are likely to work better than exhortation.[^s6]

## Connections

Survivorship bias is an instance of [[selection-bias]]: the sample is distorted by the process that decides which cases remain observable.[^s1] Feiler, Tong and Larrick's censored-environment studies demonstrate the judgment error under controlled conditions.[^s4] Denrell's model of undersampled failure supports the claim that it systematically distorts managerial theories of success.[^s3] It is studied extensively in finance, where fund and stock databases that drop failures bias performance estimates.[^s5] It sits alongside [[base-rate-neglect]] and [[hasty-generalization]], since all three involve generalising without attending to the full reference class, and [[consider-the-opposite]] is a natural prompt for asking what the unseen cases would show.[^s3]

## Sources

[^s1]: Encyclopaedia Britannica, "Survivorship bias". https://www.britannica.com/science/survivorship-bias (accessed 2026-11-17)
[^s2]: Casselman, "The Legend of Abraham Wald", AMS Feature Column, 2016. https://www.ams.org/samplings/feature-column/fc-2016-06 (accessed 2026-11-17)
[^s3]: Denrell, "Vicarious learning, undersampling of failure, and the myths of management", Organization Science 14(3), 2003. https://www.gsb.stanford.edu/faculty-research/publications/vicarious-learning-undersampling-failure-myths-management (accessed 2026-11-17)
[^s4]: Feiler, Tong & Larrick, "Biased judgment in censored environments", Management Science 59(3), 2013. https://scholars.duke.edu/publication/938357 (accessed 2026-11-17)
[^s5]: Brown et al., "Survivorship bias in performance studies", Review of Financial Studies 5(4), 1992. https://ideas.repec.org/a/oup/rfinst/v5y1992i4p553-80.html (accessed 2026-11-17)
[^s6]: Barron, Huck & Jehiel, "Everyday econometricians: Selection neglect and overoptimism when learning from others", WZB Working Paper 2023-24. https://philippe-jehiel.enpc.fr/wp-content/uploads/sites/2/2024/05/wp_202324_.pdf (accessed 2026-11-17)
