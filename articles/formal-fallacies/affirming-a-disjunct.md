---
id: ct:affirming-a-disjunct
type: FormalFallacy
title: Affirming a disjunct
aliases: [affirming one disjunct, fallacy of the alternative syllogism, improper disjunctive syllogism, asserting an alternative]
domain: formal-fallacies
summary: >-
  The invalid inference from "P or Q" and "P" to "not Q", which treats an
  inclusive "or" as if it ruled out both alternatives being true at once.
level: introductory
evidenceStatus: normative
broader: [ct:formal-fallacy]
related: [ct:affirming-the-consequent, ct:denying-the-antecedent, ct:false-dilemma, ct:method-of-counterexample, ct:syllogism, ct:monroe-beardsley]
requires: [ct:validity]
relations:
  - {predicate: invalidFormOf, object: ct:disjunctive-syllogism, source: s1, confidence: high}
  - {predicate: confusedWith, object: ct:disjunctive-syllogism, source: s1, confidence: medium}
  - {predicate: explainedBy, object: ct:conversational-implicature, source: s2, confidence: medium}
  - {predicate: explainedBy, object: ct:mental-model-theory, source: s4, confidence: medium}
criticalQuestions:
  - Could both alternatives in the "or" premise be true at the same time?
  - Is the "or" meant exclusively, and if so, has the "not both" claim been stated and supported?
  - Does the affirmed alternative by itself rule out the other one, independent of the disjunction?
  - What would a realistic case look like in which both options hold together?
argumentMap:
  premises:
    - "The release slipped because of the vendor delay or because of the staffing gap."
    - "The release slipped because of the vendor delay."
  conclusion: "The staffing gap did not contribute to the slip."
  verdict: invalid
  scheme: ct:disjunctive-syllogism
  objections:
    - "Delays often have several causes; the vendor delay and the staffing gap could both have contributed."
    - "Confirming one cause says nothing about the other unless the two are known to be mutually exclusive."
sameAs: []
sources:
  - id: s1
    title: "Affirming a Disjunct"
    publisher: The Fallacy Files (Gary N. Curtis)
    url: https://www.fallacyfiles.org/afonedis.html
    type: community
    accessed: 2026-11-06
  - id: s2
    title: "Disjunction"
    publisher: Stanford Encyclopedia of Philosophy (Maria Aloni, first published 2016; Winter 2022 edition)
    url: https://plato.stanford.edu/archives/win2022/entries/disjunction/
    type: scholarly-encyclopedia
    accessed: 2026-11-06
  - id: s3
    title: "A Plea For Affirming a Disjunct"
    publisher: "Informal Logic 8(3), 133-139 (Brian Kirby, 1986)"
    url: https://distantreader.org/stacks/journals/il/il-2691.pdf
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s4
    title: "The modulation of disjunctive assertions"
    publisher: "Quarterly Journal of Experimental Psychology 70(4), 703-717 (Quelhas & Johnson-Laird, 2017), doi:10.1080/17470218.2016.1154079, author's copy"
    url: https://modeltheory.org/papers/2016mod-disjns.pdf
    type: peer-reviewed
    accessed: 2026-11-06
created: 2026-11-06
---

# Affirming a disjunct

Affirming a disjunct is the argument form "P or Q; P; therefore not Q" (or, symmetrically, "P or Q; Q; therefore not P"). The first premise offers two alternatives, the second confirms one of them, and the conclusion rejects the other.[^s1] Under the inclusive reading of "or" that standard logic uses, a disjunction is true when at least one alternative holds, including when both do.[^s2] Confirming one alternative therefore says nothing about the other, and an argument of this shape can have true premises and a false conclusion. That defect lies in the form, which makes this a formal fallacy.[^s1] The Fallacy Files offers a simple case: either it is raining or the sun is shining; it is raining; so the sun is not shining. A sunshower makes both premises true and the conclusion false.[^s1]

## Origin

The fallacy is the invalid twin of disjunctive syllogism, the valid pattern "P or Q; not P; therefore Q", which concludes one alternative from the denial of the other. Logic dictionaries record the invalid variant under names such as "fallacy of the alternative syllogism" and "improper disjunctive syllogism".[^s1] Its status became a point of debate once logicians separated two senses of "or". Inclusive ("weak") disjunction allows both alternatives, while exclusive ("strong") disjunction allows exactly one. Brian Kirby's 1986 paper in *Informal Logic* argued that textbooks gave the inclusive reading too much priority. Many everyday disjunctions, such as a traffic light being red or green, are exclusive, and with them the "fallacious" form is valid.[^s3] Kirby concluded that whether an instance is a fallacy depends on how the "or" is meant.[^s3]

## How it works

