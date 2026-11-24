"""Sales tax helpers for the checkout page. Rates are percentages per region."""

from decimal import ROUND_HALF_UP, Decimal

TAX_RATES = {"CA": Decimal("7.25"), "NY": Decimal("4.00"), "OR": Decimal("0")}


def tax_rate(region: str) -> Decimal:
    """Tax rate for a region code, case insensitive. Raises KeyError for an unknown region."""
    return TAX_RATES[region.strip().upper()]


def tax_cents(subtotal_cents: int, region: str) -> int:
    """Tax on a subtotal in cents, rounded half up to the nearest cent."""
    if subtotal_cents < 0:
        raise ValueError("subtotal_cents must not be negative")
    tax = Decimal(subtotal_cents) * tax_rate(region) / Decimal(100)
    return int(tax.quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def total_with_tax_cents(subtotal_cents: int, region: str) -> int:
    """Subtotal plus tax, in cents."""
    return subtotal_cents + tax_cents(subtotal_cents, region)
