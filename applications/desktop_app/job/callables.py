from dataclasses import dataclass
from functools import partial
import os
from typing import Any, Callable

from task.fibonacci import fibonacci


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


def wrapped_function(callable: Callable[[], Any]) -> Any:
    pid = os.getpid()
    print(f'Running on process with PID = {pid}')
    result = callable()

    try:
        import psutil
        process = psutil.Process(pid=pid)
        memory_usage = process.memory_info().rss / 1024 ** 2
        print(f'Memory usage in process with PID = {pid}: {memory_usage} MB')
    except ImportError:
        pass

    return result


def get_callable(
        callable_name: str,
        wrap: bool = False,
        args: list[Any] = []
    ) -> Callable:
    if wrap:
        return partial(
            wrapped_function,
            partial(
                _name_to_callable[callable_name],
                *args
            )
        )
    else:
        return _name_to_callable[callable_name]
