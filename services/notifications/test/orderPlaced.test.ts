import { describe, expect, it, vi } from "vitest";

import { handleOrderPlaced } from "../src/handlers/orderPlaced";

describe("handleOrderPlaced", () => {
  it("prefers the email field", async () => {
    const mailer = { send: vi.fn().mockResolvedValue(undefined) };
    await handleOrderPlaced(
      {
        type: "order.placed",
        version: 1,
        order_id: 42,
        customer_id: 7,
        email: "new@example.com",
        customer_email: "ana@example.com",
        total_cents: 4500,
        currency: "EUR",
        lines: [{ sku: "MUG-1", quantity: 2 }],
      },
      mailer,
    );
    expect(mailer.send.mock.calls[0][0].to).toBe("new@example.com");
  });

  it("sends the receipt to the customer", async () => {
    const mailer = { send: vi.fn().mockResolvedValue(undefined) };
    await handleOrderPlaced(
      {
        type: "order.placed",
        version: 1,
        order_id: 42,
        customer_id: 7,
        customer_email: "ana@example.com",
        total_cents: 4500,
        currency: "EUR",
        lines: [{ sku: "MUG-1", quantity: 2 }],
      },
      mailer,
    );
    expect(mailer.send).toHaveBeenCalledWith({
      to: "ana@example.com",
      template: "order-receipt",
      data: { orderId: 42, total: "€45.00", itemCount: 2 },
    });
  });
});
