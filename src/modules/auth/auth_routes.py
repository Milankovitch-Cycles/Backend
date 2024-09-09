from fastapi import APIRouter
from src.modules.auth.auth_controller import AuthController

auth = APIRouter(tags=["Auth"], prefix="/auth")
controller = AuthController()


auth.add_api_route("/register", controller.register, methods=["POST"])
auth.add_api_route("/login", controller.login, methods=["POST"])
auth.add_api_route("/reset_password/init", controller.init_reset_password, methods=["POST"])
auth.add_api_route("/reset_password/verify", controller.verify_reset_password, methods=["POST"])
auth.add_api_route("/reset_password/finish", controller.finish_reset_password, methods=["POST"])
