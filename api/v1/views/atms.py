#!/usr/bin/python3

from flask import jsonify, abort, make_response, request
from api.v1.views import app_views
from models import storage
from models.engine.db_storage import ATM, Branch, Region


@app_views.route('/branches/<branch_id>/atms', strict_slashes=False)
def get_atms_by_branch(branch_id):
    """
    Retrieves the list of all atms objects
    of a specific branch
    """
    list_at = []
    branch = storage.get(Branch, branch_id)
    if not branch:
        abort(404)
    for atm in branch.atms_b:
        list_at.append(atm.to_dict())
    return jsonify(list_at)

@app_views.route('/atms_chart', strict_slashes=False)
def charts():
    """
    Retrieves data for charts
    """
    new = {}
    out = 0
    low = 0
    avail = 0
    in_service = 0
    out_service = 0
    lost_comm = 0
    for atm in storage.all(ATM).values():
        if atm.cash_level == 0:
            out += 1
        elif atm.cash_level <= 5000:
            low += 1
        elif atm.cash_level > 5000:
            avail += 1
        if atm.status == "Online":
            in_service += 1
        elif atm.status == "Offline":
            out_service += 1
        elif atm.status == "Under Maintenance":
            lost_comm += 1
    total1 = out + low + avail
    total2 = in_service + out_service + lost_comm
    new = {"Out of Cash": int((out / total1) * 100), "Cash Low": int((low / total1) * 100) , "Cash Available": int((avail / total1) * 100), "inService": int((in_service / total2) * 100), "outOfService": int((out_service / total2) * 100), "lostComm": int((lost_comm / total2) * 100)}
    return jsonify(new)

@app_views.route('/atms', strict_slashes=False)
def get_atmss():
    """
    Retrieves the list of all atm objects
    """
    all_atms = storage.all(ATM).values()
    all_regions = storage.all(Region).values()
    list_atms = []
    
    for atm in all_atms:
        new_dict = atm.to_dict()
        for region in all_regions:
            for branch in region.branches:
                if atm.branchId == branch.branchId:
                    regionName = region.regionName
        new_dict["regionName"] = regionName
        new_dict["cash_level"] = atm.cash_level
        list_atms.append(new_dict)
    return jsonify(list_atms)


@app_views.route('/atms/<atm_id>', strict_slashes=False)
def get_atm(atm_id):
    """
    Retrieves a specific atm
    """
    atm = storage.get(ATM, atm_id)
    all_regions = storage.all(Region).values()
    if not atm:
        abort(404)
    new_dict = atm.to_dict()
    for region in all_regions:
        for branch in region.branches:
            if atm.branchId == branch.branchId:
                regionName = region.regionName
    new_dict["regionName"] = regionName
    return jsonify(new_dict)

'''
@app_views.route('/atms/<atm_id>', methods=['DELETE'], strict_slashes=False)
def delete_atm(atm_id):
    """
    Deletes a specific atm
    """
    atm = storage.get(ATM, atm_id)
    if not atm:
        abort(404)
    storage.delete(atm)
    storage.save()
    return make_response(jsonify({}), 200)
'''

@app_views.route('/branches/<branch_id>/atms', methods=['POST'], strict_slashes=False)
def create_atm(branch_id):
    """
    Create a atm
    """
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'atmName' not in request.get_json():
        abort(400, description="Missing atm name")
    
    data = request.get_json()
    atm = ATM(**data, branchId=branch_id)
    storage.new(atm)
    storage.save()
    return make_response(jsonify(atm.to_dict()), 201)

@app_views.route('/atms/<atm_id>', methods=['PUT'], strict_slashes=False)
def update_atm(atm_id):
    """
    Update a atm
    """
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'atmName' not in request.get_json():
        abort(400, description="Missing atm name")
    data = request.get_json()
    atm = storage.get(ATM, atm_id)

    for k, v in data.items():
        if k not in ["id"]:
            setattr(atm, k, v)
    storage.save()
    return make_response(jsonify(atm.to_dict()), 200)
