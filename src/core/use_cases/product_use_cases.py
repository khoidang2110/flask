# src/core/use_cases/product_use_cases.py
from typing import List
from src.core.entities.product import Product
from src.core.use_cases.interfaces.repositories import IProductRepository
from src.core.exceptions.business_exceptions import NotFoundError

class ProductUseCases:
    def __init__(self, product_repository: IProductRepository):
        self.product_repository = product_repository

    def create(self, name: str, price: float, description: str, category: str, stock_quantity: int) -> Product:
        product = Product(id=0, name=name, price=price, description=description, category=category, stock_quantity=stock_quantity, created_at="")
        return self.product_repository.create(product)

    def get_by_id(self, product_id: int) -> Product:
        product = self.product_repository.find_by_id(product_id)
        if not product:
            raise NotFoundError("Product not found")
        return product

    def get_all(self) -> List[Product]:
        return self.product_repository.get_all()

    def update(self, product_id: int, name: str, price: float, description: str, category: str, stock_quantity: int) -> Product:
        product = Product(id=product_id, name=name, price=price, description=description, category=category, stock_quantity=stock_quantity, created_at="")
        updated_product = self.product_repository.update(product)
        if not updated_product:
            raise NotFoundError("Product not found")
        return updated_product

    def delete(self, product_id: int):
        if not self.product_repository.delete(product_id):
            raise NotFoundError("Product not found")