# Phase 1: Minimal Product Shell

## Goal

Deliver a visible desktop flow for choosing a frontend Web project and entering
a Chinese chat-oriented task page. All displayed project and task data may be
local placeholders; no model API, vector database, or real project mutation is
in scope.

## Scope

- Electron desktop application with React and TypeScript.
- A project-selection view showing placeholder frontend Web projects.
- A selected-project task conversation view.
- Placeholder task progress/status displayed alongside the conversation.
- Chinese-first, dark industrial technology styling with common desktop scaling
  support.

## Exclusions

- Agnes API calls, credentials, and prompt execution.
- Vector database, embeddings, and example-code retrieval.
- Real project-file modification or bug fixing.
- Cloud deployment, software publishing, or external release.

## Suggested Milestones

1. **Foundation**: Electron/React/TypeScript tooling starts, type-checks, and
   builds.
2. **Project selection flow**: placeholder project list can be selected and
   the selection is represented in UI state with focused tests.
3. **Conversation flow**: selected project opens the conversation page with
   placeholder task state and direct interaction verification.
4. **Phase hardening**: full unit/type/build checks, GitHub Actions CI, and
   user manual acceptance.

## Completion Evidence

- Applicable unit tests pass.
- Type checking passes.
- Production build passes.
- The desktop flow is directly exercised: choose a project, enter its task
  page, and observe the corresponding placeholder progress.
- User gives explicit Phase 1 approval.
