from decimal import Decimal

import pytest

from tax import tax_cents, tax_rate, total_with_tax_cents


def test_tax_rate_is_case_insensitive():
    assert tax_rate(" ca ") == Decimal("7.25")


def test_unknown_region_raises():
    with pytest.raises(KeyError):
        tax_rate("ZZ")


def test_tax_rounds_half_up():
    assert tax_cents(1000, "CA") == 73  # 72.5 rounds up
    assert tax_cents(0, "NY") == 0
    assert tax_cents(999, "OR") == 0


def test_negative_subtotal_raises():
    with pytest.raises(ValueError):
        tax_cents(-1, "CA")


def test_total_with_tax():
    assert total_with_tax_cents(1000, "NY") == 1040
