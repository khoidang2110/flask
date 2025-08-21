from pydantic import BaseModel
from typing import List, Optional
from .role import Role

class User(BaseModel):
    id: int
    username: str
    password: str
    created_at: str
    roles: List[Role] = []

    model_config = {
        "from_attributes": True  # Pydantic v2 thay cho orm_mode
    }

class Token(BaseModel):
    access_token: str
    token_type: str

class LoginRequest(BaseModel):
    username: str
    password: str

class SignupRequest(BaseModel):
    username: str
    password: str
    roles: Optional[List[str]] = ["user"]  # mặc định "user"

class UserRole(BaseModel):
    user_id: int
    role_id: int
