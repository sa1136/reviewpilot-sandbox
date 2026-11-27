from accounts.models import User

SILVER_CENTS = 50_000
GOLD_CENTS = 200_000


def tier_for(spent_cents: int) -> str:
    """Loyalty tier for the amount a customer spent in the last 12 months."""
    if spent_cents >= GOLD_CENTS:
        return User.Tier.GOLD
    if spent_cents >= SILVER_CENTS:
        return User.Tier.SILVER
    return User.Tier.STANDARD
