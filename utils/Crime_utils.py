from loguru import logger
from sqlalchemy.orm import Session

from Database.models.cache import pack_models


class CrimeFeatures(object):
    @logger.catch
    def crime_details_read(
        self,
        db: Session,
        YR: int,
        PERIOD: int,
        CITY_CODE: int,
        DAT_VOZB: int,
        DAT_SOVER: int,
        STAT: str,
    ):
        if DAT_VOZB == 0 and DAT_SOVER == 0 and STAT == 0:
            return (
                db.query(pack_models.Crime.Crime)
                .filter(pack_models.Crime.Crime.YR == YR)
                .filter(pack_models.Crime.Crime.CITY_CODE == CITY_CODE)
                .filter(pack_models.Crime.Crime.PERIOD == PERIOD)
                .all()
            )

        if DAT_VOZB == 0 and DAT_SOVER == 0:
            return (
                db.query(pack_models.Crime.Crime)
                .filter(pack_models.Crime.Crime.YR == YR)
                .filter(pack_models.Crime.Crime.CITY_CODE == CITY_CODE)
                .filter(pack_models.Crime.Crime.PERIOD == PERIOD)
                .filter(pack_models.Crime.Crime.STAT == STAT)
                .all()
            )

        if DAT_VOZB == 0:
            return (
                db.query(pack_models.Crime.Crime)
                .filter(pack_models.Crime.Crime.YR == YR)
                .filter(pack_models.Crime.Crime.CITY_CODE == CITY_CODE)
                .filter(pack_models.Crime.Crime.PERIOD == PERIOD)
                .filter(pack_models.Crime.Crime.STAT == STAT)
                .filter(pack_models.Crime.Crime.DAT_SOVER == DAT_SOVER)
                .all()
            )

        return (
            db.query(pack_models.Crime.Crime)
            .filter(pack_models.Crime.Crime.YR == YR)
            .filter(pack_models.Crime.Crime.CITY_CODE == CITY_CODE)
            .filter(pack_models.Crime.Crime.PERIOD == PERIOD)
            .filter(pack_models.Crime.Crime.STAT == STAT)
            .filter(pack_models.Crime.Crime.DAT_SOVER == DAT_SOVER)
            .filter(pack_models.Crime.Crime.DAT_VOZB == DAT_VOZB)
            .all()
        )
