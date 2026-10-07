# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.3] - 2026-10-07

A fix release, from scoring the prompt-1 agent eval runs of 0.1.2.

### Changed

- `SKILL.md` quick-start step 10: the final message names each handover item
  itself, every open input included, instead of pointing at the runbook.
- `references/strategy.md`: every running campaign gets at least
  `2.5 * MIN_DAILY` a day, the floor the campaign count is derived from, and the
  post campaign takes the rest.
- `references/strategy.md`, `conversion-tracking.md`, `campaign-manager.md` and
  `adaptation.md`: the shared retargeting campaign is tagged
  `utm_campaign=retargeting`, and its ads are `RT-01` upward with
  `utm_content=rt-01`. Both rules are recorded under *Added* in
  `references/provenance.md`.

## [0.1.2] - 2026-10-07

A fix release, from scoring the prompt-1 agent eval runs of 0.1.1 against a
fidelity rubric.

### Fixed

- `references/conversion-tracking.md` said the platform's ad name and
  `utm_content` are the same lowercase string, while `creative.md` and
  `campaign-manager.md` name the ad `SI-01`. All three now say the ad is named
  `SI-01` and `utm_content` is `si-01`. A runbook that named its ads in
  lowercase still joins, since the join ignores case.

### Changed

- `SKILL.md` critical fact 1 and `references/strategy.md`: from 1,400 to 2,100
  EUR a month the runbook plans two campaigns. Retargeting whose audience is
  still under 300 members is built in the setup week and switched on when the
  audience passes 300. Until then its budget stays with the post campaign, and
  it is never parked. Recorded under *Added* in `references/provenance.md`.
- `SKILL.md`: a dev server is not the live site. With no production domain,
  the runbook's URLs are paths, and `references/inputs.md` and
  `references/host-probe.md` say the same. The preflight is not a test suite,
  and nothing in the host's `package.json` or tests runs it.
- `SKILL.md` hard rule 3 and the README's non-negotiable 3: an input nobody
  gave takes its default from `references/inputs.md` and is listed as open. A
  host with no data store gets the count by hand, never a query against tables
  that do not exist.
- `SKILL.md` quick-start step 10 lists what the final message tells the
  operator: what blocks launch, whether the live check was done, the empty
  author slots, the conversion range with zero in it, and every open input.
- `SKILL.md` and the README point boosting a Company Page post at the
  `linkedin-boost` skill.

## [0.1.1] - 2026-09-28

A wording release that brings the repository to the skill standard's eval
requirements; the procedure, the references and the preflight are unchanged
from 0.1.0.

### Changed

- `SKILL.md` states that the post file and the host's own site are not external
  services in an eval's sense, and that a post not yet deployed gets its live
  check recorded as not done, with a ticket. The note on implementing the
  conversion event moved into quick-start step 6.
- `README.md` lists every file in the repository, `evals/` and the eval
  workflow, and says how the evals of a skill that writes no code are scored.
- `CLAUDE.md` describes `evals/` and the eval workflow, and that evals are not
  skill content.

## [0.1.0] - 2026-09-22

Initial release of the `ad-campaign-runbook` skill: one blog post turned into a
LinkedIn Ads campaign runbook a marketer can execute, for a Next.js App Router
marketing site whose posts are markdown in the repository.

### Added

- `SKILL.md` entry point: the required post argument, the architecture of the
  pipeline, eight critical facts, six hard rules, the quick-start order and the
  reference directory.
- `references/adaptation.md`: the seam with the host app, what it must provide,
  the rename table, the integration points, where the runbook lives, and what
  another channel would need.
- `references/inputs.md`: the required parameter and the preflight, the inputs to
  ask for in one batch, and every placeholder in the template.
- `references/host-probe.md`: what the site can and cannot measure, the code
  greps, the live check, the failure modes, and how to read an ad account without
  changing it.
- `references/strategy.md`: budget to structure, the budget bands, the planning
  assumptions, audience, decision rules and cadence.
- `references/creative.md`: offer, proof points, angles, five ads with their copy
  rules, the organic companion post with author slots, and the pre-publication
  audit.
- `references/conversion-tracking.md`: the UTM convention, the conversions to
  create, the client-side event in TypeScript, the engineering tickets, and
  reporting without UTM capture.
- `references/campaign-manager.md`: the click-by-click build, once per account and
  once per post, with the pre-launch checklist and the gotchas.
- `references/runbook-template.md`: the document to produce, with fixed section
  numbers.
- `references/provenance.md`: the engineering ledger, seven fixed defects, seven
  deliberate keeps and three additions.
- `assets/preflight.py`: stdlib Python that enforces the required post and reports
  the measured facts the runbook is built from, exiting `2` when the post is
  unusable.
