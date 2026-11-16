---
id: ct:cancellability-test
type: Technique
title: Cancellability test
aliases: [cancelability test, cancellation test, Gricean cancellability test, test of explicit cancellation]
domain: philosophy-of-reasoning
summary: >-
  A diagnostic, from Paul Grice, for telling what a remark merely suggests
  from what it logically commits the speaker to: if the suggested content
  can be explicitly denied ("some passed; indeed, all did") or would be
  absent in some context, without contradiction, it is a conversational
  implicature, not an entailment.
level: intermediate
evidenceStatus: contested
broader: [ct:conversational-implicature]
related: [ct:unwarranted-contrast, ct:pragmatics, ct:logical-consequence, ct:method-of-counterexample, ct:philosophy-of-language, ct:validity]
requires: [ct:logical-consequence]
relations:
  - {predicate: detects, object: ct:unwarranted-contrast, source: s1, confidence: medium}
  - {predicate: introducedBy, object: ct:paul-grice, source: s2, confidence: high}
  - {predicate: studiedIn, object: ct:pragmatics, source: s3, confidence: medium}
  - {predicate: challengedBy, object: ct:weiner-are-all-conversational-implicatures-cancellable, source: s2, confidence: high}
  - {predicate: contrastsWith, object: ct:logical-consequence, source: s1, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Implicature (Summer 2014 edition)"
    publisher: "Stanford Encyclopedia of Philosophy (Wayne Davis)"
    url: https://plato.stanford.edu/archives/sum2014/entries/implicature
    type: scholarly-encyclopedia
    accessed: 2026-11-16
  - id: s2
    title: "Conversational implicature and the cancellability test (Analysis 68(2), 156–160, 2008)"
    publisher: "Michael Blome-Tillmann, author's copy on PhilArchive"
    url: https://philarchive.org/archive/BLOCIA-3
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s3
    title: "On explicatures, cancellability and cancellation (SpringerPlus 5:1115, 2016)"
    publisher: "Grzegorz Walczak, open-access copy via CORE"
    url: https://core.ac.uk/download/205910382.pdf
    type: peer-reviewed
    accessed: 2026-11-16
created: 2026-11-16
---

# Cancellability test

The cancellability test is a way of checking whether a piece of meaning is part of what a sentence logically commits its speaker to, or only something the speaker suggests in context. The idea is simple: try to deny the suggested content right after the remark. If "Some athletes smoke; indeed, all do" is consistent, then "not all athletes smoke" was never entailed by "some athletes smoke"; it was a conversational implicature that the speaker is free to withdraw.[^s1] Entailments cannot be withdrawn that way, because denying them produces a contradiction.[^s1] For critical thinkers, the test is a quick guard against reading a hint as if it were a premise.

## Origin

The test comes from Paul Grice's theory of conversation. Grice held that a genuine conversational implicature must be cancellable, and he described two ways to check this.[^s2] In explicit cancellation, the speaker adds a clause such as "but not Q" or "I don't mean to imply that Q" without contradicting themselves.[^s2] In contextual cancellation, there is some context in which the same words would simply not carry the suggestion.[^s2] Grice paired cancellability with other marks of conversational implicature: nondetachability (another way of saying the same thing carries the same suggestion) and calculability (a listener can work the suggestion out from the cooperative principle and the maxims).[^s1] Cancellability became the most widely used of these diagnostics in philosophy of language and linguistic pragmatics.[^s3]

## How it works

The test relies on the difference between entailment and implicature. Entailment is a logical relation: if what is said is true, the entailed content must be true.[^s1] An implicature rests on assumptions about why the speaker chose these words, so it can be denied without inconsistency.[^s1] Cancellation shows which side of that line a reading falls on.[^s1]

Take a workplace example. A team lead reports, "Some of the trainees passed the certification exam." A manager concludes, "So some of them failed, and we need to budget for retakes." Apply the test: "Some of the trainees passed; actually, all of them passed." The sentence is consistent, so the "some failed" reading was cancellable and the manager's inference went beyond what the report established.[^s3] That is exactly the step the unwarranted-contrast fallacy makes, from "some S are P" to "some S are not P."[^s1]

Reinforcement is the mirror image. Adding "but not all of them" after "some passed" does not sound redundant, which is another sign the "not all" content was not already entailed.[^s1] With entailed content, the reinforcing clause sounds like a repetition and the cancelling clause sounds like a contradiction.[^s1] The SEP entry gives a second illustration: "Bill will visit France or Germany; indeed, he will drive through both" is consistent, which supports treating the exclusive reading of "or" as an implicature, not a second meaning of the word.[^s1]

## How to apply it

1. **Isolate the suggestion.** Write down the extra content you are tempted to rely on ("some failed," "only one option," "the order of events").
2. **Try explicit cancellation.** Append "in fact, not-Q" or "though I don't mean to suggest Q" to the original remark. If the result is consistent, Q was not entailed.[^s2]
3. **Try contextual cancellation.** Imagine a setting where the same words would not carry Q, for example a speaker who says "some" because they checked only a sample. If such a setting exists, Q depends on context.[^s2][^s3]
4. **Decide what to do.** If Q matters to a decision, ask for it to be stated directly or check the underlying data, instead of inferring it from word choice.

**When to use it.** Use it when a conclusion leans on quantity words ("some," "most," "or," "may"), on understatement ("not bad"), or on the order in which events were reported, and especially when reading summaries, audit findings, contracts or survey results. These are the cases where the SEP entry finds cancellable, context-driven readings, such as "some" read as "not all," exclusive "or," and understatement.[^s1]

**Pitfalls.** Passing the test is evidence, not proof. Grice himself allowed that some content that is not a conversational implicature can be cancelled, so other diagnostics are still needed.[^s3] Some implicatures are also entailed by what is said; answering "Did you drive somewhere?" with "I drove to Ithaca" implicates and entails "I drove somewhere."[^s1] Finally, a cancelling clause can be heard as sarcasm, so a failed attempt in one context does not settle the matter.[^s2]

## Evidence and limitations

The test's reliability is debated among philosophers, so its status here is marked contested. In an earlier paper in *Analysis*, as Blome-Tillmann summarises it, Weiner argued that some implicatures cannot be explicitly cancelled. In his train-ride case, a passenger's pointed remark that someone could move over still implies a request even when the speaker disclaims it, because the disclaimer sounds ironic.[^s2] In a 2008 reply in the same journal, Michael Blome-Tillmann granted that not every implicature can be cancelled in every context. He argued that a weaker principle survives: every implicature is explicitly cancellable in some context where it arises, so the test stays usable.[^s2] In a 2016 paper, Grzegorz Walczak defended the test against a different line of criticism, from Capone and from Burton-Roberts, about pragmatically enriched content (explicatures). He argued that cancellation is a thought experiment run by the analyst, not something a speaker must be able to do mid-conversation. On that reading, explicatures pass the test even when saying the cancelling clause aloud would be awkward.[^s3] The practical upshot is modest: cancellability reliably shows that a reading is not a logical consequence, but it does not by itself classify every kind of non-literal meaning.[^s1][^s3]

## Connections

- **Detects unwarranted contrast.** The "not all" reading of "some" can be cancelled ("indeed, all do"), so treating it as a premise is the logical error the fallacy names.[^s1]
- **Introduced by Paul Grice.** Grice proposed explicit and contextual cancellability as conditions any conversational implicature must meet.[^s2]
- **Studied in pragmatics.** Work on explicatures and relevance theory debates what the test can show.[^s3]
- **Challenged by Weiner.** The train-ride counterexample targets explicit cancellability; Blome-Tillmann's reply restricts the principle without giving it up.[^s2]
- **Contrasts with logical consequence.** Entailed content cannot be cancelled without contradiction; implicated content can.[^s1]
- **Related to the method of counterexample.** Both show an inference is not guaranteed by describing a case where the premise holds and the suggested conclusion fails.[^s1]

## Sources

[^s1]: W. Davis, "Implicature", Stanford Encyclopedia of Philosophy, Summer 2014 edition. https://plato.stanford.edu/archives/sum2014/entries/implicature (accessed 2026-11-16)
[^s2]: M. Blome-Tillmann, "Conversational implicature and the cancellability test", *Analysis* 68(2), 156–160 (2008), author's copy on PhilArchive. https://philarchive.org/archive/BLOCIA-3 (accessed 2026-11-16)
[^s3]: G. Walczak, "On explicatures, cancellability and cancellation", *SpringerPlus* 5:1115 (2016), open-access copy via CORE. https://core.ac.uk/download/205910382.pdf (accessed 2026-11-16)
