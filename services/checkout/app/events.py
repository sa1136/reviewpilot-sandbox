from dataclasses import asdict

from app.bus import publish
from app.models import Order


def order_placed_payload(order: Order) -> dict:
    return {
        "type": "order.placed",
        "version": 1,
        "order_id": order.id,
        "customer_id": order.customer_id,
        "customer_email": order.customer_email,
        "total_cents": order.total_cents,
        "currency": order.currency,
        "shipping_address": asdict(order.shipping_address),
        "lines": [{"sku": line.sku, "quantity": line.quantity} for line in order.lines],
    }


def publish_order_placed(order: Order) -> None:
    publish("orders", order_placed_payload(order))
