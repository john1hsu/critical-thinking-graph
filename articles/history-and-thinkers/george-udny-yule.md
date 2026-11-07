---
id: ct:george-udny-yule
type: Person
title: George Udny Yule
aliases: [G. Udny Yule, Udny Yule]
domain: history-and-thinkers
summary: >-
  British statistician (1871-1951) who worked with Karl Pearson, described in
  1903 the reversal of associations now called Simpson's paradox, and in 1926
  showed why trending time series so often produce high but meaningless
  "nonsense correlations".
level: intermediate
evidenceStatus: historical
broader: []
related: [ct:simpsons-paradox, ct:correlation-versus-causation, ct:confounding, ct:regression-to-the-mean, ct:spurious-correlation]
requires: []
relations:
  - {predicate: introduced, object: ct:simpsons-paradox, source: s2, confidence: medium}
  - {predicate: introduced, object: ct:nonsense-correlation, source: s3, confidence: high}
  - {predicate: introduced, object: ct:yules-q, source: s2, confidence: high}
  - {predicate: authored, object: ct:an-introduction-to-the-theory-of-statistics, source: s1, confidence: high}
  - {predicate: influencedBy, object: ct:karl-pearson, source: s1, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Yule, George Udny (1871-1951), statistician"
    publisher: Oxford Dictionary of National Biography (Yates, rev. Yoshioka, 2004), reproduced by MacTutor History of Mathematics, University of St Andrews
    url: https://mathshistory.st-andrews.ac.uk/DNB/Yule.html
    type: academic
    accessed: 2026-11-07
  - id: s2
    title: "Yule, George Udny"
    publisher: Encyclopedia of Mathematics (EMS / Springer; adapted from A. W. F. Edwards's StatProb article in Heyde & Seneta, Statisticians of the Centuries)
    url: https://encyclopediaofmath.org/wiki/Yule,_George_Udny
    type: scholarly-encyclopedia
    accessed: 2026-11-07
  - id: s3
    title: "Why do we Sometimes get Nonsense-Correlations between Time-Series? A Study in Sampling and the Nature of Time-Series"
    publisher: Journal of the Royal Statistical Society 89(1), 1-63 (Yule, 1926), copy hosted at gwern.net
    url: https://www.gwern.net/doc/statistics/causality/1926-yule.pdf
    type: primary
    accessed: 2026-11-07
  - id: s4
    title: "Correlations genuine and spurious in Pearson and Yule"
    publisher: Statistical Science 10(4), 364-376 (Aldrich, 1995), University of Southampton ePrints record
    url: https://eprints.soton.ac.uk/32919
    type: peer-reviewed
    accessed: 2026-11-07
created: 2026-11-07
---

# George Udny Yule

George Udny Yule (1871-1951) was a British statistician whose work sits underneath two warnings every careful reader of data needs: a pattern in pooled figures can reverse inside the groups that make it up, and two series that both drift over time can look tightly linked when they have nothing to do with each other.[^s2][^s3] Alongside Karl Pearson, he set the main ways statisticians have interpreted correlation for about a century, including where correlation-based conclusions break down.[^s4]

## Origin

Yule was born at Morham, near Haddington in East Lothian, studied engineering at University College London and physics at Bonn, and in 1893 became Pearson's demonstrator at UCL, rising to assistant professor of applied mathematics in 1896.[^s1] That post turned him to statistics. He later lectured on statistics at UCL and, from 1912, at Cambridge, where he became a fellow of St John's College.[^s1] He was president of the Royal Statistical Society from 1924 to 1926 and was elected a Fellow of the Royal Society in 1921.[^s1] His friendship with Pearson cooled after they disagreed, a break he later put down to Pearson's difficulty with colleagues who began to think for themselves.[^s1] One point of difference was how to measure association between yes/no attributes: around 1900 Yule proposed a coefficient based on the odds ratio of a 2x2 table, still called Yule's Q.[^s2]

His *An Introduction to the Theory of Statistics* (1911) grew out of evening lectures and became a standard textbook, reaching its fourteenth edition in 1950, the later ones revised with Maurice Kendall.[^s1][^s2] Late in life he applied statistics to disputed authorship in *The Statistical Study of Literary Vocabulary* (1944).[^s1]

## How it works

Two of Yule's results translate directly into everyday checks on reasoning with numbers.

**Reversal under aggregation (1903).** Working with three-way tables of attributes, Yule showed that the association between two attributes within each level of a third can differ from, and even run opposite to, the association in the combined table.[^s2] The pattern was named after E. H. Simpson only after Simpson's 1951 paper, which is why it is sometimes called the Yule-Simpson effect.[^s2] A workplace version: a support team's new triage script shows a higher overall escalation rate than the old one, yet a lower rate for both simple and complex tickets taken separately, because the new script was mostly used on the harder queue. The pooled comparison mixes the script's effect with the ticket mix.

**Nonsense correlations (1926).** In a 1926 paper in the *Journal of the Royal Statistical Society*, Yule correlated the proportion of Church of England marriages among all marriages with the standardized mortality rate for 1866-1911 and obtained +0.95, a figure the usual formula would treat as overwhelmingly significant.[^s3] He refused the standard excuse that "time" was a common cause, arguing instead that the textbook standard error assumes independent observations and is badly wrong for smooth, trending series.[^s3] Through sampling experiments he showed that short samples from such series pile up near correlations of +1 and -1: in one set, more than a third of sample correlations exceeded 0.9 in size.[^s3] A modern parallel is a dashboard showing that monthly cloud spend and headcount have moved together for two years. Two trending lines will usually correlate strongly; the figure says little until the trends are removed or the mechanism is shown.

## Legacy and limitations

Yule's 1927 analysis of sunspot numbers laid foundations for autoregressive models of time series, and the Yule-Walker equations still carry his name; he also introduced the Yule process, a simple birth process he devised in connection with evolution.[^s2] Historians credit him and Pearson jointly with the vocabulary of genuine and spurious correlation, and trace later work on the problem back to their debates, so the ideas were not his alone.[^s4] Priority for the reversal paradox is likewise shared: he described it in 1903, but the name went to Simpson.[^s2]

## Connections

- **Introduced** the reversal now called Simpson's paradox, describing it in 1903, decades before Simpson's paper gave it a name.[^s2]
- **Introduced** the idea and the name of nonsense correlations between time series, in his 1926 paper.[^s3]
- **Introduced** Yule's Q, an odds-ratio-based measure of association for 2x2 tables.[^s2]
- **Authored** *An Introduction to the Theory of Statistics* (1911), a standard text for decades.[^s1]
- **Influenced by** Karl Pearson, who hired him, launched his career in statistics and shared his long study of correlation.[^s1][^s4]
- **Related to** correlation versus causation, confounding and spurious correlation, the families of error his work helps readers detect, and to regression to the mean, another trap in reading correlated data.[^s3][^s4]

## Sources

[^s1]: F. Yates, rev. A. Yoshioka, "Yule, George Udny (1871-1951), statistician", *Oxford Dictionary of National Biography* (2004), via MacTutor, University of St Andrews. https://mathshistory.st-andrews.ac.uk/DNB/Yule.html (accessed 2026-11-07)
[^s2]: "Yule, George Udny", *Encyclopedia of Mathematics*, adapted from A. W. F. Edwards. https://encyclopediaofmath.org/wiki/Yule,_George_Udny (accessed 2026-11-07)
[^s3]: G. U. Yule, "Why do we Sometimes get Nonsense-Correlations between Time-Series?", *Journal of the Royal Statistical Society* 89(1) (1926), 1-63. https://www.gwern.net/doc/statistics/causality/1926-yule.pdf (accessed 2026-11-07)
[^s4]: J. Aldrich, "Correlations genuine and spurious in Pearson and Yule", *Statistical Science* 10(4) (1995), 364-376. https://eprints.soton.ac.uk/32919 (accessed 2026-11-07)
