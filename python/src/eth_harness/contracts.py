"""Stable data contracts shared by the CLI and future desktop bridge."""

from dataclasses import asdict, dataclass
from enum import StrEnum


class TaskStage(StrEnum):
    """The bounded lifecycle for one development request."""

    PLANNING = "planning"
    EXECUTING = "executing"
    VERIFYING = "verifying"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass(frozen=True)
class TaskRequest:
    """Input needed to create a local, inspectable development task."""

    project_name: str
    project_path: str
    instruction: str


@dataclass(frozen=True)
class TaskEvent:
    """One audit event emitted while a task advances."""

    stage: TaskStage
    message: str


@dataclass(frozen=True)
class TaskResult:
    """Serializable result returned to the Electron layer."""

    task_id: str
    stage: TaskStage
    summary: str
    plan: tuple[str, ...]
    events: tuple[TaskEvent, ...]

    def to_dict(self) -> dict[str, object]:
        """Keep serialization at the boundary so core code stays typed."""

        return asdict(self)
