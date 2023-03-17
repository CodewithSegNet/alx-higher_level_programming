#!/usr/bin/python3
"""Script prints State object with the name passed as argument
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
    instances = session.query(State).filter(State.name == argv[4]).all()
    if instances:
        for instance in instances:
            if instance.name == argv[4]:
                print("{}".format(instance.id))
    else:
        print("Not found")
    session.close()
