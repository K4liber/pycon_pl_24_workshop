from dataclasses import dataclass
from typing import Any


@dataclass
class CallableReturn:
    thread_id: int
    result: Any
    pid_to_memory_usage: dict[int, float]
