---
id: ct:bayesian-reasoning
type: ReasoningMode
title: Bayesian reasoning
aliases: [Bayesian inference, Bayesian updating, Bayesian belief revision, conditionalization]
domain: probabilistic-reasoning
summary: >-
  Reasoning that treats beliefs as degrees of probability and revises them in
  light of evidence by Bayes' theorem: the probability of a hypothesis after
  the evidence combines its prior probability with how much more likely the
  evidence is if the hypothesis is true than if it is false.
level: intermediate
evidenceStatus: normative
broader: [ct:inductive-reasoning]
related: [ct:base-rate-neglect, ct:natural-frequencies, ct:inference-to-the-best-explanation, ct:calibration, ct:conditional-probability]
requires: [ct:conditional-probability]
relations:
  - {predicate: introducedBy, object: ct:thomas-bayes, source: s5, confidence: high}
  - {predicate: appliedIn, object: ct:philosophy-of-science, source: s1, confidence: high}
  - {predicate: challengedBy, object: ct:problem-of-old-evidence, source: s1, confidence: high}
  - {predicate: studiedIn, object: ct:cognitive-psychology, source: s2, confidence: high}
argumentMap:
  premises:
    - "About 1% of the card transactions our team reviews turn out to be fraudulent."
    - "The new alert rule flags 90% of fraudulent transactions."
    - "It also flags 9% of legitimate transactions."
    - "This transaction was flagged."
  conclusion: "This transaction is probably legitimate: only about 9% of flagged transactions are fraud."
  verdict: valid
  objections:
    - "If the 1% base rate was measured on a different customer segment, the posterior may be badly off."
    - "Two independent alerts on the same transaction would raise the probability sharply; a second check is cheap."
sources:
  - id: s1
    title: "Bayesian Epistemology"
    publisher: Stanford Encyclopedia of Philosophy (Talbott, Summer 2006 archive edition)
    url: https://plato.stanford.edu/archives/Sum2006/entries/epistemology-bayesian/
    type: scholarly-encyclopedia
    accessed: 2026-11-08
  - id: s2
    title: "Why Can Only 24% Solve Bayesian Reasoning Problems in Natural Frequencies: Frequency Phobia in Spite of Probability Blindness"
    publisher: Frontiers in Psychology 9, 1833 (Weber, Binder & Krauss, 2018)
    url: https://www.frontiersin.org/articles/10.3389/fpsyg.2018.01833/pdf
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s3
    title: "Bayes' Theorem"
    publisher: Stanford Encyclopedia of Philosophy (Joyce, Spring 2018 archive edition)
    url: https://plato.stanford.edu/archives/spr2018/entries/bayes-theorem/
    type: scholarly-encyclopedia
    accessed: 2026-11-08
  - id: s4
    title: "The Use of Visualizations to Improve Bayesian Reasoning: A Literature Review"
    publisher: Vision 7 (Cui, Lo & Liu, 2023), eScholarship, University of California
    url: https://escholarship.org/content/qt5s9754p5/qt5s9754p5.pdf
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s5
    title: "An Essay towards solving a Problem in the Doctrine of Chances (Bayes, 1763), LaTeX edition"
    publisher: University of York, Department of Mathematics, history of statistics pages
    url: https://www.york.ac.uk/depts/maths/histstat/essay.htm
    type: primary
    accessed: 2026-11-08
created: 2026-11-08
---

# Bayesian reasoning

Bayesian reasoning treats belief as a matter of degree, measured by probability, and gives a rule for changing those degrees when evidence arrives.[^s1] It has two core commitments: a rational agent's degrees of belief should obey the laws of probability, and on learning evidence E with certainty, the new probability of a hypothesis should equal its old probability conditional on E, a rule called conditionalization.[^s1] Bayes' theorem supplies the arithmetic: the posterior probability of a hypothesis depends on its prior probability and on how probable the evidence would be if the hypothesis were true.[^s3] In practice this makes Bayesian reasoning the standard for questions like "how worried should I be about this positive test, alert or warning sign?"

## Origin

The theorem is named after Thomas Bayes, a Fellow of the Royal Society. After his death, his friend Richard Price found an essay among his papers and sent it to the Society, where it was read in December 1763 and printed in the *Philosophical Transactions*.[^s5] Bayes's problem was an inverse one: given how often an unknown event has happened and failed to happen, find the probability that its chance lies between two bounds. He solved it by treating the unknown chance as uniformly distributed before any trials, and Price noted that de Moivre had not solved this inverse question.[^s5] Bayesianism as a general theory of rational belief came much later, once probability had been axiomatized in the early twentieth century; Ramsey and de Finetti linked degrees of belief to betting prices and argued that incoherent beliefs expose an agent to a guaranteed loss (the "Dutch book" arguments).[^s1]

## How it works

The theorem can be read in an odds form that is easy to use: posterior odds equal prior odds multiplied by the likelihood ratio, the probability of the evidence if the hypothesis is true divided by its probability if the hypothesis is false.[^s3] Evidence supports a hypothesis when that ratio exceeds one, and the size of the ratio measures how strongly.[^s3] Two consequences follow. Surprising evidence that a hypothesis predicts confirms it strongly, and evidence that would be likely whether or not the hypothesis is true barely moves the needle.[^s1] And because the prior scales the result, the same piece of evidence can leave a rare hypothesis improbable; ignoring that prior is the error known as base-rate neglect.[^s3]

