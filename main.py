from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from Database import database
from Database.schemas.cache import pack_schemas
from Dependencies import get_db
from utils import City_code_utils

database.Database.Base.metadata.create_all(bind=database.Database.engine)

app = FastAPI()


@app.get("/api/v1/city_code/read", response_model=List[pack_schemas.City_code.CityCode])
def read_city_codes(db: Session = Depends(get_db.get_db), type: str = "city"):
    city_codes = City_code_utils.CityCode().get_city_codes(db=db, type=type)
    return city_codes
