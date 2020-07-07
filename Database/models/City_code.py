from sqlalchemy import Column, Integer, String

from ..database import Database


class City_code(Database.Base):
    __tablename__ = "city_codes"

    id = Column(Integer, primary_key=True, index=True)
    city_code = Column(Integer, index=True)
    city_name = Column(String, index=True)
    type = Column(String, index=True)
