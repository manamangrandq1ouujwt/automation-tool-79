import json

class CryptoDataHandler:
    def __init__(self, data):
        self.data = data

    def filter_by_currency(self, currency):
        return [item for item in self.data if item['currency'] == currency]

    def average_prices(self):
        prices = [item['price'] for item in self.data]
        return sum(prices) / len(prices) if prices else 0

    def to_json(self):
        return json.dumps(self.data)

    def from_json(self, json_data):
        self.data = json.loads(json_data)  
        return self.data

    def get_highest_price(self):
        return max(self.data, key=lambda x: x['price'], default=None)