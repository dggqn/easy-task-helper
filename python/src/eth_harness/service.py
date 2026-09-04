"""Deterministic task orchestration for the initial Python backend."""

from itertools import count

from .contracts import TaskEvent, TaskRequest, TaskResult, TaskStage
from .provider import FakeModelProvider, ModelProvider


class TaskService:
    """Create a governed task result without modifying the selected project."""

    def __init__(self, provider: ModelProvider | None = None) -> None:
        self._provider = provider or FakeModelProvider()
        self._sequence = count(1)

    def run(self, request: TaskRequest) -> TaskResult:
        """Advance a request through the Phase 2 placeholder workflow."""

        self._validate(request)
        events = [TaskEvent(TaskStage.PLANNING, "正在建立可审查的执行计划。")]
        plan = self._provider.create_plan(request)
        events.append(TaskEvent(TaskStage.EXECUTING, "假模型已返回计划；未修改项目文件。"))
        events.append(TaskEvent(TaskStage.VERIFYING, "等待后续真实执行器接入验证。"))
        events.append(TaskEvent(TaskStage.COMPLETED, "本地任务流程已完成。"))

        return TaskResult(
            task_id=f"task-{next(self._sequence):04d}",
            stage=TaskStage.COMPLETED,
            summary=plan.summary,
            plan=plan.steps,
            events=tuple(events),
        )

    @staticmethod
    def _validate(request: TaskRequest) -> None:
        if not request.project_name.strip():
            raise ValueError("project_name 不能为空")
        if not request.project_path.strip():
            raise ValueError("project_path 不能为空")
        if not request.instruction.strip():
            raise ValueError("instruction 不能为空")

