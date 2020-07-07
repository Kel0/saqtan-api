from sqlalchemy import Column, Float, Integer

from ..database import Database


class Crime_count(Database.Base):
    __tablename__ = "crimes_count"

    id = Column(Integer, primary_key=True, index=True)
    YR = Column(Integer, index=True)
    crimes_count = Column(Integer, index=True)
    before_perc = Column(Float, index=True)
