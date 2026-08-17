import json
import requests

class CryptoDataHandler:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self, endpoint):
        try:
            response = requests.get(f'{self.api_url}/{endpoint}')
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {'error': str(e)}

    def save_data(self, data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_data(self, filename):
        with open(filename, 'r') as f:
            return json.load(f)

    def process_data(self, data):
        return {key: value for key, value in data.items() if value}
