from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from Database import database
from Database.schemas.cache import pack_schemas
from Dependencies import get_db
from utils.cache import pack_utils

database.Database.Base.metadata.create_all(bind=database.Database.engine)

app = FastAPI()


@app.get("/api/v1/city_code/read", response_model=List[pack_schemas.City_code.CityCode])
def read_city_codes(db: Session = Depends(get_db.get_db), type: str = "city"):
    city_codes = pack_utils.City_code_utils.CityCode().get_city_codes(db=db, type=type)
    return city_codes


@app.get(
    "/api/v1/crime_count/read", response_model=List[pack_schemas.Crime_count.CrimeCount]
)
def read_crimes_count(db: Session = Depends(get_db.get_db), YR: int = 0):
    crimes_count = pack_utils.Crime_count_utils.CrimeCount().get_crimes_count(
        db=db, YR=YR
    )
    return crimes_count


@app.get(
    "/api/v1/crime_count/by_period",
    response_model=List[pack_schemas.Crime_count_period.CrimeCountPeriod],
)
def read_crimes_count_periods(
    db: Session = Depends(get_db.get_db), YR: int = 0, period: int = 0
):
    crimes_count_by_periods = pack_utils.Crime_count_period_utils.CrimeCountPeriods().get_crime_count_by_periods(
        db=db, YR=YR, period=period
    )
    return crimes_count_by_periods


@app.get(
    "/api/v1/crime_count/cities",
    response_model=List[pack_schemas.Crime_count_city.CrimeCountCity],
)
def read_count_crimes_cities(db: Session = Depends(get_db.get_db)):
    crimes_count_by_cities = pack_utils.Crime_count_city_utils.CrimeCountCity().get_crimes_count_by_cities(
        db=db
    )
    return crimes_count_by_cities


@app.get(
    "/api/v1/crime_codes/read", response_model=List[pack_schemas.Crime_code.CrimeCode]
)
def read_crime_codes(db: Session = Depends(get_db.get_db)):
    crime_codes = pack_utils.Crime_code_utils.CrimeCode().get_crime_codes(db=db)
    return crime_codes


@app.get(
    "/api/v1/crime_count/by_yr_types",
    response_model=List[pack_schemas.Crime_count_by_types.CrimeCounByTypes],
)
def read_crime_count_types(
    db: Session = Depends(get_db.get_db), yr: int = 0, crime_code: int = 0
):
    crimes_with_type = pack_utils.Crime_count_by_types.CrimeCountByTypes().get_crimes_types_by_yr(
        db=db, yr=yr, crime_code=crime_code
    )
    return crimes_with_type
