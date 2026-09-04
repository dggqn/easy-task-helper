# Permissions and Safety Boundaries

## Workspace

- Default authority: read and write within the repository workspace only.
- Allowed local operations: inspect files, create or edit project files, run
  local tests, install project dependencies, run local development servers,
  modify project configuration, and inspect generated output.
- The user grants full authority within this workspace except deletion of the
  workspace root directory itself.
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

## Sensitive Data

- Apply enterprise-style defaults to future project context: do not place
  credentials, `.env` contents, private keys, secrets, or unrelated private
  files into source control, logs, prompts, or knowledge indexes.
- For the initial frontend Web-page target, keep the implementation local and
  avoid collecting enterprise data by default.
- Define the model-data transmission policy before real model integration.

## CI/CD

- GitHub Actions is required for automated CI when the product shell exists.
- CI should run the relevant lint, type, unit-test, and build checks.
- Initial CD ends with generating a local desktop EXE artifact. Do not publish,
  deploy, or release externally unless a later task explicitly adds that scope.
