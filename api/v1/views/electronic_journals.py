#!/usr/bin/python3

from flask import jsonify, abort, make_response, request
from api.v1.views import app_views
from models import storage
from models.engine.db_storage import ElectronicJournal 


@app_views.route('/eljs', strict_slashes=False)
def get_eljs():
    """
    Retrieves the list of all ElectronicJournal objects
    """
    all_eljs = storage.all(ElectronicJournal).values()
    list_eljs = []
    for elj in all_eljs:
        list_eljs.append(elj.to_dict())
    return jsonify(list_eljs)


@app_views.route('/eljs/<elj_id>', strict_slashes=False)
def get_elj(elj_id):
    """
    Retrieves a specific ElectronicJournal
    """
    elj = storage.get(ElectronicJournal, elj_id)
    if not elj:
        abort(404)
    return jsonify(elj.to_dict())


@app_views.route('/eljs/<elj_id>', methods=['DELETE'], strict_slashes=False)
def delete_elj(elj_id):
    """
    Delete a specific elj
    """
    elj = storage.get(ElectronicJournal, elj_id)
    if not elj:
        abort(404)
    storage.delete(elj)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/eljs', methods=['POST'], strict_slashes=False)
def create_elj():
    """
    Create a elj
    """
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'ejData' not in request.get_json():
        abort(400, description="Missing ElectronicJournal data")
    
    data = request.get_json()
    elj = ElectronicJournal(**data)
    storage.new(elj)
    storage.save()
    return make_response(jsonify(elj.to_dict()), 201)

@app_views.route('/eljs/<elj_id>', methods=['PUT'], strict_slashes=False)
def update_zlj(elj_id):
    """
    Update a elj
    """
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'ejData' not in request.get_json():
        abort(400, description="Missing ElectronicJournal data")
    data = request.get_json()
    elj = storage.get(ElectronicJournal, elj_id)

    for k, v in data.items():
        if k not in ["id"]:
            setattr(elj, k, v)
    storage.save()
    return make_response(jsonify(elj.to_dict()), 200)
