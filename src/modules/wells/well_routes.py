from fastapi import APIRouter
from src.modules.wells.well_controller import WellController

wells = APIRouter(tags=["Wells"], prefix="/wells")
controller = WellController()

wells.add_api_route("/test", controller.test, methods=["GET"])
