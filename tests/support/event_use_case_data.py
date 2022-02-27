from app.domains.event import Event
from datetime import datetime

def find_result():
    event = {
        'id': 1,
        'title': "event 1",
        'quantity': 1,
        'done_at': datetime(2022, 2, 10, 9, 30, 0, 0),
        'due_at': None,
        'remind_at': None,
        'status': "done",
        'type_id': 1
    }

    return {"ok": Event(event)}

def list_result():
    event_1 = {
        'id': 1,
        'title': "event 1",
        'quantity': 1,
        'done_at': datetime(2022, 2, 10, 9, 30, 0, 0),
        'due_at': None,
        'remind_at': None,
        'status': "done",
        'type_id': 1
    }

    event_2 = {
        'id': 2,
        'title': "event 2",
        'quantity': 1,
        'done_at': datetime(2022, 2, 10, 9, 30, 0, 0),
        'due_at': None,
        'remind_at': None,
        'status': "done",
        'type_id': 1
    }

    event_1 = Event(event_1)
    event_2 = Event(event_2)

    return {"ok": [event_1, event_2]}

def create_result():
    event = {
        'id': 3,
        'title': "event created",
        'quantity': 2040,
        'done_at': datetime(2022, 2, 10, 9, 30, 0, 0),
        'due_at': None,
        'remind_at': None,
        'status': "done",
        'type_id': 1
    }

    return {"ok": Event(event)}

def update_result():
    event = {
        'id': 1,
        'title': "event updated",
        'quantity': 1,
        'done_at': datetime(2022, 2, 10, 9, 30, 0, 0),
        'due_at': None,
        'remind_at': None,
        'status': "done",
        'type_id': 1
    }

    return {"ok": Event(event)}

def not_found_result(id):
    return {"error": "Event with ID " + str(id) + " does not exist"}

def event_type_not_found_result(id):
    return {"error": "EventType with ID " + str(id) + " does not exist"}

def delete_result():
    event = {
        'id': 2,
        'title': "event 2",
        'quantity': 1,
        'done_at': datetime(2022, 2, 10, 9, 30, 0, 0),
        'due_at': None,
        'remind_at': None,
        'status': "done",
        'type_id': 1
    }

    return {"ok": Event(event)}