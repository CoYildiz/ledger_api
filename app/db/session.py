from app.core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(settings.database_url)

SessionLocal = sessionmaker(bind=engine, autoflush=True)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

