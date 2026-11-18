---
id: ct:non-sequitur
type: FormalFallacy
title: Non sequitur
aliases: [it does not follow, fallacy of non sequitur]
domain: formal-fallacies
summary: >-
  The catch-all fallacy of drawing a conclusion that does not follow from the
  reasons given: the premises are so weak or so irrelevant that, even if they
  are true, they give no real support. The label is normally kept for cases
  that no more specific fallacy name fits.
level: introductory
evidenceStatus: normative
broader: [ct:formal-fallacy]
related: [ct:ignoratio-elenchi, ct:validity, ct:argument, ct:informal-fallacy, ct:method-of-counterexample, ct:undistributed-middle, ct:red-herring, ct:affirming-the-consequent, ct:argument-from-fallacy]
requires: [ct:argument, ct:validity]
relations:
  - {predicate: contrastsWith, object: ct:ignoratio-elenchi, source: s4, confidence: high}
  - {predicate: contrastsWith, object: ct:non-argument, source: s3, confidence: high}
  - {predicate: confusedWith, object: ct:fallacy-of-the-consequent, source: s5, confidence: medium}
criticalQuestions:
  - If every premise were true, how much more likely would the conclusion be than it was before you heard them?
  - What unstated premise would be needed to connect these reasons to the conclusion, and is that premise plausible?
  - Can you describe a realistic case in which all the premises are true and the conclusion is false?
  - Does a more specific fallacy (such as undistributed middle or affirming the consequent) describe the gap better than the general label?
  - Is this really an argument, or a bare assertion or demand with no reasons offered at all?
argumentMap:
  premises:
    - "The new CRM vendor has the most polished website of the three we reviewed."
    - "Their sales representative answered every email within an hour."
  conclusion: "So their platform will keep our customer data secure."
  verdict: invalid
  objections:
    - "Marketing polish and quick sales replies say nothing about encryption, access control or breach history; a security review or third-party audit report is what bears on the conclusion."
    - "All three vendors could have responsive sales staff and still differ sharply in how they protect data."
sameAs: []
sources:
  - id: s1
    title: "Fallacies"
    publisher: Internet Encyclopedia of Philosophy (Bradley Dowden)
    url: https://iep.utm.edu/fallacy/
    type: scholarly-encyclopedia
    accessed: 2026-11-18
  - id: s2
    title: "Fallacies (Summer 2019 edition)"
    publisher: Stanford Encyclopedia of Philosophy (Hans Hansen)
    url: https://plato.stanford.edu/archives/sum2019/entries/fallacies/
    type: scholarly-encyclopedia
    accessed: 2026-11-18
  - id: s3
    title: "8.9: Non Sequitur, in Logical Reasoning"
    publisher: "Bradley H. Dowden, California State University Sacramento (Humanities LibreTexts open textbook)"
    url: https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/Logical_Reasoning_(Dowden)/08%3A_Detecting_Fallacies/8.09%3A_Non_Sequitur
    type: textbook
    accessed: 2026-11-18
  - id: s4
    title: "Ignoratio Elenchi and Non Sequitur (Introduction to Logic)"
    publisher: "Lee C. Archie, Philosophy Department, Lander University"
    url: https://philosophy.lander.edu/logic/ignoratio.html
    type: academic
    accessed: 2026-11-18
  - id: s5
    title: "Fallacy"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/fallacy
    type: encyclopedia
    accessed: 2026-11-18
created: 2026-11-18
---

# Non sequitur

A *non sequitur* (Latin for "it does not follow") is an argument whose conclusion is backed only by very weak or irrelevant reasons.[^s3] The Internet Encyclopedia of Philosophy describes it the same way and adds that any inference that is deductively invalid and also very weak by inductive standards qualifies.[^s1] Britannica gives the narrower, textbook-flavoured version: the conclusion fails to follow from the premises, and the gap is so obvious that the argument does not even look valid.[^s5] In a sense every fallacy is a failure of support, so the non sequitur is the broadest fallacy category of all. By convention, though, the label is kept for cases where no more specific fallacy name fits and the weakness of the reasons is easy to show.[^s3][^s1]

## Origin

