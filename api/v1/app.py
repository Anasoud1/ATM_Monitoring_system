#!/usr/bin/python3
from flask import Flask, make_response, jsonify
from api.v1.views import app_views
from os import getenv
from models import storage


app = Flask(__name__)
app.register_blueprint(app_views)

@app.errorhandler(404)
def not_found(error):
    """handler for 404 error"""
    return make_response(jsonify({"error": "Not found"}), 404)

@app.teardown_appcontext
def teardown_db(obj):
    """close connection with database"""
    storage.close()


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port, threaded=True)
