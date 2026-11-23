import coupons


def test_normalize_code():
    assert coupons.normalize_code("  welcome10 ") == "WELCOME10"


def test_is_welcome_code_rejects_other_codes():
    assert not coupons.is_welcome_code("SPRING5")


def test_remember_code():
    assert coupons.remember_code("a1") == ["A1"]


def test_load_coupon_terms(tmp_path, monkeypatch):
    (tmp_path / "spring.txt").write_text("Valid in April.")
    monkeypatch.setattr(coupons, "COUPON_DIR", str(tmp_path))
    assert coupons.load_coupon_terms("spring") == "Valid in April."
