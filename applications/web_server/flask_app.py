import datetime
import logging
import os
import sys
import threading
from flask import Flask

app = Flask(__name__)
logging.basicConfig(
    format='%(levelname)s: %(message)s',
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


@app.route("/sys_info")
def sys_info() -> str:
    gil_disabled = False

    if hasattr(sys, "_is_gil_enabled"):
        gil_disabled = bool(not sys._is_gil_enabled())

    gil_info = f'(GIL ' + ('disabled)' if gil_disabled else 'enabled)')
    return f'{gil_info} {sys.version})'


@app.route("/fibonacci")
@app.route("/fibonacci/<n>")
def get_fibonacci(n: int | str = 34) -> str:
    n = int(n)
    thread_id = threading.get_native_id()
    process_id = os.getpid()
    start_time = datetime.datetime.now()
    result = str(fibonacci(n=n))
    elapsed = datetime.datetime.now() - start_time
    msg = f'[PID={process_id}, TID={thread_id}] Fibonacci result = {result} (n={n}), elapsed = {elapsed.total_seconds():.2f}s'
    logger.info(msg)
    return msg
