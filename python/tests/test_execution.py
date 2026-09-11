import pytest

from eth_harness.execution import WorkspaceViolation, inspect_project, run_allowed_command


def test_inspection_stays_inside_workspace(tmp_path) -> None:
    (tmp_path / "README.md").write_text("demo", encoding="utf-8")
    result = inspect_project(tmp_path)
    assert result.files == ("README.md",)


def test_inspection_rejects_escape(tmp_path) -> None:
    with pytest.raises(WorkspaceViolation):
        inspect_project(tmp_path, "..")


def test_unknown_command_is_rejected(tmp_path) -> None:
    with pytest.raises(ValueError):
        run_allowed_command("format-disk", tmp_path)
