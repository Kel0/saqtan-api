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
