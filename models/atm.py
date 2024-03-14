#!/usr/bin/python3
"""class atm"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Enum, Integer, Float, DECIMAL
from sqlalchemy.orm import relationship


class ATM(Base, BaseModel):
    __tablename__ = "ATM"

    atmId = Column(Integer, primary_key=True)
    atmName = Column(String(45))
    networkAddress = Column(String(45))
    latitude = Column(Float)
    longitude = Column(Float)
    timezone = Column(String(100))
    subnet = Column(String(45))
    branchId = Column(Integer, ForeignKey('Branch.branchId'))
    groupId = Column(Integer, ForeignKey('Group.groupId'))
    status = Column(String(20), default="Online")
    cash_level = Column(DECIMAL(10, 2))
    last_cash_replenishment = Column(String(100))
    software_version = Column(String(50))
    uptime = Column(Integer)

    #add relationship with electronicJournal
    eljournals = relationship("ElectronicJournal", backref="atm_elj") 

    # Relationship with AtmDevice
    devices = relationship("AtmDevice", backref="atm")
