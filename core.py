import json
import requests

class CryptoAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_price(self, symbol):
        response = requests.get(f'{self.base_url}/price/{symbol}')
        return self._handle_response(response)

    def get_historical_data(self, symbol, days):
        response = requests.get(f'{self.base_url}/historical/{symbol}?days={days}')
        return self._handle_response(response)

    def _handle_response(self, response):
        if response.status_code != 200:
            raise ValueError(f'Error fetching data: {response.status_code}')
        return json.loads(response.text)

api = CryptoAPI('https://api.crypto.com')

if __name__ == '__main__':
    print(api.get_price('BTC'))
    print(api.get_historical_data('BTC', 30))