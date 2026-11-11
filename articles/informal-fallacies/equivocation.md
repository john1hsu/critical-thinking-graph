---
id: ct:equivocation
type: InformalFallacy
title: Equivocation
aliases: [fallacy of equivocation, equivocal argument, semantic equivocation, homonymy fallacy]
domain: informal-fallacies
summary: >-
  The fallacy of letting a word or phrase that occurs more than once in an
  argument shift its meaning between occurrences, so that each premise is
  plausible on one reading but the conclusion follows only if both readings
  are treated as one.
level: introductory
evidenceStatus: normative
broader: [ct:informal-fallacy]
related: [ct:ambiguity, ct:amphiboly, ct:fallacy-of-four-terms, ct:ambiguous-middle-term, ct:pragma-dialectics, ct:principle-of-charity, ct:douglas-walton, ct:richard-whately, ct:precising-definition]
requires: [ct:argument, ct:ambiguity]
relations:
  - {predicate: introducedIn, object: ct:sophistical-refutations, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:aristotle, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:amphiboly, source: s1, confidence: high}
  - {predicate: instanceOf, object: ct:fallacy-of-ambiguity, source: s1, confidence: high}
  - {predicate: studiedIn, object: ct:argumentation-theory, source: s3, confidence: medium}
criticalQuestions:
  - Which key term appears more than once, and can it be replaced by the same precise paraphrase every time it occurs?
  - Under the reading that makes the first premise true, is the second premise still true?
  - Does the conclusion follow only if two different senses of the term are treated as one?
  - Is there a reasonable general reading of the term under which all the premises can be defended, so that the charge of equivocation would be unfair?
argumentMap:
  premises:
    - "The analyst role requires experience with the company's reporting database."
    - "This candidate has experience with the reporting database: they completed a one-hour vendor tutorial on it."
  conclusion: "This candidate meets the analyst role's experience requirement."
  verdict: fallacious
  objections:
    - "In the job requirement, 'experience' means sustained hands-on work on real reports; in the second premise it means any exposure at all."
    - "Read with one sense throughout, either the second premise is false or the conclusion no longer follows."
sameAs: []
sources:
  - id: s1
    title: "Fallacies"
    publisher: Stanford Encyclopedia of Philosophy (Hansen, rev. 2024)
    url: https://plato.stanford.edu/ENTRIES/fallacies/
    type: scholarly-encyclopedia
    accessed: 2026-11-11
  - id: s2
    title: "New Dialectical Rules for Ambiguity"
    publisher: Informal Logic 20(3), 261-274 (Walton, 2000), journal PDF via Distant Reader
    url: https://distantreader.org/stacks/journals/il/il-2280.pdf
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s3
    title: "The Use of Ambiguous Expressions in Discussions"
    publisher: ISSA Proceedings 1998 (van Laar, University of Groningen), Rozenberg Quarterly
    url: https://rozenbergquarterly.com/?p=14051
    type: academic
    accessed: 2026-11-11
  - id: s4
    title: "3.1.4: Equivocation"
    publisher: "Logical Reasoning (Dowden, California State University Sacramento), Humanities LibreTexts"
    url: https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/Logical_Reasoning_(Dowden)/03%3A_Writing_with_the_Appropriate_Precision/3.01%3A_Being_Ambiguous/3.1.04%3A_Equivocation
    type: textbook
    accessed: 2026-11-11
  - id: s5
    title: "Fallacies Arising from Ambiguity"
    publisher: Springer, Applied Logic Series vol. 1 (Walton, 1996)
    url: https://link.springer.com/978-0-7923-4100-0
    type: primary
    accessed: 2026-11-11
created: 2026-11-11
---

# Equivocation

Equivocation is the fallacy of exploiting the ambiguity of a word or phrase that occurs at least twice in an argument, so that it carries one meaning in one place and another meaning elsewhere.[^s1] Dowden's textbook describes it as illegitimately switching a term's meaning partway through the reasoning.[^s4] The result can look valid on the page: the same word links premise and conclusion, but the ideas behind the word do not. A stock example plays on "end": the end of a thing is its purpose, the end of life is death, so death is the purpose of life; the first "end" means goal and the second means termination.[^s1]

## Origin

Equivocation heads the list of fallacies Aristotle catalogued in *On Sophistical Refutations*. He split thirteen sophistical refutations into those that depend on language (*in dictione*) and those that do not, and equivocation is the first of the six language-dependent ones, alongside amphiboly, combination, division, accent and form of expression.[^s1] Aristotle regarded arguments that turn on names as the commonest source of merely apparent refutations, because there are more things than names.[^s1] Hansen notes that equivocation and amphiboly are the two items from that list that survive in modern textbooks much as Aristotle understood them: equivocation is semantic, word-level ambiguity, amphiboly syntactic.[^s1]

Later logicians disagreed about where it belongs. Whately in the nineteenth century classed fallacies trading on an ambiguous middle term as "semi-logical": logical failures that can only be detected with knowledge of the subject matter; Copi later moved the fallacies of ambiguity, equivocation first, under the informal heading, which Hansen observes leaves a fallacy that is at bottom a logical failure sitting among informal ones.[^s1] Walton gave the topic a book-length treatment, *Fallacies Arising from Ambiguity* (1996), with a full chapter on equivocation.[^s5]

