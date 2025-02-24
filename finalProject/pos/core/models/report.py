from pydantic import BaseModel

class Report(BaseModel):
    n_receipts: int
    revenue: float