#!/usr/bin/python3
"""prints the State object with the name passed as
argument from the database hbtn_0e_6_usa"""

from sys import argv
from sqlalchemy.orm import session
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    seas = Session()

    stat = seas.query(State).filter(State.name == sys.argv[4].first())
    for stat:
        print("{}".format(stat.id))
    else:
        print("Not Foumd")

    seas.close()
