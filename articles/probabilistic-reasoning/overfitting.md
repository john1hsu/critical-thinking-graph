---
id: ct:overfitting
type: Phenomenon
title: Overfitting
aliases: [overfit model, fitting the noise]
domain: probabilistic-reasoning
summary: >-
  Fitting a model, rule or explanation so closely to the data at hand that it
  captures sample-specific noise as if it were signal, so that it fits the past
  well but predicts new cases poorly.
level: intermediate
evidenceStatus: robust
broader: [ct:statistical-reasoning]
related: [ct:occams-razor, ct:take-the-best, ct:fast-and-frugal-heuristics, ct:ecological-rationality, ct:weighted-additive-rule, ct:p-hacking, ct:researcher-degrees-of-freedom, ct:ad-hoc-hypothesis, ct:hasty-generalization]
requires: []
relations:
  - {predicate: explainedBy, object: ct:bias-variance-tradeoff, source: s2, confidence: high}
  - {predicate: studiedIn, object: ct:statistics, source: s4, confidence: high}
  - {predicate: studiedIn, object: ct:machine-learning, source: s1, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Choosing Prediction Over Explanation in Psychology: Lessons From Machine Learning"
    publisher: Perspectives on Psychological Science (Yarkoni & Westfall, 2017), author's copy
    url: https://www.talyarkoni.org/pdf/Yarkoni_PPS_2017.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s2
    title: "Homo Heuristicus: Why Biased Minds Make Better Inferences"
    publisher: Topics in Cognitive Science 1, 107-143 (Gigerenzer & Brighton, 2009), UC Irvine course-reading copy
    url: https://sites.socsci.uci.edu/~lpearl/courses/readings/GigerenzerBrighton2009_HomoHeuristicus.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s3
    title: "Model Selection (chapter 7 of The Material Theory of Induction, draft)"
    publisher: John D. Norton, University of Pittsburgh, Department of History and Philosophy of Science
    url: https://sites.pitt.edu/%7Ejdnorton/papers/material_theory/material_theory_April_23_chapters/7.%20Model_Selection.pdf
    type: academic
    accessed: 2026-11-16
  - id: s4
    title: "Prediction error, overfitting and the bias-variance trade-off (STAT 857 lesson notes)"
    publisher: Penn State Eberly College of Science, Department of Statistics online course notes
    url: https://online.stat.psu.edu/stat857/node/160
    type: academic
    accessed: 2026-11-16
created: 2026-11-16
---

# Overfitting

Overfitting is what happens when a model, forecasting rule or explanation is tuned so tightly to the data it was built on that it absorbs the accidental quirks of that sample along with the real pattern. Yarkoni and Westfall define it as the tendency of statistical models to mistake sample-specific noise for signal.[^s1] The overfit model looks excellent in hindsight, because it was shaped to the very cases it is scored on, and then disappoints in foresight, when it meets cases it has never seen.[^s2][^s4] For critical thinkers the idea generalises beyond statistics: any story that explains every past wrinkle perfectly deserves the question of whether it would have predicted them.[^s1][^s3]

## Origin

The problem was first posed as curve fitting. Data are produced by some underlying function blurred by noise, and a richer family of curves (quintics rather than straight lines, say) can always match a given data set more closely simply by bending to the noise.[^s3] Maximum-likelihood comparison of models with different numbers of parameters is therefore biased toward the bigger model. Hirotugu Akaike's information criterion, as Norton explains it, corrects for this by subtracting the number of adjustable parameters from the log-likelihood, a penalty derived from asking which estimators do well on average over all possible data sets.[^s3] In philosophy of science, Forster and Sober (1994) read this result as showing that statistics builds a simplicity preference into model selection, though Norton argues they overgeneralised from it.[^s3] Machine learning later made the train-versus-test distinction routine, and Yarkoni and Westfall (2017) urged psychologists to adopt it.[^s1]

## How it works

The standard explanation is the bias-variance decomposition: expected prediction error equals irreducible noise plus squared bias plus variance.[^s2][^s4] Bias is a model's systematic miss; variance is how much its fitted parameters would change if it were refitted on a fresh sample. Flexible models have low bias but high variance, so with small or noisy samples the variance term dominates and a simpler, deliberately biased model predicts better.[^s2][^s4] Error measured on the training data is optimistic for the same reason, because the data that scored the model also built it.[^s4]

A workplace example. An analyst predicting which of 50 sales leads will close regresses the outcome on 20 lead attributes and reports an R² of 0.45. Yarkoni and Westfall simulated almost exactly this design, 50 cases and 20 weak predictors, and found an in-sample R² near 0.45 when the true value was 0.07 and the out-of-sample value about 0.02.[^s1] With 200 cases and 5 stronger predictors the in-sample, true and out-of-sample values were all close to 0.3, so the same method was safe once the data were adequate.[^s1] The analyst's impressive number mostly measures how well the model memorised these 50 leads.

## Evidence

Overfitting is a mathematical consequence of estimation from finite samples, and its practical size has been shown repeatedly by cross-validation. Gigerenzer and Brighton (2009) report that across 20 real-world prediction problems, with every strategy tested on cases it had not been fitted to, the one-reason heuristic Take The Best predicted more accurately than multiple regression, and simple tallying also beat regression on average, even though regression fitted the training data best.[^s2] In their temperature example a degree-10 polynomial fitted past readings better than a degree-2 curve but predicted worse; the best predictor was degree 4.[^s2] They stress that this "less-is-more" result does not mean less information is always better, only that beyond some point added complexity hurts prediction.[^s2] Yarkoni and Westfall describe p-hacking as procedural overfitting: flexible choices about exclusions, covariates and which analysis to report tune results to one sample in the same way that extra parameters do.[^s1]

## How to spot and counter it

- **Ask for out-of-sample performance.** Fit on one part of the data and test on another; k-fold cross-validation rotates the roles, and a fully held-out sample is the strongest check.[^s1][^s4]
- **Compare complexity with sample size.** Many predictors relative to cases is the classic warning sign; large samples protect even flexible models.[^s1]
- **Penalise complexity.** Information criteria such as AIC, and regularisation methods such as ridge and lasso regression, trade a little bias for lower variance.[^s1][^s3][^s4]
- **Keep model choice inside the validation loop**, and avoid leakage such as standardising the whole data set before splitting it.[^s1]
- **Be wary of explanations that fit everything.** Norton's example of a contrived cyclic hypothesis that matches bus-arrival times perfectly shows how a perfect fit can still be judged spurious.[^s3]

Limits: complexity penalties count parameters rather than measuring simplicity itself, and Akaike's derivation assumes the true model lies within the family being considered.[^s3]

## Connections

- **Narrower than** statistical reasoning: it is a characteristic way inference from samples goes wrong.[^s4]
- **Explained by** the bias-variance trade-off, which shows why flexibility lowers fitting error while raising prediction error.[^s2][^s4]
- **Studied in** statistics, where training-error optimism and cross-validation are standard topics, and in machine learning, the source of the prediction-focused practices Yarkoni and Westfall recommend.[^s1][^s4]
- **Related to** Occam's razor, since model-selection criteria are often read as a statistical form of parsimony; to Take The Best, fast-and-frugal heuristics, ecological rationality and the weighted additive rule, whose relative accuracy depends on avoiding it; and to p-hacking and researcher degrees of freedom, its procedural cousins.[^s1][^s2][^s3]
- **Related to** ad hoc hypotheses and hasty generalization as other ways of letting a particular sample dictate a conclusion that may not hold beyond it.[^s3]

## Sources

[^s1]: Yarkoni & Westfall, "Choosing Prediction Over Explanation in Psychology: Lessons From Machine Learning", Perspectives on Psychological Science, 2017. https://www.talyarkoni.org/pdf/Yarkoni_PPS_2017.pdf (accessed 2026-11-16)
[^s2]: Gigerenzer & Brighton, "Homo Heuristicus: Why Biased Minds Make Better Inferences", Topics in Cognitive Science 1, 2009. https://sites.socsci.uci.edu/~lpearl/courses/readings/GigerenzerBrighton2009_HomoHeuristicus.pdf (accessed 2026-11-16)
[^s3]: Norton, "Model Selection", chapter 7 of The Material Theory of Induction (draft), University of Pittsburgh. https://sites.pitt.edu/%7Ejdnorton/papers/material_theory/material_theory_April_23_chapters/7.%20Model_Selection.pdf (accessed 2026-11-16)
[^s4]: Penn State Department of Statistics, STAT 857 lesson notes on prediction error, overfitting and the bias-variance trade-off. https://online.stat.psu.edu/stat857/node/160 (accessed 2026-11-16)
