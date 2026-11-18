---
id: ct:karl-pearson
type: Person
title: Karl Pearson
aliases: [Carl Pearson, K. Pearson]
domain: history-and-thinkers
summary: >-
  English mathematician (1857-1936) and a founder of modern mathematical
  statistics. At University College London he developed correlation methods
  and the chi-squared test (1900), named contingency and the contingency
  table (1904), co-founded Biometrika, and argued in The Grammar of Science
  that science describes regularities rather than explaining causes. He was
  also a leading advocate of eugenics.
level: intermediate
evidenceStatus: historical
broader: []
related: [ct:contingency-table, ct:george-udny-yule, ct:correlation-versus-causation, ct:statistical-reasoning, ct:causal-inference, ct:philosophy-of-science]
requires: []
relations:
  - {predicate: introduced, object: ct:contingency-table, source: s2, confidence: medium}
  - {predicate: introduced, object: ct:chi-squared-test, source: s3, confidence: high}
  - {predicate: authored, object: ct:the-grammar-of-science, source: s5, confidence: high}
  - {predicate: influencedBy, object: ct:francis-galton, source: s1, confidence: high}
  - {predicate: challengedBy, object: ct:ronald-fisher, source: s3, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Karl Pearson"
    publisher: MacTutor History of Mathematics, University of St Andrews (J. J. O'Connor and E. F. Robertson, 2003)
    url: https://mathshistory.st-andrews.ac.uk/Biographies/Pearson/
    type: academic
    accessed: 2026-11-18
  - id: s2
    title: "Mathematical Contributions to the Theory of Evolution. XIII. On the Theory of Contingency and its Relation to Association and Normal Correlation"
    publisher: Drapers' Company Research Memoirs, Biometric Series I (Karl Pearson, Dulau and Co., 1904), scan on Internet Archive
    url: https://ia800207.us.archive.org/16/items/cu31924003064833/cu31924003064833.pdf
    type: primary
    accessed: 2026-11-18
  - id: s3
    title: "Karl Pearson's Theoretical Errors and the Advances They Inspired"
    publisher: Statistical Science 23(2), 261-271 (Stephen M. Stigler, 2008), author's copy on arXiv
    url: https://arxiv.org/pdf/0808.4032
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s4
    title: "Pearson's Wrong Turning: Against Statistical Measures of Causal Efficacy"
    publisher: Philosophy of Science 72(5), 900-912 (Robert Northcott, 2005), Cambridge University Press
    url: https://www.cambridge.org/core/journals/philosophy-of-science/article/abs/pearsons-wrong-turning-against-statistical-measures-of-causal-efficacy/F3878AA09495AFFDE6CBAA2347D9868B
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s5
    title: "Karl Pearson"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/print/article/448102
    type: encyclopedia
    accessed: 2026-11-18
  - id: s6
    title: "Karl Pearson: A Reader's Guide - Biographical sketch"
    publisher: University of Southampton
    url: https://blog.soton.ac.uk/karlpearson/biographical-sketch/
    type: academic
    accessed: 2026-11-18
created: 2026-11-18
---

# Karl Pearson

Karl Pearson (1857-1936) was an English mathematician who, more than anyone else around 1900, turned statistics into a discipline with its own methods, journal and laboratory.[^s5] Several tools a careful reasoner still uses to ask whether two things are really related, such as the correlation coefficient, the chi-squared test and the contingency table, took their modern shape in his department at University College London.[^s1][^s2] His legacy is mixed: some of his theory contained errors that others had to correct, and he was a committed advocate of eugenics.[^s3][^s5]

## Origin

Pearson was born in London on 27 March 1857, studied mathematics at King's College, Cambridge, graduating as Third Wrangler in 1879, then studied in Heidelberg and Berlin and qualified as a barrister without practising.[^s1] In 1884 he became professor of applied mathematics and mechanics at UCL.[^s6] His Gresham lectures of 1891-94 became *The Grammar of Science* (1892) and then turned to statistics.[^s6] Working with the zoologist W. F. R. Weldon, he set out to apply Francis Galton's statistical ideas, especially correlation, to evolution, a programme they called biometry.[^s6][^s1] In 1901 Pearson, Weldon and Galton founded *Biometrika*, often called the first journal of modern statistics, which Pearson edited until his death.[^s5][^s1] He became the first Galton Professor of Eugenics in 1911, heading a new Department of Applied Statistics, and retired in 1933.[^s1][^s6]

## How it works

Pearson's lasting contribution to critical thinking is a set of ways to put a number on "how far from chance is this pattern?"[^s2][^s3]

**The chi-squared test (1900).** Pearson's 1900 paper in the *Philosophical Magazine* gave a statistic for comparing observed counts with the counts a hypothesis predicts.[^s3] A help-desk lead who sees more tickets on Mondays can use it to ask whether the excess over an even spread is larger than random variation would usually produce.

**Contingency and the contingency table (1904).** In a 1904 memoir Pearson classified cases by two attributes into a grid of rows and columns, and called any measure of how far that classification departs from independence a measure of its contingency.[^s2] He proposed the mean square contingency, built from chi-squared, and a coefficient of contingency derived from it, and showed that these approach the correlation coefficient when the grouping is fine.[^s2] He described the "pure contingency table", whose categories have no natural order, using a table of fathers' and sons' occupations.[^s2] He presented contingency as a generalisation of G. U. Yule's coefficient of association for two-by-two tables, which he criticised because its value depends on where a continuous trait is cut in two.[^s2] The everyday lesson survives: before concluding that a new onboarding course reduces early resignations, lay out all four cells (course or not, stayed or left) and compare the rates, not just the striking cell.

**Description over cause.** In *The Grammar of Science* Pearson argued that scientific method describes rather than explains, and this positivist outlook made quantification attractive across biology, medicine and social science.[^s5] Philosopher Robert Northcott notes that Pearson designed measures of association deliberately to be acausal, and argues that later practice went wrong in using them as measures of how much one factor causes another.[^s4]

## Evidence and limitations

Pearson's theory had real flaws. Stephen Stigler's 2008 review identifies two: his 1898 probable-error formulas with L. N. G. Filon, valid only for normal data, and his claim in 1900 that estimating parameters from the data does not change the degrees of freedom of chi-squared, which gives a two-by-two table three degrees of freedom instead of one.[^s3] R. A. Fisher corrected the contingency-table case in 1922 and generalised it in 1924; Stigler argues that Pearson framed both problems clearly enough for Fisher to solve them.[^s3] Relations between the two men were poor from about 1917, and by the later 1920s Fisher had become the dominant figure in the field.[^s6][^s1] Pearson's combative disputes with Bateson, Fisher and former students also damaged his reputation.[^s5] He was also an outspoken advocate of eugenics, working with Galton and directing Galton's eugenics research office from 1906, so his statistical authority was put in the service of a programme that readers today should judge separately from his methods.[^s1][^s5]

## Connections

- **Introduced** the term and measure of contingency and the contingency table in his 1904 memoir, generalising Yule's two-by-two work.[^s2]
- **Introduced** the chi-squared test of goodness of fit (1900).[^s3]
- **Authored** *The Grammar of Science* (1892), his statement of descriptive, positivist science.[^s5]
- **Influenced by** Francis Galton, whose ideas on correlation and heredity he and Weldon developed.[^s6][^s1]
- **Challenged by** R. A. Fisher, who corrected his degrees-of-freedom error and his estimation methods.[^s3]
- **Related to** correlation versus causation and causal inference, because his association measures were built to be acausal.[^s4] G. U. Yule was his most important early collaborator.[^s6]

## Sources

[^s1]: J. J. O'Connor and E. F. Robertson, "Karl Pearson", MacTutor History of Mathematics, University of St Andrews (2003). https://mathshistory.st-andrews.ac.uk/Biographies/Pearson/ (accessed 2026-11-18)
[^s2]: K. Pearson, *On the Theory of Contingency and its Relation to Association and Normal Correlation*, Drapers' Company Research Memoirs, Biometric Series I (London: Dulau, 1904). https://ia800207.us.archive.org/16/items/cu31924003064833/cu31924003064833.pdf (accessed 2026-11-18)
[^s3]: S. M. Stigler, "Karl Pearson's Theoretical Errors and the Advances They Inspired", *Statistical Science* 23(2) (2008), 261-271. https://arxiv.org/pdf/0808.4032 (accessed 2026-11-18)
[^s4]: R. Northcott, "Pearson's Wrong Turning: Against Statistical Measures of Causal Efficacy", *Philosophy of Science* 72(5) (2005), 900-912. https://www.cambridge.org/core/journals/philosophy-of-science/article/abs/pearsons-wrong-turning-against-statistical-measures-of-causal-efficacy/F3878AA09495AFFDE6CBAA2347D9868B (accessed 2026-11-18)
[^s5]: "Karl Pearson", *Encyclopaedia Britannica*. https://www.britannica.com/print/article/448102 (accessed 2026-11-18)
[^s6]: "Karl Pearson: A Reader's Guide - Biographical sketch", University of Southampton. https://blog.soton.ac.uk/karlpearson/biographical-sketch/ (accessed 2026-11-18)
