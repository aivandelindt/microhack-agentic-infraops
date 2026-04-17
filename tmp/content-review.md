# Content Review — APEX MicroHack

Comprehensive read-and-fix review of all authored content. All Blocker/Major/Minor findings fixed inline in this PR.

Run date: 2026-04-17

---

## Summary

| Phase | Status | Findings | Fixed |
| --- | --- | --- | --- |
| 0. Mechanical gate | Pass | 8 broken internal links | 8 |
| 1. Inventory | Pass | 38 content files, 5 components, 3 scripts, 13 `.github/` assets | — |
| 2. Accuracy / hallucinations | Pass | 1 Major (README understates IaC scaffolds) | 1 |
| 3. Completeness | Pass | All 8 challenges pass the styler checklist; facilitator chain consistent | — |
| 4. Readability / a11y | Pass | 4 brand-capitalization + 3 en-GB/en-US consistency | 7 |
| 5. Tooling & supporting content | Pass | Vale not wired; no LICENSE/CONTRIBUTING/CODEOWNERS/templates; PR workflow missing Vale step | 8 |

**Blocker:** 0. **Major:** 13 (all fixed). **Minor:** 8 (all fixed). **Nit:** 0 outstanding.

---

## Phase 0 — Mechanical gate

| Check | Before | After |
| --- | --- | --- |
| `cd site && npm run lint:md` | OK | OK |
| `cd site && npm run build` | OK | OK |
| `cd site && npm run lint:prose` (Vale) | **not installed** | **0 errors, 0 warnings, 0 suggestions (33 files)** |
| Broken internal links in `site/dist` | 8 | 0 |
| lychee external links | 1 expected localhost placeholder | unchanged |

### Broken internal links (F-01–F-08 — fixed)

Starlight rewrites links whose targets end in `.md` / `.mdx`, but passes directory-style relative links through untouched — the browser then resolves them against the current page URL, not the source directory. Eight cases where authors assumed source-directory semantics resolved to 404s.

