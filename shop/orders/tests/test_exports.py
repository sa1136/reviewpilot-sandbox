import csv
import io
from datetime import datetime, timedelta, timezone

import pytest

from orders.exports import HEADER, iter_orders_csv
from orders.models import Order

pytestmark = pytest.mark.django_db


def test_write_orders_csv(django_user_model):
    user = django_user_model.objects.create(username="ana", email="ana@example.com")
    Order.objects.create(customer=user, total_cents=1999, status=Order.Status.PAID)
    start = datetime.now(timezone.utc) - timedelta(days=1)
    text = "".join(iter_orders_csv(start, start + timedelta(days=2)))
    rows = list(csv.reader(io.StringIO(text)))
    assert len(rows) == 2
    assert rows[0] == HEADER
    assert rows[1][2:] == ["ana@example.com", "0", "19.99", "paid"]
