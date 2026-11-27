from django.conf import settings
from django.db import models

from catalog.models import Product


class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending"
        PAID = "paid"
        SHIPPED = "shipped"
        CANCELLED = "cancelled"

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="orders"
    )
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    total_cents = models.IntegerField()
    currency = models.CharField(max_length=3, default="USD")
    shipping_country = models.CharField(max_length=2, default="US")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)


class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="lines")
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price_cents = models.IntegerField()
