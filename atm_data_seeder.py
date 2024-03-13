import subprocess

try:
    subprocess.run(
        ["pip", "install", "sqlalchemy>=2.0.0"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
except subprocess.CalledProcessError as e:
    print("Error installing dependencies:", e)
    exit(1)

from sqlalchemy import (
    create_engine,
    MetaData,
    Column,
    Integer,
    String,
    Float,
    ForeignKey,
    DateTime,
    DECIMAL,
    Table,
    Enum,
)
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
import json
import os
import sys

# Replace with your actual database connection details
'''
connection_string = f"mysql+mysqldb://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASSWORD')}@{os.environ.get('DB_HOST')}/{os.environ.get('DB_NAME')}"

engine = create_engine(
    connection_string,
    pool_pre_ping=True,
)
'''
# declarative base class
class Base(DeclarativeBase):
    pass


class BaseModel():
    def to_dict(self):
        """
        returns a dictionary containing all keys/values of the instance"
        """
        new_dict = self.__dict__.copy()
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

# Define table models reflecting your database schema

class Region(Base, BaseModel):
    __tablename__ = "Region"

    id = Column(Integer, primary_key=True)
    regionName = Column(String(50))

    #add relationship with Branch
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


class Branch(Base, BaseModel):
    __tablename__ = "Branch"

    branchId = Column(Integer, primary_key=True)
    branchName = Column(String(50))
    regionId = Column(Integer, ForeignKey(Region.id))

    #add relationship with ATM
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

    '''
    def to_dict(self):
        """
        returns a dictionary containing all keys/values of the instance"
        """

        
        
        print("herrrre")
        new_dict = self.__dict__.copy()
        list_atms = []
        for atm in self.atms_b:
            list_atms.append(atm.to_dict())
        new_dict["atms"] = list_atms
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        print("*****", new_dict,"*****")
        return new_dict
    '''

    def __repr__(self):
        return f"Branch(branchId={self.branchId}, \
            branchName='{self.branchName}', \
                regionId={self.regionId})"


class Group(Base, BaseModel):
    __tablename__ = "Group"

    groupId = Column(Integer, primary_key=True)
    groupName = Column(String(100))
    groupDescription = Column(String(5000))
    groupType = Column(Enum("Static", "Dynamic"))

    #add relationship with ATM
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

    def __repr__(self):
        return (
            f"Group(groupId={self.groupId}, groupName='{self.groupName}', "
            f"groupDescription='{self.groupDescription}', atms={self.atms})"
        )


class Device(Base, BaseModel):
    __tablename__ = "Device"

    deviceId = Column(Integer, primary_key=True)
    deviceModel = Column(String(100))  # Adjust length as needed
    deviceManufacturer = Column(String(100))  # Adjust length as needed
    deviceSerialNumber = Column(String(50))  # Adjust length as needed

    # add relationship with AtmDevice
    atms_d = relationship("AtmDevice", backref="device")

    def __repr__(self):
        return f"Device(deviceId={self.deviceId}, \
                        deviceModel='{self.deviceModel}', \
                        deviceManufacturer='{self.deviceManufacturer}', \
                        deviceSerialNumber='{self.deviceSerialNumber}')"


class ATM(Base, BaseModel):
    __tablename__ = "ATM"

    atmId = Column(Integer, primary_key=True)
    atmName = Column(String(45))
    networkAddress = Column(String(45))
    latitude = Column(Float)
    longitude = Column(Float)
    timezone = Column(String(100))
    subnet = Column(String(45))
    branchId = Column(Integer, ForeignKey(Branch.branchId))
    groupId = Column(Integer, ForeignKey(Group.groupId))
    status = Column(String(20), default="Online")
    cash_level = Column(DECIMAL(10, 2))
    last_cash_replenishment = Column(String(100))
    software_version = Column(String(50))
    uptime = Column(Integer)

    #add relationship with electronicJournal
    eljournals = relationship("ElectronicJournal", backref="atm_elj") 

    # Relationship with AtmDevice
    devices = relationship("AtmDevice", backref="atm")
    

    def __repr__(self):
        return f"ATM(atmId={self.atmId}, \
                atmName='{self.atmName}', \
                branchId={self.branchId}, \
                groupId={self.groupId})"


# Define the association table for the many-to-many relationship
group_atm = Table(
    "group_atm",
    Base.metadata,
    Column("groupId", Integer, ForeignKey("Group.groupId"), primary_key=True),
    Column("atmId", Integer, ForeignKey("ATM.atmId"), primary_key=True),
)


class AtmDevice(Base, BaseModel):
    __tablename__ = "AtmDevice"
    id = Column(Integer, primary_key=True, autoincrement=True)
    atmId = Column(Integer, ForeignKey(ATM.atmId), primary_key=True)
    deviceId = Column(Integer, ForeignKey(Device.deviceId), primary_key=True)
    deviceStatus = Column(String(20))

    def __repr__(self):
        return f"AtmDevice(atmId={self.atmId}, \
                deviceId={self.deviceId}, \
                deviceStatus='{self.deviceStatus}')"


class ElectronicJournal(Base, BaseModel):
    __tablename__ = "ElectronicJournal"

    ejId = Column(Integer, primary_key=True)
    ejData = Column(String(1000), nullable=False)
    atmId = Column(Integer, ForeignKey("ATM.atmId"), nullable=False)
    timestamp = Column(String(100), nullable=False)

    # Relationship with ATM table
    #atm = relationship("ATM", backref="electronic_journals")
    
    #add relationship with Event table
    events = relationship("Event", backref="elj")
    
    #add relationship with Transaction table
    transactions = relationship("Transaction", backref="elj_t")

    @property
    def events(self):
        """ getter for list of events related to the elctronic journal"""
        event_list = []
        from models import storage
        for event in storage.all(Event).values():
            if event.ejId == self.ejId:
                event_list.append(event)
        return event_list 

    @property
    def transactions(self):
        """ getter for list of transactions related to the elctronic journal"""
        transaction_list = []
        from models import storage
        for transaction in storage.all(Transaction).values():
            if transaction.ejId == self.ejId:
                transaction_list.append(transaction)
        return transaction_list


    def __repr__(self):
        return f"<ElectronicJournal(ejId={self.ejId}, \
                        ejData={self.ejData}, atmId={self.atmId}, \
                        timestamp={self.timestamp})>"


class Event(Base, BaseModel):
    __tablename__ = "Event"

    eventId = Column(Integer, primary_key=True)
    eventName = Column(String(100), nullable=False, unique=True)
    eventLevel = Column(Enum("INFO", "WARNING", "ERROR", "CRITICAL"),
                        nullable=False)
    ejId = Column(Integer, ForeignKey("ElectronicJournal.ejId"))

    # Relationship with ElectronicJournal table
    #electronic_journal = relationship("ElectronicJournal", backref="events")

    def __repr__(self):
        return f"<Event(eventId={self.eventId},\
                eventName={self.eventName}, \
                eventLevel={self.eventLevel}, \
                ejId={self.ejId})>"


class Transaction(Base, BaseModel):
    __tablename__ = "Transaction"

    transactionId = Column(Integer, primary_key=True)
    transactionType = Column(String(45), nullable=False)
    transactionDetail = Column(String(1000))
    ejId = Column(Integer, ForeignKey("ElectronicJournal.ejId"))

    # Relationship with ElectronicJournal table
    #electronic_journal = relationship("ElectronicJournal",
    #                                  backref="transactions")

    def __repr__(self):
        return f"<Transaction(transactionId={self.transactionId}, \
                    transactionType={self.transactionType}, \
                    transactionDetail={self.transactionDetail}, \
                    ejId={self.ejId})>"

'''
# Create all tables in the database (comment out if tables already exist)

Base.metadata.create_all(engine)

# Open a session

# Load JSON data

with open("dummy.json", "r") as f:
    data = json.load(f)

with sessionmaker(bind=engine)() as session:
    # Iterate through each table in the JSON data
    for table_name, table_data in data.items():
        # Get the corresponding table model class
        table_model = getattr(sys.modules[__name__], table_name)

        # Insert data into the table
        for row in table_data:
            session.add(table_model(**row))

        # Commit changes to the database
        session.commit()
'''
print("Data successfully populated from JSON file.")
