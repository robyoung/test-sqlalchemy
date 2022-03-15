from sqlalchemy import BigInteger, Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Person(Base):
    __tablename__ = "person"

    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
