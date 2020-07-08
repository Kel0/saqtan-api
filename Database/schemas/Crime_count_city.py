from pydantic import BaseModel


class CrimeCountCityBase(BaseModel):
    year_2016: int
    year_2017: int
    year_2018: int
    year_2019: int
    year_2020: int


class CrimeCountCityCreate(CrimeCountCityBase):
    pass


class CrimeCountCity(CrimeCountCityBase):
    id: int
    city_code: int

    class Config:
        orm_mode = True
