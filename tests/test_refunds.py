from refunds import is_refundable, load_refund_request, refund_amount, refund_reason_label


def test_refund_amount_returns_a_number():
    assert refund_amount(100.0, 10) >= 0


def test_is_refundable_recent_purchase():
    assert is_refundable(3)


def test_load_refund_request_is_callable():
    assert callable(load_refund_request)


def test_refund_reason_label():
    assert refund_reason_label("damaged") == "Item arrived damaged"
    assert refund_reason_label("unknown") == "Other"
