import httpx


class WmsClient:
    """Warehouse management system API."""

    def __init__(self, base_url: str, api_key: str):
        self._http = httpx.Client(
            base_url=base_url, headers={"X-Api-Key": api_key}, timeout=20
        )

    def create_shipment(
        self,
        reference: str,
        recipient: str,
        address_lines: list[str],
        city: str,
        postal_code: str,
        country: str,
        items: list[tuple[str, int]],
    ) -> str:
        resp = self._http.post(
            "/shipments",
            json={
                "reference": reference,
                "recipient": recipient,
                "address": {
                    "lines": [line for line in address_lines if line],
                    "city": city,
                    "postal_code": postal_code,
                    "country": country,
                },
                "items": [{"sku": sku, "qty": qty} for sku, qty in items],
            },
        )
        resp.raise_for_status()
        return resp.json()["shipment_id"]
