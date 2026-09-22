# Host probe: what the site can and cannot measure

A campaign runbook that assumes tracking works is how a team spends two months of budget and learns nothing.
Probe the host before writing strategy. Every finding lands in the runbook's "What the site can and cannot
measure today" table as a **fact and its consequence**, dated.

## What to find

| Question | How to find it | Why it changes the plan |
| :-- | :-- | :-- |
| Is the ad platform's tag installed, and which account id? | Grep for the vendor script host (`snap.licdn.com`, `_linkedin_partner_id`) | Wrong or missing id means no audiences and no conversions |
| Where is it mounted? | Find the component's import site; check which layouts include it | A tag in the marketing layout only may miss the sign-in and app pages, where the conversion happens |
| Is it consent-gated? | Look for a consent wrapper around the tag | Visitors who decline are invisible. Conversions under-report, website audiences fill slowly |
| Is analytics consent-gated separately? | Same wrapper, different category | Analytics sessions become a floor, not a total |
| Does anything fire a conversion event? | Grep for the vendor's track call (`lintrk(`), and for analytics `event` calls | A base tag records page views only. Without a track call only URL-rule conversions are possible |
| Are UTM parameters read or stored anywhere? | Grep `utm_` | If not, a conversion cannot be tied to a campaign in the host's own data |
| What is the conversion, and what stands between the click and it? | Follow the CTA link from the post through routing and auth | Sign-in walls, email magic links and long forms decide whether ads may point at the conversion page at all |
| Do redirects keep the query string? | Read the redirect in the auth guard or proxy | A server-side redirect that rebuilds the URL drops UTMs before any page renders |
| Where is the conversion recorded server-side? | Find the insert or event for the conversion | That is the reliable hook for attribution and for counting a baseline |
| Is there a Content-Security-Policy? | `curl -sI <url>` | A CSP without the vendor hosts silently blocks the tag |
| Do headings render with ids? | Inspect the blog renderer | Without ids, ads cannot deep-link to a section |
| Is there a brand or content rules file? | Look in `docs/` for standards, tone, style | Ad copy must obey it; cite it in the runbook |
| Do campaign runbooks already exist? | Look for a runbooks folder and its index | Reuse account facts, audiences, conversions and real numbers from the last post-mortem |
| Who converts today? | Case studies, customer list, CRM stages | Audience and geography come from real customers, not from imagination |

Useful greps, adapted to the host's layout:

```bash
grep -rnE "utm_|lintrk|gtag\(|fbq\(|conversion" src --include="*.ts" --include="*.tsx" -l
grep -rn "licdn\|_linkedin_partner_id" src
grep -rn "redirect(" src/app | grep -i "access\|login\|sign"
curl -sI https://<site>/<post path> | grep -iE "^HTTP|content-security|permissions-policy"
```

## Live check

Code shows what should happen. A browser shows what does.

1. Open the live post in a normal profile and accept marketing cookies.
2. Confirm the vendor script loaded and a page-view request went out carrying the expected account id.
   `performance.getEntriesByType("resource")` filtered by the vendor host is enough.
3. Record the date of the check in the runbook.

## Failure modes and what causes them

| Symptom | Cause | What to do |
| :-- | :-- | :-- |
| The tag "reports an error" to the vendor, one request fails in about 1 ms | An ad blocker or tracking protection in the test browser. A 1 ms failure is not a network round trip | Retest in a clean profile before calling it a site defect. Check the endpoint with `curl` to confirm it is reachable |
| Ad platform UI pages render blank | The same ad blocker. LinkedIn shows a red banner about it | Use a profile without a blocker for all ad account work |
| Existing conversion shows "Inactive" | No consented, ad-sourced visitor has matched the rule recently. Not necessarily a broken rule | Read the rule. If it matches a real URL, keep it and say why it is inactive |
| A page-load conversion id is reused in a track call | Page-load and event-specific conversions are different objects | Create an event-specific conversion and use the id it issues |
| Conversion attributed to nothing | The visitor clicked the ad on a phone and opened the sign-in email on a laptop | Expect it. Report the uplift over a baseline next to platform numbers |
| The post's first conversion link is its last line | Common in essay-style posts | Landing page fix before launch: one link near the top |

## Reading an ad account

Only when the user offers a signed-in session. Read, do not change:

- Which account is active, its number and **currency** (permanent once set).
- Existing conversions: name, type, rule, status, id. Do not create duplicates.
- Existing audiences and campaign groups that can be reused.

Creating a conversion, audience or campaign changes the account and often carries an "by clicking Create you
accept the advertising agreement" line. Fill the form, stop at the review step, show the user exactly what
will be created, and let them confirm or click it themselves.

## Probe checklist

- [ ] Tag presence, account id, mount point and consent gating recorded
- [ ] Conversion event firing: yes, no, or URL-rule only
- [ ] UTM handling: stored, not stored
- [ ] Full path from ad click to conversion written as a chain, with friction named
- [ ] Redirects checked for dropped query strings
- [ ] Live check done and dated, in a browser without an ad blocker
- [ ] Brand rules file found or confirmed absent
- [ ] Earlier runbooks and post-mortems read
