# Permissions and Safety Boundaries

## Workspace

- Default authority: read and write within the repository workspace only.
- Allowed local operations: inspect files, create or edit project files, run
  local tests, run local development servers, and inspect generated output.
- Do not read unrelated directories or private data for project context.

## Commands

- Prefer existing project tooling and documented commands.
- Do not run destructive cleanup commands unless the exact target is explicit
  and the operation is required by the task.
- Never delete user-authored files as part of routine cleanup.

## External Effects

- Treat network calls, credential use, repository publication, CI/CD changes,
  and irreversible service actions as separate risk boundaries.
- Verify the exact destination, scope, and expected effect before performing
  an external action.
- Keep secrets out of source files, logs, and task state.
- Git pushes to the configured project remote are part of the milestone
  workflow when the user has requested progress synchronization.
- Push only the intended milestone commit; never force-push or rewrite remote
  history as part of routine progress updates.
