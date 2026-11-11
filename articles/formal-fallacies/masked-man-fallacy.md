---
id: ct:masked-man-fallacy
type: FormalFallacy
title: Masked-man fallacy
aliases: [illicit substitution of identicals, veiled man fallacy, hooded man fallacy]
domain: formal-fallacies
summary: >-
  The invalid inference that swaps one name or description for another that
  picks out the same thing inside a belief, knowledge or other intensional
  context ("a is b; someone believes Fa; so they believe Fb"), or that
  concludes two things are distinct because someone thinks of them
  differently.
level: intermediate
evidenceStatus: normative
broader: [ct:formal-fallacy]
related: [ct:equivocation, ct:ambiguity, ct:gottlob-frege, ct:willard-van-orman-quine, ct:quantifier-shift-fallacy, ct:method-of-counterexample, ct:liar-paradox]
requires: [ct:validity, ct:predicate-logic]
relations:
  - {predicate: invalidFormOf, object: ct:substitution-of-identicals, source: s1, confidence: high}
  - {predicate: explainedBy, object: ct:referential-opacity, source: s3, confidence: high}
  - {predicate: explainedBy, object: ct:sense-and-reference, source: s2, confidence: high}
  - {predicate: introducedBy, object: ct:eubulides, source: s5, confidence: medium}
criticalQuestions:
  - Does the conclusion swap a name or description inside "believes", "knows", "wants" or a similar verb?
  - Does the person whose attitude is reported know that the two names refer to the same thing?
  - Could the report be read as being about the thing itself (de re) rather than about how the person thinks of it?
  - Is "they know a but not b" being used to prove that a and b are different things?
argumentMap:
  premises:
    - "The anonymous reviewer of our grant proposal is the head of the research office."
    - "The project lead believes the anonymous reviewer was unfair to us."
  conclusion: "The project lead believes the head of the research office was unfair to us."
  verdict: invalid
  scheme: ct:substitution-of-identicals
  objections:
    - "The project lead does not know who the reviewer is, so their belief is about 'the reviewer', not about the head of the office."
    - "The lead may sincerely say the head of the research office has always treated the team fairly; both reports can be true at once."
sources:
  - id: s1
    title: "The Masked Man Fallacy"
    publisher: The Fallacy Files (Gary N. Curtis)
    url: https://fallacyfiles.org/illisubs.html
    type: community
    accessed: 2026-11-11
  - id: s2
    title: "Frege's Problem: Referential Opacity"
    publisher: Internet Encyclopedia of Philosophy (Graeme Forbes)
    url: https://iep.utm.edu/referential-opacity/
    type: scholarly-encyclopedia
    accessed: 2026-11-11
  - id: s3
    title: "Quantifiers and Propositional Attitudes"
    publisher: "The Journal of Philosophy 53(5), 177-187 (W. V. Quine, 1956), author's text via University of Vermont course page"
    url: https://www.uvm.edu/~lderosse/courses/lang/Quine(1956).pdf
    type: primary
    accessed: 2026-11-11
  - id: s4
    title: "The De Re/De Dicto Distinction (supplement to Propositional Attitude Reports)"
    publisher: Stanford Encyclopedia of Philosophy (Michael Nelson)
    url: https://plato.stanford.edu/ENTRIES/prop-attitude-reports/dere.html
    type: scholarly-encyclopedia
    accessed: 2026-11-11
  - id: s5
    title: "Notes to Insolubles"
    publisher: Stanford Encyclopedia of Philosophy (Stephen Read and Paul Vincent Spade)
    url: https://plato.stanford.edu/entries/insolubles/notes.html
    type: scholarly-encyclopedia
    accessed: 2026-11-11
created: 2026-11-11
---

# Masked-man fallacy

The masked-man fallacy, also called the illicit substitution of identicals, is the error of swapping one term for another that refers to the same thing inside a context where such swaps do not preserve truth. Its standard form runs: a is b; someone believes (knows, fears, wants) that a is F; therefore they believe that b is F. A reverse form runs: someone believes a is F but not that b is F; therefore a is not b.[^s1] Both are invalid, because what a person believes depends on how they think of a thing, not only on which thing it is.[^s2]

## Origin

The name comes from an ancient puzzle. Eubulides, a member of the Megarian school in the fourth century BCE, is credited with a set of dialectical puzzles that includes the liar, the heap and "the man in a veil".[^s5][^s1] In the usual telling, you know your father, you do not know the masked man in front of you, and the masked man is your father; so it seems you both know and do not know the same person.[^s1]

