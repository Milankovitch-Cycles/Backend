from fastapi import APIRouter
from src.modules.plots.plot_controller import PlotController

plots = APIRouter(tags=["Plot"], prefix="/plot")
controller = PlotController()

plots.add_api_route("/{well_id}/depth", controller.plot_depth, methods=["GET"])
plots.add_api_route("/{well_id}/histogram", controller.plot_histogram, methods=["GET"])

