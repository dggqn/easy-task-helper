# Current Dependencies

No product dependencies have been selected beyond the Phase 1 tooling baseline:

- Electron
- React
- TypeScript
- Python 3.12
- `uv`
- `pytest`
- Vitest (when renderer tests are introduced)
- Playwright (when milestone interaction checks are introduced)
- `concurrently` and `wait-on` for local desktop development orchestration
- Electron for the desktop runtime
- `electron-builder` for Windows EXE packaging
- jsdom and Testing Library for renderer unit tests
- Python 3.12 managed by `uv` for the local orchestration service
- pytest for Python unit tests
- hatchling for editable local Python package installation

Update this file whenever the effective dependency set changes. Keep versions
in actual lock files and package manifests once product scaffolding starts.
