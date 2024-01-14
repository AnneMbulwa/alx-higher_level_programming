#!/usr/bin/python3
"""deletes all State objects with a name containing the letter a
from hbtn_0e_6_usa db"""

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    ses = Session()

    state = ses.query(State).filter(State.name.like('%a%')).first()
    if stat in state:
        ses.delete(stat)

    ses.commit()
    ses.close()
