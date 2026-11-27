from datetime import timedelta

from django.core.management.base import BaseCommand
from django.db.models import Sum
from django.utils import timezone

from accounts.loyalty import tier_for
from accounts.models import User
from orders.models import Order


class Command(BaseCommand):
    help = "Recalculate every customer's loyalty tier from paid orders in the last 12 months."

    def handle(self, *args, **options):
        since = timezone.now() - timedelta(days=365)
        changed = 0
        for user in User.objects.filter(is_active=True).only("id", "loyalty_tier"):
            spent = (
                Order.objects.filter(
                    customer=user,
                    status__in=[Order.Status.PAID, Order.Status.SHIPPED],
                    created_at__gte=since,
                ).aggregate(total=Sum("total_cents"))["total"]
                or 0
            )
            tier = tier_for(spent)
            if tier != user.loyalty_tier:
                user.loyalty_tier = tier
                user.save(update_fields=["loyalty_tier"])
                changed += 1
        self.stdout.write(f"updated {changed} customers")
