# Provenance

The engineering ledger for this skill: what the audit of the earlier implementation changed and how the
procedure holds it, what was kept on purpose with the reason it is safe, and what was designed here and has
never been run. It is written for the person editing the skill, not for the reader of the README. Read it
before simplifying anything.

The earlier implementation was a LinkedIn ads runbook for a B2B marketing site: Next.js, consent-gated
analytics, a sign-in wall between the ad click and the conversion. It was revised four times against the
site's code, the live page and a real ad account, and its organic companion post was audited with an
organic-LinkedIn skill. **What the procedure and the template carry is what survived those revisions. No
campaign built from this skill has completed a run, so every performance number in the references is a
planning assumption and is labelled as one.**

Seven entries below are fixed defects, seven are deliberate keeps, three are additions.

## Fixed

### 1. A funnel the budget could not feed

The first plan had four campaigns, two cold audiences, a sponsored founder post and retargeting, sized for
several times the budget that existed. Each would have sat near the platform's daily minimum, where a
campaign cannot bid its way to a judgeable sample. **Held by:** campaign count is arithmetic on the daily
minimum, and the default is one post, one campaign. See [strategy.md](strategy.md).

### 2. Tracking taken on trust

The tag was installed, so conversions were taken to work. The probe found a base tag and nothing else: no
conversion event anywhere, no UTM stored, tag and analytics both behind consent, and an auth redirect that
rebuilt the URL before any page rendered. **Held by:** the probe is a mandatory step and its findings are a
dated section of every runbook. See [host-probe.md](host-probe.md).

### 3. An ad blocker read as a site defect

The tag reported an error and one request failed in about a millisecond, too fast for a network round trip.
The cause was the tester's own ad blocker, confirmed when the ad platform's UI showed its warning banner and
rendered blank pages. **Held by:** the failure mode table, and the rule that all ad account work happens in a
browser profile without a blocker.

### 4. An organic post that read as a company pitch

The first draft carried the link in the body, no named or dated moment, no number with a referent, three
stacked lists of three, a close that pitched the link, and an instruction for colleagues to reshare at once.
**Held by:** author slots the agent must not fill, the first-comment link rule, staggered comments in place
of reshares, and an audit step before publication. See [creative.md](creative.md).

### 5. Hooks that spent the visible characters on nothing

One ad opened on a quoted line of jargon, so the 140 characters a phone shows carried no reason to care.
Another used a "not X, your Y" contrast frame in both intro and headline. **Held by:** the copy rules and the
140-character print check in the creative audit.

### 6. Facts that went stale inside one session

The sections describing the ad account and the site's code aged as conversions were created and code shipped
the same day, and the post's length was written from memory and was wrong by more than a tenth. **Held by:**
the preflight reports measured facts, and the verification step rereads the runbook against them before it is
handed over.

### 7. A page-load conversion id nearly used in a track call

The account's only conversion was a URL rule, whose id an event-specific track call cannot use. **Held by:**
the distinction, and the instruction to copy only the number an event-specific conversion issues, in
[conversion-tracking.md](conversion-tracking.md).

## Kept deliberately

- **Cold traffic goes to the post, not to the conversion page**, although the conversion is the goal. The
  conversion sat behind an email sign-in, the post is what persuades, and the post serves the page view goal
  at the same time.
- **Traffic objective, not conversions.** It looks like leaving optimisation on the table. With a few
  conversions a month there is nothing for the platform to optimise on.
- **Three live ads, not five.** More ads on this budget means none of them reaches a sample anyone can judge
  inside a month.
- **No changes in the first three weeks.** It feels passive. At this spend, an earlier change is a reaction
  to noise.
- **Planning numbers stay, labelled as assumptions.** Without them the "what this budget buys" arithmetic
  cannot be done, and that arithmetic is what sized the plan down to one campaign.
- **Section numbers in the template are fixed.** The next post's runbook is a copy of the last one, and
  people cite "5.2" in conversation.
- **The blog post path is required and never defaulted.** Which content gets the budget is the user's
  decision, and a confident runbook for the wrong post is worse than none.

## Added

Designed in this skill and never run in the earlier implementation. Marked as such because the skill's
credibility is that it tells the two apart.

- `assets/preflight.py`. The earlier implementation was read by hand. The script was run against that post
  afterwards and reported the same two landing page problems the hand reading had found.
- The budget bands table in [strategy.md](strategy.md), generalised by arithmetic from one budget at one
  platform minimum. Recompute the bands when the minimum or the exchange rate moves. The clause that a
  retargeting campaign whose audience is still under 300 members is planned, built and switched on when it
  passes them came from the 0.1.1 agent evals, where two agents of three parked it at 2,000 EUR. It has not
  been run either.
- The generic identifiers in the conversion code. The shipped code used the host's own vocabulary; the
  generic version compiles under `strict` but has no history under those names.

## Not covered

LinkedIn is the only channel. Meta, Google and X have their own minimums, objectives, formats and build
steps, and writing them by analogy would be invention. The strategy, probe, creative and tracking references
are channel-neutral in principle and untested beyond LinkedIn.

## Repairing a runbook written without this skill

Fix order, most damaging first: budget against campaign count, the tracking probe, the destination of cold
ads, the audience expansion and Audience Network defaults, claim traceability, the organic post's link
placement and author slots, then stale facts.
