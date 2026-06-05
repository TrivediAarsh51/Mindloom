from dataclasses import dataclass, field


@dataclass
class AgentMessage:

    sender: str

    receiver: str

    task_id: str

    content: str

    status: str = "pending"

    metadata: dict = field(default_factory=dict)