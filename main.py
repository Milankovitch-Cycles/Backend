from fastapi import FastAPI
from src.modules.auth.auth_routes import auth
from src.modules.wells.well_routes import wells

app = FastAPI(title="Milankovic API")

app.include_router(auth)
app.include_router(wells)