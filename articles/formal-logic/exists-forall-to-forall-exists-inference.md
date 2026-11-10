---
id: ct:exists-forall-to-forall-exists-inference
type: ReasoningForm
title: Exists-forall to forall-exists inference
aliases: [valid quantifier shift, "∃∀ to ∀∃ inference", someone-to-everyone inference]
domain: formal-logic
summary: >-
  The valid inference from "some single y is related to every x" to "every x
  is related to some y" (from ∃y∀x Rxy to ∀x∃y Rxy), which moves an
  existential quantifier inside a universal one and so trades a strong claim
  for a weaker one that it guarantees.
level: intermediate
evidenceStatus: normative
broader: [ct:deductive-reasoning]
related: [ct:quantifier-shift-fallacy, ct:method-of-counterexample, ct:validity, ct:truth-tree]
requires: [ct:predicate-logic, ct:validity]
relations:
  - {predicate: formalizedBy, object: ct:predicate-logic, source: s2, confidence: high}
  - {predicate: explainedBy, object: ct:quantifier-scope, source: s3, confidence: high}
  - {predicate: contrastsWith, object: ct:quantifier-shift-fallacy, source: s2, confidence: high}
  - {predicate: appliedIn, object: ct:real-analysis, source: s5, confidence: medium}
argumentMap:
  premises:
    - "There is one senior engineer who reviewed every pull request merged this sprint."
  conclusion: "Every pull request merged this sprint was reviewed by some senior engineer."
  verdict: valid
  objections:
    - "The form is valid, but the premise may be false; check the review log before relying on it."
    - "The conclusion is weaker than the premise, so it cannot be used to argue back to a single reviewer."
sameAs: []
sources:
  - id: s1
    title: "Exercises 31: Informal quantifier arguments (solutions)"
    publisher: "Introduction to Formal Logic, 2nd ed. (Peter Smith), Logic Matters"
    url: https://logicmatters.net/ifl/pdfs/Exercises_solutions_31-1.pdf
    type: textbook
    accessed: 2026-11-10
  - id: s2
    title: "forall x: Calgary. An Introduction to Formal Logic (Fall 2021)"
    publisher: "P. D. Magnus, T. Button, J. R. Loftis, R. Trueman, A. Thomas-Bolduc and R. Zach, Open Logic Project, CC BY 4.0"
    url: https://philarchive.org/archive/MAGFXCv4
    type: textbook
    accessed: 2026-11-10
  - id: s3
    title: "3.7 Logical Statements with Multiple Quantifiers"
    publisher: "CSC110/111 course notes, Department of Computer Science, University of Toronto"
    url: https://teach.cs.toronto.edu/~csc110y/fall/notes/03-logic/07-multiple-quantifiers.html
    type: academic
    accessed: 2026-11-10
  - id: s4
    title: "Handout 2: Quantifier Problems"
    publisher: "MATH 3361 Introduction to Mathematical Logic (Fall 2004), Dalhousie University"
    url: https://www.mathstat.dal.ca/~selinger/3361/handouts/handout2.pdf
    type: academic
    accessed: 2026-11-10
  - id: s5
    title: "Lecture 17: Uniform Continuity and the Definition of the Derivative"
    publisher: "18.100A Real Analysis (Fall 2020), MIT OpenCourseWare"
    url: https://live.ocw.mit.edu/courses/18-100a-real-analysis-fall-2020/mit18_100af20_lec17.pdf
    type: academic
    accessed: 2026-11-10
created: 2026-11-10
---

# Exists-forall to forall-exists inference

The exists-forall to forall-exists inference is the valid step from "there is some single y that every x is related to" to "every x is related to some y or other". In predicate-logic notation it moves from ∃y∀x Rxy to ∀x∃y Rxy.[^s1][^s4] If one person is loved by everyone, then everyone loves someone, namely that person. The conclusion is weaker than the premise: it no longer says the y is the same for every x.[^s1][^s3] This is the direction of quantifier swapping that logic allows, and it is the valid pattern that the quantifier shift fallacy runs backwards.[^s2]

## Origin

The inference only becomes visible once a language marks the order of mixed quantifiers, as modern predicate logic does. Open textbooks such as *forall x: Calgary* teach that "everyone loves someone" is ambiguous between a ∀∃ and a ∃∀ reading and that the order of the quantifiers matters a great deal.[^s2] The valid direction is a standard exercise rather than a named discovery. Peter Smith's *Introduction to Formal Logic* sets "There is someone who loves everyone; hence everyone is loved by someone or other" as a practice argument and warns that the quantifiers can be swapped here, but not always.[^s1] A Dalhousie mathematical-logic problem set likewise asks students to derive ∀y∃x from ∃x∀y and then to show that the converse fails.[^s4]

