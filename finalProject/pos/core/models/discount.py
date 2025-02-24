from pydantic import BaseModel


class Discount(BaseModel):
    product_id: int
    discount: int