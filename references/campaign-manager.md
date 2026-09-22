# LinkedIn Campaign Manager: the build

Click-by-click steps to paste into the runbook, with the host's names and numbers
filled in. Menu labels change often. Write each as **English label** and, when the
account's UI is in another language, add the local label the user will actually see.
Tell the reader to search the Help Center for the bold term when a label is missing.

Steps 1 to 4 happen once per account. Every later blog post starts at step 5.

## 1. Account preflight (once)

1. Open Campaign Manager and select the right ad account. Write its **name, number
   and currency** into the runbook. Old, suspended or deleted accounts are common;
   name the ones to ignore.
2. The currency cannot be changed after creation. If the account currency differs
   from the budget currency, say so and convert every figure.
3. **Account settings → Manage access**: a second Account manager, so the account is
   not tied to one person. Sales as Viewer.
4. **Account settings → Billing**: company card, invoice details, VAT id.
5. **Measurement → Insight Tag**: the partner id shown must equal the one in the
   site's code. Browse the site with marketing cookies accepted; the domain should
   turn Active within hours. "Unverified" usually means the tester declined cookies
   or runs an ad blocker.

**Use a browser profile without an ad blocker for all of this.** With one active,
Campaign Manager shows a red warning banner and leaves some pages blank.

## 2. Conversions (once)

1. **Measure → Conversion tracking → Create conversion → Insight Tag conversion.**
2. Settings step: name, category, value (none until Sales agrees one), windows 30-day
   click and 7-day view, last touch.
3. Sources step: **Manual setup**, then **Page load** with a "URL starts with" rule,
   or **Event-specific**, which shows the snippet holding the numeric id.
4. Review step. The Create button carries a line accepting the advertising
   agreement, so the account owner clicks it.
5. New conversions show **Unverified** until the first event arrives. Test in a clean
   profile with marketing cookies accepted, then delete the test record.

Which conversions to create: [conversion-tracking.md](conversion-tracking.md).

## 3. Audiences (once)

**Plan → Audiences → Create audience.**

| Audience | Type | Settings | Used |
| :-- | :-- | :-- | :-- |
| Customers and open deals | Contact list | CSV of emails from the CRM. Refresh quarterly | Exclusion, now |
| Conversion page visitors, 180 days | Website | URL contains the conversion or sign-in path | Exclusion, now |
| Blog readers, 90 days | Website | URL contains the blog path | Collecting for later retargeting |
| Ad engagers, 90 days | Single image ad | Any engagement, all post campaigns. Create after day 2 | Collecting for later retargeting |

An audience needs **300 matched members** before it can be used, including as an
exclusion. Lists take up to 48 hours to match. Create them in the setup week; the
collecting ones are free and take months to fill, which is the reason to start now
even when retargeting is parked.

## 4. Campaign group (once)

1. **Advertise → Create → Campaign group**, named for the programme ("Blog posts"),
   Active, no end date.
2. Budget cap. Group budgets are not always monthly; if only a total is offered, set
   the run budget and renew it at each end-of-run review. The daily budget and end
   date on the campaign are what actually hold the spend.
3. Leave dynamic group budget off so spend stays comparable between posts.

## 5. The campaign (once per blog post)

1. Inside the group: **Create → Campaign**, classic manual setup. **Decline
   "Accelerate"** or any AI-assisted setup: it chooses audiences and placements and
   makes the result unreadable.
2. Objective: **Website visits**.
3. Name: `POST | <short slug> | WV | <yyyy-mm>`.
4. Audience:
   - Locations: recent or permanent, the launch countries.
   - Profile language: the site's language.
   - Attributes from the runbook. Values inside a facet are OR; use **Narrow (AND)**
     between facets. Confirm the combined size in the forecast panel.
   - Exclusions from step 3, plus the company itself.
   - **Untick "Enable audience expansion".** It is on by default and silently adds
     lookalikes.
   - Note the forecast panel's suggested bid range in the runbook. It is the first
     real number against the CPC assumption.
   - **Save as audience template.** The next post starts from it.
5. Ad format: **Single image ad**.
6. Placement: **untick LinkedIn Audience Network.** It buys cheap off-platform clicks
   that do not read long posts.
7. Budget and schedule: daily budget, start on a Tuesday, end date at the run length.
8. Bidding: optimisation goal landing page clicks, **manual bidding** at the low end
   of the suggested range. If spend stays under 60% of the daily budget for a week,
   raise the bid 10%. Switch to maximum delivery only if manual cannot spend.
9. Conversion tracking: attach every conversion. They are for reporting; the
   objective stays traffic.
10. Create one ad per launch creative. **Ad name = ad id** (`SI-01`). Destination URL
    = the full UTM URL. Check the mobile preview: the hook must be readable before
    "…see more".
11. Ad rotation: **rotate evenly** until the mid-run review, then optimise for
    performance.
12. Launch. Review usually takes under a day.

## Pre-launch checklist (paste into the runbook)

- [ ] Landing page changes are live in production
- [ ] Each destination URL opens and shows in analytics realtime with the right `utm_content`
- [ ] Tag Active; conversions attached; any conversion ids deployed
- [ ] Audience expansion unticked, Audience Network unticked
- [ ] Exclusions attached, or noted as pending the 300-member minimum
- [ ] Ad names equal `utm_content` values
- [ ] Cap, daily budget and end date set
- [ ] Organic post live with the author's slots filled by the author; link in the first comment; colleagues briefed to comment across the first hour
- [ ] Sales knows conversions may arrive and has agreed an acceptable cost per qualified one
- [ ] Baseline written down for the 28 days before launch

## Gotchas

| Gotcha | Consequence |
| :-- | :-- |
| Audience expansion and Audience Network default to on | Budget leaks to lookalikes and off-platform inventory; demographics become unreadable |
| Editing a live ad | Review and history reset. Duplicate instead |
| More than 3 or 4 live ads on a small budget | None reaches a judgeable impression count inside the month |
| Conversion objective with a few conversions a month | Erratic delivery, nothing learned |
| Acting on instructions from a signed-in session without confirming account changes | Creating objects accepts terms on the user's behalf. Stop at the review step |
