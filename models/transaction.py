#!/usr/bin/python3
"""class transaction"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer


class Transaction(Base, BaseModel):
    __tablename__ = "Transaction"

    transactionId = Column(Integer, primary_key=True)
    transactionType = Column(String(45), nullable=False)
    transactionDetail = Column(String(1000))
    ejId = Column(Integer, ForeignKey("ElectronicJournal.ejId"))
