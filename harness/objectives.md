# Objectives

## Product Goal

Build a desktop development assistant that can select a project, understand
its context, implement frontend Web features, repair bugs, manage code, and
support automated CI/CD through a governed agent workflow.

## Planned Architecture

- Electron: compact project selection, conversation, and progress UI.
- Python: model-facing orchestration, planning, execution, verification, and
  audit data.
- Vector knowledge base: searchable project and engineering context.
- Example code: reusable implementation references and patterns.
- `agnes`: reserved model provider adapter; endpoint and authentication remain
  unspecified until supplied.

## Phase 0: Development Harness

Acceptance targets:

- The agent rules are discoverable from the repository root.
- Development boundaries and stop conditions are explicit.
- A new task can be planned, executed, verified, and recorded consistently.
- Current state can be handed off without relying on chat history alone.

## Phase 1: Minimal Product Shell

Goal: create a Chinese-first, dark industrial-style Electron desktop shell for
selecting a frontend Web project and displaying a task conversation page.

Acceptance targets:

- The user can select a frontend Web project from placeholder data.
- The user can enter the task conversation page for the selected project.
- The selected project and placeholder task progress are visible on that page.
- Type checks, unit tests, production build, and direct interaction checks
  pass.
- The user manually verifies and explicitly approves Phase 1 before Phase 2
  begins.

Implementation details and the task breakdown are in `phase-1-plan.md`.
