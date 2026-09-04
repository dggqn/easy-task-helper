# CI Quality Gates

## Required Before Merge

- Electron frontend code checks pass.
- Electron frontend production build passes.
- Python harness syntax checks pass.
- Python harness unit tests pass.
- No `.env`, API key, token, private key, or equivalent secret file is
  included in the commit.
- Dependency lock files contain no unexplained abnormal change.

GitHub Actions should run the same checks as local development whenever the
corresponding product layer exists. A missing layer is recorded as not
applicable until that layer is introduced. CI failure blocks merge.
