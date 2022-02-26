from app.domains.event import Event
from datetime import datetime, timedelta

class CreateEvent:
    def execute(event_repo, event_type_repo, data) -> Event:
        now = datetime.now()

        data['id'] = None
        data['done_at'] = datetime.now()
        data['status'] = 'done'
        data['due_at'] = None
        data['remind_at'] = None
        event = Event(data)

        created_event = event_repo.create(event)

        type_id = created_event.type_id
        event_type = event_type_repo.find(type_id)

        if (None == event_type):
            return {"error": "EventType with ID " + str(type_id) + " does not exist"}

        quantity_by_unit = created_event.quantity / event_type.unit_quantity
        quantity_duration = quantity_by_unit * event_type.unit_duration # hours

        due_at = now + timedelta(hours=quantity_duration)
        due_at = due_at.replace(hour=3, minute=0, second=0, microsecond=0)

        remind_at = due_at - timedelta(hours=event_type.reminder_delay)
        remind_at = remind_at.replace(hour=3, minute=0, second=0, microsecond=0)

        reminder = {
            "id": None,
            "title": "Reminder for " + event_type.name,
            "quantity": 0,
            "type_id": type_id,
            "done_at": None,
            "status": "pending",
            "due_at": due_at,
            "remind_at": remind_at
        }

        reminder = Event(reminder)
        event_repo.create(reminder)

        return {"ok": created_event}