from typing import List
from app.domains.event import Event
from app.adapters.postgres_database.models import Event as EventModel

class EventRepo:
    def list(user: str) -> List[Event]:
        results = EventModel.query.filter_by(user=user)

        return [Event(row.serialize()) for row in results]

    def find(event_id: int) -> Event:
        event_model = EventModel.query.get(event_id)

        if (event_model):
            return Event(event_model.serialize())

        return None

    def create(event: Event) -> Event:
        event_model = EventModel(event)
        created_event = EventModel.create(event_model)

        event_model.id = created_event.id

        return Event(event_model.serialize())

    def update(event_id: int, event: Event) -> Event:
        event_to_update = EventModel.query.get(event_id)

        event_to_update.title = event.title
        event_to_update.quantity = event.quantity
        event_to_update.done_at = event.done_at
        event_to_update.due_at = event.due_at
        event_to_update.remind_at = event.remind_at
        event_to_update.status = event.status

        event_to_update = EventModel.update(event_to_update)

        return Event(event_to_update.serialize())

    def delete(event_id: int) -> None:
        event_to_delete = EventModel.query.get(event_id)
        event_to_delete = EventModel.delete(event_to_delete)

        return Event(event_to_delete.serialize())