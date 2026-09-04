# Project Development Harness

This file is the entry point for every development task in this repository.
It governs the Codex development process. It is not runtime behavior for the
future product and must not be imported by application code.

## Product Direction

- Product: Electron desktop client plus Python AI development orchestration.
- First supported project type: frontend Web pages.
- Planned context sources: vector knowledge base and example code.
- Planned model provider: `agnes`; its API contract is intentionally deferred.

## Working Authority

- The workspace root is `D:\\personal_jdx\\personal_code\\easy-task-helper`.
- Read and write authority is limited to this workspace by default.
- Do not invent external API details, credentials, or product requirements.
- Keep unrelated user changes intact.

## Required Development Loop

1. Read `harness/state/task-state.json` and the current task context.
2. Write a small plan with an explicit acceptance target.
3. Make the smallest coherent change.
4. Run focused checks, then broader checks when the change warrants them.
5. At a meaningful milestone, commit the verified node and push it to `origin`
   according to `harness/workflow.md`.
6. Record result, changed files, commit, risks, and next step in the harness
   state/log.
7. Stop when the acceptance target is met or a defined stop condition occurs.

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
- `harness/state/task-state.json`
