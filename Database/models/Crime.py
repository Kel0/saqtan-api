from sqlalchemy import Column, ForeignKey, Integer, String

from ..database import Database


class Crime(Database.Base):
    __tablename__ = "features"

    id = Column(Integer, primary_key=True, index=True)
    OBJECTID = Column(Integer, index=True)
    YR = Column(Integer, index=True)
    PERIOD = Column(Integer, index=True)
    CRIME_CODE = Column(Integer, index=True)
    TIME_PERIOD = Column(Integer, index=True)
    HARD_CODE = Column(String, index=True)
    UD = Column(String, index=True)
    ORGAN = Column(String, index=True)
    DAT_VOZB = Column(Integer, index=True)
    DAT_SOVER = Column(Integer, index=True)
    STAT = Column(String, index=True)
    DAT_VOZB_STR = Column(String, index=True)
    DAT_SOVER_STR = Column(String, index=True)
    TZ1ID = Column(String, index=True)
    REG_CODE = Column(String, index=True)
    STATUS = Column(Integer, index=True)
    ORG_CODE = Column(String, index=True)
    ENTRYDATE = Column(Integer, index=True, nullable=True)
    FZ1R18P5 = Column(String, index=True, nullable=True)
    FZ1R18P6 = Column(String, index=True, nullable=True)
    ORGAN_KZ = Column(String, index=True)
    ORGAN_EN = Column(String, index=True)
    FE1R29P1_ID = Column(String, index=True)
    FE1R32P1 = Column(String, index=True, nullable=True)
    x_geo = Column(String, index=True)
    y_geo = Column(String, index=True)

    CITY_CODE = Column(String, ForeignKey("city_codes.city_code"))
