from app.domains.event_type import EventType

def find_result():
    event_type = {
        'id': 1,
        'name': "event type 1",
        'description': "event type 1",
        'unit_label': "g",
        'unit_quantity': 170,
        'unit_duration': 12,
        'reminder_delay': 24,
        'user': 'user1'
    }

    return EventType(event_type)

def list_result():
    event_type = {
        'id': 1,
        'name': "event type 1",
        'description': "event type 1",
        'unit_label': "g",
        'unit_quantity': 170,
        'unit_duration': 12,
        'reminder_delay': 24,
        'user': 'user1'
    }

    event_type_3 = {
        'id': 3,
        'name': "event type 3",
        'description': "event type 3",
        'unit_label': "g",
        'unit_quantity': 170,
        'unit_duration': 12,
        'reminder_delay': 24,
        'user': 'user1'
    }

    event_type = EventType(event_type)
    event_type_3 = EventType(event_type_3)

    return [event_type, event_type_3]

def create_result():
    event_type = {
        'id': 4,
        'name': "event type created",
        'description': "event type created",
        'unit_label': "g",
        'unit_quantity': 170,
        'unit_duration': 12,
        'reminder_delay': 24,
        'user': 'user1'
    }

    return EventType(event_type)

def update_result():
    event_type = {
        'id': 1,
        'name': "event type updated",
        'description': "event type updated",
        'unit_label': "g",
        'unit_quantity': 170,
        'unit_duration': 12,
        'reminder_delay': 24,
        'user': 'user1'
    }

    return EventType(event_type)

def delete_result():
    event_type = {
        'id': 2,
        'name': "event type 2",
        'description': "event type 2",
        'unit_label': "g",
        'unit_quantity': 170,
        'unit_duration': 12,
        'reminder_delay': 24,
        'user': 'user2'
    }

    return EventType(event_type)