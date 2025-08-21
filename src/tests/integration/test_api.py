# src/tests/integration/test_api.py
import pytest
from src.infrastructure.web.app import create_app
from src.infrastructure.database.connection import db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_signup(client):
    response = client.post('/api/signup', json={"username": "testuser", "password": "password"})
    assert response.status_code == 201
    assert "access_token" in response.json