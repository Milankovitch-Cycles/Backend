from typing import List
from src.common.entities.user_entity import UserEntity
from src.common.entities.well_entity import WellEntity
from src.common.entities.job_entity import JobEntity
from src.common.config.config import session
from settings import STORAGE_PATH
from fastapi import UploadFile
import shutil
from pathlib import Path


class WellService:
    def get_wells(self, limit, offset, user: UserEntity)-> List[WellEntity]:
        wells_query = session.query(WellEntity).filter(WellEntity.user_id == user.id)
        wells = wells_query.order_by(WellEntity.created_at.desc()).limit(limit).offset(offset).all()
        count = wells_query.count()
        return wells, count

    def get_well(self, id: int, user: UserEntity) -> WellEntity:
        return session.query(WellEntity).filter(WellEntity.id == id).first()

    def create_well(self, name: str, description: str, filename: str, user: UserEntity) -> WellEntity:
        well = WellEntity(name=name, description=description, filename=filename, user_id=user.id)
        session.add(well)
        session.commit()
        session.refresh(well)
        return well

    def create_job(self, well_id: int, type: str, parameters: dict, user: UserEntity):
        job = JobEntity(well_id=well_id, type=type, parameters=parameters, user_id=user.id)
        session.add(job)
        session.commit()
        session.refresh(job)
        return job

    def get_job(self, well_id: int, id: int, user: UserEntity):
        return session.query(JobEntity).filter(JobEntity.id == id, JobEntity.well_id == well_id).first()

    def save_well_file(self, well_id: int, file: UploadFile):
        # Save file to disk
        path = f"{STORAGE_PATH}/{well_id}/{file.filename}"
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, "wb+") as file_object:
            shutil.copyfileobj(file.file, file_object)
