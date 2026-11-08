---
id: ct:john-venn
type: Person
title: John Venn
aliases: [J. Venn]
domain: history-and-thinkers
summary: >-
  English logician and Cambridge don (1834-1923) who formalised the
  overlapping-circle diagrams that now bear his name, read universal
  propositions as making no claim that anything exists (so subalternation and
  weakened syllogisms fail), and was a founder of the frequency
  interpretation of probability in The Logic of Chance (1866).
level: intermediate
evidenceStatus: historical
broader: []
related: [ct:venn-diagram-test, ct:existential-fallacy, ct:existential-import, ct:square-of-opposition, ct:categorical-syllogism, ct:syllogism, ct:george-boole]
requires: []
relations:
  - {predicate: introduced, object: ct:existential-fallacy, source: s1, confidence: medium}
  - {predicate: introduced, object: ct:frequency-interpretation-of-probability, source: s2, confidence: high}
  - {predicate: authored, object: ct:the-logic-of-chance, source: s2, confidence: high}
  - {predicate: influencedBy, object: ct:george-boole, source: s1, confidence: high}
  - {predicate: influencedBy, object: ct:augustus-de-morgan, source: s5, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Modern Logic: The Boolean Period: Venn"
    publisher: "The Encyclopedia of Philosophy (P. L. Heath, 1967), via Encyclopedia.com"
    url: https://encyclopedia.com/humanities/encyclopedias-almanacs-transcripts-and-maps/modern-logic-boolean-period-venn
    type: scholarly-encyclopedia
    accessed: 2026-11-08
  - id: s2
    title: "Venn, John"
    publisher: "Complete Dictionary of Scientific Biography (T. A. A. Broadbent; Scribner's, 2008), reproduced by MacTutor History of Mathematics, University of St Andrews"
    url: https://mathshistory.st-andrews.ac.uk/DSB/Venn.pdf
    type: scholarly-encyclopedia
    accessed: 2026-11-08
  - id: s3
    title: "A Survey of Venn Diagrams"
    publisher: "The Electronic Journal of Combinatorics, Dynamic Survey DS5 (Ruskey & Weston, 2005 edition), John Venn page"
    url: https://www.combinatorics.org/files/Surveys/ds5/VennJohnEJC.html
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s4
    title: "On the diagrammatic and mechanical representation of propositions and reasonings"
    publisher: "Philosophical Magazine and Journal of Science, Series 5, 9(59) (Venn, July 1880), doi:10.1080/14786448008626877, Zenodo record"
    url: https://zenodo.org/record/1431145
    type: primary
    accessed: 2026-11-08
  - id: s5
    title: "John Venn (1834-1923)"
    publisher: "Philosophy and History of Science archives, Kyoto University (Soshichi Uchii, 2001)"
    url: https://bun.kyoto-u.ac.jp/archive/jp/philosophy_and_history_of_science/phs-archives/gallery/venn_note.html
    type: academic
    accessed: 2026-11-08
created: 2026-11-08
---

# John Venn

John Venn (1834-1923) was an English logician whose name is attached to the most familiar picture in elementary logic, the diagram of overlapping circles.[^s2][^s3] He mattered to critical thinking for three further reasons: he showed how to test syllogisms by shading regions instead of memorising rules, he argued that universal statements such as "all S are P" do not by themselves assert that any S exists, and he helped found the view that probability is a long-run relative frequency.[^s1][^s2][^s5]

## Origin

Venn was born in Hull on 4 August 1834, entered Gonville and Caius College, Cambridge, in 1853 and took a mathematics degree in 1857.[^s2] He was elected a fellow of his college and kept the fellowship until his death; after a short spell of parish work he returned to Cambridge as a lecturer in moral sciences and helped shape the moral sciences examinations.[^s2] Raised in an evangelical family and first drawn to theology, he turned to logic after reading Boole and De Morgan, in a Cambridge circle that included Henry Sidgwick.[^s5] He was elected a Fellow of the Royal Society in 1883, the year he left holy orders, though he remained a practising lay churchman.[^s2] In later life he compiled the Cambridge alumni register *Alumni Cantabrigienses* with his son.[^s2]

His main works were *The Logic of Chance* (1866), a short paper on diagrams in the *Philosophical Magazine* (July 1880), *Symbolic Logic* (1881) and *The Principles of Empirical Logic* (1889).[^s2][^s3][^s4]

## How it works

**Diagrams.** Venn did not invent the idea of drawing logical relations; diagrams of this kind are older, and the survey literature credits him because he surveyed and formalised their use and was the first to generalise them.[^s3] In his scheme each term is a closed curve, so two terms make four compartments and three terms make eight.[^s1][^s2] A universal premise is drawn by shading the compartments it says are empty; a particular premise puts a cross in a compartment it says is occupied; the conclusion is then read off the finished picture.[^s1] The name "Venn diagram" itself appeared later, in C. I. Lewis's *A Survey of Symbolic Logic* (1918).[^s3]

**Existential reading.** Traditional logic tacitly assumed its terms had members. Venn found it clearer to say what a universal proposition denies than what it asserts, so he wrote "all S are P" as the claim that the class of S-that-are-not-P is empty, which can be true even if there are no S at all; only particular propositions assert that something exists.[^s1][^s5] Heath notes that this notation improved on Boole's and is now widely used, and that it has a cost Hugh MacColl also saw: subalternation (from "all S are P" to "some S are P") fails, and syllogisms with a weakened particular conclusion must be rejected.[^s1] That is the inference introductory texts now flag as the existential fallacy. A workplace version: a policy says every contractor with admin access must pass a security review. Under Venn's reading the policy is true even if no contractor has admin access, so it cannot be used to show that some contractor has been reviewed.

**Frequency probability.** In *The Logic of Chance* Venn defined the probability of an outcome as the limit of its relative frequency as the number of trials grows without bound.[^s2] Uchii counts him among the founders of the frequency theory, while noting that later editions moved somewhat towards degree-of-belief ideas.[^s5]

## Legacy and limitations

Heath's assessment is that Venn's value lay in clarifying and fairly weighing Boole's methods rather than in many original departures; Venn himself treated the choice between rival logical notations as partly a matter of convention.[^s1] His frequency definition assumed that a unique limiting frequency exists without proving it, a gap Richard von Mises later tried to close with explicit postulates.[^s2] The circle method also becomes unwieldy beyond three or four terms, which is why other diagram schemes are preferred for larger problems.[^s1] And the attribution of "his" diagrams is a convenient label for a tradition he systematised, not proof that he was first.[^s3]

## Connections

- **Introduced** the existential reading of universal propositions on which subalternation and weakened syllogisms are invalid, the basis of the existential fallacy as taught today; he did not coin that name.[^s1]
- **Introduced** a frequency definition of probability, as one of the founders of the frequency interpretation.[^s2][^s5]
- **Authored** *The Logic of Chance* (1866).[^s2]
- **Influenced by** George Boole, whose algebra his diagrams and *Symbolic Logic* set out to interpret and correct, and by Augustus De Morgan.[^s1][^s2][^s5]
- **Related to** the Venn diagram test for syllogisms, which the graph already attributes to him, and to existential import, the square of opposition and the categorical syllogism.[^s1][^s4]

## Sources

[^s1]: P. L. Heath, "Modern Logic: The Boolean Period: Venn", *The Encyclopedia of Philosophy* (1967), via Encyclopedia.com. https://encyclopedia.com/humanities/encyclopedias-almanacs-transcripts-and-maps/modern-logic-boolean-period-venn (accessed 2026-11-08)
[^s2]: T. A. A. Broadbent, "Venn, John", *Complete Dictionary of Scientific Biography* (2008), via MacTutor, University of St Andrews. https://mathshistory.st-andrews.ac.uk/DSB/Venn.pdf (accessed 2026-11-08)
[^s3]: F. Ruskey and M. Weston, "A Survey of Venn Diagrams", *Electronic Journal of Combinatorics*, Dynamic Survey DS5, John Venn page. https://www.combinatorics.org/files/Surveys/ds5/VennJohnEJC.html (accessed 2026-11-08)
[^s4]: J. Venn, "On the diagrammatic and mechanical representation of propositions and reasonings", *Philosophical Magazine*, Series 5, 9(59) (1880), Zenodo record. https://zenodo.org/record/1431145 (accessed 2026-11-08)
[^s5]: S. Uchii, "John Venn (1834-1923)", Philosophy and History of Science archives, Kyoto University (2001). https://bun.kyoto-u.ac.jp/archive/jp/philosophy_and_history_of_science/phs-archives/gallery/venn_note.html (accessed 2026-11-08)
