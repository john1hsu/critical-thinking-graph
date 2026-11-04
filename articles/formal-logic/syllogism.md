---
id: ct:syllogism
type: ReasoningForm
title: Syllogism
aliases: [syllogistic, sullogismos, syllogistic reasoning]
domain: formal-logic
summary: >-
  A deductive argument with two premises and a conclusion in which the premises
  share a linking element (in the categorical case, a middle term) that drops
  out of the conclusion; the family includes categorical, hypothetical and
  disjunctive syllogisms.
level: introductory
evidenceStatus: normative
broader: [ct:deductive-reasoning]
related: [ct:categorical-syllogism, ct:hypothetical-syllogism, ct:disjunctive-syllogism, ct:illicit-major, ct:method-of-counterexample, ct:modus-ponens, ct:modus-tollens, ct:organon, ct:belief-bias]
requires: [ct:validity]
relations:
  - {predicate: introducedBy, object: ct:aristotle, source: s1, confidence: high}
  - {predicate: introducedIn, object: ct:prior-analytics, source: s2, confidence: high}
  - {predicate: studiedIn, object: ct:cognitive-psychology, source: s4, confidence: high}
argumentMap:
  premises:
    - "All production deployments need an approved code review."
    - "All database migrations are production deployments."
  conclusion: "All database migrations need an approved code review."
  verdict: valid
  scheme: ct:categorical-syllogism
  objections:
    - "The form (Barbara) is valid, but if some migrations run outside the deployment pipeline, the second premise is false and the argument is unsound."
sources:
  - id: s1
    title: "Aristotle's Logic"
    publisher: Stanford Encyclopedia of Philosophy (Smith, Spring 2006 archive edition)
    url: https://plato.stanford.edu/archives/spr2006/entries/aristotle-logic/index.html
    type: scholarly-encyclopedia
    accessed: 2026-11-04
  - id: s2
    title: "Medieval Theories of the Syllogism"
    publisher: Stanford Encyclopedia of Philosophy (Lagerlund, Spring 2006 archive edition)
    url: https://plato.stanford.edu/archives/spr2006/entries/medieval-syllogism/
    type: scholarly-encyclopedia
    accessed: 2026-11-04
  - id: s3
    title: "Logic: Deductive and Inductive, Chapter XII: Conditional Syllogisms"
    publisher: "Carveth Read (1914), Lit2Go, University of South Florida"
    url: https://etc.usf.edu/lit2go/37/logic-deductive-and-inductive/467/chapter-12/
    type: textbook
    accessed: 2026-11-04
  - id: s4
    title: "Theories of the Syllogism: A Meta-Analysis"
    publisher: "Psychological Bulletin 138(3), 427-457 (Khemlani & Johnson-Laird, 2012), authors' copy"
    url: https://modeltheory.org/papers/ssk/ssk2012syllogisms-meta-analysis.pdf
    type: peer-reviewed
    accessed: 2026-11-04
created: 2026-11-04
---

# Syllogism

A syllogism is a two-premise deductive argument whose premises are linked by something they share, so that a third claim follows from them taken together. In the classic categorical version, each statement relates two terms, the premises share a middle term, and the conclusion joins the two remaining terms.[^s1] Later logic textbooks extended the name to conditional forms: hypothetical syllogisms built on an "if…then" premise and disjunctive syllogisms built on an "either…or" premise.[^s3]

## Origin

The theory comes from Aristotle, whose word *sullogismos* meant, roughly, an argument in which, once certain things are laid down, something different from them follows of necessity.[^s1] Smith notes that this is broader than the modern textbook sense: for Aristotle the word covered any valid deduction, so an "invalid syllogism" would have been a contradiction in terms, and his definition also required the conclusion to differ from the premises.[^s1] The technical theory of the three figures is set out in the *Prior Analytics*, the work that Lagerlund identifies as the source the medieval tradition commented on once it returned to the Latin West in the mid-twelfth century.[^s2] Medieval logicians such as Abelard, Ockham and Buridan systematised it further, and Lagerlund judges that the syllogistic then changed little for roughly six centuries.[^s2]

## How it works

A categorical syllogism uses four kinds of statement, traditionally labelled A (all S are P), E (no S are P), I (some S are P) and O (some S are not P).[^s2] The conclusion's predicate is the major term, its subject is the minor term, and the middle term appears in both premises but not in the conclusion; where the middle term sits determines the figure.[^s1] Combining statement types within a figure gives a mood, and medieval mnemonic names such as Barbara, Celarent and Camestres record the valid ones.[^s2]

