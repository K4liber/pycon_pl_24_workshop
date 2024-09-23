from dataclasses import dataclass
from functools import partial
import logging
import os
import threading
from typing import Any, Callable

from task.fibonacci import fibonacci


_logger = logging.getLogger(__name__)


@dataclass
class CallableReturn:
    thread_id: int
    result: Any
    pid_to_memory_usage: dict[int, float]


CALLBACK_TYPE = Callable[[CallableReturn | None], Any]


@dataclass(frozen=True)
class _Callables:
    FIBONACCI: str = 'FIBONACCI'
    TEST_NUMPY: str = 'TEST NUMPY'


CALLABLES = _Callables()

_name_to_callable  = {
    CALLABLES.FIBONACCI: fibonacci,
    # CALLABLES.TEST_NUMPY: test_numpy
}


def get_available_callables() -> list[str]:
    return list(_name_to_callable.keys())


def wrapped_function(
        callable: Callable[[], Any],
        use_psutil: bool = True
    ) -> Any:
    pid = os.getpid()
    tid = threading.get_native_id()
    _logger.info(f'Running on process with PID = {pid}, TID = {tid}')
    result = callable()
    pid_to_memory_usage = {
        pid: 0
    }

    if use_psutil:
        try:
            import psutil
            process = psutil.Process(pid=pid)
            memory_usage = process.memory_info().rss / 1024 ** 2
            _logger.info(f'Memory usage in process with PID = {pid}: {memory_usage} MB')
            pid_to_memory_usage = {
                pid: memory_usage
            }
        except ImportError as e:
            _logger.warning(e)
    

    return CallableReturn(
        thread_id=tid,
        result=result,
        pid_to_memory_usage=pid_to_memory_usage
    )


def get_callable(
        callable_name: str,
        args: list[Any] = [],
        use_psutil: bool = True
    ) -> Callable[[], CallableReturn]:
    return partial(
        wrapped_function,
        partial(
            _name_to_callable[callable_name],
            *args
        ),
        use_psutil
    )
