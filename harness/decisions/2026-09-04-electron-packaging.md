# Decision: Phase 1 Desktop Packaging

- Date: 2026-09-04
- Status: accepted
- Scope: local Windows delivery

## Decision

Use Electron with electron-builder to package the Phase 1 desktop shell. Build
a Windows NSIS installer named `eth-v1.0.0.exe` under
`artifacts/desktop/eth-v1.0.0/`.

## Consequences

The package command is `npm run package:win` from `electron/`. The output is
local only and remains excluded from Git. The latest three successful artifact
directories are retained under the harness release policy.
