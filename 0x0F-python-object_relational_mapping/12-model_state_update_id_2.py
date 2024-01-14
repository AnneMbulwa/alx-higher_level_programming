#!/usr/bin/python3
"""changes the name of a State object from the database hbtn_0e_6_usa"""

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

    stat = ses.query(State).filter(State.id == 2).first()

    stat.name = "New Maexico"
    ses.commit()
    ses.close()
