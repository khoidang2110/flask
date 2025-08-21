from typing import Optional
from sqlalchemy.orm import Session
from src.core.entities.user import User as UserEntity
from src.core.entities.role import Role as RoleEntity
from src.infrastructure.database.models import User as UserModel, Role as RoleModel

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def find_by_username(self, username: str) -> Optional[UserEntity]:
        user = self.db.query(UserModel).filter(UserModel.username == username).first()
        if not user:
            return None
        return UserEntity(
            id=user.id,
            username=user.username,
            password=user.password,  # dùng cho nội bộ
            created_at=str(user.created_at),
            roles=[RoleEntity(id=r.id, name=r.name) for r in user.roles]
        )

    def create(self, username: str, password: str) -> UserEntity:
        db_user = UserModel(username=username, password=password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return UserEntity(
            id=db_user.id,
            username=db_user.username,
            password=db_user.password,
            created_at=str(db_user.created_at),
            roles=[]
        )

    def add_role(self, user_id: int, role_name: str):
        user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        role = self.db.query(RoleModel).filter(RoleModel.name == role_name).first()
        if user and role and role not in user.roles:
            user.roles.append(role)
            self.db.commit()
