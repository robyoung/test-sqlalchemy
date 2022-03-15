from datetime import date

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker
from sqlalchemy.sql.expression import text

import models

session: Session = scoped_session(sessionmaker())


def pg_url():
    return "postgresql://postgres:postgres@db:5432/postgres"


def init_session():
    engine = create_engine(pg_url())
    session.configure(bind=engine)


def create_tables():
    session.execute("""CREATE TABLE names (name text)""")
    session.commit()
    models.Base.metadata.create_all(bind=session.bind)


def create_records():
    session.add(models.Person(name="Rob", date_of_birth=date(1980, 8, 22)))
    session.add(models.Person(name="Old Rob", date_of_birth=date(1960, 8, 22)))
    session.commit()


def query_with_age():
    session.query(models.Person, text("age")).from_statement(
        text("SELECT person.*, age(date_of_birth) as age FROM person")
    ).all()
