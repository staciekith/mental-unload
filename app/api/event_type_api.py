
from app.adapters.postgres_database.repositories.event_type_repo import EventTypeRepo
from app.use_cases.list_event_types import ListEventTypes
from app.use_cases.create_event_type import CreateEventType
from app.use_cases.delete_event_type import DeleteEventType
from app.domains.event_type import EventType

from flask import current_app as app
from flask import jsonify
from flask import request

@app.route('/event_types', methods=['GET', 'POST'])
def event_types():
    if request.method == 'POST':
        return post_event_types()
    else:
        return get_event_types()

@app.route('/event_types/<int:event_type_id>', methods=['DELETE'])
def event_type(event_type_id):
    print(event_type_id)
    DeleteEventType.execute(EventTypeRepo, event_type_id)

    return 'OK', 200

def post_event_types():
    request_data = request.get_json()
    request_data['id'] = None
    event_type = EventType.from_dict(request_data)

    created_event_type = CreateEventType.execute(EventTypeRepo, event_type)

    return jsonify(created_event_type)

def get_event_types():
    resp = ListEventTypes.execute(EventTypeRepo)

    return jsonify(resp)