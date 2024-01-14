#!/usr/bin/python3
"""adds the State object “Louisiana” to the database hbtn_0e_6_usa"""

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

    """create the new object"""
    new = State(name='Louisiana')

    """add the new to the session"""
    ses.add(new)

    """commit the changes to database"""
    ses.commit()

    new_st = ses.query(State).filter(State.name == 'Louisiana').first()
    print("{}".format(new_st.id))
    ses.close()

