---
id: ct:logical-consistency
type: Concept
title: Logical consistency
aliases: [consistency, consistent set of statements, joint possibility, inconsistency]
domain: foundations
summary: >-
  The property of a set of statements that could all be true together; a set is
  inconsistent when no possible situation makes every member true, so at least
  one of them must be false.
level: introductory
evidenceStatus: normative
broader: [ct:logic]
related: [ct:validity, ct:logical-consequence, ct:square-of-opposition, ct:principle-of-explosion, ct:aristotle, ct:antilogism, ct:tu-quoque, ct:vagueness]
requires: [ct:argument]
relations:
  - {predicate: studiedIn, object: ct:logic, source: s4, confidence: high}
  - {predicate: contrastsWith, object: ct:truth, source: s3, confidence: high}
  - {predicate: contrastsWith, object: ct:dialetheism, source: s5, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Contradiction"
    publisher: Stanford Encyclopedia of Philosophy (Laurence R. Horn, Summer 2026 edition)
    url: https://plato.stanford.edu/archives/sum2026/entries/contradiction/
    type: scholarly-encyclopedia
    accessed: 2026-11-15
  - id: s2
    title: "forall x, Chapter 3: Other logical notions"
    publisher: Open Logic Project
    url: https://forallx.openlogicproject.org/html/Ch3.html
    type: textbook
    accessed: 2026-11-15
  - id: s3
    title: "9.1: Recognizing Inconsistency and Contradiction, in Logical Reasoning"
    publisher: Bradley H. Dowden, Humanities LibreTexts
    url: https://human.libretexts.org/Bookshelves/Philosophy/Logical_Reasoning_(Dowden)/09%3A_Consistency_and_Inconsistency/9.01%3A_Recognizing_Inconsistency_and_Contradiction
    type: textbook
    accessed: 2026-11-15
  - id: s4
    title: "Logical relations, in Critical Thinking Web: Basic Logic"
    publisher: Joe Lau and Jonathan Chan, Department of Philosophy, University of Hong Kong
    url: https://philosophy.hku.hk/think/logic/relations.php
    type: academic
    accessed: 2026-11-15
  - id: s5
    title: "Dialetheism (Spring 2013 edition)"
    publisher: Stanford Encyclopedia of Philosophy (Graham Priest and Francesco Berto)
    url: https://plato.stanford.edu/archives/spr2013/entries/dialetheism
    type: scholarly-encyclopedia
    accessed: 2026-11-15
  - id: s6
    title: "Tutorial One: Consistency and Validity"
    publisher: University of Oxford philosophy logic tutorials (logic.philosophy.ox.ac.uk)
    url: https://logic.philosophy.ox.ac.uk/tutorial1/tut1-01.htm
    type: academic
    accessed: 2026-11-15
created: 2026-11-15
---

# Logical consistency

A set of statements is consistent when it is possible for all of them to be true at the same time, and inconsistent when no possible situation makes every one of them true.[^s3][^s4] Some textbooks call the same property *joint possibility*: the sentences are consistent if there is at least one case in which they all hold together.[^s2] Consistency is all-or-nothing. A set is either consistent or it is not, and there is no partial credit.[^s3] Spotting an inconsistency tells you something definite but limited: at least one member of the set is false, though logic alone does not say which.[^s3][^s4]

## Origin

The underlying norm is the law of non-contradiction. In *Metaphysics* Gamma, Aristotle held that the same thing cannot both belong and not belong to the same subject in the same respect, and he treated this as the firmest of all principles, too basic to be proved.[^s1] Later logicians generalised from a single statement and its denial to whole sets of statements. Modern introductory logic courses now define consistency for sets of beliefs or sentences, alongside validity, as one of the core logical notions.[^s2][^s6] Philosophers have not been unanimous. Dialetheists such as Graham Priest argue that a few contradictions are actually true, while still accepting non-contradiction as a general law.[^s5]

## How it works

Consistency concerns whether statements fit together, not whether they are true. Two false statements can be perfectly consistent with each other. Dowden's example is two people each claiming the same historical figure as their mother: both claims are false, but nothing stops them being true together.[^s3] Conversely, any two true statements are always consistent.[^s4]

Two kinds of conflict are worth separating. **Contradictories** are pairs where exactly one must be true, such as "the report is finished" and "the report is not finished." **Contraries** cannot both be true but can both be false, such as "the budget went to marketing" and "the budget went to engineering," when it may have gone to neither.[^s1][^s3] Both make a set inconsistent, but only contradictories tell you which way the truth must fall once one is settled.

Inconsistency often only appears when several statements are combined. Take a workplace example. A project lead's update says: (1) every task on the critical path is complete; (2) the database migration is on the critical path; (3) the database migration is still in progress. Any two of these could be true together, but all three cannot.[^s2][^s3] That is a common pattern. Each statement looks fine in isolation, and the trouble only shows when they are put side by side. A related lesson: adding more statements to an inconsistent set never makes it consistent, so irrelevant extra claims cannot rescue it.[^s2]

Consistency is closely tied to validity. An argument is valid when there is no case in which its premises are all true and its conclusion false.[^s2] Two consequences follow. First, an argument whose premises are themselves inconsistent is automatically valid, because there is no case in which all its premises are true.[^s2] Second, classical logic accepts the *principle of explosion*: a contradiction entails every statement whatsoever. That is why an inconsistent set of beliefs is so damaging in classical terms, and why paraconsistent logics are designed to block that inference.[^s1][^s5]

## How to apply it

1. **List the claims explicitly.** Write each statement on its own line, using its meaning as used in context, since words like "I", "now" or "here" can change reference.[^s6]
2. **Search for a single scenario that makes them all true.** If you can describe one, the set is consistent. If every attempt fails, find the smallest subset that cannot hold together.[^s2][^s3]
3. **Check whether the conflict is real.** Ordinary speakers use "contradictory," "contrary" and "inconsistent" loosely. Ask whether "everyone" really meant "almost everyone" before charging someone with inconsistency.[^s3]
4. **Treat an inconsistency as a prompt to investigate.** At least one statement must go. Gather evidence to decide which one, rather than discarding whichever is least convenient.[^s3]
5. **Don't confuse consistency with truth.** A consistent story can still be entirely false, so consistency is a necessary test, not a sufficient one.[^s3][^s4]

## Connections

- **Studied in logic.** Consistency, along with validity and entailment, is one of the basic logical relations that introductory logic studies.[^s4][^s6]
- **Contrasts with truth.** Consistency is about statements fitting together. Truth is about statements fitting the world, and a set can satisfy the first while failing the second.[^s3]
- **Contrasts with dialetheism.** Classical logic treats every contradiction as false. Dialetheism holds that some contradictions are true and relies on paraconsistent logic to avoid explosion.[^s5]
- **Related to validity and logical consequence.** An argument is valid exactly when no case makes its premises true and its conclusion false, and jointly impossible premises make any argument trivially valid.[^s2]
- **Related to the square of opposition.** The square's distinction between contradictories, contraries and subcontraries maps out the different ways two statements can conflict.[^s1]
- **Related to the principle of explosion.** In classical logic, explosion is the reason an inconsistent set of premises lets you derive anything at all.[^s1][^s5]

## Sources

[^s1]: Horn, "Contradiction", Stanford Encyclopedia of Philosophy, Summer 2026 edition. https://plato.stanford.edu/archives/sum2026/entries/contradiction/ (accessed 2026-11-15)
[^s2]: "Chapter 3: Other logical notions", *forall x*, Open Logic Project. https://forallx.openlogicproject.org/html/Ch3.html (accessed 2026-11-15)
[^s3]: Dowden, "9.1: Recognizing Inconsistency and Contradiction", *Logical Reasoning*, Humanities LibreTexts. https://human.libretexts.org/Bookshelves/Philosophy/Logical_Reasoning_(Dowden)/09%3A_Consistency_and_Inconsistency/9.01%3A_Recognizing_Inconsistency_and_Contradiction (accessed 2026-11-15)
[^s4]: Lau and Chan, "Logical relations", *Critical Thinking Web*, University of Hong Kong. https://philosophy.hku.hk/think/logic/relations.php (accessed 2026-11-15)
[^s5]: Priest and Berto, "Dialetheism", Stanford Encyclopedia of Philosophy, Spring 2013 edition. https://plato.stanford.edu/archives/spr2013/entries/dialetheism (accessed 2026-11-15)
[^s6]: "Tutorial One: Consistency and Validity", University of Oxford logic tutorials. https://logic.philosophy.ox.ac.uk/tutorial1/tut1-01.htm (accessed 2026-11-15)
