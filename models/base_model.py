#!/usr/bin/python3
"""
Contains class BaseModel
"""
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel():
    def to_dict(self):
        """
        returns a dictionary containing all keys/values of the instance"
        """
        new_dict = self.__dict__.copy()
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict
