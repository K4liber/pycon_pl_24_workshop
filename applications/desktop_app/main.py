"""
Enforce to run without GIL:

python -Xgil=0 applications/desktop_app/main.py
"""
import logging
import time
import config

from runner.factory import RUNNER_TYPE, get_runner

from job.callables import CallableReturn, get_callable, CALLABLES


logging.basicConfig(
    format='%(levelname)s: %(message)s',
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
runner_type = RUNNER_TYPE.THREAD
runner = get_runner(runner_type=runner_type)
function_args = [34]
selected_function = get_callable(
    CALLABLES.FIBONACCI,
    args=function_args,
    use_psutil=runner_type != RUNNER_TYPE.SUBINTERPRETER  # module psutil._psutil_linux does not support loading in subinterpreters 
)
_callable_returns: list[CallableReturn] = []


def _callback(
        callable_return: CallableReturn | None = None
    ) -> None:
    if callable_return is None:
        logger.info(f'Execution started with runner {runner_type}')
    else:
        logger.info(f'Thread id: {callable_return.thread_id}, result: {callable_return.result}')
        _callable_returns.append(callable_return)


logger.info(config.sys_info())
start = time.time()
runner.start(
    callables_list=[
        selected_function
        for _ in range(config.NUMBER_OF_JOBS)
    ],
    callback=_callback
)
end = time.time()
logger.info('-' * 10 + 'SUMMARY' + '-' * 10)
logger.info(f'{config.NUMBER_OF_JOBS} tasks executed in {end - start} [s]')
pid_to_memory_usage = {}

for callable_return in _callable_returns:
    pid_to_memory_usage.update(callable_return.pid_to_memory_usage)

logger.info(f'Memory usage per PID: {pid_to_memory_usage}')
logger.info(f'Overall memory usage: {sum(pid_to_memory_usage.values())} [MB]')
