from orders import apply_filter, average_order_value, format_price, qualifies_for_free_shipping


def test_format_price():
    assert format_price(1999) == "$19.99"
    assert format_price(5) == "$0.05"


def test_average_order_value():
    assert average_order_value([10.0, 20.0]) == 15.0


def test_free_shipping_for_large_orders():
    assert qualifies_for_free_shipping(80.0)


def test_apply_filter():
    assert apply_filter([{"total": 30}, {"total": 10}], "total > 20") == [{"total": 30}]
