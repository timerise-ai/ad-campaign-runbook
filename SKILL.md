---
name: ad-campaign-runbook
description: >
  Write a LinkedIn Ads campaign runbook for one blog post: goals and metrics, a
  code-and-live probe of what the site can actually measure, budget-derived
  campaign structure, audience, ad copy traceable to the post, an organic
  companion post with author-only fact slots, UTM and conversion tracking,
  click-by-click Campaign Manager steps, operating cadence, tracking sheet and
  post-mortem template. Use when: (1) a blog post, case study or manifesto page
  should get paid LinkedIn promotion, (2) a runbook already exists and the next
  post needs its own, (3) the user mentions: ads runbook, ad campaign for this
  post, LinkedIn ads for the blog post, promote this post, campaign runbook,
  Campaign Manager instructions, ad copy for the post, utm_content, Insight Tag,
  lintrk, conversion tracking for ads, "a runbook like the last one". Carries the
  arithmetic that sizes the plan to the budget, a probe that establishes what the
  site measures before anything is promised, copy traceable sentence by sentence
  to the post, and the platform defaults that leak budget when left on. Takes the
  path to the post's markdown file as a required argument and stops without it.
  Written for a Next.js App Router marketing site whose posts are markdown in the
  repository; the host's analytics vendor, consent component, conversion
  vocabulary and runbook folder are the seam. LinkedIn only. Not an organic
  posting skill, not an ads API client, and not a writer of the blog post itself.
---

# Ad campaign runbook: one post, one campaign

Turns one blog post into a runbook a marketer can execute without the author in the room. The idea the whole
design turns on: **at small B2B budgets the plan is decided by arithmetic and by what the site can measure,
not by the funnel you would like to draw.** So the skill measures first, does the sums, and writes copy last.

## Required input

```
/ad-campaign-runbook <path/to/blog-post.md> [monthly budget + currency]
```

**The blog post path is mandatory.** If it is missing, is not a file, or is not markdown: stop, say what is
missing, and ask for it. Never choose a post, never fall back to the latest one, never work from a URL or a
summary. The preflight enforces it and exits `2` when the post is unusable:

```bash
python3 <skill-dir>/assets/preflight.py <post.md> [--cta /path] [--site https://site]
```

## When to use

- A post with a real offer in it should get paid LinkedIn traffic.
- The host already has one campaign runbook and the next post needs the same.
- Someone asks for ad copy, UTMs or Campaign Manager steps for a specific post.

## When NOT to use

- **Writing or publishing organic LinkedIn posts or comments**: the `linkedin-marketing` skill owns that.
  This skill drafts one organic companion post and hands it to that skill's audit.
- **Writing the blog post itself**: `blog-markdown` and the host's content workflow.
- **Meta, Google or X ads**: not covered, see [provenance.md](references/provenance.md).
- **Creating campaigns through an ads API**: this produces a document for a human to execute.
- **A post with no offer or next step**: fix the post first, and say so.

## Architecture

```
/ad-campaign-runbook <post.md> [budget]
        |
        +- assets/preflight.py ... required post, measured facts, landing warnings (exit 2: stop and ask)
        |
        +- host probe ............ tag, consent, conversion events, UTMs, the path from click to conversion
        |
        +- inputs, one batch ..... budget and currency, goals, countries, organic author, ad account
        |
        +- strategy math ......... campaign count, live ads, clicks, conversion range, audience, decisions
        |
        +- creative .............. offer, proof points, angles, five ads, organic post with author slots
        |
        +- tracking spec ......... UTMs, conversions, the client-side event, engineering tickets
        |
        +- build steps ........... Campaign Manager, once per account and once per post
        |
        v
   <channel>-ads-<short slug>.md in the host's runbook folder, audited, then added to the docs index
```

The preflight is the only executable file and it reads the post, nothing else. The probe reads the host's
code and one live page. Everything after it is written by the agent into one file whose section numbers are
fixed, because the next post's runbook is a copy of this one and people cite sections by number.

## Critical facts

1. **Budget decides structure.** LinkedIn's daily minimum per campaign is about 10 USD. A monthly budget
   under roughly 1,400 EUR funds one campaign properly, not a funnel.
2. **An installed tag is not conversion tracking.** A base tag records page views. Check for a track call,
   UTM storage, consent gating and redirects that drop query strings before promising any measurement.
3. **Small budgets produce 0 to 3 conversions a month.** Write that range down. Steer monthly by CTR, CPC and
   engaged reads, and judge conversions over a rolling three-month window.
