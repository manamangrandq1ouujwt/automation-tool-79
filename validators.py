import re

def validate_address(address):
    pattern = r'^[a-zA-Z0-9]{34}$'
    if not re.match(pattern, address):
        raise ValueError('Invalid address format')


def validate_amount(amount):
    if not isinstance(amount, (int, float)) or amount <= 0:
        raise ValueError('Amount must be a positive number')


def validate_input(address, amount):
    validate_address(address)
    validate_amount(amount)
