---
id: ct:formal-fallacy
type: Concept
title: Formal fallacy
aliases: [formal fallacies, deductive fallacy, fallacy of form, logical fallacy of form]
domain: formal-fallacies
summary: >-
  An argument that is deductively invalid because of its logical structure: it
  instantiates an invalid form, so any argument with the same form can have true
  premises and a false conclusion, whatever its subject matter.
level: introductory
evidenceStatus: normative
broader: [ct:fallacy]
related: [ct:informal-fallacy, ct:affirming-the-consequent, ct:denying-the-antecedent, ct:affirming-a-disjunct, ct:undistributed-middle, ct:illicit-major, ct:existential-fallacy, ct:modus-ponens, ct:modus-tollens, ct:method-of-counterexample, ct:truth-table, ct:venn-diagram-test]
requires: [ct:argument, ct:validity]
relations:
  - {predicate: studiedIn, object: ct:formal-logic, source: s2, confidence: high}
  - {predicate: influencedBy, object: ct:sophistical-refutations, source: s1, confidence: medium}
  - {predicate: studiedIn, object: ct:cognitive-psychology, source: s5, confidence: high}
  - {predicate: challengedBy, object: ct:gerald-massey, source: s3, confidence: medium}
sources:
  - id: s1
    title: "Fallacy"
    publisher: Encyclopaedia Britannica (Rescher & Schagrin)
    url: https://www.britannica.com/topic/fallacy/Introduction
    type: encyclopedia
    accessed: 2026-11-08
  - id: s2
    title: "Introduction to Logic and Critical Thinking, Version 1.4 (section 4.1, Formal vs. informal fallacies)"
    publisher: "Matthew J. Van Cleave, Lansing Community College (open textbook, eCampusOntario Open Library)"
    url: https://openlibrary-repo.ecampusontario.ca/jspui/bitstream/123456789/314/2/Logic%20text%20v%201.4.pdf
    type: textbook
    accessed: 2026-11-08
  - id: s3
    title: "Four Reasons There are No Fallacies?, in Problems in Argument Analysis and Evaluation"
    publisher: Windsor Studies in Argumentation, University of Windsor (Govier, 2018 edition)
    url: https://ecampusontario.pressbooks.pub/wsia062018/chapter/9/
    type: academic
    accessed: 2026-11-08
  - id: s4
    title: "¿Hay instancias válidas de la falacia de afirmación del consecuente? (Are there valid instances of the fallacy of affirmation of the consequent?)"
    publisher: "Discusiones Filosóficas 12(19), 87-97 (García Duque, 2011), Universidad de Caldas"
    url: https://revistasojs.ucaldas.edu.co/index.php/discusionesfilosoficas/article/download/617/541
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s5
    title: "A Meta-Analysis of Conditional Reasoning"
    publisher: "International Conference on Cognitive Modeling, ICCM 2019 (Ragni, Dames & Johnson-Laird), authors' copy"
    url: https://modeltheory.org/papers/2019meta-conditionals.pdf
    type: peer-reviewed
    accessed: 2026-11-08
created: 2026-11-08
---

# Formal fallacy

A formal fallacy is an argument whose defect lies in its structure: it is deductively invalid because the logical form it follows does not guarantee its conclusion.[^s1] Since validity depends on form rather than content, every argument sharing an invalid form is invalid, so the error can be diagnosed without knowing what the sentences are about.[^s2] This is what separates formal fallacies from informal ones, whose flaws lie in content, wording or presumption and can only be identified by understanding the concepts involved.[^s1][^s2]

## Origin

The idea goes back to Aristotle. His *Sophistical Refutations*, whose classification of fallacies is still widely used, describes a "fallacy of the consequent" that later logic split into the two conditional errors now called affirming the consequent and denying the antecedent.[^s1] The syllogistic tradition added errors of distribution, such as the illicit major and illicit minor, in which a term undistributed in a premise becomes distributed in the conclusion.[^s1] Modern textbooks define the family by contrast with the valid forms of propositional and syllogistic logic: a formal fallacy is the invalid look-alike of a valid pattern such as modus ponens or modus tollens.[^s2]

## How it works

The two classic conditional cases show the pattern. *Affirming the consequent* runs: if P then Q; Q; therefore P. *Denying the antecedent* runs: if P then Q; not P; therefore not Q. Both resemble valid forms closely enough to be mistaken for them.[^s2] Van Cleave makes the point with nonsense words: an argument that toves are brillig because "if toves are brillig they are slithy" and they are slithy is invalid even though no one knows what the words mean, because the form alone fails.[^s2]

