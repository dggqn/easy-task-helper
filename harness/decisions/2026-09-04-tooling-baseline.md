# Decision: Initial Tooling Baseline

- Date: 2026-09-04
- Status: accepted
- Scope: Phase 1 product shell

## Decision

Use Electron + React + TypeScript for the desktop product shell. Use Python
3.12 with `uv` for the Python layer, `pytest` for Python unit tests, Vitest for
renderer unit tests, and Playwright for milestone-level interaction checks.

## Consequences

Future dependency or runtime changes must be recorded as a new decision and
must follow the dependency change policy.
