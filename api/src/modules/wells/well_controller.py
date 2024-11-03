
from src.common.utils.files import list_files
from fastapi import Depends, HTTPException, Form, File, UploadFile
from typing import Annotated
from settings import STORAGE_PATH
from src.common.utils.pagination import get_pagination
from src.common.entities.user_entity import UserEntity
from src.common.entities.well_entity import GetWellModel, GetWellsDto
from src.common.entities.job_entity import GetJobModel, CreateJobModel, JobEntity, UpdateWellDto
from src.modules.auth.dependencies.dependencies import get_user_in_login_flow
from src.modules.wells.well_service import WellService
from src.common.services.jobs.jobs_queue_service import jobs_queue_service
from src.common.types.types import Message


class WellController:
    def __init__(self):
        self.well_service = WellService()

    def get_wells(
        self,
        limit: int = 10,
        offset: int = 0,
        user: UserEntity = Depends(get_user_in_login_flow),
    ) -> GetWellsDto:
        wells, count = self.well_service.get_wells(limit, offset, user)
        pagination = get_pagination(limit, offset, count)
        return {"wells": wells, "pagination": pagination}

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
        name: Annotated[str, Form()],
        description: Annotated[str, Form()],
        file: Annotated[UploadFile, File()],
        user: UserEntity = Depends(get_user_in_login_flow),
    ) -> GetWellModel:
        # Create well in db
        new_well = self.well_service.create_well(name, description, file.filename, user)
        self.well_service.save_well_file(new_well.id, file)
        # Create a job for processing the new Well
        job: JobEntity = self.well_service.create_job(well_id=new_well.id, type="NEW_WELL",
                                                      parameters={"filename": file.filename},
                                                      user=user)
        await jobs_queue_service.queue_job(job)
        return new_well
    
    def delete_well(
        self,
        id: int,
        user: UserEntity = Depends(get_user_in_login_flow),
    ) -> Message:
        self.well_service.delete_well(id, user)
        self.well_service.delete_well_file(id)
        
        return { "message": "Well deleted" }

    def update_well(
        self,
        id: int,
        data: UpdateWellDto,
        user: UserEntity = Depends(get_user_in_login_flow),
    ) -> GetWellModel:
        return self.well_service.update_well(id, data.model_dump(), user)

    def get_well_jobs(
        self,
        id: int,
        user: UserEntity = Depends(get_user_in_login_flow),
    ) -> list[GetJobModel]:
        well = self.well_service.get_well(id, user)
        if not well:
            raise HTTPException(status_code=404, detail="Well not found")
        return well.jobs

    def get_well_job(
        self,
        id: int,
        job_id: int,
        user: UserEntity = Depends(get_user_in_login_flow),
    ) -> GetJobModel:
        job = self.well_service.get_job(id, job_id, user)
        if not job:
            raise HTTPException(status_code=404, detail="Job not found")        
        return GetJobModel(
            id=job.id,
            user_id=job.user_id,
            type=job.type,
            parameters=job.parameters,
            result=job.result,
            status=job.status,
            created_at=job.created_at,
            graphs=list_files(f"{STORAGE_PATH}/{id}/{job_id}/graphs")
        )

    async def create_well_job(
        self,
        id: int,
        job: CreateJobModel,
        user: UserEntity = Depends(get_user_in_login_flow),
    ) -> GetJobModel:
        well = self.well_service.get_well(id, user)
        if not well:
            raise HTTPException(status_code=404, detail="Well not found")
        # Create job in db, then queue it for processing
        new_job: JobEntity = self.well_service.create_job(well.id, job.type, job.parameters, user)
        await jobs_queue_service.queue_job(new_job)
        return new_job
