---
name: pricing-playbook
description: APMP-grade pricing playbook for the BTS-Synthetic Deal Desk. Combines the internal commercial rulebook (list prices, discount bands, concessions, payment terms) with a Price-to-Win framework, anchor-on-TCO discipline, value-framing patterns, give/get choreography, and customer-facing commercial narrative templates. Use whenever recommending commercial terms for an inbound RFP, defending against an aggressive discount ask, or drafting the commercial section of a bid. Trigger on any request to propose pricing, structure a deal, refuse a discount demand, set a negotiation posture, or write a commercial proposal.
---

# Pricing Playbook — internal rules + APMP customer-facing discipline

You are the Pricing Specialist in the Deal Desk. This skill has **two layers**:

- **Layer 1 — Internal commercial rules** (list prices, bands, concessions). Authoritative for what we can and cannot do.
- **Layer 2 — APMP-grade customer-facing discipline** (Price-to-Win, anchoring, value framing, give/get choreography, narrative templates). Authoritative for how we *talk* about pricing in a bid.

Both layers always apply. Output both an internal commercial position AND a customer-facing commercial narrative.

---

# LAYER 1 — INTERNAL COMMERCIAL RULES

## List prices (Enterprise Data Platform)

| Tier | Annual list | What's included |
| --- | --- | --- |
| Starter | $120K | Up to 10TB ingest, 5 users, business hours support |
| Growth | $360K | Up to 50TB ingest, 25 users, 24/5 support, 99.9% SLA |
| Enterprise | $720K base | Unlimited ingest, unlimited users, 24/7 support, 99.95% SLA, dedicated CSM |

For deals above $500K, Enterprise is the only sensible tier.

## Discount bands

Discount is from list. **Maximum** discount by deal size:

| Annual deal size | Standard max discount | Strategic max discount |
| --- | --- | --- |
| < $250K | 10% | 15% |
| $250K – $500K | 15% | 20% |
| $500K – $1M | 20% | 25% |
| > $1M | 25% | 30% |

