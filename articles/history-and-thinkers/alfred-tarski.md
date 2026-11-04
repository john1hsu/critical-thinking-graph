---
id: ct:alfred-tarski
type: Person
title: Alfred Tarski
aliases: [Alfred Tajtelbaum, Alfred Teitelbaum]
domain: history-and-thinkers
summary: >-
  Polish-American logician and mathematician (1901-1983) whose 1933 definition
  of truth for formal languages and 1936 model-theoretic definition of logical
  consequence gave modern logic its standard account of what it means for an
  argument to be valid.
level: intermediate
evidenceStatus: historical
broader: []
related: [ct:validity, ct:soundness, ct:liar-paradox, ct:formal-logic, ct:method-of-counterexample]
requires: []
relations:
  - {predicate: introduced, object: ct:logical-consequence, source: s1, confidence: high}
  - {predicate: introduced, object: ct:validity, source: s4, confidence: medium}
  - {predicate: introduced, object: ct:convention-t, source: s3, confidence: high}
  - {predicate: influencedBy, object: ct:stanislaw-lesniewski, source: s1, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Alfred Tarski"
    publisher: Stanford Encyclopedia of Philosophy (Gómez-Torrente, rev. 2023)
    url: https://plato.stanford.edu/ENTRIES/tarski/
    type: scholarly-encyclopedia
    accessed: 2026-11-04
  - id: s2
    title: "Alfred Tarski (biography)"
    publisher: MacTutor History of Mathematics, University of St Andrews (O'Connor & Robertson)
    url: https://mathshistory.st-andrews.ac.uk/Biographies/Tarski/
    type: academic
    accessed: 2026-11-04
  - id: s3
    title: "Tarski's Truth Definitions"
    publisher: Stanford Encyclopedia of Philosophy (Hodges, rev. 2022)
    url: https://plato.stanford.edu/ENTRIES/tarski-truth/
    type: scholarly-encyclopedia
    accessed: 2026-11-04
  - id: s4
    title: "Logical Consequence, Model-Theoretic Conceptions"
    publisher: Internet Encyclopedia of Philosophy
    url: https://iep.utm.edu/logcon-m/
    type: scholarly-encyclopedia
    accessed: 2026-11-04
  - id: s5
    title: "Semantic Theory of Truth"
    publisher: Internet Encyclopedia of Philosophy
    url: https://iep.utm.edu/s-truth/
    type: scholarly-encyclopedia
    accessed: 2026-11-04
created: 2026-11-04
---

# Alfred Tarski

Alfred Tarski (1901-1983) was a Polish-born logician and mathematician who spent most of his career at the University of California, Berkeley.[^s1][^s2] For critical thinkers he matters because he turned two everyday ideas into precise definitions: what it means for a sentence to be true, and what it means for a conclusion to follow logically from premises. The second is the definition of validity that logic textbooks still teach.[^s1][^s4]

## Origin

Tarski was born in Warsaw, then part of the Russian Empire, with the family name Tajtelbaum, which he changed to Tarski around 1923.[^s1][^s2] He studied mathematics and philosophy at the University of Warsaw from 1918 and took his doctorate there in 1924 under Stanisław Leśniewski, after courses with Łukasiewicz, Kotarbiński and Sierpiński, central figures of the Lvov-Warsaw school.[^s1] The same year he published with Stefan Banach the result now known as the Banach-Tarski paradox.[^s2]

In August 1939 he travelled to the United States for a Unity of Science congress; war broke out within weeks and he could not return, while his wife and children stayed in Poland until 1946.[^s1][^s2] After temporary posts at Harvard, the City College of New York and the Institute for Advanced Study, he joined Berkeley in 1942, became a full professor later that decade and built one of the leading schools of logic there; he died in Berkeley in October 1983.[^s1][^s2]

## How it works

**Truth (1933).** In *The Concept of Truth in Formalized Languages* Tarski set out what an adequate definition of "true sentence" must achieve and showed that such definitions exist for a range of formal languages.[^s3] His adequacy test, Convention T, requires the definition to yield every instance of the pattern "'Snow is white' is true if and only if snow is white."[^s3][^s5] To avoid the liar paradox, he defined truth for an object language inside a separate, richer metalanguage, and proved that a language strong enough to express arithmetic cannot define its own truth.[^s1][^s5] He built truth from the recursive notion of satisfaction, a forerunner of the definition of truth in a model that logicians use today.[^s3]

**Logical consequence (1936).** Tarski argued that consequence could not be captured by derivability alone: some theories prove every instance of a general claim but not the claim itself, even though it intuitively follows.[^s1] He also showed that a test based only on swapping non-logical words is necessary but not sufficient, because a language may lack names for everything.[^s1] His replacement was semantic: a sentence follows from a set of premises when every model, or interpretation of the non-logical vocabulary, that makes all the premises true also makes the sentence true.[^s1][^s4] An argument is valid when no structure makes its premises true and its conclusion false.[^s4]

A workplace example shows the test in use. "All approved invoices are paid within 30 days. This invoice was paid within 30 days. So it was approved." Keep "all", "this" and "so" fixed and reinterpret the content words: let "approved invoice" mean "cat", "paid within 30 days" mean "mammal" and "this invoice" name a dog. The premises come out true and the conclusion false, so the argument is invalid in Tarski's sense, whatever the facts about invoices.[^s4] This is the formal basis for the familiar method of refuting an argument by counterexample.

## Legacy and limitations

Model-theoretic semantics and the model-based definition of consequence became central to logic, and Tarski's work on truth reshaped the views of philosophers including Carnap and Popper.[^s5] The account has critics. Etchemendy argues that it does not capture the necessity of logical consequence, since whether an argument counts as valid can depend on how many objects exist.[^s4] Its verdicts also depend on which words are classed as logical; Tarski admitted he saw no sharp boundary and later proposed that logical notions are those unchanged by any one-to-one transformation of the universe.[^s1][^s4] Critics of his truth theory object that its hierarchy of languages fits poorly with how speakers use "true."[^s5] None of this removed the core idea from textbooks, but it is why philosophers still debate what validity ultimately is.[^s4]

## Connections

- **Introduced the model-theoretic definition of logical consequence** in his 1936 paper, defining consequence as truth preservation across all models.[^s1]
- **Introduced the modern definition of validity.** On his account an argument is valid when no structure makes its premises true and its conclusion false; the underlying idea of necessary following goes back to Aristotle's syllogistic, but the precise semantic test is Tarski's.[^s4]
- **Introduced Convention T**, the adequacy condition for definitions of truth.[^s3]
- **Influenced by Stanisław Leśniewski**, his doctoral supervisor, whose views on the liar paradox Tarski followed in relativizing truth to a language.[^s1][^s5]
- **Related to soundness, the liar paradox and the method of counterexample.** Soundness adds true premises to his notion of validity, the liar paradox drove his object-language and metalanguage split, and reinterpretation counterexamples are how his definition is applied.[^s4][^s5]

## Sources

[^s1]: Gómez-Torrente, "Alfred Tarski", Stanford Encyclopedia of Philosophy, rev. 2023. https://plato.stanford.edu/ENTRIES/tarski/ (accessed 2026-11-04)
[^s2]: O'Connor & Robertson, "Alfred Tarski", MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Tarski/ (accessed 2026-11-04)
[^s3]: Hodges, "Tarski's Truth Definitions", Stanford Encyclopedia of Philosophy, rev. 2022. https://plato.stanford.edu/ENTRIES/tarski-truth/ (accessed 2026-11-04)
[^s4]: "Logical Consequence, Model-Theoretic Conceptions", Internet Encyclopedia of Philosophy. https://iep.utm.edu/logcon-m/ (accessed 2026-11-04)
[^s5]: "Semantic Theory of Truth", Internet Encyclopedia of Philosophy. https://iep.utm.edu/s-truth/ (accessed 2026-11-04)
