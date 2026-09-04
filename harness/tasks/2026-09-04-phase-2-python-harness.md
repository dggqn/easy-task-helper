# Phase 2 Python Harness

- Task ID: `phase-2-python-harness`
- Goal: create the local Python orchestration foundation for a selected
  frontend Web project and a development instruction.
- Scope: typed task workflow, deterministic fake model provider, JSON command
  boundary, tests, and CI validation.
- Exclusions: real Agnes integration, packaged Python distribution, project
  file writes, vector knowledge, and generated code execution.

## Acceptance

- [x] Valid task input yields a structured plan and completed task state.
- [x] Missing required fields yield an explicit validation error.
- [x] Provider can be replaced without changing orchestration code.
- [x] Python syntax and unit tests pass under Python 3.12 through `uv`.
- [x] CI validates the Python package.
- [x] Electron invokes the local development-time Python bridge and displays a
  Chinese structured plan.
- [ ] User manually verifies and approves Phase 2.

## Risks

- The Agnes endpoint/authentication/request contract is intentionally unknown.
- The fake provider must not be mistaken for a live model integration.

## Automated Evidence

- `uv run python -m compileall -q src`: passed.
- `uv run pytest`: passed, 5 tests.
- `npm run lint`, `npm run test`, and `npm run build`: passed; 4 renderer tests.
- Direct Electron development run: selected the placeholder project, entered
  `为数据列表增加状态筛选`, and observed the UTF-8 Chinese plan returned by
  the Python fake provider.

## Result

- Status: ready for manual approval.
- Known limitation: the packaged EXE does not yet bundle Python. The bridge is
  intentionally limited to the local development environment in this phase.
- Next step: user manually verifies Phase 2 and explicitly approves it.
