# Inputs and the placeholder table

One input is required and cannot be defaulted. Everything else has a default or is discovered by the host
probe.

## The required parameter: the blog post

| Rule | Why |
| :-- | :-- |
| The path to the post's `.md` or `.mdx` file must be given by the user | A runbook is a spending plan. Choosing which content gets the budget is the user's decision, never the agent's |
| No path, a path that is not a file, or a non-markdown file: **stop and ask** | Guessing the "latest" or "best" post produces a confident runbook for the wrong offer |
| A post under 300 words: stop and say so | Five distinct ad angles, each traceable to a sentence, do not exist in a short post |
| A URL instead of a file: ask for the file | Claims must be traced to the source text, not to a rendered page that may differ |

Run the preflight first. It enforces the rule and returns the facts the runbook is built from:

```bash
python3 <skill-dir>/assets/preflight.py <post.md> --cta <conversion path> --site <https://site>
```

Exit code `2` means stop. Show the user the `error` string and ask for the post. Exit code `0` prints JSON:
title, slug, URL, word count, H2 sections, image count, internal links, how many times the post links to the
conversion path and **at which word the first such link appears**. Warnings in that JSON go into the runbook's
landing page section verbatim; they are usually the cheapest wins in the whole plan.

`--cta` and `--site` are optional on the first run. Run it once without them to validate the post, do the host
probe to learn the conversion path, then run it again with both.

## Inputs to ask for

Ask in one batch, after the preflight and the host probe, so the questions can quote what was found. Skip any
the user already gave.

| Input | Ask | Default if the user declines |
| :-- | :-- | :-- |
| Monthly budget and currency | "What is the monthly ad budget, in which currency?" | None. Do not invent a budget. Write the runbook with the structure table from [strategy.md](strategy.md) for three budget levels and mark the choice open |
| Goals | "Page views, conversions, or both? What counts as a conversion worth paying for?" | Both; the conversion found by the probe; "qualified" means Sales accepted it |
| Geography and language | "Which countries? Is the site in one language?" | Countries from existing customers or case studies; the site's language as profile language |
| Who is the organic author | "Who posts the organic companion post, from a personal profile?" | A founder. Leave the facts as slots, see [creative.md](creative.md) |
| Ad account | "Does an ad account exist? Its currency?" | Assume none; the runbook's preflight section covers creating one. The account currency is permanent, so it must match the budget currency |
| Acceptable cost per qualified conversion | "What may one qualified conversion cost?" | Left as a pre-launch checklist item for Sales |

Never ask for ad account credentials, and never sign in on the user's behalf. If the user offers a signed-in
browser session, reading the account is fine; creating or changing anything in it needs an explicit yes for
that action.

## Placeholders

Every `{{NAME}}` in [runbook-template.md](runbook-template.md) is defined here. A placeholder left in a
finished runbook is a defect: the verification step greps for `{{`.

| Placeholder | Source | Example |
| :-- | :-- | :-- |
| `{{POST_TITLE}}` | preflight `title` | From Brief to Clickable Prototype in 48 Hours |
| `{{POST_PATH}}` | the required parameter, repo-relative | content/blog/en/from-brief-to-prototype.md |
| `{{POST_URL}}` | preflight `url`, confirmed live | https://example.com/blog/from-brief-to-prototype |
| `{{POST_WORDS}}` | preflight `word_count`, rounded to the nearest 50 | 1,000 |
| `{{SHORT_SLUG}}` | preflight suggestion, shortened by hand to 2 or 3 words | prototype-48h |
| `{{RUNBOOK_FILE}}` | `<channel>-ads-<short slug>.md` in the host's runbook folder | linkedin-ads-prototype-48h.md |
| `{{TODAY}}` | today's date, ISO | 2026-09-21 |
| `{{CURRENCY}}` | user input | PLN |
| `{{MONTHLY_BUDGET}}` | user input | 3,000 |
| `{{DAILY_BUDGET}}` | monthly / 30, rounded down to a round number | 100 |
| `{{RUN_WEEKS}}` | [strategy.md](strategy.md), default 8 | 8 |
| `{{RUN_BUDGET}}` | daily x 7 x run weeks | 5,600 |
| `{{CAMPAIGN_COUNT}}` | [strategy.md](strategy.md) budget table | 1 |
| `{{LIVE_ADS}}` | [strategy.md](strategy.md) impressions math | 3 |
| `{{CPC_LOW}}`, `{{CPC_HIGH}}` | planning assumption or last post-mortem | 17, 40 |
| `{{CLICKS_LOW}}`, `{{CLICKS_HIGH}}` | monthly / CPC high, monthly / CPC low | 75, 175 |
| `{{CONVERSION_NAME}}` | host probe: what the business calls it | brief |
| `{{CONVERSION_PATH}}` | host probe | /brief |
| `{{CONVERSION_FRICTION}}` | host probe: steps between click and conversion | email sign-in, then a 15 minute chat |
| `{{QUALIFIED_DEFINITION}}` | host probe or user | moved to CRM stage "qualified" |
| `{{OFFER}}` | [creative.md](creative.md), two or three sentences | |
| `{{PROOF_POINTS}}` | [creative.md](creative.md), each traceable to the post | |
| `{{HONESTY_CONSTRAINTS}}` | [creative.md](creative.md), limits the post itself states | |
| `{{BRAND_RULES_FILE}}` | host probe: content standards or style guide | docs/CONTENT_STANDARDS.md |
| `{{AUDIENCE_BLOCK}}` | [strategy.md](strategy.md) | |
| `{{COUNTRIES_START}}`, `{{COUNTRIES_HELD}}` | user input plus [strategy.md](strategy.md) | |
| `{{TRACKING_FACTS_TABLE}}` | [host-probe.md](host-probe.md) | |
| `{{CONVERSIONS_TABLE}}` | [host-probe.md](host-probe.md) and [conversion-tracking.md](conversion-tracking.md) | |
| `{{TICKETS_TABLE}}` | [conversion-tracking.md](conversion-tracking.md) | |
| `{{ANGLES_TABLE}}`, `{{ADS_TABLE}}` | [creative.md](creative.md) | |
| `{{ORGANIC_POST}}` | [creative.md](creative.md), with author slots | |
| `{{LANDING_FIXES}}` | preflight warnings plus the probe | |
| `{{AD_ACCOUNT}}` | user or a read of the account | Example Ltd, no. 123456789, PLN |
| `{{BASELINE_QUERY}}` | host probe: how conversions are counted in the host's own data | SQL or a dashboard path |
| `{{NEXT_CANDIDATES}}` | two or three other posts whose text already contains an offer | |

## Input checklist

- [ ] Preflight exited `0` on a path the user gave
- [ ] Preflight rerun with `--cta` and `--site` after the probe
- [ ] Budget and currency came from the user, not from a default
- [ ] Account currency matches budget currency, or the mismatch is written down
- [ ] Every open input is listed as open in the runbook, not silently filled
