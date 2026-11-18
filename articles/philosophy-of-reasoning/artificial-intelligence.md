---
id: ct:artificial-intelligence
type: Field
title: Artificial intelligence
aliases: [AI, machine intelligence]
domain: philosophy-of-reasoning
summary: >-
  The field that designs and studies computational agents that perceive their
  environment and act, often by reasoning, learning and deciding under
  uncertainty. For critical thinking it matters both as a source of formal
  models of reasoning (nonmonotonic logic, argumentation frameworks,
  probabilistic inference) and as a producer of claims that need evaluating.
level: introductory
evidenceStatus: mixed
broader: [ct:computer-science]
related: [ct:defeasible-reasoning, ct:argumentation-theory, ct:argumentation-schemes, ct:abstract-argumentation-frameworks, ct:herbert-simon, ct:bounded-rationality, ct:predicate-logic, ct:bayesian-reasoning, ct:logic, ct:douglas-walton]
requires: [ct:reasoning]
relations:
  - {predicate: introducedBy, object: ct:john-mccarthy, source: s5, confidence: medium}
  - {predicate: influencedBy, object: ct:alan-turing, source: s3, confidence: high}
  - {predicate: influencedBy, object: ct:logic, source: s1, confidence: high}
  - {predicate: influencedBy, object: ct:formal-logic, source: s2, confidence: high}
sources:
  - id: s1
    title: "Artificial Intelligence"
    publisher: Stanford Encyclopedia of Philosophy (Selmer Bringsjord and Naveen Sundar Govindarajulu, 2018)
    url: https://plato.stanford.edu/ENTRIES/artificial-intelligence/
    type: scholarly-encyclopedia
    accessed: 2026-11-18
  - id: s2
    title: "Logic-Based Artificial Intelligence"
    publisher: Stanford Encyclopedia of Philosophy (Richmond Thomason, revised 2024)
    url: https://plato.stanford.edu/ENTRIES/logic-ai/
    type: scholarly-encyclopedia
    accessed: 2026-11-18
  - id: s3
    title: "Computing Machinery and Intelligence"
    publisher: Mind 59(236), 1950 (Alan M. Turing; course copy, Princeton University COS 109)
    url: https://www.cs.princeton.edu/courses/archive/fall23/cos109/turingpaper.pdf
    type: primary
    accessed: 2026-11-18
  - id: s4
    title: "Artificial Intelligence: A Modern Approach, preface"
    publisher: Stuart Russell and Peter Norvig, UC Berkeley (textbook companion site)
    url: https://aima.cs.berkeley.edu/preface.html
    type: textbook
    accessed: 2026-11-18
  - id: s5
    title: "Ray Solomonoff and the Dartmouth Summer Research Project in Artificial Intelligence, 1956"
    publisher: Grace Solomonoff (historical paper, Ray Solomonoff archive)
    url: https://www.raysolomonoff.com/dartmouth/dartray.pdf
    type: preprint
    accessed: 2026-11-18
created: 2026-11-18
---

# Artificial intelligence

Artificial intelligence (AI) is the field that tries to build computational systems that perceive, reason, learn and act; the Stanford Encyclopedia notes that it has no single agreed definition.[^s1] Russell and Norvig's standard textbook frames it around the *intelligent agent*: a system that receives percepts from an environment and maps sequences of them to actions, with the right design depending on the task environment.[^s4] The same textbook sorts definitions of AI along two axes, thinking versus acting and human-like versus ideally rational performance, and favours building agents that act rationally.[^s1] For critical thinkers, AI is relevant twice over: its researchers produced precise models of everyday reasoning, and its products now generate claims, summaries and recommendations that people must evaluate.[^s1][^s2]

## Origin

