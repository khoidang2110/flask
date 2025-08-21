# src/core/use_cases/user_use_cases.py
from typing import Optional
from src.core.entities.user import User
from src.core.use_cases.interfaces.repositories import IUserRepository
from src.shared.utils.password import hash_password, verify_password
from src.core.exceptions.business_exceptions import InvalidCredentialsError, UserAlreadyExistsError

class AuthUseCases:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def login(self, username: str, password: str) -> Optional[User]:
        user = self.user_repository.find_by_username(username)
        if not user or not verify_password(password, user.password):
            raise InvalidCredentialsError()
        return user

    def signup(self, username: str, password: str, roles: list[str] = ["user"]) -> User:
        if self.user_repository.find_by_username(username):
            raise UserAlreadyExistsError()
        password_hash = hash_password(password)
        user = User(id=0, username=username, created_at="", roles=[])
        created_user = self.user_repository.create(user, password_hash)
        for role in roles:
            self.user_repository.add_role(created_user.id, role)
        return created_user