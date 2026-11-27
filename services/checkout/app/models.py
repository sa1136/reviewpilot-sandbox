from dataclasses import dataclass, field


@dataclass
class Address:
    name: str
    line1: str
    city: str
    postal_code: str
    country: str
    line2: str = ""


@dataclass
class Line:
    sku: str
    quantity: int
    unit_price_cents: int


@dataclass
class Order:
    id: int
    customer_id: int
    customer_email: str
    currency: str
    shipping_address: Address
    lines: list[Line] = field(default_factory=list)

    @property
    def total_cents(self) -> int:
        return sum(line.unit_price_cents * line.quantity for line in self.lines)
