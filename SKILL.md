---
name: ad-campaign-runbook
description: >
  Write a LinkedIn Ads campaign runbook for one blog post: goals and metrics, a
  code-and-live probe of what the site can actually measure, budget-derived campaign
  structure, audience, ad copy traceable to the post, an organic companion post with
  author-only fact slots, UTM and conversion tracking, click-by-click Campaign Manager
  steps, cadence, tracking sheet and post-mortem template. Use when: (1) a blog post,
  case study or manifesto page should get paid LinkedIn promotion, (2) an earlier
  campaign runbook exists and the next post needs its own, (3) the user mentions: ads
  runbook, ad campaign for this post, LinkedIn ads for the blog post, promote this
  post, campaign runbook, Campaign Manager instructions, ad copy for the post, "create
  a runbook like the last one". REQUIRES the path to the post's .md file as its
  argument and refuses to run without it. One post, one campaign; budget decides the
  structure. LinkedIn only; not an organic posting skill and not an ads API client.
argument-hint: "<path/to/blog-post.md> [monthly budget + currency]"
---

# Ad Campaign Runbook

Turns one blog post into a runbook a marketer can execute without the author in the
room. The insight that shapes it: **at small B2B budgets the plan is decided by
arithmetic and by what the site can measure, not by the funnel you would like to
draw.** So the skill measures first, does the sums, and only then writes copy.

## Required input

```
/ad-campaign-runbook <path/to/blog-post.md> [monthly budget + currency]
```

**The blog post path is mandatory.** If it is missing, is not a file, or is not
markdown: stop, say what is missing, and ask for it. Never choose a post yourself,
never fall back to the "latest" one, never work from a URL or a summary. Enforce it
with the preflight, which exits `2` when the post is unusable:

```bash
python3 <skill-dir>/scripts/preflight.py <post.md> [--cta /path] [--site https://site]
```

## When to use

- A post with a real offer in it should get paid LinkedIn traffic.
- The host already has one campaign runbook and the next post needs the same.
- Someone asks for ad copy, UTMs or Campaign Manager steps for a specific post.

## When NOT to use

- **Writing or publishing organic LinkedIn posts or comments**: the
  `linkedin-marketing` skill owns that. This skill drafts one organic companion post
  and hands it to that skill's audit.
- **Writing the blog post itself**: `blog-markdown` and the host's content workflow.
- **Meta, Google or X ads**: not covered; see [provenance.md](references/provenance.md).
- **Creating campaigns through an ads API**: this produces a document for a human.
- **A post with no offer or next step**: fix the post first. Say so.

## Flow

```
post.md (required) ─► preflight ─► host probe ─► ask inputs ─► strategy math
                                                                    │
      index + verify ◄─ write runbook ◄─ audit copy ◄─ creative ◄───┘
```

## Critical facts

1. **Budget decides structure.** LinkedIn's daily minimum per campaign is about 10 USD.
   A monthly budget under roughly 1,400 EUR funds one campaign properly, not a funnel.
2. **An installed tag is not conversion tracking.** A base tag records page views.
   Check for a track call, UTM storage, consent gating and redirects that drop query
   strings before promising any measurement.
3. **Small budgets produce 0 to 3 conversions a month.** Write that range down. Steer
   monthly by CTR, CPC and engaged reads; judge conversions over three months.
4. **Cold ads point at the post, not at the conversion page.** Sign-in walls and long
   forms bounce cold clicks, and the post is what persuades.
5. **Only 140 characters of an ad show on mobile.** The reason to care goes there.
6. **An ad blocker breaks both the tag test and the ad platform's UI.** A 1 ms failed
   request and blank Campaign Manager pages are the tell. Use a clean profile.
7. **A page-load conversion id cannot be used in a track call.** Event-specific
   conversions issue their own id.
8. **Audience expansion and Audience Network are on by default.** Both must be off.

## Hard rules

> **Never run without the post file.** Which content gets the budget is the user's
> decision. A confident runbook for the wrong post is worse than none.

> **Never write a claim the post does not make.** Every ad sentence traces to a post
> sentence, and the post's own caveats bind the ads.

> **Never invent a budget, a benchmark or a fact about the author.** Budgets come from
> the user. Planning numbers are labelled as assumptions. Personal facts in the
> organic post stay as marked slots for the author.

> **Never assume tracking works.** Probe the code and the live page, date the
> findings, and list the gaps as tickets.

> **Never change the ad account without an explicit yes for that action.** Reading a
> signed-in session is fine. Creating objects accepts terms on the user's behalf:
> fill the form, stop at review, show what will be created.

> **Never leave a placeholder or a stale fact in the finished runbook.** Grep for
> `{{`, and reread sections 2, 5 and 6 against what is true today.

## Quick start

1. **Preflight** the post; stop on exit `2` — [inputs.md](references/inputs.md)
2. **Probe the host**: tag, consent, conversion events, UTMs, the path from click to
   conversion, earlier runbooks — [host-probe.md](references/host-probe.md)
3. **Ask for inputs** in one batch: budget and currency, goals, countries, organic
   author, ad account — [inputs.md](references/inputs.md)
4. **Do the strategy math**: campaign count, live ads, expected clicks and
   conversions, audience, decision rules — [strategy.md](references/strategy.md)
5. **Write the creative**: offer, proof points, angles, five ads, the organic post
   with author slots, landing page fixes — [creative.md](references/creative.md)
6. **Specify tracking**: UTMs, conversions, event code if the host lacks it, tickets —
   [conversion-tracking.md](references/conversion-tracking.md)
7. **Write the build steps** with the host's names and UI language —
   [campaign-manager.md](references/campaign-manager.md)
8. **Assemble the runbook** from the template, keep the section numbers —
   [runbook-template.md](references/runbook-template.md)
9. **Audit and verify**: traceability, 140-character hooks, no `{{`, formatter, and
   add the runbook to the host's docs index — [creative.md](references/creative.md)

Optional: implement the conversion event in the host when the probe shows none and
the user asks for it. It is a code change, so follow the host's test and lint setup.

## Reference directory

| Scenario | Trigger keywords | Reference |
| :-- | :-- | :-- |
| Enforcing the required post, what to ask, every placeholder | required parameter, preflight, missing post, inputs, budget, currency, placeholders | [inputs.md](references/inputs.md) |
| Finding out what the site measures | Insight Tag, lintrk, consent, UTM, redirect drops query, CSP, ad blocker, Inactive conversion, live check | [host-probe.md](references/host-probe.md) |
| Sizing the plan | budget, daily minimum, campaign count, CPC, CTR, audience size, geography, decision rules, cadence | [strategy.md](references/strategy.md) |
| Writing ads and the organic post | offer, proof points, angles, hook, 140 characters, headline, image spec, founder post, author slots, first comment, audit | [creative.md](references/creative.md) |
| UTMs, conversions and event code | utm_content, conversion_id, event-specific, page load, consent at fire time, dedupe, attribution, baseline | [conversion-tracking.md](references/conversion-tracking.md) |
| Building it in the ad platform | Campaign Manager, campaign group, audience expansion, Audience Network, manual bidding, Accelerate, matched audiences, 300 members | [campaign-manager.md](references/campaign-manager.md) |
| The document to produce | template, sections, runbook structure, post-mortem, tracking sheet, appendix | [runbook-template.md](references/runbook-template.md) |
| What was proven and what was added | provenance, source, fixed defects, kept deliberately, not covered | [provenance.md](references/provenance.md) |
