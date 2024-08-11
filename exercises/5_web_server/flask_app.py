import datetime
import logging
import os
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


@app.route("/fibonacci")
def get_fibonacci(n: int = 34) -> str:
    thread_id = threading.get_native_id()
    process_id = os.getpid()
    start_time = datetime.datetime.now()
    result = str(fibonacci(n=n))
    elapsed = datetime.datetime.now() - start_time
    msg = f'[PID={process_id}, TID={thread_id}] Fibonacci result = {result} (n={n}), elapsed = {elapsed.total_seconds():.2f}s'
    logger.info(msg)
    return msg
