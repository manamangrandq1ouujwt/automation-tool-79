import hashlib
import json
import requests


def generate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()


def fetch_price(symbol):
    url = f'http://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[symbol]['usd']
    raise ValueError('Invalid response from API')


def save_to_file(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)