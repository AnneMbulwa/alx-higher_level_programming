#!/usr/bin/pyhton3
"""lists all State objects that contain letter a from database hbtn_0e_6_us"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = session(bind=engine)
    session = Session()

    first = session.query(State).filter(State.name.like('%a%')).order_by(State.id)

    for row in first:
        print ("{}: {}".format(first.id, first.name))

    session.close()
