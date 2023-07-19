#!/usr/bin/python3
"""a script that lists all State objects from
the database
"""
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
if __name__ == '__main__':
    url = "mysql://{}:{}@localhost:3306/{}".format(sys.argv[1],
                                                   sys.argv[2], sys.argv[3])
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()
    for row in session.query(State)\
            .filter(State.name.like('%a%')).order_by(State.id):
        print("{}:".format(row.id), row.name)
