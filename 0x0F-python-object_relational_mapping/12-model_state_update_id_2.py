#!/usr/bin/python3
"""Change name of State object with id=2 in database
Takes three arguments
    mysql username
    mysql password
    database name
Connects to host localhost and default port (3306)
"""
if __name__ == "__main__":
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from sys import argv
    Session = sessionmaker()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    session.commit()
    session.close()
