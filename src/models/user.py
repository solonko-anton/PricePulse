from sqlmodel import SQLModel, Field, create_engine


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str