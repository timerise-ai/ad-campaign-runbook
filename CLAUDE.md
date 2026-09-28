# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

An [Agent Skill](https://agentskills.io) package: markdown, plus one standard-library Python script. There is
no `package.json` here and nothing in this repository is part of an application. It teaches an agent to turn
one blog post into a LinkedIn Ads campaign runbook: preflight the post, probe what the host site measures,
size the plan by arithmetic, write copy traceable to the post, specify tracking, write the Campaign Manager
steps, and assemble one document with fixed section numbers.

Keep the two straight: the commands, code and checklists in `references/` describe the runbook the agent will
write and the host app it is written for, not this repository. The greps and `curl` calls in `host-probe.md`,
the TypeScript in `conversion-tracking.md` and the build steps in `campaign-manager.md` all run against the
host app and the user's ad account. The one file that executes here is `assets/preflight.py`, which reads a
markdown post and prints JSON.

The skill was written by the engineer who has shipped this work; the earlier implementation it was audited
against was a LinkedIn ads runbook for a B2B marketing site with consent-gated analytics and a sign-in wall
between the ad click and the conversion. `references/provenance.md` is the ledger of that audit: seven fixed
defects with how the procedure holds each one, seven deliberate keeps with the reason each is safe, and three
additions designed here that have never been run. That file is the rationale layer: read it before
"simplifying" anything.

## Structure

- `SKILL.md`: entry point, loaded whole on every activation, so it stays between 130 and 160 lines, the
  closing index line aside. The frontmatter is `name` and `description`, and the description is the trigger
  surface. The body carries the required-input contract, the architecture diagram, eight **critical facts**,
  six **hard rules**, the quick-start order, the **reference directory table** mapping trigger keywords to
  files, and a closing line linking the skills index.
- `README.md`: the human-facing front door, in the section order of the skill standard: install, activation,
  the file table, the six non-negotiables, requirements, the *Not this* table, contributing.
- `references/*.md`: one topic per file, loaded on demand. `adaptation.md` (the seam with the host) and
  `inputs.md` (the required argument and every placeholder) are the entry points; `host-probe.md`,
  `strategy.md`, `creative.md`, `conversion-tracking.md` and `campaign-manager.md` are the working order of
  the pipeline; `runbook-template.md` is the document to produce; `provenance.md` is the audit ledger.
- `assets/preflight.py`: the required-post check and the measured facts. Standard library only, so it runs in
  any host without an install step.
- `evals/`: `prompts.md` holds what an operator types after installing, in their words, each carrying the
  post it works on; the first prompt is the agent eval run before every release. Every other file there is
  one eval run: measured frontmatter that is never edited, then the notes of the person who ran it, scored
  against the hard rules. Add a prompt rather than rewording one that has results. The procedure is section
  10 of the index's STANDARD.md.
- `.github/workflows/agent-eval.yml`: the caller of the index's reusable eval workflow, run on every
  published release and on a maintainer's dispatch. It is copied verbatim, the same in every skill, and was
  set up by a maintainer; do not edit it, and never add a trigger on `push` or `pull_request`.

## Editing conventions

- **Code blocks name their destination or the command that runs them** on the first line, as a comment for a
  file, for example `// conversions.ts`. A continuation block that extends a file already introduced omits
  it.
- **The TypeScript block is written to compile** under `strict` and `noUncheckedIndexedAccess`, with imports
  complete and types explicit. It is a template for the host app, so its identifiers are the generic ones the
  rename table in `adaptation.md` maps to the host's vocabulary.
- **`assets/preflight.py` is stdlib only.** No third-party import, no network call, no write: it reads one
  markdown file and prints JSON. Exit `2` is the contract that makes the required argument enforceable, and
  `inputs.md` and `SKILL.md` both state it. Change one and change all three.
- **Identifiers are shared across files.** `FunnelConversion`, `trackFunnelConversion`, `parseConsent`,
  `claim`, `AD_PLATFORM_CONVERSION_IDS`, `CONSENT_STORAGE_KEY`, the ad ids `SI-01` upward, the UTM values
  `utm_source=linkedin`, `utm_medium=paid`, `utm_campaign=post-<short slug>` and `utm_content=<ad id>`, and
  every `{{PLACEHOLDER}}` name appear in several references. Rename in all of them or none.
- **Keep the three tables in sync** with `references/` and `assets/`: the reference directory in `SKILL.md`,
  the quick-start list in `SKILL.md`, and the file table in `README.md`. Links are relative:
  `[x.md](references/x.md)` from `SKILL.md`, `[x.md](x.md)` between references.
- **The placeholder table is the contract between two files.** Every `{{NAME}}` in `runbook-template.md` has
  a row in `inputs.md` giving its source. Adding a placeholder to one without the other is a defect, because
  the verification step only greps for `{{`.
- **The section numbers in `runbook-template.md` are fixed.** People cite "5.2" in conversation and the next
  post's runbook is a copy of the last one. Add sections at the end of a group rather than renumbering.
- **Do not remove the odd-looking parts.** The traffic objective instead of conversions, three live ads
  rather than five, cold traffic pointed at the post and not at the conversion page, the three weeks without
  changes, the author slots the agent must not fill, and the planning numbers that stay in labelled as
  assumptions: each is a ledger entry in `provenance.md`. Check it before touching one.
- **The numbers that remain are load-bearing.** The platform's daily minimum, the budget bands, the 140
  visible characters, the 300-member audience minimum, the 30-day click and 7-day view windows, the 0 to 3
  conversions a month, and the ledger's own entry counts. They are design parameters, vendor facts or counts
  of this repository. Do not restate them loosely and do not add new ones. Figures describing the earlier
  implementation's own content or account do not appear anywhere.
- **Mark additions as additions.** Anything designed in this skill and never run in the earlier
  implementation belongs in the "Added" section of `provenance.md`, stated as such. The skill's credibility
  is that it distinguishes the two.
- **Evals are not skill content.** A new prompt or an eval result is committed as `chore(evals): ...`,
  never causes a version bump and never rides in a release commit. The frontmatter of a result file is what
  was measured and is not edited; a failing run stays committed, and the fix is the next release.
- **Never present the non-negotiables as optional.** The required post file, claims traceable to the post,
  budgets and personal facts that are never invented, tracking that is probed rather than assumed, an ad
  account that is never changed without a yes, and a finished runbook with no placeholder and no stale fact
  are stated as hard rules in `SKILL.md`, as non-negotiables in `README.md` and restated in
  `adaptation.md`; keep them that way everywhere.
- The conversion vocabulary, the funnel event names, the programme name, the short slug and the runbook
  folder are meant to be renamed by the host, and `adaptation.md` carries that table. The UTM parameter names
  and values are the join key with the host's analytics and are not renamed.
