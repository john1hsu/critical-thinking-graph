---
id: ct:lemperts-modeling-relevance
type: Work
title: Lempert's Modeling Relevance
aliases: [Modeling Relevance, "Lempert (1977)", likelihood-ratio theory of relevance]
domain: history-and-thinkers
summary: >-
  Richard O. Lempert's 1977 Michigan Law Review article that used the odds
  form of Bayes' theorem to define legally relevant evidence as evidence whose
  likelihood ratio differs from one, and used regret matrices to model unfair
  prejudice. It is the usual starting point for treating the likelihood ratio
  as the measure of relevance and probative value at trial.
level: intermediate
evidenceStatus: historical
broader: []
related: [ct:likelihood-ratio, ct:bayesian-reasoning, ct:legal-reasoning, ct:burden-of-proof, ct:prosecutors-fallacy, ct:conditional-probability]
requires: [ct:bayesian-reasoning]
relations:
  - {predicate: introduces, object: ct:likelihood-ratio, source: s1, confidence: high}
  - {predicate: authoredBy, object: ct:richard-lempert, source: s2, confidence: high}
  - {predicate: influencedBy, object: ct:trial-by-mathematics, source: s2, confidence: medium}
  - {predicate: appliedIn, object: ct:legal-reasoning, source: s1, confidence: high}
  - {predicate: challengedBy, object: ct:bergman-moore-1991-mistrial-by-likelihood-ratio, source: s4, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Legal Probabilism"
    publisher: Stanford Encyclopedia of Philosophy (Marcello Di Bello, first published 2021)
    url: https://plato.stanford.edu/ENTRIES/legal-probabilism/
    type: scholarly-encyclopedia
    accessed: 2026-11-12
  - id: s2
    title: "Modeling Relevance"
    publisher: Michigan Law Review 75(5), 1021-1057 (Richard O. Lempert, 1977); University of Michigan Law School repository copy via CORE
    url: https://core.ac.uk/download/270045519.pdf
    type: primary
    accessed: 2026-11-12
  - id: s3
    title: "Trial by Mathematics: Precision and Ritual in the Legal Process"
    publisher: Harvard Law Review 84, 1329 (Laurence H. Tribe, 1971); copy hosted at the University of Edinburgh School of Mathematics
    url: https://webhomes.maths.ed.ac.uk/~v1ranick/dreyfus/tribe.pdf
    type: primary
    accessed: 2026-11-12
  - id: s4
    title: "Mistrial by Likelihood Ratio: Bayesian Analysis Meets the F-Word"
    publisher: Cardozo Law Review 13 (Paul Bergman & Albert J. Moore, UCLA School of Law, 1991); eScholarship
    url: https://escholarship.org/content/qt7fd990ks/qt7fd990ks.pdf
    type: academic
    accessed: 2026-11-12
created: 2026-11-12
---

# Lempert's Modeling Relevance

*Modeling Relevance* is a 1977 article by Richard O. Lempert of the University of Michigan Law School, published in the *Michigan Law Review*, that used two simple decision-theoretic tools, Bayes' theorem and regret matrices, to explain what the rules of evidence mean by "relevance" and when relevant evidence may still be kept from a jury.[^s2] Its central move, defining relevant evidence as evidence whose likelihood ratio is not equal to one, became the standard probabilistic account of relevance in evidence scholarship.[^s1]

## Origin

Lempert wrote in reply to Laurence Tribe's 1971 *Trial by Mathematics*, which had warned that numbers presented at trial can dazzle jurors, that laypeople cannot set a credible starting probability for Bayesian updating, and that hard statistics tend to crowd out softer, case-specific evidence.[^s3] Lempert largely conceded Tribe's practical point that formal mathematics in the jury room costs more than it yields, but argued that Tribe had ignored a different use: mathematical models as heuristic devices for understanding legal rules.[^s2] He took as his target the then-new Federal Rules of Evidence, whose Rule 401 defines relevant evidence as evidence that makes a fact of consequence more or less probable.[^s2][^s1] The Stanford Encyclopedia of Philosophy credits the article with establishing likelihood ratios as the common measure of relevance for trial evidence.[^s1]

## How it works

In the odds form of Bayes' theorem, new evidence multiplies the prior odds of guilt by a likelihood ratio: the probability of the evidence if the defendant is guilty, divided by its probability if not.[^s2] Lempert's illustration is blood type: if a stain matches the defendant's type and that type is twice as likely to turn up if he is guilty, the ratio is 2:1, and odds of 1:1 become 2:1.[^s2] A ratio of exactly one leaves the odds unchanged, so on this model the evidence is logically irrelevant; the further the ratio is from one, the more probative it is.[^s2][^s1]

A workplace analogue: an auditor asks whether a manager falsified an expense claim. A badge log showing the manager was in the building that evening is relevant only if that is more (or less) likely under "falsified" than under "not falsified"; if the manager is in the building most evenings anyway, the ratio is near one and, on Lempert's model, the log adds little.[^s2]

Lempert then used regret matrices, which weigh the costs of wrongful conviction against wrongful acquittal, to model unfair prejudice. Evidence such as a prior crime can shift how much jurors regret each kind of error, which in effect lowers the burden of proof even when the evidence itself is weak.[^s2] He argued that judges using their discretion to exclude evidence should be more reluctant to do so the further its likelihood ratio sits from one.[^s2] For multiple items of evidence, he noted that simple multiplication assumes the items are conditionally independent, that redundant evidence adds little, and that impeachment lowers a witness's likelihood ratio.[^s2] He did not propose that jurors compute these numbers, and he doubted they consciously update odds after each item.[^s2]

## Reception and limitations

The likelihood-ratio reading of relevance is now standard, but it has well-known critics.[^s1] Ronald Allen's "small town murder" case describes evidence that is equally probable under guilt and innocence, so its ratio is one, yet any trial judge would admit it; Michael Pardo has offered similar cases.[^s1] Defenders reply that a piece of evidence has no single likelihood ratio: it can still be relevant by bearing on a sub-hypothesis, which Bayesian networks can display.[^s1] A further problem is that the ratio depends on which competing hypotheses are compared, and ad hoc hypotheses chosen only to fit the evidence can drive any ratio to one.[^s1] Bergman and Moore argued in 1991 that likelihood ratios yield frequency-based assessments rather than the individualized judgments of believability that trials require.[^s4]

## Connections

- **Introduces the likelihood ratio framework** for legal relevance: the Stanford Encyclopedia names Lempert (1977) as the work after which likelihood ratios became the usual measure of relevance.[^s1]
- **Authored by Richard Lempert**, then at the University of Michigan Law School.[^s2]
- **Influenced by Tribe's *Trial by Mathematics***, the critique it answers while accepting much of it.[^s2][^s3]
- **Applied in legal reasoning**, where it underpins the probabilistic reading of Rule 401 and debates about probative value.[^s1]
- **Challenged by Bergman and Moore (1991)**, who rejected likelihood-ratio analysis of believability, and by the counterexamples of Allen and Pardo.[^s4][^s1]
- It **requires** a grasp of Bayesian reasoning, since its whole model runs on the odds form of Bayes' theorem and on conditional probabilities of the evidence under each hypothesis.[^s2] It relates to the **prosecutor's fallacy**, the misreading of a match probability as the probability of innocence that Tribe found in the *Collins* case.[^s3]

## Sources

[^s1]: Di Bello, "Legal Probabilism", Stanford Encyclopedia of Philosophy (2021). https://plato.stanford.edu/ENTRIES/legal-probabilism/ (accessed 2026-11-12)
[^s2]: Lempert, "Modeling Relevance", Michigan Law Review 75:1021-1057 (1977). https://core.ac.uk/download/270045519.pdf (accessed 2026-11-12)
[^s3]: Tribe, "Trial by Mathematics: Precision and Ritual in the Legal Process", Harvard Law Review 84:1329 (1971). https://webhomes.maths.ed.ac.uk/~v1ranick/dreyfus/tribe.pdf (accessed 2026-11-12)
[^s4]: Bergman & Moore, "Mistrial by Likelihood Ratio: Bayesian Analysis Meets the F-Word", Cardozo Law Review 13 (1991). https://escholarship.org/content/qt7fd990ks/qt7fd990ks.pdf (accessed 2026-11-12)
