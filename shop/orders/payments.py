import httpx
from django.conf import settings


class PaymentDeclined(Exception):
    pass


def charge(amount_cents: int, token: str, idempotency_key: str) -> str:
    """Charge the card behind `token`. Returns the payment id."""
    resp = httpx.post(
        f"{settings.PAYMENTS_API_URL}/charges",
        json={"amount": amount_cents, "currency": "usd", "source": token},
        headers={
            "Authorization": f"Bearer {settings.PAYMENTS_API_KEY}",
            "Idempotency-Key": idempotency_key,
        },
        timeout=15,
    )
    if resp.status_code == 402:
        raise PaymentDeclined(resp.json().get("message", "declined"))
    resp.raise_for_status()
    return resp.json()["id"]
