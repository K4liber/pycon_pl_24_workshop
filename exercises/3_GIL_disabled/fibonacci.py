"""
The exercise shows that using python 3.13 without GIL we do not lose on performance 
changing from ProcessPoolExecutor to ThreadPoolExecutor.

It also shows that python 3.13 without GIL introduce an overhead due to 
making the program thread-safety. Indeed, python 3.13 without GIL utilize all CPUs 
with a ThreadPoolExecutor but it is slower than python 3.12 with GIL. 
Based on the CPU utilization and the elapsed time we can conclude that 
with python 3.13 we do more clock cycles comparing to the 3.12.

# TEST Linux 5.15.0-58-generic, Ubuntu 20.04.6 LTS

INFO: Python 3.12.0a7 (main, Oct  8 2023, 12:41:37) [GCC 9.4.0]
INFO: Executor = ThreadPoolExecutor, cpus (workers) = 2
INFO: Elapsed: 10.55 seconds

INFO: Python 3.12.0a7 (main, Oct  8 2023, 12:41:37) [GCC 9.4.0]
INFO: Executor = ProcessPoolExecutor, cpus (workers) = 2
INFO: Elapsed: 4.17 seconds

INFO: Python 3.13.0b3 experimental free-threading build (heads/3.13.0b3:7b413952e8, Aug  3 2024, 14:47:48) [GCC 9.4.0]
INFO: Executor = ThreadPoolExecutor, cpus (workers) = 2
INFO: Elapsed: 7.06 seconds

INFO: Python 3.13.0b3 experimental free-threading build (heads/3.13.0b3:7b413952e8, Aug  3 2024, 14:47:48) [GCC 9.4.0]
INFO: Executor = ProcessPoolExecutor, cpus (workers) = 2
INFO: Elapsed: 7.27 seconds

"""
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import datetime
from functools import partial
import sys
import logging
import multiprocessing

logging.basicConfig(
    format='%(levelname)s: %(message)s',
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
cpus = multiprocessing.cpu_count()
pool_executor = ProcessPoolExecutor if len(sys.argv) > 1 and sys.argv[1] == '1' else ThreadPoolExecutor
logger.info(f"Python {sys.version}")
logger.info(f'Executor = {pool_executor.__name__}, cpus (workers) = {cpus}')


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

start = datetime.datetime.now()

with pool_executor(cpus) as executor:
    for task_id in range(30):
        executor.submit(partial(fibonacci, 30))

    executor.shutdown(wait=True)

end = datetime.datetime.now()
elapsed = end - start
logger.info(f'Elapsed: {elapsed.total_seconds():.2f} seconds')
