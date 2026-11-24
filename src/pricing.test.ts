import { describe, expect, it } from "vitest";
import { applyCoupon, formatPrice, renderPriceBadge, subtotalCents } from "./pricing";

describe("pricing", () => {
  it("adds up a single item", () => {
    expect(subtotalCents([{ sku: "a", priceCents: 250, qty: 1 }])).toBe(250);
  });

  it("applies no coupon", () => {
    expect(applyCoupon(1000, 0)).toBe(1000);
  });

  it("formats cents as dollars", () => {
    expect(formatPrice(1999)).toBe("$19.99");
  });

  it("renders a badge", () => {
    expect(renderPriceBadge("Sale", 500)).toContain("$5.00");
  });
});
