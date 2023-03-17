#!/usr/bin/python3
"""Script prints all City objects
Takes three arguments
    mysql username
    mysql password
    database name
Connects to host localhost and default port (3306)
"""
if __name__ == "__main__":
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import aliased, sessionmaker
    from model_state import Base, State
    from model_city import City
    from sys import argv
    Session = sessionmaker()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    result = (session.query(State.name, City.id, City.name).filter(
        State.id == City.state_id).order_by(City.id).all())
    for i in result:
        print("{}: ({:d}) {}".format(i[0], i[1], i[2]))
    session.close()
