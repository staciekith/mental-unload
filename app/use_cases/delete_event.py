from app.domains.event import Event

class DeleteEvent:
    def execute(repo, event_id: int) -> None:
        event = repo.find(event_id)

        if None == event:
            return {"error": "Event with ID " + str(event_id) + " does not exist"}

        event = repo.delete(event_id)

        return {"ok": event}