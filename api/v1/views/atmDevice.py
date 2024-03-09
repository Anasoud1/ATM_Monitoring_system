#!/usr/bin/python3

from flask import jsonify, abort, make_response, request
from api.v1.views import app_views
from models import storage
from models.engine.db_storage import AtmDevice


@app_views.route('/atms/<atm_id>/devices', strict_slashes=False)
def get_atm_devices(atm_id):
    """
    Retrieves devices from a specific atm
    """
    list_atms = []
    for atm in storage.all(AtmDevice).values():
        if str(atm.atmId) == atm_id:
            list_atms.append(atm.to_dict())
    return jsonify(list_atms)
