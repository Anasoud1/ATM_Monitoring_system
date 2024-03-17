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
        if str(atm.atmId) == atm_id:
            for device in storage.all(Device).values():
                if device.deviceId == atm.deviceId:
                    dict_devices[device.deviceModel] = atm.deviceStatus

    new_dict["atmName"] = storage.get(ATM, atm_id).atmName
    new_dict["devices"] = dict_devices
    
    return jsonify(new_dict)
