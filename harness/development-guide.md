# Development Guide

This guide explains how to develop `easy-task-helper` under the repository
harness. It is written for both the Codex development agent and a human who
later takes over the project.

## 1. Project Intent

`easy-task-helper` is a desktop development assistant. A user selects a
project, describes a feature or bug, and receives a governed implementation
workflow with code changes, verification, progress, and CI/CD support.

The first visible target is a frontend Web page project. The first product
experience should therefore make project selection, conversation, task state,
and generated Web output easy to inspect.

## 2. Architecture Boundaries

### Electron desktop layer

Electron owns the compact desktop experience:

- project selection;
- conversation input and response display;
- task progress and verification summaries;
- safe presentation of logs and generated output.

It should not contain model orchestration, prompt policy, filesystem policy, or
long-running development logic.

### Python orchestration layer

Python owns the main development workflow:

- task planning and state transitions;
- project inspection and context assembly;
- model-provider adapter calls;
- code change proposals and execution;
- tests, preview checks, and acceptance evidence;
- structured logs and recoverable task state.

The `agnes` provider is reserved behind an adapter boundary. Do not invent its
endpoint, authentication, request format, or model name before they are
provided and recorded as a decision.

### Knowledge and examples

The vector knowledge base and example-code library are context providers, not
authorities. Retrieved material must be treated as input to a task plan and
must not override repository rules or user decisions.

## 3. Recommended Repository Shape

Keep product code separate from harness documentation:

```text
AGENTS.md                 # mandatory agent entry rules
harness/                  # development governance and handoff state
  state/                  # machine-readable current task state
  logs/                   # durable milestone notes
  templates/              # reusable task and acceptance forms
electron/                 # future desktop UI
python/                   # future orchestration layer
knowledge/                # future vector KB integration
examples/                 # future reference projects and snippets
tests/                    # cross-layer or integration tests
```

Create only the directories needed by the active phase. Do not create empty
product layers merely to match the planned shape.

## 4. Standard Task Lifecycle

For every concrete task:

1. **Context**: read `AGENTS.md`, the current task state, relevant source, and
   the latest durable log.
2. **Plan**: write the goal, scope, acceptance target, risks, and checks.
3. **Implement**: make the smallest coherent change and preserve unrelated
   work.
4. **Verify**: run focused checks first; add broader checks for shared or
   user-visible behavior.
5. **Accept**: compare evidence with the acceptance target. A green command is
   not sufficient if the user-visible result is wrong.
6. **Record**: update task state and write a concise durable log.
7. **Commit**: at an appropriately sized verified milestone, commit with
   `<phase>: <milestone>` and push to `origin`. Do not commit every edit.
8. **Handoff**: leave a precise next step and known risks.

Use `harness/templates/acceptance.md` for the acceptance record. Keep one
concrete objective active at a time.

## 5. State and Logging

`harness/state/task-state.json` is the resumable summary, not a transcript. It
should contain the active task, status, acceptance targets, verified evidence,
changed files, retry count, latest commit, and next step.

Use `harness/logs/` for meaningful decisions and milestone results. A log must
answer: what changed, why, how it was verified, what remains uncertain, and
what should happen next. Never place credentials, tokens, or private unrelated
data in state or logs.

## 6. Testing and Acceptance

Testing should grow with risk:

- pure logic: deterministic unit tests;
- Python/Electron boundary: contract or integration tests;
- Web UI: local run plus direct visual/interaction inspection;
- model and knowledge integrations: adapter-level tests with fakes, then an
  explicitly configured integration check.

Every completed task needs reproducible evidence. Record the exact check or
command, its result, and any limitation. If verification fails twice for the
same cause, stop retrying and report the evidence.

## 7. Change and Commit Rules

Prefer small, reviewable commits. A phase milestone commit should include the
complete verified node, not half of a feature. Before pushing:

- inspect the changed-file list;
- run `git diff --check`;
- verify the commit message and `origin` destination;
- confirm no unrelated user changes are included.

Routine progress synchronization must never use force-push or rewrite remote
history.

### Choosing the right milestone size

A good milestone is a complete slice that can be explained in one sentence,
reviewed as one change, and verified with a focused acceptance check. It is not
so small that the history becomes a list of implementation fragments, and not
so large that unrelated features or unverifiable intermediate states are mixed
together.

Use these questions before committing:

- Does this change meet one coherent acceptance target?
- Can its verification evidence be listed without referring to unfinished
  future work?
- Would splitting it make either part independently useful and testable?
- Would combining it with the next planned change obscure review or failure
  diagnosis?

Examples of suitable milestones include a complete project-selection flow, a
tested Electron/Python boundary, or a working vector-retrieval slice. A single
button, a formatting-only change, or an entire unverified product phase is not
an appropriate milestone.

## 8. Taking Over the Project

A new developer should start with:

1. `AGENTS.md` for mandatory rules;
2. this guide for architecture and workflow;
3. `harness/state/task-state.json` for the current task;
4. the latest file in `harness/logs/` for context;
5. `git log --oneline -5` and `git status` for repository state.

If state, logs, and code disagree, trust directly verified repository evidence,
then update the harness records before continuing.
