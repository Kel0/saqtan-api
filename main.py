from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from Database.schemas.cache import pack_schemas
from Database import database, services
from Dependecies import db


database.Database.Base.metadata.create_all(bind=database.Database.engine)

app = FastAPI()


@app.get("/api/v1/city_code/read", response_model=List[pack_schemas.City_code.CityCode])
def read_city_codes(db: Session = Depends(db.get_db)):
    city_codes = services.CityCode().get_city_codes(db=db)
    return city_codes

