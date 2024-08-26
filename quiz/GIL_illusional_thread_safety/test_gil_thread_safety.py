# noqa: f401

"""
import dis
dis.dis(illusional_thread_safe_task)

>>>
 16           RESUME                   0

 17           LOAD_GLOBAL              0 (_global_dict)
              LOAD_CONST               1 (0)
              COPY                     2
              COPY                     2
              BINARY_SUBSCR
              LOAD_CONST               2 (1)
              BINARY_OP               13 (+=)
              SWAP                     3
              SWAP                     2
              STORE_SUBSCR
              RETURN_CONST             0 (None)

QUESTION:

Why despite the presence of the GIL, the function "illusional_thread_safe_task"
might not behave as thread-safe when executed by multiple threads concurrently?

"""

from concurrent.futures import ThreadPoolExecutor

import pytest

from .gil_thread_safety import (
    _global_dict,
    illusional_thread_safe_task,
    indeed_thread_safe_task,
    no_thread_safe_task,
    reset_global_dict,
)


@pytest.fixture
def n():
    """Constant for testing function n times."""
    return 100


@pytest.mark.parametrize(
    "func", [indeed_thread_safe_task, illusional_thread_safe_task, no_thread_safe_task]
)
def test_thread_switching_in_shared_mutable_state_introduces_race_condition(
    n: int, func
):
    """Test thread switching in dictionary increment."""
    reset_global_dict()
    with ThreadPoolExecutor(8) as executor:
        for _ in range(n):
            executor.submit(func)

        executor.shutdown(wait=True)
    is_function_thread_safe = _global_dict[0] == n

    assert is_function_thread_safe, f"{_global_dict[0]}, {n}"
