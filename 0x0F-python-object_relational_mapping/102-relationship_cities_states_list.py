#!/usr/bin/python3
"""Module for print states
"""


from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':
    eng_creation = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
    engine = create_engine(eng_creation)
    Session = sessionmaker(bind=engine)
    session = Session()
    Statex = session.query(State).order_by(State.id)
    Cityx = session.query(City).order_by(City.id)
    for instance1 in Cityx:
        for instance2 in Statex:
            if instance1.state_id == instance2.id:
                print(f'{instance1.id}: {instance1.name} -> {instance2.name}')

    session.close()
