from pydantic import BaseModel


class CrimeCountBase(BaseModel):
    YR: int
    crimes_count: int
    before_perc: float


class CrimeCountCreate(CrimeCountBase):
    pass


class CrimeCount(CrimeCountBase):
    id: int

    class Config:
        orm_mode = True
