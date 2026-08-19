import requests
import json

def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def load_config(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def save_config(file_path, config):
    with open(file_path, 'w') as f:
        json.dump(config, f, indent=4)


def format_address(address):
    return address.lower() if isinstance(address, str) else ''


def is_valid_address(address):
    return isinstance(address, str) and len(address) in [34, 42]  # Common lengths for crypto addresses
