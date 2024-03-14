#!/usr/bin/python3
"""ATMCassette Class"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class ATMCassette(Base):
    __tablename__ = 'atm_cassettes'

    id = Column(Integer, primary_key=True)
    cassette_num = Colum(Integer)
    denomination = Column(Integer)
    cassete_type = Columm(String(50))
    num_bills = Column(Integer)
