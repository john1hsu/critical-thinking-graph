---
id: ct:carroll-diagram
type: Technique
title: Carroll diagram
aliases: [Carroll's method of diagrams, Lewis Carroll's square diagram, biliteral and triliteral diagrams, Game of Logic diagram]
domain: formal-logic
summary: >-
  Lewis Carroll's square-diagram method for categorical reasoning: the whole
  universe is a square divided into cells for each combination of attributes
  and their negations, premises are recorded by marking cells as occupied or
  empty, and the only legitimate conclusion is whatever the marks transfer to
  the two-term diagram.
level: introductory
evidenceStatus: normative
broader: [ct:diagrammatic-reasoning, ct:categorical-syllogism]
related: [ct:venn-diagram-test, ct:euler-diagram, ct:existential-import, ct:rules-of-the-categorical-syllogism, ct:affirmative-conclusion-from-a-negative-premise, ct:syllogism]
requires: [ct:categorical-proposition, ct:validity]
relations:
  - {predicate: detects, object: ct:affirmative-conclusion-from-a-negative-premise, source: s3, confidence: medium}
  - {predicate: detects, object: ct:undistributed-middle, source: s3, confidence: high}
  - {predicate: introducedBy, object: ct:lewis-carroll, source: s4, confidence: high}
  - {predicate: introducedIn, object: ct:the-game-of-logic, source: s4, confidence: high}
  - {predicate: contrastsWith, object: ct:venn-diagram-test, source: s4, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Symbolic Logic, Part I: Elementary (1896), Project Gutenberg eBook #28696"
    publisher: "Lewis Carroll (C. L. Dodgson), Macmillan; Project Gutenberg edition"
    url: https://gutenberg.org/cache/epub/28696/pg28696-images.html
    type: primary
    accessed: 2026-11-14
  - id: s2
    title: "The Game of Logic (1886), Chapter 1, Part 2"
    publisher: "Lewis Carroll; Lit2Go edition, Florida Center for Instructional Technology, University of South Florida"
    url: https://etc.usf.edu/lit2go/136/the-game-of-logic/2513/chapter-1-part-2/
    type: primary
    accessed: 2026-11-14
  - id: s3
    title: "The Game of Logic (1886), Chapter 1, Part 3"
    publisher: "Lewis Carroll; Lit2Go edition, Florida Center for Instructional Technology, University of South Florida"
    url: https://etc.usf.edu/lit2go/136/the-game-of-logic/2514/chapter-1-part-3/
    type: primary
    accessed: 2026-11-14
  - id: s4
    title: "Diagrams and Diagrammatical Reasoning"
    publisher: Stanford Encyclopedia of Philosophy (Summer 2026 edition)
    url: https://plato.stanford.edu/archives/sum2026/entries/diagrams/
    type: scholarly-encyclopedia
    accessed: 2026-11-14
  - id: s5
    title: "A New Algorithmic Decision for Categorical Syllogisms via Carroll's Diagrams (Kircali Gursoy, Senturk, Oner & Gursoy)"
    publisher: arXiv:1802.04127
    url: https://arxiv.org/pdf/1802.04127
    type: preprint
    accessed: 2026-11-14
created: 2026-11-14
---

# Carroll diagram

A Carroll diagram is Lewis Carroll's way of drawing categorical statements and testing what follows from them. The universe of discourse is a square. Two attributes, say x and y, cut it into four cells (xy, xy′, x′y, x′y′), where a primed letter means "not" that attribute. A third, middle attribute is drawn as an inner square, giving eight cells.[^s1][^s5] Each cell is marked as occupied, marked as empty, or left blank when nothing is known. A syllogism is solved by recording both premises on the three-term diagram and then copying to the two-term diagram only what the marks force; whatever can be read there is the conclusion, and nothing else is.[^s1][^s2]

## Origin

Lewis Carroll (the pen name of C. L. Dodgson) presented the method in *The Game of Logic* (1886), a book meant for children and beginners, and developed it in *Symbolic Logic, Part I* (1896).[^s2][^s1] The Stanford Encyclopedia of Philosophy lists his square diagrams alongside Euler circles and Venn diagrams as the best-known diagrams for syllogistic reasoning and treats them as a variant of Venn's and Euler's proposals.[^s4] Its main novelty is that complements are regions of their own: "not-x" is a visible half of the square rather than the background outside a circle. This lets the diagram reason about negative classes directly, at the cost of drawing some classes as disconnected pieces.[^s4]

## How it works

In *The Game of Logic*, players place counters on a printed board. A grey counter means a cell is empty, and a red counter means it has at least one member. A red counter that could belong in either of two cells sits on the line between them.[^s2] *Symbolic Logic* keeps the counters for the two-term ("biliteral") diagram and uses the marks "O" and "I" on the three-term ("triliteral") one.[^s1] "No x are y" puts grey in the xy cell, and "Some x are y" puts red there. "All x are y" combines both: red in xy and grey in xy′. So for Carroll a universal affirmative also says that some x exist.[^s1] Carroll advises placing grey counters for negative premises first, because they can always be placed with certainty.[^s2]

The transfer rule is the core of the method. A quarter of the two-term diagram is marked occupied if either of its two three-term cells holds an "I". It is marked empty only if both of its cells hold an "O".[^s1] Everything else stays blank, which means the premises say nothing about it.

**Worked example.** "No contractors have admin access. Some contractors work the night shift. So some night-shift staff have admin access." Let x = night shift, y = admin access and m = contractor. The first premise is negative: it puts "O" in both contractor cells that have admin access. The second needs an "I" in the contractor/night-shift region. One of its two cells (with admin access) is already empty, so the "I" goes in the other (no admin access). Transferring, the night-shift/no-admin quarter is occupied, while the night-shift/admin quarter has only one "O" and stays blank. The diagram yields "Some night-shift staff lack admin access". The affirmative conclusion offered does not appear, so it is a fallacious conclusion.[^s1][^s3] The negative premise only emptied cells, which pushed the one occupied mark to the no-admin side. That is the pattern behind the traditional rule that a negative premise cannot support an affirmative conclusion.[^s2][^s3]

## How to apply it

1. Name the three attributes and choose which of x and y is the subject of the desired conclusion. Treat any "not-" as the primed half of an attribute, not as a separate term.[^s1]
2. Mark negative (empty) information first, then the "some" information. Place an "I" inside one cell only when the other cell is already empty; otherwise put it on the dividing line.[^s1][^s2]
3. Transfer to the two-term diagram using the two rules: one "I" makes a quarter occupied, two "O"s make it empty.[^s1]
4. Read off the conclusion and compare it with the one offered. Carroll calls a conclusion fallacious when it goes beyond the diagram. If the two-term diagram gets no marks, the premises are fallacious: nothing follows.[^s3] A proposed conclusion that is true but leaves out information is defective, not fallacious.[^s3]
5. Remember his reading of "all", which asserts that the subject class exists. Under that reading a conclusion like "Some x are y" can follow from universal premises, though the Boolean reading used in Venn's test would not allow it.[^s1][^s4]

## Evidence and limitations

As a logical procedure, the method is a standard of correctness, not an empirical claim. A 2018 preprint by Kircali Gursoy and colleagues encodes Carroll's marked two-term diagrams as numbers and builds a decision algorithm for categorical syllogisms on them.[^s5] Carroll himself pointed out a mismatch with traditional rules. Because his attributes may be negative, some premise pairs that the traditional rules dismiss (for example two negative premises) can still yield a conclusion about "not-" classes. He argued that the older rules were right only within their narrower system.[^s3] Like Venn's test, it covers only statements about classes.[^s4]

## Connections

- **Detects the affirmative conclusion from a negative premise.** Carroll's check compares a proposed conclusion with what the transfer actually yields. A negative premise contributes only empty cells, so an affirmative conclusion that relies on it is shown up as going beyond the diagram.[^s3]
- **Detects the undistributed middle.** Carroll's own example, which reasons from "all soldiers are brave" and "some Englishmen are brave" to "some Englishmen are soldiers", leaves the two-term diagram without information.[^s3]
- **Introduced by Lewis Carroll** in *The Game of Logic* (1886).[^s4][^s2]
- **Contrasts with the Venn diagram test.** Both mark empty and occupied regions, but Carroll draws complements as explicit regions inside a closed square.[^s4]
- **Related to existential import**, since Carroll's "All x are y" asserts that x exists.[^s1]

## Sources

[^s1]: Lewis Carroll, *Symbolic Logic, Part I: Elementary* (1896), Project Gutenberg eBook #28696. https://gutenberg.org/cache/epub/28696/pg28696-images.html (accessed 2026-11-14)
[^s2]: Lewis Carroll, *The Game of Logic* (1886), Chapter 1, Part 2, Lit2Go, University of South Florida. https://etc.usf.edu/lit2go/136/the-game-of-logic/2513/chapter-1-part-2/ (accessed 2026-11-14)
[^s3]: Lewis Carroll, *The Game of Logic* (1886), Chapter 1, Part 3, Lit2Go, University of South Florida. https://etc.usf.edu/lit2go/136/the-game-of-logic/2514/chapter-1-part-3/ (accessed 2026-11-14)
[^s4]: "Diagrams and Diagrammatical Reasoning", Stanford Encyclopedia of Philosophy (Summer 2026 edition). https://plato.stanford.edu/archives/sum2026/entries/diagrams/ (accessed 2026-11-14)
[^s5]: Kircali Gursoy, Senturk, Oner & Gursoy (2018), "A New Algorithmic Decision for Categorical Syllogisms via Carroll's Diagrams", arXiv:1802.04127 (preprint). https://arxiv.org/pdf/1802.04127 (accessed 2026-11-14)
