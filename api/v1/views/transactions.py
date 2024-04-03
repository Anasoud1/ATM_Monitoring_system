#!/usr/bin/python3

from flask import jsonify, abort, make_response, request
from api.v1.views import app_views
from models import storage
from models.engine.db_storage import Transaction, ElectronicJournal


@app_views.route('/eljs/<elj_id>/transactions', strict_slashes=False)
def get_transaction_by_elj(elj_id):
    """
    Retrieves the list of all transaction objects
    of a specific electonicJournal
    """
    list_tr = []
    ej = storage.get(ElectronicJournal, elj_id)
    if not ej:
        abort(404)
    for transaction in ej.transactions:
        list_tr.append(transaction.to_dict())
    return jsonify(list_tr)


@app_views.route('/transaction_chart/<atm_id>', strict_slashes=False)
def transaction_chart(atm_id):
    """
    Retrieve a dictionnary of a specific Transaction objects
    """
    all_transactions = storage.all(Transaction).values()
    list_transactions = []
    new = {}
    w = 0
    d = 0
    t = 0
    b = 0
    for transaction in all_transactions:
        if transaction.ejId == int(atm_id):
            if transaction.transactionType == "Withdrawal":
                w += 1
            elif transaction.transactionType == "Deposit":
                d += 1
            elif transaction.transactionType == "Balance Inquiry":
                b += 1
            elif transaction.transactionType == "Transfer":
                t += 1
    total = w + d + b + t
    new["withdrawal"] = int((w / total) * 100)
    new["deposit"] = int((d / total) * 100)
    new["balanceInquiry"] = int((b / total) * 100)
    new["transfer"] = int((t / total) * 100)
    return jsonify(new)


@app_views.route('/transactions', strict_slashes=False)
def get_transactions_chart():
    """
    Retrieves the list of all Transaction objects
    """
    all_transactions = storage.all(Transaction).values()
    list_transactions = []
    new = {}
    w = 0
    d = 0
    t = 0
    b = 0
    for transaction in all_transactions:
        #list_transactions.append(transaction.to_dict())
        if transaction.transactionType == "Withdrawal":
            w += 1
        elif transaction.transactionType == "Deposit":
            d += 1
        elif transaction.transactionType == "Balance Inquiry":
            b += 1
        elif transaction.transactionType == "Transfer":
            t += 1
    total = w + d + b + t
    new["withdrawal"] = int((w / total) * 100)
    new["deposit"] = int((d / total) * 100)
    new["balanceInquiry"] = int((b / total) * 100)
    new["transfer"] = int((t / total) * 100)
    return jsonify(new)


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


@app_views.route('/eljs/<elj_id>/transactions', methods=['POST'], strict_slashes=False)
def create_transaction(elj_id):
    """
    Create a transaction
    """
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'transactionType' not in request.get_json():
        abort(400, description="Missing transaction type")
    
    data = request.get_json()
    transaction = Transaction(**data, ejId=elj_id)
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
