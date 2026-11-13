---
id: ct:denying-a-conjunct
type: FormalFallacy
title: Denying a conjunct
aliases: [denying one conjunct]
domain: formal-fallacies
summary: >-
  The invalid inference from "not both P and Q" and "not P" to "Q", which
  forgets that denying a conjunction leaves open the case where both
  conjuncts are false.
level: introductory
evidenceStatus: normative
broader: [ct:formal-fallacy]
related: [ct:affirming-a-disjunct, ct:denying-the-antecedent, ct:affirming-the-consequent, ct:false-dilemma, ct:method-of-counterexample, ct:stoic-logic, ct:chrysippus]
requires: [ct:validity, ct:propositional-logic]
relations:
  - {predicate: invalidFormOf, object: ct:conjunctive-syllogism, source: s1, confidence: high}
  - {predicate: confusedWith, object: ct:conjunctive-syllogism, source: s1, confidence: medium}
  - {predicate: contrastsWith, object: ct:disjunctive-syllogism, source: s1, confidence: medium}
criticalQuestions:
  - Could both conjuncts be false at the same time?
  - Has anyone actually established that at least one of the two options must hold, or is that an unstated assumption?
  - Does the denied conjunct, on its own, imply the conclusion regardless of the "not both" premise?
  - Is the speaker treating "they can't both be true" as if it meant "it has to be one or the other"?
argumentMap:
  premises:
    - "The outage was not caused by both the database migration and the network change."
    - "The outage was not caused by the database migration."
  conclusion: "The outage was caused by the network change."
  verdict: invalid
  scheme: ct:conjunctive-syllogism
  objections:
    - "Neither change may be responsible; a third cause, such as an expired certificate, fits both premises."
    - "The premises only rule out the two changes acting together; they never say one of them must be the cause."
sameAs: []
sources:
  - id: s1
    title: "Denying a Conjunct"
    publisher: The Fallacy Files (Gary N. Curtis)
    url: https://fallacyfiles.org/denyconj.html
    type: community
    accessed: 2026-11-13
  - id: s2
    title: "4.06: Formal Fallacies"
    publisher: "Critical Reasoning and Writing (Noah Levin et al.), Golden West College / NGE Far Press, via Humanities LibreTexts"
    url: https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/Critical_Reasoning_and_Writing_(Levin_et_al.)/04%3A_Deductive_Arguments/4.06%3A_Formal_Fallacies
    type: textbook
    accessed: 2026-11-13
  - id: s3
    title: "Demonstration and the Indemonstrability of the Stoic Indemonstrables"
    publisher: "Phronesis (Susanne Bobzien; accepted 2019), author's copy on PhilArchive"
    url: https://philarchive.org/archive/BOBDAT-2
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s4
    title: "Negating compound sentences"
    publisher: "Proceedings of the 34th Annual Meeting of the Cognitive Science Society (Khemlani, Orenes & Johnson-Laird, 2012), author's copy"
    url: https://modeltheory.org/papers/ssk/ssk2012negating-compound-sentences.pdf
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s5
    title: "Stoic Logic (CLAS 196/PHIL 196 Stoicism course notes)"
    publisher: University of Vermont
    url: https://www.uvm.edu/~jbailly/courses/196Stoicism/notes/StoicLogic.html
    type: academic
    accessed: 2026-11-13
created: 2026-11-13
---

# Denying a conjunct

Denying a conjunct is the argument form "not both P and Q; not P; therefore Q" (or, symmetrically, "not both P and Q; not Q; therefore P").[^s1] The first premise denies a conjunction: it says the two statements are not true together. That leaves three possibilities open: P without Q, Q without P, and neither. The second premise rules out P, but the "neither" case survives, so the conclusion that Q must be true does not follow.[^s1][^s2] Because an argument of this shape can have true premises and a false conclusion, the defect lies in its form, and it counts as a formal fallacy.[^s1] Gary Curtis's counterexample makes the gap plain: it isn't both raining and snowing; it isn't raining; so it's snowing. On a dry, clear day both premises are true and the conclusion is false.[^s1]

## Origin

The fallacy is the invalid twin of a valid pattern logicians have used since antiquity. The Stoics, whose logic was systematised by Chrysippus, listed five "indemonstrable" argument forms that needed no proof, and the third of them starts from a negated conjunction.[^s5] Susanne Bobzien gives its standard example: not both is it day and is it night; it is day; so it is not night.[^s3] On her account, the Stoics held that the validity of such forms is immediately evident once the form is recognised.[^s3] The valid pattern affirms one conjunct and denies the other; the fallacy reverses this, denying one conjunct and affirming the other.[^s1] Curtis traces the modern label to logic textbooks such as Howard Pospesel's *Introduction to Logic: Propositional Logic* and notes a confusing older alias from W. L. Reese's *Dictionary of Philosophy and Religion*, which he argues muddles "not both" with an exclusive "either…or".[^s1]

