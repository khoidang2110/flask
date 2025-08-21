from flask import request
from flask_restx import Namespace, Resource, fields
from src.core.use_cases.user_use_cases import AuthUseCases
from src.adapters.repositories.user_repository import UserRepository
from src.infrastructure.database.connection import get_db  # đúng file connection.py
from src.core.exceptions.business_exceptions import InvalidCredentialsError, UserAlreadyExistsError
from flask_jwt_extended import create_access_token
from pydantic import ValidationError
from src.infrastructure.web.schemas.auth_schemas import LoginRequest
from pydantic import ValidationError


api = Namespace("auth", description="Authentication operations")

# -------- Swagger Models (DTOs) --------
login_model = api.model("LoginRequest", {
    "username": fields.String(required=True, description="Tên đăng nhập"),
    "password": fields.String(required=True, description="Mật khẩu"),
})

signup_model = api.model("SignupRequest", {
    "username": fields.String(required=True, description="Tên đăng nhập"),
    "password": fields.String(required=True, description="Mật khẩu"),
})

token_model = api.model("TokenResponse", {
    "access_token": fields.String(description="JWT token"),
    "token_type": fields.String(description="Loại token (Bearer)")
})

# -------- Routes --------
@api.route("/login")
class LoginResource(Resource):
    @api.expect(login_model)
    @api.response(200, "Success", token_model)
    @api.response(401, "Invalid credentials")
    @api.response(422, "Validation Error")
    def post(self):
        data = request.json
        try:
            # Validate dữ liệu request bằng Pydantic
            validated_data = LoginRequest(**data)
        except ValidationError as e:
            # Trả về lỗi nếu không hợp lệ
            return {"message": "Validation failed", "errors": e.errors()}, 422

        with get_db() as db:
            repo = UserRepository(db)
            auth_use_cases = AuthUseCases(repo)
            try:
                # Dùng dữ liệu đã validated
                user = auth_use_cases.login(
                    validated_data.username, validated_data.password
                )
                token = create_access_token(identity=user.id)
                return {"access_token": token, "token_type": "Bearer"}, 200
            except InvalidCredentialsError:
                return {"message": "Invalid username or password"}, 401


@api.route("/signup")
class SignupResource(Resource):
    @api.expect(signup_model)
    @api.response(201, "User created successfully")
    @api.response(400, "User already exists")
    def post(self):
        data = request.json
        with get_db() as db:
            repo = UserRepository(db)
            auth_use_cases = AuthUseCases(repo)
            try:
                user = auth_use_cases.signup(data["username"], data["password"])
                return {"message": "User created", "user_id": user.id}, 201
            except UserAlreadyExistsError:
                return {"message": "User already exists"}, 400
