---
id: ct:theodore-sterling
type: Person
title: Theodore Sterling
aliases: [Theodor D. Sterling, T. D. Sterling, Ted Sterling]
domain: history-and-thinkers
summary: >-
  Vienna-born American-Canadian statistician (died 2005) whose 1959 survey of
  psychology journals, showing that almost every published significance test
  rejected the null hypothesis, was the first empirical warning that the
  published record is a filtered sample of research; he later founded computing
  science at Simon Fraser University.
level: intermediate
evidenceStatus: historical
broader: []
related: [ct:publication-bias, ct:null-hypothesis-significance-testing, ct:replication-crisis, ct:preregistration, ct:systematic-review, ct:registered-reports]
requires: [ct:null-hypothesis-significance-testing]
relations:
  - {predicate: introduced, object: ct:publication-bias, source: s3, confidence: high}
  - {predicate: influenced, object: ct:hubbard-armstrong-1992-null-results-in-marketing-study, source: s4, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "About the Sterlings (Nora and Ted Sterling Prize in Support of Controversy)"
    publisher: Office of the Vice-President, Academic, Simon Fraser University
    url: https://www.sfu.ca/vpacademic/awards/nora-and-ted-sterling-prize/about-the-sterlings.html
    type: academic
    accessed: 2026-11-12
  - id: s2
    title: "Publication Decisions and Their Possible Effects on Inferences Drawn from Tests of Significance - or Vice Versa"
    publisher: Journal of the American Statistical Association 54(285), 30-34 (Sterling, 1959); scanned copy hosted by gwern.net
    url: https://www.Gwern.net/doc/statistics/bias/publication/1959-sterling.pdf
    type: primary
    accessed: 2026-11-12
  - id: s3
    title: "Publication Decisions Revisited"
    publisher: The American Statistician 49(1), 108-112 (Sterling, Rosenbaum & Weinkam, 1995); scanned copy hosted by gwern.net
    url: https://Www.Gwern.net/doc/statistics/bias/publication/1995-sterling.pdf
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s4
    title: "Are Null Results Becoming an Endangered Species in Marketing?"
    publisher: Marketing Letters 3(2), 127-136 (Hubbard & Armstrong, 1992); author copy, University of Southampton CogPrints archive
    url: https://web-archive.southampton.ac.uk/cogprints.org/5178/1/are_null_results_becoming.pdf
    type: peer-reviewed
    accessed: 2026-11-12
created: 2026-11-12
---

# Theodore Sterling

Theodore D. Sterling was a statistician and computer scientist best remembered in critical thinking for a four-page 1959 paper showing that the journals of his day published almost nothing but "significant" results.[^s2] From that pattern he drew a lesson that still anchors the study of publication bias: when the decision to publish depends on the outcome of a test, the published literature stops being a fair sample of the research that was done, and the error rates authors report can no longer be taken at face value.[^s2][^s3]

## Origin

Sterling was born and raised in Vienna and fled Nazism with his family in 1940, arriving in the United States with almost nothing. After army service in the Second World War he completed high school in a single year, and by 1955 he held two degrees from the University of Chicago and a doctorate from Tulane.[^s1] He held posts at Alabama, Michigan and Cincinnati; the 1959 paper lists him at the University of Cincinnati.[^s1][^s2] In 1972 he moved to Simon Fraser University in Canada, where he founded the computer science department and served as its first chair. Simon Fraser describes him as an early user of computers to mine large public-health databases in epidemiology and risk analysis, and as one of the first to warn about the threat computing posed to privacy. He died in Vancouver in January 2005.[^s1]

## How it works

The 1959 study was a simple audit. Sterling took a year of issues from four psychology journals, one each in experimental, comparative and physiological, clinical and social psychology, and coded every research report. Of 362 reports, 294 used significance tests; 286 of those rejected the null hypothesis and only 8 did not. None of the 362 was a replication of earlier published work.[^s2]

His argument turned that count into a problem of inference. If non-significant results usually go unpublished, other researchers never learn of them and may run the same experiment again; sooner or later one of them gets a significant result by chance alone, and that result is the one that appears in print. Because published findings were rarely replicated, such Type I errors could sit in the literature unchallenged. A reader therefore cannot accept an author's stated significance level as the real risk of error, because the reader does not know how many similar studies failed and stayed in the drawer.[^s2] Sterling suggested this filtering came mainly from authors' own choices about what to submit rather than from any formal editorial rule, and he implied that readers need the distribution of outcomes across similar experiments, not one study's p-value.[^s2]

A workplace example makes the logic concrete. Suppose ten product teams each test a new onboarding email and only the one team whose result came out "significant" presents it at the company review. Everyone at the review sees a clean win; no one sees the nine flat results that would show the win was probably luck. The journal record, on Sterling's argument, works like that company review scaled up.[^s2]

## Legacy and limitations

In 1995 Sterling and two Simon Fraser colleagues repeated the audit. In eight psychology journals from the late 1980s, about 96% of articles that used significance tests rejected the null for their main hypothesis, against about 97% in his original sample; three medical journals showed about 85%.[^s3] The authors called the 1959 paper the first to suggest that published results are unrepresentative, concluded that the bias had persisted for some thirty years, and distinguished two harms: false hypotheses that eventually get a lucky positive result into print, and true hypotheses whose weak or null results are under-reported. They argued that awareness alone had not helped and proposed judging studies without regard to outcome and registering clinical trials.[^s3] Both ideas anticipate today's preregistration and results-blind review.

Others took up his method. Hubbard and Armstrong (1992) cited the 1959 study as an early empirical look at the scarcity of null results and adopted Sterling's coding scheme to show that only 7.8% of significance-testing papers in three leading marketing journals reported null results, a share that roughly halved from the 1970s to the 1980s.[^s4]

Two limits are worth keeping in view. A high rate of significant results is suggestive rather than proof of bias, since a field could in principle test mostly true hypotheses with powerful designs; Sterling's case rests on the combination of that rate with the absence of replications.[^s2] Hubbard and Armstrong addressed part of this by checking statistical power and found that low power did not explain the missing null results in their sample.[^s4] And the 1959 sample was small and confined to psychology, which is why the later re-audits across fields mattered.[^s3]

## Connections

- **Introduced publication bias** as an empirical concern: his 1995 paper with Rosenbaum and Weinkam describes the 1959 survey as the first to suggest that published results are not representative.[^s3]
- **Influenced** Hubbard and Armstrong's 1992 study of null results in marketing, which adopted his classification scheme for coding papers.[^s4]
- **Related: null hypothesis significance testing**, whose stated error rates his argument showed to be distorted by selective publication, and the **replication crisis**, foreshadowed by his finding that published results were essentially never replicated.[^s2]
- **Related: preregistration, registered reports and systematic review**, the remedies that echo his 1995 calls for outcome-blind review and trial registration.[^s3]

## Sources

[^s1]: Simon Fraser University, "About the Sterlings". https://www.sfu.ca/vpacademic/awards/nora-and-ted-sterling-prize/about-the-sterlings.html (accessed 2026-11-12)
[^s2]: Sterling, "Publication Decisions and Their Possible Effects on Inferences Drawn from Tests of Significance - or Vice Versa", Journal of the American Statistical Association 54(285), 1959. https://www.Gwern.net/doc/statistics/bias/publication/1959-sterling.pdf (accessed 2026-11-12)
[^s3]: Sterling, Rosenbaum & Weinkam, "Publication Decisions Revisited", The American Statistician 49(1), 1995. https://Www.Gwern.net/doc/statistics/bias/publication/1995-sterling.pdf (accessed 2026-11-12)
[^s4]: Hubbard & Armstrong, "Are Null Results Becoming an Endangered Species in Marketing?", Marketing Letters 3(2), 1992. https://web-archive.southampton.ac.uk/cogprints.org/5178/1/are_null_results_becoming.pdf (accessed 2026-11-12)
