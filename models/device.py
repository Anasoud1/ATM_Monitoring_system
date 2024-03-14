#!/usr/bin/python3
"""Device class"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Device(Base, BaseModel):
    __tablename__ = "Device"

    deviceId = Column(Integer, primary_key=True)
    deviceName = Column(String())

    atms_d = relationship("AtmDevice", backref="device")
