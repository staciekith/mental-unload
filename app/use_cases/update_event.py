from app.domains.event import Event

class UpdateEvent:
    def execute(repo, id, data) -> Event:
        event_to_update = repo.find(id)

        if None == event_to_update:
            return {"error": "Event with ID " + str(id) + " does not exist"}

        data = event_to_update.to_dict() | data
        event = Event.from_dict(data)

        updated_event = repo.update(id, event)

        return {"ok": updated_event}