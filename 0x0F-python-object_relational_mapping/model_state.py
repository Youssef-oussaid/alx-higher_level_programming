#!/usr/bin/python3
"""class state def"""

from sys import argv
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'States'
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)


engine = create_engine(f'mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
Base.metadata.create_all(engine)
