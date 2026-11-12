---
id: ct:sorites-paradox
type: Concept
title: Sorites paradox
aliases: [paradox of the heap, heap paradox, little-by-little argument]
domain: philosophy-of-reasoning
summary: >-
  The ancient puzzle in which a chain of individually plausible small steps
  ("removing one grain cannot turn a heap into a non-heap") leads by valid
  reasoning from a clearly true starting point to a clearly false conclusion;
  it arises from tolerant, vague predicates and tests how logic should handle
  borderline cases.
level: intermediate
evidenceStatus: normative
broader: [ct:paradox]
related: [ct:slippery-slope, ct:line-drawing-fallacy, ct:bright-line-rule, ct:chrysippus, ct:stoic-logic, ct:liar-paradox, ct:precising-definition, ct:deductive-reasoning]
requires: [ct:vagueness, ct:modus-ponens]
relations:
  - {predicate: explainedBy, object: ct:vagueness, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:eubulides, source: s1, confidence: high}
  - {predicate: studiedIn, object: ct:philosophy-of-language, source: s1, confidence: high}
  - {predicate: formalizedBy, object: ct:fuzzy-logic, source: s1, confidence: medium}
  - {predicate: studiedIn, object: ct:experimental-philosophy, source: s3, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Sorites Paradox"
    publisher: Stanford Encyclopedia of Philosophy (Hyde & Raffman, rev. 2025)
    url: https://plato.stanford.edu/entries/sorites-paradox/
    type: scholarly-encyclopedia
    accessed: 2026-11-12
  - id: s2
    title: "11.3: Drawing the Line"
    publisher: "Critical Reasoning: A User's Manual (Southworth & Swoyer), Humanities LibreTexts"
    url: https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/Critical_Reasoning%3A_A_User's_Manual_(Southworth_and_Swoyer)/11%3A_Fallacies-_Common_Ways_of_Reasoning_Badly/11.03%3A_Drawing_the_Line
    type: textbook
    accessed: 2026-11-12
  - id: s3
    title: "Vagueness, Logic and Use: Four Experimental Studies on Vagueness"
    publisher: Serchuk, Hargreaves & Zach, Mind & Language (2011), author's copy on PhilArchive
    url: https://philarchive.org/archive/SERVLA
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s4
    title: "Vagueness and Order Effects in Color Categorization"
    publisher: Egré, de Gardelle & Ripley, Journal of Logic, Language and Information 22, 391-420 (2013)
    url: https://link.springer.com/doi/10.1007/s10849-013-9183-7
    type: peer-reviewed
    accessed: 2026-11-12
created: 2026-11-12
---

# Sorites paradox

The sorites paradox is an argument that marches from an obviously true premise, through a long series of premises that each look harmless, to an obviously false conclusion.[^s1] In the classic version, one grain of sand is not a heap; adding a single grain to something that is not a heap never makes it a heap; so a million grains are not a heap.[^s1] Every step seems acceptable and the logic seems valid, yet the conclusion is absurd, so something we accept about language, truth or logic has to give.[^s1] For critical thinkers it is the formal skeleton behind many "just one more" arguments in budgets, policies and personal resolutions.

## Origin

The name comes from the Greek *soros*, "heap", and the puzzle is usually credited to the Megarian philosopher Eubulides in the fourth century BC; modern restatements often run the same steps with hairs on a balding head.[^s1] Ancient sceptics then used it as a weapon against Stoic claims to knowledge, and Hyde and Raffman list the Stoic logician Chrysippus as an early holder of the view that vague words have sharp but unknowable boundaries.[^s1] After antiquity the puzzle drew little attention until the late nineteenth century; in 1908 the Marxist writer Plekhanov cited it against classical logic.[^s1] Modern work took off in the 1970s with Crispin Wright's analysis of tolerance, Kit Fine's 1975 supervaluationism and Michael Dummett's 1975 claim that vague observational predicates are incoherent.[^s1]

## How it works

Hyde and Raffman distinguish several versions.[^s1] The **conditional sorites** chains thousands of modus ponens steps ("if 1 grain is not a heap, 2 grains are not; if 2 are not, 3 are not…"). The **mathematical-induction sorites** compresses those steps into one universal premise: for every *n*, if *n* grains are not a heap, *n*+1 grains are not. The **line-drawing sorites** runs in reverse: since one grain is not a heap and a million are, the least-number principle says there is some exact number where heaps begin, which seems equally incredible. The **forced march** is the conversational version, in which a speaker is walked through the series and asked to classify each case in turn.[^s1]

What powers every version is **tolerance**: a vague predicate such as "heap", "tall" or "late" seems to keep applying across a change too small to matter.[^s1] The same reasoning can also run upward, appearing to show that any number of grains, even one, makes a heap.[^s1]

A workplace example: a project lead accepts a change request because one extra day of work cannot turn an on-schedule project into a late one. The next request gets the same reasoning, and so on. Each step is defended by tolerance, yet thirty such steps later the project is plainly late. Hyde and Raffman describe everyday cousins of this pattern, such as the dieter who reasons that one more snack makes no difference.[^s1]

## How to apply it

- **Recognise the structure.** When an argument says "this small step changes nothing, so the next one cannot either", ask whether the steps accumulate.[^s1]
- **Keep the clear cases.** Lacking a sharp boundary does not erase the difference between the ends: 2 p.m. is day and 2 a.m. is night, and that difference survives the dusk.[^s2]
- **Don't accept an arbitrary line as just any line.** An imprecise boundary does not make every proposed boundary equally good.[^s2]
- **Sharpen where stakes require it.** Set an explicit threshold (a change budget, a deadline, a cap) when a decision cannot tolerate drift, while recognising that demanding precision everywhere is impractical.[^s2]

## Evidence and limitations

The paradox itself is a logical puzzle, so its status is normative; there is no agreed solution.[^s1] Epistemicists (Williamson, Sorensen, and arguably Chrysippus) keep classical logic and say there is a sharp cutoff we cannot know; supervaluationists say the argument is valid but unsound because the tolerance premise is not true on every sharpening; degree theorists, building on fuzzy logic, let premises be nearly but not fully true so small losses add up; contextualists such as Kamp and Raffman say the tolerance premise is false but seems true because the boundary shifts as we move along the series.[^s1]

Experimental work tests the psychological claims these theories make. Serchuk, Hargreaves and Zach surveyed several hundred undergraduates and found, among other things, that a conjunctive version of the tolerance premise favoured by some fuzzy-logic theorists was not judged more persuasive than the plain conditional version; they caution that such data constrain theories only when studies are carefully designed.[^s3] Contextualist accounts predicted hysteresis, a tendency to keep the starting label longer during a forced march, but Egré, de Gardelle and Ripley found the opposite in colour-categorisation tasks: participants switched categories earlier, an effect they call enhanced contrast.[^s4] These results are small and task-specific, so they inform rather than settle the debate.[^s3][^s4]

## Connections

- **Explained by** vagueness: the paradox exists only because predicates like "heap" tolerate tiny changes and have borderline cases.[^s1]
- **Introduced by** Eubulides of Megara, to whom the ancient heap puzzle is usually attributed.[^s1]
- **Studied in** philosophy of language and philosophical logic, where the rival theories of vague predicates are developed.[^s1]
- **Formalized by** fuzzy and other many-valued logics, which model the creep of small truth losses along the series.[^s1]
- **Studied in** experimental philosophy, which tests how ordinary speakers actually judge the tolerance premise and borderline cases.[^s3]
- **Related to** the slippery slope and the line-drawing fallacy, which misuse the same gray zone; the bright-line rule and precising definitions, which stop the slide by fixing a boundary; Chrysippus and Stoic logic, which engaged it in antiquity; and the liar paradox, which some theorists treat in a unified way.[^s1][^s2]

## Sources

[^s1]: D. Hyde & D. Raffman, "Sorites Paradox", Stanford Encyclopedia of Philosophy (rev. 2025). https://plato.stanford.edu/entries/sorites-paradox/ (accessed 2026-11-12)
[^s2]: J. Southworth & C. Swoyer, "11.3: Drawing the Line", *Critical Reasoning: A User's Manual*, Humanities LibreTexts. https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/Critical_Reasoning%3A_A_User's_Manual_(Southworth_and_Swoyer)/11%3A_Fallacies-_Common_Ways_of_Reasoning_Badly/11.03%3A_Drawing_the_Line (accessed 2026-11-12)
[^s3]: P. Serchuk, I. Hargreaves & R. Zach, "Vagueness, Logic and Use: Four Experimental Studies on Vagueness", *Mind & Language* (2011), author's copy. https://philarchive.org/archive/SERVLA (accessed 2026-11-12)
[^s4]: P. Egré, V. de Gardelle & D. Ripley, "Vagueness and Order Effects in Color Categorization", *Journal of Logic, Language and Information* 22, 391-420 (2013). https://link.springer.com/doi/10.1007/s10849-013-9183-7 (accessed 2026-11-12)
