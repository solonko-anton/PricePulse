from sqlmodel import create_engine, SQLModel, Session
from config.database.db_config import settings_db

engine = create_engine(settings_db, echo=True)

def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)

def dbsave(data: list) -> None:
    with Session(engine) as session:
        session.add_all(data)
        session.commit()
