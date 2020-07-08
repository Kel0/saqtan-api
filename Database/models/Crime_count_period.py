from sqlalchemy import Column, Integer

from ..database import Database


class Crime_count_period(Database.Base):
    __tablename__ = "crimes_count_periods"

    id = Column(Integer, primary_key=True, index=True)
    YR = Column(Integer, index=True)
    period = Column(Integer, index=True)
    crimes_count = Column(Integer, index=True)