4. **Cold ads point at the post, not at the conversion page.** Sign-in walls and long forms bounce cold
   clicks, and the post is what persuades.
5. **Only 140 characters of an ad show on mobile.** The reason to care goes there.
6. **An ad blocker breaks both the tag test and the ad platform's UI.** A failed request in about a
   millisecond and blank Campaign Manager pages are the tell. Use a clean browser profile.
7. **A page-load conversion id cannot be used in a track call.** Event-specific conversions issue their own
   id, and only the number is copied.
8. **Audience expansion and Audience Network are on by default.** Both are unticked at build time.

## Hard rules

> **Never run without the post file.** Which content gets the budget is the user's decision. A confident
> runbook for the wrong post is worse than none.

> **Never write a claim the post does not make.** Every ad sentence traces to a post sentence, and the post's
> own caveats bind the ads.

> **Never invent a budget, a benchmark or a fact about the author.** Budgets come from the user. Planning
> numbers are labelled as assumptions. Personal facts in the organic post stay as slots for the author.

> **Never assume tracking works.** Probe the code and the live page, date the findings, and list the gaps as
> tickets.

> **Never change the ad account without an explicit yes for that action.** Reading a signed-in session is
> fine. Creating objects accepts terms on the user's behalf: fill the form, stop at review, show what will be
> created.

> **Never leave a placeholder or a stale fact in the finished runbook.** Grep for `{{`, and reread the
> tracking, creative and build sections against what is true today.

## Quick start

1. **Preflight** the post and stop on exit `2`: [inputs.md](references/inputs.md)
2. **Probe the host** for the tag, consent, conversion events, UTMs, the path from click to conversion and
   earlier runbooks: [host-probe.md](references/host-probe.md)
3. **Ask for inputs** in one batch: budget and currency, goals, countries, organic author, ad account:
   [inputs.md](references/inputs.md)
4. **Do the strategy math**: campaign count, live ads, expected clicks and conversions, audience, decision
   rules: [strategy.md](references/strategy.md)
5. **Write the creative**: offer, proof points, angles, five ads, the organic post with author slots, landing
   page fixes: [creative.md](references/creative.md)
6. **Specify tracking**: UTMs, conversions, the event code if the host lacks one, tickets:
   [conversion-tracking.md](references/conversion-tracking.md)
7. **Write the build steps** with the host's names and UI language:
   [campaign-manager.md](references/campaign-manager.md)
8. **Assemble the runbook** from the template, keeping the section numbers:
   [runbook-template.md](references/runbook-template.md)
9. **Audit and verify**: traceability, 140-character hooks, no `{{`, then add the runbook to the host's docs
   index: [creative.md](references/creative.md) and [adaptation.md](references/adaptation.md)

Implementing the conversion event in the host, when the probe finds none and the user asks for it, is a code
change: follow the host's test and lint setup.

## Reference directory

| Scenario | Trigger keywords | Reference |
| :-- | :-- | :-- |
| What the host must provide, naming, where the runbook lives | seam, adaptation, rename, runbook folder, docs index, another channel, non-negotiables | [adaptation.md](references/adaptation.md) |
| The required post, what to ask, every placeholder | required parameter, preflight, missing post, inputs, budget, currency, placeholders | [inputs.md](references/inputs.md) |
| What the site measures | Insight Tag, lintrk, consent, UTM, redirect drops query, CSP, ad blocker, Inactive conversion, live check | [host-probe.md](references/host-probe.md) |
| Sizing the plan | budget, daily minimum, campaign count, CPC, CTR, audience size, geography, decision rules, cadence | [strategy.md](references/strategy.md) |
| Ads and the organic post | offer, proof points, angles, hook, 140 characters, headline, image spec, founder post, author slots, first comment, audit | [creative.md](references/creative.md) |
| UTMs, conversions and event code | utm_content, conversion_id, event-specific, page load, consent at fire time, dedupe, attribution, baseline | [conversion-tracking.md](references/conversion-tracking.md) |
| Building it in the ad platform | Campaign Manager, campaign group, audience expansion, Audience Network, manual bidding, Accelerate, matched audiences, 300 members | [campaign-manager.md](references/campaign-manager.md) |
| The document to produce | template, sections, runbook structure, post-mortem, tracking sheet, appendix | [runbook-template.md](references/runbook-template.md) |
| The audit ledger: what changed, was kept and was added | provenance, fixed defects, kept deliberately, added, not covered, repairing an old runbook | [provenance.md](references/provenance.md) |

Part of the [Timerise Skills](https://github.com/timerise-ai/skills) index, which lists the sibling skills.
