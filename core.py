import requests
import json

def fetch_balance(api_key: str, wallet_address: str) -> dict:
    url = f'https://api.crypto.com/v1/balance/{wallet_address}'
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else {'error': 'Unable to fetch balance'}


def send_transaction(api_key: str, transaction_data: dict) -> dict:
    url = 'https://api.crypto.com/v1/send_token'
    headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(transaction_data))
    return response.json() if response.status_code == 200 else {'error': 'Transaction failed'}


def get_transaction_status(api_key: str, transaction_id: str) -> dict:
    url = f'https://api.crypto.com/v1/transaction/{transaction_id}'
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else {'error': 'Status fetch failed'}

