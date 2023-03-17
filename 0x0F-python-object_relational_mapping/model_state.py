#!/usr/bin/python3
"""File contains class State and instance Base = declarative_base()"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class inherits from Base
    Links to MySQL table 'states'
    Attributes:
        id: column of auto-generated unique integer, can't be NULL, primary key
        name: column of string with max 128 characters, can't be NULL
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
