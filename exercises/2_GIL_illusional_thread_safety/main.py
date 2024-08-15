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
from threading import Lock
import time


_global_dict: dict[int, int] = {
    0: 0
}
_lock = Lock()


def illusional_thread_safe_task() -> None:
    _global_dict[0] += 1


def no_thread_safe_task() -> None:
    actual_value = _global_dict[0]
    time.sleep(0.001)  # Thread Switching
    _global_dict[0] = actual_value + 1


def indeed_thread_safe_task() -> None:
    with _lock:
        no_thread_safe_task()


if __name__ == '__main__':
    n = 100
    function_to_check = no_thread_safe_task

    with ThreadPoolExecutor(8) as executor:
        for task_id in range(n):
            executor.submit(function_to_check)

        executor.shutdown(wait=True)

    actual_n = _global_dict[0]
    print(f'expected = {n}, actual = {actual_n}')
    assert actual_n == n, f'Your function {function_to_check} is not thread-safe!'
    print(f'Seems like function {function_to_check} is thread-safe.')
