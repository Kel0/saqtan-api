from loguru import logger
from sqlalchemy.orm import Session

from Database.models.cache import pack_models


class CrimeCountPeriods(object):
    @logger.catch
    def get_crime_count_by_periods(self, db: Session, YR: int, period: int):
        if YR + period == 0:
            return db.query(pack_models.Crime_count_period.Crime_count_period).all()

        if YR == 0:
            return (
                db.query(pack_models.Crime_count_period.Crime_count_period)
                .filter(
                    pack_models.Crime_count_period.Crime_count_period.period == period
                )
                .all()
            )

        if period == 0:
            return (
                db.query(pack_models.Crime_count_period.Crime_count_period)
                .filter(pack_models.Crime_count_period.Crime_count_period.YR == YR)
                .all()
            )

        if period != 0 and YR != 0:
            return (
                db.query(pack_models.Crime_count_period.Crime_count_period)
                .filter(pack_models.Crime_count_period.Crime_count_period.YR == YR)
                .filter(
                    pack_models.Crime_count_period.Crime_count_period.period == period
                )
                .all()
            )
