from typing import List
from app.domains.event import Event
from app.adapters.postgres_database.models import Event as EventModel

class EventRepo:
    def list(filters = None) -> List[Event]:
        results = EventModel.query.all()

        return [Event(**row.serialize()) for row in results]

    def create(event: Event) -> Event:
        event_model = EventModel(event)
        created_event = EventModel.create(event_model)

        event_model.id = created_event.id

        return Event(**event_model.serialize())

    def delete(event_id: int) -> None:
        event_to_delete = EventModel.query.get(event_id)

        if (event_to_delete):
            EventModel.delete(event_to_delete)