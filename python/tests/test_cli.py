import json
import subprocess
import sys


def test_cli_returns_json_for_a_valid_request() -> None:
    request = {
        "project_name": "运营数据控制台",
        "project_path": r"D:\\workspace\\ops-console",
        "instruction": "增加状态筛选",
    }

    completed = subprocess.run(
        [sys.executable, "-m", "eth_harness"],
        input=json.dumps(request, ensure_ascii=False),
        text=True,
        capture_output=True,
        check=True,
    )

    result = json.loads(completed.stdout)
    assert result["stage"] == "completed"
    assert result["plan"][0] == "分析需求：增加状态筛选"