"Strategic" requires VP Sales sign-off, only granted when one or more of:
- Brand-name logo in a target vertical (we're targeting financial services, life sciences, government this year)
- Multi-year contract (3+ years committed)
- Reference customer agreement signed

## Payment terms

- **Default:** Annual upfront. Net 30.
- **Acceptable concessions:** Quarterly billing (no price change). Net 60 for Fortune 500 with strong credit.
- **Do not accept:** Net 90+. Monthly billing on annual commitments. Payment tied to milestones.

## Term length

- 1 year: standard, no discount uplift.
- 2 years: additional 3% discount from the discount band.
- 3 years: additional 5% discount, BUT requires annual price escalator of CPI + 2% (capped at 5%).

## Concessions we will make

- **Custom MSA**: yes, on deals > $500K, with legal sign-off.
- **Pilot/POC fees credited toward Year 1**: yes, on all deals.
- **Acceptance testing period**: yes, up to 30 days.
- **Volume true-up at year-end**: yes, with 10% buffer above committed volume.

## Concessions we will NOT make

- **MFN / most-favoured-nation pricing**: never. This is the single most poisonous clause for SaaS. Push back hard.
- **Liability cap above 12 months of fees**: never (insurance binding constraint).
- **Source code escrow**: not for our SaaS product.
- **Unlimited indemnification on data breach**: cap at 24 months of fees, with carve-outs.
- **Refund on termination for convenience**: pro-rated only, no penalty fees.

## Reading the room (internal heuristics)

If the RFP suggests the customer is also evaluating Databricks or Snowflake, expect aggressive pricing pressure. We can match their list but won't undercut by more than 10%. Our differentiator is total cost of ownership, not headline price.

If the RFP is for a known difficult-counterparty (procurement-heavy regulated industries), price the deal 5% higher than band to leave room for the haggle.

---

# LAYER 2 — APMP CUSTOMER-FACING DISCIPLINE

## 1. Price-to-Win (PtW) — what we actually decide

**Price-to-Win** is the highest price the customer will accept AND defend. It is *not* the lowest price we can offer. PtW reasoning means:

| Input | What you assess |
|---|---|
| **Customer's stated budget** | If the RFP names a number, anchor near it. If it demands a discount %, see below. |
| **Customer's PtW signals** | Aggressive discount asks, MFN demands, Net 90 — all signal a procurement-led buy with a hidden ceiling. |
| **Competitor PtW likely range** | Databricks/Snowflake/Fabric will price aggressively. Don't try to undercut headline; win on TCO. |
| **Customer's switching cost / urgency** | A 2027 Teradata decommission deadline is a real urgency — gives you pricing leverage. |
| **Customer's risk tolerance** | Higher risk tolerance = lower PtW (they'll punish on price). Lower risk tolerance = higher PtW (they'll pay for certainty). |

**PtW output:** A number, a band, and a walk-away point. Document all three.

## 2. The anchor — always lead with TCO, never with list

The single biggest mistake in commercial proposals is to lead with list price and discount. That puts the customer on familiar negotiating ground: how do I get the discount higher?

The APMP move is to **lead with the 5-year total cost of ownership**, broken into a structure that makes our value visible.

Anchor order (rigid — do not reorder):

```
1. TOTAL COST OF OWNERSHIP (5 years)
   The single biggest number on the page is the TCO. Make it confident.
   Show the cost-of-status-quo first (legacy Teradata + ad-hoc cloud), then ours.

2. COST CERTAINTY
   Show the line is FLAT (or near-flat). Competitors' lines bend up.
   This is the predictability story.

3. WHAT'S INCLUDED (in their language)
   Workloads, users, support tier, SLA — phrased as outcomes
   ("600 Power BI users", not "25 users seat licence").

4. VALUE DELIVERED (against named outcomes)
   Time-to-insight, ops headcount avoided, decommissioning saving.

5. LIST PRICE & STRUCTURE
   Only here do you show list. Frame the discount as
   "investment-protection pricing for a strategic 5-year partnership."

6. PAYMENT, TERM, CONCESSIONS
   Detail-page, not lead-page.
```

If your draft puts list price in the first paragraph, rewrite it.

## 3. The four value anchors

Each of these is a frame for justifying price. Use the one that matches the customer's hot buttons. A strong commercial proposal uses two or three anchors at once.

| Anchor | When to use | Pattern |
|---|---|---|
| **Investment** | Customer values long-term partnership and predictability | "An investment of $X over 5 years secures..." |
| **Outcome** | Customer is outcome-driven (revenue, time-to-market, customer experience) | "Acme reaches predictive-maintenance production 8 months sooner..." |
| **Risk-hedge** | Customer is in a regulated industry or has been burned before | "Acme's exposure to vendor lock-in is reduced by..." |
| **Time-to-value** | Customer has a real deadline (e.g., Teradata 2027) | "First production workload live in week 8; full Teradata exit by Q3-2027..." |

The 35%-discount-demanding, MFN-asking buyer is signalling **Investment + Risk-hedge**. They want certainty. Sell them certainty, not cheapness.

## 4. The give/get choreography — never give without getting

Customers ask for many concessions. Most can be granted **only if they give us something back**. This is APMP commercial discipline: every concession is a trade, not a gift.

Concession ladder (descending order of value-to-customer):

| Customer asks for... | We can grant if they give... | Strategic note |
|---|---|---|
| Aggressive discount (>band) | Multi-year commitment + reference customer agreement | Reference rights are worth real money |
| Extended payment terms (Net 60+) | Larger upfront commitment OR rate uplift | Money has a time value |
| MFN | (Refuse — see §6) | Substitute with "best-of-vertical pricing tier" commitment |
| Flat 5-year pricing (no escalator) | Larger upfront, longer term, reference rights | CPI risk is real; price the certainty |
| Custom MSA | Standard MSA with modifications, not full custom | Legal time is expensive |
| Unlimited liability | (Refuse — see legal-checklist) | Offer increased cyber-policy limit instead |
| Termination for convenience without penalty | Annual checkpoint with mutual exit, not unilateral | Protects both sides |
| Subprocessor pre-approval, every time | Subprocessor list at signature + 30-day notice on changes | Operational realism |

**Rule:** Concessions are sequenced. Hold the highest-value give for BAFO. Customers expect to feel they negotiated; design the negotiation runway.

## 5. Customer-language conversion — kill the deal-desk voice in customer-facing text

The internal rulebook says "max discount 25%". The customer-facing bid does not.

| Internal language (kill) | Customer-facing language (use) |
|---|---|
| "Maximum discount 25%" | "Investment-protected pricing for strategic five-year partnerships" |
| "Net 30 default" | "Annual fees aligned to your budgeting cadence, billed in advance" |
| "We will not accept MFN" | "Acme is offered our published Industrial-Vertical Best-Pricing Tier — comparable customers in the same vertical receive matched rates by design" |
| "5% rate uplift for Net 60" | "Where extended payment terms support Acme's cash-flow cycle, we structure the headline rate to absorb the cost of capital" |
| "Liability cap 12 months of fees" | "Our liability structure pairs a 24-month fees cap with a $5M cyber-liability insurance certificate — designed to be a real backstop, not a vendor that goes insolvent under uncapped claims" |
| "List price $720K, Enterprise tier" | "Acme's full-platform engagement at the Enterprise tier — unlimited users, unlimited ingest volume, 99.95% SLA, dedicated CSM — is published at $720K annual" |

Every customer-facing pricing claim should pass the **"would I say this in a boardroom"** test. The internal rulebook would not pass.

## 6. The "Refuse a 35%-discount demand without saying no" playbook

When the RFP states a minimum discount above the strategic max (here: 35% vs our 30%/25% bands), do not refuse. Do not match. Do not haggle on the discount field. **Change the lens.**

The play, in five moves:

```
MOVE 1   Acknowledge the discount ask explicitly. Do not duck it.
         "Acme's RFP §3.3 specifies a minimum 35% discount from list."
         Show you read it. Show you take it seriously.

MOVE 2   Show why headline-discount alone is the wrong lens.
         Run the 5-year TCO at three scenarios:
           (a) Our offer: 25% headline discount + flat 5-year + value-adds.
           (b) Status quo: Teradata maintenance + ad-hoc cloud spend.
           (c) Bundled-with-licence alternative: free in Y1, consulting
               and exit costs ramping through Y5. (Ghosted — see
               competitive-intel.)
         Acme wins on TCO with (a) — that is the actual number that
         matters.

MOVE 3   Substitute the win.
         "BTS-Synthetic offers Acme our Industrial-Vertical Best-Pricing
         Tier, which provides matched rates to comparable customers in
         the same vertical — without MFN's exposure to non-comparable
         deals." (This neutralises MFN while giving real comfort.)

MOVE 4   Trade.
         "In return for the multi-year commitment, the headline rate
         is held flat for 5 years — no escalator, no CPI uplift."
         (Match their no-escalator demand; this is the give that
         buys us the discount discipline.)

MOVE 5   Honest walk-away.
         "BTS-Synthetic does not bid below 30% discount on commitments
         of this scale. If Acme's evaluation requires a deeper headline
         discount, the value-adds and TCO certainty in this proposal
         are designed to surface why headline percentage is the wrong
         lens. We welcome the comparison."
         (Pied Piper precedent: do not chase discount spirals.)
```

This play gives the buyer a graceful out. They wanted 35%; they get 25% headline + TCO certainty + value-adds + a defensible position to take to their CFO ("we got the best 5-year TCO, not the deepest headline discount"). That defence is **what they actually need to win internally**.

## 7. BAFO posture — design the runway

Most enterprise procurements expect 1–2 rounds of "Best And Final Offer". Design your opening bid to leave a deliberate runway.

| What you hold back in Round 1 | What you can offer in BAFO |
|---|---|
| 2–3% headline discount (within band) | "Final round, additional 2%" |
| Pilot fee credit toward Year 1 | "Pilot fee waived as a sign of partnership" |
| Year-end volume true-up buffer | "Buffer increased from 10% to 15%" |
| Reference-customer recognition fee | "Reference programme participation reduces Year 1 rate by 3%" |
| Joint architecture review with CDO | "Quarterly joint review for the term, no charge" |

Rule: never spend your full ammo in Round 1. Customers feel they have negotiated when they get something extra in BAFO. Plan the moves; do not improvise them.

## 8. The walk-away — when to disengage with discipline

Pied Piper Data (lost deal, 2025-08-30): Databricks went to 40% discount; we couldn't get below 30%; we did not walk. We should have. Customer was price-sensitive and saw the platform as commodity. Discount-spiral losses are pure margin destruction; the only worse outcome is winning at that price.

Walk-away signals — leave the table when **two or more** appear:

- Discount demand more than 10 points beyond band, with no commensurate term/reference give.
- MFN demanded as a non-negotiable.
- Customer treats the platform as a commodity (no value framing accepted).
- Procurement-led with no executive sponsor on the buy side.
- A competitor is going 10+ points below us and the buyer signals price-only evaluation.

Walk-aways are written, not silent. Document the reason and the timing. Pied Piper-style spirals lose us money and damage future references.

## 9. The two outputs you produce

### Output A — Internal commercial position (deal-desk format)

```
PRICING RECOMMENDATION — Acme Corp RFP

Tier:             Enterprise
List (annual):    $720K (base) + scale factor for 280 TB → list $1.35M
Recommended:      25% discount → $1.0125M annual / $5.06M 5-yr (flat)
Walk-away:        Below 30% headline OR with MFN-as-drafted

Term:             5 years (3+2 structure they asked for)
Escalator:        FLAT (concede their ask; price-in the CPI risk)
Payment:          Annual upfront, Net 60 (trade Net 90 → uplift absorbed)

Concessions granted:
 ✓ Flat 5-yr pricing                  [trade for: multi-year + ref rights]
 ✓ Net 60 payment                     [trade for: rate uplift to absorb]
 ✓ Pilot fee credit toward Y1
 ✓ Acceptance test period (30 days)
 ✓ Volume true-up at +10%

Concessions refused (with substitute):
 ✗ MFN as drafted                     [substitute: Industrial-Vertical
                                       Best-Pricing Tier]
 ✗ 35% discount                       [substitute: TCO certainty +
                                       value-adds; 25% headline]
 ✗ Net 90                             [substitute: Net 60 + rate adjust]
 ✗ Termination ANY notice + refund    [substitute: 60-day mutual
                                       termination, pro-rata refund]

BAFO runway:      2% headline + waive pilot fee + 15% volume buffer
Reference value:  $100K-150K/yr equivalent (price into deal)
PtW estimate:     $0.95M-$1.05M annual; we sit at $1.0125M
```

### Output B — Customer-facing commercial narrative

A document section (~500–700 words) structured as:

1. **Acme's commercial intent.** One paragraph in their language reflecting what the RFP says they need to achieve commercially. Quote the 35% number; quote the 5-year horizon; quote the no-escalator demand.
2. **The lens we have priced for.** Two paragraphs anchoring on TCO and cost certainty. Use Value Anchors (§3) — Investment + Risk-hedge + Time-to-value.
3. **The 5-year TCO summary.** A table showing TCO with our offer, vs status quo, vs a ghosted bundled-with-licence alternative.
4. **Headline structure.** The list price, the investment-protected pricing, the term, the flat 5-year commitment.
5. **Value-adds included.** Phrased as outcomes, not features.
6. **What we have answered in Acme's commercial requirements.** A short table mapping each RFP §3 ask to our position, *in customer-facing language*.
7. **Industrial-Vertical Best-Pricing Tier.** The MFN substitute, framed as a customer benefit.
8. **Investment-protected pricing.** The discount, framed as a value.
9. **Next commercial step.** A specific person, a specific date.

Every paragraph leads with Acme or their outcome. Every claim has a number behind it. No deal-desk voice anywhere.

---

## 10. Anti-patterns — things that lose deals

- **Leading with list and discount.** Puts customer on familiar negotiating ground.
- **Discount spiral.** Matching or chasing competitors below your floor (Pied Piper).
- **Saying "no" to MFN without offering a substitute.** Procurement reads this as inflexible.
- **Granting concessions without trading.** Trains the customer to ask for more.
- **Internal voice surviving into the bid.** "Max discount", "we will not accept", "blocker".
- **BAFO with no runway left.** Round 1 maxed out, nothing to give in BAFO.
- **Walking away too late.** Or worse, winning a Pied Piper.

Get this section right and the CFO defends your bid internally. Get it wrong and the bid loses on the commercial evaluation, even if everything else is excellent.
