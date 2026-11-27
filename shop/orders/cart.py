from catalog.pricing import unit_price


def line_total_cents(product, quantity: int) -> int:
    return int(unit_price(product) * 100) * quantity


def cart_total_cents(lines) -> int:
    """lines: (product, quantity) pairs."""
    return sum(line_total_cents(product, quantity) for product, quantity in lines)