## How it works

The fallacy borrows the look of the valid "conjunctive argument", in which knowing one conjunct is true lets you infer that the other is false. It swaps the affirmation for a denial, and that move needs a premise nobody supplied: that at least one of the two must be true.[^s1] Introductory textbooks make the same point with a simple case: I can't be both at home and in the city; I'm not at home; so I'm in the city. The speaker could be somewhere else entirely.[^s2]

The argument map above gives a workplace version. During an incident review, the team agrees the outage wasn't caused by the database migration and the network change acting together. Someone then shows the migration was not at fault and declares the network change guilty. Both premises can be true while the conclusion is false, because a third cause, such as an expired certificate, fits everything that has been established. The hidden assumption is that the two changes exhaust the candidates.[^s1][^s2]

## How to spot it

Look for a "can't be both" or "not both" claim, a statement ruling out one of the options, and a conclusion that the other option must therefore hold.[^s1][^s2] Then apply the method of counterexample: keep both premises true and ask whether both options could be false. If a realistic "neither" case exists, the inference fails.[^s1] Check one exception before calling foul. If the denied conjunct alone implies the conclusion, the argument may be valid for reasons unrelated to the "not both" premise.[^s1]

## How to counter it

Name the missing premise. Adding "either P or Q" turns the argument into a valid disjunctive syllogism, so the real question becomes whether that disjunction is true.[^s1] Sometimes it is obviously implied by the context, as when only two candidates are possible; Curtis treats such cases as acceptable enthymemes rather than fallacies.[^s1] Where the options are not exhaustive, as with causes of an outage or explanations for a missed target, ruling one out is a reason to keep looking, not a reason to convict the other. This is the same discipline that guards against a false dilemma, which presents two options as the only ones.[^s1][^s2]

## Evidence

The invalidity of the form is a standard logical result, not an empirical claim.[^s1][^s2] Psychological work suggests people find negated conjunctions hard to represent. In a 2012 study, Khemlani, Orenes and Johnson-Laird asked 22 participants which combinations of cases were possible given the denial of a conjunction. Only 18% of responses were correct, compared with 89% for denied disjunctions, and most participants selected a single possibility.[^s4] In a second experiment with 21 participants, none formulated a correct denial of a conjunction; about two-thirds wrote "not A and not B", collapsing the three possibilities into one.[^s4] The authors explain the difficulty with mental model theory: people tend to represent only one possibility for a negated conjunction rather than all three.[^s4] That evidence comes from small samples and concerns understanding negation in general, not this fallacy in particular, so it is suggestive rather than direct.[^s4]

## Connections

- **Invalid form of the conjunctive syllogism.** The Fallacy Files presents denying a conjunct as the non-validating look-alike of the conjunctive argument, which affirms rather than denies a conjunct.[^s1]
- **Confused with the conjunctive syllogism.** The same source attributes the fallacy's appeal to its surface resemblance to that valid form.[^s1]
- **Contrasts with disjunctive syllogism.** Adding the disjunctive premise "P or Q" makes the inference valid as a disjunctive syllogism; the fallacy treats "not both" as though it said "one or the other".[^s1]
- **Related to Stoic logic and Chrysippus.** The valid counterpart is the third Stoic indemonstrable.[^s3][^s5]
- **Related to affirming a disjunct, denying the antecedent and affirming the consequent.** These are sibling propositional fallacies that each misuse a valid form, and each yields to the method of counterexample.[^s1][^s2]

## Sources

[^s1]: Curtis, "Denying a Conjunct", *The Fallacy Files*. https://fallacyfiles.org/denyconj.html (accessed 2026-11-13)
[^s2]: Levin et al., "4.06: Formal Fallacies", *Critical Reasoning and Writing*, Humanities LibreTexts. https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/Critical_Reasoning_and_Writing_(Levin_et_al.)/04%3A_Deductive_Arguments/4.06%3A_Formal_Fallacies (accessed 2026-11-13)
[^s3]: Bobzien, "Demonstration and the Indemonstrability of the Stoic Indemonstrables", *Phronesis* (author's copy). https://philarchive.org/archive/BOBDAT-2 (accessed 2026-11-13)
[^s4]: Khemlani, Orenes & Johnson-Laird, "Negating compound sentences", *Proceedings of the 34th Annual Meeting of the Cognitive Science Society*, 2012. https://modeltheory.org/papers/ssk/ssk2012negating-compound-sentences.pdf (accessed 2026-11-13)
[^s5]: "Stoic Logic", CLAS 196/PHIL 196 *Stoicism* course notes, University of Vermont. https://www.uvm.edu/~jbailly/courses/196Stoicism/notes/StoicLogic.html (accessed 2026-11-13)
