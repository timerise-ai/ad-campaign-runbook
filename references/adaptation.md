# Adaptation: the seam with the host app

This skill produces a document, and one optional code change. The seam is therefore narrow: what the host
must already have for a runbook to be worth writing, the vocabulary the runbook renames to the host's own,
and where the finished file lives. Read this before the first runbook in a repository. For the second one,
[inputs.md](inputs.md) and the appendix of [runbook-template.md](runbook-template.md) are enough.

## What the host must provide

| Requirement | Why it is required | If it is missing |
| :-- | :-- | :-- |
| A blog post as a `.md` or `.mdx` file in the repository, over 300 words | Every ad sentence is traced to a post sentence, in the file the user names | Stop and ask for the file. A URL or a summary is not a substitute |
| The post published and reachable at a stable URL | It is the landing page, and the destination URL carries the UTMs | Write the runbook and mark launch as blocked on publication |
| An offer with a next step somewhere in the post | Without it, paid traffic has nowhere to go and there is nothing to measure | Say so and propose the change to the post, or a different post |
| A conversion the business can name, and a way to count it outside the ad platform | Platform numbers alone cannot be trusted for a handful of conversions a month | Section 8 of the runbook records how to count it by hand until the query exists |
| An analytics vendor and a consent component, whatever they are | The probe reads both; the event code reads consent at fire time | The probe records their absence as a fact and the tickets table carries the work |
| A place for operational documents, and its index | The runbook is committed beside the host's other documents, not pasted into a chat | Propose `docs/runbooks/` and add the index entry as the last step |
| An ad account, or the intent to create one | Currency and existing conversions decide several numbers in the runbook | The runbook's account preflight section covers creating one |

Optional, and used when present: a content standards or brand rules file, earlier runbooks with their
post-mortems, a CRM definition of a qualified conversion, and a case study or customer list to build the
audience from.

## Rename table

The skill's canonical vocabulary is generic so that the runbook can carry the host's. Rename in every place
the word appears, or in none.

| Canonical | What the host substitutes | Appears in |
| :-- | :-- | :-- |
| conversion | The host's own word for the thing worth paying for: brief, demo, trial, quote, application | Runbook sections 1, 2, 5 and 8, ad copy, conversion names in the ad account |
| conversion started, conversion completed | The host's two funnel moments, for example `brief_created` and `brief_submitted` | `FunnelConversion` members, conversion names, analytics event names |
| post campaign | The host's programme name, for example "Blog posts" | Campaign group name, campaign names |
| short slug | Two or three words of the post slug | `utm_campaign=post-<short slug>`, campaign name, runbook file name |
| ad id | `SI-01` upward, one per ad, never reused | Ad name in the platform, `utm_content`, the tracking sheet |
| runbook file | `<channel>-ads-<short slug>.md` in the host's documents folder | The file this skill writes, and the post-mortem beside it |

Names that are not renamed: the UTM parameter names, `utm_source=linkedin`, and `utm_medium=paid` or
`organic`. They are the join key between the platform's numbers and the host's own data, and the host's
analytics compares posts on them.

## Integration points

- **Content source.** The post is read from the file the user names. The preflight reports title, slug, word
  count, H2 sections, images, internal links and where the first conversion link appears. A host that keeps
  posts in a CMS needs the post exported to a file first, because the claims are traced to the text.
- **Analytics and consent.** The event code in [conversion-tracking.md](conversion-tracking.md) reads the
  host's consent key and shape, and fires to the host's analytics as well as the ad platform. Marketing
  consent gates the ad platform and analytics consent gates analytics: one flag for both leaks data one way
  or the other.
- **Conversion recording.** The reliable hook for attribution is wherever the conversion is written
  server-side. The first-party UTM capture ticket attaches campaign and ad id there.
- **Locale.** One campaign targets one profile language. A site in several languages runs one campaign per
  language post, each with its own runbook, and the audience's profile language matches the post's.
- **Where the runbook lives.** Commit it in the host's documents folder, add the index entry, and commit the
  post-mortem beside it as `<runbook name>-results.md` at the end of the run.
- **Another channel.** The strategy, probe, creative and tracking references are channel-neutral in
  principle. The build steps are not: [campaign-manager.md](campaign-manager.md) is LinkedIn, and another
  channel needs its own minimums, objectives and formats established first, not written by analogy.

## Order of work

1. Preflight the post. Stop on exit `2`.
2. Probe the host and read any earlier runbook and post-mortem.
3. Ask for the inputs in one batch, quoting what the probe found.
4. Do the arithmetic, then the creative, then the tracking spec, then the build steps.
5. Assemble the file from the template, keeping the section numbers.
6. Audit the copy and the organic post, grep for `{{`, and add the runbook to the index.

## The non-negotiables, restated

They travel with the runbook and are never optional:

1. **Never run without the post file.**
2. **Never write a claim the post does not make.**
3. **Never invent a budget, a benchmark or a fact about the author.**
4. **Never assume tracking works.**
5. **Never change the ad account without an explicit yes for that action.**
6. **Never leave a placeholder or a stale fact in the finished runbook.**

Everything else is the host app's: its vocabulary, its analytics vendor, its consent component, its documents
folder, its brand rules and its definition of a qualified conversion.
