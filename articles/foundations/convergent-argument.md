---
id: ct:convergent-argument
type: Concept
title: Convergent argument
aliases: [convergent support, convergent reasoning structure, independent-reasons argument]
domain: foundations
summary: >-
  An argument structure in which two or more reasons each give independent
  support to the same conclusion, so that losing one reason weakens but does
  not cancel the others; it is contrasted with a linked argument, whose
  premises support the conclusion only jointly.
level: introductory
evidenceStatus: normative
broader: [ct:argument]
related: [ct:conductive-argument, ct:argument-mapping, ct:argument-evaluation, ct:argument-reconstruction, ct:monroe-beardsley, ct:pragma-dialectics]
requires: [ct:argument]
relations:
  - {predicate: introducedBy, object: ct:monroe-beardsley, source: s1, confidence: high}
  - {predicate: introducedIn, object: ct:practical-logic, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:linked-argument, source: s2, confidence: high}
  - {predicate: confusedWith, object: ct:multiple-argumentation, source: s2, confidence: high}
  - {predicate: studiedIn, object: ct:informal-logic, source: s3, confidence: high}
  - {predicate: formalizedBy, object: ct:aspic-plus, source: s5, confidence: medium}
sources:
  - id: s1
    title: "The Linked-Convergent Distinction"
    publisher: "ISSA Proceedings 2014 (David Hitchcock, McMaster University), reprinted by Rozenberg Quarterly"
    url: https://rozenbergquarterly.com/issa-proceedings-2014-the-linked-convergent-distinction/?print=pdf
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s2
    title: "Argument Structure and Disciplinary Perspective"
    publisher: "ISSA Proceedings 1998 (James B. Freeman, Hunter College CUNY), reprinted by Rozenberg Quarterly"
    url: https://rozenbergquarterly.com/issa-proceedings-1998-argument-structure-and-disciplinary-perspective/?print=pdf
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s3
    title: "Walton on Argument Structure"
    publisher: "Informal Logic 27(1), 5-25 (G. C. Goddu, 2007)"
    url: https://distantreader.org/stacks/journals/il/il-462.pdf
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s4
    title: "Against Making the Linked-Convergent Distinction"
    publisher: "ISSA Proceedings 2006 (G. C. Goddu, University of Richmond), reprinted by Rozenberg Quarterly"
    url: https://rozenbergquarterly.com/issa-proceedings-2006-against-making-the-linked-convergent-distinction/?print=pdf
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s5
    title: "Defining the Structure of Arguments with AI Models of Argumentation"
    publisher: "Workshop on Computational Models of Natural Argument, CMNA 12 (Bin Wei and Henry Prakken)"
    url: https://cmna.csc.liv.ac.uk/CMNA12/paper_16.pdf
    type: academic
    accessed: 2026-11-17
created: 2026-11-17
---

# Convergent argument

A convergent argument is one in which several reasons bear on the same conclusion, each relevant on its own. If one reason turns out to be false, the others still count for the conclusion, though the case as a whole may be weaker.[^s2] Its opposite is a linked argument, where the premises work only as a team: take one away and the rest no longer give a reason at all, or give a very different one.[^s2][^s5] David Hitchcock argues that the distinction is primarily about the ways two or more reasons can directly support a claim; calling a whole argument "convergent" is a derived use.[^s1]

## Origin

Monroe Beardsley introduced the term "convergent" in his 1950 textbook *Practical Logic*, alongside "divergent" and "serial" structures, and drew each reason with its own arrow to the conclusion.[^s1] Hitchcock notes that Beardsley's definition was ambiguous and that he dropped the concept from later editions.[^s1] Stephen Thomas refined the idea in *Practical Reasoning in Natural Language* (the earliest edition Hitchcock could find is from 1977), coined the contrasting term "linked", and added a diagramming convention for it.[^s1] Michael Scriven drew a similar line in 1976 under the heading of balance-of-considerations reasoning.[^s1] The pair later became a standard section of introductory critical thinking textbooks and a core topic in informal logic, debated by James Freeman, Douglas Walton and others.[^s1][^s3]

## How it works

Freeman illustrates the contrast with a classic textbook case on capital punishment.[^s2] One arguer offers four separate reasons against it: there is no evidence it deters; it cannot restore the life taken; a wrongful execution cannot be redressed; and it signals that brutality is an option for the state. If the deterrence reason were refuted, the other three would still count against the practice. That is convergent support.[^s2]

