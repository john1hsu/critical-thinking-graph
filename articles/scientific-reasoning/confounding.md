---
id: ct:confounding
type: Phenomenon
title: Confounding
aliases: [confounding bias, confounder, confounding variable, lurking variable, third-variable problem]
domain: scientific-reasoning
summary: >-
  The distortion of an apparent cause-and-effect relationship that occurs when
  the exposure and the outcome share a common cause, so that the groups being
  compared differ in their risk of the outcome for reasons other than the
  exposure itself.
level: introductory
evidenceStatus: robust
broader: [ct:causal-inference]
related: [ct:correlation-versus-causation, ct:simpsons-paradox, ct:randomized-controlled-trial, ct:mills-methods, ct:selection-bias, ct:post-hoc-ergo-propter-hoc, ct:causal-diagrams]
requires: [ct:correlation-versus-causation]
relations:
  - {predicate: formalizedBy, object: ct:causal-diagrams, source: s3, confidence: high}
  - {predicate: appliedIn, object: ct:epidemiology, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:ronald-fisher, source: s4, confidence: medium}
  - {predicate: introducedIn, object: ct:the-design-of-experiments, source: s4, confidence: medium}
  - {predicate: contrastsWith, object: ct:berksons-paradox, source: s3, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Confounding: a routine concern in the interpretation of epidemiological studies"
    publisher: "IARC Statistical Methods in Cancer Research Vol. V (Scientific Publication No. 171), ch. 3 (Richardson, Costello, Kaufman et al., 2024)"
    url: https://publications.iarc.fr/_publications/media/download/7289/e5e6a8f8bd7a1e202db8280d5637d8ae0a939284.pdf
    type: intergovernmental
    accessed: 2026-11-08
  - id: s2
    title: "Simpson's Paradox, Confounding, and Collapsibility"
    publisher: "Causality: Models, Reasoning, and Inference, 2nd ed., ch. 6, pp. 173-200, Cambridge University Press (Pearl, 2009), doi:10.1017/CBO9780511803161.008"
    url: https://www.cambridge.org/core/books/causality/simpsons-paradox-confounding-and-collapsibility/034402052E7C35736C06AA13DF709B59
    type: primary
    accessed: 2026-11-08
  - id: s3
    title: "Understanding Simpson's Paradox"
    publisher: "UCLA Cognitive Systems Laboratory Technical Report R-414 (Pearl, 2013); published in The American Statistician, 2014"
    url: https://ftp.cs.ucla.edu/pub/stat_ser/r414.pdf
    type: academic
    accessed: 2026-11-08
  - id: s4
    title: "The history of confounding"
    publisher: "Sozial- und Präventivmedizin 47(4):216-224 (Vandenbroucke, 2002), doi:10.1007/BF01326402"
    url: https://link.springer.com/article/10.1007/BF01326402
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s5
    title: "Confounding factors may be the reason that randomized controlled trials of HRT conflict with observational studies"
    publisher: "Agency for Healthcare Research and Quality, Research Activities, January 2004 (summarising Ray, American Journal of Epidemiology 158(9):915-920, 2003); archived by the UNT End of Term web archive"
    url: https://webarchive.library.unt.edu/eot2008/20081105021835/http:/www.ahrq.gov/research/jan04/0104RA6.htm
    type: government
    accessed: 2026-11-08
created: 2026-11-08
---

# Confounding

Confounding is what happens when an exposure and an outcome share a common cause, so that part of the association between them reflects differences between the compared groups rather than any effect of the exposure. The variable responsible is called a confounder: typically something that causes the outcome, is associated with the exposure, and is not itself a consequence of the exposure.[^s1] Because it concerns what would have happened to the same people without the exposure, confounding is a causal notion; Judea Pearl argues that it cannot be defined from frequency data alone and needs assumptions about causal structure.[^s2]

## Origin

The underlying problem is as old as comparison itself. Jan Vandenbroucke's history traces it to John Stuart Mill's demand that "all other things be equal" when using the method of difference, while noting that the word originally meant simply to mix up or fail to distinguish.[^s4] Ronald Fisher was, to Vandenbroucke's knowledge, the first to use "confounding" for research design, in *The Design of Experiments*; there it named a deliberate device in agricultural field trials, in which some higher-order interactions were intentionally mixed with other effects to save plots.[^s4] The modern sense of an unwanted, uncontrolled extraneous variable entangled with the factor of interest came from Leslie Kish, writing on social-science research design in 1959, and epidemiologists such as Jerome Cornfield and Olli Miettinen later separated it from selection and measurement bias and made the choice of confounders an explicit prior judgement.[^s4]

## How it works

Suppose a sales director sees that representatives who took an optional negotiation course closed 20% more deals the following quarter. If the most experienced and motivated reps were the ones who signed up, experience is a common cause: it raises the chance of enrolling and, independently, the chance of closing deals. The course and the results then move together even if the course did nothing, which is exactly the "differences in outcome risk not caused by the exposure" that defines confounding.[^s1]

Confounding can be strong enough to reverse a conclusion. In Simpson's paradox, a treatment can look beneficial in aggregate yet harmful in every subgroup once a pre-treatment variable such as sex, which influences both who is treated and who recovers, is taken into account.[^s3] Which table to trust depends on the causal story, not the numbers: Pearl's back-door criterion says to adjust for a variable that blocks every back-door path into the exposure and is not caused by it.[^s3]

## How to spot and control it

1. **Ask who got the exposure and why.** Any reason for receiving it that also affects the outcome is a candidate confounder; check that it precedes the exposure and is related to both exposure and outcome.[^s1]
2. **Randomise when you can.** Random assignment is the most widely accepted way to break the link between confounders and exposure, though it is often infeasible for ethical or practical reasons.[^s1]
3. **Restrict or match.** Studying only one level of the suspected confounder (for example, only non-smokers) or matching on it can remove its influence, but restricting on the wrong variable can create bias.[^s1]
4. **Adjust in the analysis, carefully.** Stratification and multivariable models handle measured confounders; imperfect measurement leaves residual confounding, and adjusting for a mediator or a collider adds bias rather than removing it.[^s1][^s3]
5. **Name the alternative.** Vandenbroucke argues that reasoning about confounding is almost entirely a priori: a critic who suspects it should state which variable and how strong it would have to be.[^s4]

## Evidence

Confounding is one of the best-documented threats to causal conclusions. In the 1950s Fisher argued that an inherited constitution might cause both smoking and lung cancer; Cornfield and colleagues replied in 1959 that any such hidden factor would need an effect even larger than the roughly tenfold risk increase observed, a reasoning step that remains a template for judging proposed confounders.[^s4] Even randomised trials are not immune: Cornfield showed in 1971 that chance baseline imbalances can confound a trial's comparison.[^s4] A widely cited case is hormone therapy. Observational studies suggested it protected women's hearts, but randomised trials did not confirm this; a 2003 analysis by Wayne Ray, summarised by the US Agency for Healthcare Research and Quality, attributed the gap partly to women who chose hormone therapy having healthier cardiovascular profiles, a "healthy user" effect many studies had not measured.[^s5] The limitation is conceptual rather than empirical: no statistical test on the data alone can certify that confounding is absent, so control always rests on causal assumptions.[^s2]

## Connections

Confounding is **formalized by** causal diagrams, in which a confounder appears as an open back-door path that adjustment must block.[^s3] It is a routine concern **applied in** epidemiology, where hazard assessments judge whether residual confounding could explain reported associations.[^s1] The word was **introduced by** Ronald Fisher in **The Design of Experiments**, although in a design sense that later shifted to the modern one.[^s4] It **contrasts with** Berkson's paradox: conditioning on a confounder removes spurious association, whereas conditioning on a collider, a common effect, creates it.[^s3] Confounding is the main mechanism behind the gap between correlation and causation, explains reversals in Simpson's paradox, and is what randomised controlled trials and Mill's method of difference try to rule out.[^s1][^s3][^s4]

## Sources

[^s1]: Richardson, Costello, Kaufman et al., "Confounding: a routine concern in the interpretation of epidemiological studies", in *Statistical Methods in Cancer Research Vol. V*, IARC Scientific Publication No. 171, 2024. https://publications.iarc.fr/_publications/media/download/7289/e5e6a8f8bd7a1e202db8280d5637d8ae0a939284.pdf (accessed 2026-11-08)
[^s2]: Pearl, "Simpson's Paradox, Confounding, and Collapsibility", ch. 6 of *Causality: Models, Reasoning, and Inference*, 2nd ed., Cambridge University Press, 2009. https://www.cambridge.org/core/books/causality/simpsons-paradox-confounding-and-collapsibility/034402052E7C35736C06AA13DF709B59 (accessed 2026-11-08)
[^s3]: Pearl, "Understanding Simpson's Paradox", UCLA Technical Report R-414, 2013. https://ftp.cs.ucla.edu/pub/stat_ser/r414.pdf (accessed 2026-11-08)
[^s4]: Vandenbroucke, "The history of confounding", *Sozial- und Präventivmedizin* 47(4):216-224, 2002. https://link.springer.com/article/10.1007/BF01326402 (accessed 2026-11-08)
[^s5]: Agency for Healthcare Research and Quality, "Confounding factors may be the reason that randomized controlled trials of HRT conflict with observational studies", *Research Activities*, January 2004. https://webarchive.library.unt.edu/eot2008/20081105021835/http:/www.ahrq.gov/research/jan04/0104RA6.htm (accessed 2026-11-08)
