from sqlalchemy import Column, ForeignKey, Integer

from ..database import Database


class Crime_count_city(Database.Base):
    __tablename__ = "count_crimes_cities"

    id = Column(Integer, primary_key=True, index=True)
    city_code = Column(Integer, ForeignKey("city_codes.city_code"))
    year_2016 = Column(Integer, index=True)
    year_2017 = Column(Integer, index=True)
    year_2018 = Column(Integer, index=True)
    year_2019 = Column(Integer, index=True)
    year_2020 = Column(Integer, index=True)
