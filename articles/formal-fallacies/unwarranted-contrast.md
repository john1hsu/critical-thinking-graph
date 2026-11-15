---
id: ct:unwarranted-contrast
type: FormalFallacy
title: Unwarranted contrast
aliases: [some are/some are not, some-are-some-are-not fallacy, fallacy of unwarranted contrast]
domain: formal-fallacies
summary: >-
  The invalid immediate inference from "Some S are P" to "Some S are not P"
  (or the reverse). The two statements are subcontraries, which can both be
  true, so neither entails the other; the "not all" reading of "some" is a
  conversational implicature that context can cancel, not a logical
  implication.
level: intermediate
evidenceStatus: normative
broader: [ct:formal-fallacy]
related: [ct:square-of-opposition, ct:categorical-proposition, ct:existential-fallacy, ct:illicit-conversion, ct:venn-diagram-test, ct:method-of-counterexample, ct:quantifier-shift-fallacy]
requires: [ct:categorical-proposition, ct:square-of-opposition, ct:validity]
relations:
  - {predicate: explainedBy, object: ct:conversational-implicature, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:existential-fallacy, source: s1, confidence: medium}
  - {predicate: introducedIn, object: ct:the-cambridge-dictionary-of-philosophy, source: s1, confidence: medium}
  - {predicate: studiedIn, object: ct:pragmatics, source: s4, confidence: medium}
criticalQuestions:
  - Does the premise say anything at all about the members of the class that lack the property, or is the "not" only suggested by the word "some"?
  - Could every member of the class have the property without making the premise false?
  - Did the speaker say "some" because they lacked information about the rest, rather than because they knew some were excluded?
  - Would the speaker withdraw anything if told "in fact, all of them do"?
argumentMap:
  premises:
    - "The audit report says some of our supplier invoices were paid late."
  conclusion: "So some of our supplier invoices were paid on time."
  verdict: invalid
  objections:
    - "If every invoice in the period was paid late, the premise is still true and the conclusion is false."
    - "The auditors may have checked only a sample and said 'some' because they could not speak for the rest."
sameAs: []
sources:
  - id: s1
    title: "Some Are/Some Are Not"
    publisher: The Fallacy Files (Gary N. Curtis)
    url: https://fallacyfiles.org/somernot.html
    type: community
    accessed: 2026-11-15
  - id: s2
    title: "The Traditional Square of Opposition"
    publisher: "Stanford Encyclopedia of Philosophy (Parsons; rev. Ciola, 2025)"
    url: https://plato.stanford.edu/ENTRIES/square/
    type: scholarly-encyclopedia
    accessed: 2026-11-15
  - id: s3
    title: "Implicature"
    publisher: "Stanford Encyclopedia of Philosophy (Davis, rev. 2024)"
    url: https://plato.stanford.edu/ENTRIES/implicature/
    type: scholarly-encyclopedia
    accessed: 2026-11-15
  - id: s4
    title: "Some utterances are underinformative: The onset and time course of scalar inferences (Journal of Memory and Language 51(3), 2004)"
    publisher: "Bott & Noveck, Cardiff University ORCA repository"
    url: https://orca.cardiff.ac.uk/id/eprint/3267/
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s5
    title: "When children are more logical than adults: Experimental investigations of scalar implicature (Cognition 78(2), 2001), author's announcement"
    publisher: "Noveck, Relevance Theory Online Bibliographic Service, University College London"
    url: https://www.phon.ucl.ac.uk/home/relevance/relevance_archives/0112.html
    type: academic
    accessed: 2026-11-15
created: 2026-11-15
---

# Unwarranted contrast

Unwarranted contrast, also called the "some are/some are not" fallacy, is the immediate inference from a particular affirmative statement to the matching particular negative, or the reverse: "Some S are P, therefore some S are not P," or "Some S are not P, therefore some S are P."[^s1] The Fallacy Files classes it as a formal fallacy of quantificational logic: the premise can be true while the conclusion is false, so the form is invalid whatever the subject matter.[^s1] It is tempting because, in ordinary talk, saying "some" usually suggests "not all." That suggestion is real, but it belongs to the act of saying something, not to what the sentence logically implies.[^s1][^s3]

## Origin

The logical core is old. In the traditional square of opposition, the I form ("Some S is P") and the O form ("Some S is not P") are subcontraries: they cannot both be false, but they can both be true.[^s2] Subcontrariety is not entailment, so the square licenses no step from either one to the other.[^s2] The Stanford Encyclopedia notes that Aristotle worded the O form as "Not every S is P," and that his own paired example, some man is white and not every man is white, has both members true together.[^s2] The label "some are/some are not" is credited to W. Kent Wilson's entry on formal fallacy in the *Cambridge Dictionary of Philosophy*, and the standard diagnosis draws on Paul Grice's account of conversational implicature in "Logic and Conversation."[^s1]

## How it works

