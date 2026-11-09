---
id: ct:disjunctive-syllogism
type: ReasoningForm
title: Disjunctive syllogism
aliases: [modus tollendo ponens, fifth indemonstrable, argument by elimination of alternatives]
domain: formal-logic
summary: >-
  The valid inference form "P or Q; not P; therefore Q", which reaches one
  alternative of a disjunction by ruling out the other.
level: introductory
evidenceStatus: normative
broader: [ct:deductive-reasoning]
related: [ct:false-dilemma, ct:modus-ponens, ct:modus-tollens, ct:truth-table, ct:syllogism, ct:chrysippus, ct:principle-of-explosion]
requires: [ct:validity]
relations:
  - {predicate: formalizedBy, object: ct:stoic-logic, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:affirming-a-disjunct, source: s2, confidence: high}
  - {predicate: studiedIn, object: ct:propositional-logic, source: s2, confidence: high}
  - {predicate: challengedBy, object: ct:paraconsistent-logic, source: s4, confidence: high}
  - {predicate: challengedBy, object: ct:relevance-logic, source: s4, confidence: medium}
argumentMap:
  premises:
    - "The shared printer is failing because of the network connection or because of the print driver."
    - "Network diagnostics show the printer's connection is working."
  conclusion: "The printer is failing because of the print driver."
  verdict: valid
  objections:
    - "The form is valid, but the first premise may leave out live options such as a paper jam or a hardware fault, which would make the argument unsound."
    - "If the diagnostics are unreliable, the second premise is doubtful and the elimination does not go through."
sameAs: []
sources:
  - id: s1
    title: "Ancient Logic"
    publisher: Stanford Encyclopedia of Philosophy (Susanne Bobzien, Winter 2021 edition)
    url: https://plato.stanford.edu/archives/win2021/entries/logic-ancient/
    type: scholarly-encyclopedia
    accessed: 2026-11-09
  - id: s2
    title: "4.5: Common Forms of Arguments"
    publisher: "Critical Reasoning and Writing (Levin et al.), Humanities LibreTexts, CC BY-NC-SA"
    url: https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/Critical_Reasoning_and_Writing_(Levin_et_al.)/04%3A_Deductive_Arguments/4.05%3A_Commons_Forms_of_Arguments
    type: textbook
    accessed: 2026-11-09
  - id: s3
    title: "Paraconsistent Logic"
    publisher: Stanford Encyclopedia of Philosophy (Priest, Tanaka and Weber; rev. 2026)
    url: https://plato.stanford.edu/entries/logic-paraconsistent/
    type: scholarly-encyclopedia
    accessed: 2026-11-09
  - id: s4
    title: "Paraconsistent Logic"
    publisher: Internet Encyclopedia of Philosophy (Zach Weber)
    url: https://iep.utm.edu/para-log/
    type: scholarly-encyclopedia
    accessed: 2026-11-09
  - id: s5
    title: "Course notes: Stoic Logic (CLAS/PHIL 196, Stoicism)"
    publisher: University of Vermont
    url: https://www.uvm.edu/~jbailly/courses/196Stoicism/notes/StoicLogic.html
    type: academic
    accessed: 2026-11-09
created: 2026-11-09
---

# Disjunctive syllogism

Disjunctive syllogism is the inference "P or Q; not P; therefore Q". One premise offers two alternatives, a second premise rejects one of them, and the conclusion accepts the one that remains. The order of the premises does not matter, and either alternative may be the one that is ruled out.[^s2] It is the logical core of reasoning by elimination: narrowing a list of candidates until only one survives. In classical propositional logic it is valid, so if both premises are true the conclusion must be true as well.[^s2]

## Origin

The pattern was set out as a basic rule by the Stoics of the third century BCE. Their logic recognised five "indemonstrable" arguments, which needed no proof and served as the base to which other valid arguments were reduced. The fifth of them infers, from a disjunction and the contradictory of one disjunct, the other disjunct.[^s1] Susanne Bobzien credits Chrysippus with the main achievement of building Stoic propositional logic, while noting that later Stoics systematised parts of his work.[^s1] The Stoic "or" was exclusive: a disjunction counted as true when exactly one of its parts was true. That reading also licensed the fourth indemonstrable, "P or Q; P; therefore not Q".[^s1][^s5] The fifth pattern is also known by the later Latin label *modus tollendo ponens*, "the mode that affirms by denying", as course notes on Stoic logic still call it.[^s5]

## How it works

