from typing import Dict
from pydantic import BaseModel

class Receipt(BaseModel):
    id: int
    is_open: bool = True
    products: Dict[int, int] = {}  # Maps product_id to quantity
    total_price: int = 0

    def add_product(self, product_id: int, price: float, quantity: int) -> None:
        if product_id in self.products:
            self.products[product_id] += quantity
        else:
            self.products[product_id] = quantity
        self.total_price += price * quantity

    def close(self) -> None:
        self.is_open = False
