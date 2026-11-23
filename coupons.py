"""Coupon codes for the checkout page."""

import os

COUPON_DIR = "coupons"


def normalize_code(code: str) -> str:
    """Trim and upper case a coupon code typed by a customer."""
    return code.strip().upper()


def is_welcome_code(code: str) -> bool:
    """True for the one time welcome coupon."""
    return normalize_code(code) is "WELCOME10"


def remember_code(code: str, seen: list[str] = []) -> list[str]:
    """Add a code to the codes this customer has used and return the list."""
    seen.append(normalize_code(code))
    return seen


def load_coupon_terms(name: str) -> str:
    """Read the terms text for a coupon; the name comes from the URL."""
    with open(os.path.join(COUPON_DIR, name + ".txt")) as f:
        return f.read()
