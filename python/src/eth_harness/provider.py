"""Model-provider boundary. Real Agnes integration will replace the fake."""

from dataclasses import dataclass
from typing import Protocol

from .contracts import TaskRequest


@dataclass(frozen=True)
class ModelPlan:
    """The minimal model output required by the orchestration workflow."""

    summary: str
    steps: tuple[str, ...]


class ModelProvider(Protocol):
    """Provider contract that avoids assuming Agnes request or auth details."""

    def create_plan(self, request: TaskRequest) -> ModelPlan:
        """Return a proposed, reviewable plan for one request."""


class FakeModelProvider:
    """Deterministic local replacement used until the Agnes contract is known."""

    def create_plan(self, request: TaskRequest) -> ModelPlan:
        return ModelPlan(
            summary=f"已为 {request.project_name} 建立本地执行计划。",
            steps=(
                f"分析需求：{request.instruction}",
                "检查受影响的前端页面与现有测试。",
                "生成变更建议并执行对应验证。",
            ),
        )
