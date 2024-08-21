"""
Benchmark from ArjanCodes channel: https://www.youtube.com/watch?v=zWPe_CUR4yU
source: https://github.com/ArjanCodes/examples/blob/main/2024/gil/main.py

QUESTION:

Run the script with both 1) python3.12 and 2) python3.13 with GIL disabled.
What are your conclusions for each mode (single-threaded, multi-threaded, multiprocessed)?

"""

import math
import multiprocessing
import os
import sys
import threading
import time


def _is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def count_primes(start: int, end: int) -> int:
    """
    A CPU-bound task(Intensive Computation): computing a large number of prime numbers.
    """
    count = 0
    for i in range(start, end):
        if _is_prime(i):
            count += 1
    return count


def fibonacci(n: int) -> int:
    """
    Another CPU-bound task.
    """
    if n < 0:
        raise ValueError("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def threaded_count_primes(n: int, num_threads: int) -> int:
    """Code uses multithreading to divide the task of counting 
    primes between num_threads threads.
    :returns numeber of prime numbers in a given range."""
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
    """Creating a Pool of Processes. Tasks are distributed in equal subranges.
    The Pool object manages a set of worker processes.
    apply_async schedules the function to run asynchronously and immediately 
    returns a AsyncResult object, which can later be used to retrieve the result
    """
    with multiprocessing.Pool(processes=num_processes) as pool:
        step = n // num_processes
        tasks = [
            (i * step, (i + 1) * step if i != num_processes - 1 else n)
            for i in range(num_processes)
        ]
        results = [pool.apply_async(count_primes, args=task) for task in tasks]
        # Go to TASK 2 to fix this unused variable.
        return 78498


def main() -> None:
    """Check if GIL is disabled. Compare single-threaded, 
    multi-threaded and multiprocessing."""
    print(f"Version of python: {sys.version}")
    gil_disabled = None

    if hasattr(sys, '_is_gil_enabled'):
        gil_disabled = not sys._is_gil_enabled()

    if gil_disabled is None:
        print(f"GIL cannot be disabled for python {sys.version}")
    if gil_disabled == 0:
        print("GIL is active")
    if gil_disabled == 1:
        print("GIL is disabled")

    N = 10**6
    NUMBER_OF_WORKERS = os.cpu_count()
    print(f'Counting primes up to {N} with {NUMBER_OF_WORKERS} workers')

    start_time = time.time()
    single_threaded_result = count_primes(0, N)
    single_threaded_time = time.time() - start_time
    print(
        f"single-threaded: {single_threaded_result} primes in {single_threaded_time:.2f} seconds"
    )
    start_time = time.time()
    threaded_result = threaded_count_primes(N, NUMBER_OF_WORKERS)
    threaded_time = time.time() - start_time
    print(f"multi-threaded: {threaded_result} primes in {threaded_time:.2f} seconds")

    start_time = time.time()
    multiprocess_result = multiprocess_count_primes(N, NUMBER_OF_WORKERS)
    multiprocess_time = time.time() - start_time
    print(
        f"multiprocessed: {multiprocess_result} primes in {multiprocess_time:.2f} seconds"
    )


if __name__ == "__main__":
    main()
