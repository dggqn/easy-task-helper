# Last Dependency Change

- Date: 2026-09-04
- Status: accepted
- Change: installed Python 3.12 through `uv`; added pytest and hatchling to
  the local Python Harness development environment.
- Verification: Python syntax compilation and 5 pytest cases pass; Electron
  lint, 4 renderer tests, and production build pass.
- Policy: after a successful dependency change, retain this file and
  `current.md` only; remove older dependency-change records unless a decision
  document requires their retention.
