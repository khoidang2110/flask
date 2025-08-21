# src/adapters/repositories/product_repository.py
from typing import Optional, List
from sqlalchemy.orm import Session
from src.core.entities.product import Product as ProductEntity
from src.infrastructure.database.models import Product as ProductModel
from src.core.use_cases.interfaces.repositories import IProductRepository

class ProductRepository(IProductRepository):
    def __init__(self, db: Session):
        self.db = db

    def find_by_id(self, product_id: int) -> Optional[ProductEntity]:
        product = self.db.query(ProductModel).filter(ProductModel.id == product_id).first()
        if not product:
            return None
        return ProductEntity(
            id=product.id,
            name=product.name,
            price=product.price,
            description=product.description,
            category=product.category,
            stock_quantity=product.stock_quantity,
            created_at=product.created_at.isoformat()
        )

    def get_all(self) -> List[ProductEntity]:
        products = self.db.query(ProductModel).all()
        return [ProductEntity(
            id=p.id,
            name=p.name,
            price=p.price,
            description=p.description,
            category=p.category,
            stock_quantity=p.stock_quantity,
            created_at=p.created_at.isoformat()
        ) for p in products]

    def create(self, product: ProductEntity) -> ProductEntity:
        db_product = ProductModel(
            name=product.name,
            price=product.price,
            description=product.description,
            category=product.category,
            stock_quantity=product.stock_quantity
        )
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return ProductEntity(
            id=db_product.id,
            name=db_product.name,
            price=db_product.price,
            description=db_product.description,
            category=db_product.category,
            stock_quantity=db_product.stock_quantity,
            created_at=db_product.created_at.isoformat()
        )

    def update(self, product: ProductEntity) -> Optional[ProductEntity]:
        db_product = self.db.query(ProductModel).filter(ProductModel.id == product.id).first()
        if not db_product:
            return None
        db_product.name = product.name
        db_product.price = product.price
        db_product.description = product.description
        db_product.category = product.category
        db_product.stock_quantity = product.stock_quantity
        self.db.commit()
        self.db.refresh(db_product)
        return ProductEntity(
            id=db_product.id,
            name=db_product.name,
            price=db_product.price,
            description=db_product.description,
            category=db_product.category,
            stock_quantity=db_product.stock_quantity,
            created_at=db_product.created_at.isoformat()
        )

    def delete(self, product_id: int) -> bool:
        db_product = self.db.query(ProductModel).filter(ProductModel.id == product_id).first()
        if not db_product:
            return False
        self.db.delete(db_product)
        self.db.commit()
        return True