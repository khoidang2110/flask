# src/tests/unit/test_use_cases.py
import pytest
from src.core.use_cases.user_use_cases import AuthUseCases
from src.core.entities.user import User
from src.core.exceptions.business_exceptions import InvalidCredentialsError, UserAlreadyExistsError
from unittest.mock import Mock

def test_login_success():
    user_repo = Mock()
    user = User(id=1, username="testuser", created_at="2023-01-01T00:00:00", roles=[])
    user.password = "$2b$12$..."  # Hashed password
    user_repo.find_by_username.return_value = user
    auth_use_cases = AuthUseCases(user_repo)

    result = auth_use_cases.login("testuser", "password")
    assert result.id == 1
    assert result.username == "testuser"

def test_login_invalid_credentials():
    user_repo = Mock()
    user_repo.find_by_username.return_value = None
    auth_use_cases = AuthUseCases(user_repo)

    with pytest.raises(InvalidCredentialsError):
        auth_use_cases.login("testuser", "wrongpassword")