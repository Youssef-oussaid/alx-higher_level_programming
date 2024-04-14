#!/usr/bin/python3
"""Lists states ordered"""


from sys import argv
from sqlalchemy import engine_create, MetaData
from model_state import Base, State


engine = engine_create(f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}")

metadata = MetaData()
metadata.reflect(bind=engine)

states = 'states'
table = metadata.tables[states]

for column in table.columns:
    print(column.name)