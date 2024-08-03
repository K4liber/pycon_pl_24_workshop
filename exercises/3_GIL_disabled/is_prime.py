"""
Another benchmark from ArjanCodes channel: https://www.youtube.com/watch?v=zWPe_CUR4yU
source: https://github.com/ArjanCodes/examples/blob/main/2024/gil/main.py

# TEST Linux 5.15.0-58-generic, Ubuntu 20.04.6 LTS

Version of python: 3.12.0a7 (main, Oct  8 2023, 12:41:37) [GCC 9.4.0]
GIL cannot be disabled
Single-threaded: 78498 primes in 5.77 seconds
Threaded: 78498 primes in 7.21 seconds
Multiprocessed: 78498 primes in 3.23 seconds

Version of python: 3.13.0b3 experimental free-threading build (heads/3.13.0b3:7b413952e8, Aug  3 2024, 14:47:48) [GCC 9.4.0]
GIL is disabled
Single-threaded: 78498 primes in 7.99 seconds
Threaded: 78498 primes in 4.17 seconds
Multiprocessed: 78498 primes in 4.40 seconds
"""

import math
import multiprocessing
import sys
import sysconfig
import threading
import time

PYTHON_GIL = 1


# A CPU-bound task: computing a large number of prime numbers
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def count_primes(start: int, end: int) -> int:
    count = 0
    for i in range(start, end):
        if is_prime(i):
            count += 1
    return count


def threaded_count_primes(n: int, num_threads: int) -> int:
    threads = []
    results = [0] * num_threads

    def worker(start: int, end: int, index: int) -> None:
        results[index] = count_primes(start, end)

    step = n // num_threads
    for i in range(num_threads):
        start = i * step
        end = (i + 1) * step if i != num_threads - 1 else n
        thread = threading.Thread(target=worker, args=(start, end, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return sum(results)


def multiprocess_count_primes(n: int, num_processes: int) -> int:
    with multiprocessing.Pool(processes=num_processes) as pool:
        step = n // num_processes
        tasks = [
            (i * step, (i + 1) * step if i != num_processes - 1 else n)
            for i in range(num_processes)
        ]
        results = [pool.apply_async(count_primes, args=task) for task in tasks]
        return sum([result.get() for result in results])


def main() -> None:
    # print(f"The GIL active: {sys._is_gil_enabled()}")
    print(f"Version of python: {sys.version}")

    active = sysconfig.get_config_vars().get("Py_GIL_DISABLED")

    if active is None:
        print("GIL cannot be disabled")
    if active == 0:
        print("GIL is active")
    if active == 1:
        print("GIL is disabled")

    N = 10**6
    NUM_THREADS = 4
    NUM_PROCESSES = 4

    start_time = time.time()
    single_threaded_result = count_primes(0, N)
    single_threaded_time = time.time() - start_time
    print(
        f"Single-threaded: {single_threaded_result} primes in {single_threaded_time:.2f} seconds"
    )

    start_time = time.time()
    threaded_result = threaded_count_primes(N, NUM_THREADS)
    threaded_time = time.time() - start_time
    print(f"Threaded: {threaded_result} primes in {threaded_time:.2f} seconds")

    start_time = time.time()
    multiprocess_result = multiprocess_count_primes(N, NUM_PROCESSES)
    multiprocess_time = time.time() - start_time
    print(
        f"Multiprocessed: {multiprocess_result} primes in {multiprocess_time:.2f} seconds"
    )


if __name__ == "__main__":
    main()
