# src/infrastructure/web/schemas/product_schemas.py
from pydantic import BaseModel
from typing import Optional
from src.core.entities.product import Product

class ProductCreate(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    category: Optional[str] = None
    stock_quantity: int = 0

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None
    category: Optional[str] = None
    stock_quantity: Optional[int] = None

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str]
    category: Optional[str]
    stock_quantity: int
    created_at: str

    @classmethod
    def from_entity(cls, product: Product):
        return cls(
            id=product.id,
            name=product.name,
            price=product.price,
            description=product.description,
            category=product.category,
            stock_quantity=product.stock_quantity,
            created_at=product.created_at
        )