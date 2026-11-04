---
id: ct:modus-tollens
type: ReasoningForm
title: Modus tollens
aliases: [denying the consequent, modus tollendo tollens, second indemonstrable]
domain: formal-logic
summary: >-
  The valid inference form "if P then Q; not Q; therefore not P", which
  concludes the denial of a conditional's antecedent from the conditional
  together with the denial of its consequent.
level: introductory
evidenceStatus: normative
broader: [ct:deductive-reasoning]
related: [ct:modus-ponens, ct:affirming-the-consequent, ct:falsifiability, ct:contraposition]
requires: [ct:validity]
relations:
  - {predicate: formalizedBy, object: ct:stoic-logic, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:denying-the-antecedent, source: s2, confidence: high}
  - {predicate: challengedBy, object: ct:a-counterexample-to-modus-tollens, source: s3, confidence: medium}
  - {predicate: studiedIn, object: ct:cognitive-psychology, source: s4, confidence: high}
argumentMap:
  premises:
    - "If the nightly backup job ran successfully, there is a backup file stamped with today's date."
    - "There is no backup file stamped with today's date."
  conclusion: "The nightly backup job did not run successfully."
  verdict: valid
  objections:
    - "The form is valid, but the conditional premise may be false: the job could have succeeded while writing to a different folder or stamping the file in another time zone."
sources:
  - id: s1
    title: "Ancient Logic"
    publisher: Stanford Encyclopedia of Philosophy (Bobzien, rev. 2020)
    url: https://plato.stanford.edu/entries/logic-ancient/
    type: scholarly-encyclopedia
    accessed: 2026-11-04
  - id: s2
    title: "Chapter Eleven: If-Then Arguments"
    publisher: "A Guide to Good Reasoning: Cultivating Intellectual Virtues (Wilson), University of Minnesota Libraries Publishing"
    url: https://open.lib.umn.edu/goodreasoning/chapter/if-then-arguments/
    type: textbook
    accessed: 2026-11-04
  - id: s3
    title: "A Counterexample to Modus Tollens"
    publisher: Journal of Philosophical Logic 41, 1001-1024 (Yalcin, 2012), author's copy
    url: https://static1.squarespace.com/static/551f03bce4b0bf9fbfefa27c/t/5aae05db8a922d6d3cc98e7f/1521354204788/yalcin+2012+counterexampleMT.pdf
    type: primary
    accessed: 2026-11-04
  - id: s4
    title: "Is inferential reasoning just probabilistic reasoning in disguise?"
    publisher: Memory & Cognition 33(7), 1315-1323 (Markovits & Handley, 2005)
    url: https://link.springer.com/content/pdf/10.3758/BF03193231.pdf
    type: peer-reviewed
    accessed: 2026-11-04
  - id: s5
    title: "Popper, Karl: Philosophy of Science"
    publisher: Internet Encyclopedia of Philosophy (Shea)
    url: https://iep.utm.edu/pop-sci/
    type: scholarly-encyclopedia
    accessed: 2026-11-04
created: 2026-11-04
---

# Modus tollens

Modus tollens is the inference form "If P then Q; not Q; therefore not P." The first premise is a conditional, the second denies its consequent, and the conclusion denies the antecedent, which is why textbooks also call it denying the consequent; the Latin name means roughly "the method of denying".[^s2] Every argument with this shape is deductively valid: if the if-clause would bring about the then-clause, and the then-clause did not happen, the if-clause cannot have been true.[^s2] It is the basic pattern of ruling something out by its missing consequences, and it underlies everyday troubleshooting, auditing and testing.

## Origin

The Stoic logicians of the Hellenistic period made this form the second of their five indemonstrables, the axiomatic arguments to which, together with four inference rules called *themata*, all other valid arguments were to be reduced.[^s1] They described it as concluding the contradictory of a conditional's antecedent from the conditional and the contradictory of its consequent, with examples such as: if it is day, it is not night; but it is night; so it is not day.[^s1] Modus ponens was the first indemonstrable, and the remaining three dealt with negated conjunctions and disjunctions.[^s1] Much of surviving Stoic logic goes back to Chrysippus, though the sources do not let us credit each piece to him individually.[^s1]

## How it works

The argument map above is a workplace case. If the nightly backup ran successfully, there would be a backup file stamped with today's date; there is no such file; so the backup did not run successfully. Accepting both premises commits you to the conclusion.[^s2] As with any valid form, the weak point is usually the conditional premise. If the job could succeed while writing elsewhere or stamping the file in another time zone, the conditional is false, and the argument is valid but unsound.

