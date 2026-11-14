---
id: ct:statistical-reasoning
type: ReasoningMode
title: Statistical reasoning
aliases: [reasoning with data, statistical inference in everyday reasoning]
domain: probabilistic-reasoning
summary: >-
  The way people reason with statistical ideas and make sense of data: drawing
  conclusions about populations, processes or causes from samples while taking
  account of variation, chance, sample size and how the data were produced.
  It is an ampliative, inductive mode of reasoning whose conclusions are
  probable rather than certain.
level: intermediate
evidenceStatus: normative
broader: [ct:inductive-reasoning]
related: [ct:bayesian-reasoning, ct:null-hypothesis-significance-testing, ct:regression-to-the-mean, ct:random-sampling, ct:numeracy, ct:statistical-reasoning-training, ct:problem-of-induction, ct:hypothesis-testing]
requires: [ct:inductive-reasoning]
relations:
  - {predicate: studiedIn, object: ct:philosophy-of-statistics, source: s1, confidence: high}
  - {predicate: studiedIn, object: ct:statistics-education, source: s2, confidence: high}
  - {predicate: formalizedBy, object: ct:probability-theory, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:outcome-approach, source: s4, confidence: high}
  - {predicate: contrastsWith, object: ct:law-of-small-numbers, source: s2, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Philosophy of Statistics"
    publisher: Stanford Encyclopedia of Philosophy (Romeijn, 2014; revised 2025)
    url: https://plato.stanford.edu/ENTRIES/statistics/
    type: scholarly-encyclopedia
    accessed: 2026-11-14
  - id: s2
    title: "The Challenge of Developing Statistical Reasoning"
    publisher: Journal of Statistics Education 10(3) (Garfield, 2002)
    url: https://jse.amstat.org/v10n3/garfield.html
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s3
    title: "Statistical thinking in empirical enquiry"
    publisher: International Statistical Review 67(3), 223-265 (Wild & Pfannkuch, 1999), IASE author copy
    url: https://www.stat.auckland.ac.nz/~iase/publications/isr/99.Wild.Pfannkuch.pdf
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s4
    title: "Informal Conceptions of Probability"
    publisher: Cognition and Instruction 6(1), 59-98 (Konold, 1989), UMass SRRI copy
    url: https://srri.umass.edu/sites/srri/files/Konold1989/index.pdf
    type: primary
    accessed: 2026-11-14
created: 2026-11-14
---

# Statistical reasoning

Statistical reasoning is the way people reason with statistical ideas and make sense of statistical information: reading data, graphs and summaries, and drawing on ideas such as distribution, centre, spread, association, randomness, uncertainty and sampling. Joan Garfield, adopting a definition she and Iddo Gal proposed in 1999, notes that the label is often used interchangeably with "statistical thinking" and that there is no settled consensus on where one ends and the other begins.[^s2] Philosophically, it is a form of inductive inference: it relates data to hypotheses stated as probability distributions over possible samples, and its conclusions go beyond what the data strictly entail.[^s1]

## Origin

Formal statistics grew out of probability theory, and its competing schools frame the reasoning differently. The classical tradition of Fisher and of Neyman and Pearson tests hypotheses and controls long-run error rates; the Bayesian tradition updates degrees of belief from prior to posterior; likelihoodists, following Hacking, Edwards and Royall, read likelihoods as measures of evidential support.[^s1] Jan-Willem Romeijn's encyclopedia entry presents all three as attempts to answer Hume's problem of induction, or to reinterpret their outputs so they sidestep it.[^s1]

Statistical reasoning as a teachable competence, rather than a set of procedures, became a research topic in statistics education in the 1980s and 1990s. Clifford Konold's 1989 interview study of informal probability reasoning,[^s4] Chris Wild and Maxine Pfannkuch's 1999 framework built from interviews with students and professional statisticians,[^s3] and Garfield's 2002 review of how students develop reasoning about sampling and distributions[^s2] are landmarks of that work.

## How it works

Wild and Pfannkuch describe statistical thinking in an enquiry as four interacting dimensions: an investigative cycle (problem, plan, data, analysis, conclusions); characteristic types of thinking; an interrogative cycle of generating, seeking, interpreting, criticising and judging; and dispositions such as curiosity, scepticism and perseverance.[^s3] The types of thinking they single out as fundamental are recognising the need for data rather than anecdote, re-representing data to understand it ("transnumeration"), noticing and modelling variation, reasoning with statistical models, and moving back and forth between statistical and contextual knowledge.[^s3]

A workplace example shows the moves. A support team's weekly satisfaction average falls from 4.3 to 3.9, based on 15 survey replies, and a manager proposes retraining. A statistical reasoner first asks how much the weekly average normally varies, how 15 replies compare with the usual volume, who chose to respond, and whether last week's 4.3 was itself unusually high, so that some fall back was to be expected. Only if the drop stands out against ordinary week-to-week variation, and the sample is not obviously skewed, does it count as a signal worth acting on. This is the habit of judging a result against its variation and sampling process, rather than reading every change as a cause.[^s3][^s2]

## Common failures

Garfield lists recurring misconceptions: treating an average as the most common value, believing a good sample must be a large share of the population, expecting small random samples to mirror the population closely (the law of small numbers), and believing a tail is due after a run of heads.[^s2] Konold identified an "outcome approach" in which people treat a probability question as a call about the next single trial: a 70% rain forecast is read as a prediction that it will rain, and the forecaster is judged wrong if it does not.[^s4] In his study of 16 undergraduates, several judged a forecaster who said 70% on ten days and saw rain on seven to be only fairly accurate, although seven of ten is exactly what a well-calibrated 70% forecast predicts.[^s4]

## How to apply it

- Ask what process produced the data, and whether the sample could differ systematically from the population of interest.[^s3]
- Compare any difference or change with the variation you would expect by chance, and be wary of small samples.[^s2]
- Judge probabilistic forecasts across many cases, not on single outcomes.[^s4][^s2]
- State conclusions with their uncertainty, and keep the statistical result tied to its real-world context.[^s3][^s1]

## Evidence and limitations

The research is largely descriptive and small-scale. Konold's interview sample was small and homogeneous, and he cautions that it cannot show how widespread the outcome approach is, though students who had taken a statistics course showed it less.[^s4] Garfield reports that students can earn good grades in statistics courses yet score poorly on the Statistical Reasoning Assessment, because teaching tends to cover procedures and assume reasoning will follow; she calls for more classroom research on what helps.[^s2] At the philosophical level there is no agreement on whether statistical conclusions are inferences at all, or which school's reading of probability is correct, so "good statistical reasoning" is itself partly school-relative.[^s1]

## Connections

Statistical reasoning is a species of inductive reasoning and a natural home for the problem of induction, which is why it is studied in the philosophy of statistics and formalised by probability theory.[^s1] It is also a central object of research in statistics education.[^s2] Bayesian reasoning and null-hypothesis significance testing are two of its formal schools.[^s1] It stands in contrast to Konold's outcome approach, which reads probabilities as single-case predictions,[^s4] and to the intuitive law of small numbers, which Garfield lists among the misconceptions it must overcome.[^s2] Statistical reasoning training is the debiasing technique that tries to teach it directly.

## Sources

[^s1]: Romeijn, "Philosophy of Statistics", Stanford Encyclopedia of Philosophy (2014; rev. 2025). https://plato.stanford.edu/ENTRIES/statistics/ (accessed 2026-11-14)
[^s2]: Garfield, "The Challenge of Developing Statistical Reasoning", Journal of Statistics Education 10(3), 2002. https://jse.amstat.org/v10n3/garfield.html (accessed 2026-11-14)
[^s3]: Wild & Pfannkuch, "Statistical thinking in empirical enquiry", International Statistical Review 67(3), 1999. https://www.stat.auckland.ac.nz/~iase/publications/isr/99.Wild.Pfannkuch.pdf (accessed 2026-11-14)
[^s4]: Konold, "Informal Conceptions of Probability", Cognition and Instruction 6(1), 1989. https://srri.umass.edu/sites/srri/files/Konold1989/index.pdf (accessed 2026-11-14)
