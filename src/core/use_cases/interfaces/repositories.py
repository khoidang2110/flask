# src/core/use_cases/interfaces/repositories.py
from abc import ABC, abstractmethod
from typing import Optional, List
from src.core.entities.user import User
from src.core.entities.role import Role
from src.core.entities.product import Product

class IUserRepository(ABC):
    @abstractmethod
    def find_by_username(self, username: str) -> Optional[User]:
        pass

    @abstractmethod
    def create(self, user: User, password_hash: str) -> User:
        pass

    @abstractmethod
    def add_role(self, user_id: int, role_name: str):
        pass

class IProductRepository(ABC):
    @abstractmethod
    def find_by_id(self, product_id: int) -> Optional[Product]:
        pass

    @abstractmethod
    def get_all(self) -> List[Product]:
        pass

    @abstractmethod
    def create(self, product: Product) -> Product:
        pass

    @abstractmethod
    def update(self, product: Product) -> Optional[Product]:
        pass

    @abstractmethod
    def delete(self, product_id: int) -> bool:
        pass