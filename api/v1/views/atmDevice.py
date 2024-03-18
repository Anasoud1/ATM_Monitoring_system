#!/usr/bin/python3

from flask import jsonify, abort, make_response, request
from api.v1.views import app_views
from models import storage
from models.engine.db_storage import AtmDevice, ATM, Device


@app_views.route('/atms/<atm_id>/devices', strict_slashes=False)
def get_atm_devices(atm_id):
    """
    Retrieves devices from a specific atm
    """
    dict_devices = {}
    new_dict = {}
    for atm in storage.all(AtmDevice).values():
        '''
        dic = atm.to_dict()
        list_cass = []
        for cass in atm.cassettes:
            list_cass.append(cass.to_dict())
        dic["cassettes"] = list_cass
        '''
        #print("**** dic:", atm.calculate_cash(), "id:", atm.atmId, "****")
        if str(atm.atmId) == atm_id:
            cash_balance = atm.calculate_cash()
            for device in storage.all(Device).values():
                if device.deviceId == atm.deviceId:
                    dict_devices[device.deviceModel] = atm.deviceStatus
    

    new_dict["atmName"] = storage.get(ATM, atm_id).atmName
    new_dict["devices"] = dict_devices
    new_dict["cash_balance"] = cash_balance

    
    return jsonify(new_dict)

@app_views.route('/atms/cash_balance', strict_slashes=False)
def get_cash_balance():
    '''
    Retrieves cash balance for each atms"
    '''
    list_cass = []
    for atm in storage.all(AtmDevice).values():
        new_dict = {}
        if atm.deviceId == 1:
            new_dict["atmId"] = atm.atmId
            new_dict["cash_balance"] = atm.calculate_cash()
            list_cass.append(new_dict)
    return jsonify(list_cass)
