from app.domains.event_type import EventType

class CreateEventType:
    def execute(repo, event_type: EventType) -> EventType:
        created_event_type = repo.create(event_type)

        return created_event_type