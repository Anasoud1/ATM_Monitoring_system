#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.teardown_appcontext
def close(error):
    '''Remove the current SQLAlchemy Session'''
    storage.close()


@app.route('/', strict_slashes=False)
def index():
    '''test for group'''
    url = "http://0.0.0.0:5000/api/v1/groups/1"
    response = requests.get(url)
    if response.status_code == 200:
        group = response.json()
        return render_template('g.html', group=group)
    else:
        return "Error: Unable to fetch data from the API"


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5001)
