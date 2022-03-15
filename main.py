from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from session import app

print(app)
session = scoped_session(sessionmaker())


def pg_url():
    return "postgresql://postgres:postgres@db:5432/postgres"


def init_session():
    engine = create_engine(pg_url())
    session.configure(bind=engine)


def create_table():
    session.execute("""CREATE TABLE names (name text)""")
