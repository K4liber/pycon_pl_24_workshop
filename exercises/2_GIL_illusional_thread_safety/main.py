"""
"Before any opcode is executed in the frame-evaluation
loop, the GIL is acquired by the thread. Once the opcode has been executed, the
GIL is released"

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
    a = 1
    with ThreadPoolExecutor(8) as executor:
        for task_id in range(100):
            executor.submit(no_thread_safe_task)

        executor.shutdown(wait=True)

    print(sum(value for value in _global_dict.values()))
