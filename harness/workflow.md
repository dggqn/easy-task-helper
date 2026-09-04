# Development Workflow

## 1. Plan

- State the concrete task and why it is needed.
- List affected areas and a measurable acceptance target.
- Identify assumptions, risks, and required external information.

## 2. Execute

- Inspect the relevant files before editing.
- Implement the smallest coherent change.
- Keep progress notes short and factual.

## 3. Verify

- Run the narrowest useful check first.
- Add broader checks for shared or user-facing behavior.
- Inspect generated output when visual or integration behavior matters.
- Record commands, results, and unresolved risks.

## 4. Retry

- Retry only after identifying a distinct cause or changing an input.
- Maximum automatic retries for one failing check: 2.
- After the limit, stop and report evidence instead of looping.

## 5. Stop Conditions

Stop and report when:

- acceptance criteria are met;
- required product information is missing;
- the change would exceed the declared authority;
- a destructive or external action needs a new decision;
- verification remains failing after the retry limit;
- the working tree contains an unexplained conflicting change.

## 6. Milestone Progress Commits

- Commit and push at milestone boundaries, not after every file edit or small
  correction.
- A milestone is an appropriately sized, independently verifiable unit that
  delivers a coherent slice of capability, closes a meaningful acceptance
  target, or records a durable architecture decision.
- A milestone should be large enough to have user or engineering value, but
  small enough that its purpose, changed files, and verification evidence are
  easy to review. Split a milestone when it contains unrelated outcomes; join
  adjacent edits when they cannot be meaningfully verified alone.
- Typical milestone examples: a complete project-selection flow, a tested
  Python/Electron contract, or a working knowledge-retrieval slice. Non-
  milestones include one-line fixes, formatting-only edits, and intermediate
  scaffolding with no independently useful behavior.
- Run the relevant checks before committing. Do not commit known failing work
  unless the task is explicitly a failure checkpoint.
- Push the milestone commit to the configured `origin` remote after verifying
  the commit summary and destination.
- If the push fails, keep the local commit and record the exact failure and
  recovery step in the task state/log; do not rewrite history automatically.

## 7. Handoff

Update `harness/state/task-state.json` and add a durable note in `harness/logs/`
for meaningful work. Include current status, verified result, next step, and
known risks.
