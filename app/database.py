from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 


engine = create_engine("sqlite:///db.sqlite3")
SessionLocal = sessionmaker(bind=engine)


@contextmanager
def get_db():
    try:
        db = SessionLocal()
        yield db 
    finally:
        db.close()

