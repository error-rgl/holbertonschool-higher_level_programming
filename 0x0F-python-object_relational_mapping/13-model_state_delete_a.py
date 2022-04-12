#!/usr/bin/python3
""" Deletes all State objects from the database that contain 'a'
using SQLAlchemy and importing State and Base from model_state
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    # Config engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query
    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        session.delete(state)
    session.commit()

    session.close()
