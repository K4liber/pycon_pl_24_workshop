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
import pytest
from concurrent.futures import ThreadPoolExecutor
from gil_thread_safety import _global_dict
from gil_thread_safety import no_thread_safe_task

@pytest.fixture
def n():
    """Constant for testing function n times."""
    return 100


def test_thread_switching_in_shared_mutable_state_introduces_race_condition(n: int):
    """ Test thread switching in dictionary increment."""
    with ThreadPoolExecutor(8) as executor:
        for _ in range(n):
            executor.submit(no_thread_safe_task)

        executor.shutdown(wait=True)
    is_function_thread_safe = _global_dict[0] == n
    assert not is_function_thread_safe
