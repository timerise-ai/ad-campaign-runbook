# Strategy: budget decides the structure

The most expensive mistake in a small B2B campaign is a structure the budget cannot
feed. Do the arithmetic before drawing the funnel.

## The model: one post, one campaign

| Rule | Why |
| :-- | :-- |
| One blog post gets one campaign, inside one always-on campaign group that holds the monthly cap | Results stay comparable post to post, and setup (account, conversions, audiences, group) is done once |
| Cold traffic goes to the post, never to the conversion page | The post does the persuading. A cold click that lands on a sign-in wall or a long form bounces |
| Objective is traffic ("Website visits"), not conversions, below roughly 15 conversions a month | Conversion optimisation with nothing to learn from delivers erratically. Attach conversions for reporting only |
| One format per campaign, single image by default | The platform enforces one format per campaign; single image is the cheapest to produce and compare |
| Posts run one after another, not in parallel | Two campaigns on one small budget each learn half as fast |

## Budget to structure

LinkedIn's minimum is about 10 USD per campaign per day. Convert to the account
currency and call it `MIN_DAILY`. Then:

```
daily            = monthly_budget / 30
campaigns        = 0 if daily < 1.2 * MIN_DAILY                  # cannot clear the platform floor: do not run paid
                   else max(1, floor(daily / (2.5 * MIN_DAILY))) # 2.5x the floor so a campaign can actually spend and bid
clicks_low/high  = monthly_budget / cpc_high , monthly_budget / cpc_low
impressions      = clicks / ctr
live_ads         = min(4, floor(impressions_low_per_month / 5000))   # each ad needs ~3,000 impressions inside a month to be judged
```

| Monthly budget, EUR equivalent | Campaigns | What to run |
| :-- | :-- | :-- |
| under 350 | 0 | Do not run paid. Put the effort into the organic post and the page |
| 350 to 1,400 | 1 | The post campaign only. Everything else is parked |
| 1,400 to 2,100 | 2 | Add retargeting to the conversion page, shared across all post campaigns |
| 2,100 to 3,500 | 3 | Add a sponsored version of the organic author's post |
| over 3,500 | 3 or 4 | Split the cold audience, add higher-bid countries, carousel or video |

The bands are arithmetic on the platform minimum, not benchmarks. Recompute them when
the minimum or the exchange rate moves.

**Worked example.** 3,000 PLN a month is about 700 EUR, so one campaign at 100 PLN a
day. At a planned CPC of 17 to 40 PLN that is 75 to 175 clicks; at 0.5% CTR, 15,000
to 35,000 impressions, so 3 live ads. At 1 to 3% post-reader to conversion start and
50 to 70% completion, that is **0 to 3 conversions a month**.

Say that last number plainly in the runbook. A month with zero conversions is inside
normal variance at this volume. The monthly signals that can be trusted are CTR, CPC,
engaged-read rate and clicks on the post's conversion links. Judge conversions on a
rolling three-month window.

## Planning assumptions

Until the host has its own history, these are **assumptions, and the runbook must
label them so**. After the first post-mortem, replace them with actuals and carry the
actuals into every later runbook.

| Assumption | Planning value | Note |
| :-- | :-- | :-- |
| CPC, sponsored content, European B2B | 4 to 9 EUR | Senior, narrow audiences sit at the top. The forecast panel's suggested bid is the first real data point |
| CTR, single image | 0.4% to 0.7% | |
| Click to engaged read | 35% to 50% | Engaged read: 75% scroll or 60 seconds |
| Post reader to conversion started | 1% to 3% | Cold traffic |
| Started to completed | depends on friction | Name the friction found by the probe |

## Audience

Build one audience from real customers, not from a persona exercise.

1. List the host's case studies and customers: industry, company size, who signed.
2. Job functions or titles of the person who owns the problem the post describes.
3. Seniority that can say yes: Manager and above.
4. Company size band that matches the case studies, widened one step.
5. Target size **50,000 to 200,000** for one campaign at small budgets. With roughly
   25,000 impressions a month, a larger audience means nobody sees the ad twice.

Geography: start with countries where bids are lower and the site's language works,
and hold the highest-bid markets back (in Europe typically the UK and DACH; the US
always as its own campaign). This is an assumption to check against the forecast
panel while building, and the runbook must say so.

Exclusions, always: the company's own employees, a contact list of customers and open
deals, people who already visited the conversion page. Add "Staffing and Recruiting"
and "Marketing Services" when demographics show agencies clicking.

Verify the facet logic in the platform's forecast panel. Whether a job-title list can
be OR-ed with job functions inside one group has changed over time; do not state it
as fact in the runbook.

## Decision rules

Write them into the runbook with the host's numbers. Rules stated before launch are
what stop mid-campaign tinkering.

| Signal | Action |
| :-- | :-- |
| Ad CTR under 0.35% after 3,000 impressions | Pause it, replace with a new variant of the best angle |
| Ad CTR over 0.8% but engaged-read rate under 25% | The hook overpromises. Rewrite the intro to match the post's opening |
| CPC above the planned high for 5 consecutive days | Widen the audience before raising the bid |
| Spend under 60% of daily budget for a week | Raise the bid 10%, or the audience is too small |
| Over 30% of clicks from agencies, recruiters, students | Add exclusions |
| 250 ad-sourced sessions and no conversion-link clicks | The problem is on the page, not in the ads |
| End of run: healthy traffic, at least one qualified conversion | Keep running, one change a month |
| End of run: healthy traffic, no conversions | Hand the budget to the next post. Pause, do not delete |
| Three months across posts, no qualified conversion | Stop paid. Invest in organic and the page |

## Cadence

Default run is 8 weeks with reviews at week 4 and week 8, a 15 minute check on
Mondays, and **no changes in weeks 1 to 3** unless spend is off by more than a third.
At small spend, daily numbers are noise, and looking daily leads to changes the data
cannot justify.

Never edit a running ad's text or URL: the platform resets its review and history.
Duplicate it, give it a new ad id and a new `utm_content`.

## Strategy checklist

- [ ] Campaign count derived from the arithmetic, not from a funnel diagram
- [ ] Expected clicks and conversions per month stated as a range, zero included if it applies
- [ ] Every planning number labelled as an assumption or sourced to a post-mortem
- [ ] Audience traced to real customers; target size checked in the forecast panel
- [ ] Held-back countries listed with the reason
- [ ] Decision rules written with thresholds before launch
- [ ] Parked tactics listed with the budget at which to revisit them
