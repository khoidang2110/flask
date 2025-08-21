# src/infrastructure/web/app.py

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_restx import Api

from src.infrastructure.database.connection import db, init_db
from src.infrastructure.config.settings import settings
from src.infrastructure.web.routes.products import api as product_ns
from src.infrastructure.web.routes.auth import api as auth_ns



def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = settings.DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = settings.JWT_SECRET_KEY

    init_db(app)
    JWTManager(app)
    CORS(app)

    # Khởi tạo RESTX API
    api = Api(
        app,
        version="1.0",
        title="My API",
        description="API with Flask-RESTX and Swagger UI",
        doc="/swagger"   # Swagger UI ở /swagger
    )
    
      # Đăng ký namespace
    api.add_namespace(auth_ns, path="/api/auth")
    api.add_namespace(product_ns, path="/api/products")
    
    return app