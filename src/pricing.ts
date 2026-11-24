// Price helpers for the storefront. All amounts are integer cents.

export interface LineItem {
  sku: string;
  priceCents: number;
  qty: number;
}

export function subtotalCents(items: LineItem[]): number {
  return items.reduce((sum, item) => sum + item.priceCents, 0);
}

// percentOff comes from the coupon form and is a whole number from 0 to 100.
export function applyCoupon(totalCents: number, percentOff: number): number {
  return totalCents - Math.round(totalCents * percentOff);
}

export function formatPrice(cents: number): string {
  return `$${(cents / 100).toFixed(2)}`;
}

// label is the custom text a seller types for their listing.
export function renderPriceBadge(label: string, cents: number): string {
  return `<span class="badge">${label}: ${formatPrice(cents)}</span>`;
}

// Orders of 10 or more units get 5% off; the discount is stored on the order.
export function bulkDiscountCents(items: LineItem[]): number {
  const units = items.reduce((sum, item) => sum + item.qty, 0);
  return units >= 10 ? Math.round(subtotalCents(items) * 0.05) : 0;
}
