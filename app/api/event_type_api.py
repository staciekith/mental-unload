
from app.adapters.postgres_database.repositories.event_type_repo import EventTypeRepo
from app.use_cases.list_event_types import ListEventTypes
from app.use_cases.create_event_type import CreateEventType
from app.use_cases.update_event_type import UpdateEventType
from app.use_cases.delete_event_type import DeleteEventType
from app.domains.event_type import EventType
from app.domains.error import Error

from flask import current_app as app
from flask import jsonify
from flask import request

@app.route('/event_types', methods=['GET', 'POST'])
def event_types():
    if request.method == 'POST':
        return post_event_types()
    else:
        return get_event_types()

@app.route('/event_types/<int:event_type_id>', methods=['DELETE', 'PUT'])
def event_type(event_type_id):
    if request.method == 'DELETE':
        return delete_event_type(event_type_id)
    else:
        return put_event_type(event_type_id)

def post_event_types():
    request_data = request.get_json()

    missing_fields = EventType.validate_fields(request_data)

    if (0 != len(missing_fields)):
        error = Error("Some fields are missing.", {"missing_fields": missing_fields})

        return jsonify(error), 400

    created_event_type = CreateEventType.execute(EventTypeRepo, request_data)

    return jsonify(created_event_type)

def get_event_types():
    resp = ListEventTypes.execute(EventTypeRepo)

    return jsonify(resp)

def delete_event_type(event_type_id):
    DeleteEventType.execute(EventTypeRepo, event_type_id)

    return 'OK', 200

def put_event_type(event_type_id):
    request_data = request.get_json()

    result = UpdateEventType.execute(EventTypeRepo, event_type_id, request_data)

    if "error" in result.keys():
        return jsonify(result.get("error")), 400

    return jsonify(result.get("ok"))