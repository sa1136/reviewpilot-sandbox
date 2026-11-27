import {
  DeleteMessageCommand,
  ReceiveMessageCommand,
  SQSClient,
} from "@aws-sdk/client-sqs";

import type { BusEvent, OrderPlacedEvent } from "./events";
import { handleOrderPlaced } from "./handlers/orderPlaced";
import type { Mailer } from "./mailer";

export async function dispatch(event: BusEvent, mailer: Mailer): Promise<void> {
  switch (event.type) {
    case "order.placed":
      return handleOrderPlaced(event as OrderPlacedEvent, mailer);
    default:
      return;
  }
}

export async function poll(queueUrl: string, mailer: Mailer, sqs = new SQSClient({})): Promise<never> {
  for (;;) {
    const resp = await sqs.send(
      new ReceiveMessageCommand({ QueueUrl: queueUrl, MaxNumberOfMessages: 10, WaitTimeSeconds: 20 }),
    );
    for (const message of resp.Messages ?? []) {
      try {
        await dispatch(JSON.parse(message.Body ?? "{}") as BusEvent, mailer);
      } catch (err) {
        console.error("notification failed", message.MessageId, err);
        continue; // redelivered by SQS, dead letter queue after 5 receives
      }
      await sqs.send(new DeleteMessageCommand({ QueueUrl: queueUrl, ReceiptHandle: message.ReceiptHandle }));
    }
  }
}
