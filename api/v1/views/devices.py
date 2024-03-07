#!/usr/bin/python3

from flask import jsonify, abort, make_response, request
from api.v1.views import app_views
from models import storage
from models.engine.db_storage import Device


@app_views.route('/devices', strict_slashes=False)
def get_devices():
    """
    Retrieves the list of all device objects
    """
    all_devices = storage.all(Device).values()
    list_devices = []
    for device in all_devices:
        list_devices.append(device.to_dict())
    return jsonify(list_devices)


@app_views.route('/devices/<device_id>', strict_slashes=False)
def get_device(device_id):
    """
    Retrieves a specific device
    """
    device = storage.get(Device, device_id)
    if not device:
        abort(404)
    return jsonify(device.to_dict())


@app_views.route('/devices/<device_id>', methods=['DELETE'], strict_slashes=False)
def delete_device(device_id):
    """
    Delete a specific device
    """
    device = storage.get(Device, device_id)
    if not device:
        abort(404)
    storage.delete(device)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/devices', methods=['POST'], strict_slashes=False)
def create_device():
    """
    Create a device
    """
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'deviceModel' not in request.get_json():
        abort(400, description="Missing device model")
    
    data = request.get_json()
    device = Device(**data)
    storage.new(device)
    storage.save()
    return make_response(jsonify(device.to_dict()), 201)

@app_views.route('/devices/<device_id>', methods=['PUT'], strict_slashes=False)
def update_device(device_id):
    """
    Update a device
    """
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'deviceModel' not in request.get_json():
        abort(400, description="Missing device model")
    data = request.get_json()
    device = storage.get(Device, device_id)

    for k, v in data.items():
        if k not in ["id"]:
            setattr(device, k, v)
    storage.save()
    return make_response(jsonify(device.to_dict()), 200)
