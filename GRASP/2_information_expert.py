from dataclasses import dataclass, field
from datetime import datetime
from pprint import pprint as pp


# ● Given an object o, which responsibilities can
# be assigned to o?
# ● Expert principle says – assign those
# responsibilities to o for which o has the
# information to fulfill that responsibility.
# ● They have all the information needed to
# perform operations, or in some cases they
# collaborate with others to fulfill their
# responsibilities.

@dataclass(kw_only=True)
class ProductDescription:
    price: int
    description: str


@dataclass
class SaleLineItem:
    product: ProductDescription
    quantity: int

    @property
    def total_price(self) -> in t:
        return self.quantity * self.product.price


@dataclass
class Sale:
    items: list[SaleLineItem] = field(default_factory=list)
    time: datetime = field(default=datetime.now())

    @property
    def total_price(self) -> int:
        return sum((line.quantity * line.product.price for line in self.items))

    def add_line_item(self, product: ProductDescription, quantity: int) -> None:
        self.items.append(SaleLineItem(product, quantity))


def main() -> None:
    headset = ProductDescription(price=5_000, description="Logitech headset")
    keyboard = ProductDescription(price=7_500, description="Reddragon gaming heyboard")

    row1 = SaleLineItem(headset, quantity=2)
    pp(f"Price of line 1: ${row1.total_price / 100:.2f}")

    row2 = SaleLineItem(keyboard, quantity=3)
    pp(f"Price of line 2: ${row2.total_price / 100:.2f}")

    sale = Sale()
    sale.add_line_item(product=headset, quantity=2)
    sale.add_line_item(product=keyboard, quantity=3)

    pp(f"Total price of sale: ${sale.total_price / 100:.2f}")


if __name__ == "__main__":
    main()