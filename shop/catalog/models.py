from django.db import models


class Product(models.Model):
    sku = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.sku} {self.name}"
