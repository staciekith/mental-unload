from app.domains.event_type import EventType

class DeleteEventType:
    def execute(repo, event_type_id: int) -> None:
        repo.delete(event_type_id)