The argument map above shows a workplace case. About 1% of reviewed card transactions are fraudulent, a new alert rule catches 90% of fraud, and it falsely flags 9% of legitimate transactions. Out of 1,000 transactions, about 10 are fraud and 9 of those get flagged; of the 990 legitimate ones, about 89 get flagged. So only about 9 of roughly 98 flagged transactions, around 9%, are fraud. The flag raises the probability of fraud ninefold, yet fraud remains unlikely. Counting cases in one reference group like this is the natural-frequency route to the same Bayesian answer.[^s2][^s4]

## How to apply it

1. Name the hypothesis and its rival, and write down a prior: how often is the hypothesis true in a relevant reference class before this evidence?[^s3]
2. Estimate two likelihoods: how often you would see this evidence if the hypothesis were true, and how often if it were false. Their ratio tells you how diagnostic the evidence is.[^s3]
3. Combine them, either with the odds form or by imagining a concrete group of 100 or 1,000 cases and counting, which people find far easier than multiplying percentages.[^s2][^s4]
4. Update again as new, independent evidence arrives; the posterior from one step becomes the prior for the next.[^s1]
5. When two people disagree, check whether they differ on priors or on likelihoods; people who disagree about priors can often still agree on likelihoods, which localizes the dispute.[^s3]

## Evidence

As a normative standard, Bayesianism has well-known limits. The *problem of priors* asks where starting probabilities come from: objective Bayesians try to fix them with principles such as maximum entropy, while subjective Bayesians require only coherence.[^s1] Convergence theorems show that agents with different priors tend to agree after enough shared evidence, but only under conditions such as rough initial agreement, and convergence can be slow.[^s1] Glymour's *problem of old evidence* notes that evidence already known cannot raise a hypothesis's probability under conditionalization, even though discovering that a theory explains it seems to support the theory.[^s1] Critics add that full coherence demands unrealistic logical omniscience.[^s1]

As a description of human judgment, the record is poor. A 2023 review of the literature summarized correct-answer rates on textbook Bayesian problems as ranging from only about 4% to 24% of students.[^s4] It reported that McDowell and Jacobs's 2017 meta-analysis, covering 35 articles and 226 performance estimates, found an advantage for natural frequencies over probabilities, with visual aids also helping.[^s4] Weber, Binder and Krauss (2018) noted that even with natural frequencies about three quarters of participants in that meta-analysis still failed. In their study of 180 German university students, the format people actually calculated in mattered most: those who computed with frequencies got 53–61% correct, against 9–13% for those who computed with probabilities.[^s2]

## Connections

- **Introduced by Thomas Bayes.** His posthumous 1763 essay, communicated by Richard Price, posed and solved the inverse-probability problem the theorem now bears his name for.[^s5]
- **Applied in philosophy of science.** Bayesian confirmation theory explains why surprising predictions, varied evidence and favorable likelihood ratios confirm hypotheses.[^s1]
- **Challenged by the problem of old evidence.** Glymour's puzzle is one of the central objections to conditionalization as a full account of confirmation.[^s1]
- **Studied in cognitive psychology.** Experiments on Bayesian reasoning tasks measure how often people reach the normative answer and which formats help.[^s2]
- **Related to base-rate neglect.** Base-rate neglect is the characteristic failure of Bayesian reasoning: treating the likelihood of the evidence as if it were the posterior and ignoring the prior.[^s3]
- **Related to natural frequencies, inductive reasoning and inference to the best explanation.** Natural frequencies are a representation that makes Bayesian updating easier;[^s4] Bayesian accounts are a probabilistic theory of inductive support, and likelihood ratios give one way to weigh rival explanations.[^s1]

## Sources

[^s1]: Talbott, "Bayesian Epistemology", Stanford Encyclopedia of Philosophy, Summer 2006 archive edition. https://plato.stanford.edu/archives/Sum2006/entries/epistemology-bayesian/ (accessed 2026-11-08)
[^s2]: Weber, Binder & Krauss, "Why Can Only 24% Solve Bayesian Reasoning Problems in Natural Frequencies: Frequency Phobia in Spite of Probability Blindness", *Frontiers in Psychology* 9, 1833 (2018). https://www.frontiersin.org/articles/10.3389/fpsyg.2018.01833/pdf (accessed 2026-11-08)
[^s3]: Joyce, "Bayes' Theorem", Stanford Encyclopedia of Philosophy, Spring 2018 archive edition. https://plato.stanford.edu/archives/spr2018/entries/bayes-theorem/ (accessed 2026-11-08)
[^s4]: Cui, Lo & Liu, "The Use of Visualizations to Improve Bayesian Reasoning: A Literature Review", *Vision* 7 (2023). https://escholarship.org/content/qt5s9754p5/qt5s9754p5.pdf (accessed 2026-11-08)
[^s5]: Bayes, "An Essay towards solving a Problem in the Doctrine of Chances", *Philosophical Transactions of the Royal Society* 53 (1763), LaTeX edition, University of York. https://www.york.ac.uk/depts/maths/histstat/essay.htm (accessed 2026-11-08)
