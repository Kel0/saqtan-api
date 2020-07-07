from dataclasses import dataclass

import pymysql
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.config import DATABASE_URL


@dataclass
class Database:
    pymysql.install_as_MySQLdb()

    SQLALCHEMY_DATABASE_URL: str = DATABASE_URL

    engine: sqlalchemy.engine.base.Engine = create_engine(SQLALCHEMY_DATABASE_URL)
    SessionLocal: sqlalchemy.orm.session.Session = sessionmaker(
        autocommit=False, autoflush=False, bind=engine
    )

    Base = declarative_base()
