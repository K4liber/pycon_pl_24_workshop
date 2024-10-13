from concurrent.futures import Future, ProcessPoolExecutor
from functools import partial
from typing import Callable

from job.callables import CALLBACK_TYPE
from job.callable_return import CallableReturn
from runner.interface import RunnerInterface


def _callback(
        callback: CALLBACK_TYPE,
        future: Future,
    ) -> None:
    if future.exception():
        print(f'Exception: {future.exception()}')

    callable_result = future.result()
    callback(callable_result)


class RunnerProcesses(RunnerInterface):

    def start(
        self,
        callables_list: list[Callable[[], CallableReturn]],
        callback: CALLBACK_TYPE
    ) -> None:
        mp_context = None  # get_context('spawn')  # Force the same context on both Unix and Windows

        with ProcessPoolExecutor(self._no_workers, mp_context=mp_context) as executor:
            for callable in callables_list:
                task = executor.submit(callable)
                task.add_done_callback(
                    partial(
                        _callback, callback
                    )
                )
        
            callback()
