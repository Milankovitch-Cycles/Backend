from fastapi import APIRouter
from src.modules.wells.well_controller import WellController

wells = APIRouter(tags=["Wells"], prefix="/wells")
controller = WellController()


wells.add_api_route("/jobs", controller.get_user_jobs, methods=["GET"])

# Wells
wells.add_api_route("/", controller.get_wells, methods=["GET"])
wells.add_api_route("/{id}", controller.get_well, methods=["GET"])
wells.add_api_route("/{id}", controller.update_well, methods=["PATCH"])
wells.add_api_route("/", controller.create_well, methods=["POST"])
wells.add_api_route("/", controller.delete_well, methods=["DELETE"])

# Well Jobs
wells.add_api_route("/{id}/jobs", controller.get_well_jobs, methods=["GET"])
wells.add_api_route("/{id}/jobs/{job_id}", controller.get_well_job, methods=["GET"])
wells.add_api_route("/{id}/jobs", controller.create_well_job, methods=["POST"])