The modern diagnosis comes from philosophy of language. Gottlob Frege argued in 1892 that names have a sense (a mode of presentation) as well as a reference, and that inside a "that"-clause a name stands for its sense; two names for one object can differ in sense, so substitution is not licensed.[^s2] W. V. Quine's 1956 paper "Quantifiers and Propositional Attitudes" made the problem central to modern logic. His character Ralph suspects a man in a brown hat of spying but believes the respectable man he once met at the beach is no spy, without knowing they are the same man. Quine called belief contexts referentially opaque: swapping co-referring terms there can change the truth value of the whole sentence.[^s3]

## How it works

In ordinary, extensional contexts, substituting identicals is valid. If the masked man is Mr. Hyde and the masked man committed the crime, then Mr. Hyde committed the crime.[^s1] The rule, known as identity elimination or Leibniz's law, says that if x and y are the same object they share every property.[^s2] The trouble starts when the term sits inside an attitude verb, a quotation, or a modal phrase such as "necessarily". Those positions describe a way of thinking or speaking about the object rather than the object alone, so swapping terms can change what is being claimed.[^s2][^s1]

The argument map above shows a workplace case. The anonymous reviewer and the head of the research office are the same person, and the project lead thinks the reviewer was unfair. But the lead does not know who wrote the review and may well think the head of the office has always been fair. Both premises are true and the conclusion is false, so the form is invalid.[^s4] The reverse form is just as tempting: "I trust our new supplier; I do not trust the company that sent last month's late shipment; so they are different companies" fails if the two turn out to be one firm trading under another name.[^s1][^s3]

## How to spot it

Look for an identity premise ("x is y", "these are the same") combined with a verb of mind or speech: believes, knows, suspects, wants, hopes, recognises, expects.[^s1][^s2] Then check whether the conclusion swaps the terms inside that verb, or whether it uses a difference in someone's attitudes to argue that two things are distinct.[^s1] Quotation and modal words ("must", "could have") create the same trap.[^s2]

## How to counter it

First ask whether the person in question knows the identity. If they do not, the substituted report may be false even though the identity holds.[^s3][^s4] Second, separate two readings of the report. Read de dicto, it describes the person's belief as they would put it, and substitution fails. Read de re, it says of the person or thing itself that they are believed to have the property, and on that reading co-referring terms can be swapped.[^s4] Stating which reading you mean usually dissolves the dispute. Third, never use differences in what someone knows as proof of non-identity; investigate the identity directly.[^s1]

Philosophers still disagree about why substitution fails. Fregeans locate the shift in sense, Quine treated it as a feature of opaque contexts, and Russellian accounts hold that, semantically, the swapped report may even be true while sounding wrong.[^s2] The practical lesson for argument evaluation is the same on each view: the step is not licensed by the identity premise alone.[^s2][^s4]

## Connections

- **Invalid look-alike of substitution of identicals.** The valid rule works in extensional contexts; the fallacy applies it inside intensional ones.[^s1]
- **Explained by referential opacity.** Quine showed that belief contexts block the swap of co-referring terms.[^s3]
- **Explained by sense and reference.** Frege's distinction explains why two names for one object can differ inside a "that"-clause.[^s2]
- **Introduced by Eubulides.** The veiled-man puzzle is attributed to him alongside the liar and the heap.[^s5]
- **Related to equivocation and ambiguity.** The IEP notes Frege treats the bad substitution as an equivocation, and the de re/de dicto ambiguity of reports lets it pass unnoticed.[^s2][^s4]
- **Related to the quantifier shift fallacy and the method of counterexample.** Both are scope errors exposed by a case where premises are true and the conclusion false.[^s4]

## Sources

[^s1]: G. N. Curtis, "The Masked Man Fallacy", The Fallacy Files. https://fallacyfiles.org/illisubs.html (accessed 2026-11-11)
[^s2]: G. Forbes, "Frege's Problem: Referential Opacity", Internet Encyclopedia of Philosophy. https://iep.utm.edu/referential-opacity/ (accessed 2026-11-11)
[^s3]: W. V. Quine, "Quantifiers and Propositional Attitudes", *The Journal of Philosophy* 53(5), 177-187 (1956). https://www.uvm.edu/~lderosse/courses/lang/Quine(1956).pdf (accessed 2026-11-11)
[^s4]: M. Nelson, "The De Re/De Dicto Distinction", supplement to "Propositional Attitude Reports", Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/ENTRIES/prop-attitude-reports/dere.html (accessed 2026-11-11)
[^s5]: S. Read and P. V. Spade, "Notes to Insolubles", Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/entries/insolubles/notes.html (accessed 2026-11-11)
