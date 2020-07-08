from typing import Optional

from pydantic import BaseModel


class CrimeCounByTypesBase(BaseModel):
    yr: int
    crime_type: Optional[str]
    crime_count: int


class CrimeCounByTypesCreate(CrimeCounByTypesBase):
    pass


class CrimeCounByTypes(CrimeCounByTypesBase):
    id: int
    crime_code: int

    class Config:
        orm_mode = True