In 1950 Alan Turing argued that "Can machines think?" was too vague to settle and replaced it with an *imitation game*, in which an interrogator exchanges typed messages with a hidden human and a hidden machine.[^s3] He predicted that within about fifty years an average interrogator would have no better than a 70 percent chance of picking out the machine after five minutes, answered nine objections (including Lady Lovelace's claim that machines only do what they are told), and proposed educating a simple "child machine" rather than programming an adult mind.[^s3]

The name came from a 1955 proposal by John McCarthy, Marvin Minsky, Nathaniel Rochester and Claude Shannon for a summer workshop at Dartmouth, built on the conjecture that every feature of intelligence could in principle be described precisely enough for a machine to simulate it.[^s5] The 1956 meeting is where the term was coined, and Allen Newell and Herbert Simon's Logic Theorist, which proved theorems of propositional logic, was one of its highlights.[^s1] The Stanford Encyclopedia adds that the field's roots run much deeper, to Aristotle's syllogistic and to the early probability theory of Pascal.[^s1]

## How it works

Three broad traditions coexist. *Logicist* AI represents knowledge as formulas in a logic, such as first-order logic, and derives actions by inference; *probabilistic* AI uses tools such as Bayesian networks; and *neurocomputational* AI trains artificial neural networks, today mostly through supervised, unsupervised and reinforcement learning.[^s1] Modern systems often combine them.[^s1] Neural networks fell out of favour after Minsky and Papert's 1969 *Perceptrons* and returned in 1986 with backpropagation, and deep learning later produced results such as AlphaGo's 2016 win over a Go champion.[^s1]

The logicist strand is where AI most directly shaped the theory of reasoning. McCarthy's 1959 work set out to formalize commonsense problems such as planning a trip to the airport, and in 1969 McCarthy and Hayes identified the *frame problem*: how to capture, without listing endless axioms, what does not change when an action is taken.[^s2] Because practical reasoning ignores unlikely possibilities and withdraws conclusions when new facts arrive, researchers built nonmonotonic logics; three influential versions appeared in 1980, McDermott and Doyle's modal logic, Reiter's default logic and McCarthy's circumscription.[^s2] Abstract argumentation grew out of the same work, treating default reasoning as a contest among arguments that attack one another.[^s2]

A workplace example shows the idea. A help-desk triage system might hold the default rule "tickets from enterprise customers are urgent" and the exception "test accounts are never urgent". Classical logic would derive a contradiction for an enterprise test account; a default-logic or argumentation system instead lets the more specific argument defeat the general one, and retracts "urgent" once the test-account flag appears. That is the same structure as defeasible human reasoning.[^s2]

## Evidence and limitations

AI's influence on reasoning research is real but contested in scope. Thomason notes that the logicist programme is controversial inside AI itself, since many machine-learning researchers see no need to formalize reasoning at all, and that by the late 1980s probabilistic methods were often preferred for reasoning under uncertainty.[^s2] Nonmonotonic logics also produced surprises: the Yale Shooting anomaly (Hanks and McDermott, mid-1980s) showed that a naive default treatment of inertia licenses an unintended conclusion.[^s2] On the learning side, the Stanford Encyclopedia points to adversarial inputs that fool trained networks and observes that consciousness and creativity remain largely absent from the field's main textbooks.[^s1] Turing's fifty-year prediction and his conversational test are still debated, and passing a short test is not the same as reasoning well.[^s3][^s1]

For practice, treat an AI system's output as testimony from a source whose method you may not know: ask what kind of system produced it (rules, probabilities or learned patterns), what evidence it was built on, and whether the claim survives the critical questions you would put to any other source.[^s1][^s4]

## Connections

AI was **introduced by** John McCarthy and his co-authors in the sense that their 1955 Dartmouth proposal named the field.[^s5] It was **influenced by** Alan Turing, whose 1950 paper posed the question the field took up,[^s3] by **logic**, from which it inherited the syllogism and much of its formal machinery,[^s1] and specifically by **formal logic**, since philosophical logic was the early foundation of logical AI.[^s2] In return, AI is a setting where defeasible reasoning, argumentation theory and Walton-style argumentation schemes are **applied**, through nonmonotonic logics and abstract argumentation frameworks.[^s2] Herbert Simon, co-author of the Logic Theorist, ties the field's history to the study of human problem solving, and its probabilistic strand connects it to Bayesian reasoning.[^s1]

## Sources

[^s1]: Bringsjord and Govindarajulu, "Artificial Intelligence", Stanford Encyclopedia of Philosophy, 2018. https://plato.stanford.edu/ENTRIES/artificial-intelligence/ (accessed 2026-11-18)
[^s2]: Thomason, "Logic-Based Artificial Intelligence", Stanford Encyclopedia of Philosophy, revised 2024. https://plato.stanford.edu/ENTRIES/logic-ai/ (accessed 2026-11-18)
[^s3]: Turing, "Computing Machinery and Intelligence", Mind 59(236), 1950. https://www.cs.princeton.edu/courses/archive/fall23/cos109/turingpaper.pdf (accessed 2026-11-18)
[^s4]: Russell and Norvig, *Artificial Intelligence: A Modern Approach*, preface. https://aima.cs.berkeley.edu/preface.html (accessed 2026-11-18)
[^s5]: G. Solomonoff, "Ray Solomonoff and the Dartmouth Summer Research Project in Artificial Intelligence, 1956". https://www.raysolomonoff.com/dartmouth/dartray.pdf (accessed 2026-11-18)
