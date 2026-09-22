# Creative: the offer, the ads and the organic post

The post is the source of truth. The ads do not get to say anything the post does
not, and the landing page must deliver what the ad promised in the first screen.

## 1. Extract the offer

Read the whole post, then write, in this order:

| Output | Rule |
| :-- | :-- |
| **The offer**, two or three sentences | What the reader gets, what it costs, how long it takes, what they must do. Use the post's own words |
| **Proof points** | A flat list of claims ads may use. Each one must be traceable to a sentence in the post. If you cannot point at the sentence, it is not a proof point |
| **Honesty constraints** | The limits the post itself states ("the clock can shift", "it is a mockup, not a trial"). Ads must not contradict them. Prefer "within 48 hours" to "guaranteed" |
| **Brand rules** | Cite the host's content standards file. Typical rules: no absolute claims, no manufactured urgency, no naming or disparaging competitors |

A post with no offer in it (pure opinion, no next step) is a poor paid candidate. Say
so and suggest the change to the post, or a different post, before writing ads.

## 2. Angles

One angle per persuasive section of the post. The preflight's `h2_sections` list is
the starting point.

| Column | Content |
| :-- | :-- |
| ID | `A1`, `A2`, … |
| Angle | A three or four word name |
| Post section | The H2 it comes from, quoted |
| One-line idea | The thought an ad built on it would carry |

Aim for five or six angles. Fewer than four means the post is thin for paid.

## 3. Ads

Write five single image ads, launch three, keep two in reserve for the mid-run swap.
Launch the three whose hooks differ most, so the test teaches something.

| Item | Spec |
| :-- | :-- |
| Image | 1200 × 1200 px, PNG or JPG, under 5 MB. Square first: most feed impressions are mobile |
| Intro text | Hook inside the first **140 characters** (the mobile "…see more" cut). 600 maximum, 200 to 300 works |
| Headline | 70 characters or fewer |
| CTA button | "Learn more" for cold traffic to a post |
| Ad ID | `SI-01` … `SI-05`. The ad's name in the platform, and lowercase as `utm_content`. Never reused |

Copy rules, each learned from a rejected or weak draft:

- **Lead with the benefit or the concrete scene, not with a quotation or jargon.** A
  reader who sees only 140 characters must see why to care.
- **No "not X, it's Y" contrast frames**, in intro or headline ("Not a template. Your
  services…", "built from your brief, not from a template"). State the positive
  claim. The pattern reads as machine-written and is reported as reach-negative.
- One idea per ad. One natural list of three at most across the ad.
- No vocabulary like leverage, seamless, robust, unlock, streamline, game-changer.
- Every sentence traceable to the post. Reviewers reject claims that read as
  guarantees; so do readers.
- Do not reuse one opening across the ad set and the organic post. Side by side they
  read as a template.

Visual direction:

- Show the thing the post is about. If the post argues "seeing beats reading", the ad
  shows a screen.
- Never show a real customer's private material unless cleared in writing.
- Reuse the host's visual language (cover motif, colour tokens, typeface) so ad, post
  cover and page feel like one thing. Do not invent a campaign look.
- At most 8 words on the image. The key number legible at thumbnail size.
- Later variants change text **or** image, never both, or the result teaches nothing.

## 4. The organic companion post

Paid reach at small budgets is modest, so the unpaid post from a founder or named
expert is part of the plan, not a nice-to-have. It costs nothing and its engagers
later feed retargeting.

**Write it with slots the author must fill.** A draft full of "we" offer terms is a
company pitch. What makes it read as a person is one named, dated moment and one
odd-precision number with a referent. The agent does not have those facts and must
not invent them:

```
[AUTHOR SLOT 1: one real moment, named and dated. Who, when, what it cost them.]
[AUTHOR SLOT 2: one flat fact with an odd-precision number and a referent. Stated
plainly, with no "to be honest" framing.]
```

The runbook says, above the draft, that the post must not be published with a slot
empty or invented.

Publishing rules to include as a table:

| Rule | What to do |
| :-- | :-- |
| Link | Never in the body. First comment, with `utm_medium=organic` |
| Length | 900 to 1,300 characters. Hook inside 140 |
| Close | A specific, experience-anchored question. Never "Thoughts?" |
| Format | Best: a PDF document post, 5 to 7 slides, under 12 words a slide. Next: 3 or 4 images. Avoid a single image |
| When | Tuesday or Wednesday, 7:00 to 8:30 in the audience's timezone |
| Before | The author leaves 3 to 5 substantive comments on other posts in the 15 minutes before |
| First 90 minutes | The author replies to every comment, each reply written fresh |
| Colleagues | **Comments, not reshares**, 12 or more words, each with their own angle, spread across the first hour. Several accounts acting in the same minute looks like an engagement pod |
| Edits | None in the first 3 hours |
| Hashtags | None, or at most 2 niche ones at the end |
| Company page | Its own text a day later, link also in the first comment |

A carousel that the budget cannot carry as an ad is often free as the organic
document post. Reuse the outline.

## 5. Audit before anything is published

| Check | How |
| :-- | :-- |
| Traceability | For each ad sentence, name the post sentence it comes from. Drop what has no source |
| Hook | Print the first 140 characters of every intro. Would you stop scrolling? |
| Lengths | Intro under 600, headline under 70 |
| Contrast frames and vocabulary | Grep for `\bnot\b.{1,40},? (it's|your|but)` and the vocabulary list |
| Brand rules | Reread the host's standards file against the copy |
| Organic post | If the `linkedin-marketing` skill is installed, run its humanizer in audit mode on the organic post. Its checklist owns organic-feed heuristics; its reach multipliers do **not** apply to paid delivery |

## 6. The landing page is part of the creative

Put these in the runbook as work to ship **before day 1**, because changing the page
mid-run makes before and after incomparable:

1. A conversion link near the top of the post (the preflight reports where the first
   one is).
2. Show the thing on the page, if the offer is visual and the post has no image.
3. If the site has a chat assistant, confirm it answers "how do I get this?" with the
   conversion path.
4. No separate landing page. The post is the landing page, which also serves the page
   view goal.

## Creative checklist

- [ ] Offer, proof points and honesty constraints written from the post
- [ ] Five or six angles, each tied to an H2
- [ ] Five ads, three marked for launch, two in reserve
- [ ] Every intro's first 140 characters carries the reason to care
- [ ] No contrast frames, no banned vocabulary, no untraceable claim
- [ ] Organic post drafted with two author slots and the publishing rules table
- [ ] Landing page fixes listed with "ship before day 1"
