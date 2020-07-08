from loguru import logger
from sqlalchemy.orm import Session

from Database.models.cache import pack_models


class CrimeCountByTypes(object):
    @logger.catch
    def get_crimes_types_by_yr(self, db: Session, yr: int, crime_code: int):
        if yr > 0 and crime_code == 0:
            return (
                db.query(pack_models.Crime_count_by_types.Crime_count_by_types)
                .filter(pack_models.Crime_count_by_types.Crime_count_by_types.yr == yr)
                .all()
            )

        if yr == 0 and crime_code > 0:
            return (
                db.query(pack_models.Crime_count_by_types.Crime_count_by_types)
                .filter(
                    pack_models.Crime_count_by_types.Crime_count_by_types.crime_code
                    == crime_code
                )
                .all()
            )

        if yr == 0 and crime_code == 0:
            return db.query(pack_models.Crime_count_by_types.Crime_count_by_types).all()

        if yr != 0 and crime_code != 0:
            return (
                db.query(pack_models.Crime_count_by_types.Crime_count_by_types)
                .filter(pack_models.Crime_count_by_types.Crime_count_by_types.yr == yr)
                .filter(
                    pack_models.Crime_count_by_types.Crime_count_by_types.crime_code
                    == crime_code
                )
                .all()
            )
