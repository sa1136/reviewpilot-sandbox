from django.db import transaction

from orders.cart import cart_total_cents, line_total_cents
from orders.guest_checkout import resolve_customer
from orders.models import Order, OrderLine
from orders.payments import charge


class CheckoutError(Exception):
    pass


def place_order(email: str, lines: list, payment_token: str, shipping_country: str | None = None):
    """lines: (product, quantity) pairs from the cart."""
    if not lines:
        raise CheckoutError("cart is empty")
    with transaction.atomic():
        customer = resolve_customer(email)
        total = cart_total_cents(lines)
        order = Order.objects.create(
            customer=customer, total_cents=total, shipping_country=shipping_country
        )
        OrderLine.objects.bulk_create(
            [
                OrderLine(
                    order=order,
                    product=product,
                    quantity=quantity,
                    unit_price_cents=line_total_cents(product, 1),
                )
                for product, quantity in lines
            ]
        )
    charge(total, payment_token, idempotency_key=f"order-{order.id}")
    order.status = Order.Status.PAID
    order.save(update_fields=["status"])
    return order
