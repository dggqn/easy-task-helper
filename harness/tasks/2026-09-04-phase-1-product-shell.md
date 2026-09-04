# Phase 1 Product Shell

- Status: ready_for_manual_approval
- Phase: Phase 1
- Goal: build a visible Electron desktop flow for selecting a frontend Web
  project and entering a task conversation page.
- Scope: Electron + React + TypeScript shell, placeholder project data,
  Chinese-first dark industrial chat UI, placeholder task progress.
- Exclusions: Agnes API, vector database, real project mutation, cloud release.

## Acceptance

- [x] User can select a frontend Web project from placeholder data.
- [x] User can enter the selected project's task conversation page.
- [x] Selected project and placeholder task progress are visible.
- [x] Required unit tests pass.
- [x] Type checking passes.
- [x] Production build passes.
- [x] Direct interaction verification passes.
- [x] GitHub Actions CI is configured for available checks.
- [ ] User manually verifies and explicitly approves Phase 1.

## Planned Nodes

1. Foundation tooling and runnable Electron shell.
2. Project selection flow.
3. Task conversation flow and visual polish.
4. Hardening, CI, build artifact, and Phase 1 acceptance.

## Current Evidence

- Environment inspected; repository starts with harness only.
- Next action: scaffold the Electron/React/TypeScript foundation.

## Risks

- Python 3.12 is not currently available in the environment; Python work is
  outside the first frontend shell node.
- Agnes API contract remains intentionally unspecified.
- Electron runtime and Windows packaging succeeded locally; the EXE is
  unsigned because code-signing credentials are not configured.

## Next Step

User manually verifies the Phase 1 flow and explicitly approves the phase.
