import concurrent.futures
from dataclasses import dataclass
import datetime
import json
import logging
import requests
import urllib.parse


server_url = 'http://127.0.0.1:8000'
url = urllib.parse.urljoin(server_url, 'fibonacci')
number_of_tasks = 40
clients = 20
logging.basicConfig(
    format='%(levelname)s: %(message)s',
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@dataclass(frozen=True)
class Response:
    msg: str
    memory_usage: float = 0
    pid: int = 0

    def __str__(self) -> str:
        return f'Message = {self.msg}. Memory usage = {self.memory_usage}. PID = {self.pid}'


def make_request(request_id: int) -> str:
    print(f'Sending request (id={request_id}) to {url}')
    try:
        response = requests.get(url)
        response = Response(**json.loads(response.text))
        logger.info(str(response))
        return response
    except Exception as e:
        return Response(msg=str(e))


def execute_requests_concurrently(
        max_workers: int,
        number_of_requests: int = number_of_tasks
    ) -> list[Response]:
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_payload = [executor.submit(make_request, request_id) for request_id in range(number_of_requests)]
        for future in concurrent.futures.as_completed(future_to_payload):
            try:
                result = future.result()
                results.append(result)
            except Exception as exc:
                results.append(Response(msg=str(exc)))
    return results


response = requests.get(urllib.parse.urljoin(server_url, 'sys_info'))
server_info = response.text
logger.info(f"Testing server: {server_info}")
start_time = datetime.datetime.now()
results = execute_requests_concurrently(max_workers=clients)
elapsed = datetime.datetime.now() - start_time
logger.info(f'{number_of_tasks} tasks executed in {elapsed.total_seconds():.2f}s')
pid_to_memory_usage = {result.pid: result.memory_usage for result in results}
logger.info(f'Memory usage per PID: {pid_to_memory_usage}')
logger.info(f'Overall memory usage: {sum(pid_to_memory_usage.values())} [MB]')
