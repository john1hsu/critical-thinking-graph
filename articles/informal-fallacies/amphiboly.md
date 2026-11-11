---
id: ct:amphiboly
type: InformalFallacy
title: Amphiboly
aliases: [amphibology, fallacy of amphiboly, amphibolia, fallacy of syntactic ambiguity]
domain: informal-fallacies
summary: >-
  The fallacy of reasoning from a sentence whose grammatical structure allows
  two readings, accepting a premise on one reading and drawing the conclusion
  on the other, even though no single word in it is ambiguous.
level: introductory
evidenceStatus: normative
broader: [ct:fallacy-of-ambiguity, ct:informal-fallacy]
related: [ct:ambiguity, ct:equivocation, ct:quantifier-shift-fallacy, ct:de-re-de-dicto-distinction, ct:principle-of-charity, ct:precising-definition, ct:william-of-ockham, ct:douglas-walton]
requires: [ct:argument, ct:ambiguity]
relations:
  - {predicate: introducedIn, object: ct:sophistical-refutations, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:aristotle, source: s1, confidence: high}
  - {predicate: instanceOf, object: ct:fallacy-of-ambiguity, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:equivocation, source: s2, confidence: high}
  - {predicate: explainedBy, object: ct:ambiguity, source: s4, confidence: high}
  - {predicate: studiedIn, object: ct:argumentation-theory, source: s3, confidence: medium}
criticalQuestions:
  - Which sentence in the argument can be parsed in more than one way, and what are the readings?
  - On the reading that makes the premise true or authoritative, does the conclusion still follow?
  - Is there evidence from context, the author's purpose or how the text has been applied before that settles which reading was intended?
  - Could the sentence be rewritten so that only one structure is possible, and does the argument survive the rewrite?
argumentMap:
  premises:
    - "The expense policy says receipts are required for meals and taxi fares over $25."
    - "This client lunch cost $18, which is not over $25."
  conclusion: "No receipt is required for this lunch."
  verdict: fallacious
  objections:
    - "The policy sentence can mean 'all meals, plus taxi fares over $25' or 'meals over $25 and taxi fares over $25'; the conclusion needs the second reading."
    - "If finance wrote the rule to cover every meal, the first premise is true only on the reading under which the conclusion does not follow."
sameAs: []
sources:
  - id: s1
    title: "Fallacies"
    publisher: Stanford Encyclopedia of Philosophy (Hansen, Spring 2024 edition)
    url: https://plato.stanford.edu/archives/spr2024/entries/fallacies/
    type: scholarly-encyclopedia
    accessed: 2026-11-11
  - id: s2
    title: "Fallacies"
    publisher: Internet Encyclopedia of Philosophy (Dowden)
    url: https://iep.utm.edu/fallacy/
    type: scholarly-encyclopedia
    accessed: 2026-11-11
  - id: s3
    title: "Profiles of Dialogue for Amphiboly"
    publisher: Informal Logic 40(1) (Walton, 2020), doi:10.22329/il.v40i1.5997, record via Isidore
    url: https://isidore.science/document/10670/1.fld19j
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s4
    title: "3.4: Fallacies of Ambiguity and Grammatical Analogy"
    publisher: "Critical Reasoning and Writing (Levin, Golden West College), Humanities LibreTexts"
    url: https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/Critical_Reasoning_and_Writing_(Levin_et_al.)/03%3A_Informal_Fallacies_-_Mistakes_in_Reasoning/3.04%3A_Fallacies_of_Ambiguity_and_Grammatical_Analogy
    type: textbook
    accessed: 2026-11-11
  - id: s5
    title: "Summa Logicae, Book III-4, Chapter 5 (on amphiboly)"
    publisher: William of Ockham, Latin text and translation, The Logic Museum
    url: https://www.logicmuseum.com/wiki/Authors/Ockham/Summa_Logicae/Book_III-4/Chapter_5
    type: primary
    accessed: 2026-11-11
  - id: s6
    title: "Chapter 21: Fallacy Round-Up"
    publisher: "Critical Thinking, Logic, and Argument, AU Press (Athabasca University)"
    url: https://read.aupress.ca/read/critical-thinking-logic-and-argument/section/79d847f7-75b3-474e-8e16-2465da141e85
    type: textbook
    accessed: 2026-11-11
created: 2026-11-11
---

# Amphiboly

Amphiboly is the fallacy of trading on a sentence whose grammar, rather than any one word, supports two meanings: a premise is accepted under one parse and the conclusion is drawn under the other.[^s1][^s2] The IEP entry describes it as taking a grammatically ambiguous phrase two different ways in the course of the reasoning.[^s2] Hansen's illustration is a notice that police were told to stop drinking on campus after midnight: it may tell the officers themselves to stop drinking, or tell them to stop students from drinking, and an argument that needs the first reading while the context supports the second is fallacious.[^s1] An ambiguous sentence is not yet a fallacy; the error appears only when an inference depends on the slide between readings.[^s4]

## Origin

