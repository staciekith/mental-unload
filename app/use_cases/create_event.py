from app.domains.event import Event
from datetime import datetime, timedelta

class CreateEvent:
    def execute(event_repo, event_type_repo, data) -> Event:
        data['id'] = None
        data['done_at'] = datetime.now()
        data['status'] = 'done'
        data['due_at'] = None
        data['remind_at'] = None
        event = Event.from_dict(data)

        created_event = event_repo.create(event)

        type_id = created_event.type_id
        event_type = event_type_repo.find(type_id)

        quantity_by_unit = created_event.quantity / event_type.unit_quantity
        quantity_duration = quantity_by_unit * event_type.unit_duration # hours

        due_at = datetime.now() + timedelta(hours=quantity_duration)
        remind_at = due_at - timedelta(hours=event_type.reminder_delay)

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

        reminder = Event.from_dict(reminder)
        event_repo.create(reminder)

        return {"ok": created_event}