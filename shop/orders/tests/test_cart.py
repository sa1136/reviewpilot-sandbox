from decimal import Decimal

from catalog.models import Product
from orders.cart import cart_total_cents, line_total_cents
from orders.money import format_cents


def mug(price="12.00", sale=None):
    return Product(sku="A1", name="Mug", price=Decimal(price), sale_price=sale and Decimal(sale))


def test_line_total_cents():
    assert line_total_cents(mug("12.50"), 3) == 3750


def test_cart_total_uses_sale_price():
    assert cart_total_cents([(mug("12.00", "9.99"), 2), (mug("1.00"), 1)]) == 2098


def test_format_cents():
    assert format_cents(1999) == "19.99"
    assert format_cents(5) == "0.05"
    assert format_cents(-250) == "-2.50"
