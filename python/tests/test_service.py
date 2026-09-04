import pytest

from eth_harness.contracts import TaskRequest, TaskStage
from eth_harness.service import TaskService


def make_request(**changes: str) -> TaskRequest:
    values = {
        "project_name": "运营数据控制台",
        "project_path": r"D:\workspace\ops-console",
        "instruction": "为数据列表增加状态筛选",
    }
    values.update(changes)
    return TaskRequest(**values)


def test_run_returns_a_completed_reviewable_plan() -> None:
    result = TaskService().run(make_request())

    assert result.task_id == "task-0001"
    assert result.stage is TaskStage.COMPLETED
    assert "运营数据控制台" in result.summary
    assert len(result.plan) == 3
    assert [event.stage for event in result.events] == [
        TaskStage.PLANNING,
        TaskStage.EXECUTING,
        TaskStage.VERIFYING,
        TaskStage.COMPLETED,
    ]


@pytest.mark.parametrize("field", ["project_name", "project_path", "instruction"])
def test_run_rejects_required_blank_fields(field: str) -> None:
    with pytest.raises(ValueError):
        TaskService().run(make_request(**{field: "  "}))
