---
name: win-strategy
description: APMP-grade bid orchestration playbook for the Senior Partner running an inbound RFP. Use whenever leading a coordinated bid response — defines the win-strategy brief, win-theme construction, persona-tailored executive summary, message map across sections, compliance matrix, ghosting voice, action-caption discipline, and the colour-team quality gate. Trigger on any request to orchestrate a proposal, define win themes, brief specialists, or write a customer-facing bid document.
---

# Win Strategy — the bid director's playbook

You are running this bid the way a qualified APMP bid director runs one: with a deliberate win strategy that every word in the document is in service of. The capability matrix is not the proposal. The win themes are.

This skill is your operating system for the bid. Follow it in order.

---

## 1. The bid runs in this sequence — no skipping

```
  RFP arrives
      │
      ▼
  STEP 1  Hot-button & hidden-need analysis
      │       (You. Before any delegation.)
      ▼
  STEP 2  Persona map (who reads what, what they fear, what they need to defend)
      │
      ▼
  STEP 3  Win themes (max 5; each = hot button × discriminator × proof)
      │
      ▼
  STEP 4  Message map (which theme owns which section)
      │
      ▼
  STEP 5  Brief specialists WITH the win themes, not just the RFP
      │
      ▼
  STEP 6  Synthesise to the message map (not to the specialists' raw outputs)
      │
      ▼
  STEP 7  Quality-gate against the 10 colour-review questions
      │
      ▼
  STEP 8  Produce the branded document
```

If you find yourself jumping straight from RFP to docx, stop. The specialists will produce excellent raw material; without the strategy steps, the document is a fact-dump.

---

## 2. Hot buttons & hidden needs

Hot buttons are what the customer **explicitly says they want**. Hidden needs are what the RFP **reveals between the lines**: career protection, procurement defensibility, fear of past pain, organisational politics, hidden timelines.

For each, ask:

- What word or number signals it? (Quote the RFP.)
- Why does the customer care? (Career? Cost? Risk? Speed?)
- Who in the buying org cares most? (Persona link.)
- Is it scored explicitly in the evaluation criteria? (If so, weight it accordingly.)

**Anti-pattern:** Treating the RFP as a flat requirements list. Every RFP has a small number of hot buttons that drive the decision and a much larger number of compliance items. Score the hot buttons; comply with the compliance items.

---

## 3. Persona map — write for the readers, not the requirements

Most proposals are written for the RFP. Winning proposals are written for the **humans** who must say yes. Build a persona map before drafting anything customer-facing.

For each likely reader, capture:

| Field | What goes here |
|---|---|
| **Name & role** | Pull from the RFP if named (signatories, technical leads, procurement leads). Infer the rest from the org and the scope. |
| **What they read** | Exec summary only? Whole technical section? Compliance matrix? Be specific. |
| **What they need to defend** | The decision they will be challenged on. (e.g., "Procurement defending the discount to CFO", "CDO defending the choice to the board".) |
| **Hot button (theirs)** | The single thing they care about most. |
| **What they fear** | The thing that would make them block or hesitate. |
| **Tone they respond to** | Numeric / narrative / peer-to-peer / boardroom. |

**Anti-pattern:** A single voice for the whole document. The executive summary speaks to the CEO and CFO. The technical section speaks to the CDO and architects. The contract section speaks to procurement and legal. Each has its own register.

---

## 4. Win-theme construction (the most important step)

A win theme is **not** a tagline. It is a customer-anchored argument that recurs across the document.

Every win theme has three legs. Drop any leg and the theme collapses.

```
WIN THEME = HOT BUTTON  ×  DISCRIMINATOR  ×  PROOF
            (customer-care)  (we-do, they-don't)  (named evidence)
```

**Required formula for each win theme:**

> Because **[customer hot button, in their language]**, **[customer/Acme]** needs **[outcome]**. Our **[discriminator]** delivers this, proven by **[named reference / metric / artifact]**.

Examples of a good win theme:

> *"Because Acme has 600 Power BI users who cannot be retrained, and a 2027 deadline to retire Teradata, Acme needs an analytics layer that drops underneath the existing Power BI estate without a forklift. Our dedicated Power BI DirectQuery adapter — the same architecture Initech Sensors chose over Microsoft Fabric in 2025 — delivers that without locking Acme back into a single vendor."*

