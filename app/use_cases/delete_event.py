from app.domains.event import Event

class DeleteEvent:
    def execute(repo, event_id: int) -> None:
        repo.delete(event_id)