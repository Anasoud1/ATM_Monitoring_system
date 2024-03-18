#!/usr/bin/python3
"""class AtmDevice"""

from models.base_model import BaseModel, Base
from models.atm_cassette import ATMCassette
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class AtmDevice(Base, BaseModel):
    __tablename__ = "AtmDevice"

    id = Column(Integer, primary_key=True, autoincrement=True)
    atmId = Column(Integer, ForeignKey('ATM.atmId'), primary_key=True)
    #atm = relationship("ATM")
    deviceId = Column(Integer, ForeignKey('Device.deviceId'), primary_key=True)
    #device = relationship("Device")

    deviceStatus = Column(String(50))
    
    cassettes = relationship(ATMCassette, backref="cassette")  

    @property
    def cassettes(self):
        list_cass = []
        from models import storage
        for cassette in storage.all(ATMCassette).values():
            if cassette.dispenserId == self.id:
                list_cass.append(cassette)
        return list_cass

    def calculate_cash(self):
        """calculate level of cash in atm"""
        total_cash = 0
        for cass in self.cassettes:
            total_cash += cass.denomination * cass.num_bills 

        return total_cash
