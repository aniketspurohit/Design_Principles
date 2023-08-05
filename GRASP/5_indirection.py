# ● How can we avoid a direct coupling between
# two or more elements.
# ● Indirection introduces an intermediate unit to
# communicate between the other units, so that
# the other units are not directly coupled.
# ● Benefits: low coupling
# ● Example: Adapter, Facade, Obserever

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from pprint import pprint as pp

YEAR = 360
HALF_YEAR = YEAR // 2


@dataclass
class Order:
    """Represents and order in an e-commerce system."""

    # If customer object is used, then there will be high coupling
    # hence indirection allows to computer discount using Discount class
    # and use the same in orders. This is indirect way of reducing coupling
    discount: Discount

    def get_discount(self):
        return self.discount.get_lifetime_discount()


@dataclass
class Discount:
    """Discount calculations."""

    customer: Customer

    def get_lifetime_discount(self) -> float:
        """Returns the discount based on how long the person has been a client."""
        if self.customer.lifetime_days < HALF_YEAR:
            return 0.0
        elif HALF_YEAR <= self.customer.lifetime_days < YEAR:
            return 0.1
        elif YEAR <= self.customer.lifetime_days < YEAR * 2:
            return 0.15
        else:
            return 0.2


@dataclass
class Customer:
    """Represents a client."""

    since: date

    @property
    def lifetime_days(self) -> int:
        """Returns how long the person has been a customer in days."""
        return (date.today() - self.since).days


def main() -> None:
    # Usage
    henry = Customer(since=date(2023, 1, 1))
    henry_discount = Discount(henry)
    order1 = Order(henry_discount)
    pp(f"Henry got {order1.get_discount() * 100:.0f} % discount")

    anthony = Customer(since=date(2018, 1, 1))
    discount_old_customer = Discount(anthony)
    order2 = Order(discount_old_customer)
    pp(f"Anthony got {order2.get_discount() * 100:.0f} % discount")


if __name__ == "__main__":
    main()