from catalog.pricing import on_sale, unit_price


def _dollars(cents: int) -> str:
    return f"{cents // 100}.{cents % 100:02d}"


def product_json(product) -> dict:
    return {
        "sku": product.sku,
        "name": product.name,
        "price": _dollars(unit_price(product)),
        "price_cents": unit_price(product),
        "list_price": str(product.price),
        "on_sale": on_sale(product),
    }
