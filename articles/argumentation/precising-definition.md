---
id: ct:precising-definition
type: Technique
title: Precising definition
aliases: [precising definitions, sharpening a definition, fixing the sense of a key term]
domain: argumentation
summary: >-
  A definition that starts from a term's existing, accepted meaning and narrows
  it with an explicit criterion for a given context (for example, "lunchtime
  means noon to 1:30 p.m."), so that a vague or ambiguous word is used in one
  checkable sense throughout an argument, a rule or a dispute.
level: introductory
evidenceStatus: normative
broader: [ct:definition]
related: [ct:ambiguity, ct:vagueness, ct:equivocation, ct:fallacy-of-ambiguity, ct:amphiboly, ct:bright-line-rule, ct:principle-of-charity, ct:verbal-dispute]
requires: [ct:ambiguity, ct:argument]
relations:
  - {predicate: counteracts, object: ct:equivocation, source: s1, confidence: high}
  - {predicate: detects, object: ct:equivocation, source: s2, confidence: medium}
  - {predicate: instanceOf, object: ct:definition, source: s4, confidence: high}
  - {predicate: contrastsWith, object: ct:stipulative-definition, source: s5, confidence: high}
  - {predicate: appliedIn, object: ct:legal-reasoning, source: s1, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Logical Reasoning, ch. 3: Writing with the Appropriate Precision"
    publisher: Bradley H. Dowden, California State University Sacramento (open textbook, PDF)
    url: https://www.csus.edu/indiv/d/dowdenb/4/Logical-Reasoning.pdf
    type: textbook
    accessed: 2026-11-11
  - id: s2
    title: "New Dialectical Rules for Ambiguity"
    publisher: Informal Logic 20(3), 261-274 (Walton, 2000), journal PDF via Distant Reader
    url: https://distantreader.org/stacks/journals/il/il-2280.pdf
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s3
    title: "Definitions"
    publisher: Stanford Encyclopedia of Philosophy (Gupta & Mackereth, rev. 2023)
    url: https://plato.stanford.edu/entries/definitions/
    type: scholarly-encyclopedia
    accessed: 2026-11-11
  - id: s4
    title: "4.4: Definition and Meaning"
    publisher: "Introduction to Philosophy (Lumen Learning), text by Garth Kemerling, Humanities LibreTexts"
    url: https://human.libretexts.org/Courses/Lumen_Learning/Book%3A_Introduction_to_Philosophy-2_(Lumen)/04%3A_Module_2%3A_Logic/04.4%3A_Definition_and_Meaning
    type: textbook
    accessed: 2026-11-11
  - id: s5
    title: "2.6: Defining Terms: Types and Purposes of Definitions"
    publisher: "Critical Reasoning and Writing (Levin et al., Golden West College), Humanities LibreTexts"
    url: https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/Critical_Reasoning_and_Writing_(Levin_et_al.)/02%3A_Language_-_Meaning_and_Definition/2.06%3A_Defining_Terms-_Types_and_Purposes_of_Definitions
    type: textbook
    accessed: 2026-11-11
created: 2026-11-11
---

# Precising definition

A precising definition takes a word whose ordinary meaning is already established and makes that meaning more exact for a particular purpose, typically by adding an explicit cut-off or criterion. Logic textbooks illustrate it with everyday cases: "a nice car" fixed as one retailing above a stated price, "lunchtime" fixed as noon to 1:30 p.m., or "horsepower" fixed as a definite rate of work.[^s1] Unlike a stipulative definition, it does not invent a meaning or hand a new word an arbitrary one; unlike a lexical (dictionary) definition, it does not merely report how people already use the word. It sharpens an existing sense, as when "a small amount of salt" is fixed as less than half a teaspoon.[^s5] Because it must stay faithful to the accepted meaning while narrowing it, a precising definition is judged both on accuracy to usage and on whether its added limit suits the job.[^s4]

## Origin

The sorting of definitions by purpose (lexical, stipulative, precising, theoretical and persuasive) is a staple of twentieth-century introductory logic teaching rather than the discovery of one author; textbooks present it as a toolkit for clear communication and for settling disputes, and trace the underlying worry to John Locke's complaint that words without fixed meanings hamper knowledge.[^s4] Philosophical work on definition draws a related but distinct line: Rudolf Carnap's *explication* deliberately keeps some central uses of a vague concept and stipulates the rest, so that the result can be more exact than the everyday notion it replaces and is judged by how well it serves its purpose.[^s3] Law is a long-standing home of the practice: courts repeatedly refine vague statutory or constitutional language, such as what counts as an "unreasonable seizure", when a new case falls in a grey zone, reasoning from what the drafters likely intended and from the public interest.[^s1]

## How it works

Two different defects call for precision. An ambiguous word has a few distinct senses ("critical thinker" as a fault-finder or as a perceptive reasoner); a vague word has a continuum of borderline cases ("bald", "rich", "experienced").[^s1] Equivocation exploits either kind by letting the key word slide from one sense to another between premise and conclusion, so that each step looks acceptable but the inference only goes through if the two senses are treated as one.[^s1] A precising definition blocks the slide by fixing one sense up front and holding every occurrence of the word to it.

A workplace example. A hiring policy says analysts need "experience with the reporting database"; a manager argues that a candidate who sat through a one-hour vendor tutorial "has experience" and therefore qualifies. Writing a precising definition into the policy, say "at least six months building production reports in the database", makes the shift visible at once: under that definition the second premise is false, and under the looser sense the policy's purpose is not met. The argument cannot be accepted on both readings at once, which is exactly the test for equivocation: hold the key word to one sense and see whether the reasons still support the conclusion.[^s1]

In interpretation of someone else's text, the same move works as evidence. Walton's dialectical rules for ambiguity give weight to an explicit definition the author supplied earlier, presume that a term used twice in one text keeps the same meaning, and allow a critic to evaluate the argument separately under each candidate reading when the text supports more than one.[^s2]

## How to apply it

1. **Find the load-bearing term.** Look for a key word that appears in more than one premise or links a premise to the conclusion, and watch whether its sense changes partway through.[^s1]
2. **Start from accepted usage.** Write down the ordinary or technical sense the context calls for; a precising definition that departs from usage is really a stipulation and should be labelled as one.[^s4][^s5]
3. **Add the narrowing criterion.** State a threshold, list of conditions or measurement that settles the borderline cases relevant to the decision at hand, not every conceivable one.[^s1]
4. **Substitute and re-read.** Replace every occurrence of the term with the definition and check whether each premise is still true and the conclusion still follows. If it fails, either the argument equivocated or the definition was set at the wrong place.[^s1][^s2]
5. **Check for a merely verbal dispute.** When the parties agree once terms are fixed, the disagreement was verbal; when they still disagree, the clarification has exposed the real issue, which can now be argued directly.[^s4]

Pitfalls: a definition can be bent to persuade rather than clarify, and can be faulty by being too broad, too narrow, circular or inconsistent.[^s1] Some vagueness cannot be removed and is useful, since looser conclusions are easier to defend; precision should match what the decision needs.[^s1] The definition only settles a disagreement if both parties accept it, since agreeing on terms is what removes differences in usage.[^s4]

## Connections

- **Instance of** definition: textbooks distinguish precising definitions from lexical, stipulative, theoretical and persuasive ones.[^s4]
- **Contrasts with** stipulative definition, which assigns a meaning without being bound to existing usage, whereas a precising definition sharpens an accepted one.[^s5]
- **Counteracts** equivocation, by fixing one sense of the shifting term and holding every occurrence to it.[^s1]
- **Detects** equivocation: an explicit definition gives the critic a principled basis for deciding which sense a term carries, and for testing the argument under each candidate reading.[^s2]
- **Applied in** legal reasoning, where courts refine vague statutory and constitutional terms case by case.[^s1]
- **Related to** ambiguity and vagueness (the two defects it repairs), to Carnap-style explication (which likewise trades fidelity to everyday usage for purpose-fitted precision), to the bright-line rule (a sharp threshold on a vague scale), to verbal disputes (which agreed definitions dissolve), and to the principle of charity (prefer the reading that makes sense of the text before testing it).[^s1][^s2][^s3][^s4]

## Sources

[^s1]: Dowden, *Logical Reasoning*, ch. 3 "Writing with the Appropriate Precision" (sections on equivocation, vagueness and precising definitions), California State University Sacramento. https://www.csus.edu/indiv/d/dowdenb/4/Logical-Reasoning.pdf (accessed 2026-11-11)
[^s2]: Walton, "New Dialectical Rules for Ambiguity", Informal Logic 20(3), 261-274 (2000). https://distantreader.org/stacks/journals/il/il-2280.pdf (accessed 2026-11-11)
[^s3]: Gupta & Mackereth, "Definitions", Stanford Encyclopedia of Philosophy (rev. 2023). https://plato.stanford.edu/entries/definitions/ (accessed 2026-11-11)
[^s4]: Kemerling, "Definition and Meaning", in *Introduction to Philosophy* (Lumen Learning), Humanities LibreTexts. https://human.libretexts.org/Courses/Lumen_Learning/Book%3A_Introduction_to_Philosophy-2_(Lumen)/04%3A_Module_2%3A_Logic/04.4%3A_Definition_and_Meaning (accessed 2026-11-11)
[^s5]: Levin et al., "Defining Terms: Types and Purposes of Definitions", *Critical Reasoning and Writing*, Humanities LibreTexts. https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/Critical_Reasoning_and_Writing_(Levin_et_al.)/02%3A_Language_-_Meaning_and_Definition/2.06%3A_Defining_Terms-_Types_and_Purposes_of_Definitions (accessed 2026-11-11)
