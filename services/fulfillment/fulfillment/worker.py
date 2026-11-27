import json
import logging

import boto3

from fulfillment.wms import WmsClient

log = logging.getLogger(__name__)


def handle_message(body: str, wms: WmsClient) -> None:
    event = json.loads(body)
    if event.get("type") != "order.placed":
        return
    address = event["shipping_address"]
    wms.create_shipment(
        reference=f"order-{event['order_id']}",
        recipient=address["name"],
        address_lines=[address["line1"], address.get("line2", "")],
        city=address["city"],
        postal_code=address["postal_code"],
        country=address["country"],
        items=[(line["sku"], line["quantity"]) for line in event["lines"]],
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
