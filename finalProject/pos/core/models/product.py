from pydantic import BaseModel


class Product(BaseModel):
    id: int
    unit: str
    name: str
    barcode: str
    price: int
