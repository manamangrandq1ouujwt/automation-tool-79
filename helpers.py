import requests
import json
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def format_currency(amount, currency='USD'):
    return f'{amount:,.2f} {currency}'

def save_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def load_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def validate_address(address, regex):
    import re
    return re.match(regex, address) is not None

def get_price(symbol):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd'
    return fetch_data(url)[symbol]['usd']