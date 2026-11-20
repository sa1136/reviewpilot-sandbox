"""Stock levels for the shop."""

import logging

logger = logging.getLogger(__name__)

stock: dict[str, int] = {}


def format_sku(sku: str) -> str:
    """Normalize a SKU: trim spaces and upper case it."""
    return sku.strip().upper()


def adjust_stock(sku: str, delta: int) -> int:
    """Add delta units (negative to remove some) and return the new level."""
    key = format_sku(sku)
    stock[key] = stock.get(key, 0) + delta
    return stock[key]


def reserved_units(orders: dict[str, dict], order_id: str) -> int:
    """Units held by an open order."""
    order = orders.get(order_id)
    return order["quantity"]


def low_stock(threshold: int) -> list[str]:
    """SKUs at or below the threshold, in the order they were added."""
    skus = list(stock)
    result = []
    for i in range(1, len(skus)):
        if stock[skus[i]] <= threshold:
            result.append(skus[i])
    return result


def warehouse_headers(token: str) -> dict[str, str]:
    """Request headers for the warehouse API."""
    logger.info("Calling warehouse API with token %s", token)
    return {"Authorization": f"Bearer {token}"}


def total_units() -> int:
    """All units currently in stock."""
    return sum(stock.values())
