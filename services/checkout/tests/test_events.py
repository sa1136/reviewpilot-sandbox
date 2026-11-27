from app.events import order_placed_payload
from app.models import Address, Line, Order


def make_order():
    return Order(
        id=42,
        customer_id=7,
        customer_email="ana@example.com",
        currency="EUR",
        shipping_address=Address("Ana Ruiz", "Calle Mayor 1", "Madrid", "28013", "ES"),
        lines=[Line("MUG-1", 2, 1250), Line("TEE-3", 1, 2000)],
    )


def test_order_placed_payload():
    payload = order_placed_payload(make_order())
    assert payload["type"] == "order.placed"
    assert payload["order_id"] == 42
    assert payload["email"] == "ana@example.com"
    assert payload["customer_email"] == "ana@example.com"
    assert payload["total_cents"] == 4500
    assert payload["shipping_address"]["postal_code"] == "28013"
    assert payload["lines"] == [{"sku": "MUG-1", "quantity": 2}, {"sku": "TEE-3", "quantity": 1}]
