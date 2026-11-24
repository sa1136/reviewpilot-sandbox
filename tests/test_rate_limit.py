from rate_limit import allow, client_key, retry_after_seconds, window_usage


def test_client_key_uses_remote_addr():
    assert client_key({}, "10.0.0.1") == "10.0.0.1"


def test_first_request_is_allowed():
    assert allow("a", now=1000.0)
    assert window_usage("a") == 1


def test_no_window_means_no_wait():
    assert retry_after_seconds("never-seen") == 0.0
