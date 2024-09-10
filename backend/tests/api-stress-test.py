import requests
from config import generate_config
import threading
import time as Time
import uuid

request = generate_config()['request']
concurrency = generate_config()['concurrency']
time = generate_config()['time']

method = request['method']
url = request['url']
headers = request['headers']

timer = []
total = []
request_ids = []
time_metrics = []

def timer_init():
    timer.append(1)
    counter = time
    while counter > 0:
        Time.sleep(1)
        counter -= 1
    timer.clear()

def create_thread():
    while (len(timer) > 0):
        stress_test()

def check_response(status_code: int):
    response_status = status_code

    if response_status >= 200 and response_status < 300:
        total.append('Success')
    else:
        total.append('Fail')

def calculate_metrics():
    while (len(timer) > 0 or len(request_ids) > 0):
        pass

    total_requests = len(total)
    success_number = len(list(filter(lambda x: x == 'Success', total)))
    fail_number = len(list(filter(lambda x: x == 'Fail', total)))
    success_percentage = round((success_number / total_requests) * 100, 2)
    avg_time = round(sum(time_metrics) / len(time_metrics), 2)

    show_metrics(total_requests, success_number, fail_number, success_percentage, time_metrics, avg_time)

def show_metrics(total_requests, success_number, fail_number, success_percentage, time_metrics, avg_time):
    print(f'Total number of requests: {total_requests}')
    print(f'Success percentage: {success_percentage}%')
    print(f'Number of success: {success_number}')
    print(f'Number of failures: {fail_number}')
    print(f'Fastest request: {min(time_metrics)}s')
    print(f'Slowest request: {max(time_metrics)}s')
    print(f'Average time: {avg_time}s')

def stress_test():
    request_id = str(uuid.uuid4())
    request_ids.append(request_id)

    init_time = Time.process_time()
    status_code = 0

    try:
        response = requests.request(
            method = method,
            url = url,
            headers = headers
        )

        status_code = response.status_code
    except:
        status_code = 500

    total_time = round(Time.process_time() - init_time, 2)
    time_metrics.append(total_time)

    check_response(status_code)

    request_ids.remove(request_id)

if __name__ == "__main__":
    print(f'Initiating Stress Test for {concurrency} threads in {time} seconds')
    print(" ")

    threading.Thread(target = timer_init).start()
    threading.Thread(target = calculate_metrics).start()

    for thread in range(concurrency):
        threading.Thread(target = create_thread).start()