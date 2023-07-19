#!/usr/bin/python3
"""a python file that contains the class
    definition of a State and an instance
    Base = declarative_base()
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, String, Column, Integer, ForeignKey
from model_state import State

Base = declarative_base()


class City(Base):
    """here we define body
    of the Model class State
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
                unique=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
