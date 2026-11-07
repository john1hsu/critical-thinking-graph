---
id: ct:charles-hamblin
type: Person
title: Charles Hamblin
aliases: [C. L. Hamblin, Charles Leonard Hamblin, Hamblin]
domain: history-and-thinkers
summary: >-
  Australian philosopher and computer pioneer (1922-1985) whose book Fallacies
  (1970) attacked the textbook "standard treatment" of fallacies and proposed
  formal dialectic, rule-governed dialogue games with commitment stores, as the
  proper framework for studying them, helping launch modern informal logic and
  formal argumentation.
level: intermediate
evidenceStatus: historical
broader: []
related: [ct:informal-fallacy, ct:informal-logic, ct:argumentation-theory, ct:sophistical-refutations, ct:burden-of-proof, ct:pragma-dialectics, ct:karl-popper, ct:begging-the-question, ct:ad-hominem, ct:tu-quoque]
requires: [ct:informal-fallacy]
relations:
  - {predicate: authored, object: ct:hamblins-fallacies, source: s1, confidence: high}
  - {predicate: introduced, object: ct:formal-dialectic, source: s1, confidence: high}
  - {predicate: introduced, object: ct:standard-treatment-of-fallacies, source: s2, confidence: high}
  - {predicate: introduced, object: ct:commitment-store, source: s5, confidence: high}
  - {predicate: influencedBy, object: ct:ludwig-wittgenstein, source: s2, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Notes on C. L. Hamblin, Fallacies (graduate seminar study notes, after McBurney's intellectual biography)"
    publisher: McMaster University, Department of Philosophy (David Hitchcock's course pages)
    url: https://humanities.mcmaster.ca/~hitchckd/hamblin.htm
    type: academic
    accessed: 2026-11-07
  - id: s2
    title: "The Coherence of Hamblin's Fallacies"
    publisher: "Informal Logic 31(4), 305-317 (Johnson, 2011), full text via Distant Reader"
    url: https://distantreader.org/stacks/journals/il/il-3345.pdf
    type: peer-reviewed
    accessed: 2026-11-07
  - id: s3
    title: "Editors' Introduction: Special Issue on Charles Hamblin"
    publisher: "Informal Logic 31(4), i-iv (Walton and Johnson, 2011), full text via Distant Reader"
    url: https://distantreader.org/stacks/journals/il/il-3502.pdf
    type: peer-reviewed
    accessed: 2026-11-07
  - id: s4
    title: "Fallacies 1: Contemporary approaches"
    publisher: "Dictionnaire de l'argumentation 2021, ICAR laboratory, CNRS (Plantin)"
    url: https://icar.cnrs.fr/dicoplantin/?p=4960
    type: academic
    accessed: 2026-11-07
  - id: s5
    title: "A Framework for Deliberation Dialogues"
    publisher: "OSSA Conference Archive, OSSA 4, University of Windsor (Hitchcock, McBurney and Parsons, 2001)"
    url: https://core.ac.uk/download/72768372.pdf
    type: academic
    accessed: 2026-11-07
created: 2026-11-07
---

# Charles Hamblin

Charles Leonard Hamblin (1922-1985) was an Australian philosopher, logician and early computer scientist who spent his career at the University of New South Wales in Sydney.[^s1][^s3] In critical thinking he is remembered for one book, *Fallacies* (1970), which Walton and Johnson called the best book on the subject since Aristotle.[^s3] It argued that logic textbooks were teaching fallacies badly, and that fallacies are best understood as breaches of the rules of a regulated dialogue.[^s1][^s2]

## Origin

Hamblin studied mathematics, philosophy and physics at the University of Melbourne and served as a radar officer in the Royal Australian Air Force during the Second World War.[^s1] He then wrote a doctorate at the London School of Economics under Karl Popper, criticising Shannon's notion of information from the standpoint of meaning.[^s1] From 1955 until his death in 1985 he taught at the New South Wales University of Technology, later the University of New South Wales.[^s1][^s3]

His early work was in computing. In 1957 he devised reverse Polish notation, reversing Łukasiewicz's bracket-free notation so that machines could evaluate expressions without brackets or many separate memory stores, and he also designed the zero-address store and the GEORGE programming language.[^s1][^s3] In 1959 he proposed a formal measure of plausibility distinct from probability.[^s1] A book on imperatives appeared after his death, in 1987.[^s1]

## How it works

*Fallacies* has a deliberate plan that early readers often missed.[^s2] Its opening chapter attacks what Hamblin called the **standard treatment**: the fallacy chapters of mainstream logic textbooks, which he found dogmatic, tied to tradition and cut off from modern logic.[^s1][^s2] Those chapters recycled a few inherited lists, including Aristotle's, the Latin *ad* arguments and the syllogistic errors, and defined a fallacy as an argument that seems valid but is not.[^s4] Hamblin noted that "seems" quietly brings in psychology, which logicians had not examined.[^s4] Several chapters then trace the history of the subject in Western and Eastern thought and conclude that formal logic alone cannot give a general account of fallacy.[^s1][^s2]

His positive proposal was **formal dialectic**: precisely stated dialogue games in which two parties take turns making moves such as assertions, questions and challenges, under rules about which moves are allowed.[^s1][^s3] Each party has a **commitment store**, a public record of the propositions they have gone on record as accepting, which grows or shrinks as moves are made.[^s3][^s5] On this view, begging the question or asking a loaded "many questions" query is a move the rules of good dialogue forbid, not a flaw in an argument's logical form.[^s1] The book closes with a chapter on equivocation, which Johnson reads as an attempt to supply the dialectical test of meaning that any such theory needs.[^s2]

A workplace example shows the idea. In a design review, an engineer asserts that a library is secure. A colleague asks why, and the engineer replies that it is widely used. The engineer is now committed to "widely used libraries are secure", and the colleague can challenge that commitment or point to a recent flaw found in a popular library. Tracking who is committed to what makes it clear when someone shifts ground or simply assumes the point at issue.[^s1][^s3]

## Influence and limitations

Hamblin's critique helped start the revival of fallacy research. Plantin's survey places informal logic in his wake: John Woods and Douglas Walton went on to examine the logical and pragmatic conditions under which ordinary arguments succeed, and pragma-dialectics later defined fallacies as violations of the rules of a critical discussion, a view in the same rule-based, dialogical spirit.[^s4] His dialogue games then moved into computer science, where argumentation became a research paradigm in artificial intelligence and multi-agent systems; protocols for negotiation and deliberation between software agents still keep a public commitment store for each participant.[^s3][^s5]

The project was left incomplete. Johnson judges that Hamblin's dialectic rests on an underdeveloped theory of argument and doubts that its Wittgensteinian justification holds up.[^s2] Walton and Johnson add that separating commitment from belief has proved hard.[^s3]

## Connections

Hamblin **authored** *Fallacies* (1970), the book that set out his critique and proposal.[^s1] In it he named and attacked the **standard treatment of fallacies** and **introduced formal dialectic** as a discipline.[^s1][^s2] Later work on dialogue systems credits his book with the **commitment store** that each participant keeps.[^s5] Johnson traces his account of dialogue rules to **Wittgenstein's** influence.[^s2] He studied under **Karl Popper**, and his ideas fed directly into **informal logic**, **argumentation theory** and **pragma-dialectics**.[^s1][^s4]

## Sources

[^s1]: Notes on C. L. Hamblin, *Fallacies*, McMaster University Department of Philosophy (Hitchcock course pages, drawing on McBurney's intellectual biography). https://humanities.mcmaster.ca/~hitchckd/hamblin.htm (accessed 2026-11-07)
[^s2]: Johnson, "The Coherence of Hamblin's Fallacies", *Informal Logic* 31(4), 305-317, 2011. https://distantreader.org/stacks/journals/il/il-3345.pdf (accessed 2026-11-07)
[^s3]: Walton and Johnson, "Editors' Introduction: Special Issue on Charles Hamblin", *Informal Logic* 31(4), 2011. https://distantreader.org/stacks/journals/il/il-3502.pdf (accessed 2026-11-07)
[^s4]: Plantin, "Fallacies 1: Contemporary approaches", *Dictionnaire de l'argumentation* 2021, ICAR, CNRS. https://icar.cnrs.fr/dicoplantin/?p=4960 (accessed 2026-11-07)
[^s5]: Hitchcock, McBurney and Parsons, "A Framework for Deliberation Dialogues", OSSA 4, 2001. https://core.ac.uk/download/72768372.pdf (accessed 2026-11-07)
