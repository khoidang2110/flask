# src/infrastructure/web/schemas/auth_schemas.py
from pydantic import BaseModel
from typing import List

class LoginRequest(BaseModel):
    username: str
    password: str

class SignupRequest(BaseModel):
    username: str
    password: str
    roles: List[str] = ["user"]

class Token(BaseModel):
    access_token: str
    token_type: str