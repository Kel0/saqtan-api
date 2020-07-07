from Database.database import Database


def get_db():
    db = Database.SessionLocal()
    try:
        yield db
    finally:
        db.close()