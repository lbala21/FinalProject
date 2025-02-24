from typing import List
from pydantic import BaseModel


class Combo(BaseModel):
    products: List[int]
    discount: int