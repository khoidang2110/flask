# src/infrastructure/web/routes/products.py
from flask_restx import Namespace, Resource, fields
from flask import request
import os
import redis
from src.core.use_cases.product_use_cases import ProductUseCases
from src.adapters.repositories.product_repository import ProductRepository
from src.infrastructure.database.connection import get_db
from src.infrastructure.web.schemas.product_schemas import ProductCreate, ProductUpdate, ProductResponse
from src.core.exceptions.business_exceptions import NotFoundError
from redis import Redis
import json

api = Namespace("products", description="Product operations")

redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
redis_client = redis.from_url(redis_url, decode_responses=True)

# Định nghĩa Swagger models
product_model = api.model("Product", {
    "id": fields.Integer(readonly=True),
    "name": fields.String(required=True),
    "price": fields.Float(required=True),
    "description": fields.String,
    "category": fields.String,
    "stock_quantity": fields.Integer
})

create_model = api.model("ProductCreate", {
    "name": fields.String(required=True),
    "price": fields.Float(required=True),
    "description": fields.String,
    "category": fields.String,
    "stock_quantity": fields.Integer
})

update_model = api.inherit("ProductUpdate", create_model, {})

# CRUD Routes
@api.route("/")
class ProductList(Resource):
    @api.marshal_list_with(product_model)
    def get(self):
        """Get all products with Redis cache"""
        # 1. Check Redis cache
        cached_products = redis_client.get("products")
        if cached_products:
            print(">>> Returned from cache")  # log ra console
            products_list = json.loads(cached_products)
            return products_list

        # 2. Nếu không có cache, query DB
        with get_db() as db_session:
            use_cases = ProductUseCases(ProductRepository(db_session))
            products = use_cases.get_all()
            products_list = [ProductResponse.from_entity(p).dict() for p in products]

            # 3. Lưu vào Redis, expire 60s
            redis_client.setex("products", 60, json.dumps(products_list))
            print(">>> Returned from DB and cached")  # log ra console

        return products_list

@api.route("/<int:product_id>")
@api.response(404, "Product not found")
class Product(Resource):
    @api.marshal_with(product_model)
    def get(self, product_id):
        """Get a product by ID"""
        with get_db() as db_session:
            use_cases = ProductUseCases(ProductRepository(db_session))
            try:
                product = use_cases.get_by_id(product_id)
                return ProductResponse.from_entity(product).dict()
            except NotFoundError:
                api.abort(404, "Product not found")

    @api.expect(update_model)
    @api.marshal_with(product_model)
    def put(self, product_id):
        """Update a product"""
        data = request.json
        with get_db() as db_session:
            use_cases = ProductUseCases(ProductRepository(db_session))
            try:
                product = use_cases.update(
                    product_id,
                    data["name"],
                    data["price"],
                    data.get("description"),
                    data.get("category"),
                    data.get("stock_quantity", 0)
                )
                return ProductResponse.from_entity(product).dict()
            except NotFoundError:
                api.abort(404, "Product not found")

    def delete(self, product_id):
        """Delete a product"""
        with get_db() as db_session:
            use_cases = ProductUseCases(ProductRepository(db_session))
            try:
                use_cases.delete(product_id)
                return {"message": "Product deleted"}, 200
            except NotFoundError:
                api.abort(404, "Product not found")

