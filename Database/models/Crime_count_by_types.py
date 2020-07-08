from sqlalchemy import Column, ForeignKey, Integer, String

from ..database import Database


class Crime_count_by_types(Database.Base):
    __tablename__ = "crime_counts_by_types"

    id = Column(Integer, primary_key=True, index=True)
    yr = Column(Integer, index=True)
    crime_type = Column(String, index=True)
    crime_count = Column(Integer, index=True)

    crime_code = Column(Integer, ForeignKey("crime_codes.crime_code"))
