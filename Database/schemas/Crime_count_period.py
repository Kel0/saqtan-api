from pydantic import BaseModel


class CrimeCountPeriodBase(BaseModel):
    YR: int
    period: int
    crimes_count: int


class CrimeCountPeriodCreate(CrimeCountPeriodBase):
    pass


class CrimeCountPeriod(CrimeCountPeriodBase):
    id: int

    class Config:
        orm_mode = True
