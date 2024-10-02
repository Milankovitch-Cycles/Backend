
from fastapi import Depends
from src.common.entities.user_entity import UserEntity
from src.modules.auth.dependencies.dependencies import get_user_in_login_flow
from src.modules.wells.well_service import WellService

class WellController:
    def __init__(self):
        self.well_service = WellService()

    def test(
        self,
        user: UserEntity = Depends(get_user_in_login_flow),
    ):
        return self.well_service.test(user)