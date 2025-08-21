# src/infrastructure/config/settings.py
import os
from pydantic_settings import BaseSettings
from pydantic import ConfigDict
from dotenv import load_dotenv

load_dotenv()  # Load biến môi trường từ .env

class Settings(BaseSettings):
    DATABASE_URL: str  # ví dụ: postgresql://user:pass@host:port/dbname
    REDIS_URL: str     # ví dụ: redis://host:port/0
    SECRET_KEY: str
    JWT_SECRET_KEY: str

    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra='ignore'
    )

settings = Settings()
