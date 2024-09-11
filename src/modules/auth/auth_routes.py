from fastapi import APIRouter
from src.modules.auth.auth_controller import AuthController

auth = APIRouter(tags=["Auth"], prefix="/auth")
controller = AuthController()

auth.add_api_route("/register/start", controller.start_registration, methods=["POST"])
auth.add_api_route("/register/finish", controller.finish_registration, methods=["POST"])
auth.add_api_route("/login", controller.login, methods=["POST"])
auth.add_api_route("/password/reset/start", controller.start_password_reset, methods=["POST"])
auth.add_api_route("/password/reset/verify", controller.verify_password_reset, methods=["POST"])
auth.add_api_route("/password/reset/finish", controller.finish_password_reset, methods=["POST"])
