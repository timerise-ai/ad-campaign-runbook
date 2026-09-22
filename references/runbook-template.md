# The runbook template

Copy everything below the line into `{{RUNBOOK_FILE}}` and replace every
placeholder. Placeholders are defined in [inputs.md](inputs.md). Tables marked as
blocks come from the other references; do not shorten them to a sentence.

Keep the section numbers. People refer to "5.2" and "3.5" in conversation, and the
next post's runbook is a copy of this one.

What may be dropped: nothing structural. What must be adapted: every number, every
name, every claim. A section that does not apply stays, with one line saying why.

---

# Runbook: LinkedIn Ads for "{{POST_TITLE}}"

**Type:** Campaign runbook (strategy, creative spec, Campaign Manager steps, operating cadence)
**Model:** one blog post, one LinkedIn campaign
**Budget:** {{MONTHLY_BUDGET}} {{CURRENCY}} per month
**Source content:** `{{POST_PATH}}`, live at `{{POST_URL}}`
**Owner:** Marketing (campaign), Sales ({{CONVERSION_NAME}} qualification)
**Status:** Draft, not launched
**Last updated:** {{TODAY}}

> How to use this file: sections 1 to 5 are the spec and are decided once. Section 6 is
> the click-by-click build in LinkedIn Campaign Manager. Sections 7 to 9 are what you run
> while the campaign is live. For the next blog post, follow the appendix.

## 1. Goals and what we measure

Two goals, in order of funnel depth: page views of the post by plausible buyers, and
{{CONVERSION_NAME}}s created, with the share Sales accepts.

Metric table: post sessions from ads, landing page clicks, engaged reads,
{{CONVERSION_NAME}} started, **created**, **qualified** ({{QUALIFIED_DEFINITION}}),
cost per each. For every metric name its definition and its **source of truth**.
Conversion counts come from the host's own data, never from the ad platform alone.

State what "value" means: qualified conversions and their cost, not raw count.

### Planning assumptions (replace with actuals after month 1)

The assumptions table from strategy, in {{CURRENCY}}: CPC {{CPC_LOW}} to {{CPC_HIGH}},
CTR, click to engaged read, reader to started, started to completed
({{CONVERSION_FRICTION}}). Label them as assumptions or cite the post-mortem they
come from.

**What {{MONTHLY_BUDGET}} {{CURRENCY}} buys:** {{CLICKS_LOW}} to {{CLICKS_HIGH}} clicks
a month and the resulting conversion range. If that range includes zero, say so, and
name the signals that can be trusted monthly.

## 2. What the site can and cannot measure today

Dated. A short paragraph on the live check, then:

{{TRACKING_FACTS_TABLE}}

Close with two short paragraphs: what works with zero code changes, and what needs an
engineering ticket.

## 3. Strategy

### 3.1 The offer

{{OFFER}}

Proof points allowed in ads, all taken from the post: {{PROOF_POINTS}}

Honesty constraints that ads must not contradict: {{HONESTY_CONSTRAINTS}}

Follow `{{BRAND_RULES_FILE}}`.

### 3.2 Campaign model

An ASCII tree: the campaign group with its cap, {{CAMPAIGN_COUNT}} campaign(s), and
{{LIVE_ADS}} live ads. Then the reasons, as bullets: one objective and destination;
ads never point at `{{CONVERSION_PATH}}` and why; traffic objective and why; the
group holds the budget; default run {{RUN_WEEKS}} weeks ({{RUN_BUDGET}} {{CURRENCY}})
with two reviews. Name what is left out on purpose.

### 3.3 Audience

{{AUDIENCE_BLOCK}}

**Geography.** Start: {{COUNTRIES_START}}. Held back: {{COUNTRIES_HELD}}, with the
reason, stated as an assumption to check in the forecast panel.

Exclusions and target size.

### 3.4 Budget

A period table: setup week, weeks 1 to 3, mid-run review, second half, end-of-run
review, each with the daily budget ({{DAILY_BUDGET}} {{CURRENCY}}) and what happens.
One line on the platform's daily minimum in {{CURRENCY}}.

### 3.5 Decision rules

The decision rules table from strategy, with this host's thresholds.

### 3.6 Not in this plan, and when to revisit

Parked tactics, each needing a second campaign, with the monthly budget at which to
revisit.

## 4. Creative and content spec

### 4.1 Messaging angles

{{ANGLES_TABLE}}

### 4.2 Format spec

The spec table and the visual direction bullets.

### 4.3 Ad copy

Which three launch and which two are reserve, then:

{{ADS_TABLE}}

**Organic companion post (no spend).** The warning about empty or invented slots,
then:

{{ORGANIC_POST}}

Then the publishing rules table and, if used, the document post outline.

### 4.4 Landing page work (content, not ads)

The post is about {{POST_WORDS}} words and it is the landing page.

{{LANDING_FIXES}}

Ship before day 1.

## 5. Tracking prerequisites

### 5.1 UTM convention

The scheme with `utm_campaign=post-{{SHORT_SLUG}}`, a full example URL for the first
ad, and the organic URL.

### 5.2 Conversions

{{CONVERSIONS_TABLE}}

With each conversion's state: exists (with id), to create, or code ready.

### 5.3 Engineering tickets

{{TICKETS_TABLE}}

### 5.4 Reporting without UTM capture

The likely-not-confirmed matching procedure.

## 6. LinkedIn Campaign Manager instructions

Account: {{AD_ACCOUNT}}.

6.1 Account preflight, 6.2 Conversions, 6.3 Audiences, 6.4 Campaign group, 6.5 The
campaign, 6.6 Pre-launch checklist: the steps from the Campaign Manager reference,
with this host's names, labels in the account's UI language, and numbers. Mark what
already exists so nobody creates it twice.

## 7. Operating cadence while live

A table: day 1 and 2, Monday check, mid-run review, end-of-run review. The rule about
never editing a live ad.

## 8. Tracking sheet

Two tabs, columns listed: "Ads" (one row per ad) and "Monthly" (one row per post
campaign per month). Say which columns come from the host's data, and give the way to
count conversions there:

{{BASELINE_QUERY}}

## 9. Post-mortem template

Numbers against baseline; assumptions versus actuals; best and worst ad with a guess
at why; audience findings; page findings; the decision; what to change in the runbook.
Commit it beside the runbook as `<runbook name>-results.md`.

## Appendix: the next blog post's campaign

What already exists, then the steps: run the skill with the new post's path; carry
actuals forward; rebuild offer, angles and ads from the new post; check the post
against 4.4; draft and audit the organic post; new `utm_campaign`; start Campaign
Manager at 6.5 from the saved audience template; pause the previous campaign unless
the review said to keep it. Candidates: {{NEXT_CANDIDATES}}
