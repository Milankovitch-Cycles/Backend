
from fastapi import Depends, HTTPException
from src.common.entities.user_entity import UserEntity
from src.common.entities.well_entity import CreateWellModel, GetWellModel
from src.modules.auth.dependencies.dependencies import get_user_in_login_flow
from src.modules.wells.well_service import WellService
from src.common.services.jobs.jobs_queue_service import jobs_queue_service
from fastapi.encoders import jsonable_encoder
import json


class WellController:
    def __init__(self):
        self.well_service = WellService()

    def get_wells(
        self,
        limit: int = 10,
        offset: int = 0,
        user: UserEntity = Depends(get_user_in_login_flow),
    ) -> list[GetWellModel]:
        return self.well_service.get_wells(limit, offset, user)

    def get_well(
        self,
        id: int,
        user: UserEntity = Depends(get_user_in_login_flow),
    ) -> GetWellModel:
        well = self.well_service.get_well(id, user)
        if not well:
            raise HTTPException(status_code=404, detail="Well not found")
        return well

    async def create_well(
        self,
        well: CreateWellModel,
        user: UserEntity = Depends(get_user_in_login_flow),
    ) -> GetWellModel:
        new_well = self.well_service.create_well(well.name, well.description, well.filename, user)
        # TODO: Create a job for processing the new Well
        await jobs_queue_service.queue_job(json.dumps(jsonable_encoder(new_well)))
        return new_well
