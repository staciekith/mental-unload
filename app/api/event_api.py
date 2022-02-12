
from datetime import datetime
from app.adapters.postgres_database.repositories.event_repo import EventRepo
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
    print(event_id)
    DeleteEvent.execute(EventRepo, event_id)

    return 'OK', 200

def post_events():
    request_data = request.get_json()
    request_data['id'] = None
    request_data['done_at'] = datetime.now()
    request_data['status'] = 'done'
    request_data['due_at'] = None
    request_data['remind_at'] = None
    event = Event.from_dict(request_data)
    # creer l'event pour le reminder

    created_event = CreateEvent.execute(EventRepo, event)

    return jsonify(created_event)

def get_events():
    resp = ListEvents.execute(EventRepo)

    return jsonify(resp)