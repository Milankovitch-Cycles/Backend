from src.common.entities.user_entity import UserEntity
from src.common.entities.well_entity import WellEntity
from src.common.config.config import session


class WellService:
    def get_wells(self, limit, offset, user: UserEntity):
        return session.query(WellEntity).order_by(WellEntity.created_at.desc()).limit(limit).offset(offset).all()

    def get_well(self, id: int, user: UserEntity):
        return session.query(WellEntity).filter(WellEntity.id == id).first()

    def create_well(self, name: str, description: str, filename: str, user: UserEntity) -> WellEntity:
        well = WellEntity(name=name, description=description, filename=filename, user_id=user.id)
        session.add(well)
        session.commit()
        session.refresh(well)
        return well
