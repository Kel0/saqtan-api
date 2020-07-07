from sqlalchemy.orm import Session

from .models import City_code
from loguru import logger


class CityCode(object):
    @logger.catch
    def get_city_codes(self, db: Session):
        return db.query(City_code.City_code).all()
