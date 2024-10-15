
from fastapi import Depends, HTTPException
from src.common.entities.user_entity import UserEntity
from src.modules.auth.dependencies.dependencies import get_user_in_login_flow
from src.modules.wells.well_service import WellService


class WellController:
    def __init__(self):
        self.well_service = WellService()

    def get_wells(
        self,
        limit: int = 10,
        offset: int = 0,
        user: UserEntity = Depends(get_user_in_login_flow),
    ):
        return self.well_service.get_wells(limit, offset, user)

    def get_well(
        self,
        id: int,
        user: UserEntity = Depends(get_user_in_login_flow),
    ):
        well = self.well_service.get_well(id, user)
        if not well:
            raise HTTPException(status_code=404, detail="Well not found")
        return well

    def create_well(
        self,
        name: str = None,
        description: str = None,
        filename: str = None,
        user: UserEntity = Depends(get_user_in_login_flow),
    ):
        return self.well_service.create_well(name, description, filename, user)
