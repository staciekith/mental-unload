
from app.adapters.postgres_database.repositories.event_repo import EventRepo
from app.adapters.postgres_database.repositories.event_type_repo import EventTypeRepo
from app.use_cases.list_events import ListEvents
from app.use_cases.create_event import CreateEvent
from app.use_cases.delete_event import DeleteEvent
from app.domains.event import Event

from flask import current_app as app
from flask import jsonify
from flask import request

@app.route('/events', methods=['GET', 'POST'])
def events():
    if request.method == 'POST':
        return post_events()
    else:
        return get_events()

@app.route('/events/<int:event_id>', methods=['DELETE'])
def event(event_id):
    DeleteEvent.execute(EventRepo, event_id)

    return 'OK', 200

def post_events():
    request_data = request.get_json()

    created_event = CreateEvent.execute(EventRepo, EventTypeRepo, request_data)

    return jsonify(created_event)

def get_events():
    resp = ListEvents.execute(EventRepo)

    return jsonify(resp)