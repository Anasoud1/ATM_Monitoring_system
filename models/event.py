#!/usr/bin/python3
"""class event"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Enum, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Event(Base, BaseModel):
    __tablename__ = "Event"

    eventId = Column(Integer, primary_key=True)
    eventName = Column(String(100), nullable=False, unique=True)
    eventLevel = Column(Enum("INFO", "WARNING", "ERROR", "CRITICAL"),
                        nullable=False)
    ejId = Column(Integer, ForeignKey("ElectronicJournal.ejId"))
