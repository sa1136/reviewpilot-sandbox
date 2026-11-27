from catalog.pricing import on_sale, unit_price, unit_price_cents


def product_json(product) -> dict:
    return {
        "sku": product.sku,
        "name": product.name,
        "price": str(unit_price(product)),
        "price_cents": unit_price_cents(product),
        "list_price": str(product.price),
        "on_sale": on_sale(product),
    }
