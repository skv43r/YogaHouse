from typing import Generator
from sqlmodel import SQLModel, Session, create_engine
from config import settings

class Database:
    def __init__(self, database_url: str, echo: bool = True) -> None:
        self.engine = create_engine(database_url, echo=echo)

    def create_db_and_tables(self) -> None:
        SQLModel.metadata.create_all(self.engine)
    
    def get_session(self) -> Generator[Session, None, None]:
        with Session(self.engine) as session:
            yield session

db = Database(database_url=settings.DATABASE_URL)