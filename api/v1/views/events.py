#!/usr/bin/python3

from flask import jsonify, abort, make_response, request
from api.v1.views import app_views
from models import storage
from models.engine.db_storage import ElectronicJournal, Event


@app_views.route('/eljs/<elj_id>/events', strict_slashes=False)
def get_events_by_elj(elj_id):
    """
    Retrieves the list of all event objects
    of a specific electonicJournal
    """
    list_ev = []
    ej = storage.get(ElectronicJournal, elj_id)
    if not ej:
        abort(404)
    for event in ej.events:
        list_ev.append(event.to_dict())
    return jsonify(list_ev)

@app_views.route('/events', strict_slashes=False)
def get_events():
    """
    Retrieves the list of all event objects
    """
    all_events = storage.all(Event).values()
    list_events = []
    for event in all_events:
        list_events.append(event.to_dict())
    return jsonify(list_events)


@app_views.route('/events/<event_id>', strict_slashes=False)
def get_event(event_id):
    """
    Retrieves a specific event
    """
    event = storage.get(Event, event_id)
    if not event:
        abort(404)
    return jsonify(event.to_dict())


@app_views.route('events/<event_id>', methods=['DELETE'], strict_slashes=False)
def delete_event(event_id):
    """
    Delete a specific event
    """
    event = storage.get(Event, event_id)
    if not event:
        abort(404)
    storage.delete(event)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/eljs/<elj_id>/events', methods=['POST'], strict_slashes=False)
def create_event(elj_id):
    """
    Create a event
    """
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'eventName' not in request.get_json():
        abort(400, description="Missing event name")
    
    data = request.get_json()
    event = Event(**data, ejId=elj_id)
    storage.new(event)
    storage.save()
    return make_response(jsonify(event.to_dict()), 201)

@app_views.route('events/<event_id>', methods=['PUT'], strict_slashes=False)
def update_event(event_id):
    """
    Update a event
    """
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'eventName' not in request.get_json():
        abort(400, description="Missing event name")
    data = request.get_json()
    event = storage.get(Event, event_id)

    for k, v in data.items():
        if k not in ["id"]:
            setattr(event, k, v)
    storage.save()
    return make_response(jsonify(event.to_dict()), 200)