Compare a two-premise version: capital punishment signals that brutality is an option for the state; brutality must never be an option for the state; so capital punishment must not be permitted. If the first premise were false, the second would give little reason for the conclusion, so the support is linked.[^s2] An everyday example of convergence: a manager argues that a team should adopt a new scheduling tool because it is cheaper, because it integrates with the existing calendar, and because two other teams already use it. Each reason stands on its own; a map would draw three arrows to the conclusion rather than one arrow from a bundled group.[^s1][^s2]

## How to apply it

Several tests have been proposed for telling the structures apart, most of them asking what happens when one premise is removed or shown false.[^s1][^s4]

1. **Falsity test.** Suppose one premise is false. If the others still give the conclusion the same support, the support is convergent; if they are undercut, it is linked. Freeman prefers this test.[^s2]
2. **Suspension tests.** Walton's family of tests asks whether suspending a premise leaves the conclusion with no support or with insufficient support; he treats them as diagnostic indicators to be combined with textual cues (such as "also" or "besides") and context.[^s3]
3. **Evaluate accordingly.** Treating support as convergent means assessing each reason separately and then weighing them together; doing that for linked premises makes no sense, because their strength lies in the combination.[^s1]

A common pitfall is to read a convergent argument as several separate arguments. Freeman insists it is one argument with internally independent reasons, and that it should not be equated with the dialectical notion of "multiple argumentation" in pragma-dialectics, where several distinct defences of a standpoint are offered.[^s2]

## Limitations

The distinction is contested at the level of theory, though not as an empirical finding. Hitchcock lists a series of tests (diminished support, no support, insufficient support and type reduction upon removing a premise) and calls attempts to define linkage that way futile, because one must already have evaluated an argument to classify it.[^s1] He concludes that classification is often a judgment call.[^s1] G. C. Goddu goes further: he shows that the main tests give conflicting verdicts on simple cases, that Walton never says how to resolve clashes between kinds of evidence, and that argument evaluation can proceed without the distinction at all.[^s3][^s4] He also argues that the claimed payoffs (knowing which premises a critic must refute, spotting begged questions, finding unstated premises) depend on context and sufficiency of support rather than on structure.[^s4] Researchers in computational argumentation have responded by recasting the distinction formally; Bin Wei and Henry Prakken use the ASPIC+ framework to separate strict from defeasible inferences and reanalyse some puzzling cases as separate arguments sharing a premise.[^s5]

## Connections

- **Broader: argument.** Convergence is a way the premises of a single argument can be organised.[^s2]
- **Introduced by Monroe Beardsley in *Practical Logic*.** Hitchcock credits the 1950 book with the term.[^s1]
- **Contrasts with linked argument.** Freeman defines the two by whether falsity of one premise undercuts the rest.[^s2]
- **Confused with multiple argumentation.** Freeman separates the logical linked-convergent distinction from the pragma-dialectical distinction between multiple and coordinatively compound argumentation.[^s2]
- **Studied in informal logic.** Goddu's *Informal Logic* paper reviews Walton's tests and the debate over whether the distinction is needed.[^s3]
- **Formalized by ASPIC+.** Wei and Prakken propose defining argument structure with this AI model of argumentation.[^s5]
- **Related to conductive argument and argument mapping.** Conductive arguments weigh convergent reasons, and maps draw independent reasons as separate arrows.[^s1][^s2]

## Sources

[^s1]: Hitchcock, "The Linked-Convergent Distinction", ISSA Proceedings 2014. https://rozenbergquarterly.com/issa-proceedings-2014-the-linked-convergent-distinction/?print=pdf (accessed 2026-11-17)
[^s2]: Freeman, "Argument Structure and Disciplinary Perspective", ISSA Proceedings 1998. https://rozenbergquarterly.com/issa-proceedings-1998-argument-structure-and-disciplinary-perspective/?print=pdf (accessed 2026-11-17)
[^s3]: Goddu, "Walton on Argument Structure", Informal Logic 27(1), 2007. https://distantreader.org/stacks/journals/il/il-462.pdf (accessed 2026-11-17)
[^s4]: Goddu, "Against Making the Linked-Convergent Distinction", ISSA Proceedings 2006. https://rozenbergquarterly.com/issa-proceedings-2006-against-making-the-linked-convergent-distinction/?print=pdf (accessed 2026-11-17)
[^s5]: Wei and Prakken, "Defining the Structure of Arguments with AI Models of Argumentation", CMNA 12. https://cmna.csc.liv.ac.uk/CMNA12/paper_16.pdf (accessed 2026-11-17)
