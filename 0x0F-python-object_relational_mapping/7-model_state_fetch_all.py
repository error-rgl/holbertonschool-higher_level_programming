#!/usr/bin/python3
""" Lists all State objects from the database in ascending order
using SQLAlchemy and importing State and Base from model_state
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker


if __name__ = '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
