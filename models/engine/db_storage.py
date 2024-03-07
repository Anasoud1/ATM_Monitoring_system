#!/usr/bin/python3
"""
        storage data engine
        MySQL DataBase
"""

import models
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
'''
from models.base_model import Base
from models.atm import Atm
from models.atmdevice import AtmDevice
from models.branch import Branch
from models.device import Device
from models.event import Event
from models.region import Region
from models.electrinicjournal import ElectronicJournal
from models.transaction import Transaction
from models.group import Group
'''
from atm_data_seeder import Base, Region, Branch, Group, Device, ATM, AtmDevice, ElectronicJournal, Event, Transaction


class DBStorage:
    """
    mysql database engine class orm
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        initialization...
        """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
             getenv("DB_USER"),
                getenv("DB_PASSWORD"),
                getenv("DB_HOST"),
                getenv("DB_NAME"),
            ),
            pool_pre_ping=True, 
        )

    def all(self, cls=None):
        """
        query on the current database session
        all objects depending of the class name (argument cls)
        """
        obj_dict = {}
        objs_list = [Group, Transaction, ElectronicJournal, Region, Event, Device, Branch, AtmDevice, ATM]
        dict_id = {'Group': 'groupId', 'Transaction': 'transactionId', 'ElectronicJournal': 'ejId', 'Region': 'id', 'Event': 'eventId', 'Device': 'deviceId', 'Branch': 'branchId', 'ATM': 'atmId'}
        objs = []
        if cls is not None:
            objs.extend(self.__session.query(cls).all())
        else:
            for table_name in objs_list:
                objs.extend(self.__session.query(table_name).all())
        for obj in objs:
            key = f"{obj.__class__.__name__}.{getattr(obj, dict_id[cls.__name__])}"
            obj_dict[key] = obj
        return obj_dict
    
    def new(self, obj):
        """
        add the object to the current database session.
        """
        self.__session.add(obj)
        self.__session.flush()

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database and the current database session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        close a connected  session
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        self.__session.close()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        objs_list = [Group, Transaction, ElectronicJournal, Region, Event, Device, Branch, AtmDevice, ATM]
        dict_id = {'Group': 'groupId', 'Transaction': 'transactionId', 'ElectronicJournal': 'ejId', 'Region': 'id', 'Event': 'eventId', 'Device': 'deviceId', 'Branch': 'branchId', 'ATM': 'atmId'}
        if cls not in objs_list:
            return None
        dict_obj = models.storage.all(cls)
        for k, v in dict_obj.items():
            if str(getattr(v, dict_id[cls.__name__])) == id:
                return v
        return None
