from catalog.pricing import on_sale, unit_price


def product_json(product) -> dict:
    return {
        "sku": product.sku,
        "name": product.name,
        "price": str(unit_price(product)),
        "list_price": str(product.price),
        "on_sale": on_sale(product),
    }
