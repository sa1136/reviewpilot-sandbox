"""A tiny shopping cart. Clean baseline for planting review bugs in PRs."""

from dataclasses import dataclass, field


@dataclass
class Item:
    sku: str
    name: str
    unit_price: float
    quantity: int = 1


@dataclass
class Cart:
    items: dict[str, Item] = field(default_factory=dict)

    def add(self, item: Item) -> None:
        if item.quantity <= 0:
            raise ValueError("quantity must be positive")
        if item.sku in self.items:
            self.items[item.sku].quantity += item.quantity
        else:
            self.items[item.sku] = item

    def remove(self, sku: str, quantity: int = 1) -> None:
        if sku not in self.items:
            raise KeyError(sku)
        existing = self.items[sku]
        if quantity >= existing.quantity:
            del self.items[sku]
        else:
            existing.quantity -= quantity

    def subtotal(self) -> float:
        return sum(i.unit_price * i.quantity for i in self.items.values())

    def total(self, discount_percent: float = 0.0, tax_rate: float = 0.0) -> float:
        if not 0 <= discount_percent <= 100:
            raise ValueError("discount_percent must be between 0 and 100")
        discounted = self.subtotal() * (1 - discount_percent / 100)
        return round(discounted * (1 + tax_rate), 2)


def parse_quantity(text: str) -> int:
    """Parse a user supplied quantity like ' 3 '. Rejects zero, negatives and non numbers."""
    value = int(text.strip())
    if value <= 0:
        raise ValueError("quantity must be positive")
    return value


def average_price(items: list[Item]) -> float:
    if not items:
        return 0.0
    return sum(i.unit_price for i in items) / len(items)
