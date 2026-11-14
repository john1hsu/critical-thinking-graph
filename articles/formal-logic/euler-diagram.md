---
id: ct:euler-diagram
type: Technique
title: Euler diagram
aliases: [Euler circles, Eulerian circles, Euler's circles]
domain: formal-logic
summary: >-
  A way of drawing categorical statements as closed curves whose spatial
  arrangement (one inside another, overlapping, or apart) shows how the classes
  relate, used to check immediate inferences and syllogisms by drawing every
  arrangement the premises allow and asking whether the conclusion holds in all
  of them.
level: introductory
evidenceStatus: normative
broader: [ct:diagrammatic-reasoning]
related: [ct:venn-diagram-test, ct:categorical-proposition, ct:conversion, ct:method-of-counterexample, ct:categorical-syllogism, ct:square-of-opposition]
requires: [ct:categorical-proposition]
relations:
  - {predicate: detects, object: ct:illicit-conversion, source: s3, confidence: high}
  - {predicate: introducedBy, object: ct:leonhard-euler, source: s1, confidence: high}
  - {predicate: introducedIn, object: ct:letters-to-a-german-princess, source: s2, confidence: high}
  - {predicate: influencedBy, object: ct:gottfried-wilhelm-leibniz, source: s5, confidence: medium}
  - {predicate: contrastsWith, object: ct:venn-diagram-test, source: s1, confidence: high}
  - {predicate: studiedIn, object: ct:psychology-of-reasoning, source: s3, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Diagrams"
    publisher: "Stanford Encyclopedia of Philosophy (Shin & Lemon, Fall 2005 archive)"
    url: https://plato.stanford.edu/archives/fall2005/entries/diagrams/
    type: scholarly-encyclopedia
    accessed: 2026-11-14
  - id: s2
    title: "From Logical Calculus to Logical Formality: What Kant Did with Euler's Circles"
    publisher: "Huaping Lu-Adler, in Kant and His German Contemporaries (Cambridge University Press, 2017), author's copy on PhilArchive"
    url: https://philarchive.org/archive/LUAFLC
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s3
    title: "A three-factor model of syllogistic reasoning: The study of isolable stages"
    publisher: "Donald L. Fisher, Memory & Cognition 9(5), 496-514 (1981)"
    url: https://link.springer.com/content/pdf/10.3758/BF03202344.pdf
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s4
    title: "How diagrams can support syllogistic reasoning: an experimental study"
    publisher: "Yuri Sato & Koji Mineshima, Journal of Logic, Language and Information 24(4), 409-455 (2015), University of Brighton research portal"
    url: https://research.brighton.ac.uk/en/publications/how-diagrams-can-support-syllogistic-reasoning-an-experimental-st/
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s5
    title: "Review of Deborah Bennett, 'Drawing logical conclusions' (Math Horizons, 2015), MR3313806"
    publisher: "Brendan Larvor, MathSciNet review, University of Hertfordshire Research Archive"
    url: https://uhra.herts.ac.uk/id/eprint/5195/1/AMS3313806.pdf
    type: academic
    accessed: 2026-11-14
  - id: s6
    title: "Leonhard Euler's letters to a German Princess"
    publisher: "MacTutor History of Mathematics, University of St Andrews"
    url: https://mathshistory.st-andrews.ac.uk/Extras/Euler_letters
    type: academic
    accessed: 2026-11-14
created: 2026-11-14
---

# Euler diagram

An Euler diagram represents each class in a categorical statement as a closed curve, usually a circle, and lets the arrangement of the curves carry the meaning. One circle wholly inside another shows "all A are B"; two circles that do not touch show "no A is B"; partial overlap is used for "some" statements.[^s1] Because it shows only arrangements that could actually hold, it works as a quick check on inferences between categorical statements: draw every arrangement the premises permit, and an inference is valid only if its conclusion is true in all of them.[^s1][^s3]

## Origin

Leonhard Euler used circles to explain syllogistic reasoning in his *Lettres à une Princesse d'Allemagne*, published in 1768.[^s1] The letters were written from 1760 to Princess Friederike Charlotte of the Prussian royal family, 234 letters in all; volumes one and two appeared in St Petersburg in 1768 and an English translation followed in 1795.[^s6] In Letters CII to CV Euler treats each general notion as an enclosed space holding all its objects, describes how a subject space can sit wholly inside, partly inside, partly outside or wholly outside a predicate space, and then uses the figures to test syllogisms and expose an invalid one.[^s2] Euler was not the first to draw such figures: an unpublished Leibniz fragment, printed in 1903, contains diagrams matching Euler's apart from the labels, and Bennett suggests the idea may have reached Euler through intermediaries such as the Bernoullis.[^s5] Kant later adapted Euler's circles in his own treatment of logic.[^s2]

## How it works

The key point is that a single categorical statement is often compatible with more than one picture. Fisher's 1981 analysis lists the possible relations: "All A are B" allows two (A identical to B, or A a proper subset of B); "No A are B" allows one (disjoint); "Some A are not B" allows three; and "Some A are B" allows up to four.[^s3] An inference is valid only if its conclusion holds in every picture the premise allows.

This is what makes the technique useful against illicit conversion. Suppose a manager reasons: "All of our certified suppliers passed the safety audit, so every supplier that passed is certified." Draw "certified" as a circle and "passed" as a circle. The premise allows two pictures: the circles coincide, or the certified circle sits inside a larger passed circle. The conclusion holds only in the first. The second picture, with passing suppliers outside the certified circle, is a counterexample, so the inference fails.[^s3] By contrast, "No certified supplier failed" allows only the disjoint picture, which reads the same in both directions, which is why E statements convert safely.[^s3]

## How to apply it

1. Rewrite each premise in standard categorical form (all, no, some, some ... not) and give each class its own circle.[^s1][^s2]
2. For each premise, list every arrangement it permits: equal or nested for "all", separate for "no", and so on, using Fisher's counts as a checklist.[^s3]
3. Combine the premises, keeping every combination that fits them all. Euler himself had to draw three cases for one of his syllogisms because no single figure captured both premises.[^s1]
4. Check the conclusion against every remaining picture. If one picture makes the premises true and the conclusion false, sketch it: it is your counterexample.[^s1][^s3]

The main pitfall is drawing only the most obvious picture. For "all A are B" people tend to draw two equal circles or one nested pair, and whichever they pick hides the other case.[^s3]

## Evidence and limitations

As a logical procedure the method is correct when every case is drawn; its weaknesses are practical. The Stanford Encyclopedia notes that a partial overlap is ambiguous, since the same figure can be read as "some A is B", "some B is A", "some A is not B" or "some B is not A", and Euler had to add a special mark for non-emptiness to patch this.[^s1] Some sets of statements cannot be combined in one figure, and circles can suggest intersections that the premises do not guarantee.[^s1] Venn's 1881 reform answered these problems by drawing every possible region first and shading the empty ones, which shows partial information that Euler's figures cannot.[^s1]

Empirically, people rarely enumerate all the cases. In Fisher's 1981 study of 18 participants, only one interpreted every premise logically, only seven gave all the logically possible pictures for "All A are B", and participants derived the right relations 48% of the time when five relations were possible against 76% when only one was.[^s3] Diagrams that do the enumeration for the reader seem to help: Sato and Mineshima (2015) built an Euler-style system that avoids the traditional ambiguities and found that it supported syllogistic reasoning, concluding that a diagram's benefit depends on how it encodes the relations in each sentence.[^s4]

## Connections

- **Detects illicit conversion.** Because "All A are B" allows a proper-subset picture in which "All B are A" is false, drawing both cases exposes the invalid swap; Fisher discusses conversion accounts of reasoning errors alongside these Euler relations.[^s3]
- **Introduced by Leonhard Euler in the *Letters to a German Princess*.** The circles first appear as a teaching device in the 1768 letters.[^s1][^s2][^s6]
- **Influenced by Leibniz.** Leibniz's earlier, unpublished diagrams were nearly identical, and Bennett suggests a route by which Euler may have learned of them.[^s5]
- **Contrasts with the Venn diagram test.** Euler shows the actual relations between classes; Venn shows all possible regions and marks what is known, which handles partial information better.[^s1]
- **Studied in the psychology of reasoning.** Researchers have used Euler relations to model how people interpret premises and where syllogistic errors come from.[^s3][^s4]

## Sources

[^s1]: Sun-Joo Shin and Oliver Lemon, "Diagrams", Stanford Encyclopedia of Philosophy (Fall 2005 archive). https://plato.stanford.edu/archives/fall2005/entries/diagrams/ (accessed 2026-11-14)
[^s2]: Huaping Lu-Adler, "From Logical Calculus to Logical Formality: What Kant Did with Euler's Circles", in C. Dyck and F. Wunderlich (eds.), *Kant and His German Contemporaries*, Cambridge University Press (2017), 35-55. https://philarchive.org/archive/LUAFLC (accessed 2026-11-14)
[^s3]: Donald L. Fisher, "A three-factor model of syllogistic reasoning: The study of isolable stages", *Memory & Cognition* 9(5), 496-514 (1981). https://link.springer.com/content/pdf/10.3758/BF03202344.pdf (accessed 2026-11-14)
[^s4]: Yuri Sato and Koji Mineshima, "How diagrams can support syllogistic reasoning: an experimental study", *Journal of Logic, Language and Information* 24(4), 409-455 (2015). https://research.brighton.ac.uk/en/publications/how-diagrams-can-support-syllogistic-reasoning-an-experimental-st/ (accessed 2026-11-14)
[^s5]: Brendan Larvor, review of Deborah Bennett, "Drawing logical conclusions", *Math Horizons* 22(3) (2015), MathSciNet MR3313806. https://uhra.herts.ac.uk/id/eprint/5195/1/AMS3313806.pdf (accessed 2026-11-14)
[^s6]: "Leonhard Euler's letters to a German Princess", MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Extras/Euler_letters (accessed 2026-11-14)
