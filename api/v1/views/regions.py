#!/usr/bin/python3

from flask import jsonify, abort, make_response, request
from api.v1.views import app_views
from models import storage
from models.engine.db_storage import Region


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/regions', strict_slashes=False)
def get_regions():
    """
    Retrieves the list of all Region objects
    """
    all_regions = storage.all(Region).values()
    list_regions = []
    for region in all_regions:
        list_regions.append(region.to_dict())
    return jsonify(list_regions)


@app_views.route('/regions/<region_id>', strict_slashes=False)
def get_region(region_id):
    """
    Retrieves a specific region
    """
    print("enter here")
    region = storage.get(Region, region_id)
    if not region:
        abort(404)
    return jsonify(region.to_dict())


@app_views.route('/regions/<region_id>', methods=['DELETE'], strict_slashes=False)
def delete_region(region_id):
    """
    Delete a specific region
    """
    region = storage.get(Region, region_id)
    if not region:
        abort(404)
    storage.delete(region)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/regions', methods=['POST'], strict_slashes=False)
def create_region():
    """
    Create a REgion
    """
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'regionName' not in request.get_json():
        abort(400, description="Missing region name")
    
    data = request.get_json()
    region = Region(**data)
    storage.new(region)
    storage.save()
    return make_response(jsonify(region.to_dict()), 201)

@app_views.route('/regions/<region_id>', methods=['PUT'], strict_slashes=False)
def update_region(region_id):
    """
    Update a Region
    """
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'regionName' not in request.get_json():
        abort(400, description="Missing region name")
    data = request.get_json()
    region = storage.get(Region, region_id)

    for k, v in data.items():
        if k not in ["id"]:
            setattr(region, k, v)
    storage.save()
    return make_response(jsonify(region.to_dict()), 200)
