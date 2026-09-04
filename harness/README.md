# Development Harness

This directory defines the development contract for the agent building
`easy-task-helper`.

The harness is process documentation and state, not product runtime code.
Keep it technology-neutral until an implementation decision is recorded.

## Files

- `objectives.md`: product direction and phase goals.
- `standards.md`: implementation, documentation, and verification rules.
- `permissions.md`: workspace authority and external-side-effect boundaries.
- `workflow.md`: plan, execute, verify, retry, and stop protocol.
- `development-guide.md`: detailed architecture, lifecycle, testing, commit,
  and handoff guide.
- `phase-1-plan.md`: executable scope and acceptance contract for the minimal
  product shell.
- `state/task-state.json`: current task state for handoff and recovery.
- `templates/acceptance.md`: acceptance checklist for each concrete task.
- `logs/`: durable execution notes; one Markdown file per meaningful task.

## First Phase

The first phase is harness establishment. Product code starts only after the
harness acceptance checklist is complete and the next task is explicitly
selected.
