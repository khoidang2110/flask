# Clean Architecture Python Project Structure

## Project Structure
```
my_clean_app/
├── Pipfile                     # Pipenv dependencies
├── Pipfile.lock               # Locked dependencies
├── .env                       # Environment variables
├── .env.example              # Environment template
├── .gitignore                # Git ignore rules
├── README.md                 # Project documentation
├── pyproject.toml            # Tool configuration
├── .pre-commit-config.yaml   # Pre-commit hooks
├── docker-compose.yml        # Docker development setup
├── Dockerfile                # Container definition
├── requirements.txt          # For deployment
├── app.py                    # Flask application entry point
├── wsgi.py                   # Production WSGI entry
├── migrations/               # Database migrations
└── src/                      # Source code
    ├── __init__.py
    ├── core/                 # Enterprise Business Rules
    │   ├── __init__.py
    │   ├── entities/         # Business entities
    │   │   ├── __init__.py
    │   │   ├── user.py
    │   │   └── product.py
    │   ├── use_cases/        # Application Business Rules
    │   │   ├── __init__.py
    │   │   ├── interfaces/   # Abstract interfaces
    │   │   │   ├── __init__.py
    │   │   │   ├── repositories.py
    │   │   │   └── services.py
    │   │   ├── user_use_cases.py
    │   │   └── product_use_cases.py
    │   └── exceptions/       # Business exceptions
    │       ├── __init__.py
    │       └── business_exceptions.py
    ├── adapters/             # Interface Adapters
    │   ├── __init__.py
    │   ├── repositories/     # Data access implementations
    │   │   ├── __init__.py
    │   │   ├── user_repository.py
    │   │   └── product_repository.py
    │   ├── services/         # External services
    │   │   ├── __init__.py
    │   │   ├── cache_service.py
    │   │   └── email_service.py
    │   └── serializers/      # Data transformation
    │       ├── __init__.py
    │       ├── user_serializer.py
    │       └── product_serializer.py
    ├── infrastructure/       # Frameworks & Drivers
    │   ├── __init__.py
    │   ├── web/              # Web framework (Flask)
    │   │   ├── __init__.py
    │   │   ├── app.py        # Flask app factory
    │   │   ├── routes/       # API routes
    │   │   │   ├── __init__.py
    │   │   │   ├── auth.py
    │   │   │   ├── users.py
    │   │   │   └── products.py
    │   │   ├── middleware/   # Middleware
    │   │   │   ├── __init__.py
    │   │   │   ├── auth_middleware.py
    │   │   │   └── error_handler.py
    │   │   └── schemas/      # Pydantic models for API
    │   │       ├── __init__.py
    │   │       ├── auth_schemas.py
    │   │       ├── user_schemas.py
    │   │       └── product_schemas.py
    │   ├── database/         # Database configuration
    │   │   ├── __init__.py
    │   │   ├── models.py     # SQLAlchemy models
    │   │   ├── connection.py # Database connection
    │   │   └── migrations.py # Migration utilities
    │   ├── external/         # External service clients
    │   │   ├── __init__.py
    │   │   ├── redis_client.py
    │   │   └── email_client.py
    │   └── config/           # Configuration
    │       ├── __init__.py
    │       ├── settings.py   # Application settings
    │       └── dependencies.py # Dependency injection
    ├── shared/               # Shared utilities
    │   ├── __init__.py
    │   ├── utils/           # Common utilities
    │   │   ├── __init__.py
    │   │   ├── password.py
    │   │   ├── validators.py
    │   │   └── datetime_utils.py
    │   └── constants/       # Application constants
    │       ├── __init__.py
    │       └── app_constants.py
    └── tests/               # Test files
        ├── __init__.py
        ├── conftest.py      # Pytest configuration
        ├── unit/            # Unit tests
        │   ├── __init__.py
        │   ├── test_entities.py
        │   ├── test_use_cases.py
        │   └── test_repositories.py
        ├── integration/     # Integration tests
        │   ├── __init__.py
        │   ├── test_api.py
        │   └── test_database.py
        └── fixtures/        # Test fixtures
            ├── __init__.py
            └── sample_data.py
```



source ~/.local/share/virtualenvs/crud_flask-DddQAB1f/bin/activate
python app.py
http://127.0.0.1:5001/swagger