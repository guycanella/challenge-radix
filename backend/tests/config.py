import sys

args = sys.argv

default_concurrency = 500
default_time = 1

config = {
    'method': 'GET',
    'url': 'http://127.0.0.1:8000/data-sensor',
    'headers': {
        'content-type': 'application/json'
    }
}

def generate_config():
    concurrency = int(args[1])
    time = int(args[2])

    return {
        'request': config,
        'concurrency': concurrency,
        'time': time
    }