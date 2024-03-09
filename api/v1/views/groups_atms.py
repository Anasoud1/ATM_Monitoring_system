#!/usr/bin/python3

from flask import jsonify, abort, make_response, request
from api.v1.views import app_views
from models import storage
from models.engine.db_storage import Group


@app_views.route('/groups/<group_id>/atms', strict_slashes=False)
def get_group_by_atms(group_id):
    """
    Retrieves atms from a specific group
    """
    list_atms = []
    group = storage.get(Group, group_id)
    if not group:
        abort(404)
    for atm in group.atms_g:
        list_atms.append(atm.to_dict())
    return jsonify(list_atms)
