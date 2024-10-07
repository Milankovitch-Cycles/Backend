from fastapi import APIRouter
from src.modules.auth.auth_controller import AuthController
from src.common.types.types import Token, Message

auth = APIRouter(tags=["Auth"], prefix="/auth")
controller = AuthController()

auth.add_api_route("/register/start", controller.start_registration, response_model=Token, methods=["POST"])
auth.add_api_route("/register/finish", controller.finish_registration, response_model=Message, methods=["POST"])
auth.add_api_route("/login", controller.login,  response_model=Token, methods=["POST"])
auth.add_api_route("/token", controller.token,  response_model=Token, methods=["POST"])
auth.add_api_route("/password/reset/start", controller.start_password_reset, response_model=Token, methods=["POST"])
auth.add_api_route("/password/reset/verify", controller.verify_password_reset, response_model=Message, methods=["POST"])
auth.add_api_route("/password/reset/finish", controller.finish_password_reset, response_model=Message, methods=["POST"])
