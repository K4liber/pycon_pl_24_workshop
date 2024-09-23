import os
from concurrent.futures import ThreadPoolExecutor
import pickle
from textwrap import dedent
from typing import Any, Callable

import _interpreters as interpreters

from job.callables import CALLBACK_TYPE
from runner.interface import RunnerInterface


def _run(
        callback: CALLBACK_TYPE,
        subinterpreter_id: int,
        callable: Callable[[], Any]
    ) -> None:
    try:
        result_read_pipe, result_write_pipe = os.pipe()
        callable_read_pipe, callable_write_pipe = os.pipe()

        with open(callable_write_pipe, 'wb') as w_pipe:
            pickle.dump(callable, w_pipe)

        interpreters.run_string(
            subinterpreter_id,
            dedent(f"""
                import os
                import sys
                sys.path.append(os.getcwd())

                import pickle

                with open({callable_read_pipe}, 'rb') as r_pipe:
                    callable = pickle.load(r_pipe)
                
                result = callable()

                with open({result_write_pipe}, 'wb') as w_pipe:
                   pickle.dump(result, w_pipe)

                """
            )
        )

        with open(result_read_pipe, 'rb') as r_pipe:
            result = pickle.load(r_pipe)
    except Exception as exc:
        callback(str(exc))

    callback(result)


class RunnerSubinterpreters(RunnerInterface):

    def start(
        self,
        callables_list: list[Callable[[], Any]],
        callback: CALLBACK_TYPE
    ) -> None:
        callables_length = len(callables_list)
        subinterpreter_ids = [
            interpreters.create()
            for _ in range(callables_length)
        ]

        with ThreadPoolExecutor(self._no_workers) as executor:
            for _callable_index in range(callables_length):
                _subinterpreter_id = subinterpreter_ids[_callable_index]
                callable = callables_list[_callable_index]
                executor.submit(_run, callback, _subinterpreter_id, callable)

            callback()
