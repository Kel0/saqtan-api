from pydantic import BaseModel


class CityCodeBase(BaseModel):
    city_code: int
    city_name: str
    type: str


class CityCodeCreate(CityCodeBase):
    pass


class CityCode(CityCodeBase):
    id: int

    class Config:
        orm_mode = True
