from dataclasses import dataclass

import config
from runner.interface import RunnerInterface
from runner.processes import RunnerProcesses
from runner.threads import RunnerThreads
from runner.subinterpreters import RunnerSubinterpreters


@dataclass(frozen=True)
class _RunnerType:
    THREAD = 'THREAD'
    PROCESS = 'PROCESS'
    SUBINTERPRETER = 'SUBINTERPRETER'


RUNNER_TYPE = _RunnerType()
_runner_type_to_class = {
    RUNNER_TYPE.THREAD: RunnerThreads,
    RUNNER_TYPE.PROCESS: RunnerProcesses,
    RUNNER_TYPE.SUBINTERPRETER: RunnerSubinterpreters
}

def get_runner(
        runner_type: str
    ) -> RunnerInterface:
    runner_class = _runner_type_to_class.get(runner_type)
    return runner_class(
        no_workers=config.NUMBER_OF_WORKERS,
        runner_type=runner_type
    )