The argument map shows the first-figure mood Barbara in a workplace setting: every premise is a universal affirmative, "production deployments" is the middle term, and the conclusion about database migrations follows necessarily. Aristotle treated a few first-figure moods as perfect, needing no proof, and showed the others valid by reducing them to those through conversion rules (for instance, "no A is B" converts to "no B is A") or by proof through the impossible.[^s1] To show that a pair of premises does not yield a conclusion, he supplied concrete terms that make the premises true and the conclusion false, the ancestor of the modern counterexample method.[^s1]

Conditional syllogisms work differently. A hypothetical syllogism pairs a conditional premise with a categorical one: affirming the antecedent (modus ponens) or denying the consequent (modus tollens) is valid, while denying the antecedent or affirming the consequent is not.[^s3] A disjunctive syllogism pairs an "either…or" premise with a categorical one: denying one alternative licenses affirming the other, but affirming one licenses denying the other only when the alternatives are exclusive.[^s3]

## How to apply it

To test an everyday argument, first restate it as two premises and a conclusion, then name the three terms and confirm that the middle term means the same thing in both premises.[^s1] Next check the rules Aristotle derived: nothing follows from two negative premises or two particular premises; a negative conclusion needs a negative premise; and a universal conclusion needs two universal premises.[^s1] If the form passes, judge the premises separately, since a valid syllogism with a false premise still proves nothing. If you suspect the form, look for a substitution of terms that keeps the premises true while the conclusion fails.[^s1]

## Evidence and limitations

As a standard of good reasoning, valid syllogistic form is normative rather than empirical, but people's performance on syllogisms has been studied heavily. A 2012 meta-analysis of six experiments covering all 64 premise pairs reported that some syllogisms are solved by about 90% of participants and others by about 1%, that accuracy varies widely between individuals, that believable conclusions are accepted more readily than unbelievable ones (especially when invalid), and that none of the twelve psychological theories it compared fully accounts for the data.[^s4] The syllogistic itself is also limited in expressive power: Lagerlund describes how medieval logicians increasingly placed it inside a broader theory of logical consequence, and modern predicate logic handles relations and nested quantifiers that categorical forms cannot express.[^s2]

## Connections

- **Introduced by Aristotle.** Aristotle defined *sullogismos* and built the first theory of its figures and moods.[^s1]
- **Introduced in the Prior Analytics.** The technical syllogistic is set out in the *Prior Analytics*, part of the *Organon*, which later commentators took as their base text.[^s2]
- **Studied in cognitive psychology.** Experiments on all 64 premise pairs measure how people solve syllogisms and how conclusion believability (belief bias) sways them.[^s4]
- **Broader: deductive reasoning; requires validity.** A syllogism is one kind of deductive argument, and judging it presupposes the notion of validity.[^s1]
- **Related forms and fallacies.** The categorical syllogism is the case analysed in figures and moods, and fallacies such as the illicit major break its rules; hypothetical and disjunctive syllogisms are the conditional branches, whose valid moods include modus ponens and modus tollens.[^s3] Aristotle's disproof by substituted terms anticipates the method of counterexample.[^s1]

## Sources

[^s1]: Smith, "Aristotle's Logic", Stanford Encyclopedia of Philosophy (Spring 2006 archive), sections 3, 3.2 and 5.1-5.5. https://plato.stanford.edu/archives/spr2006/entries/aristotle-logic/index.html (accessed 2026-11-04)
[^s2]: Lagerlund, "Medieval Theories of the Syllogism", Stanford Encyclopedia of Philosophy (Spring 2006 archive). https://plato.stanford.edu/archives/spr2006/entries/medieval-syllogism/ (accessed 2026-11-04)
[^s3]: Read, *Logic: Deductive and Inductive* (1914), ch. XII, Lit2Go, University of South Florida. https://etc.usf.edu/lit2go/37/logic-deductive-and-inductive/467/chapter-12/ (accessed 2026-11-04)
[^s4]: Khemlani & Johnson-Laird, "Theories of the Syllogism: A Meta-Analysis", Psychological Bulletin 138(3), 427-457 (2012). https://modeltheory.org/papers/ssk/ssk2012syllogisms-meta-analysis.pdf (accessed 2026-11-04)
