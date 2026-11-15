---
id: ct:weighted-additive-rule
type: Technique
title: Weighted additive rule
aliases: [WADD, weighted additive strategy, Franklin's rule, moral algebra, prudential algebra]
domain: decision-making
summary: >-
  A compensatory way of choosing among options: rate every option on every
  relevant attribute, multiply each rating by how much that attribute matters,
  add the products and pick the option with the highest total, so that strengths
  on some attributes can make up for weaknesses on others.
level: introductory
evidenceStatus: mixed
broader: [ct:decision-analysis, ct:decision-strategy]
related: [ct:take-the-best, ct:ecological-rationality, ct:fast-and-frugal-heuristics, ct:bounded-rationality, ct:expected-utility-theory, ct:value-focused-thinking, ct:overfitting]
requires: [ct:judgment-and-decision-making]
relations:
  - {predicate: counteracts, object: ct:take-the-best, source: s3, confidence: medium}
  - {predicate: introducedBy, object: ct:benjamin-franklin, source: s1, confidence: medium}
  - {predicate: contrastsWith, object: ct:elimination-by-aspects, source: s2, confidence: high}
  - {predicate: supportedBy, object: ct:the-robust-beauty-of-improper-linear-models, source: s4, confidence: high}
  - {predicate: studiedIn, object: ct:judgment-and-decision-making, source: s2, confidence: high}
  - {predicate: challengedBy, object: ct:one-reason-decision-making, source: s5, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Benjamin Franklin to Joseph Priestley, 19 September 1772"
    publisher: Founders Online, U.S. National Archives (The Papers of Benjamin Franklin, vol. 19)
    url: https://founders.archives.gov/documents/Franklin/01-19-02-0200
    type: primary
    accessed: 2026-11-15
  - id: s2
    title: "Adaptive Strategy Selection in Decision Making"
    publisher: Payne, Bettman & Johnson, Technical Report 86-1, Office of Naval Research (1986), via DTIC
    url: https://apps.dtic.mil/sti/pdfs/ADA170858.pdf
    type: primary
    accessed: 2026-11-15
  - id: s3
    title: "On heuristic and linear models of judgment: Mapping the demand for knowledge"
    publisher: "Hogarth & Karelaia, Universitat Pompeu Fabra working paper 974 (2006); published as Heuristic and linear models of judgment - Matching rules and environments, Psychological Review 114(3), 2007"
    url: https://econ-papers.upf.edu/papers/974.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s4
    title: "The robust beauty of improper linear models in decision making"
    publisher: American Psychologist 34(7), 571-582 (Dawes, 1979), Carnegie Mellon University copy
    url: https://www.cmu.edu/dietrich/sds/docs/dawes/the-robust-beauty-of-improper-linear-models-in-decision-making.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s5
    title: "One-reason decision making"
    publisher: Gigerenzer, Martignon, Hoffrage, Rieskamp, Czerlinski & Goldstein, Handbook of Experimental Economics Results vol. 1, ch. 108 (Elsevier, 2008), Max Planck repository
    url: https://pure.mpg.de/pubman/item/item_2100203_3/component/file_2100202/GG_One_2008.pdf
    type: primary
    accessed: 2026-11-15
  - id: s6
    title: "Children's application of decision strategies in a compensatory environment"
    publisher: Judgment and Decision Making 13(6), 514-528 (Betsch, Lehmann, Jekel, Lindow & Glöckner, 2018)
    url: https://dlab.sauder.ubc.ca/sjdm/journal/18/18225/jdm18225.html
    type: peer-reviewed
    accessed: 2026-11-15
created: 2026-11-15
---

# Weighted additive rule

The weighted additive rule (WADD) is the "add it all up" way of choosing. You score each option on every attribute that matters, multiply each score by that attribute's importance weight, sum the products, and choose the option with the highest total.[^s2] Because every attribute contributes, a strong showing on one can offset a weak showing on another: the rule is *compensatory*, the opposite of one-reason rules such as take-the-best that stop at the first attribute that separates the options.[^s2][^s5]

## Origin

The informal version is old. In a letter of 19 September 1772, Benjamin Franklin advised the chemist Joseph Priestley, who was weighing a job offer as librarian to Lord Shelburne, to use what Franklin called "moral or prudential algebra".[^s1] Priestley was to list reasons for and against in two columns over three or four days, estimate each reason's weight, strike out reasons of equal weight on opposite sides (one strong reason could cancel two weaker ones), and decide by the balance that remained.[^s1] Franklin conceded the weights are imprecise but held that seeing all reasons at once guards against rash choices.[^s1]

The modern, explicit form comes from judgment and decision-making research. John Payne, James Bettman and Eric Johnson, in a 1986 report for the Office of Naval Research, defined WADD formally and set it against heuristics such as the lexicographic rule, equal weighting and elimination by aspects, measuring each strategy's accuracy and the mental effort it costs.[^s2]

## How it works

Workplace example: a team is choosing between two project-management tools. The criteria and weights are security (40%), ease of use (30%), integration with existing systems (20%) and price (10%). Tool A scores 9, 5, 4 and 6 out of 10; Tool B scores 8, 8, 8 and 4. A's weighted total is 3.6 + 1.5 + 0.8 + 0.6 = 6.5; B's is 3.2 + 2.4 + 1.6 + 0.4 = 7.6. B wins even though A is better on the most important criterion. A one-reason rule looking only at security would have picked A.[^s2][^s5]

A simplified variant drops the weights and simply adds standardised scores. Robyn Dawes showed in 1979 that such equal-weight ("improper") linear models usually predict nearly as well as statistically optimised weights and better than expert judges: in one graduate-admissions study the equal-weight composite correlated .48 with later faculty ratings, against .19 for the admissions committee.[^s4] The hard part, Dawes argued, is choosing the right attributes and knowing which direction each points; once those are fixed, people are worse at integrating them in their heads than a simple sum is.[^s4]

## How to apply it

1. **List the options and the attributes** that genuinely bear on the goal, and agree on which direction is better for each.[^s4]
2. **Weight the attributes** by importance. If you lack a sound basis for fine weights, equal weights on standardised scores are a robust default.[^s4]
3. **Score every option on every attribute** on a common scale, gathering evidence rather than impressions.[^s2]
4. **Multiply and sum**, then look at which attributes drive the gap and whether a reasonable change of weights would flip the result.[^s4]
5. **Let it sit.** Franklin recommended waiting a day or two to see whether new considerations appear before acting.[^s1]

**When to use it:** choices with several attributes that each carry real weight, where a strength on one can sensibly make up for a weakness on another, and where there is time to gather the scores.[^s3][^s5]

**Pitfalls:** the full rule is effortful. In Payne and colleagues' studies, its accuracy fell sharply under severe time pressure, when faster attribute-based heuristics did better and people shifted toward them.[^s2] Weighted sums also add little when one attribute matters more than all the others combined; in such noncompensatory environments take-the-best gives the same answers with less work.[^s5] Weights estimated from small samples can overfit, which is one reason equal weights often hold up better out of sample.[^s4][^s5]

## Evidence

Comparisons show that no strategy wins everywhere. Hogarth and Karelaia's analysis (2006 working paper, published 2007), combining theory, simulation and a meta-analysis of lens-model studies, found that when cue weights are similar (a compensatory environment) equal-weight adding was the most accurate rule, at about 77% correct, while take-the-best and single-variable rules did best when weights were steeply dispersed.[^s3] Their meta-analysis of 252 judgment tasks found people too inconsistent at intuitive weighing to beat good heuristics, so they advised mapping the task before choosing a rule.[^s3] Gigerenzer and colleagues, in their 2008 review, reported that across 20 real-world data sets take-the-best predicted out of sample more accurately on average than both multiple regression and a unit-weight model, while proving that a unit-weight model has the advantage when many uncertain cues are available.[^s5] Adults do apply the rule when the environment calls for it: in a 2018 study with a compensatory task, 74% of 31 adults were classified as WADD users, compared with 21% of 9-to-10-year-olds and none of the preschoolers tested.[^s6] Hence the *mixed* status: weighing everything is reliably better than a single cue in compensatory settings, but it is not the best strategy in every environment.[^s3][^s5]

## Connections

- It **counteracts** take-the-best where that heuristic fails: in compensatory environments, where several moderate cues together outweigh the top one, additive integration was more accurate than stopping at the first discriminating cue.[^s3]
- It was **introduced by** Benjamin Franklin in its informal pro-and-con form, the "moral or prudential algebra" of his 1772 letter to Joseph Priestley.[^s1]
- It **contrasts with** elimination by aspects and the other attribute-based heuristics that Payne, Bettman and Johnson set against it in their effort-accuracy analysis.[^s2]
- Its simplest version is **supported by** Dawes's "The robust beauty of improper linear models", which showed equal-weight sums outpredicting expert judges.[^s4]
- It is **studied in** **judgment and decision making**, where it serves as the normative benchmark for strategy choice.[^s2]
- It is **challenged by** Gigerenzer and colleagues' "One-reason decision making", which shows that in noncompensatory and data-poor environments one good reason can predict as well or better.[^s5]

## Sources

[^s1]: Franklin, letter to Joseph Priestley, 19 September 1772, Founders Online, U.S. National Archives. https://founders.archives.gov/documents/Franklin/01-19-02-0200 (accessed 2026-11-15)
[^s2]: Payne, Bettman & Johnson, "Adaptive Strategy Selection in Decision Making", ONR Technical Report 86-1, 1986. https://apps.dtic.mil/sti/pdfs/ADA170858.pdf (accessed 2026-11-15)
[^s3]: Hogarth & Karelaia, "On heuristic and linear models of judgment: Mapping the demand for knowledge", UPF working paper 974, 2006 (published in *Psychological Review* 114(3), 2007). https://econ-papers.upf.edu/papers/974.pdf (accessed 2026-11-15)
[^s4]: Dawes, "The robust beauty of improper linear models in decision making", *American Psychologist* 34(7), 1979. https://www.cmu.edu/dietrich/sds/docs/dawes/the-robust-beauty-of-improper-linear-models-in-decision-making.pdf (accessed 2026-11-15)
[^s5]: Gigerenzer, Martignon, Hoffrage, Rieskamp, Czerlinski & Goldstein, "One-reason decision making", *Handbook of Experimental Economics Results* vol. 1, 2008. https://pure.mpg.de/pubman/item/item_2100203_3/component/file_2100202/GG_One_2008.pdf (accessed 2026-11-15)
[^s6]: Betsch, Lehmann, Jekel, Lindow & Glöckner, "Children's application of decision strategies in a compensatory environment", *Judgment and Decision Making* 13(6), 2018. https://dlab.sauder.ubc.ca/sjdm/journal/18/18225/jdm18225.html (accessed 2026-11-15)
