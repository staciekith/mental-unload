from app.domains.event_type import EventType

class UpdateEventType:
    def execute(repo, id, data) -> EventType:
        data['id'] = id
        event_type = EventType.from_dict(data)

        updated_event_type = repo.update(id, event_type)

        return updated_event_type