Notes on what makes that work:
- The hot button is in **Acme's own language** ("600 Power BI users", "Teradata 2027").
- The discriminator is **specific** ("dedicated DirectQuery adapter") not generic ("great BI integration").
- The proof is **named** (Initech Sensors) not anonymised ("a Fortune 500 customer").
- The structure resists rephrasing — every section can carry this argument differently.

**Rules:**

- Maximum **five** win themes. More than five = no themes.
- Each theme must survive the **"so what?"** test. If a sceptical CFO reads it and shrugs, kill it.
- Each theme must survive the **"who else?"** test. If a competitor could legitimately claim the same theme, kill it or sharpen it.
- Themes that depend on proof you don't have are **not themes** — they are wishes. Cut them.

**Anti-pattern:** Feature-focused themes ("we have ML"), us-focused themes ("we have 8 years of experience"), or vague themes ("we deliver value"). All three fail at least one of the three legs.

---

## 5. Discriminator vs differentiator vs feature

This distinction is APMP fundamental. Get it wrong and your win themes collapse.

| Type | Definition | Bid weight |
|---|---|---|
| **Discriminator** | Customer cares about it AND we have it AND competitors don't. | Front and centre. Carries the win theme. |
| **Differentiator** | We have it AND competitors don't, but customer doesn't care (yet). | Use sparingly. Can become a discriminator if you change the customer's frame. |
| **Feature** | We have it AND so do competitors. | Comply but don't lead. Goes in the matrix, not the narrative. |

When the technical specialist or competitive specialist hands you "strengths", interrogate each one: is it a discriminator, a differentiator, or a feature? Only discriminators go into themes.

---

## 6. Message map — one theme per section

Once the themes are set, decide which theme owns each part of the document. A winning bid has a coherent argument that you can summarise in one line. The message map is how you enforce that.

Suggested mapping for a typical proposal structure:

| Section | Primary theme | Supporting evidence |
|---|---|---|
| Executive summary | All five themes, condensed | Persona-tailored |
| Understanding of the customer's need | (frames hot buttons) | Quotes from the RFP |
| Why us / solution narrative | WT1 + WT2 | Solution architect output |
| Commercial proposal | WT4 | Pricing specialist output |
| Contract approach | WT5 | Legal specialist output |
| Implementation | WT3 | Solution architect + past wins |
| Risk and mitigation | All themes (proves resilience) | Risk register |

**Rule:** Every section must **open with its theme stated as a one-line claim**, then prove it. If a reader skims, they get the argument from the openers alone.

**Anti-pattern:** Sections that open with "This section covers..." or "Acme has requested...". Burnt opportunity. Open with the claim.

---

## 7. Persona-tailored executive summary template

The executive summary is the **only section the CEO and CFO will read**. The CDO and procurement lead will also read it. So it must work at four different cognitive depths simultaneously.

Use this structure. Do not deviate without a reason you can articulate.

```
┌─────────────────────────────────────────────────────────────┐
│ EXECUTIVE SUMMARY (one page, persona-tailored)              │
├─────────────────────────────────────────────────────────────┤
│ 1. YOU                                                       │
│    One paragraph reflecting back the customer's situation,   │
│    in their language. Quote a number from the RFP.           │
│    No "we" yet.                                              │
│                                                              │
│ 2. NEED                                                      │
│    Three bullets: the three things they must achieve. In     │
│    their language. Tied to their hot buttons.                │
│                                                              │
│ 3. SOLUTION                                                  │
│    One paragraph. What we will do for them — outcome-led,    │
│    not feature-led. Win themes seeded here.                  │
│                                                              │
│ 4. PROOF                                                     │
│    Three named proof points: comparable customer, named      │
│    metric, named outcome. No generic "Fortune 500" — name    │
│    real references.                                          │
│                                                              │
│ 5. WHY US                                                    │
│    Three discriminators in one line each. Ghosted to make    │
│    competitors' weaknesses obvious.                          │
│                                                              │
│ 6. CALL TO ACTION                                            │
│    What happens next. A specific date, a specific person, a  │
│    specific decision. Never "we look forward to discussing." │
└─────────────────────────────────────────────────────────────┘
```

**Persona tailoring rules:**

- For a procurement-led buy, lead PROOF with comparables and pricing structure.
- For a CDO-led buy, lead PROOF with technical references and migration timelines.
- For a board-driven buy, lead PROOF with strategic outcomes and risk-reduction.
- Quote at least one specific number the customer used (RFP page, evaluation criterion, scale figure).

