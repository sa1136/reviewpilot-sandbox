from accounts.loyalty import tier_for


def test_tiers():
    assert tier_for(0) == "standard"
    assert tier_for(49_999) == "standard"
    assert tier_for(50_000) == "silver"
    assert tier_for(200_000) == "gold"
