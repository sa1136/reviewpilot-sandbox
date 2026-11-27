from app.events import publish_order_placed
from app.models import Order
from app.repository import OrderRepository


def place_order(repo: OrderRepository, order: Order) -> Order:
    """Save the order, then tell fulfillment and notifications about it."""
    saved = repo.insert(order)
    publish_order_placed(saved)
    return saved
