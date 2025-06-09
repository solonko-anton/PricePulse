from sqlmodel import create_engine, SQLModel, Session
from src.config.database.db_config import settings_db

engine = create_engine(str(settings_db.database_url), echo=True)

def create_db_and_tables() -> None:      # without docker
    SQLModel.metadata.create_all(engine, echo=True)

def get_session():
    with Session(engine) as session:
        yield session