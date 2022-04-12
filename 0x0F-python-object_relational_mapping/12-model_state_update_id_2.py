#!/usr/bin/python3
"""
Adds the State object "Lousiana" to the database hbtn_0e_6_usa
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

    stateUpd = session.query(State).filter(State.id == 2).first()
    if stateUpd:
        stateUpd.name = 'New Mexico'
        session.commit()

    session.close()
