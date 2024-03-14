#!/usr/bin/python3
"""class group"""

from models.base_model import BaseModel, Base
from models.atm import ATM
from sqlalchemy import Column, String, ForeignKey, Enum, Integer
from sqlalchemy.orm import relationship


class Group(Base, BaseModel):
    __tablename__ = "Group"

    groupId = Column(Integer, primary_key=True)
    groupName = Column(String(100))
    groupDescription = Column(String(5000))
    groupType = Column(Enum("Static", "Dynamic"))

    atms_g = relationship("ATM", secondary="group_atm", backref="groups")

    @property
    def atms_g(self):
        """ getter for list of atms related to the group"""
        atm_list = []
        from models import storage
        for atm in storage.all(ATM).values():
            if atm.groupId == self.groupId:
                atm_list.append(atm)
        return atm_list
