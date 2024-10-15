from fastapi import APIRouter
from src.modules.wells.well_controller import WellController

wells = APIRouter(tags=["Wells"], prefix="/wells")
controller = WellController()

wells.add_api_route("/", controller.get_wells, methods=["GET"])
wells.add_api_route("/{id}", controller.get_well, methods=["GET"])

wells.add_api_route("/", controller.create_well, methods=["POST"])
