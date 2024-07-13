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


def actually_thread_safe_task() -> None:
    with _lock:
        no_thread_safe_task()


if __name__ == '__main__':
    a = 1
    with ThreadPoolExecutor(8) as executor:
        for task_id in range(100):
            executor.submit(no_thread_safe_task)

        executor.shutdown(wait=True)

    print(sum(value for value in _global_dict.values()))
