import json
from unittest.mock import MagicMock

from fulfillment.worker import ShipmentRequest, handle_message

EVENT = {
    "type": "order.placed",
    "version": 1,
    "order_id": 42,
    "customer_id": 7,
    "customer_email": "ana@example.com",
    "total_cents": 4500,
    "currency": "EUR",
    "shipping": {
        "name": "Ana Ruiz",
        "line1": "Calle Mayor 1",
        "line2": "",
        "city": "Madrid",
        "postal_code": "28013",
        "country": "ES",
    },
    "lines": [{"sku": "MUG-1", "quantity": 2}],
}


def test_creates_shipment():
    wms = MagicMock()
    handle_message(json.dumps(EVENT), wms)
    wms.create_shipment.assert_called_once_with(
        reference="order-42",
        recipient="Ana Ruiz",
        address_lines=["Calle Mayor 1", ""],
        city="Madrid",
        postal_code="28013",
        country="ES",
        items=[("MUG-1", 2)],
    )


def test_ignores_other_events():
    wms = MagicMock()
    handle_message(json.dumps({"type": "order.cancelled", "order_id": 1}), wms)
    wms.create_shipment.assert_not_called()


def test_shipment_request_from_event():
    request = ShipmentRequest.from_event(EVENT)
    assert request.reference == "order-42"
    assert request.postal_code == "28013"
    assert request.items == [("MUG-1", 2)]
