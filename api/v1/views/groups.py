#!/usr/bin/python3

from flask import jsonify, abort, make_response, request
from api.v1.views import app_views
from models import storage
from models.engine.db_storage import Group


@app_views.route('/groups', strict_slashes=False)
def get_groups():
    """
    Retrieves the list of all group objects
    """
    all_groups = storage.all(Group).values()
    list_groups = []
    for group in all_groups:
        list_groups.append(group.to_dict())
    return jsonify(list_groups)


@app_views.route('/groups/<group_id>', strict_slashes=False)
def get_grou(group_id):
    """
    Retrieves a specific group
    """
    group = storage.get(Group, group_id)
    list_atms = []
    for atm in group.atms_g:
        list_atms.append(atm.to_dict())
    if not group:
        abort(404)
    new_dict = group.to_dict()
    new_dict["atms"] = list_atms
    return jsonify(new_dict)


@app_views.route('/groups/<group_id>', methods=['DELETE'], strict_slashes=False)
def delete_group(group_id):
    """
    Delete a specific group
    """
    group = storage.get(Group, group_id)
    if not group:
        abort(404)
    storage.delete(group)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/groups', methods=['POST'], strict_slashes=False)
def create_group():
    """
    Create a group
    """
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'groupName' not in request.get_json():
        abort(400, description="Missing group name")
    
    data = request.get_json()
    group = Group(**data)
    storage.new(group)
    storage.save()
    return make_response(jsonify(group.to_dict()), 201)

@app_views.route('/groups/<group_id>', methods=['PUT'], strict_slashes=False)
def update_group(group_id):
    """
    Update a group
    """
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'groupName' not in request.get_json():
        abort(400, description="Missing group name")
    data = request.get_json()
    group = storage.get(Group, group_id)

    for k, v in data.items():
        if k not in ["id"]:
            setattr(group, k, v)
    storage.save()
    return make_response(jsonify(group.to_dict()), 200)
