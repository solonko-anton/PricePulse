from sqlmodel import create_engine, SQLModel, Session
from config.database.db_config import settings_db

engine = create_engine(settings_db, echo=True)

# def create_db_and_tables() -> None:      # without docker
#     SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session