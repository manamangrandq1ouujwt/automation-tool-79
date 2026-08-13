import json
from validators import validate_input

def process_transactions(transactions):
    for transaction in transactions:
        if not validate_input(transaction):
            print(f'Invalid transaction: {transaction}')
            continue
        # Process valid transaction
        print(f'Processing transaction: {transaction}')

def main():
    sample_transactions = [
        {'amount': 0.1, 'currency': 'BTC'},
        {'amount': -0.5, 'currency': 'ETH'},
        {'amount': 0.25, 'currency': 'LTC'},
    ]
    process_transactions(sample_transactions)

if __name__ == '__main__':
    main()