A workplace example: "If last night's release broke the checkout service, error rates will spike. Error rates have spiked. So the release broke checkout." The inference affirms the consequent. The premises may both be true while a payment-provider outage, a traffic surge or a database failover caused the spike. The way to expose this is to keep the form and swap in content where the premises are plainly true and the conclusion plainly false, or simply to describe one possible scenario in which that happens, which is how invalidity is shown in general.[^s2]

## How to spot it

Strip the argument to its skeleton and compare it with known valid forms. Watch for a conditional premise used "backwards" (reasoning from the consequent to the antecedent, or from a false antecedent to a false consequent), for a disjunction treated as exclusive when it need not be, and for syllogisms whose middle term is never distributed or whose conclusion says more about a term than the premises did.[^s1][^s2] Then test the suspicion: try to imagine a case with true premises and a false conclusion. If one exists, the argument is invalid.[^s2] Truth tables and Venn diagrams make the same test mechanical for propositional and categorical arguments.[^s2]

## Evidence and limitations

People commit these errors readily. A 2019 meta-analysis of 39 conditional-reasoning experiments with 2,378 participants found that the single most common response pattern was to accept all four conditional inferences, including affirming the consequent and denying the antecedent; that pattern is only valid when "if" is read as "if and only if".[^s5] Part of what looks like a formal error may therefore be a reasonable reading of everyday conditionals, which often carry a biconditional sense.[^s5]

Philosophers also question how far form settles the matter. Gerald Massey argued for an asymmetry: validity can be shown by translating an argument into a valid form, but showing invalidity would require that no adequate translation in any logical system is valid, so naming an invalid form proves little.[^s3] Trudy Govier answers that Massey's case only works inside a strictly formalist framework, that judging an adequate paraphrase is a non-formal skill people often exercise well, and that a true-premises-false-conclusion counterexample remains a legitimate way to show invalidity.[^s3] Carlos García Duque (2011) rejects Massey's claimed valid instance of affirming the consequent, arguing that it either is not a genuine instance of the pattern or, read as one, is invalid after all.[^s4] Govier adds that invalidity is neither necessary nor sufficient for fallaciousness, since some fallacies occur in valid arguments and many good arguments are not deductive.[^s3]

## Connections

Formal fallacy is the umbrella for this graph's invalid-form errors: affirming the consequent and denying the antecedent (invalid look-alikes of modus ponens and modus tollens), affirming a disjunct, and the syllogistic errors of undistributed middle, illicit major and the existential fallacy.[^s1][^s2] It is **studied in formal logic**, which defines validity by form,[^s2] and in **cognitive psychology**, where conditional-reasoning studies measure how often people make these inferences.[^s5] The concept was **influenced by *Sophistical Refutations***, where Aristotle described the fallacy of the consequent.[^s1] Its diagnostic power is **challenged by Gerald Massey**, whose asymmetry thesis questions whether invalidity can be proved by citing a form.[^s3][^s4] It contrasts with the informal fallacy, and it is detected in practice with the method of counterexample, truth tables and the Venn diagram test.[^s2]

## Sources

[^s1]: Rescher & Schagrin, "Fallacy", Encyclopaedia Britannica. https://www.britannica.com/topic/fallacy/Introduction (accessed 2026-11-08)
[^s2]: Van Cleave, *Introduction to Logic and Critical Thinking*, Version 1.4, Lansing Community College, section 4.1 (pp. 185-186) and section 1.6 (pp. 18-20). https://openlibrary-repo.ecampusontario.ca/jspui/bitstream/123456789/314/2/Logic%20text%20v%201.4.pdf (accessed 2026-11-08)
[^s3]: Govier, "Four Reasons There are No Fallacies?", in *Problems in Argument Analysis and Evaluation*, Windsor Studies in Argumentation (2018). https://ecampusontario.pressbooks.pub/wsia062018/chapter/9/ (accessed 2026-11-08)
[^s4]: García Duque, "¿Hay instancias válidas de la falacia de afirmación del consecuente?", *Discusiones Filosóficas* 12(19), 87-97 (2011). https://revistasojs.ucaldas.edu.co/index.php/discusionesfilosoficas/article/download/617/541 (accessed 2026-11-08)
[^s5]: Ragni, Dames & Johnson-Laird, "A Meta-Analysis of Conditional Reasoning", International Conference on Cognitive Modeling (2019). https://modeltheory.org/papers/2019meta-conditionals.pdf (accessed 2026-11-08)
