from decimal import Decimal
from typing import Dict, Any


def convert_to_decimal(value: float) -> Decimal:
    """
    Convert a float to Decimal.
    
    Args:
        value (float): The float value to convert.
    
    Returns:
        Decimal: The converted Decimal value.
    """
    return Decimal(value)


def calculate_market_cap(supply: float, price: float) -> Decimal:
    """
    Calculate the market capitalization.
    
    Args:
        supply (float): Total supply of the asset.
        price (float): Current price of the asset.
    
    Returns:
        Decimal: Market capitalization of the asset.
    """
    return convert_to_decimal(supply) * convert_to_decimal(price)


def get_asset_info(asset_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extract relevant information from asset data.
    
    Args:
        asset_data (Dict[str, Any]): A dictionary containing asset data.
    
    Returns:
        Dict[str, Any]: A dictionary with the asset's name, market cap, and price.
    """
    name = asset_data.get('name', '')
    price = asset_data.get('current_price', 0.0)
    supply = asset_data.get('total_supply', 0.0)
    market_cap = calculate_market_cap(supply, price)
    return {'name': name, 'market_cap': market_cap, 'price': convert_to_decimal(price)}
