from settings import STORAGE_PATH
from src.common.entities.job_entity import GetJobModel
from src.common.utils.files import list_files

def map_to_well_with_graphs(well):
     for job in well.jobs:
            job.graphs = list_files(f"{STORAGE_PATH}/{job.well_id}/{job.id}/graphs")  
     return well

def map_to_job_with_graphs(job):
    return GetJobModel(
        id=job.id,
        user_id=job.user_id,
        type=job.type,
        parameters=job.parameters,
        result=job.result,
        status=job.status,
        created_at=job.created_at,
        graphs=list_files(f"{STORAGE_PATH}/{job.well_id}/{job.id}/graphs")
    )