A truth table shows why the form is valid. Write the premises as P ∨ Q and ¬P. The only row on which both are true is the one where P is false and Q is true, and on that row the conclusion Q is true too. No row makes the premises true and the conclusion false.[^s2] This holds whether "or" is read inclusively (at least one) or exclusively (exactly one). That separates disjunctive syllogism from its look-alike "P or Q; P; therefore not Q", which fails for inclusive "or" because both alternatives might hold. A textbook example is someone who likes mustard or ketchup and likes mustard. That does not show they dislike ketchup.[^s2]

The argument map above gives a workplace case. An office manager reasons that the shared printer is failing because of either the network or the print driver. Diagnostics clear the network, so the manager concludes that the driver is at fault. The step from premises to conclusion is airtight.[^s2] The weak point, as the objections note, is usually the disjunction itself. If a paper jam or a hardware fault was also possible, the "either-or" premise is false and the conclusion is not guaranteed. Valid form only passes on whatever truth the premises have.

## How to apply it

Use the form deliberately whenever you troubleshoot, diagnose or narrow options.

1. **List the alternatives explicitly** and ask whether the list is complete. An incomplete list turns a valid elimination into a false dilemma.
2. **Rule an option out with evidence**, not by default. The conclusion is only as secure as the denial premise.
3. **Accept what remains**, and keep in mind that it is established only relative to the list you started with.
4. **Do not run the move backwards.** Confirming one option does not eliminate the other unless the options are known to be exclusive.[^s2]

## Evidence and limitations

Within classical logic the validity of disjunctive syllogism is a theorem, not an empirical claim.[^s2] It has nonetheless been the main target of logicians who reject the "principle of explosion", the classical result that a contradiction implies every statement. Zach Weber's Internet Encyclopedia entry sets out the standard derivation: from A, infer "A or B" (B can be anything); then from "not A", disjunctive syllogism yields B.[^s4] Anyone who wants to block explosion must therefore deny that disjunctive syllogism is valid in general. Paraconsistent logics do exactly that, and relevance logics, which follow the same route, need a separate conditional so that modus ponens survives.[^s4] The Stanford Encyclopedia notes that some fifteenth-century logicians already resisted explosion by rejecting this inference.[^s3] It also describes adaptive logics, which apply disjunctive syllogism only while no contradiction has turned up and withdraw the step if one does.[^s3] Weber stresses that classical reasoning, including this form, remains appropriate in consistent domains such as tax returns or murder mysteries. The dispute matters mainly for reasoning with inconsistent information, such as paradoxes or conflicting databases.[^s4]

## Connections

- **Formalized by Stoic logic.** The form is the fifth Stoic indemonstrable, one of the basic arguments of Stoic propositional logic.[^s1]
- **Contrasts with affirming a disjunct.** The valid form denies one alternative; the invalid look-alike affirms one and rejects the other, which fails under inclusive "or".[^s2]
- **Studied in propositional logic.** It is one of the standard argument forms of propositional logic, proved valid with a truth table.[^s2]
- **Challenged by paraconsistent logic and relevance logic.** Because the form is a step in the derivation of explosion, these logics deny that it is valid in general.[^s4] The Stanford entry adds that adaptive logics restore it only where no contradiction obtains.[^s3]
- **Related to false dilemma, modus ponens and modus tollens.** A false dilemma feeds this valid form a disjunction that leaves out real options. Modus ponens and modus tollens are the conditional counterparts among the Stoic indemonstrables, the first and second of the five.[^s1]

## Sources

[^s1]: Bobzien, "Ancient Logic", *Stanford Encyclopedia of Philosophy* (Winter 2021 edition), §§5.2, 5.4. https://plato.stanford.edu/archives/win2021/entries/logic-ancient/ (accessed 2026-11-09)
[^s2]: Levin et al., "4.5: Common Forms of Arguments", *Critical Reasoning and Writing*, Humanities LibreTexts. https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/Critical_Reasoning_and_Writing_(Levin_et_al.)/04%3A_Deductive_Arguments/4.05%3A_Commons_Forms_of_Arguments (accessed 2026-11-09)
[^s3]: Priest, Tanaka & Weber, "Paraconsistent Logic", *Stanford Encyclopedia of Philosophy* (rev. 2026), §§1.2, 3.4. https://plato.stanford.edu/entries/logic-paraconsistent/ (accessed 2026-11-09)
[^s4]: Weber, "Paraconsistent Logic", *Internet Encyclopedia of Philosophy*, §§2c, 3d. https://iep.utm.edu/para-log/ (accessed 2026-11-09)
[^s5]: "Stoic Logic", course notes for CLAS/PHIL 196 (Stoicism), University of Vermont. https://www.uvm.edu/~jbailly/courses/196Stoicism/notes/StoicLogic.html (accessed 2026-11-09)
