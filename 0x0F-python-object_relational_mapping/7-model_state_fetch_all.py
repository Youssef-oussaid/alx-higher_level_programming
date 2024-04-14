#!/usr/bin/python3
"""Lists states ordered"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (engine_create)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = engine_create(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(argv[1], argv[2],
                argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id).all():
            print("{}: {}".format(state.id, state.name))
    session.close()
