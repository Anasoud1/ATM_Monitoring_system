#!/usr/bin/python3

from flask import jsonify, abort, make_response, request
from api.v1.views import app_views
from models import storage
from models.engine.db_storage import Transaction


@app_views.route('/transactions', strict_slashes=False)
def get_transactions():
    """
    Retrieves the list of all Transaction objects
    """
    all_transactions = storage.all(Transaction).values()
    list_transactions = []
    for transaction in all_transactions:
        list_transactions.append(transaction.to_dict())
    return jsonify(list_transactions)


@app_views.route('/transactions/<transaction_id>', strict_slashes=False)
def get_transaction(transaction_id):
    """
    Retrieves a specific transaction
    """
    transaction = storage.get(Transaction, transaction_id)
    if not transaction:
        abort(404)
    return jsonify(transaction.to_dict())


@app_views.route('/transactions/<transaction_id>', methods=['DELETE'], strict_slashes=False)
def delete_transaction(transaction_id):
    """
    Delete a specific transaction
    """
    transaction = storage.get(Transaction, transaction_id)
    if not transaction:
        abort(404)
    storage.delete(transaction)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/transactions', methods=['POST'], strict_slashes=False)
def create_transaction():
    """
    Create a transaction
    """
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'transactionType' not in request.get_json():
        abort(400, description="Missing transaction type")
    
    data = request.get_json()
    transaction = Transaction(**data)
    storage.new(transaction)
    storage.save()
    return make_response(jsonify(transaction.to_dict()), 201)

@app_views.route('/transactions/<transaction_id>', methods=['PUT'], strict_slashes=False)
def update_transaction(transaction_id):
    """
    Update a transaction
    """
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'transactionType' not in request.get_json():
        abort(400, description="Missing transaction type")
    data = request.get_json()
    transaction = storage.get(Transaction, transaction_id)

    for k, v in data.items():
        if k not in ["id"]:
            setattr(transaction, k, v)
    storage.save()
    return make_response(jsonify(transaction.to_dict()), 200)
