# Local EXE Build Guide

## Initial Release Contract

- Product artifact name: `eth-v<version>.exe`.
- Initial version: `v1.0.0`.
- Output directory: `artifacts/desktop/eth-v<version>/`.
- Build output is local and is not committed to Git.
- Initial CD stops after a successful local EXE build; no external release or
  deployment is included.

## Retention

Keep the latest three successful EXE version directories. Remove older
successful artifacts only after confirming the newer build is complete and
readable. Never remove the current successful artifact during routine cleanup.

## Build Evidence

Record the build command, version, output path, file existence, and packaging
limitation in the task acceptance record.
