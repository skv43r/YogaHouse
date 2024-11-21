from sqlmodel import SQLModel, Field

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