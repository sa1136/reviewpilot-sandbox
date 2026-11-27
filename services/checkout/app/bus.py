import json
import os

import boto3

_sns = boto3.client("sns")

TOPICS = {
    "orders": os.environ.get("ORDERS_TOPIC_ARN", ""),
}


def publish(topic: str, payload: dict) -> None:
    """Publish one JSON event. Subscribers get the raw JSON body (raw message delivery)."""
    _sns.publish(
        TopicArn=TOPICS[topic],
        Message=json.dumps(payload),
        MessageAttributes={"type": {"DataType": "String", "StringValue": payload["type"]}},
    )