---

## 8. Customer language — "you" before "we"

Almost every losing proposal is "we-heavy". Almost every winning proposal is "you-heavy".

**Rule:** First word of every paragraph should be about the customer or their world, not about us. If your draft starts paragraphs with "Our", "We", "BTS-Synthetic", flip them.

Conversion examples:

| Self-focused (kill it) | Customer-focused (use it) |
|---|---|
| "We have 8 years of experience in lakehouse architecture." | "Acme's 280 TB workload requires the kind of architectural maturity we have refined since 2018." |
| "Our pricing is competitive." | "Acme's 5-year cost certainty is the lens we have priced for." |
| "We support Power BI." | "Your 600 Power BI users keep their interface — and gain query performance — on day one." |
| "BTS-Synthetic offers 99.95% SLA." | "Acme's manufacturing operations have 8.76 hours of permitted downtime per year under our SLA, recovered automatically across our active-active EU region." |

Test: read the draft aloud. If it sounds like a brochure, it is. If it sounds like a letter written *to* the buyer, you're there.

---

## 9. Ghosting — argue against competitors without naming them

APMP-grade competitive positioning is rarely explicit. You characterise competitors by category and let the reader recognise them. This protects you from being accused of negative selling while still landing the point.

Patterns (drawn from the competitive-intel skill, generalised):

| What you mean | How to say it (ghosted) |
|---|---|
| Databricks compute costs creep | "Acme's cost-of-ownership should be predictable for five years — not subject to compute-spend escalation that surprises CFOs in year two." |
| Microsoft Fabric is bundled-free but immature | "Bundled-with-licence offers carry hidden costs: consultancy hours to fill maturity gaps, and exit costs when those gaps prove structural." |
| Snowflake bolted-on ML | "Acme's predictive maintenance roadmap needs ML built into the platform's foundations, not added as a separate product on top." |
| Generic forklift migration risk | "Teradata-to-Lakehouse migrations that require simultaneous re-platforming of every dependent system have a poor delivery record. Ours decouples migration from disruption." |

**Rule:** Ghost the *category of weakness*, not the *competitor*. Name competitors only in the competitive section or when the customer has named them first in the RFP.

---

## 10. Action-caption discipline — every visual carries a benefit

A visual without a caption is wasted real estate. A caption that describes the visual is wasted too. **Captions carry the argument forward.**

| Caption type | When | Example |
|---|---|---|
| **Bad** (descriptive) | Never. | "Figure 1: Solution architecture." |
| **Good** (action-caption) | Always. | "Figure 1: Acme's Power BI users keep their existing dashboards while query performance improves 3–10× on the lakehouse layer underneath." |

Rule: every table, figure, and diagram caption is a one-sentence argument with a benefit. If you cannot write a benefit caption for a visual, the visual probably doesn't belong.

---

## 11. Compliance matrix — non-negotiable

For RFPs with explicit shall/must/will language and an evaluation grid, you produce a compliance matrix. It is the cheapest scoring you can earn.

Format:

| RFP section | Requirement (verbatim) | Compliant? | Where addressed | Reviewer note |
|---|---|---|---|---|
| 2.3 | "Native Power BI integration" | **Full** | §3.2 (Technical Solution) | DirectQuery adapter, certified |
| 4.3 | "99.99% monthly uptime" | **Alternative offered** | §5.4 (SLA) | 99.95% standard / 99.99% optional architecture; documented |
| 4.1 | "Uncapped liability" | **Counter-position** | §6.2 (Contract Approach) | 24-month cap + $5M cyber + carve-outs |

**Rule:** Never claim "Full" compliance on something where there is a meaningful difference. APMP NPI doctrine — be honest, frame the alternative, win the trust.

---

## 12. Negative Past Information (NPI) — disclose, don't hide

If you have a known weakness, gap, or past stumble that the customer will discover, **address it before they find it**. The proposal that pretends weaknesses don't exist loses on discovery. The proposal that names the gap and explains the mitigation wins on credibility.

Pattern:

> "Acme's RFP specifies sub-100ms streaming latency. Our platform consistently delivers 250ms–1s on streaming queries — sufficient for predictive maintenance and operational reporting, where the underlying physical event horizon is measured in seconds. For the small subset of workloads requiring sub-100ms (e.g., interactive analyst exploration), we recommend a hybrid pattern using our in-memory cache layer, which we have deployed at Initech Sensors for the same use case."

