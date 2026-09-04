# Development Standards

## Code

- Match the selected language's established formatter and lint rules.
- Use small modules with one clear responsibility.
- Name symbols by intent; avoid unexplained abbreviations.
- Validate inputs at boundaries and return actionable errors.
- Keep configuration separate from business logic.

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
