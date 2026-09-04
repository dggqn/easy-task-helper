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

This phase is pending. It will define the smallest Electron/Python loop that
can select a frontend Web project and display a governed task conversation.
