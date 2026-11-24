import pytest

from cart import Cart, Item, average_price, parse_quantity


def test_add_merges_same_sku():
    cart = Cart()
    cart.add(Item("a", "Apple", 1.0, 2))
    cart.add(Item("a", "Apple", 1.0, 3))
    assert cart.items["a"].quantity == 5


def test_add_rejects_zero_quantity():
    with pytest.raises(ValueError):
        Cart().add(Item("a", "Apple", 1.0, 0))


def test_remove_all_drops_the_line():
    cart = Cart()
    cart.add(Item("a", "Apple", 1.0, 2))
    cart.remove("a", 2)
    assert "a" not in cart.items


def test_remove_unknown_sku_raises():
    with pytest.raises(KeyError):
        Cart().remove("missing")


def test_total_applies_discount_then_tax():
    cart = Cart()
    cart.add(Item("a", "Apple", 10.0, 2))
    assert cart.total(discount_percent=10, tax_rate=0.5) == 27.0


def test_total_rejects_bad_discount():
    with pytest.raises(ValueError):
        Cart().total(discount_percent=101)


def test_parse_quantity_trims():
    assert parse_quantity(" 3 ") == 3


@pytest.mark.parametrize("text", ["0", "-2"])
def test_parse_quantity_rejects_non_positive(text):
    with pytest.raises(ValueError):
        parse_quantity(text)


def test_average_price_of_empty_list():
    assert average_price([]) == 0.0
