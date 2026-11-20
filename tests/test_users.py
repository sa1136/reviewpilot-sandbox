from cart import Cart, Item
from users import normalize_email


def test_normalize_email_trims_and_lowercases():
    assert normalize_email("  Ana@Example.COM ") == "ana@example.com"


def test_item_count_sums_quantities():
    cart = Cart()
    cart.add(Item("a", "Apple", 1.0, 2))
    cart.add(Item("b", "Bread", 3.0, 1))
    assert cart.item_count() == 3
