"""Deterministic task orchestration for the local Python backend."""

from itertools import count

from .contracts import TaskEvent, TaskRequest, TaskResult, TaskStage
from .provider import FakeModelProvider, ModelProvider
from .storage import TaskStore


class TaskService:
    """Create a governed task result without modifying the selected project."""

    def __init__(self, provider: ModelProvider | None = None, store: TaskStore | None = None) -> None:
        self._provider = provider or FakeModelProvider()
        self._store = store or TaskStore()
        self._sequence = count(1)

    def run(self, request: TaskRequest) -> TaskResult:
        """Advance a request and persist each lifecycle event."""
        self._validate(request)
        task_id = f"task-{next(self._sequence):04d}"
        while self._store.has_task(task_id):
            task_id = f"task-{next(self._sequence):04d}"
        self._store.create_task(task_id, request)
        events: list[TaskEvent] = []

        def emit(stage: TaskStage, message: str) -> None:
            event = TaskEvent(stage, message)
            events.append(event)
            self._store.append_event(task_id, event)

        emit(TaskStage.PLANNING, "正在建立可审查的执行计划。")
        plan = self._provider.create_plan(request)
        emit(TaskStage.EXECUTING, "模型已返回计划；未修改项目文件。")
        emit(TaskStage.VERIFYING, "等待后续真实执行器接入验证。")
        emit(TaskStage.COMPLETED, "本地任务流程已完成。")
        result = TaskResult(task_id, TaskStage.COMPLETED, plan.summary, plan.steps, tuple(events))
        self._store.complete_task(result)
        return result

    @staticmethod
    def _validate(request: TaskRequest) -> None:
        if not request.project_name.strip():
            raise ValueError("project_name 不能为空")
        if not request.project_path.strip():
            raise ValueError("project_path 不能为空")
        if not request.instruction.strip():
            raise ValueError("instruction 不能为空")
