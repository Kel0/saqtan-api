from loguru import logger
from sqlalchemy.orm import Session

from Database.models.cache import pack_models


class CityCode(object):
    @logger.catch
    def get_city_codes(self, db: Session, type: str):
        return (
            db.query(pack_models.City_code.City_code)
            .filter(pack_models.City_code.City_code.type == type)
            .all()
        )
