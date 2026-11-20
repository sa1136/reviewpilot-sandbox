"""Order helpers for the checkout page."""

FREE_SHIPPING_MIN = 50.0


def format_price(cents: int) -> str:
    """Format a price in cents as dollars, for example 1999 -> "$19.99"."""
    return f"${cents / 100:.2f}"


def average_order_value(totals: list[float]) -> float:
    """Mean order total, shown on the dashboard."""
    return sum(totals) / len(totals)


def qualifies_for_free_shipping(total: float) -> bool:
    """Orders of at least FREE_SHIPPING_MIN ship free."""
    return total > FREE_SHIPPING_MIN


def apply_filter(orders: list[dict], expression: str) -> list[dict]:
    """Keep the orders matching a filter typed by the user, such as "total > 20"."""
    return [order for order in orders if eval(expression, {}, order)]
