from src.common.entities.user_entity import UserEntity
from src.common.entities.well_entity import WellEntity
from src.common.config.config import session
import lasio


class WellService:
    def get_wells(self, limit, offset, user: UserEntity):
        return session.query(WellEntity).order_by(WellEntity.created_at.desc()).limit(limit).offset(offset).all()

    def get_well(self, id: int, user: UserEntity):
        return session.query(WellEntity).filter(WellEntity.id == id).first()

    def create_well(self, name: str, description: str, filename: str, user: UserEntity):
        well = WellEntity(name=name, description=description, filename=filename, user_id=user.id)
        session.add(well)
        session.commit()
        return well

    def get_dataframe(self, id: int, user: UserEntity):
        well = self.get_well(id, user)
        file = lasio.read(well.filename)
        return file.df()