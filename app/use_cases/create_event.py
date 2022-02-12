from app.domains.event import Event

class CreateEvent:
    def execute(repo, event: Event) -> Event:
        created_event = repo.create(event)

        return created_event