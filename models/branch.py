#!/usr/bin/python3
"""class branch"""

from models.base_model import BaseModel, Base
from models.atm import ATM
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship



class Branch(Base, BaseModel):
    __tablename__ = "Branch"

    branchId = Column(Integer, primary_key=True)
    branchName = Column(String(50))
    regionId = Column(Integer, ForeignKey('Region.id'))

    atms_b = relationship("ATM", backref='branch')

    @property
    def atms_b(self):
        """ getter for list of atms related to the branch"""
        atm_list = []
        from models import storage
        for atm in storage.all(ATM).values():
            if atm.branchId == self.branchId:
                atm_list.append(atm)
        return atm_list
