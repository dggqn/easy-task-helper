# Last Dependency Change

- Date: 2026-09-04
- Status: accepted
- Change: added Electron, concurrently, wait-on, Vitest, jsdom, Testing
  Library, and electron-builder for the Phase 1 desktop shell, tests, and local
  EXE packaging.
- Verification: lint, unit tests, and renderer build pass. Electron runtime
  binary download remains pending because the current command-line network path
  cannot fetch Electron archives.
- Policy: after a successful change, retain this file and `current.md` only;
  remove older dependency-change records unless a decision document requires
  their retention.
