"""SQLite persistence for task state and audit events."""

from __future__ import annotations

import os
import sqlite3
from pathlib import Path

from .contracts import TaskEvent, TaskRequest, TaskResult, TaskStage


def default_database_path() -> Path:
    """Return a per-user database path outside the selected project."""
    data_root = os.environ.get("APPDATA")
    return (Path(data_root) / "eth" / "data" / "tasks.db") if data_root else Path.home() / ".local" / "share" / "eth" / "tasks.db"


class TaskStore:
    """Small transactional repository backed by SQLite."""

    def __init__(self, database_path: str | Path | None = None) -> None:
        self.database_path = Path(database_path) if database_path else Path(":memory:")
        self._memory_connection: sqlite3.Connection | None = None
        if self.database_path != Path(":memory:"):
            self.database_path.parent.mkdir(parents=True, exist_ok=True)
        self._initialize()

    def _connect(self) -> sqlite3.Connection:
        if self.database_path == Path(":memory:"):
            if self._memory_connection is None:
                self._memory_connection = sqlite3.connect(":memory:")
                self._memory_connection.row_factory = sqlite3.Row
            return self._memory_connection
        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        return connection

    def _initialize(self) -> None:
        with self._connect() as connection:
            connection.executescript(
                """
                PRAGMA journal_mode = WAL;
                CREATE TABLE IF NOT EXISTS tasks (
                    task_id TEXT PRIMARY KEY, project_name TEXT NOT NULL,
                    project_path TEXT NOT NULL, instruction TEXT NOT NULL,
                    stage TEXT NOT NULL, summary TEXT NOT NULL DEFAULT '',
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                );
                CREATE TABLE IF NOT EXISTS task_events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task_id TEXT NOT NULL REFERENCES tasks(task_id),
                    stage TEXT NOT NULL, message TEXT NOT NULL,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                );
                CREATE INDEX IF NOT EXISTS idx_task_events_task_id ON task_events(task_id, id);
                """
            )

    def create_task(self, task_id: str, request: TaskRequest) -> None:
        with self._connect() as connection:
            connection.execute(
                "INSERT INTO tasks (task_id, project_name, project_path, instruction, stage) VALUES (?, ?, ?, ?, ?)",
                (task_id, request.project_name, request.project_path, request.instruction, TaskStage.PLANNING.value),
            )

    def has_task(self, task_id: str) -> bool:
        with self._connect() as connection:
            return connection.execute("SELECT 1 FROM tasks WHERE task_id = ?", (task_id,)).fetchone() is not None

    def append_event(self, task_id: str, event: TaskEvent) -> None:
        with self._connect() as connection:
            connection.execute("INSERT INTO task_events (task_id, stage, message) VALUES (?, ?, ?)", (task_id, event.stage.value, event.message))
            connection.execute("UPDATE tasks SET stage = ?, updated_at = CURRENT_TIMESTAMP WHERE task_id = ?", (event.stage.value, task_id))

    def complete_task(self, result: TaskResult) -> None:
        with self._connect() as connection:
            connection.execute("UPDATE tasks SET stage = ?, summary = ?, updated_at = CURRENT_TIMESTAMP WHERE task_id = ?", (result.stage.value, result.summary, result.task_id))

    def get_task(self, task_id: str) -> dict[str, object] | None:
        with self._connect() as connection:
            row = connection.execute("SELECT * FROM tasks WHERE task_id = ?", (task_id,)).fetchone()
        return dict(row) if row else None

    def list_events(self, task_id: str) -> list[dict[str, object]]:
        with self._connect() as connection:
            rows = connection.execute("SELECT * FROM task_events WHERE task_id = ? ORDER BY id", (task_id,)).fetchall()
        return [dict(row) for row in rows]
