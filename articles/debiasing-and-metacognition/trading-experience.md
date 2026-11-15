---
id: ct:trading-experience
type: Technique
title: Trading experience
aliases: [market experience, exchange practice, forced-trade practice]
domain: debiasing-and-metacognition
summary: >-
  A debiasing intervention in which people gain repeated practice at
  exchanging or giving up goods they hold, which in field and lab experiments
  shrinks the endowment effect and the gap between willingness to accept and
  willingness to pay.
level: intermediate
evidenceStatus: mixed
broader: [ct:debiasing]
related: [ct:endowment-effect, ct:loss-aversion, ct:status-quo-bias, ct:broad-bracketing, ct:reversal-test, ct:behavioral-economics]
requires: [ct:endowment-effect]
relations:
  - {predicate: counteracts, object: ct:endowment-effect, source: s1, confidence: medium}
  - {predicate: introducedBy, object: ct:john-a-list, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: ct:list-2003-sportscard-market-experiment, source: s1, confidence: high}
  - {predicate: supportedBy, object: ct:list-2011-exogenous-market-experience, source: s2, confidence: medium}
  - {predicate: supportedBy, object: ct:engelmann-hollard-2010-forced-trade-experiment, source: s3, confidence: medium}
  - {predicate: explainedBy, object: ct:trade-uncertainty, source: s3, confidence: medium}
  - {predicate: appliedIn, object: ct:behavioral-economics, source: s1, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Does Market Experience Eliminate Market Anomalies?"
    publisher: Quarterly Journal of Economics 118(1), 41-71 (List, 2003), RePEc/IDEAS record
    url: https://ideas.repec.org/a/oup/qjecon/v118y2003i1p41-71..html
    type: primary
    accessed: 2026-11-15
  - id: s2
    title: "Does Market Experience Eliminate Market Anomalies? The Case of Exogenous Market Experience"
    publisher: NBER Working Paper 16908 (List, 2011); published in American Economic Review 101(3), 313-317
    url: https://ideas.repec.org/p/nbr/nberwo/16908.html
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s3
    title: "Reconsidering the Effect of Market Experience on the 'Endowment Effect'"
    publisher: Econometrica 78(6), 2005-2019 (Engelmann & Hollard, 2010), Econometric Society
    url: https://econometricsociety.org/publications/econometrica/2010/11/01/reconsidering-effect-market-experience-“endowment-effect”
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s4
    title: "Consumption Experience, Choice Experience and the Endowment Effect"
    publisher: Journal of the Economic Science Association 3(2), 109-120 (Humphrey, Lindsay & Starmer, 2017), Springer
    url: https://link.springer.com/article/10.1007/s40881-017-0044-z
    type: peer-reviewed
    accessed: 2026-11-15
created: 2026-11-15
---

# Trading experience

Trading experience is the practice of repeatedly exchanging, selling or giving up things one holds, used as a remedy for the endowment effect: the tendency of owners to demand far more to part with a good than non-owners would pay for it. Field and laboratory experiments find that people with more exchange practice show a smaller gap between willingness to accept (WTA) and willingness to pay (WTP), and that deliberately inducing such practice can remove the asymmetry in later choices.[^s1][^s2][^s3] The evidence is promising but not uniform, so it is best treated as one tool rather than a guaranteed cure.[^s4]

## Origin

The idea was put to an empirical test by the economist John A. List in a 2003 *Quarterly Journal of Economics* paper. At a sportscard show and a collectible-pin market he randomly handed people one of two items of similar value and offered a swap. Inexperienced consumers mostly kept whatever they were given, while dealers and frequent traders swapped at roughly the rate standard theory predicts. In parallel auctions, non-dealers asked several times more to sell a card sheet than they would pay for it, whereas dealers' selling and buying prices were statistically indistinguishable.[^s1] A follow-up a year later and fixed-effects models suggested that accumulating trades, not just a stable trait of the people who trade, drove the change.[^s1]

Because people who trade a lot may differ from those who do not, List later ran a framed field experiment that assigned market experience exogenously and concluded that experience alone can eliminate the WTP-WTA disparity.[^s2] Dirk Engelmann and Guillaume Hollard (2010, *Econometrica*) then asked what kind of experience matters. They distinguished uncertainty about which good one prefers from uncertainty about the act of trading itself, and found that making subjects give away their endowments across a series of exchanges removed the asymmetry in a subsequent test.[^s3]

## How it works

The endowment effect is often explained by loss aversion: once a mug or a ticket is "mine", giving it up feels like a loss. Engelmann and Hollard's account adds that inexperienced people are unsure about trading as such (whether the deal is fair, whether they will regret it) and so default to keeping what they have. Practice at letting things go reduces that trade uncertainty.[^s3]

A workplace example: a facilities manager must decide whether to sell an under-used company van. Having held it for years, she values it well above what she would pay for an identical van today. A team that routinely buys and disposes of assets, auctions surplus stock, or rotates equipment between sites builds exactly the exchange practice the studies describe, and tends to price such assets closer to their market value.[^s1][^s3]

## How to apply it

1. **Practise low-stakes exchanges.** Before a high-stakes sale or swap, run several small, real exchanges of things you hold; in the forced-trade design, the practice exchanges preceded the test choice.[^s3]
2. **Make the trading frequent, not one-off.** The field evidence ties lower asymmetry to how often people trade, with diminishing returns once trading is regular.[^s1]
3. **Separate the trading decision from the preference question.** Ask which item you would choose if you held neither, then treat the transaction as routine; this mirrors the distinction between choice and trade uncertainty.[^s3]
4. **Pair it with other checks.** Experience may help less for unfamiliar goods or bundles, so combine it with a direct comparison of buying and selling prices.[^s4]

Pitfalls: List's own data show experienced traders exploiting inexperienced ones, so practice changes behaviour but does not guarantee fair deals,[^s1] and gains from one market may not transfer to very different goods.[^s4]

## Evidence

List's 2003 field results were strong for frequent traders but rested on small samples, and his short lab study still found a residual effect after several sessions.[^s1] The exogenous-experience experiment strengthens the causal case,[^s2] and the forced-trade results replicate the elimination in a controlled lab setting.[^s3] A 2017 study by Humphrey, Lindsay and Starmer found that giving people prior choice experience raised swap rates from about 23% to 35%, a difference that just missed conventional significance, and that bundled goods showed no endowment effect to remove at all.[^s4] The status is therefore **mixed**: experience reliably moves behaviour in the predicted direction, but the size of the effect depends on the goods and the kind of practice.

## Connections

- **Broader:** `ct:debiasing`, as a deliberate intervention against a documented bias.[^s3]
- **Counteracts:** `ct:endowment-effect`, the WTA-WTP asymmetry that experienced traders do not show.[^s1]
- **Introduced by:** `ct:john-a-list`, who first tested market experience as a remedy in the field.[^s1]
- **Demonstrated by:** `ct:list-2003-sportscard-market-experiment`, the sportscard and pin-market swaps.[^s1]
- **Supported by:** `ct:list-2011-exogenous-market-experience`, which assigned experience at random,[^s2] and `ct:engelmann-hollard-2010-forced-trade-experiment`, which removed the asymmetry with forced exchanges.[^s3]
- **Explained by:** `ct:trade-uncertainty`, uncertainty about the act of exchanging that practice reduces.[^s3]
- **Applied in:** `ct:behavioral-economics`, where it bears on whether market anomalies survive experience.[^s1]
- **Related:** `ct:loss-aversion` and `ct:status-quo-bias`, the neighbouring reference-dependent effects; `ct:broad-bracketing` and `ct:reversal-test`, other remedies for the same family of biases.

## Sources

[^s1]: List, "Does Market Experience Eliminate Market Anomalies?", *Quarterly Journal of Economics* 118(1), 2003. https://ideas.repec.org/a/oup/qjecon/v118y2003i1p41-71..html (accessed 2026-11-15)
[^s2]: List, "Does Market Experience Eliminate Market Anomalies? The Case of Exogenous Market Experience", NBER Working Paper 16908 / *American Economic Review* 101(3), 2011. https://ideas.repec.org/p/nbr/nberwo/16908.html (accessed 2026-11-15)
[^s3]: Engelmann & Hollard, "Reconsidering the Effect of Market Experience on the 'Endowment Effect'", *Econometrica* 78(6), 2010. https://econometricsociety.org/publications/econometrica/2010/11/01/reconsidering-effect-market-experience-“endowment-effect” (accessed 2026-11-15)
[^s4]: Humphrey, Lindsay & Starmer, "Consumption Experience, Choice Experience and the Endowment Effect", *Journal of the Economic Science Association* 3(2), 2017. https://link.springer.com/article/10.1007/s40881-017-0044-z (accessed 2026-11-15)
