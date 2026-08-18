import json
import requests

class CryptoDataProcessor:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self, symbol):
        response = requests.get(f'{self.api_url}/{symbol}')
        response.raise_for_status()
        return response.json()

    def transform_data(self, data):
        return {
            'symbol': data['symbol'],
            'price': float(data['price']),
            'volume': float(data['volume']),
            'timestamp': data['timestamp']
        }

    def process_data(self, symbol):
        raw_data = self.fetch_data(symbol)
        return self.transform_data(raw_data)

if __name__ == '__main__':
    processor = CryptoDataProcessor('https://api.crypto.com/data')
    processed_data = processor.process_data('BTC')
    print(json.dumps(processed_data, indent=4))