from decimal import Decimal

from catalog.models import Product
from catalog.pricing import on_sale, unit_price
from catalog.serializers import product_json


def make(price, sale=None):
    return Product(sku="A1", name="Mug", price=Decimal(price), sale_price=sale and Decimal(sale))


def test_unit_price_uses_lower_sale_price():
    assert unit_price(make("12.00", "9.50")) == Decimal("9.50")


def test_unit_price_ignores_higher_sale_price():
    assert unit_price(make("12.00", "15.00")) == Decimal("12.00")


def test_on_sale():
    assert on_sale(make("12.00", "9.50"))
    assert not on_sale(make("12.00"))


def test_product_json():
    assert product_json(make("12.00", "9.50"))["price"] == "9.50"
