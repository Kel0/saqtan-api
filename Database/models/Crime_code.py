from sqlalchemy import Column, Integer, String

from ..database import Database


class Crime_code(Database.Base):
    __tablename__ = "crime_codes"

    id = Column(Integer, primary_key=True, index=True)
    crime_code = Column(Integer, index=True)
    crime_desc = Column(String, index=True)
