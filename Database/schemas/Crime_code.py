from pydantic import BaseModel


class CrimeCodeBase(BaseModel):
    crime_code: int
    crime_desc: str


class CrimeCodeCreate(CrimeCodeBase):
    pass


class CrimeCode(CrimeCodeBase):
    id: int

    class Config:
        orm_mode = True
