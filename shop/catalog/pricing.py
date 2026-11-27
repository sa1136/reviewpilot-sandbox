def unit_price(product) -> int:
    """Current selling price in cents: the sale price when it is lower than the list price."""
    price = product.price
    if product.sale_price is not None and product.sale_price < product.price:
        price = product.sale_price
    return int(price * 100)


def on_sale(product) -> bool:
    return unit_price(product) < int(product.price * 100)
