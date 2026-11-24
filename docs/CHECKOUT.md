# Checkout guide

How a cart becomes an order.

## Flow

1. The customer adds items with `Cart.add`. Adding a SKU that is already in the cart increases
   its quantity instead of adding a second line.
2. `Cart.remove` takes away a quantity; removing as many or more than the cart holds drops the
   line.
3. `Cart.total(discount_percent, tax_rate)` applies the discount first, then tax, and rounds to
   cents. A discount outside 0 to 100 raises `ValueError`.

## Quantities from forms

Use `parse_quantity` for any quantity a customer types. It trims spaces and rejects zero,
negative numbers and text that is not a number.

## Averages

`average_price` returns 0.0 for an empty list, so report pages never divide by zero.
