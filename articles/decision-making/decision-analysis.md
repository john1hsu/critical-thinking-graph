---
id: ct:decision-analysis
type: Method
title: Decision analysis
aliases: [applied decision theory, prescriptive decision analysis]
domain: decision-making
summary: >-
  A prescriptive method for hard choices that breaks a decision into its
  alternatives, uncertainties and values, models them explicitly with tools such
  as decision trees, probabilities and utilities, and uses the model to find the
  alternative with the highest expected utility and to show which factors drive it.
level: intermediate
evidenceStatus: mixed
broader: [ct:decision-theory, ct:judgment-and-decision-making]
related: [ct:value-focused-thinking, ct:expected-value, ct:expected-utility-theory, ct:calibration, ct:reversible-and-irreversible-decisions, ct:bayesian-reasoning]
requires: [ct:expected-value, ct:conditional-probability]
relations:
  - {predicate: introducedBy, object: ct:ronald-howard, source: s4, confidence: high}
  - {predicate: introducedIn, object: ct:decision-analysis-applied-decision-theory, source: s2, confidence: medium}
  - {predicate: influencedBy, object: ct:howard-raiffa, source: s3, confidence: high}
  - {predicate: influencedBy, object: ct:expected-utility-theory, source: s5, confidence: high}
  - {predicate: challengedBy, object: ct:hubbard-samuelson-2009-analysis-placebos, source: s6, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Decision Analysis: An Overview"
    publisher: "Operations Research 30(5), 803-838 (Ralph L. Keeney, 1982), Harvard Center for Health Decision Science repository record"
    url: https://repository.chds.hsph.harvard.edu/repository/2711/
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s2
    title: "The Emergence of Decision Analysis"
    publisher: "Ralph F. Miles Jr., in Edwards, Miles & von Winterfeldt (eds.), Advances in Decision Analysis, Cambridge University Press, 2007"
    url: https://www.cambridge.org/core/books/abs/advances-in-decision-analysis/emergence-of-decision-analysis/D17E93A6C613140B8AD1365B362F70B1
    type: textbook
    accessed: 2026-11-14
  - id: s3
    title: "Decision Analysis: A Personal Account of How It Got Started and Evolved"
    publisher: "Howard Raiffa, in Edwards, Miles & von Winterfeldt (eds.), Advances in Decision Analysis, Cambridge University Press, 2007"
    url: https://cambridge.org/core/books/advances-in-decision-analysis/decision-analysis-a-personal-account-of-how-it-got-started-and-evolved/149F8E2B27B9FE17E58800B290815E18
    type: primary
    accessed: 2026-11-14
  - id: s4
    title: "Ronald A. Howard: Brief Biography"
    publisher: "INFORMS, History of O.R. Excellence biographical profiles"
    url: https://www.informs.org/Explore/History-of-O.R.-Excellence/Biographical-Profiles/Howard-Ronald-A
    type: institutional
    accessed: 2026-11-14
  - id: s5
    title: "Decision Theory and Decision Analysis (course slides)"
    publisher: "Marek J. Druzdzel, Faculty of Computer Science, Bialystok University of Technology"
    url: https://www.aragorn.wi.pb.edu.pl/~druzdzel/decision_theory/07%20Decision%20Theory%20and%20Decision%20Analysis.pdf
    type: academic
    accessed: 2026-11-14
  - id: s6
    title: "Analysis Placebos"
    publisher: "Douglas W. Hubbard & Douglas A. Samuelson, INFORMS Analytics, 7 December 2009"
    url: https://pubsonline.informs.org/do/10.1287/LYTX.2009.06.10/full/
    type: institutional
    accessed: 2026-11-14
created: 2026-11-14
---

# Decision analysis

Decision analysis is a prescriptive method for making hard choices on purpose rather than by feel. It takes a decision apart into three ingredients: the alternatives on offer, the uncertainties that will shape how they turn out, and the values by which outcomes are judged. It models each ingredient explicitly and then puts them back together to see which alternative is best and why.[^s1][^s5] Ralph Keeney's classic overview describes it as a formalisation of common sense for problems too complex to handle informally. More technically, it is a set of logical axioms plus systematic procedures that follow from them.[^s1] Where descriptive research reports how people actually decide, decision analysis is the applied, normative side: an aid to judgment, much as a calculator aids arithmetic.[^s5]

## Origin

The discipline grew out of post-war statistical decision theory. Howard Raiffa traces his path from operations research, through von Neumann and Morgenstern's game theory and Wald's statistical decision theory, to Leonard Savage's subjectivist *Foundations of Statistics* (1954). That route led to *Applied Statistical Decision Theory* (1961), written with Robert Schlaifer, and to Raiffa's *Decision Analysis* (1968), the first book on the subject.[^s3] Ronald Howard of Stanford gave the field its name. After teaching decision theory to General Electric staff, he spent a year applying it to real problems. He presented the result at a Boston conference in 1965, choosing "decision analysis" over "decision engineering".[^s4] Ralph Miles places the formal naming in Howard's 1966 paper, which joined decision theory to systems analysis, and treats the field as something distinct from both decision theory and operations research.[^s2] Howard founded a decision analysis group at SRI International in 1966, which became the consulting firm Strategic Decisions Group in 1980. In 1981 he and James Matheson introduced influence diagrams.[^s4] Raiffa and Keeney's *Decisions with Multiple Objectives* (1976) laid much of the groundwork for how the field is practised today.[^s3]

## How it works

Keeney names five features that make a decision hard enough to need analysis: several objectives, a choice among alternatives, consequences that differ by alternative, uncertainty about those consequences, and outcomes the decision maker does not value equally.[^s1] The method answers each feature with a model:

- **Structure.** Alternatives, uncertain events and outcomes are laid out in a decision tree or a more compact influence diagram.[^s5][^s4]
- **Uncertainty.** Each uncertain event gets a probability, ideally elicited carefully from experts or estimated from data.[^s5]
- **Values.** Outcomes are scored with a utility function that captures trade-offs between objectives and the decision maker's attitude to risk. Plain expected money is not enough, as the St Petersburg paradox shows.[^s5]
- **Evaluation.** The alternative with the highest expected utility is identified. Sensitivity analysis then shows which inputs actually change the recommendation, and value-of-information analysis asks what it would be worth to learn more before deciding.[^s5]

Workplace example: a manufacturer must decide whether to launch a new product nationally now or run a regional pilot first. The decision tree has three branches: launch now, pilot then decide, or drop the product. Demand is the key uncertainty, and the sales team's estimates are turned into probabilities for strong, moderate and weak demand. The analysis might show that launching now has the highest expected profit but carries a real chance of a loss the firm could not absorb, and the utility function counts that risk. Sensitivity analysis shows the choice hinges almost entirely on the probability of weak demand. Value-of-information analysis then shows that the pilot is worth its cost, because it reduces exactly that uncertainty.[^s1][^s5]

## How to apply it

1. **Frame the decision.** State what is being decided, the objectives that matter and the realistic alternatives. Draft objectives before alternatives, so the list of options is not limited to the obvious ones.[^s1][^s3]
2. **Model uncertainty explicitly.** Draw the tree or influence diagram and attach elicited probabilities rather than single-point guesses.[^s5]
3. **Model preferences.** Make trade-offs and risk attitude explicit, using multi-attribute utility when there are several objectives.[^s3][^s5]
4. **Evaluate, then probe.** Compute expected utilities, then run sensitivity and value-of-information analysis. The aim is insight, not a number to obey.[^s5]

Use it for high-stakes, uncertain, non-routine choices with several objectives. The pitfalls are false precision, too much time spent modelling minor branches, and treating the output as the answer rather than as a guide to what matters.[^s1][^s6]

## Evidence and limitations

The method's normative logic is well established, since it follows from the axioms of expected-utility theory.[^s1][^s5] Behavioural research gives a reason to use it: people are better at supplying and coding pieces of information than at integrating them, and simple models often beat unaided expert judgment.[^s5] Direct evidence that decision analysis improves real outcomes is thinner. Robert Clemen (2008) distinguished *strong effectiveness*, meaning better outcomes, from *weak effectiveness*, meaning users are satisfied with the process. He noted that almost no research had compared decision analysis with other methods on strong effectiveness.[^s6] Hubbard and Samuelson (2009) warn that satisfaction and confidence can act as "analysis placebos". They cite a study in which users of one multi-criteria method felt more satisfied without making better choices. They also argue that some components, such as calibrated probability estimates, decomposition and Monte Carlo modelling, do have outcome evidence.[^s6] The status is therefore **mixed**: the method is sound in principle, its parts are partly validated, and evidence that whole analyses improve real decisions is limited.

## Connections

- **Introduced by Ronald Howard**, who named and first presented the discipline in 1965–66[^s4], and set out in his 1966 paper "Decision Analysis: Applied Decision Theory".[^s2]
- **Influenced by Howard Raiffa**, whose Bayesian decision theory with Schlaifer and whose 1968 book shaped the field.[^s3]
- **Influenced by expected-utility theory**, the normative theory it puts into practice by choosing the option with the highest expected utility.[^s5]
- **Challenged by** Hubbard and Samuelson's "analysis placebo" critique, which asks for outcome-based evidence rather than user satisfaction.[^s6]
- **Related to value-focused thinking**, Keeney's objectives-first way of structuring the framing step,[^s1] and to calibration, since its probabilities are only as good as the forecasters supplying them.[^s6]

## Sources

[^s1]: Keeney, "Decision Analysis: An Overview", *Operations Research* 30(5), 1982. https://repository.chds.hsph.harvard.edu/repository/2711/ (accessed 2026-11-14)
[^s2]: Miles, "The Emergence of Decision Analysis", in *Advances in Decision Analysis*, Cambridge University Press, 2007. https://www.cambridge.org/core/books/abs/advances-in-decision-analysis/emergence-of-decision-analysis/D17E93A6C613140B8AD1365B362F70B1 (accessed 2026-11-14)
[^s3]: Raiffa, "Decision Analysis: A Personal Account of How It Got Started and Evolved", in *Advances in Decision Analysis*, Cambridge University Press, 2007. https://cambridge.org/core/books/advances-in-decision-analysis/decision-analysis-a-personal-account-of-how-it-got-started-and-evolved/149F8E2B27B9FE17E58800B290815E18 (accessed 2026-11-14)
[^s4]: INFORMS, "Ronald A. Howard: Brief Biography". https://www.informs.org/Explore/History-of-O.R.-Excellence/Biographical-Profiles/Howard-Ronald-A (accessed 2026-11-14)
[^s5]: Druzdzel, "Decision Theory and Decision Analysis", course slides, Bialystok University of Technology. https://www.aragorn.wi.pb.edu.pl/~druzdzel/decision_theory/07%20Decision%20Theory%20and%20Decision%20Analysis.pdf (accessed 2026-11-14)
[^s6]: Hubbard & Samuelson, "Analysis Placebos", INFORMS *Analytics*, 2009. https://pubsonline.informs.org/do/10.1287/LYTX.2009.06.10/full/ (accessed 2026-11-14)
