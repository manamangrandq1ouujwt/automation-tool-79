import requests
import time
from requests.exceptions import RequestException

def retry_request(url, max_retries=3, backoff_factor=0.5):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except RequestException:
            retries += 1
            time.sleep(backoff_factor * (2 ** retries))
    raise Exception('Max retries exceeded')

# Example usage
if __name__ == '__main__':
    try:
        response = retry_request('https://api.example.com/data')
        print(response.json())
    except Exception as e:
        print(f'Failed to fetch data: {e}')