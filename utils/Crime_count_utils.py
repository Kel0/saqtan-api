from loguru import logger
from sqlalchemy.orm import Session

from Database.models.cache import pack_models


class CrimeCount(object):
    @logger.catch
    def get_crimes_count(self, db: Session, YR: int):
        if YR == 0:
            return db.query(pack_models.Crime_count.Crime_count).all()

        else:
            return (
                db.query(pack_models.Crime_count.Crime_count)
                .filter(pack_models.Crime_count.Crime_count.YR == YR)
                .all()
            )
