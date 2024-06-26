#!/usr/bin/python3
"""insets a new state"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}',
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_to_update = session.query(State).filter(State.id == 2).all()
    if state_to_update:
        state_to_update[0].name = 'New Mexico'
    session.commit()
    session.close()
