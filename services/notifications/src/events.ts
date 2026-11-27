export interface OrderPlacedEvent {
  type: "order.placed";
  version: number;
  order_id: number;
  customer_id: number;
  customer_email: string;
  total_cents: number;
  currency: string;
  lines: { sku: string; quantity: number }[];
}

export type BusEvent = OrderPlacedEvent | { type: string };
