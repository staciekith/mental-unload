from app.domains.event_type import EventType

class DeleteEventType:
    def execute(repo, event_type_id: int) -> None:
        event_type = repo.find(event_type_id)

        if None == event_type:
            return {"error": "EventType with ID " + str(event_type_id) + " does not exist"}

        event_type = repo.delete(event_type_id)

        return {"ok": event_type}