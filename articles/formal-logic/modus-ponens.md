---
id: ct:modus-ponens
type: ReasoningForm
title: Modus ponens
aliases: [affirming the antecedent, modus ponendo ponens, first indemonstrable]
domain: formal-logic
summary: >-
  The valid inference form "if P then Q; P; therefore Q", which concludes the
  consequent of a conditional from the conditional together with its
  antecedent.
level: introductory
evidenceStatus: normative
broader: [ct:deductive-reasoning]
related: [ct:modus-tollens, ct:affirming-the-consequent, ct:denying-the-antecedent, ct:suppression-effect]
requires: [ct:validity]
relations:
  - {predicate: formalizedBy, object: ct:stoic-logic, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:affirming-the-consequent, source: s3, confidence: high}
  - {predicate: challengedBy, object: ct:a-counterexample-to-modus-ponens, source: s4, confidence: medium}
  - {predicate: studiedIn, object: ct:cognitive-psychology, source: s5, confidence: high}
  - {predicate: introducedBy, object: ct:chrysippus, source: s6, confidence: medium}
argumentMap:
  premises:
    - "If a support ticket is marked urgent, it must get a first response within one hour."
    - "This support ticket is marked urgent."
  conclusion: "This support ticket must get a first response within one hour."
  verdict: valid
  objections:
    - "The form is valid, but the conclusion is only as good as the policy premise: if urgent tickets also require an on-call engineer to be reachable, the stated conditional is incomplete."
sources:
  - id: s1
    title: "Ancient Logic"
    publisher: Stanford Encyclopedia of Philosophy (Bobzien, rev. 2020)
    url: https://plato.stanford.edu/entries/logic-ancient/
    type: scholarly-encyclopedia
    accessed: 2026-11-03
  - id: s2
    title: "Stoic Logic (CLAS 196/PHIL 196: Stoicism course notes)"
    publisher: University of Vermont
    url: https://www.uvm.edu/%7Ejbailly/courses/196Stoicism/notes/StoicLogic.html
    type: academic
    accessed: 2026-11-03
  - id: s3
    title: "3.3: Conditional Arguments"
    publisher: "Critical Reasoning: A User's Manual (Southworth & Swoyer), LibreTexts"
    url: https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/Critical_Reasoning%3A_A_User's_Manual_(Southworth_and_Swoyer)/03%3A_Conditionals_and_Conditional_Arguments/3.03%3A_Conditional_Arguments
    type: textbook
    accessed: 2026-11-03
  - id: s4
    title: "A Counterexample to Modus Ponens"
    publisher: The Journal of Philosophy 82(9), 462-471 (McGee, 1985), course copy
    url: https://joelvelasco.net/teaching/4310/McGee-CounterexampleModusPonens-1985.pdf
    type: primary
    accessed: 2026-11-03
  - id: s5
    title: "How knowledge interferes with reasoning: Suppression effects by content and context"
    publisher: Proceedings of the 21st Annual Conference of the Cognitive Science Society, 468-473 (Neth & Beller, 1999), University of Göttingen copy
    url: https://www.psych.uni-goettingen.de/de/cognition/publikationen-dateien-neth-3/1999_nethbeller_how-knowledge-interferes-with-reasoning_suppression-effects-by-content-and-context.pdf
    type: peer-reviewed
    accessed: 2026-11-03
  - id: s6
    title: "Crísipo de Solos y los indemostrables (Chrysippus of Soli and the Indemonstrables)"
    publisher: Revista de Filosofía 74, 193-214, Universidad de Chile (Ramírez Figueroa, 2018)
    url: https://revistaschilenas.uchile.cl/handle/2250/15306?show=full
    type: peer-reviewed
    accessed: 2026-11-03
created: 2026-11-03
---

# Modus ponens

Modus ponens is the inference form "If P then Q; P; therefore Q." The first premise is a conditional, the second affirms its antecedent, and the conclusion is the consequent, which is why textbooks also call it affirming the antecedent.[^s3] Every argument with this shape is deductively valid: if both premises are true, the conclusion cannot be false, whatever P and Q are about.[^s3] It is the most basic way of putting a rule to work, and much everyday reasoning about policies, procedures and specifications has this structure.

## Origin

The form was treated as a basic, self-evident pattern by the Stoic logicians of the Hellenistic period. In Stoic syllogistic it is the first of five indemonstrables, the axiomatic arguments to which every other valid argument was to be reduced using four rules called *themata*.[^s1] The Stoics defined it as the argument that concludes the consequent from a conditional and its antecedent, and gave examples such as: if five is a number, five is odd or even; five is a number; so five is odd or even.[^s1] Their premises stood for whole propositions rather than terms, which is why Stoic logic is read as an early propositional logic, and they wrote schemata with ordinals: if the first, then the second; the first; therefore the second.[^s2] Much of this system is credited to Chrysippus, the most prolific Stoic logician, though the surviving sources do not let us attribute each piece to him.[^s1] Latin labels for the five patterns, such as *modus ponendo ponens*, are later conveniences rather than the Stoics' own terms.[^s2]

