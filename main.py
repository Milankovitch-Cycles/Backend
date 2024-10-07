from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.modules.auth.auth_routes import auth
from src.modules.wells.well_routes import wells

app = FastAPI(title="Milankovic API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth)
app.include_router(wells)
