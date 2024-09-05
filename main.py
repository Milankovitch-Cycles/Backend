from fastapi import FastAPI
from src.modules.auth.auth_controller import auth

app = FastAPI(title="Milankovic API")

app.include_router(auth)
