#!/usr/bin/python3
"""Module for print states"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == '__main__':
    eng_creation = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
    engine = create_engine(eng_creation)
    Session = sessionmaker(bind=engine)
    session = Session()

    instance = session.query(State).filter(State.name.like(argv[4])).first()
    if instance:
        print(f'{instance.id}')
    else:
        print('Not found')

    session.close()
