from concurrent.futures import Future, ThreadPoolExecutor
from functools import partial
from typing import Any, Callable

from job.callables import CALLBACK_TYPE
from runner.interface import RunnerInterface


def thread_callback(
        callback: CALLBACK_TYPE,
        future: Future,
    ) -> None:
    if future.exception():
        print(f'Exception: {future.exception()}')

    callback(future.result())


class RunnerThreads(RunnerInterface):

    def start(
        self,
        callables_list: list[Callable[[], Any]],
        callback: CALLBACK_TYPE
    ) -> None:

        with ThreadPoolExecutor(self._no_workers) as executor:
            for callable in callables_list:
                task = executor.submit(callable)
                task.add_done_callback(
                    partial(
                        thread_callback, callback
                    )
                )

            callback()