Aristotle listed amphiboly (*amphibolia*) second among the six fallacies that depend on language in *On Sophistical Refutations*, the family later called *in dictione*.[^s1] Hansen judges that it and equivocation have come down to modern logic textbooks largely unchanged from Aristotle's conception: equivocation is semantic, amphiboly a product of indefinite grammatical structure.[^s1] Copi's *Introduction to Logic* placed it among the "fallacies of ambiguity" with equivocation, accent, composition and division.[^s1]

Medieval logicians developed the idea in detail. In his *Summa Logicae* William of Ockham defined amphiboly as a whole sentence admitting several senses although no individual term is ambiguous, and gave rules for constructions that produce it: a Latin verb whose subject and object cases coincide, so that a report could say either the Romans beat the Greeks or the reverse; ablative absolutes and gerunds that can be read as causal, conditional or temporal; and modal sentences such as "a white thing can be black" versus "it is possible that white is black".[^s5] That last case is what modern logicians call a scope ambiguity.

## How it works

Grammar leaves room for more than one parse when a modifier could attach to different words, a pronoun has two possible antecedents, or a list can be grouped in two ways.[^s4] Levin's textbook gives a used-car advertisement listing "new exhaust and chrome rims": a buyer argues the rims were advertised as new, but the grammar lets "new" modify only the exhaust.[^s4]

The argument map above is a workplace version. A policy requires receipts "for meals and taxi fares over $25". Read one way, every meal needs a receipt and only taxis have a threshold; read the other way, both have the threshold. The employee's conclusion follows only on the second parse, so if finance meant the first, the premise that gives the rule its authority does not support the conclusion. Nothing in the argument fails at the level of individual words, which is why amphiboly is easy to miss once a reader has settled on one structure.[^s6]

## How to spot it

- Identify each sentence the argument depends on and ask whether it parses more than one way: misplaced or dangling modifiers, unclear pronouns, "and/or" lists, and words such as "only", "all" or "possible" whose scope is unclear.[^s4][^s5]
- Write out each reading as a separate, unambiguous sentence, then check whether the premise is true, and the conclusion follows, on the same reading.[^s2]
- Separate it from equivocation: if one word changes meaning, it is equivocation; if every word keeps its meaning but the structure changes, it is amphiboly.[^s2][^s4]
- Do not cry fallacy at every awkward sentence. Headlines and jokes exploit grammatical ambiguity without arguing anything.[^s4]

## How to counter it

Prevention is careful drafting: build sentences so that only one structure is possible, and supply enough context to rule out the likely unintended readings.[^s6] In policies, contracts and requirements, repeat the qualifier ("meals of any amount; taxi fares over $25"), split long lists, and replace pronouns with nouns. When an argument already depends on an amphibolous sentence, state the competing readings and ask which one the arguer is relying on. Walton's 2020 paper treats the question as one of evidence: it offers a five-step procedure that compares how the dialogue actually went with how an ideal critical discussion would have gone, to decide whether a given ambiguous sentence in a real text was used fallaciously.[^s3]

## Connections

- **Introduced in** *Sophistical Refutations* **and by** Aristotle, as one of the six language-dependent fallacies.[^s1]
- **Instance of** the fallacies of ambiguity in Copi's classification.[^s1]
- **Contrasts with** equivocation, which turns on the shifting meaning of a single word rather than on sentence structure.[^s2]
- **Explained by** ambiguity, specifically its structural or grammatical kind.[^s4]
- **Studied in** argumentation theory, where Walton's profiles of dialogue judge alleged amphibolies by the evidence of the exchange in which they occur.[^s3]
- **Related** to William of Ockham's rules for amphibolous sentences, to modal and quantifier scope ambiguities such as the de re/de dicto distinction and the quantifier shift fallacy, and to precising definitions and the principle of charity as remedies.[^s5]

## Sources

[^s1]: H. Hansen, "Fallacies", Stanford Encyclopedia of Philosophy (Spring 2024 edition). https://plato.stanford.edu/archives/spr2024/entries/fallacies/ (accessed 2026-11-11)
[^s2]: B. Dowden, "Fallacies", Internet Encyclopedia of Philosophy. https://iep.utm.edu/fallacy/ (accessed 2026-11-11)
[^s3]: D. Walton, "Profiles of Dialogue for Amphiboly", Informal Logic 40(1) (2020), doi:10.22329/il.v40i1.5997. https://isidore.science/document/10670/1.fld19j (accessed 2026-11-11)
[^s4]: N. Levin, "3.4: Fallacies of Ambiguity and Grammatical Analogy", *Critical Reasoning and Writing*, Humanities LibreTexts. https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/Critical_Reasoning_and_Writing_(Levin_et_al.)/03%3A_Informal_Fallacies_-_Mistakes_in_Reasoning/3.04%3A_Fallacies_of_Ambiguity_and_Grammatical_Analogy (accessed 2026-11-11)
[^s5]: William of Ockham, *Summa Logicae* III-4, ch. 5, The Logic Museum. https://www.logicmuseum.com/wiki/Authors/Ockham/Summa_Logicae/Book_III-4/Chapter_5 (accessed 2026-11-11)
[^s6]: "Chapter 21: Fallacy Round-Up", *Critical Thinking, Logic, and Argument*, AU Press. https://read.aupress.ca/read/critical-thinking-logic-and-argument/section/79d847f7-75b3-474e-8e16-2465da141e85 (accessed 2026-11-11)
