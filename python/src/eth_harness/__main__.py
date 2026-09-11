"""JSON-lines command entry point for the future Electron process bridge."""

import json
import sys

from .contracts import TaskRequest
from .service import TaskService
from .storage import TaskStore, default_database_path


def main() -> int:
    """Read one JSON request from stdin and write one JSON result to stdout."""

    try:
        payload = json.load(sys.stdin)
        request = TaskRequest(
            project_name=str(payload["project_name"]),
            project_path=str(payload["project_path"]),
            instruction=str(payload["instruction"]),
        )
        print(json.dumps(TaskService(store=TaskStore(default_database_path())).run(request).to_dict(), ensure_ascii=False))
        return 0
    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
