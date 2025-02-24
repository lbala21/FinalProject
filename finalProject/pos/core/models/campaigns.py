from pydantic import BaseModel
from typing import List

class Discount(BaseModel):
    id: int
    product_id: int
    discount: int

class BuyNGetN(BaseModel):
    id: int
    product_id: int
    product_amount: int
    gift_id: int
    gift_amount: int

class Combo(BaseModel):
    id: int
    products: List[int]
    discount: int