## How it works

An equivocal argument usually trades on a word with an everyday sense and a narrower technical or evaluative sense. Dowden's example begins with "discrimination" as the denial of people's rights, then shifts to discrimination as merely noticing differences (picking ripe tomatoes), and concludes that discrimination is too ordinary to worry about.[^s4] Walton discusses an older textbook case built on "law": a statute needs a lawgiver, the regularities of nature are laws, so nature has a lawgiver. Each premise is plausible only on a different reading of "law", so the argument fails even though it can seem valid to someone who does not notice the shift.[^s2]

The argument map above shows a workplace version. A job requirement asks for "experience" with a reporting database, meaning sustained practical work; a recruiter's note counts a one-hour tutorial as experience. Each premise sounds true on its own reading, but on any single reading either the second premise is false or the conclusion does not follow. Van Laar's analysis of a similar case with "obligatory" (legally versus morally) makes the same point: on one reading a premise is unacceptable, on the other the conclusion does not follow.[^s3]

Van Laar argues that the dangerous cases involve polysemy, related senses of one word, more than clean homonymy such as "bank". Unrelated senses are easy to spot and rarely mislead, whereas related senses allow a broad reading that seems to cover both, so the shift slips past an attentive listener.[^s3]

## How to spot it

- Mark every term that appears in more than one premise, or in a premise and the conclusion, especially words with both an everyday and a technical meaning.[^s4]
- Write a precise paraphrase for the term at its first occurrence and substitute it everywhere. If a premise turns false or the conclusion stops following, the argument equivocates.[^s4]
- Be suspicious when an argument looks valid, its premises sound true, yet its conclusion is surprising or plainly false; a hidden shift of meaning is a common cause, and in a syllogism it produces four terms rather than three.[^s1]
- Do not over-apply the label. Dowden notes that the reasonable default is to assume a repeated term means the same thing unless there is a reason to think otherwise.[^s4] Walton holds a standing presumption that ambiguity is not in itself fallacious and that each case must be judged on its evidence.[^s2]

## How to counter it

Pragma-dialectics treats equivocation as breaking the discussion rule that formulations should be clear and unambiguous, so the remedy is procedural.[^s1] Van Laar describes two moves for the listener: *distinguo*, stating which sense you accept in each premise, and the stronger charge of equivocation, which obliges you to show how the argument misleads.[^s3] The arguer may then pick one sense and defend the premise that was doubted under it, argue that the premises hold on every reading, or stipulate a definition, though stipulating against ordinary usage has its own costs.[^s3] Walton proposes rules for deciding which meaning a term carries in context, drawing on Grice's maxims of cooperative conversation and on principles used to interpret legal and religious texts.[^s2] In workplace writing, the simplest prevention is to define load-bearing terms (critical, experience, available, complete) where policies and contracts first use them.

## Connections

- **Introduced in** *Sophistical Refutations* **and by** Aristotle, as the first of the six fallacies that depend on language.[^s1]
- **Contrasts with** amphiboly: both exploit ambiguity, but equivocation rests on a word's meaning and amphiboly on sentence structure.[^s1]
- **Instance of** the fallacies of ambiguity, Copi's family that also includes amphiboly, accent, composition and division.[^s1]
- **Studied in** argumentation theory, where dialectical accounts such as van Laar's and Walton's evaluate it by what a discussant can reasonably defend rather than by form alone.[^s2][^s3]
- **Related** to the fallacy of four terms (its syllogistic shape), the ambiguous middle term Whately analysed, and the principle of charity, which asks critics to prefer a defensible reading before alleging equivocation.[^s1][^s4]

## Sources

[^s1]: H. Hansen, "Fallacies", Stanford Encyclopedia of Philosophy (rev. 2024). https://plato.stanford.edu/ENTRIES/fallacies/ (accessed 2026-11-11)
[^s2]: D. Walton, "New Dialectical Rules for Ambiguity", Informal Logic 20(3) (2000), 261-274. https://distantreader.org/stacks/journals/il/il-2280.pdf (accessed 2026-11-11)
[^s3]: J. A. van Laar, "The Use of Ambiguous Expressions in Discussions", ISSA Proceedings 1998, Rozenberg Quarterly. https://rozenbergquarterly.com/?p=14051 (accessed 2026-11-11)
[^s4]: B. Dowden, "3.1.4: Equivocation", *Logical Reasoning*, Humanities LibreTexts. https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/Logical_Reasoning_(Dowden)/03%3A_Writing_with_the_Appropriate_Precision/3.01%3A_Being_Ambiguous/3.1.04%3A_Equivocation (accessed 2026-11-11)
[^s5]: D. Walton, *Fallacies Arising from Ambiguity*, Applied Logic Series 1, Springer (1996). https://link.springer.com/978-0-7923-4100-0 (accessed 2026-11-11)
