---
id: ct:dialectic
type: Method
title: Dialectic
aliases: [dialectical method, dialectical reasoning, art of dialectic, dialectical argument]
domain: argumentation
summary: >-
  Reasoning conducted as an exchange between opposing positions, classically
  a disciplined question-and-answer contest in which a questioner tries to
  draw a respondent's concessions into contradiction; the term later also
  named formal logic (Stoics, medieval schools), Kant's critique of reason
  overreaching itself, Hegel's account of concepts developing through their
  own contradictions, and today's dialogue-based theories of argument.
level: intermediate
evidenceStatus: normative
broader: [ct:argumentation]
related: [ct:aristotle, ct:plato, ct:topics, ct:sophistical-refutations, ct:endoxa, ct:stoic-logic, ct:pragma-dialectics, ct:informal-logic, ct:formal-dialogue-systems, ct:douglas-walton]
requires: [ct:argument]
relations:
  - {predicate: formalizedBy, object: ct:topics, source: s2, confidence: high}
  - {predicate: contrastsWith, object: ct:rhetoric, source: s2, confidence: high}
  - {predicate: appliedIn, object: ct:argumentation-theory, source: s4, confidence: high}
  - {predicate: challengedBy, object: ct:karl-popper, source: s3, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Dialectic (logic)"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/print/article/161174
    type: encyclopedia
    accessed: 2026-11-12
  - id: s2
    title: "Aristotle's Logic"
    publisher: Stanford Encyclopedia of Philosophy (Smith, rev. 2022; Spring 2026 archive)
    url: https://plato.stanford.edu/archives/spr2026/entries/aristotle-logic/
    type: scholarly-encyclopedia
    accessed: 2026-11-12
  - id: s3
    title: "Hegel's Dialectics"
    publisher: Stanford Encyclopedia of Philosophy (Maybee, rev. 2020; Winter 2023 archive)
    url: https://plato.stanford.edu/archives/Win2023/Entries/hegel-dialectics/
    type: scholarly-encyclopedia
    accessed: 2026-11-12
  - id: s4
    title: "Informal Logic"
    publisher: Stanford Encyclopedia of Philosophy (Groarke, rev. 2011; Fall 2016 archive)
    url: https://plato.stanford.edu/archives/fall2016/entries/logic-informal/
    type: scholarly-encyclopedia
    accessed: 2026-11-12
created: 2026-11-12
---

# Dialectic

Dialectic is reasoning carried out between positions rather than inside one head: a claim is put forward, challenged, defended and revised through an exchange of moves. Among the classical Greeks the word covered a technique for refuting an opponent in debate, a method for testing definitions, and a way of sorting general and specific concepts; from the Stoics to the end of the Middle Ages it was largely a name for formal logic; Kant used it for exposing reason's illusions when it overreaches experience; and Hegel and then Marx used it for development driven by internal contradiction.[^s1] For critical thinkers the most useful sense is the oldest and the newest one: argument as a rule-governed dialogue in which views are tested against objections.[^s2][^s4]

## Origin

The art took shape in Plato's Academy, where a stylised exercise pitted an answerer defending a thesis against a questioner seeking yes-or-no concessions that would lead to a contradiction, with judges keeping score.[^s2] Aristotle's *Topics* is the first systematic manual of the practice. On Robin Smith's reading, it supplies two things: a method for finding premises from which a desired conclusion follows, organised around "common" terms such as opposites and "more and less", and an inventory of premises that different kinds of interlocutor are likely to grant; its appendix, *On Sophistical Refutations*, catalogues arguments that only appear to work.[^s2] Aristotle distinguished dialectical arguments from scientific demonstrations not by their logical form but by their premises: demonstration starts from true, primary principles, dialectic from accepted opinions (*endoxa*) that the respondent concedes.[^s2] He called rhetoric dialectic's counterpart, since both persuade from what the audience already accepts.[^s2]

Hegel later recast dialectic as the movement by which a fixed concept proves one-sided, passes into its opposite, and is taken up into a richer concept that cancels and preserves both. The familiar slogan "thesis–antithesis–synthesis" is Fichte's vocabulary, not Hegel's own, and fits his texts poorly.[^s3]

## How it works

Classical dialectic turns on roles. The questioner may only ask; the respondent may only grant or refuse; whatever is granted becomes a premise. A contradiction among the respondent's concessions refutes the thesis. Aristotle's "testing" use of the method rests on the principle that someone who really knows a subject holds consistent beliefs about it, so exposed inconsistency shows a gap in knowledge, which is why the practice resembles, and probably descends from, Socrates' interrogations.[^s2]

A workplace example: a product lead asserts that the team should drop manual QA because automated tests catch everything. A colleague, acting as questioner, asks: Did automated tests run on last quarter's release? (Yes.) Did that release ship a layout bug customers reported? (Yes.) Do our automated tests check visual layout? (No.) The concessions now conflict with "tests catch everything", so the thesis must be narrowed (perhaps to "automated tests catch logic regressions") or defended with new premises. Nothing has been proved about QA in general; the exchange shows only that this set of commitments is inconsistent, which is exactly the limited but valuable result Aristotle attributed to refutation.[^s2]

Modern argumentation theory generalises the structure. Dialectical approaches treat an argument as part of an exchange of positions and counter-positions; pragma-dialectics models a critical discussion through confrontation, opening, argumentation and closing stages, and treats fallacies as violations of its discussion rules.[^s4] Douglas Walton distinguishes dialogue types (persuasion, inquiry, discovery, negotiation, information-seeking, deliberation and eristic quarrel), each with its own goals and norms, so a move acceptable in bargaining can be fallacious in inquiry.[^s4] Ralph Johnson adds that a full argument has a "dialectical tier" answering foreseeable objections and alternative positions, beyond its core of premises and conclusion, though Govier and Hitchcock deny this is necessary for something to count as an argument.[^s4]

## How to apply it

1. **Fix the thesis.** Write the claim under test in one sentence and agree who defends it.[^s2]
2. **Ask for concessions, not speeches.** Pose answerable questions whose answers become shared premises; record them.[^s2]
3. **Look for collisions.** Check whether the granted premises, together, contradict the thesis; if so, the defender must retract a concession or revise the thesis.[^s2]
4. **Name the dialogue type.** Decide whether you are inquiring, deliberating or negotiating, because the permissible moves differ.[^s4]
5. **Build the dialectical tier.** Before finalising a written case, list the strongest objections and answer them.[^s4]

Pitfalls: refutation shows inconsistency, not which belief is false, so a "win" is not a proof of the opposite;[^s2] the format slides into eristic point-scoring if the goal shifts from testing ideas to beating a person;[^s4] and premises drawn from accepted opinion inherit that opinion's errors, as Aristotle's sophistical cases show.[^s2]

## Connections

Aristotle's *Topics* gives dialectic its first systematic, technical treatment, which is why the node is **formalized by** that work, and its appendix *On Sophistical Refutations* treats counterfeit dialectical arguments.[^s2] Dialectic **contrasts with** rhetoric: Aristotle saw them as counterpart arts that both work from accepted premises, one by question and answer with an individual, the other by speech to an audience.[^s2] Dialectic is **applied in** argumentation theory, where pragma-dialectics, Walton's dialogue types and Johnson's dialectical tier are its modern descendants, alongside informal logic.[^s4] Hegelian dialectic is **challenged by** Karl Popper, who held that its tolerance of contradiction would mean the breakdown of science; defenders such as Priest reply that some contradictions can be handled coherently.[^s3] The Socratic method is a narrower form of dialectical questioning, and the Stoic tradition shows the period when "dialectic" simply meant logic.[^s1][^s2]

## Sources

[^s1]: "Dialectic (logic)", Encyclopaedia Britannica. https://www.britannica.com/print/article/161174 (accessed 2026-11-12)
[^s2]: Smith, "Aristotle's Logic", Stanford Encyclopedia of Philosophy (Spring 2026 archive). https://plato.stanford.edu/archives/spr2026/entries/aristotle-logic/ (accessed 2026-11-12)
[^s3]: Maybee, "Hegel's Dialectics", Stanford Encyclopedia of Philosophy (Winter 2023 archive). https://plato.stanford.edu/archives/Win2023/Entries/hegel-dialectics/ (accessed 2026-11-12)
[^s4]: Groarke, "Informal Logic", Stanford Encyclopedia of Philosophy (Fall 2016 archive). https://plato.stanford.edu/archives/fall2016/entries/logic-informal/ (accessed 2026-11-12)
