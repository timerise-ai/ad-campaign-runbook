# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
