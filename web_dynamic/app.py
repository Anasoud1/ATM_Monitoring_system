#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from flask import Flask, render_template
import requests
from api.v1.app import app


app2 = Flask(__name__)


@app2.teardown_appcontext
def close(error):
    '''Remove the current SQLAlchemy Session'''
    storage.close()


@app2.route('/', strict_slashes=False)
def index():
    '''test for group'''
    url = "http://0.0.0.0:5000/api/v1/branches"
    url2 = "http://0.0.0.0:5000/api/v1/atms"
    url3 = "http://0.0.0.0:5000/api/v1/groups"
    url6 = "http://0.0.0.0:5000/api/v1/transactions"
    url7 = "http://0.0.0.0:5000/api/v1/atms_chart"

    response = requests.get(url)
    response2 = requests.get(url2)
    response3 = requests.get(url3)
    response6 = requests.get(url6)
    response7 = requests.get(url7)
    
    branches = response.json()
    atms = response2.json()
    groups = response3.json()
    transactions = response6.json()
    atms_chart = response7.json()

    return render_template('index.html', branches=branches, atms=atms, groups=groups, transactions=transactions, atms_chart=atms_chart)

@app2.route('/atms/<atm_id>', strict_slashes=False)
def atm(atm_id):
    '''return a specific atm'''
    url = "http://0.0.0.0:5000/api/v1/branches"
    url2 = "http://0.0.0.0:5000/api/v1/atms"
    url3 = "http://0.0.0.0:5000/api/v1/atms/{}".format(atm_id)
    url4 = "http://0.0.0.0:5000/api/v1/groups"
    url5 = "http://0.0.0.0:5000/api/v1/atms/{}/devices".format(atm_id)
    url6 = "http://0.0.0.0:5000/api/v1/transaction_chart/{}".format(atm_id)

    response = requests.get(url)
    response2 = requests.get(url2)
    response3 = requests.get(url3)
    response4 = requests.get(url4)
    response5 = requests.get(url5)
    response6 = requests.get(url6)

    branches = response.json()
    atms = response2.json()
    atm = response3.json()
    groups = response4.json()
    device = response5.json()
    trans = response6.json()

    cash_balance = device["cash_balance"]
    devices = device["devices"]
    print("***", device , "****")
    return render_template('atm.html', branches=branches, atms=atms, atm=atm, groups=groups, cash_balance=cash_balance, devices=devices, trans=trans)

@app2.route('/groups/<group_id>', strict_slashes=False)
def group(group_id):
    '''return a specific atm'''
    url = "http://0.0.0.0:5000/api/v1/branches"
    url2 = "http://0.0.0.0:5000/api/v1/atms"
    url4 = "http://0.0.0.0:5000/api/v1/groups"
    url5 = "http://0.0.0.0:5000/api/v1/groups/{}".format(group_id)
    response = requests.get(url)
    response2 = requests.get(url2)
    response4 = requests.get(url4)
    response5 = requests.get(url5)

    branches = response.json()
    atms = response2.json()
    groups = response4.json()
    grp = response5.json()
    return render_template('group.html', branches=branches, atms=atms, groups=groups, grp=grp)

@app2.route('/transactions/<ej_id>', strict_slashes=False)
def transaction(ej_id):
    '''return a specific atm'''
    url = "http://0.0.0.0:5000/api/v1/branches"
    url2 = "http://0.0.0.0:5000/api/v1/atms"
    url3 = "http://0.0.0.0:5000/api/v1/atms/{}".format(ej_id)
    url4 = "http://0.0.0.0:5000/api/v1/groups"
    url5 = "http://0.0.0.0:5000/api/v1/eljs/{}/transactions".format(ej_id)
    response = requests.get(url)
    response2 = requests.get(url2)
    response3 = requests.get(url3)
    response4 = requests.get(url4)
    response5 = requests.get(url5)

    branches = response.json()
    atms = response2.json()
    atm = response3.json()
    groups = response4.json()
    transactions = response5.json()
    return render_template('transaction.html', branches=branches, atms=atms, groups=groups, atm=atm, transactions=transactions)

if __name__ == "__main__":
    """ Main Function """
    app2.run(host='0.0.0.0', port=5001)
