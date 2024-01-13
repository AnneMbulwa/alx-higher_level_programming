#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa
"""

from model_state import Base, State
import sys
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    stats = session.query(State).order_by(State.id).all()

    for state in stats:
        print("{}: {}".format(state.id, state.name))
