from sqlmodel import SQLModel, Session, create_engine
from decouple import config

DB_URL = config("DB_URL")

engine = create_engine(DB_URL)

def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session