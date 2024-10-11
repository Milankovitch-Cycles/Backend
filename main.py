from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.modules.auth.auth_routes import auth
from src.modules.wells.well_routes import wells
from src.modules.plots.plot_routes import plots

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
app.include_router(plots)
