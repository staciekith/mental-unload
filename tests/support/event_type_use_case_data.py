from app.domains.event_type import EventType

def list_result():
    event_type = {
        'id': 1,
        'name': "event type 1",
        'description': "event type 1",
        'unit_label': "g",
        'unit_quantity': 170,
        'unit_duration': 12,
        'reminder_delay': 24
    }

    event_type_2 = {
        'id': 2,
        'name': "event type 2",
        'description': "event type 2",
        'unit_label': "g",
        'unit_quantity': 170,
        'unit_duration': 12,
        'reminder_delay': 24
    }

    event_type = EventType(event_type)
    event_type_2 = EventType(event_type_2)

    return {"ok": [event_type, event_type_2]}

def create_result():
    event_type = {
        'id': 3,
        'name': "event type created",
        'description': "event type created",
        'unit_label': "g",
        'unit_quantity': 170,
        'unit_duration': 12,
        'reminder_delay': 24
    }

    return {"ok": EventType(event_type)}

def update_result():
    event_type = {
        'id': 1,
        'name': "event type updated",
        'description': "event type updated",
        'unit_label': "g",
        'unit_quantity': 170,
        'unit_duration': 12,
        'reminder_delay': 24
    }

    return {"ok": EventType(event_type)}

def not_found_result(id):
    return {"error": "EventType with ID " + str(id) + " does not exist"}

def delete_result():
    event_type = {
        'id': 2,
        'name': "event type 2",
        'description': "event type 2",
        'unit_label': "g",
        'unit_quantity': 170,
        'unit_duration': 12,
        'reminder_delay': 24
    }

    return {"ok": EventType(event_type)}