A useful check is that a conditional is equivalent to its contrapositive, "if not Q then not P", so every modus tollens argument can be rewritten as a modus ponens on the contrapositive.[^s2] That equivalence explains why both forms are valid and why the look-alikes are not.

## How to apply it

- **Find which part is denied.** If the second premise denies the consequent (Q), the form is modus tollens and valid; if it denies the antecedent (P), it is the fallacy of denying the antecedent.[^s2]
- **Check the conclusion.** A valid modus tollens concludes "not P"; an argument that concludes "not Q" from "not P" has gone wrong.[^s2]
- **Normalise the wording first.** Restate variants such as "P only if Q" as "if P then Q" before judging the form.[^s2]
- **Test the conditional.** Ask whether P could hold without producing Q; if so, the missing Q does not rule P out.

Modus tollens is also the logical shape of refutation in science. Popper's falsificationism rests on an asymmetry: no number of confirming cases proves a universal law, but one genuine counter-instance can refute it.[^s5] Critics drawing on the Duhem-Quine thesis note that a failed prediction usually follows from a theory plus auxiliary assumptions, so the denial of the consequent tells you only that at least one premise in the bundle is false.[^s5]

## Evidence and limitations

People find modus tollens markedly harder than modus ponens. In a 2005 study with 120 university students, Markovits and Handley found that 83 percent accepted the modus ponens conclusion as certain, but only 50 percent did so for modus tollens; the gap persisted when participants instead rated how probable the conclusion was (96 versus 72 percent).[^s4] Reasoning research therefore treats the form as a standard test of how people handle negation and conditional information.[^s4]

Philosophers have also questioned whether modus tollens holds for every English conditional. Seth Yalcin's 2012 paper describes an urn in which most big marbles are red but most marbles overall are blue: one can accept that if the marble is big it is likely red, and that it is not likely red, yet sensibly decline to conclude that it is not big.[^s3] Yalcin argues that the form fails for indicative conditionals whose consequents contain probability operators, while granting that it holds for plain cases and on the material, strict and Stalnaker-Lewis analyses of the conditional.[^s3] The dispute concerns the meaning of "if" plus "likely", not the validity of the form in classical propositional logic.

## Connections

- **Formalized by Stoic logic.** The Stoics made it the second indemonstrable, a primitive rule of their system.[^s1]
- **Contrasts with denying the antecedent.** The valid form denies the consequent and concludes against the antecedent; its invalid look-alike denies the antecedent and concludes against the consequent.[^s2]
- **Challenged by "A Counterexample to Modus Tollens".** Yalcin's 2012 paper argues the form fails for some probabilistic indicative conditionals.[^s3]
- **Studied in cognitive psychology.** Conditional-reasoning experiments use it alongside modus ponens and the two classic fallacies, and find it endorsed far less often than modus ponens.[^s4]
- **Related ideas.** Modus ponens is its companion valid form; affirming the consequent is the other common look-alike fallacy; and falsification in science follows the same refuting pattern.[^s2][^s5]

## Sources

[^s1]: Bobzien, "Ancient Logic", *Stanford Encyclopedia of Philosophy* (rev. 2020). https://plato.stanford.edu/entries/logic-ancient/ (accessed 2026-11-04)
[^s2]: Wilson, "If-Then Arguments", *A Guide to Good Reasoning: Cultivating Intellectual Virtues*, University of Minnesota Libraries Publishing. https://open.lib.umn.edu/goodreasoning/chapter/if-then-arguments/ (accessed 2026-11-04)
[^s3]: Yalcin, "A Counterexample to Modus Tollens", *Journal of Philosophical Logic* 41 (2012), 1001-1024. https://static1.squarespace.com/static/551f03bce4b0bf9fbfefa27c/t/5aae05db8a922d6d3cc98e7f/1521354204788/yalcin+2012+counterexampleMT.pdf (accessed 2026-11-04)
[^s4]: Markovits & Handley, "Is inferential reasoning just probabilistic reasoning in disguise?", *Memory & Cognition* 33(7), 2005, 1315-1323. https://link.springer.com/content/pdf/10.3758/BF03193231.pdf (accessed 2026-11-04)
[^s5]: Shea, "Popper, Karl: Philosophy of Science", *Internet Encyclopedia of Philosophy*. https://iep.utm.edu/pop-sci/ (accessed 2026-11-04)
