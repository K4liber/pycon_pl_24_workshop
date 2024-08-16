"""
Testing on CPython3.13b1+

Requires some recent patches from main.
pip install hypercorn

Have successfully run the following apps:
- fastapi==0.99.0
- Flask
"""

from time import sleep, time
import _interpreters as interpreters
import _interpchannels as channels
import threading
from hypercorn.config import Config, Sockets
from socket import dup
import logging
import os

logging.basicConfig(
    format='%(levelname)s: %(message)s',
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

WORKERS = os.cpu_count() or 2

"""
    This function is started inside the subinterpreter.

    Shared globals:
    - worker_number: int
    - workers: int
    - channel_id: int
    - insecure_sockets: tuple of tuples
    - application_path: str
    - log_level: int
"""

worker_init = open('interpreter_worker.py', 'r').read()


class SubinterpreterWorker(threading.Thread):

    def __init__(
        self,
        number: int,
        config: Config,
        sockets: Sockets,
        log_level: int = logging.INFO,
    ):
        self.worker_number = number
        self.interp = interpreters.create()
        self.channel = channels.create()
        self.config = config
        self.sockets = sockets
        self.log_level = log_level
        super().__init__(target=self.run, daemon=True)

    def run(self):
        # Convert insecure sockets to a tuple of tuples because the Sockets type cannot be shared
        insecure_sockets = [(int(s.family), int(s.type), s.proto, dup(s.fileno())) for s in self.sockets.insecure_sockets]
        logger.debug("Starting worker {}, interpreter {}".format(self.worker_number, self.interp))
        interpreters.run_string(
            self.interp,
            worker_init,
            shared={
                "worker_number": self.worker_number,
                "insecure_sockets": tuple(insecure_sockets),
                "application_path": self.config.application_path,
                "workers": self.config.workers,
                "channel_id": self.channel,
                "log_level": self.log_level,
            },
        )
        logger.info("Worker {}, interpreter {} finished".format(self.worker_number, self.interp))

    def is_alive(self) -> bool:
        return interpreters.is_running(self.interp) and super().is_alive()

    def request_stop(self):
        logger.info("Sending stop signal to worker {}, interpreter {}".format(self.worker_number, self.interp))
        channels.send(self.channel, "stop", blocking=False)

    def stop(self, timeout: float = 5.0):
        if self.is_alive():
            # wait to stop
            start = time()
            while self.is_alive():
                if time() - start > timeout:
                    logger.warning("Worker {}, interpreter {} did not stop in time".format(self.worker_number, self.interp))
                    break
                sleep(0.1)
        else:
            logger.debug("Worker {}, interpreter {} already stopped".format(self.worker_number, self.interp))

    def destroy(self):
        if interpreters.is_running(self.interp):
            raise ValueError("Cannot destroy a running interpreter")
        interpreters.destroy(self.interp)


def fill_pool(
        threads,
        config,
        workers: int,
        sockets
    ) -> None:
    for i in range(workers):
        t = SubinterpreterWorker(
            i, config, sockets, log_level=logger.level
        )
        t.start()
        threads.append(t)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "application",
        help="The application to dispatch to as path.to.module:instance.path",
    )
    parser.add_argument(
        "-w",
        "--workers",
        dest="workers",
        help="The number of workers to spawn and use, defaults to the number of CPUs",
        default=WORKERS,
        type=int,
    )
    args = parser.parse_args()
    config = Config()
    config.application_path = args.application
    config.workers = args.workers
    sockets = config.create_sockets()
    logger.info(f'Starting {args.workers} subinterpreter workers')
    threads: list[threading.Thread] = []
    fill_pool(
        threads=threads,
        config=config,
        workers=args.workers,
        sockets=sockets
    )

    try:
        for t in threads:
            t.join()
    except KeyboardInterrupt:
        logger.debug("Received keyboard interrupt, shutting down workers")
        for t in threads:
            t.request_stop()
        for t in threads:
            t.stop()
