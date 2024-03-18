#!/usr/bin/python3
"""ATMCassette Class"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class ATMCassette(Base, BaseModel):
    __tablename__ = 'atm_cassettes'

    id = Column(Integer, primary_key=True)
    cassette_num = Column(Integer)
    denomination = Column(Integer)
    cassete_type = Column(String(50))
    num_bills = Column(Integer)

    dispenserId = Column(Integer, ForeignKey('AtmDevice.id'))
