# Phase 2: Python Harness Foundation

## Goal

Deliver a local Python orchestration foundation that turns a selected frontend
Web project and task instruction into a structured, auditable plan. The model
provider is deliberately fake until the Agnes endpoint, authentication, and
request contract are supplied.

## Scope

- Python 3.12 project managed by `uv`.
- Typed task contracts, lifecycle events, validation, and structured result.
- Replaceable provider interface with a deterministic fake implementation.
- JSON stdin/stdout command boundary for future Electron IPC integration.
- Pytest unit and command-boundary tests.
- CI coverage for Python syntax and unit tests.

## Exclusions

- Real Agnes API calls, credentials, or assumed request format.
- Electron UI flow changes or Electron-to-Python live IPC.
- Project filesystem mutation, code generation, vector retrieval, and CI/CD
  execution against a selected user project.

## Milestones

1. Python environment, typed contracts, fake provider, and unit tests.
2. JSON command boundary and CI validation.
3. Phase hardening and automated acceptance evidence.

## Completion Evidence

- `uv run --project python pytest` passes.
- `uv run --project python python -m compileall -q src` passes.
- A JSON request produces a structured completed task result.
- Repository CI runs the Python checks alongside Electron checks.
- User manually verifies and explicitly approves Phase 2.

