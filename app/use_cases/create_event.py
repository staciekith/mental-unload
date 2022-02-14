from app.domains.event import Event
from datetime import datetime

class CreateEvent:
    def execute(repo, data) -> Event:
        data['id'] = None
        data['done_at'] = datetime.now()
        data['status'] = 'done'
        data['due_at'] = None
        data['remind_at'] = None
        event = Event.from_dict(data)

        created_event = repo.create(event)

        # creer l'event pour le reminder

        return created_event