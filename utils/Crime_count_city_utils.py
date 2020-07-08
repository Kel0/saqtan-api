from loguru import logger
from sqlalchemy.orm import Session

from Database.models.cache import pack_models


class CrimeCountCity(object):
    @logger.catch
    def get_crimes_count_by_cities(self, db: Session):
        return db.query(pack_models.Crime_count_city.Crime_count_city).all()
