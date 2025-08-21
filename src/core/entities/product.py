# src/core/entities/product.py
from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str]
    category: Optional[str]
    stock_quantity: int
    created_at: str