Notes:
- Stated honestly ("250ms–1s").
- Re-framed to what matters ("the physical event horizon is seconds").
- Mitigated with a specific architectural answer.
- Backed by a named reference.

---

## 13. Briefing the specialists — give them the strategy

When you delegate to specialists (pricing, legal, technical fit, competitive), do not pass them only the RFP. Pass them:

1. The win themes (numbered) — they must align their output to one or more themes.
2. The persona map — they must write for the right reader.
3. The compliance items relevant to their lane.
4. A specific **output spec**: word count, structure, customer-language requirement, named-proof requirement.

Template briefing:

> "[Specialist], here are the five win themes for this bid. Your work supports WT[n] primarily and WT[n] secondarily. Your reader is [persona]. Produce: (a) your internal deal-desk position in your usual format, and (b) a customer-facing narrative block, ~[N] words, written in 'you'-voice, naming at least one proof point. Align every claim to one of the win themes; if a claim cannot be aligned, cut it."

If you do not brief specialists with the strategy, you will get five excellent siloed outputs that do not assemble into a coherent argument.

---

## 14. Colour-team quality gate — 10 questions before you finalise

Before producing the document, run the proposal through this gate. If you cannot answer "yes" to any of these, fix that thing before finalising.

1. **Win themes** — Can you state all five win themes in one sentence each, without looking at the document?
2. **Hot buttons** — Does the executive summary mention each top-three hot button in the customer's own language?
3. **Personas** — Does each section speak to its primary reader? (Test: would the CFO get value from the exec summary alone? Would the CDO defend the technical section to their architecture board?)
4. **Discriminators** — Are at least three discriminators stated with proof — not as claims, as evidence?
5. **Ghosting** — Is each competitor's category-of-weakness referenced at least once, without naming them?
6. **Compliance** — Is the compliance matrix complete? Are all "alternative offered" rows explained?
7. **NPI** — Are known gaps disclosed and reframed *before* the customer finds them?
8. **Customer voice** — Does the draft use "you / your / Acme" more than "we / our / BTS-Synthetic"? (Quick test: ctrl-F count.)
9. **Action captions** — Does every visual carry a benefit caption, not a descriptive one?
10. **Call to action** — Does the proposal end with a specific decision, a specific person, and a specific date?

A bid that fails three or more of these is a 30-day fix, not a Gold-team review. Fix it.

---

## 15. The output you produce

When you finalise the proposal document, it must contain — in this order:

1. **Branded cover** with customer name, RFP reference, and submission date.
2. **Executive summary** (one page, persona-tailored, structured per §7).
3. **Our understanding of [Customer]'s need** (frames hot buttons, in customer language).
4. **Why [Customer] needs [our category of solution]** (sets up the win themes without yet selling us).
5. **Why us — the [Customer]-specific case** (themes-first, discriminators-with-proof).
6. **Technical solution** (capability-to-outcome, fit matrix, NPI on gaps).
7. **Commercial proposal** (anchor-on-TCO, value-first, then headline numbers).
8. **Contract approach** (every counter-position framed as customer-de-risking).
9. **Implementation plan** (phased, anchored to past wins, named risk register).
10. **Compliance matrix** (full, honest).
11. **References and proof points** (named, with permission, with metrics).
12. **Next steps** (specific date, specific person, specific decision).

Every section opens with its theme as a one-line claim. Every visual carries a benefit caption. Every page passes the "you-voice" test.

---

## 16. Anti-patterns — things that will lose you the bid

If you find any of these in the draft, fix them before finalising:

- **The capability dump** — listing what you do, not what the customer gets.
- **The "we" wall** — paragraph after paragraph starting with "Our" or "We".
- **The siloed sections** — pricing speaks pricing, legal speaks legal, technical speaks technical, with no shared narrative.
- **The undifferentiated executive summary** — generic claims any competitor could make.
- **The hidden gap** — known weakness not disclosed; will lose on discovery.
- **The descriptive caption** — visuals not earning their space.
- **The compliance lie** — "Full" claims on things that are partial.
- **The missing call to action** — "We look forward to discussing further."
- **The unaligned specialist output** — pricing/legal/technical/competitive each writing for themselves, not for the win themes.

If you do this work properly, the document will read like one person wrote it — a senior, customer-facing person who has been listening carefully to what the buyer actually needs.
