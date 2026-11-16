---
id: ct:distributive-collective-distinction
type: Technique
title: Distributive-collective distinction
aliases: [distributive vs collective predication, distributive and collective senses of a term, collective-distributive test]
domain: argumentation
summary: >-
  An analytic check that asks whether a claim about a group applies to each
  member taken separately (distributive sense) or to the group taken as one
  unit (collective sense), used to expose arguments that slide from one sense
  to the other, as in the fallacies of composition and division.
level: introductory
evidenceStatus: normative
broader: [ct:argument-evaluation]
related: [ct:fallacy-of-composition, ct:fallacy-of-division, ct:equivocation, ct:ambiguity, ct:distribution-of-terms, ct:precising-definition, ct:predicate-logic, ct:richard-whately, ct:informal-logic]
requires: [ct:argument, ct:ambiguity]
relations:
  - {predicate: counteracts, object: ct:fallacy-of-composition, source: s5, confidence: high}
  - {predicate: counteracts, object: ct:fallacy-of-division, source: s5, confidence: high}
  - {predicate: detects, object: ct:equivocation, source: s4, confidence: medium}
  - {predicate: formalizedBy, object: ct:plural-logic, source: s2, confidence: medium}
  - {predicate: studiedIn, object: ct:argumentation-theory, source: s3, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Fallacies"
    publisher: Stanford Encyclopedia of Philosophy (Hansen, rev. 2024)
    url: https://plato.stanford.edu/ENTRIES/fallacies
    type: scholarly-encyclopedia
    accessed: 2026-11-16
  - id: s2
    title: "Plural Quantification"
    publisher: Stanford Encyclopedia of Philosophy (Linnebo)
    url: https://plato.stanford.edu/ENTRiES/plural-quant/
    type: scholarly-encyclopedia
    accessed: 2026-11-16
  - id: s3
    title: "ISSA Proceedings 2014 - Ubiquity, Ambiguity, and Metarationality: Searching for the Fallacy of Composition"
    publisher: Rozenberg Quarterly (Finocchiaro, ISSA 2014 conference paper)
    url: https://rozenbergquarterly.com/issa-proceedings-2014-ubiquity-ambiguity-and-metarationality-searching-for-the-fallacy-of-composition/
    type: academic
    accessed: 2026-11-16
  - id: s4
    title: "Fallacy: Verbal fallacies"
    publisher: Encyclopaedia Britannica (Rescher and Schagrin)
    url: https://britannica.com/topic/fallacy/Verbal-fallacies
    type: encyclopedia
    accessed: 2026-11-16
  - id: s5
    title: "Distributive Fallacy"
    publisher: Palomar College, philosophy course materials
    url: https://www.palomar.edu/users/bthompson/Distributive%20Fallacy.html
    type: academic
    accessed: 2026-11-16
created: 2026-11-16
---

# Distributive-collective distinction

The distributive-collective distinction separates two ways a term or claim can be about a group. Used distributively, it says something about each member taken one at a time ("cows eat grass": every cow does). Used collectively, it says something about the group as a single unit ("cows are important to Wisconsin's economy": no individual cow is).[^s5] Applying the distinction as a check means asking, for each group claim in an argument, which of the two senses is meant in each premise and in the conclusion. If the sense shifts between them, the argument trades on an ambiguity, and the two classic results are the fallacies of composition and division.[^s5][^s4]

## Origin

The idea is old, but its role as a diagnostic grew out of the traditional treatment of composition and division. Whately treated those fallacies as "semi-logical": mostly logical failures arising from an ambiguous middle term, but ones that can only be spotted with knowledge of what the terms mean and of the subject matter.[^s1] Copi's widely used *Introduction to Logic* later filed composition and division among the fallacies of ambiguity, next to equivocation and amphiboly.[^s1] His best-known illustration of the distributive-to-collective slide is the inference that, since a bus uses more fuel than a car, all buses together use more fuel than all cars together.[^s3] Rescher and Schagrin's Britannica account makes the same diagnosis explicit, treating both fallacies as a kind of equivocation in which the distributive and collective senses of a term are run together; their contrast is a crowd "filing through the turnstile" (each person) versus a crowd packed into one city block (the crowd as a whole).[^s4]

In formal logic and the semantics of plurals the same contrast appears as distributive versus collective (non-distributive) predicates. Linnebo's survey defines a predicate as distributive when it holds of some things just in case it holds of each of them, as with "is on the table", and gives "form a circle" as a predicate that fails this test; capturing such collective predicates requires an extended plural logic.[^s2]

## How it works

Take a workplace version of Copi's bus case. A finance analyst argues: "A senior engineer costs us more than a junior engineer, so our senior engineers cost us more than our junior engineers." The premise is distributive (one senior versus one junior); the conclusion is collective (the two groups' total payroll). If the company employs forty juniors and six seniors, the premise can be true while the conclusion is false. The argument looks valid only because the plural phrase quietly changed sense.[^s3][^s5]

