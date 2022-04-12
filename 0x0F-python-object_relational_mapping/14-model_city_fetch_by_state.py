#!/usr/bin/python3
""" Deletes all State objects from the database that contain 'a'
using SQLAlchemy and importing State and Base from model_state
"""
import sys
from model_state import Base, State
from model_city import City
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

    st_ct = session.query(State, City).filter(State.id == City.state_id).all()
    for state, city in st_ct:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
