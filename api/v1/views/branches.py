#!/usr/bin/python3

from flask import jsonify, abort, make_response, request
from api.v1.views import app_views
from models import storage
from models.engine.db_storage import Region, Branch


@app_views.route('/branches', strict_slashes=False)
def get_branches():
    """
    Retrieves the list of all Branch objects
    """
    all_branches = storage.all(Branch).values()
    list_branches = []
    for branch in all_branches:
        list_branches.append(branch.to_dict())
    return jsonify(list_branches)


@app_views.route('/regions/<region_id>/branches', strict_slashes=False)
def get_branches_by_region(region_id):
    """
    Retrieves the list of all branches objects
    of a specific region
    """
    list_br = []
    region = storage.get(Region, region_id)
    if not region:
        abort(404)
    for branch in region.branches:
        list_br.append(branch.to_dict())
    return jsonify(list_br)

@app_views.route('/branches/<branch_id>', strict_slashes=False)
def get_branch(branch_id):
    """
    Retrieves a specific branch
    """
    branch = storage.get(Branch, branch_id)
    if not branch:
        abort(404)
    return jsonify(branch.to_dict())


@app_views.route('/branches/<branch_id>', methods=['DELETE'], strict_slashes=False)
def delete_branch(branch_id):
    """
    Delete a specific branch
    """
    branch = storage.get(Branch, branch_id)
    if not branch:
        abort(404)
    storage.delete(branch)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/branches', methods=['POST'], strict_slashes=False)
def create_branch():
    """
    Create a Branch
    """
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'branchName' not in request.get_json():
        abort(400, description="Missing branch name")
    
    data = request.get_json()
    branch = Branch(**data)
    storage.new(branch)
    storage.save()
    return make_response(jsonify(branch.to_dict()), 201)

@app_views.route('/branches/<branch_id>', methods=['PUT'], strict_slashes=False)
def update_branch(branch_id):
    """
    Update a branch
    """
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'branchName' not in request.get_json():
        abort(400, description="Missing branch name")
    data = request.get_json()
    branch = storage.get(Branch, branch_id)

    for k, v in data.items():
        if k not in ["id"]:
            setattr(branch, k, v)
    storage.save()
    return make_response(jsonify(branch.to_dict()), 200)
