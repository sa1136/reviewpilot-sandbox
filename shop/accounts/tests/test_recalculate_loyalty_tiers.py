import pytest
from django.core.management import call_command

from orders.models import Order

pytestmark = pytest.mark.django_db


def test_recalculate_loyalty_tiers(django_user_model):
    big = django_user_model.objects.create(username="big", email="big@example.com")
    small = django_user_model.objects.create(username="small", email="small@example.com")
    Order.objects.create(customer=big, total_cents=250_000, status=Order.Status.PAID)
    Order.objects.create(customer=small, total_cents=1_000, status=Order.Status.PAID)
    Order.objects.create(customer=small, total_cents=90_000, status=Order.Status.CANCELLED)

    call_command("recalculate_loyalty_tiers")

    big.refresh_from_db()
    small.refresh_from_db()
    assert big.loyalty_tier == "gold"
    assert small.loyalty_tier == "standard"
