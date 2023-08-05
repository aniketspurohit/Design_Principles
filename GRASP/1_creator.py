# this is the first principle of GRASP design principles

from dataclasses import dataclass, field
from datetime import datetime
from pprint import pprint

@dataclass
class ProductDescription:
    price: int
    description: str


@dataclass
class SaleLineItem:
    product: ProductDescription
    quantity: int

@dataclass
class Sale:
    items: list[SaleLineItem] = field(default_factory=list)
    time: datetime = field(default=datetime.now())

    # SaleLineItem created inside Sale. creator responsibility fulfilled
    def add_line_item(self, product: ProductDescription, quantity: int):
        self.items.append(SaleLineItem(product, quantity))

def main() -> None:
    headset = ProductDescription(price=5_000, description="Gaming headset")
    keyboard = ProductDescription(price=7_500, description="Mechanical gaming keyboard")

    sale = Sale()
    sale.add_line_item(product=headset, quantity=2)
    sale.add_line_item(product=keyboard, quantity=3)

    pprint(sale)


if __name__ == "__main__":
    main()


