#!/usr/bin/python3
"""class AtmDevice"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class AtmDevice(Base, BaseModel):
    __tablename__ = "AtmDevice"

    atm_id = Column(Integer, ForeignKey('ATM.atmId'), primary_key=True)
    atm = relationship("ATM")
    device_Id = Column(Integer, ForeignKey('Device.deviceId'), primary_key=True)
    device = relationship("Device")

    deviceStatus = Column(String(50))
