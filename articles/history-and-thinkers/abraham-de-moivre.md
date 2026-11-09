---
id: ct:abraham-de-moivre
type: Person
title: Abraham de Moivre
aliases: [Abraham De Moivre, Abraham Demoivre, De Moivre]
domain: history-and-thinkers
summary: >-
  French-born Huguenot mathematician (1667-1754) who worked in London and whose
  Doctrine of Chances (1718; 2nd ed. 1738; 3rd ed. 1756) gave the first
  textbook theory of probability, stating the rules for independent and
  dependent events that underlie conditional probability, and who first
  formulated the normal approximation to the binomial in 1733.
level: intermediate
evidenceStatus: historical
broader: []
related: [ct:christiaan-huygens, ct:conditional-probability, ct:bayesian-reasoning, ct:gamblers-fallacy, ct:andrey-kolmogorov, ct:thomas-bayes]
requires: []
relations:
  - {predicate: introduced, object: ct:conditional-probability, source: s3, confidence: medium}
  - {predicate: introduced, object: ct:statistical-independence, source: s5, confidence: high}
  - {predicate: introduced, object: ct:central-limit-theorem, source: s3, confidence: high}
  - {predicate: authored, object: ct:the-doctrine-of-chances, source: s2, confidence: high}
  - {predicate: influencedBy, object: ct:christiaan-huygens, source: s1, confidence: medium}
  - {predicate: studiedIn, object: ct:probability-theory, source: s1, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Abraham de Moivre (biography)"
    publisher: "MacTutor History of Mathematics Archive, University of St Andrews (J. J. O'Connor and E. F. Robertson)"
    url: https://mathshistory.st-andrews.ac.uk/Biographies/De_Moivre.html
    type: academic
    accessed: 2026-11-09
  - id: s2
    title: "Maty's Biography of Abraham De Moivre, Translated, Annotated and Augmented"
    publisher: "Statistical Science 22(1), 109-136 (David R. Bellhouse and Christian Genest, 2007), doi:10.1214/088342306000000268, arXiv author's copy"
    url: https://arxiv.org/pdf/0708.3965
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s3
    title: "The aftermath of Abraham de Moivre's Doctrine of Chances and Annuities on Lives in 18th-century Europe"
    publisher: "Ivo Schneider (Münchner Zentrum für Wissenschafts- und Technikgeschichte), ch. 14 of Historia de la Probabilidad y la Estadística (IV), pp. 231-240"
    url: https://core.ac.uk/download/189091293.pdf
    type: academic
    accessed: 2026-11-09
  - id: s4
    title: "A betting interpretation for probabilities and Dempster-Shafer degrees of belief"
    publisher: "Glenn Shafer, Rutgers working paper no. 31 (revised 2018), arXiv:1001.1653"
    url: https://arxiv.org/pdf/1001.1653
    type: preprint
    accessed: 2026-11-09
  - id: s5
    title: "History of statistics: 18th century"
    publisher: "Kees Verduin, Leiden University (course material)"
    url: https://web.universiteitleiden.nl/fsw/verduin/stathist/sh_18.htm
    type: academic
    accessed: 2026-11-09
created: 2026-11-09
---

# Abraham de Moivre

Abraham de Moivre (1667-1754) was a French-born mathematician who spent his working life in London and wrote *The Doctrine of Chances*, first published in English in 1718.[^s1] Historian Ivo Schneider describes the book's introduction as the first theory of probability, whose core concepts include conditional probability, dependent and independent events, expectation and the multiplication rule.[^s3] De Moivre also derived the normal approximation to the binomial distribution in 1733, the first formulation of what is now called the central limit theorem.[^s3][^s2] For critical thinkers he matters because he wrote down, in plain arithmetic, the rule that joins two uncertain events, which is the rule people most often get wrong.

## Origin

De Moivre was born in Vitry-le-François in Champagne and raised a Protestant. As a student of logic at Saumur he read Christiaan Huygens's treatise on games of chance.[^s1] After Louis XIV revoked the Edict of Nantes in 1685 he was confined in the priory of Saint-Martin in Paris, then left for England. Bellhouse and Genest note that the priory was a school for re-educating Protestant children, so "imprisoned" may overstate it, and they place him in London by 1686 or 1687.[^s2][^s1] He never obtained a university post. He lived by private tutoring and was known in the Huguenot coffee houses of St Martin's Lane, while being elected to the Royal Society in 1697 and trusted by Isaac Newton for decades.[^s2][^s1]

His probability work grew from a Latin paper, *De mensura sortis* (1711), into the 1718 *Doctrine of Chances*, dedicated to Newton, with enlarged editions in 1738 and 1756.[^s2][^s1] The 1733 normal approximation first circulated as a pamphlet printed for friends and was added to the later editions.[^s2][^s3] He also wrote *Annuities upon Lives* (1724), which applied probability to Halley's mortality data.[^s1]

## How it works

De Moivre's contribution to everyday reasoning is a pair of rules. For events that do not depend on each other, the probability that both happen is the product of their separate probabilities; Verduin's history of statistics traces this definition of independence to his 1711 paper and its probability form to the 1718 book.[^s5] For dependent events, he stated that the probability of both is the probability of the first multiplied by the probability the second will have once the first is taken as having happened.[^s4][^s3] Glenn Shafer's working paper credits him as the first to state this rule of compound probability, which modern notation writes as P(A and B) = P(A) × P(B | A). For de Moivre, unlike for modern axioms, the rule was a claim to be argued from betting prices, not a definition.[^s4]

A workplace case shows why the distinction matters. Suppose two servers each fail on 2% of days. If they are independent, both fail on about 0.04% of days. If they share a power supply, so that the second fails on half the days the first does, both fail on about 1% of days, roughly 25 times as often. Treating dependent risks as independent is exactly the mistake de Moivre's two rules separate, and it is why reviewers should ask what a second event looks like *given* the first.[^s5][^s4]

## Influence and limitations

The book shaped the field's vocabulary; most eighteenth-century English writers called the subject "the doctrine of chances".[^s3] Thomas Simpson reused its results, often without credit, and Lagrange and Laplace each apparently began a French translation that was never finished.[^s3] Schneider calls a direct influence on Thomas Bayes's essay only hypothetical, though he suggests de Moivre's remarks on the limit theorem may have motivated it.[^s3] Shafer observes that the twentieth century dropped de Moivre's way of grounding probability in gamblers' expectations; modern treatments instead define conditional probability as a ratio, which turns his rule into a trivial consequence.[^s4] Calling him the "introducer" of conditional probability is therefore a claim about the first explicit rule, not about the modern definition, and Huygens and others had already reasoned about expectations in games.[^s1][^s3]

## Connections

- **Introduced conditional probability** in the sense of first stating the compound-probability rule for dependent events in the *Doctrine of Chances*.[^s3][^s4]
- **Introduced statistical independence**, defined first in ratios (1711) and then as a product of probabilities (1718).[^s5]
- **Introduced the central limit theorem** through his 1733 normal approximation to the binomial.[^s3][^s2]
- **Authored *The Doctrine of Chances*,** the book Maty's biography and its annotators treat as his main work.[^s2]
- **Influenced by Christiaan Huygens,** whose treatise on games of chance he read as a student at Saumur.[^s1]
- **Studied in probability theory,** a subject that, in Todhunter's judgment, owed more to him than to anyone except Laplace.[^s1]
- **Related:** later axiomatic treatments made conditional probability a definition, Bayesian reasoning builds on the multiplication rule, and the gambler's fallacy is a misreading of independence.[^s4][^s5]

## Sources

[^s1]: O'Connor & Robertson, "Abraham de Moivre", *MacTutor History of Mathematics Archive*, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/De_Moivre.html (accessed 2026-11-09)
[^s2]: Bellhouse & Genest, "Maty's Biography of Abraham De Moivre, Translated, Annotated and Augmented", *Statistical Science* 22(1), 2007. https://arxiv.org/pdf/0708.3965 (accessed 2026-11-09)
[^s3]: Schneider, "The aftermath of Abraham de Moivre's Doctrine of Chances and Annuities on Lives in 18th-century Europe", *Historia de la Probabilidad y la Estadística (IV)*, pp. 231-240. https://core.ac.uk/download/189091293.pdf (accessed 2026-11-09)
[^s4]: Shafer, "A betting interpretation for probabilities and Dempster-Shafer degrees of belief", working paper (revised 2018). https://arxiv.org/pdf/1001.1653 (accessed 2026-11-09)
[^s5]: Verduin, "History of statistics: 18th century", Leiden University. https://web.universiteitleiden.nl/fsw/verduin/stathist/sh_18.htm (accessed 2026-11-09)
