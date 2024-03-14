#!/usr/bin/python3
"""class Region"""

from models.base_model import BaseModel, Base
from models.branch import Branch
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Region(Base, BaseModel):
    __tablename__ = "Region"

    id = Column(Integer, primary_key=True)
    regionName = Column(String(50))

    branches = relationship("Branch", backref='region')

    @property
    def branches(self):
        """ getter for list of branches related to the region"""
        branch_list = []
        from models import storage
        for branch in storage.all(Branch).values():
            if branch.regionId == self.id:
                branch_list.append(branch)
        return branch_list
