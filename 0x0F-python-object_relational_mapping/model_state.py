#!/usr/bin/python3
""" Defines State class that inherits from Base = declarative_base()
and links to MySQL table states using SQLAlchemy
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mydata = MetaData()
Base = declarative_base(metadata=mydata)


class State(Base):
    """ Defines State class that links to MySQL table 'states'
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
