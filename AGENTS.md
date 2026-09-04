# Project Development Harness

This file is the entry point for every development task in this repository.
It governs the Codex development process. It is not runtime behavior for the
future product and must not be imported by application code.

## Product Direction

- Product: Electron desktop client plus Python AI development orchestration.
- First supported project type: frontend Web pages.
- Product stack: Electron, React, TypeScript, Python 3.12, and `uv`.
- Planned context sources: vector knowledge base and example code.
- Planned model provider: `agnes`; its API contract is intentionally deferred.

## Working Authority

- The workspace root is `D:\\personal_jdx\\personal_code\\easy-task-helper`.
- Read and write authority is limited to this workspace by default.
- Local installation, configuration, test execution, and development-server
  operations are allowed within this workspace. Do not delete the workspace
  root directory.
- Do not invent external API details, credentials, or product requirements.
- Keep unrelated user changes intact.

## Required Development Loop

1. Read `harness/state/task-state.json` and the current task context.
2. Apply `harness/admission.md`; stop if the task lacks an executable target.
3. Write a small plan with an explicit acceptance target.
4. Make the smallest coherent change.
5. Apply `harness/definition-of-done.md` and run the checks matching the change
   size.
6. At an appropriately sized, verified milestone, commit the complete node and
   push it to `origin` according to `harness/workflow.md`; do not commit every
   small edit.
7. Record result, changed files, commit, risks, and next step in the harness
   state/log.
8. Stop when the acceptance target is met or a defined stop condition occurs.

## Escalation Boundaries

- Explain and wait before changing architecture, dependencies, persistent data
  structures, or user flows.
- Local implementation improvements that preserve those boundaries may proceed.
- A phase is complete only after its automated checks pass and the user has
  manually verified and approved the phase result.

## Quality Bar

- Prefer simple, maintainable code over premature abstraction.
- Keep comments concise and explain intent or non-obvious constraints.
- Preserve existing behavior unless the task explicitly changes it.
- Every user-visible behavior needs a reproducible verification step.
- Do not claim success without evidence from a check or direct inspection.

## Governing Documents

- `harness/objectives.md`
- `harness/standards.md`
- `harness/permissions.md`
- `harness/workflow.md`
- `harness/development-guide.md`
- `harness/admission.md`
- `harness/definition-of-done.md`
- `harness/state/task-state.json`
