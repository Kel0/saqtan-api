from loguru import logger
from sqlalchemy.orm import Session

from Database.models.cache import pack_models


class CrimeCode(object):
    @logger.catch
    def get_crime_codes(self, db: Session):
        return db.query(pack_models.Crime_code.Crime_code).all()
