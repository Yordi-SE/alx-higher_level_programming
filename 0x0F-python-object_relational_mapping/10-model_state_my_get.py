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
    row = session.query(State.id).filter_by(name=sys.argv[4]).all()
    if row == []:
        print("Not Found")
    else:
        print(row[0][0])