Grice distinguished what a speaker says from what the speaker implicates, the further meaning a cooperative listener reads into the remark.[^s3] One of his maxims, Quantity, asks speakers to be as informative as the exchange requires.[^s3] If a speaker knew that every S was P, saying only "some" would be less informative than they could have been, so listeners take "Some athletes smoke" to suggest that not all do.[^s3] This is a scalar or quantity implicature. Unlike an entailment, it can be cancelled without contradiction: "Some athletes smoke; indeed, all do" is odd but consistent.[^s3] The fallacy treats that cancellable suggestion as if it were a logical consequence, confusing implicature with implication.[^s1]

The argument map above shows the pattern at work. An audit summary says that some supplier invoices were paid late, and a manager concludes that some were paid on time. If every invoice in the period was late, the summary is still true and the manager's conclusion is false. In a Venn diagram of the premise, the region for invoices paid on time is left blank, not marked as occupied.[^s1] The auditors may also have said "some" because they checked only a sample, which gives no information about the rest.

## How to spot it

Look for a conclusion about the members that lack a property when the only premise is about the members that have it, or the reverse.[^s1] Watch for words such as "so the others," "which means some don't," or "at least some must," used right after a "some" claim. A quick test is cancellation: add "in fact, all of them" to the premise. If the result is consistent, the premise did not entail the contrast.[^s3] Also ask why the speaker chose "some." An implicature of "not all" arises only when the speaker is assumed to know the full picture. A speaker who lacks that knowledge implicates only that they cannot say more.[^s3]

## How to counter it

Name the gap: the premise tells you about some members of the class and is silent about the rest.[^s1] Offer the counterexample in which every member has the property, so the premise stays true and the conclusion fails.[^s1][^s2] If the contrast matters, for example when a decision depends on whether any invoices were paid on time, ask for a direct statement or the underlying data rather than reading it off the word "some." Writers can avoid inviting the error by saying "only some" or "some but not all" when they mean exclusion. Those phrases state the exclusion outright, so it can no longer be cancelled.[^s3]

## Evidence

Although the fallacy itself is a matter of logic, psychologists have studied how readily people draw the "not all" inference. In a 2001 paper in *Cognition*, Ira Noveck reported that children aged eight and ten mostly treated the French *certains* ("some") as compatible with "all," while adults split between that logical reading and the pragmatic "not all" reading.[^s5] In four sentence-verification experiments published in 2004, Lewis Bott and Noveck found that adults who gave the "some but not all" reading to underinformative sentences such as "Some elephants are mammals" responded more slowly. The rate of that reading also rose when people were allowed more time to respond.[^s4] The authors took these results as evidence that the scalar inference is an effortful, context-driven step, not an automatic default.[^s4] For critical thinkers, the point is that the "not all" reading is common but optional, which is why it cannot carry a logical conclusion.

## Connections

- **Explained by conversational implicature.** The fallacy mistakes Grice's Quantity implicature from "some" to "not all" for a logical implication.[^s1][^s3]
- **Contrasts with the existential fallacy.** The Fallacy Files notes that chaining "all S are P" to "some S are P" (the existential step) and then to "some S are not P" yields a contradiction, which shows at least one step is invalid; the existential fallacy covers the first step, and unwarranted contrast covers the second.[^s1]
- **Introduced in the *Cambridge Dictionary of Philosophy*.** W. Kent Wilson's entry on formal fallacy is the source the Fallacy Files cites for the name.[^s1]
- **Studied in pragmatics.** Experimental pragmatics measures when and how people draw the scalar inference that the fallacy depends on.[^s4][^s5]
- **Related to the square of opposition.** I and O are subcontraries, which can both be true, so neither follows from the other.[^s2]

## Sources

[^s1]: G. N. Curtis, "Some Are/Some Are Not", The Fallacy Files. https://fallacyfiles.org/somernot.html (accessed 2026-11-15)
[^s2]: T. Parsons (rev. G. Ciola), "The Traditional Square of Opposition", Stanford Encyclopedia of Philosophy, substantive revision 2025. https://plato.stanford.edu/ENTRIES/square/ (accessed 2026-11-15)
[^s3]: W. Davis, "Implicature", Stanford Encyclopedia of Philosophy, substantive revision 2024. https://plato.stanford.edu/ENTRIES/implicature/ (accessed 2026-11-15)
[^s4]: L. Bott and I. A. Noveck, "Some utterances are underinformative: The onset and time course of scalar inferences", *Journal of Memory and Language* 51(3), 437–457 (2004), Cardiff University ORCA record. https://orca.cardiff.ac.uk/id/eprint/3267/ (accessed 2026-11-15)
[^s5]: I. A. Noveck, "When children are more logical than adults: Experimental investigations of scalar implicature", *Cognition* 78(2), 165–188 (2001), announcement in the Relevance Theory Online Bibliographic Service, UCL. https://www.phon.ucl.ac.uk/home/relevance/relevance_archives/0112.html (accessed 2026-11-15)
