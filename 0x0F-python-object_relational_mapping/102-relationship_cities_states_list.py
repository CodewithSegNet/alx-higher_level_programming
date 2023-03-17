#!/usr/bin/python3
"""Lists all City objects with respective State
Takes three arguments
    mysql username
    mysql password
    database name
Connects to host localhost and default port (3306)
"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import Base, State
    from relationship_city import City
    from sys import argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    session = Session(bind=engine)
    for city, state in session.query(City, State).filter(
            State.id == City.state_id).order_by(City.id).all():
        print("{:d}: {} -> {}".format(city.id, city.name, state.name))
    session.close()
