#!/usr/bin/python3
""" Defines City class that inherits from Base = declarative_base()
and links to MySQL table cities using SQLAlchemy
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """ Class that defines each city
    """
    __tablename__ = 'Cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