The idea that a conclusion must actually come from its premises goes back to Aristotle. His *Sophistical Refutations* lists seven fallacies that do not depend on language. One of them, *non-cause*, is ruled out by Aristotle's requirement that a deduction's conclusion be produced by its premises.[^s2] Another, the fallacy of the *consequent*, rests on the mistaken belief that consequence converts: because a fevered person is hot, someone who is hot is assumed to have a fever.[^s2] Britannica notes that some authors use "non sequitur" interchangeably with this fallacy of the consequent, which is why the two names still turn up side by side in older logic texts.[^s5]

## How it works

In the argument map above, a procurement team is choosing a customer-relationship platform. Someone argues that one vendor will keep customer data secure because its website is the most polished and its sales representative answers email within an hour. Both premises may be true, and both may be good news, but neither bears on data security. Encryption, access controls and breach history would; website design does not.[^s3] Dowden's own examples have the same shape: refusing to buy a television because it is Tuesday and Tuesdays are boring, or accepting a risky policy because driving a car is also risky. In both cases the reason would persuade only someone who already accepted the conclusion.[^s3]

A non sequitur can also be a broken formal structure. Archie's example, "Everyone wants to be happy; virtuous people are happy; so everyone wants to be virtuous," fails because some happy people are not virtuous. That is the specific pattern logicians call the undistributed middle, and the IEP notes that formal fallacies in general are invalid arguments that people mistake for valid ones.[^s4][^s1]

## How to spot it

- **The gut reaction test.** Dowden suggests a simple signal: if your response is "that's no sensible reason for that," you are probably looking at a non sequitur.[^s3]
- **Grant the premises.** Assume every premise is true and ask how much the conclusion's likelihood changes. If it barely moves, the reasons are irrelevant or extremely weak.[^s1][^s3]
- **Look for a counterexample.** A case where all the premises hold and the conclusion fails shows the argument is invalid. Archie's happiness example is refuted by pointing to happy people who are not virtuous.[^s4]
- **Check that there is an argument at all.** Dowden separates a non sequitur from a *non-argument*: a bare demand to vote a certain way, with no reason attached, contains nothing that could fail to follow.[^s3]

## How to counter it

Name the gap, not the person. Ask what unstated premise would link the reasons to the conclusion, then say it out loud so everyone can see whether it is believable ("Is a polished website evidence of strong security?").[^s3] Where a more precise diagnosis is available, use it. Dowden advises reserving "non sequitur" for cases no specific fallacy name covers, because a precise label (undistributed middle, affirming the consequent, red herring) tells the arguer exactly what to repair.[^s3][^s4] Finally, keep the verdict proportional: showing that the conclusion does not follow leaves the conclusion unsupported, not false.[^s1]

## Connections

- **Contrasts with ignoratio elenchi.** Archie places the fault of a non sequitur in the link between premises and conclusion, so it is always invalid. An *ignoratio elenchi* may be a perfectly valid argument that proves the wrong point. Some texts treat the non sequitur as a subtype of irrelevant conclusion.[^s4]
- **Contrasts with a non-argument.** Dowden distinguishes an argument whose reasons fail to support it from an utterance that offers no reasons at all, though he notes some writers use the term more loosely.[^s3]
- **Confused with the fallacy of the consequent.** Britannica records that some authors equate the two names.[^s5] Aristotle's fallacy of the consequent is sometimes cited as an early form of affirming the consequent.[^s2]
- **Broader category: formal fallacy.** The IEP counts all deductively invalid reasoning as formal fallacy, and a non sequitur is the most general way for a deduction to fail.[^s1]

## Sources

[^s1]: Dowden, "Fallacies", *Internet Encyclopedia of Philosophy*. https://iep.utm.edu/fallacy/ (accessed 2026-11-18)
[^s2]: Hansen, "Fallacies", *Stanford Encyclopedia of Philosophy* (Summer 2019 edition). https://plato.stanford.edu/archives/sum2019/entries/fallacies/ (accessed 2026-11-18)
[^s3]: Dowden, "8.9: Non Sequitur", *Logical Reasoning*, Humanities LibreTexts. https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/Logical_Reasoning_(Dowden)/08%3A_Detecting_Fallacies/8.09%3A_Non_Sequitur (accessed 2026-11-18)
[^s4]: Archie, "Ignoratio Elenchi", *Introduction to Logic*, Philosophy Department, Lander University. https://philosophy.lander.edu/logic/ignoratio.html (accessed 2026-11-18)
[^s5]: "Fallacy", *Encyclopaedia Britannica*. https://www.britannica.com/topic/fallacy (accessed 2026-11-18)
