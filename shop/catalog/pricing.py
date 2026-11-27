from decimal import Decimal


def unit_price(product) -> Decimal:
    """Current selling price in dollars: the sale price when it is lower than the list price."""
    if product.sale_price is not None and product.sale_price < product.price:
        return product.sale_price
    return product.price


def unit_price_cents(product) -> int:
    """unit_price in cents, for clients that do integer money math."""
    return int(unit_price(product) * 100)


def on_sale(product) -> bool:
    return unit_price(product) < product.price
