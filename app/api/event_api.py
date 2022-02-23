
from app.adapters.postgres_database.repositories.event_repo import EventRepo
from app.adapters.postgres_database.repositories.event_type_repo import EventTypeRepo
from app.use_cases.list_events import ListEvents
from app.use_cases.create_event import CreateEvent
from app.use_cases.update_event import UpdateEvent
from app.use_cases.delete_event import DeleteEvent
from app.domains.event import Event
from app.domains.event_type import EventType
from app.domains.error import Error

from flask import current_app as app
from flask import jsonify
from flask import request

@app.route('/events', methods=['GET', 'POST'])
def events():
    if request.method == 'POST':
        return post_events()
    else:
        return get_events()

@app.route('/events/<int:event_id>', methods=['DELETE', 'PUT'])
def event(event_id):
    if request.method == 'DELETE':
        return delete_event(event_id)
    else:
        return put_event(event_id)

def post_events():
    request_data = request.get_json()

    missing_fields = Event.validate_fields(request_data)

    if (0 != len(missing_fields)):
        error = Error("Some fields are missing.", {"missing_fields": missing_fields})

        return jsonify(error), 400

    created_event = CreateEvent.execute(EventRepo, EventTypeRepo, request_data)

    return jsonify(created_event)

def get_events():
    resp = ListEvents.execute(EventRepo)

    return jsonify(resp)

def delete_event(event_id):
    DeleteEvent.execute(EventRepo, event_id)

    return 'OK', 200

def put_event(event_id):
    request_data = request.get_json()

    result = UpdateEvent.execute(EventRepo, event_id, request_data)

    if "error" in result.keys():
        return jsonify(result.get("error")), 400

    return jsonify(result.get("ok"))