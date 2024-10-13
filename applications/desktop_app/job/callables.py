from dataclasses import dataclass
from functools import partial
import logging
import os
import threading
from typing import Any, Callable

from job.callable_return import CallableReturn
from task.fibonacci import fibonacci


_logger = logging.getLogger(__name__)
CALLBACK_TYPE = Callable[[CallableReturn | None], Any]


@dataclass(frozen=True)
class _Callables:
    FIBONACCI: str = 'FIBONACCI'
    TEST_NUMPY: str = 'TEST NUMPY'


CALLABLES = _Callables()

def _get_available_callables():
    available_callables = {
        CALLABLES.FIBONACCI: fibonacci,
    }    

    try:
        from task.test_numpy import test_numpy
        available_callables[CALLABLES.TEST_NUMPY] = test_numpy
    except Exception:
        pass

    return available_callables


def get_available_callables() -> list[str]:
    return list(_get_available_callables().keys())


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
            _get_available_callables()[callable_name],
            *args
        ),
        use_psutil
    )