## How it works

The argument map above is a workplace case. A support policy says urgent tickets must get a first response within an hour; this ticket is urgent; so it must get a response within the hour. Validity comes from the form alone, so anyone who accepts both premises is committed to the conclusion.[^s3] Validity is not truth, though. If the policy premise is out of date or incomplete, the argument stays valid but stops being sound, and the right response is to challenge the premise, not the inference.[^s3]

The method of counterexample shows why the form is valid: try to describe a case where "if P then Q" and "P" are both true and Q is false. There is none, because such a case would make the conditional itself false.[^s3] The same test, applied to the look-alike that affirms the consequent instead ("if P then Q; Q; so P"), finds counterexamples easily, which is why that form is invalid.[^s3]

## Evidence and limitations

Modus ponens is the conditional inference people accept most readily. In a 1999 study by Neth and Beller, participants endorsed it about 93 percent of the time when given only the conditional and its antecedent.[^s5] Endorsement drops when a second conditional reminds people of an extra requirement: following Byrne's 1989 "suppression effect", adding a premise such as "if the museum is still open, she visits it" made participants less willing to draw the conclusion, and in Neth and Beller's experiment acceptance fell to about 64 percent.[^s5] They argue that background knowledge about sufficient and necessary conditions, carried by content and context, drives these shifts.[^s5] The lesson for practice is that people treat everyday conditionals as defeasible rules with unstated conditions, which is exactly where real arguments should be probed.

Philosophers have also asked whether modus ponens holds for every natural-language conditional. In 1985 Vann McGee offered apparent counterexamples involving conditionals whose consequent is itself a conditional. Using a three-candidate election where one candidate leads and a second candidate from the same party trails far behind, he argued that someone can reasonably believe both premises yet reasonably reject the conclusion.[^s4] McGee concluded that an adequate logic of English conditionals must restrict modus ponens for such nested cases; others have defended the form, and the debate concerns the meaning of "if", not the validity of the form for the material conditional of classical logic.[^s4][^s3]

## Connections

- **Formalized by Stoic logic.** The Stoics made it the first indemonstrable, a primitive rule of their deductive system.[^s1]
- **Contrasts with affirming the consequent.** The valid form affirms the antecedent; its invalid counterpart affirms the consequent and concludes the antecedent.[^s3]
- **Challenged by McGee's "A Counterexample to Modus Ponens".** McGee's 1985 paper argues that the form fails for some nested English conditionals.[^s4]
- **Studied in cognitive psychology.** Reasoning research uses it as the baseline conditional inference and studies how background knowledge suppresses it.[^s5]
- **Introduced by Chrysippus.** Specialist work on the Stoic indemonstrables credits Chrysippus's treatment of the five basic forms, of which this is the first, as the foundation of the Stoic system; many ancient reports name only "the Stoics", so the attribution is medium-confidence.[^s6]
- **Related forms.** Modus tollens, which denies the consequent, is the other valid conditional form; denying the antecedent is the invalid look-alike of modus tollens.[^s3]

## Sources

[^s1]: Bobzien, "Ancient Logic", *Stanford Encyclopedia of Philosophy* (rev. 2020). https://plato.stanford.edu/entries/logic-ancient/ (accessed 2026-11-03)
[^s2]: "Stoic Logic", CLAS 196/PHIL 196 Stoicism course notes, University of Vermont. https://www.uvm.edu/%7Ejbailly/courses/196Stoicism/notes/StoicLogic.html (accessed 2026-11-03)
[^s3]: Southworth & Swoyer, "Conditional Arguments", *Critical Reasoning: A User's Manual*, LibreTexts. https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/Critical_Reasoning%3A_A_User's_Manual_(Southworth_and_Swoyer)/03%3A_Conditionals_and_Conditional_Arguments/3.03%3A_Conditional_Arguments (accessed 2026-11-03)
[^s4]: McGee, "A Counterexample to Modus Ponens", *The Journal of Philosophy* 82(9), 1985, 462-471. https://joelvelasco.net/teaching/4310/McGee-CounterexampleModusPonens-1985.pdf (accessed 2026-11-03)
[^s5]: Neth & Beller, "How knowledge interferes with reasoning: Suppression effects by content and context", *Proceedings of the 21st Annual Conference of the Cognitive Science Society*, 1999. https://www.psych.uni-goettingen.de/de/cognition/publikationen-dateien-neth-3/1999_nethbeller_how-knowledge-interferes-with-reasoning_suppression-effects-by-content-and-context.pdf (accessed 2026-11-03)
[^s6]: Ramírez Figueroa, "Crísipo de Solos y los indemostrables", *Revista de Filosofía* 74 (2018), 193-214. https://revistaschilenas.uchile.cl/handle/2250/15306?show=full (accessed 2026-11-03)
