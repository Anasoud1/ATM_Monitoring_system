#!/usr/bin/python3
"""class ElectronicJournal"""

from models.base_model import BaseModel, Base
from models.event import Event
from models.transaction import Transaction
from sqlalchemy import Column, String, ForeignKey, Enum, Integer, Float
from sqlalchemy.orm import relationship


class ElectronicJournal(Base, BaseModel):
    __tablename__ = "ElectronicJournal"

    ejId = Column(Integer, primary_key=True)
    ejData = Column(String(1000), nullable=False)
    atmId = Column(Integer, ForeignKey("ATM.atmId"), nullable=False)
    timestamp = Column(String(100), nullable=False)

    #add relationship with Event table
    events = relationship("Event", backref="elj")
    
    #add relationship with Transaction table
    transactions = relationship("Transaction", backref="elj_t")

    @property
    def events(self):
        """ getter for list of events related to the elctronic journal"""
        event_list = []
        from models import storage
        for event in storage.all(Event).values():
            if event.ejId == self.ejId:
                event_list.append(event)
        return event_list 

    @property
    def transactions(self):
        """ getter for list of transactions related to the elctronic journal"""
        transaction_list = []
        from models import storage
        for transaction in storage.all(Transaction).values():
            if transaction.ejId == self.ejId:
                transaction_list.append(transaction)
        return transaction_list
