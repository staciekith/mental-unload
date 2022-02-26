from app.domains.event_type import EventType

class CreateEventType:
    def execute(repo, data) -> EventType:
        data['id'] = None
        event_type = EventType(data)

        created_event_type = repo.create(event_type)

        return {"ok": created_event_type}