The reverse slide runs from collective to distributive. "The audit team has decades of experience, so each auditor on it is highly experienced" moves from a fact about the team's combined experience to a claim about every member, though the total may come from two veterans and several new hires. This is division, the mirror image of composition.[^s5][^s4]

## How to apply it

1. **Mark every group term.** Underline plurals and group nouns ("the team", "our suppliers", "customers") in the premises and the conclusion.[^s5]
2. **Label each occurrence D or C.** Ask: is this true of each member individually, or only of the members taken together? The Palomar notes' cow example suggests a quick probe: if the claim would survive any single member dropping out, it is probably collective.[^s5]
3. **Compare the labels.** A D in the premises and a C in the conclusion signals possible composition; a C in the premises and a D in the conclusion signals possible division.[^s5]
4. **Check whether the property transfers anyway.** Some properties do carry over (if every part of a box is made of steel, the box is steel). Van Eemeren and Grootendorst proposed that transfer from parts to whole requires the property to be absolute rather than relative and the whole to be unstructured; Finocchiaro reads these as necessary, not sufficient, conditions.[^s3]
5. **Ask for direct evidence about the target level.** If the conclusion is about the group, look for evidence about the group itself rather than only its members.[^s1]

Pitfalls: a sense shift is a warning sign, not proof of error, since some distributive-to-collective inferences are sound. Finocchiaro argues that "fallacy of composition" bundles at least three different patterns (distributive-to-collective, part-to-whole and member-to-group) that are often confused, so the D/C check catches the first cleanly but needs the transfer question in step 4 for the others.[^s3] Kahane complained that textbook examples are often contrived, so practice on real arguments rather than toy ones.[^s3]

## Connections

- **Counteracts** the fallacy of composition, which moves from the distributive to the collective sense, from parts to whole.[^s5]
- **Counteracts** the fallacy of division, which moves from the collective to the distributive sense, from whole to parts.[^s5]
- **Detects** equivocation, since Rescher and Schagrin analyse both fallacies as equivocation between the two senses of a term.[^s4]
- **Formalized by** plural logic, whose extended languages add predicates that take plural arguments so that collective (non-distributive) predication can be expressed.[^s2]
- **Studied in** argumentation theory, where Finocchiaro's research programme on composition separates the distributive-collective reading from other part-whole patterns.[^s3]
- **Related** to the traditional notion of distribution of terms in syllogistic, to precising definitions that fix a term's sense, and to Whately's account of semi-logical fallacies.[^s1]

## Sources

[^s1]: H. Hansen, "Fallacies", Stanford Encyclopedia of Philosophy (rev. 2024). https://plato.stanford.edu/ENTRIES/fallacies (accessed 2026-11-16)
[^s2]: Ø. Linnebo, "Plural Quantification", Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/ENTRiES/plural-quant/ (accessed 2026-11-16)
[^s3]: M. A. Finocchiaro, "Ubiquity, Ambiguity, and Metarationality: Searching for the Fallacy of Composition", ISSA Proceedings 2014, Rozenberg Quarterly. https://rozenbergquarterly.com/issa-proceedings-2014-ubiquity-ambiguity-and-metarationality-searching-for-the-fallacy-of-composition/ (accessed 2026-11-16)
[^s4]: N. Rescher and M. L. Schagrin, "Fallacy: Verbal fallacies", Encyclopaedia Britannica. https://britannica.com/topic/fallacy/Verbal-fallacies (accessed 2026-11-16)
[^s5]: "Distributive Fallacy", Palomar College. https://www.palomar.edu/users/bthompson/Distributive%20Fallacy.html (accessed 2026-11-16)
