"""
The exercise shows that using python 3.13 without GIL we do not lose on performance 
changing from ProcessPoolExecutor to ThreadPoolExecutor.

It also shows that python 3.13 without GIL itroduce a significant overhead due to 
making the program thread-safety. Actually, python 3.13 without GIL utilize all CPUs 
with a ThreadPoolExecutor but it is much slower than python 3.12 with GIL.
"""
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import datetime
from functools import partial
import sys
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(5)

pool_executor = ThreadPoolExecutor if len(sys.argv) > 1 and sys.argv[1] == '1' else ProcessPoolExecutor
python_version_str = f'{sys.version_info.major}.{sys.version_info.minor}'
logger.info(f'Executing with {pool_executor.__name__} using python {python_version_str}')


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

with pool_executor(8) as executor:
    for task_id in range(30):
        executor.submit(partial(fibonacci, 30))

    executor.shutdown(wait=True)

end = datetime.datetime.now()
elapsed = end - start
logger.info(f'Elapsed: {elapsed}')
