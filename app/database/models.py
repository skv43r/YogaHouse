from sqlmodel import SQLModel, Field
from datetime import datetime

class IndividualSpecialists(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str | None = Field(default=None)
    photo: str | None = Field(default=None)

class IndividualServices(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str | None = Field(default=None)
    price: int | None = Field(default=None, index=True)
    photo: str | None = Field(default=None)

class Massage(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str | None = Field(default=None)
    price: int | None = Field(default=None, index=True)

class GroupSpecialists(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str | None = Field(default=None)
    photo: str | None = Field(default=None)

class GroupServices(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str | None = Field(default=None)
    price: int | None = Field(default=None, index=True)
    photo: str | None = Field(default=None)

class Booking(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(index=True)
    service: str = Field(nullable=False)
    master: str = Field(nullable=False)
    date: str = Field(nullable=False)
    time: str = Field(nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)