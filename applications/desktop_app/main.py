"""
Enforce to run without GIL:

python -Xgil=0 applications/desktop_app/main.py
"""
import time
from typing import Any
import config

from runner.factory import RUNNER_TYPE, get_runner

from job.callables import get_callable, CALLABLES

runner_type = RUNNER_TYPE.THREAD
runner = get_runner(runner_type=runner_type)
function_args = [34]
selected_function = get_callable(
    CALLABLES.FIBONACCI,
    wrap=True,
    args=function_args
)


def _callback(
        worker_id: int | None = None,
        result: Any = None
    ) -> None:
    if worker_id is None:
        print(f'Execution started with runner {runner_type}')
    else:
        print(f'Worker id: {worker_id}, result: {result}')


print(config.sys_info())
start = time.time()
runner.start(
    callables_list=[
        selected_function
        for _ in range(config.NUMBER_OF_JOBS)
    ],
    callback=_callback
)
end = time.time()
print(f'{config.NUMBER_OF_JOBS} tasks executed in {end - start} [s]')
