import type { OrderPlacedEvent } from "../events";
import type { Mailer } from "../mailer";
import { formatMoney } from "../money";

export async function handleOrderPlaced(event: OrderPlacedEvent, mailer: Mailer): Promise<void> {
  await mailer.send({
    to: event.customer_email,
    template: "order-receipt",
    data: {
      orderId: event.order_id,
      total: formatMoney(event.total_cents, event.currency),
      itemCount: event.lines.reduce((n, line) => n + line.quantity, 0),
    },
  });
}
