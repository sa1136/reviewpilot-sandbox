import json
import logging
from dataclasses import dataclass

import boto3

from fulfillment.wms import WmsClient

log = logging.getLogger(__name__)


@dataclass(frozen=True)
class ShipmentRequest:
    reference: str
    recipient: str
    address_lines: list[str]
    city: str
    postal_code: str
    country: str
    items: list[tuple[str, int]]

    @classmethod
    def from_event(cls, event: dict) -> "ShipmentRequest":
        address = event["shipping"]
        return cls(
            reference=f"order-{event['order_id']}",
            recipient=address["name"],
            address_lines=[address["line1"], address.get("line2", "")],
            city=address["city"],
            postal_code=address["postal_code"],
            country=address["country"],
            items=[(line["sku"], line["quantity"]) for line in event["lines"]],
        )


def handle_message(body: str, wms: WmsClient) -> None:
    event = json.loads(body)
    if event.get("type") != "order.placed":
        return
    request = ShipmentRequest.from_event(event)
    log.info("creating shipment %s (%d items)", request.reference, len(request.items))
    wms.create_shipment(
        reference=request.reference,
        recipient=request.recipient,
        address_lines=request.address_lines,
        city=request.city,
        postal_code=request.postal_code,
        country=request.country,
        items=request.items,
    )


def run(queue_url: str, wms: WmsClient) -> None:
    """Poll the fulfillment queue forever. A message that fails is left on the queue; SQS
    redelivers it and moves it to the dead letter queue after 5 receives."""
    sqs = boto3.client("sqs")
    while True:
        resp = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=10, WaitTimeSeconds=20)
        for message in resp.get("Messages", []):
            try:
                handle_message(message["Body"], wms)
            except Exception:
                log.exception("failed to handle message %s", message["MessageId"])
                continue
            sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=message["ReceiptHandle"])
