#!/usr/bin/python3
"""class AtmDevice"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class AtmDevice(Base, BaseModel):
    __tablename__ = "AtmDevice"

    id = Column(Integer, primary_key=True, autoincrement=True)
    atmId = Column(Integer, ForeignKey('ATM.atmId'), primary_key=True)
    deviceId = Column(Integer, ForeignKey('Device.deviceId'), primary_key=True)
    deviceStatus = Column(String(20))