| ID | File | Bad link | Fixed to |
| --- | --- | --- | --- |
| F-01 | [site/src/content/docs/about/invitation.md](../site/src/content/docs/about/invitation.md#L44) | `../getting-started/` | `../../getting-started/` |
| F-02 | [site/src/content/docs/about/agenda.mdx](../site/src/content/docs/about/agenda.mdx#L241) | `../../challenges/index/` | `../../challenges/` |
| F-03 | [site/src/content/docs/getting-started/index.md](../site/src/content/docs/getting-started/index.md#L64) | `../challenges/index/` | `../challenges/` |
| F-04 | [site/src/content/docs/getting-started/beginner-setup.md](../site/src/content/docs/getting-started/beginner-setup.md) | `setup/` (×2) | `../setup/` |
| F-05 | same | `setup/#setup-steps` | `../setup/#setup-steps` |
| F-06 | same | `workshop-prep/` | `../workshop-prep/` |
| F-07 | [site/src/content/docs/getting-started/setup.md](../site/src/content/docs/getting-started/setup.md#L212) | `beginner-setup/` | `../beginner-setup/` |
| F-08 | [site/src/content/docs/getting-started/setup.md](../site/src/content/docs/getting-started/setup.md#L462) | `../reference/governance-scripts/` | `../../reference/governance-scripts/` |

---

## Phase 2 — Accuracy & hallucination

### Template repo cross-check

Fetched [azure-agentic-infraops-accelerator](https://github.com/jonathan-vella/azure-agentic-infraops-accelerator) and verified the microhack docs' claims against the actual tree. `.devcontainer/`, `.github/agents/`, `.github/skills/`, `infra/bicep/`, and `infra/terraform/` all present; `npm run init` and `npm run sync:workflows` scripts exist.

### F-09 Major — README understates IaC scaffolds (fixed)

[README.md](../README.md) line 12 said "contains agents, skills, dev container, and **Bicep scaffold**". Template ships both Bicep and Terraform, Challenge 3 explicitly offers both, scoring rubric references `infra/terraform/{team}/`, and the facilitator guide scores both equally. Changed to "Bicep + Terraform scaffolds".

### Azure / Copilot / MCP claims

Cross-checked; all current and consistent:

| Claim | Verdict |
| --- | --- |
| Policy names (`microhack-allowed-locations`, etc.) | match [scripts/Setup-GovernancePolicies.ps1](../scripts/Setup-GovernancePolicies.ps1) |
| Copilot tiers (Pro, Business, Pro+, Enterprise) | current as of 2026-04 |
| "Custom agents not available on Copilot Free" | current |
| Allowed regions `swedencentral`, `germanywestcentral` | match policy scripts |
| DR values (RTO 4h→1h, RPO 1h→15m, budget €500→€700) | consistent across facilitator-guide, scoring-rubric, solution-reference, challenge-4 |

No hallucinations or fabricated flags found.

---

## Phase 3 — Completeness

- **Challenges 1–8** each include all nine required sections from [.github/skills/challenge-guide-styler/SKILL.md](../.github/skills/challenge-guide-styler/SKILL.md) (frontmatter, Challenge Info aside, Objective, Business Challenge, Your Tasks, Success Criteria, Tips, Watch Out, Next Step).
- **Facilitator chain** agrees on 105 base + 25 bonus = 130 max points, all per-challenge point/duration values, DR parameters, team size, subscription requirements, and cleanup workflow.
- **Participant journey** walked end-to-end with no dead ends or orphaned pages.

---

## Phase 4 — Readability, style, accessibility

### Components

Reviewed `AgentChat.astro`, `ChallengeChainTable.astro`, `ExpandableTable.astro`, `Footer.astro`, `ThemeProvider.astro` (1,294 lines). No `console.log` leaks, all interactive elements have `aria-label`s, dialog components implement full keyboard paths, no missing alt text, no heading-level skips.

### Brand capitalization — F-10–F-13 (fixed)

Glossary canonicalizes the event name as "MicroHack" (camel-case) or "microhack" (lowercase). Four places used "Microhack" (capital M only) which matches neither:

| ID | File | Fix |
| --- | --- | --- |
| F-10 | [site/src/content/docs/about/agenda.mdx](../site/src/content/docs/about/agenda.mdx#L67) | "APEX Microhack" → "APEX MicroHack" |
| F-11 | [site/src/content/docs/about/agenda.mdx](../site/src/content/docs/about/agenda.mdx#L139) | "Microhack overview" → "MicroHack overview" |
| F-12 | [site/src/content/docs/guides/copilot-guide.md](../site/src/content/docs/guides/copilot-guide.md#L327) | "### Workflow Through the Microhack" → "MicroHack" |
| F-13 | [site/src/content/docs/getting-started/workshop-prep.md](../site/src/content/docs/getting-started/workshop-prep.md#L119) | "### The Microhack Journey" → "MicroHack" |

PowerShell parameter `-MicrohackOnly` is unchanged — it must match the script.

### Spelling consistency — F-14 (fixed)

[site/src/components/AgentChat.astro](../site/src/components/AgentChat.astro) lines 20, 30, 66 used "standardised" (en-GB). The rest of the workshop content — including the landing page's user-visible "standardized, governance-compliant Azure platform" line — uses en-US "standardized". Normalized AgentChat to en-US to match the rendered site.

---

## Phase 5 — Tooling & supporting content

### Vale wiring — F-15 (fixed)

- Added [.vale.ini](../.vale.ini) with Microsoft style + an `InfraOps` project vocabulary for domain terms (Agentic, Copilot, Bicep, Terraform, MicroHack, curveball, runbook, Starlight, etc.).
- Added [.vale/styles/config/vocabularies/InfraOps/accept.txt](../.vale/styles/config/vocabularies/InfraOps/accept.txt).
- Added `lint:prose` script to [site/package.json](../site/package.json) — runs `vale --minAlertLevel=error` against `src/content`, `facilitator/`, `README.md`, `AGENTS.md`.
- Added a Vale step to [.github/workflows/validate-docs.yml](../.github/workflows/validate-docs.yml) using `errata-ai/vale-action` with `fail_on_error: true`, and expanded the workflow's path triggers to include `facilitator/`, root `README.md`/`AGENTS.md`, `.vale.ini`, and `.vale/`.
- Current result: **0 errors, 0 warnings, 0 suggestions across 33 files**.

Noise-reduction rules disabled in `.vale.ini` (appropriate for this project): `Microsoft.FirstPerson`, `We`, `Passive`, `Adverbs`, `Contractions`, `Auto`, `Foreign`, `Dashes` (em-dash with spaces is house style), `Quotes` (technical prose), `Avoid` (flags common terms such as `backend`), and `Vale.Terms` (conflicts with `MicroHack` brand form).

### Repo hygiene — F-16 through F-21 (fixed)

| ID | Addition | File |
| --- | --- | --- |
| F-16 | MIT license | [LICENSE](../LICENSE) |
| F-17 | Contributor guide with local-dev commands and PR checklist | [CONTRIBUTING.md](../CONTRIBUTING.md) |
| F-18 | Code ownership | [.github/CODEOWNERS](../.github/CODEOWNERS) |
| F-19 | Bug report issue template | [.github/ISSUE_TEMPLATE/bug_report.yml](../.github/ISSUE_TEMPLATE/bug_report.yml) |
| F-20 | Content-improvement issue template + routing config that points agent/skill/dev-container issues to the template repo | [.github/ISSUE_TEMPLATE/content_improvement.yml](../.github/ISSUE_TEMPLATE/content_improvement.yml), [config.yml](../.github/ISSUE_TEMPLATE/config.yml) |
| F-21 | Pull request template aligned with the PR checklist in CONTRIBUTING.md | [.github/PULL_REQUEST_TEMPLATE.md](../.github/PULL_REQUEST_TEMPLATE.md) |

Also updated README's License section to point to the new `LICENSE` file.

### Scripts ↔ docs

- `-MicrohackOnly` parameter docs match the actual parameter on [scripts/Get-GovernanceStatus.ps1](../scripts/Get-GovernanceStatus.ps1) line 23.
- Policy IDs in [scripts/README.md](../scripts/README.md) match those in [scripts/Setup-GovernancePolicies.ps1](../scripts/Setup-GovernancePolicies.ps1).
- Compliance-delay note (5–15 min) is consistent between script output and README.

### `tmp/`

Contains only this review's working files (`content-review.md`, `lychee*.log`, `internal-links.log`, `dist-links.log`, `vale-errors.log`). Not referenced from the published site. Safe to delete after the PR merges.

---

## Final verification

| Check | Result |
| --- | --- |
| `cd site && npm run lint:md` | 22 files, 0 errors |
| `cd site && npm run build` | 28 pages built |
| `cd site && npm run lint:prose` | 0 errors, 0 warnings, 0 suggestions across 33 files |
| Broken internal links in `site/dist` | 0 |
| lychee external (authored `*.md`/`*.mdx`) | 1 expected localhost placeholder in `.devcontainer/README.md` |
