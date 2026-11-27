import csv

from django.db.models import Count

from orders.models import Order
from orders.money import format_cents

HEADER = ["order_id", "created_at", "customer_email", "lines", "total", "status"]


class _Echo:
    """File-like object for csv.writer that hands each row back instead of storing it."""

    def write(self, value):
        return value


def iter_orders_csv(start, end):
    """CSV lines for orders created in [start, end), header first."""
    writer = csv.writer(_Echo())
    yield writer.writerow(HEADER)
    orders = (
        Order.objects.filter(created_at__gte=start, created_at__lt=end)
        .select_related("customer")
        .annotate(line_count=Count("lines"))
        .order_by("created_at")
    )
    for order in orders.iterator(chunk_size=2000):
        yield writer.writerow(
            [
                order.id,
                order.created_at.isoformat(),
                order.customer.email,
                order.line_count,
                format_cents(order.total_cents),
                order.status,
            ]
        )
