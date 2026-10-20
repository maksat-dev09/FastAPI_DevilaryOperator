from pydantic import BaseModel
from datetime import datetime


class ProductInputSchema(BaseModel):
    product_name: str
    price: int

class ProductOutputSchema(BaseModel):
    id: int
    product_name: str
    price: int
    created_date: datetime



