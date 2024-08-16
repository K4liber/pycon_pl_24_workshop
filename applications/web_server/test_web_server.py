import concurrent.futures
import datetime
import logging
import requests

url = "http://127.0.0.1:8000/fibonacci"
number_of_tasks = 40
clients = 8
logging.basicConfig(
    format='%(levelname)s: %(message)s',
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def make_request(request_id: int) -> str:
    print(f'Sending request (id={request_id}) to {url}')
    try:
        start_time = datetime.datetime.now()
        response = requests.get(url)
        response_text = response.text
        elapsed = datetime.datetime.now() - start_time
        logger.info(f'Get response = {response_text}, elapsed = {elapsed.total_seconds():.2f}s.')
        return response_text
    except Exception as e:
        return str(e)


def execute_requests_concurrently(
        max_workers: int,
        number_of_requests: int = number_of_tasks
    ) -> list[str]:
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_payload = [executor.submit(make_request, request_id) for request_id in range(number_of_requests)]
        for future in concurrent.futures.as_completed(future_to_payload):
            try:
                result = future.result()
                results.append(result)
            except Exception as exc:
                results.append(str(exc))
    return results


requests.get(f"{url}/1")

start_time = datetime.datetime.now()
results = execute_requests_concurrently(max_workers=clients)
elapsed = datetime.datetime.now() - start_time
logger.info(f'{number_of_tasks} tasks executed in {elapsed.total_seconds():.2f}s')
