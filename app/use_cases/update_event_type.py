from app.domains.event_type import EventType

class UpdateEventType:
    def execute(repo, id, data) -> EventType:
        event_type_to_update = repo.find(id)

        if None == event_type_to_update:
            return {"error": "EventType with ID " + str(id) + " does not exist"}

        data = event_type_to_update.to_dict() | data
        event_type = EventType.from_dict(data)

        updated_event_type = repo.update(id, event_type)

        return {"ok": updated_event_type}