## How it works

The premise names, or at least guarantees, one witness that works for every case. The conclusion only needs a witness for each case separately, and the single witness supplies that.[^s1][^s3] Smith's informal proof runs in three moves. Suppose some person, call her Alex, loves everyone. Pick any person, Bobbie; Alex loves Bobbie, so Bobbie is loved by someone. Since Bobbie was arbitrary, everyone is loved by someone, and since nothing depended on who Alex was, the conclusion follows from the original existential premise.[^s1] In a natural-deduction system these moves are existential elimination with a fresh name, universal elimination, existential introduction and universal introduction. The book's restrictions on those rules, a fresh name for existential elimination and no name from an undischarged assumption for universal introduction, are what let this proof go through while blocking any proof of the reverse.[^s2]

The argument map above applies the form at work. If one senior engineer reviewed every pull request merged this sprint, then every merged pull request was reviewed by some senior engineer. The step is valid whatever the subject matter; whether the argument is sound depends on whether the premise is true.[^s1][^s2]

The University of Toronto notes describe the difference in terms of choice. In ∃∀ the existential choice must be made once, independently of the universal variable; in ∀∃ it may depend on it. A choice that works for everything therefore also works for each thing, but a choice that varies need not have a single common value.[^s3]

## How to apply it

1. Rewrite both claims with explicit quantifiers and check which comes first.[^s2][^s3]
2. If the premise is ∃∀ and the conclusion ∀∃ with the same relation, the inference is valid; use the premise's single witness for every case.[^s1]
3. If the premise is ∀∃ and the conclusion ∃∀, stop: that is the quantifier shift fallacy. Look for an interpretation in which each case gets its own witness and no one witness serves all, such as a domain of couples where each person has a partner but no one is partnered with everyone.[^s2]
4. Remember that a strong uniform claim usually needs its own evidence; the weaker pointwise claim can then be had for free.[^s3][^s5]

## Evidence and limitations

As a rule of classical first-order logic the inference is valid in every interpretation, so its status is normative rather than empirical.[^s2] Its main practical limitation is that it only runs one way. Mathematics gives a clear case. Continuity lets the δ in the ε-δ definition depend on the point, while uniform continuity requires one δ for all points, so a uniformly continuous function is continuous at every point. The converse fails: MIT's real-analysis notes show that 1/x is continuous on (0, 1) but not uniformly continuous there.[^s5][^s2]

## Connections

- **Formalized by predicate logic.** Only a language that fixes quantifier order can state the form and prove it with quantifier rules.[^s2]
- **Explained by quantifier scope.** Whether the existential choice may depend on the universal variable is fixed by which quantifier has wider scope.[^s3]
- **Contrasts with the quantifier shift fallacy.** The fallacy moves from ∀∃ to ∃∀, the invalid reverse of this form, and is refuted by counter-interpretations of the kind the textbook gives.[^s2]
- **Applied in real analysis.** The step from uniform to pointwise continuity is this inference applied to the choice of δ.[^s5]

## Sources

[^s1]: P. Smith, "Exercises 31: Informal quantifier arguments", *Introduction to Formal Logic*, 2nd ed., Logic Matters. https://logicmatters.net/ifl/pdfs/Exercises_solutions_31-1.pdf (accessed 2026-11-10)
[^s2]: P. D. Magnus, T. Button et al., *forall x: Calgary. An Introduction to Formal Logic*, Fall 2021, §§24.3, 32.3, 34. https://philarchive.org/archive/MAGFXCv4 (accessed 2026-11-10)
[^s3]: University of Toronto, CSC110/111 course notes, "3.7 Logical Statements with Multiple Quantifiers". https://teach.cs.toronto.edu/~csc110y/fall/notes/03-logic/07-multiple-quantifiers.html (accessed 2026-11-10)
[^s4]: Dalhousie University, MATH 3361 Introduction to Mathematical Logic, "Handout 2: Quantifier Problems" (Fall 2004). https://www.mathstat.dal.ca/~selinger/3361/handouts/handout2.pdf (accessed 2026-11-10)
[^s5]: MIT OpenCourseWare, 18.100A Real Analysis, "Lecture 17: Uniform Continuity and the Definition of the Derivative" (Fall 2020). https://live.ocw.mit.edu/courses/18-100a-real-analysis-fall-2020/mit18_100af20_lec17.pdf (accessed 2026-11-10)
