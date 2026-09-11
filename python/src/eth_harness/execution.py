"""Read-only project inspection and allow-listed command execution."""

from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path


class WorkspaceViolation(ValueError):
    """Raised when a path escapes the configured workspace."""


def resolve_workspace_path(workspace: str | Path, target: str | Path) -> Path:
    root = Path(workspace).resolve()
    path = (root / target).resolve() if not Path(target).is_absolute() else Path(target).resolve()
    if path != root and root not in path.parents:
        raise WorkspaceViolation("目标路径必须位于当前工作区内")
    return path


@dataclass(frozen=True)
class ProjectInspection:
    path: str
    files: tuple[str, ...]
    directories: tuple[str, ...]


def inspect_project(workspace: str | Path, target: str | Path = ".", max_entries: int = 200) -> ProjectInspection:
    path = resolve_workspace_path(workspace, target)
    if not path.is_dir():
        raise ValueError("检查目标必须是目录")
    files: list[str] = []
    directories: list[str] = []
    for entry in sorted(path.iterdir(), key=lambda item: item.name.lower()):
        (directories if entry.is_dir() else files).append(entry.name)
        if len(files) + len(directories) >= max_entries:
            break
    return ProjectInspection(str(path), tuple(files), tuple(directories))


ALLOWED_COMMANDS: dict[str, tuple[str, ...]] = {
    "python-tests": ("uv", "run", "pytest"),
    "python-syntax": ("uv", "run", "python", "-m", "compileall", "-q", "src"),
}


@dataclass(frozen=True)
class CommandRun:
    name: str
    command: tuple[str, ...]
    return_code: int
    output: str
    timed_out: bool


def run_allowed_command(name: str, workspace: str | Path, timeout_seconds: int = 30) -> CommandRun:
    if name not in ALLOWED_COMMANDS:
        raise ValueError("命令不在允许列表中")
    cwd = resolve_workspace_path(workspace, ".")
    command = ALLOWED_COMMANDS[name]
    try:
        completed = subprocess.run(command, cwd=cwd / "python", capture_output=True, text=True, timeout=timeout_seconds, check=False)
        return CommandRun(name, command, completed.returncode, (completed.stdout + completed.stderr).strip(), False)
    except subprocess.TimeoutExpired as error:
        output = (error.stdout or "") + (error.stderr or "")
        return CommandRun(name, command, -1, output, True)
