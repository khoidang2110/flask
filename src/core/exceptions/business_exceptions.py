# src/core/exceptions/business_exceptions.py
class InvalidCredentialsError(Exception):
    """Raised when login credentials are invalid."""
    def __init__(self, message: str = "Invalid username or password"):
        super().__init__(message)

class UserAlreadyExistsError(Exception):
    """Raised when attempting to create a user that already exists."""
    def __init__(self, message: str = "User already exists"):
        super().__init__(message)

class NotFoundError(Exception):
    """Raised when a resource is not found."""
    def __init__(self, message: str = "Resource not found"):
        super().__init__(message)