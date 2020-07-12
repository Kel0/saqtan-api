from typing import Union

from pydantic import BaseModel


class CrimeBase(BaseModel):
    OBJECTID: int
    YR: int
    PERIOD: int
    CRIME_CODE: int
    TIME_PERIOD: int
    HARD_CODE: str
    UD: str
    ORGAN: str
    DAT_VOZB: int
    DAT_SOVER: int
    STAT: str
    DAT_VOZB_STR: str
    DAT_SOVER_STR: str
    TZ1ID: str
    REG_CODE: str
    CITY_CODE: str
    STATUS: int
    ORG_CODE: str
    ENTRYDATE: Union[int, None]
    FZ1R18P5: Union[str, None]
    FZ1R18P6: Union[str, None]
    ORGAN_KZ: str
    ORGAN_EN: str
    FE1R29P1_ID: str
    FE1R32P1: Union[str, None]
    x_geo: str
    y_geo: str


class CrimeCreate(CrimeBase):
    pass


class Crime(CrimeBase):
    id: int

    class Config:
        orm_mode = True
