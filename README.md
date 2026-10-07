# ad-campaign-runbook

[![Agent Skills](https://img.shields.io/badge/Agent_Skills-open_format-059669)](https://agentskills.io)
[![skills.sh](https://img.shields.io/badge/skills.sh-npx_skills_add-059669)](https://www.skills.sh)
[![Claude Code](https://img.shields.io/badge/Claude_Code-compatible-059669)](https://docs.claude.com/en/docs/claude-code/skills)
[![Codex CLI](https://img.shields.io/badge/Codex_CLI-compatible-059669)](https://developers.openai.com/codex/skills)
[![Gemini CLI](https://img.shields.io/badge/Gemini_CLI-compatible-059669)](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/skills.md)

An [Agent Skill](https://agentskills.io) that teaches an agent to turn one blog post into a LinkedIn Ads
campaign runbook a marketer can execute without the author in the room: goals and metrics, a probe of what
the site can actually measure, a campaign structure derived from the budget, audience, five ads whose every
sentence traces back to the post, an organic companion post with slots only the author can fill, UTM and
conversion tracking, click-by-click Campaign Manager steps, operating cadence, tracking sheet and
post-mortem. It is written for a **Next.js App Router** marketing site whose posts are markdown in the
repository.

**At small B2B budgets the plan is decided by arithmetic and by what the site can measure, not by the funnel
you would like to draw.** A monthly budget that cannot keep two campaigns above the platform's daily minimum
buys one campaign, whatever the funnel diagram says, and a tag that records page views cannot report a
conversion however the runbook words it. So the skill measures the post, probes the site, does the sums, and
only then writes copy. It takes the path to the post's markdown file as a required argument, because
choosing which content gets the budget is the user's decision.

This skill was written by the engineer who has shipped this work. The earlier implementation it was audited
against was a LinkedIn ads runbook for a B2B marketing site with consent-gated analytics and a sign-in wall
between the ad click and the conversion. The procedure holds the properties a runbook has to hold: a
campaign count that follows from the budget and the platform minimum, a dated record of what the site
measures, every ad claim traceable to a sentence in the post, personal facts left as slots for the person
whose name goes on them, an ad account the agent reads but never changes without a yes, and a finished file
with no placeholder and no fact older than the day it was handed over.
[`references/provenance.md`](references/provenance.md) has the record.

## Install

One command, via the [skills.sh](https://www.skills.sh) CLI, which installs the skill into every
skills-compatible agent it detects, including Claude Code, Codex CLI and Gemini CLI:

```bash
npx skills add timerise-ai/ad-campaign-runbook
```

Name the agents instead with `-a`, for example `npx skills add timerise-ai/ad-campaign-runbook -a
claude-code -a codex`.

### Manual install

Nothing here is Claude-specific: the skill is a plain [Agent Skills](https://agentskills.io) folder,
`SKILL.md` plus markdown references and one stdlib Python script, with no file that calls a model, so cloning
it into an agent's skills directory is all an install is. For Claude Code:

```bash
git clone https://github.com/timerise-ai/ad-campaign-runbook.git ~/.claude/skills/ad-campaign-runbook
```

To scope it to a single project instead, clone it into that project's `.claude/skills/` directory. For
another agent, clone into that agent's skills directory, or symlink the Claude Code copy so one `git pull`
updates every agent:

```bash
mkdir -p ~/.agents/skills
ln -s ~/.claude/skills/ad-campaign-runbook ~/.agents/skills/ad-campaign-runbook
```

Update the skill with `git pull` in its directory. The current release is **0.1.3**. See
[CHANGELOG.md](CHANGELOG.md). The [skills index](https://github.com/timerise-ai/skills) lists the other
Timerise Skills and how to install them all at once.

## Activation

The skill activates automatically when a task matches its description: promoting a blog post with paid
LinkedIn traffic, writing ad copy or UTMs for a specific post, planning a campaign against a monthly budget,
or asking for a runbook like the last one. Invoke it explicitly with `/ad-campaign-runbook` in Claude Code,
`$ad-campaign-runbook` in Codex CLI, or from `/skills` in Gemini CLI.

The skill takes the path to the post as a required argument and a monthly budget as an optional one:
`/ad-campaign-runbook content/blog/en/from-brief-to-prototype.md 3000 PLN`. Without the path it stops and
asks; it never picks a post, never falls back to the latest one, and never works from a URL or a summary.

Each host matches a task against the description its own way, so invoke the skill explicitly on a first run
rather than assuming it fired. Only `SKILL.md` is read up front; the `references/` files load on demand, so
the skill stays cheap in context until a topic is actually needed.

## What's inside

| File | Contents |
|---|---|
| `SKILL.md` | Entry point: the required input, architecture, eight critical facts, six hard rules, quick start, and the reference directory |
| `references/adaptation.md` | The seam with the host app: what it must provide, the rename table, integration points, where the runbook lives, another channel |
| `references/inputs.md` | The required post and the preflight, the inputs to ask for in one batch, and every placeholder in the template |
| `references/host-probe.md` | What the site can and cannot measure: tag, consent, conversion events, UTMs, redirects, CSP, the live check, failure modes, reading an ad account |
| `references/strategy.md` | Budget to structure, the budget bands, planning assumptions, audience, decision rules, cadence |
| `references/creative.md` | Offer, proof points, angles, the five ads and their copy rules, the organic companion post with author slots, the pre-publication audit |
| `references/conversion-tracking.md` | The UTM convention, the conversions to create, the client-side event in TypeScript, the engineering tickets, reporting without UTM capture |
| `references/campaign-manager.md` | Click-by-click build: account preflight, conversions, audiences, campaign group, the campaign, pre-launch checklist, gotchas |
| `references/runbook-template.md` | The document to produce, with fixed section numbers and every placeholder |
| `references/provenance.md` | The engineering ledger: what the audit changed and how the procedure holds it, what was kept on purpose, what was added here |
| `assets/preflight.py` | Stdlib Python: enforces the required post and reports the measured facts the runbook is built from. Exit `2` means stop |
| `README.md` | This file |
| `CHANGELOG.md` | Release history, newest first |
| `CLAUDE.md` | The editing conventions, for an agent editing this repository |
| `LICENSE` | MIT |
| `evals/` | The prompts an operator types after installing (`prompts.md`) and one file per agent eval: the skill installed into an empty Next.js app, one prompt carrying the post, no help, then type-checked, built and tested |
| `.github/workflows/agent-eval.yml` | The caller of the index's reusable eval workflow, run on every published release and on a maintainer's dispatch |

The seam is the table at the top of `references/adaptation.md`, and it is short because the deliverable is a
document: the host provides a markdown post with an offer in it, an analytics vendor and a consent component,
a way to count the conversion outside the ad platform, and a folder for operational documents. The host's
word for the conversion, its funnel event names, its programme name and its runbook location are renamed
through one table. The UTM parameter values are not renamed: they are the join key between the platform's
numbers and the host's own data.

The skill writes a document rather than code, so its evals score the agent against the hard rules, not the
app: the checks only confirm the app was left intact, and the notes on each run carry the score. Two of the
prompts give no usable post, and a run passes on those only when the agent stops and asks.

## The six non-negotiables

These travel with the runbook and are never optional. Each is stated as a hard rule in `SKILL.md`, restated
in `references/adaptation.md`, and carried by a checklist in the reference that owns it:

1. **Never run without the post file.** Which content gets the budget is the user's decision. The preflight
   exits `2` on a missing, non-file or non-markdown argument, and the skill stops there and asks.
2. **Never write a claim the post does not make.** Every ad sentence names the post sentence it comes from,
   and the post's own caveats bind the ads. The creative audit drops what has no source.
3. **Never invent a budget, a benchmark or a fact about the author.** Budgets come from the user, planning
   numbers are labelled as assumptions until a post-mortem replaces them, personal facts stay as slots the
   author fills before publication, and an input nobody gave takes its documented default and is listed as
   open.
4. **Never assume tracking works.** An installed tag records page views. The probe reads the code and one
   live page, dates its findings, and what is missing becomes a ticket rather than a promise.
5. **Never change the ad account without an explicit yes for that action.** Reading a signed-in session is
   fine. Creating a conversion, audience or campaign accepts the advertising agreement on the user's behalf,
   so the skill fills the form, stops at the review step and shows what will be created.
6. **Never leave a placeholder or a stale fact in the finished runbook.** The verification step greps for
   `{{` and rereads the tracking, creative and build sections against what is true on the day it is handed
   over.

Everything else is the host app's: its vocabulary, its analytics vendor, its consent component, its documents
folder, its brand rules and its definition of a qualified conversion.

## Requirements

Python 3 for `assets/preflight.py`, which uses the standard library only and runs in any host without an
install step. A blog post of more than 300 words as a markdown file in the repository, published at a stable
URL. A LinkedIn ad account, or the intent to create one; its currency is permanent once set, so it has to
match the budget currency. Nothing else is installed, and the skill writes no file into the host app except
the runbook and, when asked, the conversion event.

## Not this

| Not this | Use instead |
|---|---|
| Writing and publishing organic LinkedIn posts or comments | The `linkedin-marketing` skill. This skill drafts one companion post and hands it to that skill's audit |
| Boosting a Company Page post (Engagement objective, link in the first comment) | The `linkedin-boost` skill |
| Writing the blog post itself | `blog-markdown` and the host's content workflow. A post with no offer in it is not a paid candidate |
| Meta, Google or X campaigns | Not covered. The build steps are LinkedIn's, and another channel needs its own minimums, objectives and formats established first |
| Creating campaigns through an ads API | This skill produces a document for a human to execute in Campaign Manager |
| Reporting on a campaign that has already run | Section 9 of the template, the post-mortem, which feeds its actuals into the next runbook |

## Contributing

Issues and pull requests are welcome here. Pure markdown plus one stdlib Python script, with no build step,
but the content is checked: every code block names its destination or the command that runs it, the
TypeScript block in `conversion-tracking.md` is written to compile under `strict` and
`noUncheckedIndexedAccess`, and the preflight runs on Python 3 with no third-party import. Claims in this
skill are meant to be verifiable: if you change a factual claim, say how you verified it, whether against
LinkedIn's own documentation, the Campaign Manager UI on the day you looked, the ad platform's help centre,
or a reproduction.

Adding, removing or renaming a file in `references/` or `assets/` means updating the quick start and the
reference directory table in `SKILL.md`, the file table above, and any relative cross-links. Every
odd-looking part of the procedure is there for a reason, and `references/provenance.md` is the ledger that
must stay truthful: read it before simplifying anything, and add an entry for anything you change. Commits
follow Conventional Commits and releases follow
[STANDARD.md](https://github.com/timerise-ai/skills/blob/main/STANDARD.md) in the index; `CLAUDE.md` carries
the full editing conventions.

## Part of the Timerise Skills

This is one of the [Timerise Skills](https://github.com/timerise-ai/skills): modules for **Next.js App
Router** apps written by our own senior engineers from the modules they have shipped, not synthetic, each
published as its own repository and indexed there. They share one layout, so an agent that has read one knows
how to read the next: a `SKILL.md` entry point, `references/` loaded on demand, and a seam contract carrying
the module's non-negotiables.

## Author

Built and maintained by [Timerise](https://timerise.ai).

## License

MIT. See [LICENSE](LICENSE).
