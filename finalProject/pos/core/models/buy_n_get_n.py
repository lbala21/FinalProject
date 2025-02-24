from pydantic import BaseModel


class BuyNGetN(BaseModel):
    product_id: int
    product_amount: int
    gift_id: int
    gift_amount: int