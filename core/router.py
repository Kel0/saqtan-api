from typing import List

from Dependencies import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils.cache import pack_utils

from Database import database
from Database.schemas.cache import pack_schemas

database.Database.Base.metadata.create_all(bind=database.Database.engine)

router = APIRouter()


@router.get(
    "/api/v1/city_code/read",
    response_model=List[pack_schemas.City_code.CityCode],
    tags=["city_code"],
)
def read_city_codes(db: Session = Depends(get_db.get_db), type: str = "city"):
    city_codes = pack_utils.City_code_utils.CityCode().get_city_codes(db=db, type=type)
    return city_codes


@router.get(
    "/api/v1/crime_count/read",
    response_model=List[pack_schemas.Crime_count.CrimeCount],
    tags=["crime_count"],
)
def read_crimes_count(db: Session = Depends(get_db.get_db), YR: int = 0):
    crimes_count = pack_utils.Crime_count_utils.CrimeCount().get_crimes_count(
        db=db, YR=YR
    )
    return crimes_count


@router.get(
    "/api/v1/crime_count/by_period",
    response_model=List[pack_schemas.Crime_count_period.CrimeCountPeriod],
    tags=["crime_count"],
)
def read_crimes_count_periods(
    db: Session = Depends(get_db.get_db), YR: int = 0, period: int = 0
):
    crimes_count_by_periods = pack_utils.Crime_count_period_utils.CrimeCountPeriods().get_crime_count_by_periods(
        db=db, YR=YR, period=period
    )
    return crimes_count_by_periods


@router.get(
    "/api/v1/crime_count/cities",
    response_model=List[pack_schemas.Crime_count_city.CrimeCountCity],
    tags=["crime_count"],
)
def read_count_crimes_cities(db: Session = Depends(get_db.get_db)):
    crimes_count_by_cities = pack_utils.Crime_count_city_utils.CrimeCountCity().get_crimes_count_by_cities(
        db=db
    )
    return crimes_count_by_cities


@router.get(
    "/api/v1/crime_codes/read",
    response_model=List[pack_schemas.Crime_code.CrimeCode],
    tags=["crime_count"],
)
def read_crime_codes(db: Session = Depends(get_db.get_db)):
    crime_codes = pack_utils.Crime_code_utils.CrimeCode().get_crime_codes(db=db)
    return crime_codes


@router.get(
    "/api/v1/crime_count/by_yr_types",
    response_model=List[pack_schemas.Crime_count_by_types.CrimeCounByTypes],
    tags=["crime_count"],
)
def read_crime_count_types(
    db: Session = Depends(get_db.get_db), yr: int = 0, crime_code: int = 0
):
    crimes_with_type = pack_utils.Crime_count_by_types.CrimeCountByTypes().get_crimes_types_by_yr(
        db=db, yr=yr, crime_code=crime_code
    )
    return crimes_with_type


@router.get(
    "/api/v1/crime/read", response_model=List[pack_schemas.Crime.Crime], tags=["crime"]
)
def crime_read(
    db: Session = Depends(get_db.get_db),
    YR: int = 2016,
    PERIOD: int = 1,
    CITY_CODE: int = 1971,
    DAT_VOZB: int = 0,
    DAT_SOVER: int = 0,
    STAT: str = 0,
):
    crime_features = pack_utils.Crime_utils.CrimeFeatures().crime_details_read(
        db=db,
        YR=YR,
        PERIOD=PERIOD,
        CITY_CODE=CITY_CODE,
        DAT_VOZB=DAT_VOZB,
        DAT_SOVER=DAT_SOVER,
        STAT=STAT,
    )
    return crime_features