The fallacy imitates disjunctive syllogism but swaps a denial for an affirmation. Disjunctive syllogism eliminates one alternative and is valid whichever sense of "or" is used. Affirming a disjunct instead confirms one alternative and tries to eliminate the other, which only works when the alternatives cannot both be true.[^s1][^s3]

The argument map above gives a workplace version. A project lead says the release slipped because of a vendor delay or a staffing gap. A review confirms the vendor delay, and the lead concludes the staffing gap played no part. Delays often have more than one cause, so both premises can be true while the conclusion is false. The inference rests on an unstated "not both" premise that nobody has checked.[^s1]

Philosophers of language explain why the move feels natural. Maria Aloni's Stanford Encyclopedia entry describes the "not both" reading of an ordinary "or" as an extra inference added to its inclusive core. It can be cancelled, as in "she invited John or Bill, or both". Following H. P. Grice, many linguists treat this reading as a conversational implicature: a speaker who knew both were true would normally have said "and".[^s2] A listener can then reason from a "not both" message the speaker never asserted.[^s2]

## How to spot it

Look for an "either…or" claim, a statement confirming one option, and a conclusion that rejects the other option.[^s1] Then test the form: assume both premises are true and try to imagine a case in which both alternatives hold together. If one is easy to find, as with multiple causes of a delay, two skills on a CV, or rain with sunshine, the inference fails.[^s1][^s3] Also check whether the affirmed alternative alone rules out the other. If confirming P is itself incompatible with Q, the argument can be valid for reasons unrelated to the disjunction.[^s1]

## How to counter it

Ask whether the speaker means an exclusive "or". If so, the honest repair is to state the hidden premise, "not both P and Q", and defend it. The argument is then valid, but now depends on that premise.[^s1][^s3] Some disjunctions earn the exclusive reading because the options are known to be incompatible, as with a stoat or a weasel, or ordering the chicken or the steak. Others, such as an allergist suspecting goldenrod or cat dander behind a rash, plainly allow both.[^s3] Where both are possible, as in diagnosis and incident reviews, confirming one cause is a reason to keep checking the others rather than to end the search.

## Evidence

As a matter of logic, the form is invalid for inclusive disjunction and valid for exclusive disjunction; this is a standard textbook result, not an empirical claim.[^s2][^s3] Psychological research shows that people's readings of "or" depend on content. In a 2017 *Quarterly Journal of Experimental Psychology* paper, Quelhas and Johnson-Laird ran three experiments with between 35 and 88 participants each. They found that knowledge about the clauses shaped which possibilities people saw. In their third experiment, 80% of conclusions drawn from disjunctions with incompatible alternatives (such as being in Portugal or in Spain) were exclusive, such as "not B". That figure fell to 32-44% for disjunctions whose contents allowed both alternatives.[^s4] The authors explain this with mental model theory: "or" starts with inclusive possibilities, and background knowledge can block the "both" possibility.[^s4] So people do not apply a blanket exclusive reading, which suggests the fallacy mainly arises when content makes the alternatives look like rivals even though they can coexist.[^s4]

## Connections

- **Invalid form of disjunctive syllogism.** The Fallacy Files presents it as the non-validating look-alike of disjunctive syllogism, differing in affirming rather than denying a disjunct.[^s1]
- **Confused with disjunctive syllogism.** The same source suggests people accept the fallacy because they mistake it for that valid form.[^s1]
- **Explained by conversational implicature.** The "not both" reading of "or" is widely treated as a Gricean implicature, not part of what is said.[^s2]
- **Explained by mental model theory.** Quelhas and Johnson-Laird account for when people draw the exclusive conclusion by content blocking the "both" model.[^s4]
- **Related to false dilemma, affirming the consequent and denying the antecedent.** False dilemma attacks the disjunctive premise, while this fallacy misuses a true one. The other two are the parallel invalid forms built on conditionals, and all three can be exposed by the method of counterexample.[^s1][^s3]

## Sources

[^s1]: Curtis, "Affirming a Disjunct", *The Fallacy Files*. https://www.fallacyfiles.org/afonedis.html (accessed 2026-11-06)
[^s2]: Aloni, "Disjunction", *Stanford Encyclopedia of Philosophy* (Winter 2022 edition). https://plato.stanford.edu/archives/win2022/entries/disjunction/ (accessed 2026-11-06)
[^s3]: Kirby, "A Plea For Affirming a Disjunct", *Informal Logic* 8(3), 1986. https://distantreader.org/stacks/journals/il/il-2691.pdf (accessed 2026-11-06)
[^s4]: Quelhas & Johnson-Laird, "The modulation of disjunctive assertions", *Quarterly Journal of Experimental Psychology* 70(4), 2017. https://modeltheory.org/papers/2016mod-disjns.pdf (accessed 2026-11-06)
