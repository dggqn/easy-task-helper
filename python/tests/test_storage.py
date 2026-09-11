from eth_harness.contracts import TaskRequest
from eth_harness.service import TaskService
from eth_harness.storage import TaskStore


def test_task_and_events_are_persisted(tmp_path) -> None:
    store = TaskStore(tmp_path / "tasks.db")
    result = TaskService(store=store).run(TaskRequest("demo", str(tmp_path), "创建页面"))

    task = store.get_task(result.task_id)
    assert task is not None
    assert task["stage"] == "completed"
    assert task["project_name"] == "demo"
    assert [event["stage"] for event in store.list_events(result.task_id)] == [
        "planning", "executing", "verifying", "completed"
    ]
