---
id: ct:stoic-logic
type: Field
title: Stoic logic
aliases: [Stoic dialectic, Stoic propositional logic, Stoic hypothetical syllogistic]
domain: formal-logic
summary: >-
  The logic developed by the Stoic school of ancient Greece, above all by
  Chrysippus (3rd century BCE): a system of whole propositions joined by
  connectives such as "if", "or", "and" and "not", with five basic
  argument forms (the indemonstrables) and rules for reducing other arguments
  to them; it is the earliest substantial forerunner of modern propositional
  logic.
level: intermediate
evidenceStatus: historical
broader: [ct:formal-logic]
related: [ct:chrysippus, ct:propositional-logic, ct:modus-ponens, ct:modus-tollens, ct:disjunctive-syllogism, ct:hypothetical-syllogism, ct:material-conditional, ct:syllogism, ct:organon, ct:liar-paradox, ct:sorites-paradox, ct:validity]
requires: [ct:deductive-reasoning, ct:validity]
relations:
  - {predicate: introducedBy, object: ct:chrysippus, source: s4, confidence: medium}
  - {predicate: influencedBy, object: ct:diodorus-cronus, source: s4, confidence: high}
  - {predicate: contrastsWith, object: ct:categorical-syllogism, source: s2, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Stoicism: Inferential logic"
    publisher: Routledge Encyclopedia of Philosophy (Sedley, 1998)
    url: https://www.rep.routledge.com/articles/thematic/stoicism/v-1/sections/inferential-logic
    type: scholarly-encyclopedia
    accessed: 2026-11-09
  - id: s2
    title: "Logic (ch. 5), in The Cambridge History of Hellenistic Philosophy"
    publisher: Cambridge University Press (Barnes, Bobzien & Mignucci; eds. Algra, Barnes, Mansfeld & Schofield, 1999)
    url: https://cambridge.org/core/product/identifier/CBO9781139053617A013/type/BOOK_PART
    type: textbook
    accessed: 2026-11-09
  - id: s3
    title: "Stoic Propositional Logic: A New Reconstruction"
    publisher: McMaster University (Hitchcock, 2002)
    url: https://experts.mcmaster.ca/display/publication1933971
    type: academic
    accessed: 2026-11-09
  - id: s4
    title: "History of logic: The Megarians and the Stoics"
    publisher: Encyclopaedia Britannica
    url: https://britannica.com/topic/history-of-logic/The-Megarians-and-the-Stoics
    type: encyclopedia
    accessed: 2026-11-09
created: 2026-11-09
---

# Stoic logic

Stoic logic is the system of reasoning built by the Stoic school in Athens, whose leading logician was Chrysippus (c. 279-206 BCE).[^s4] Where Aristotle analysed the inside of simple propositions ("all A are B"), the Stoics took whole propositions as their units and studied the words that join them, such as "if", "or", "and" and "not".[^s4][^s1] That focus makes it the closest ancient relative of modern propositional logic, and it is the source of the classical names for forms like modus ponens and modus tollens.[^s4]

## Origin

The school was founded by Zeno of Citium (c. 336-265 BCE), but its logic grew out of the Megarian dialecticians, notably Diodorus Cronus and his pupil Philo, who had already argued over modality and over when an "if" statement is true.[^s4] Philo held that a conditional is true unless its antecedent is true and its consequent false, which is the modern material conditional; Diodorus required that this combination be impossible at any time.[^s4] Chrysippus then systematised the field, though none of his logical books survives and the system is reconstructed from later reports.[^s4][^s3] Ancient writers came to treat logic as two rival syllogistics: a "categorical" one tied to Aristotle's followers and a "hypothetical" one tied to the Stoics; each school claimed its own system covered all of formal logic.[^s2]

## How it works

The basic unit is the assertible (*axioma*), a sayable that is true or false; its truth can change over time, so "it is day" is true now and false tonight.[^s3][^s1] Negation applies to the whole assertible, not to a predicate.[^s1] Compound assertibles are built with connectives. Negation and conjunction behave truth-functionally, while the main Stoic disjunction is exclusive (exactly one disjunct true) and the conditional was given stricter, non-truth-functional readings.[^s4][^s3] Stoic logicians also seem to have been the first to define some connectives in terms of others.[^s4]

Arguments were written as schemata with ordinals standing for whole propositions. Chrysippus treated five as indemonstrable, needing no proof:[^s4][^s1]

1. If the first, then the second; the first; therefore the second.
2. If the first, then the second; not the second; therefore not the first.
3. Not both the first and the second; the first; therefore not the second.
4. Either the first or the second; the first; therefore not the second.
5. Either the first or the second; not the second; therefore the first.[^s4]

A workplace example of the fifth: "Either the release ships Friday or it slips to next sprint; it is not slipping; so it ships Friday." Longer arguments were shown valid by reducing them, with four rules called *themata*, to chains of these five.[^s1][^s3] Chrysippus tested validity with a demanding notion of "following": an argument is valid when the conclusion follows from the conjoined premises the way a consequent follows from its antecedent in a true conditional, and he counted a conditional true only when the denial of its consequent conflicts with its antecedent (a relation called *synartesis*, cohesion).[^s1]

## Evidence and limitations

Because the sources are fragmentary, scholars disagree on details; Hitchcock's 2002 reconstruction notes ten earlier competing reconstructions and argues the system is sound by Chrysippus's standard of validity but not complete, so the Stoic claim that every valid argument reduces to the five indemonstrables was probably false.[^s3][^s4] The strict test for conditionals also had costs: many everyday "if" claims, including empirical rules of thumb, had to be recast as negated conjunctions, which made some Stoics wary of inductive inference.[^s1] Puzzles such as the Liar and the Sorites pressed hard on the system, and Chrysippus's solution to the Liar is lost.[^s1]

## Connections

Stoic logic is a historical branch of formal logic and the main ancient precursor of propositional logic, with Philo's conditional anticipating the material conditional.[^s4] It is credited to Chrysippus as its systematiser and was shaped by Diodorus Cronus's debates over conditionals and possibility.[^s4] It contrasts with Aristotle's categorical syllogistic: late antiquity treated the two as rival systems of "hypothetical" and "categorical" syllogisms rather than complementary halves.[^s2] Its first, second and fifth indemonstrables are modus ponens, modus tollens and disjunctive syllogism; its validity test makes it a direct ancestor of the modern idea of validity.[^s4][^s1]

## Sources

[^s1]: Sedley, "Stoicism: Inferential logic", Routledge Encyclopedia of Philosophy (1998). https://www.rep.routledge.com/articles/thematic/stoicism/v-1/sections/inferential-logic (accessed 2026-11-09)
[^s2]: Barnes, Bobzien & Mignucci, "Logic", in Algra et al. (eds.), The Cambridge History of Hellenistic Philosophy, Cambridge University Press (1999), 77-176. https://cambridge.org/core/product/identifier/CBO9781139053617A013/type/BOOK_PART (accessed 2026-11-09)
[^s3]: Hitchcock, "Stoic Propositional Logic: A New Reconstruction", McMaster University (2002). https://experts.mcmaster.ca/display/publication1933971 (accessed 2026-11-09)
[^s4]: "History of logic: The Megarians and the Stoics", Encyclopaedia Britannica. https://britannica.com/topic/history-of-logic/The-Megarians-and-the-Stoics (accessed 2026-11-09)
