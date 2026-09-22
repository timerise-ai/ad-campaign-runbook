# Provenance

Extracted in September 2026 from one working session that produced a LinkedIn ads
runbook for a B2B marketing site (Next.js, consent-gated analytics, a sign-in wall in
front of the conversion). The runbook went through four revisions in that session,
was checked against the site's code, the live page and the real ad account, and was
audited with an organic-LinkedIn skill. **Fidelity claim: the procedure and template
are what survived those revisions. No campaign built from it has completed a run yet,
so every performance number here is a planning assumption, not a result.**

## Fixed in the templates

### 1. A funnel the budget could not feed

The first draft had four campaigns (two cold audiences, a sponsored founder post,
retargeting) sized for a budget four times the real one. At the real budget each
campaign would have sat near the platform's daily minimum and learned nothing.
**Shipped:** campaign count is derived from arithmetic on the daily minimum, and the
default is one post, one campaign. See [strategy.md](strategy.md).

### 2. Tracking assumed, not checked

The tag was installed, so conversions were assumed to work. The probe showed a base
tag only: no conversion event anywhere, no UTM stored, the tag and analytics both
consent-gated, and an auth redirect that dropped the query string before any page
rendered. **Shipped:** the probe is a mandatory step and its findings are a dated
section of every runbook. See [host-probe.md](host-probe.md).

### 3. A site defect that was an ad blocker

The tag reported an error and one request failed. The cause was the tester's ad
blocker, confirmed when the ad platform's own UI showed a warning banner and rendered
blank pages. **Shipped:** the failure mode table, and the rule to do all account work
in a clean browser profile.

### 4. The organic post failed its audit

The first draft put the link in the body, had no named or dated fact, no number with
a referent, three stacked lists of three, and closed on a link pitch. It also told
colleagues to reshare, all at once. **Shipped:** author slots that the agent must not
fill, the first-comment link rule, staggered comments in place of reshares, and an
audit step. See [creative.md](creative.md).

### 5. Two ads with weak or flagged hooks

One opened on a quoted line of jargon, so the 140 characters visible on mobile carried
no reason to care. One used a "not X, your Y" contrast frame in both intro and
headline. **Shipped:** the copy rules and the 140-character print check.

### 6. Stale facts after in-session changes

Sections describing the ad account and the code fell out of date as conversions were
created and code shipped the same day, and the post's length was stated from memory
(1,100 words; the file has 987). **Shipped:** the preflight reports measured facts,
and the verification step rereads the runbook against them.

### 7. A page-load conversion id nearly reused for an event

The account's only conversion was a URL rule. Its id cannot be used in a track call.
**Shipped:** the distinction in [conversion-tracking.md](conversion-tracking.md).

## Kept deliberately

- **Cold traffic goes to the post, not to the conversion page**, even though the
  conversion is the goal. The conversion sat behind an email sign-in; the post is
  what persuades, and it serves the page view goal too.
- **Traffic objective, not conversions.** It looks like leaving optimisation on the
  table. With a few conversions a month there is nothing to optimise on.
- **Three live ads, not five.** More ads means none reaches a judgeable sample.
- **No changes in the first three weeks.** It feels passive. At this spend, earlier
  changes are reactions to noise.
- **Planning numbers stay in, labelled as assumptions.** Removing them would make the
  "what this budget buys" arithmetic impossible, and that arithmetic is what stopped
  the oversized funnel.
- **Section numbers are fixed.** The next runbook is a copy; people cite "5.2".
- **The blog post path is required and never defaulted.** Which content gets the
  budget is the user's decision.

## Added

Marked because they were designed at a desk, not proven in the source session:

- `scripts/preflight.py`. The source session read the post by hand. The script was
  tested on the source post and found the same two landing page problems.
- The budget bands table in [strategy.md](strategy.md), generalised from one budget.
- The generic names in the conversion code. The shipped code used the host's
  vocabulary; the generic version was compiled under `strict` but has no production
  history under those names.

## Not covered

LinkedIn is the only channel here. Meta, Google and X would need their own build
steps, minimums and specs; adding them by analogy would be invention. The strategy,
creative, probe and tracking references are channel-neutral in principle, and
untested beyond LinkedIn.

## If you are repairing a runbook written without this skill

Fix order, most damaging first: budget against campaign count; tracking probe;
destination of cold ads; audience expansion and Audience Network defaults; claim
traceability; organic post link placement and slots; stale facts.
