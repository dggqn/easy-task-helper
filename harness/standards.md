# Development Standards

## Code

- Match the selected language's established formatter and lint rules.
- Use small modules with one clear responsibility.
- Name symbols by intent; avoid unexplained abbreviations.
- Validate inputs at boundaries and return actionable errors.
- Keep configuration separate from business logic.

## Technology Baseline

- Desktop and renderer: Electron, React, and TypeScript.
- Python: version 3.12, with `uv` for dependency and environment management.
- Python unit tests: `pytest`.
- Renderer unit tests: Vitest when the renderer is introduced.
- End-to-end interaction checks: Playwright for milestone-level Electron/Web
  workflows when the product shell is ready.
- Do not add model or vector-database packages until their integration contract
  is defined.

## Comments and Documentation

- Comments explain why, constraints, or non-obvious behavior.
- Do not narrate obvious syntax.
- Public modules and workflows need short usage documentation.
- Update documentation when behavior, commands, or acceptance criteria change.

## Testing

- Add focused tests for new logic and failure paths.
- Verify permission boundaries and stop conditions when touched.
- Prefer deterministic tests; isolate network and model calls behind adapters.
- A test command and its result must be recorded for completed work.
- Small isolated UI changes, such as one dialog or select control, require at
  least type checking and focused unit coverage when logic is introduced.
- A complete page or major module requires unit tests, type checking, a
  production build, and direct interaction verification.
- A phase requires all applicable automated evidence plus explicit user manual
  verification and approval.

## UI

- Chinese is the default product language.
- Use a concise dark industrial technology style with a chat-oriented primary
  workflow.
- Support common desktop window sizes and normal operating-system display
  scaling. Avoid layout assumptions tied to one fixed resolution.

## Change Scope

- Make the smallest complete change that satisfies the current acceptance
  target.
- Do not mix unrelated refactors, dependency upgrades, or visual redesigns.
- Preserve user changes already present in the working tree.

## Git Milestone Records

- Commit messages use the form `<phase>: <milestone>`.
- The commit body should summarize the completed node and verification result.
- Do not create a commit for every edit. Keep one coherent milestone per
  commit, and group supporting edits that belong to the same acceptance target.
- Avoid milestones that are trivial implementation fragments or broad phase
  dumps with no clear verification boundary.
- Before pushing, confirm the commit contains only intended project changes and
  that the remote is the expected repository.
