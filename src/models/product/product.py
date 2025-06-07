from pydantic import field_validator
from sqlmodel import SQLModel, Field


class Product(SQLModel, table=True):
    name: str = Field()
    price: float = Field()
    description: str = Field(default=None)


